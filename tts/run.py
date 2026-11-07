"""Adım 5 — seslendirme (onay kapısından sonra).

normalized.json'daki her birim cümle cümle sentezlenir, aralara doğal duraklar eklenir, birimler
birleştirilip ses yüksekliği normalize edilir, kelime zamanları çıkarılır.
Çıktılar: audio/sentences/*.wav (önbellek), audio/voice.wav, timeline.json
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import numpy as np
import pyloudnorm as pyln
import soundfile as sf

from common.config import ROOT, episode_dir, read_json, settings, write_json
from normalizer.core import LEAD, TRAIL, Token, lookup, split_sentences
from review.run import require_approval
from tts.align import align_sentence
from tts.backends import BACKENDS


def _sentence_id(backend: str, voice: str, emotion: str, text: str) -> str:
    """Önbellek anahtarı: model/ses/metin değişirse yeniden üretilir."""
    return hashlib.sha1(f"{backend}|{voice}|{emotion}|{text}".encode()).hexdigest()[:12]


def _spoken(t: Token, field: str) -> str:
    """Modele gidecek kelime. Bulut modelleri orijinal yazımı okur, ancak harf harf okunan İngilizce kısaltmaları
    Türkçe harflerle okur ("PHP" → "pehepe"); sözlükte okunuşu olan kısaltmalarda fonetik yazım gönderilir."""
    if field == "tts":
        return t.tts
    core = re.split(r"['’]", t.display.lstrip(LEAD).rstrip(TRAIL))[0]
    if re.fullmatch(r"[A-Z0-9]{2,6}", core) and re.search(r"[A-Z]", core) and lookup(core) is not None:
        return t.tts
    return t.display


def voice_for_week(week: str, cfg: dict, backend: str) -> str:
    """Sabit ses verilmişse o; yoksa `voices` listesinden ISO hafta numarasına göre sıradaki (kadın/erkek dönüşümü).
    `voices` model adına göre sözlük de olabilir: {pocket_tr: [...], elevenlabs: [...], gemini: [...]}."""
    if cfg.get("voice"):
        return cfg["voice"]
    voices = cfg.get("voices") or [""]
    if isinstance(voices, dict):
        voices = voices.get(backend) or [""]
    return voices[int(week[6:]) % len(voices)]


def synthesize(job: dict, python: str) -> None:
    if python:
        # Yapılandırmadaki yol repo köküne göre olabilir; Windows'ta .exe uzantısı da gerekir
        exe = (ROOT / python) if not Path(python).is_absolute() else Path(python)
        if sys.platform == "win32" and exe.suffix != ".exe":
            exe = exe.with_suffix(".exe")
        job_path = ROOT / "episodes" / ".tts_job.json"
        job_path.write_text(json.dumps(job, ensure_ascii=False), encoding="utf-8")
        subprocess.run([str(exe), "-m", "tts.worker", str(job_path)], cwd=ROOT, check=True)
    else:
        from tts.worker import run_job

        run_job(job)


def run(week: str, force: bool = False, voice: str | None = None, backend: str | None = None) -> None:
    require_approval(week)
    ep = episode_dir(week)
    cfg = settings()["tts"]
    out_voice, out_timeline = ep / "audio" / "voice.wav", ep / "timeline.json"
    if out_timeline.exists() and out_voice.exists() and not force:
        print("[tts] voice.wav ve timeline.json var, atlanıyor (--force ile yenile)")
        return
    norm = read_json(ep / "normalized.json")
    backend = backend or cfg["backend"]
    cls = BACKENDS[backend]
    voice = voice or voice_for_week(week, cfg, backend)
    emotion = (cfg.get("voice_styles") or {}).get(voice) or cfg.get("emotion") or ""
    python = "" if cls.cloud else cfg.get("python") or ""
    print(f"[tts] {backend} / ses: {voice or 'varsayılan'}")
    sent_dir = ep / "audio" / "sentences"

    # 1) Sentez parçaları. chunk=unit: her birim (haber anlatımı, öğrenci notu...) tek parça üretilir;
    # cümleler arası tonlama model tarafından kurulur (cümle cümle üretim "okuyan robot" hissi veriyor).
    # chunk=sentence: her cümle ayrı üretilip araya sabit durak eklenir (uzun girdide zorlanan modeller için).
    # Bulut modelleri: bölüm, parçalara (giriş, her haber, kapanış) ayrılıp her biri tek istekte okunur; birimler
    # sonradan kelime zamanlarından ayrılır. Tüm bölümü tek istekte okutmak uzun metnin sonlarına doğru
    # robotikleşiyordu (2026-11-07 dinlemesi); ~6 istek ücretsiz günlük sınırın (10) içinde kalır.
    chunk = "episode" if cls.cloud else cfg.get("chunk", "unit")
    field = "display" if cls.reads_display else "tts"
    units = [(u, [Token(**{k: t[k] for k in ("display", "tts", "unknown")}) for t in u["tokens"]]) for u in norm["units"]]
    plan = []
    if chunk == "episode":
        for group in _sections(units):
            text = "\n\n".join(" ".join(_spoken(t, field) for t in toks if t.tts) for _, toks in group)
            plan.append({"unit": None, "group": group, "text": text,
                         "out": str(sent_dir / f"{_sentence_id(backend, voice, emotion, text)}.wav")})
    else:
        for u, tokens in units:
            for sent in (split_sentences(tokens) if chunk == "sentence" else [tokens]):
                text = " ".join(_spoken(t, field) for t in sent if t.tts).strip()
                if not text:
                    continue
                sid = _sentence_id(backend, voice, emotion, text)
                plan.append({"unit": u["id"], "tokens": sent, "text": text, "out": str(sent_dir / f"{sid}.wav")})
    synthesize({"backend": backend, "voice": voice, "emotion": emotion,
                "items": [{"text": p["text"], "out": p["out"]} for p in plan]}, python)

    # 2) Birleştirme + kelime zamanları
    if chunk == "episode":
        pieces, timeline_units, cursor = [], [], 0.0
        for p in plan:
            part, sr, part_units = _assemble_episode(p["out"], p["group"], field, cfg)
            for u in part_units:
                u["start"], u["end"] = round(u["start"] + cursor, 3), round(u["end"] + cursor, 3)
                for w in u["words"]:
                    w["start"], w["end"] = round(w["start"] + cursor, 3), round(w["end"] + cursor, 3)
            timeline_units += part_units
            gap = np.zeros(int(sr * 0.2), np.float32)  # parçaların kendi baş/son sessizliğine ek kısa es
            pieces += [part, gap]
            cursor += (len(part) + len(gap)) / sr
        audio = np.concatenate(pieces)
    else:
        audio, sr, timeline_units = _assemble_pieces(plan, units, field, cfg)

    # Konuşma izi hedefin 2 dB altına çekilir; müzikle karışımdan sonra final -14 LUFS'a ayarlanır
    meter = pyln.Meter(sr)
    audio = pyln.normalize.loudness(audio, meter.integrated_loudness(audio), cfg["target_lufs"] - 2)
    audio = np.clip(audio, -0.98, 0.98)
    out_voice.parent.mkdir(parents=True, exist_ok=True)
    sf.write(out_voice, audio, sr)
    write_json(out_timeline, {"week": week, "backend": backend, "voice": voice, "sample_rate": sr,
                              "duration": round(len(audio) / sr, 3), "units": timeline_units,
                              "license_note": cls.license_note, "caption_credit": cls.caption_credit})
    print(f"[tts] {len(plan)} parça, toplam {len(audio) / sr:.1f} sn → audio/voice.wav, timeline.json")


def _quiet_cut(wav: np.ndarray, sr: int, center: float, reach: float = 0.6) -> tuple[float, float]:
    """Birim sınırı için kesim noktası: center'a en yakın gerçek sessizlik bloğunun (≥60 ms, -45 dBFS altı) ortası
    ve bloğun süresi. Whisper'ın kelime zamanlarına güvenilmez (bitişler erken; "Dört"/"4" gibi eşleşmeyen kelimelerde
    zaman tahmindir), bu yüzden sınır sesin kendisinden bulunur. Blok yoksa aralıktaki en sessiz 20 ms."""
    hop = int(sr * 0.01)
    i0, i1 = max(0, int((center - reach) * sr)), min(len(wav), int((center + reach) * sr))
    frames = np.arange(i0, max(i0 + 1, i1 - hop), hop)
    db = np.array([10 * np.log10(np.mean(wav[f:f + hop] ** 2) + 1e-12) for f in frames])
    quiet = np.concatenate([[False], db < -45, [False]])
    edges = np.diff(quiet.astype(int))
    runs = [(s, e) for s, e in zip(np.where(edges == 1)[0], np.where(edges == -1)[0]) if e - s >= 6]
    if runs:
        s, e = min(runs, key=lambda r: abs((frames[r[0]] + frames[r[1] - 1] + hop) / 2 / sr - center))
        return float(frames[s] + frames[e - 1] + hop) / 2 / sr, float(e - s) * hop / sr
    k = int(np.argmin(db))
    return float(frames[k] + hop / 2) / sr, 0.0


def _sections(units: list) -> list[list]:
    """Birimleri okuma parçalarına böler: haber öncesi (kanca, teaser), her haber (köprü+anlatım+not), kapanış."""
    groups: dict = {}
    seen_segment = False
    for u, toks in units:
        seen_segment = seen_segment or bool(u["segment"])
        key = u["segment"] or ("son" if seen_segment else "giris")
        groups.setdefault(key, []).append((u, toks))
    return list(groups.values())


def _token_words(tokens: list[Token], field: str) -> tuple[list[str], list[int]]:
    """Hizalanacak kelimeler ve her kelimenin ait olduğu token sırası."""
    words, owner = [], []
    for ti, t in enumerate(tokens):
        for w in (_spoken(t, field) if t.tts else "").split():
            words.append(w)
            owner.append(ti)
    return words, owner


def _display_words(tokens: list[Token], owner: list[int], times: list, offset: float) -> list[dict]:
    """Kelime zamanlarını display token'larına taşır (altyazı orijinal yazımı gösterir)."""
    out: list[dict] = []
    for ti, t in enumerate(tokens):
        spans = [times[j] for j, o in enumerate(owner) if o == ti]
        if spans:
            out.append({"text": t.display, "start": round(offset + spans[0][0], 3), "end": round(offset + spans[-1][1], 3)})
        elif out:  # tts'i boş token (ör. tek başına noktalama) bir önceki kelimeye eklenir
            out[-1]["text"] += " " + t.display
    return out


def _unit_gap(u: dict, cfg: dict) -> float:
    return 0.15 if u["kind"] == "bridge" else cfg["unit_pause_ms"] / 1000  # köprüden habere kısa es


def _assemble_pieces(plan: list[dict], units: list, field: str, cfg: dict):
    sr = sf.info(plan[0]["out"]).samplerate
    sent_gap = np.zeros(int(sr * cfg["sentence_pause_ms"] / 1000), np.float32)
    pieces, out_units, cursor = [], [], 0.0
    for u, _ in units:
        u_plan = [p for p in plan if p["unit"] == u["id"]]
        u_start, words = cursor, []
        for k, p in enumerate(u_plan):
            wav, wsr = sf.read(p["out"], dtype="float32")
            assert wsr == sr, "tüm cümleler aynı örnekleme hızında olmalı"
            tts_words, owner = _token_words(p["tokens"], field)
            words += _display_words(p["tokens"], owner, align_sentence(wav, sr, tts_words), cursor)
            pieces.append(wav)
            cursor += len(wav) / sr
            if k < len(u_plan) - 1:
                pieces.append(sent_gap)
                cursor += len(sent_gap) / sr
        out_units.append({"id": u["id"], "kind": u["kind"], "segment": u["segment"],
                          "start": round(u_start, 3), "end": round(cursor, 3), "words": words})
        gap = np.zeros(int(sr * _unit_gap(u, cfg)), np.float32)
        pieces.append(gap)
        cursor += len(gap) / sr
    return np.concatenate(pieces), sr, out_units


def _assemble_episode(path: str, units: list, field: str, cfg: dict):
    """Tek parça bölüm sesi: tüm metin bir kez hizalanır, birimler aradaki sessizliğin ortasından kesilir;
    doğal es birim arası durağından kısaysa sessizlik eklenir (haber geçişleri nefes alsın)."""
    wav, sr = sf.read(path, dtype="float32")
    if wav.ndim > 1:
        wav = wav.mean(axis=1)
    per_unit = [_token_words(toks, field) for _, toks in units]
    times = align_sentence(wav, sr, [w for words, _ in per_unit for w in words])
    spans, k = [], 0
    for words, _ in per_unit:
        spans.append(times[k:k + len(words)])
        k += len(words)
    bounds = [(sp[0][0], sp[-1][1]) if sp else None for sp in spans]
    pieces, out_units, cursor, t_prev = [], [], 0.0, 0.0
    fade = int(sr * 0.006)
    for i, (u, toks) in enumerate(units):
        nxt = next((b for b in bounds[i + 1:] if b), None)
        # Whisper'ın kelime bitişi çoğu zaman erken: aradaki ortalamada kesmek son sesi ("ücretsi|z") bölüyordu.
        # Kesim, iki kelime arasındaki gerçekten en sessiz ana yapılır.
        cut, natural = len(wav) / sr, 0.0
        if nxt is not None and bounds[i] is not None:
            cut, natural = _quiet_cut(wav, sr, (bounds[i][1] + nxt[0]) / 2)
        local = [(s - t_prev, e - t_prev) for s, e in spans[i]]
        u_words = _display_words(toks, per_unit[i][1], local, cursor)
        if u_words:
            out_units.append({"id": u["id"], "kind": u["kind"], "segment": u["segment"],
                              "start": u_words[0]["start"], "end": u_words[-1]["end"], "words": u_words})
        seg = wav[int(t_prev * sr):int(cut * sr)].copy()
        if len(seg) > 2 * fade:  # kesim yerinde tık olmasın: 6 ms giriş/çıkış
            seg[:fade] *= np.linspace(0, 1, fade, dtype=np.float32)
            seg[-fade:] *= np.linspace(1, 0, fade, dtype=np.float32)
        pieces.append(seg)
        cursor += len(seg) / sr
        if nxt is not None and bounds[i] is not None and (extra := _unit_gap(u, cfg) - natural) > 0:
            pieces.append(np.zeros(int(sr * extra), np.float32))
            cursor += int(sr * extra) / sr
        t_prev = cut
    return np.concatenate(pieces), sr, out_units


if __name__ == "__main__":
    run(sys.argv[1])
