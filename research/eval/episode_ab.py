"""Bir bölümün metnini farklı TTS ayarlarıyla üretip, haber bazında kör dinleme sayfası kurar.

Kısa test cümleleri yerine gerçek bölüm metniyle (uzun paragraflar, tonlama) karşılaştırma yapar.
Kullanım: python research/eval/episode_ab.py 2026-W44
Çıktı: research/episode_ab/<hafta>/ (wav'lar), research/episode_ab/<hafta>/blind.html + ab_*.mp3,
       anahtar: research/results/episode_ab_<hafta>_key.json (dinleyicilerle paylaşmayın)
"""
from __future__ import annotations

import json
import secrets
import subprocess
import sys
from pathlib import Path

import numpy as np
import soundfile as sf

ROOT = Path(__file__).resolve().parents[2]
VENVS = ROOT / "research" / ".venvs"


def py(venv: str | None) -> str:
    return str((VENVS / venv / "Scripts" / "python.exe") if venv else (ROOT / ".venv" / "Scripts" / "python.exe"))


def main(week: str, only: list[str] | None = None) -> None:
    ep = ROOT / "episodes" / week
    out = ROOT / "research" / "episode_ab" / week
    out.mkdir(parents=True, exist_ok=True)
    units = json.loads((ep / "normalized.json").read_text(encoding="utf-8"))["units"]
    script = json.loads((ep / "script.json").read_text(encoding="utf-8"))["script"]
    design_f = out / "omnivoice_f" / "s1_narration.wav"  # Chatterbox referansı olarak da kullanılır

    variants = [
        ("pocket_unit", "pocket_tr", "female_1", None),
        ("omnivoice_f", "omnivoice", "design:female, young adult, moderate pitch", "omnivoice"),
        ("omnivoice_m", "omnivoice", "design:male, young adult, moderate pitch", "omnivoice"),
        ("chatterbox_ref", "chatterbox_v3", str(design_f), "chatterbox"),
    ]
    for name, backend, voice, venv in variants:
        if only and name not in only:
            continue
        job = {"backend": backend, "voice": voice, "emotion": "",
               "items": [{"text": u["tts_text"], "out": str(out / name / f"{u['id']}.wav")} for u in units]}
        job_path = out / f"{name}.job.json"
        job_path.write_text(json.dumps(job, ensure_ascii=False), encoding="utf-8")
        print(f"== {name}", flush=True)
        subprocess.run([py(venv), "-m", "tts.worker", str(job_path)], cwd=ROOT, check=True)

    # Mevcut videodaki ses (Pocket, cümle cümle) birim sınırlarından kesilir
    tl = json.loads((ep / "timeline.json").read_text(encoding="utf-8"))
    voice, sr = sf.read(ep / "audio" / "voice.wav", dtype="float32")
    (out / "pocket_sentence").mkdir(exist_ok=True)
    for u in tl["units"]:
        sf.write(out / "pocket_sentence" / f"{u['id']}.wav", voice[int(u["start"] * sr):int(u["end"] * sr)], sr)

    # Haber başına klip: anlatım + kısa es + öğrenci notu; -16 LUFS'a eşitlenir
    # Kör teste girecek sesler: verilmişse onlar, yoksa tüm birimleri hazır olan her klasör
    ready = [d.name for d in sorted(out.iterdir())
             if d.is_dir() and all((d / f"{u['id']}.wav").exists() for u in units)]
    names = [n for n in (only or ready) if n in ready]
    for old in out.glob("bt_*.mp3"):
        old.unlink()
    key, items = {}, []
    segments = [("hook", "Kanca + kapanış", ["hook", "outro"])] + [
        (f"s{i}", s["headline"], [f"s{i}_narration", f"s{i}_take"]) for i, s in enumerate(script["segments"], 1)]
    for sid, title, parts in segments:
        clips = []
        for n in names:
            wavs = []
            for p in parts:
                w, wsr = sf.read(out / n / f"{p}.wav", dtype="float32")
                if w.ndim > 1:
                    w = w.mean(axis=1)
                wavs += [w, np.zeros(int(wsr * 0.45), np.float32)]
            tmp = out / n / f"_{sid}.wav"
            sf.write(tmp, np.concatenate(wavs), wsr)
            cid = secrets.token_hex(4)
            subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(tmp), "-af", "loudnorm=I=-16:TP=-1.5:LRA=11",
                            "-ar", "44100", "-ac", "1", "-b:a", "128k", str(out / f"bt_{cid}.mp3")], check=True)
            key[cid] = {"model": n, "sentence": sid}
            clips.append(cid)
        text = " / ".join(next(u["display_text"] for u in units if u["id"] == p) for p in parts)
        items.append({"id": sid, "text": f"{title}: {text}", "clips": clips})

    (ROOT / "research" / "results").mkdir(exist_ok=True)
    (ROOT / "research" / "results" / f"episode_ab_{week}_key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
    tpl = (ROOT / "research" / "eval" / "blind_test_template.html").read_text(encoding="utf-8")
    html = tpl.replace("/*__DATA__*/[]", json.dumps(items, ensure_ascii=False)).replace("gdg-tts-blind-v1", f"gdg-tts-ab-{week}")
    (out / "blind.html").write_text(html, encoding="utf-8")
    print(f"{len(key)} klip, {len(items)} bölüm → {out / 'blind.html'}")


if __name__ == "__main__":
    # python research/eval/episode_ab.py 2026-W44 [ses1 ses2 ...]
    main(sys.argv[1], sys.argv[2:] or None)
