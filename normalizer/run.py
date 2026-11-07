"""Adım 3 — normalizasyon: script.json'daki seslendirilecek her metin için display_text + tts_text + token eşlemesi.

Çıktı: normalized.json. Seslendirme birimleri (unit) sırası videodaki sıradır:
hook, teaser, s1_bridge, s1_narration, s1_take, s2_bridge, ..., question, outro. Boş metinler birim olmaz.
"""
from __future__ import annotations

from common.config import episode_dir, read_json, write_json
from normalizer.core import dictionary, normalize


def units_from_script(script: dict) -> list[dict]:
    units = [{"id": "hook", "kind": "hook", "segment": None, "text": script["hook"]},
             {"id": "teaser", "kind": "teaser", "segment": None, "text": script.get("teaser", "")}]
    for i, seg in enumerate(script["segments"], 1):
        units.append({"id": f"s{i}_bridge", "kind": "bridge", "segment": i, "text": seg.get("bridge", "")})
        units.append({"id": f"s{i}_narration", "kind": "narration", "segment": i, "text": seg["narration"]})
        units.append({"id": f"s{i}_take", "kind": "take", "segment": i, "text": seg["student_take"]})
    units.append({"id": "question", "kind": "question", "segment": None, "text": script.get("question", "")})
    units.append({"id": "outro", "kind": "outro", "segment": None, "text": script["outro"]})
    return [u for u in units if u["text"].strip()]


def run(week: str, force: bool = False) -> None:
    ep = episode_dir(week)
    out = ep / "normalized.json"
    script_file = read_json(ep / "script.json")
    if out.exists() and not force and read_json(out).get("script_word_count") == script_file["word_count"]:
        print("[normalize] normalized.json güncel, atlanıyor")
        return
    dictionary.cache_clear()  # sözlük yeni güncellenmiş olabilir
    units = []
    for u in units_from_script(script_file["script"]):
        n = normalize(u["text"])
        units.append({**{k: v for k, v in u.items() if k != "text"}, **n.to_dict()})
    unknown = sorted({t for u in units for t in u["unknown_terms"]})
    write_json(out, {"week": week, "script_word_count": script_file["word_count"], "units": units,
                     "unknown_terms": unknown})
    print(f"[normalize] {len(units)} birim; sözlükte olmayan {len(unknown)} terim: {', '.join(unknown) or '-'}")
