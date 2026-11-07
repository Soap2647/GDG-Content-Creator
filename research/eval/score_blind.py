"""Kör test puanlarını toplar: research/results/blind_ratings/*.json + blind_key.json -> model sıralaması.

Ham ortalama MOS'un yanında dinleyici bazında z-skoru ortalaması da verilir
(sert ve cömert puanlayanların etkisini dengeler).
Kullanım: python research/eval/score_blind.py
"""
from __future__ import annotations

import json
import statistics
from collections import defaultdict
from pathlib import Path

RESULTS = Path(__file__).resolve().parents[2] / "research" / "results"


def main() -> None:
    key = json.loads((RESULTS / "blind_key.json").read_text(encoding="utf-8"))
    files = sorted((RESULTS / "blind_ratings").glob("*.json"))
    raw, z = defaultdict(list), defaultdict(list)
    for f in files:
        data = json.loads(f.read_text(encoding="utf-8"))
        scores = {cid: v for cid, v in data["ratings"].items() if cid in key}
        if not scores:
            continue
        mu = statistics.mean(scores.values())
        sd = statistics.pstdev(scores.values()) or 1.0
        for cid, v in scores.items():
            raw[key[cid]["model"]].append(v)
            z[key[cid]["model"]].append((v - mu) / sd)

    summary = sorted(
        ({"model": m, "mos": round(statistics.mean(v), 3), "n": len(v),
          "ci95": round(1.96 * statistics.stdev(v) / len(v) ** 0.5, 3) if len(v) > 1 else None,
          "z_mean": round(statistics.mean(z[m]), 3)} for m, v in raw.items()),
        key=lambda r: -r["mos"],
    )
    (RESULTS / "blind_summary.json").write_text(json.dumps({"raters": len(files), "models": summary}, indent=2), encoding="utf-8")
    print(f"{len(files)} dinleyici")
    for r in summary:
        print(f"{r['model']:<16} MOS {r['mos']:.2f} ±{r['ci95'] or 0:.2f}  z {r['z_mean']:+.2f}  (n={r['n']})")


if __name__ == "__main__":
    main()
