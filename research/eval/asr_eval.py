"""Üretilen sesleri Whisper large-v3 ile yazıya döker, WER/CER ve terim isabetini hesaplar.

Kullanım (eval ortamında, repo kökünden):
    python research/eval/asr_eval.py

faster-whisper (CTranslate2) ile large-v3 ağırlıkları kullanılır: aynı model, ~3 GB VRAM.
Transkriptler research/results/asr_cache.json'da tutulur; yalnızca yeni wav'lar yazıya dökülür.
Çıktılar: research/results/metrics.csv (cümle bazında), research/results/summary.json (model x varyant).
"""
from __future__ import annotations

import csv
import json
import sys
from collections import defaultdict
from pathlib import Path

import jiwer

sys.path.insert(0, str(Path(__file__).parent))
from textnorm import normalize  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "research"
RESULTS = RESEARCH / "results"


def transcribe_all(wavs: list[Path], cache: dict) -> None:
    todo = [w for w in wavs if str(w.relative_to(RESEARCH)) not in cache]
    if not todo:
        return
    import os
    import sysconfig

    # Windows: pip'ten gelen cuBLAS/cuDNN DLL'leri PATH'te değil; CTranslate2 bulabilsin diye ekleniyor
    for bin_dir in Path(sysconfig.get_paths()["purelib"], "nvidia").glob("*/bin"):
        os.add_dll_directory(str(bin_dir))
        os.environ["PATH"] = str(bin_dir) + os.pathsep + os.environ["PATH"]
    from faster_whisper import WhisperModel

    import numpy as np
    import subprocess

    model = WhisperModel("large-v3", device="cuda", compute_type="float16")
    for w in todo:
        # PyAV sürüm uyumsuzluğundan kaçınmak için 16 kHz mono'ya ffmpeg ile çözülür
        pcm = subprocess.run(["ffmpeg", "-loglevel", "error", "-i", str(w), "-f", "f32le", "-ac", "1", "-ar", "16000", "-"],
                             capture_output=True, check=True).stdout
        segments, _ = model.transcribe(np.frombuffer(pcm, np.float32), language="tr", beam_size=5, vad_filter=False)
        cache[str(w.relative_to(RESEARCH))] = " ".join(seg.text.strip() for seg in segments)
        print(w.relative_to(RESEARCH), "->", cache[str(w.relative_to(RESEARCH))], flush=True)


def main() -> None:
    RESULTS.mkdir(exist_ok=True)
    sentences = {s["id"]: s for s in json.loads((RESEARCH / "test_sentences.json").read_text(encoding="utf-8"))["sentences"]}
    wavs = sorted((RESEARCH / "audio").glob("*/*.wav"))
    cache_path = RESULTS / "asr_cache.json"
    cache = json.loads(cache_path.read_text(encoding="utf-8")) if cache_path.exists() else {}
    try:
        transcribe_all(wavs, cache)
    finally:
        cache_path.write_text(json.dumps(cache, ensure_ascii=False, indent=1), encoding="utf-8")

    rows = []
    for w in wavs:
        model, (sid, variant) = w.parent.name, w.stem.split("_", 1)
        s = sentences[sid]
        ref, hyp = normalize(s["raw"]), normalize(cache[str(w.relative_to(RESEARCH))])
        hyp_tokens = set(hyp.split())
        terms = [normalize(t) for t in s["terms"]]
        hits = sum(any(tok.startswith(t) for tok in hyp_tokens) for t in terms)
        rows.append({
            "model": model, "id": sid, "variant": variant,
            "wer": round(jiwer.wer(ref, hyp), 4), "cer": round(jiwer.cer(ref, hyp), 4),
            "term_hits": hits, "term_total": len(terms),
            "tags": "|".join(s["tags"]), "ref_norm": ref, "hyp_norm": hyp,
        })

    with open(RESULTS / "metrics.csv", "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)

    groups = defaultdict(list)
    for r in rows:
        groups[(r["model"], r["variant"])].append(r)
    summary = []
    for (model, variant), rs in sorted(groups.items()):
        synth_path = RESULTS / f"synth_{model}.json"
        synth = json.loads(synth_path.read_text(encoding="utf-8")) if synth_path.exists() else {}
        total_terms = sum(r["term_total"] for r in rs)
        summary.append({
            "model": model, "variant": variant, "n": len(rs),
            # Ortalama değil, toplam hata / toplam kelime: kısa cümleler sonucu şişirmesin
            "wer": round(jiwer.wer([r["ref_norm"] for r in rs], [r["hyp_norm"] for r in rs]), 4),
            "cer": round(jiwer.cer([r["ref_norm"] for r in rs], [r["hyp_norm"] for r in rs]), 4),
            "term_acc": round(sum(r["term_hits"] for r in rs) / total_terms, 4) if total_terms else None,
            "mean_rtf": synth.get("mean_rtf"), "peak_vram_mb": synth.get("peak_vram_mb"),
        })
    (RESULTS / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n{'model':<16}{'varyant':<10}{'WER':>7}{'CER':>7}{'terim':>7}{'RTF':>8}{'VRAM MB':>9}")
    for s in summary:
        print(f"{s['model']:<16}{s['variant']:<10}{s['wer']:>7.3f}{s['cer']:>7.3f}"
              f"{(s['term_acc'] or 0):>7.2f}{(s['mean_rtf'] or 0):>8.3f}{(s['peak_vram_mb'] or 0):>9.0f}")


if __name__ == "__main__":
    main()
