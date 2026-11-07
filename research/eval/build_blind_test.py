"""Kör dinleme sayfasını üretir: research/blind_test.html + yanında research/bt_*.mp3 dosyaları.

Her model için tek varyant (varsayılan: summary.json'da CER'i düşük olan) seçilir.
Tüm klipler -16 LUFS'a eşitlenir ki ses yüksekliği farkı puanları etkilemesin.
Klip adları rastgele; hangi klibin hangi modele ait olduğu yalnızca
research/results/blind_key.json'da durur (bu dosyayı dinleyicilerle paylaşma).

Kullanım: python research/eval/build_blind_test.py [--variant best|raw|phonetic] [--models a b ...]
"""
from __future__ import annotations

import argparse
import json
import secrets
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RESEARCH = ROOT / "research"
RESULTS = RESEARCH / "results"
TEMPLATE = Path(__file__).parent / "blind_test_template.html"


def pick_variants(models: list[str], mode: str) -> dict[str, str]:
    if mode != "best":
        return {m: mode for m in models}
    summary = json.loads((RESULTS / "summary.json").read_text(encoding="utf-8"))
    best = {}
    for m in models:
        rows = [r for r in summary if r["model"] == m]
        best[m] = min(rows, key=lambda r: r["cer"])["variant"] if rows else "phonetic"
    return best


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--variant", default="best")
    ap.add_argument("--models", nargs="*")
    args = ap.parse_args()

    models = args.models or sorted(p.name for p in (RESEARCH / "audio").iterdir() if p.is_dir())
    variants = pick_variants(models, args.variant)
    sentences = json.loads((RESEARCH / "test_sentences.json").read_text(encoding="utf-8"))["sentences"]

    for old in RESEARCH.glob("bt_*.mp3"):
        old.unlink()
    key, items = {}, []
    for s in sentences:
        clips = []
        for m in models:
            src = RESEARCH / "audio" / m / f"{s['id']}_{variants[m]}.wav"
            if not src.exists():
                continue
            cid = secrets.token_hex(4)
            subprocess.run(
                ["ffmpeg", "-loglevel", "error", "-y", "-i", str(src),
                 "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", "44100", "-ac", "1", "-b:a", "128k",
                 str(RESEARCH / f"bt_{cid}.mp3")],
                check=True,
            )
            key[cid] = {"model": m, "variant": variants[m], "sentence": s["id"]}
            clips.append(cid)
        items.append({"id": s["id"], "text": s["raw"], "clips": clips})

    RESULTS.mkdir(exist_ok=True)
    (RESULTS / "blind_key.json").write_text(json.dumps(key, indent=2), encoding="utf-8")
    html = TEMPLATE.read_text(encoding="utf-8").replace("/*__DATA__*/[]", json.dumps(items, ensure_ascii=False))
    (RESEARCH / "blind_test.html").write_text(html, encoding="utf-8")
    print(f"{len(key)} klip, {len(items)} cümle -> research/blind_test.html")
    print("Seçilen varyantlar:", variants)


if __name__ == "__main__":
    main()
