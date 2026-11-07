"""Test cümlelerini bir modelle sentezler, RTF ve tepe VRAM'i ölçer.

Kullanım (ilgili modelin sanal ortamında, repo kökünden):
    python research/eval/synth.py --model freya
    python research/eval/synth.py --model chatterbox_v3 --ref research/reference/ref.wav

Çıktı: research/audio/<model>/<id>_<raw|phonetic>.wav ve research/results/synth_<model>.json
Var olan wav'lar atlanır (--force ile yeniden üretilir), böylece yarıda kalan çalışma devam ettirilebilir.
"""
from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

import numpy as np
import soundfile as sf

sys.path.insert(0, str(Path(__file__).parent))
from backends import BACKENDS  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "research"


def peak_vram_mb() -> float | None:
    try:
        import torch

        if torch.cuda.is_available():
            return torch.cuda.max_memory_allocated() / 2**20
    except ImportError:
        pass
    return None


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True, choices=sorted(BACKENDS))
    ap.add_argument("--ref", help="klonlama için referans wav")
    ap.add_argument("--ref-text", help="referans kaydın metni (VoxCPM 'ultimate cloning' için)")
    ap.add_argument("--variants", nargs="+", default=["raw", "phonetic"])
    ap.add_argument("--force", action="store_true")
    args = ap.parse_args()

    sentences = json.loads((RESEARCH / "test_sentences.json").read_text(encoding="utf-8"))["sentences"]
    out_dir = RESEARCH / "audio" / args.model
    out_dir.mkdir(parents=True, exist_ok=True)

    backend = BACKENDS[args.model]()
    t0 = time.perf_counter()
    backend.load(args.ref if backend.supports_clone else None, args.ref_text)
    load_s = time.perf_counter() - t0
    backend.synth("Isınma cümlesi.")  # ilk çağrıdaki derleme/önbellek süresi RTF'yi bozmasın

    rows = []
    for s in sentences:
        for v in args.variants:
            path = out_dir / f"{s['id']}_{v}.wav"
            if path.exists() and not args.force:
                continue
            t = time.perf_counter()
            wav, sr = backend.synth(s[v])
            gen_s = time.perf_counter() - t
            sf.write(path, wav, sr)
            dur = len(wav) / sr
            rows.append({"id": s["id"], "variant": v, "gen_s": round(gen_s, 3), "audio_s": round(dur, 3),
                         "rtf": round(gen_s / dur, 4) if dur else None})
            print(f"{path.name}: {dur:.2f}s ses, RTF {gen_s / max(dur, 1e-6):.3f}", flush=True)

    res_dir = RESEARCH / "results"
    res_dir.mkdir(exist_ok=True)
    rtfs = [r["rtf"] for r in rows if r["rtf"]]
    report = {
        "model": args.model,
        "reference": args.ref if backend.supports_clone else None,
        "load_s": round(load_s, 1),
        "peak_vram_mb": peak_vram_mb(),
        "mean_rtf": round(float(np.mean(rtfs)), 4) if rtfs else None,
        "items": rows,
    }
    (res_dir / f"synth_{args.model}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: v for k, v in report.items() if k != "items"}, ensure_ascii=False))


if __name__ == "__main__":
    main()
