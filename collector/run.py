"""Adım 1 — haber toplama: çek → zaman penceresi → tekrarları birleştir → Claude ile öğrenci ilgisi puanı.

Ara çıktılar: raw_items.json (puanlamadan önce), candidates.json (puanlı, sıralı).
Puanlama başarısız olsa bile ham liste diskte kalır; `--force` olmadan ham çekim tekrarlanmaz.
"""
from __future__ import annotations

import datetime as dt
from typing import Literal

import yaml
from pydantic import BaseModel, Field
from rapidfuzz import fuzz

from collector.fetch import canonical_url, fetch_all
from common.config import CONFIG_DIR, episode_dir, read_json, settings, week_window, write_json
from common.llm import ask


def dedupe(items: list[dict], threshold: int) -> list[dict]:
    """Aynı URL veya çok benzer başlık → tek kayıt; diğer kaynaklar `also_reported_by`'a eklenir."""
    items = sorted(items, key=lambda i: -i["weight"])
    kept: list[dict] = []
    for it in items:
        cu = canonical_url(it["url"])
        dup = next(
            (k for k in kept
             if canonical_url(k["url"]) == cu
             or fuzz.token_set_ratio(k["title"].lower(), it["title"].lower()) >= threshold),
            None,
        )
        if dup:
            dup.setdefault("also_reported_by", []).append({"source": it["source"], "url": it["url"]})
        else:
            kept.append(dict(it))
    return kept


class Score(BaseModel):
    id: int
    score: int = Field(description="0-10: Türk üniversite öğrencileri (özellikle bilgisayar/mühendislik) için ilgi ve fayda")
    category: Literal["ai", "developer", "mobile", "web", "hardware", "security", "career", "opportunity", "science", "other"]
    reason: str = Field(description="Puan gerekçesi, Türkçe, en fazla 15 kelime")
    summary_tr: str = Field(description="Haberin Türkçe özeti, en fazla 30 kelime, yalnızca verilen bilgilere dayan")


class ScoreList(BaseModel):
    scores: list[Score]


SCORE_SYSTEM = """Sen GDG on Campus Kastamonu'nun haftalık teknoloji gündemi videosu için haber editörüsün.
Hedef kitle: Türkiye'deki üniversite öğrencileri (çoğu bilgisayar/yazılım/mühendislik).
Her aday haberi 0-10 arası puanla:
- 8-10: Öğrencinin bu hafta bir şey yapabileceği haberler (başvuru, ücretsiz araç/kota, yarışma, staj, açık kaynak sürüm) veya sektörü belirgin değiştiren büyük duyurular.
- 5-7: Geliştiricilerin bilmesi gereken önemli ürün/teknoloji haberleri.
- 0-4: Tüketici ürün incelemeleri, kampanyalar, magazin, yatırım/borsa, tekrar eden veya belirsiz haberler.
Google/Android/Chrome/Firebase/Gemini geliştirici haberlerine (GDG kitlesi) hafif öncelik ver, ama önemli olmayanı şişirme.
Özetlerde yalnızca başlık ve özetteki bilgileri kullan; tahmin ekleme. Her aday için tam bir kayıt döndür."""


def score(items: list[dict], task) -> list[dict]:
    lines = [
        f"[{i}] ({it['source']}, {it['lang']}, {(it['date'] or 'tarih yok')[:10]}) {it['title']} — {it['summary'][:280]}"
        for i, it in enumerate(items)
    ]
    result = ask(SCORE_SYSTEM, "Aday haberler:\n\n" + "\n".join(lines), ScoreList, task=task, effort="medium", max_tokens=48000)
    by_id = {s.id: s for s in result.scores}
    out = []
    for i, it in enumerate(items):
        s = by_id.get(i)
        if not s:
            continue
        out.append({**it, "id": f"c{i:03d}", "score": s.score, "category": s.category,
                    "score_reason": s.reason, "summary_tr": s.summary_tr,
                    "rank_score": round(s.score * it["weight"], 2)})
    return sorted(out, key=lambda c: -c["rank_score"])


def run(week: str, force: bool = False) -> None:
    ep = episode_dir(week)
    cfg = settings()["collector"]
    raw_path, out_path = ep / "raw_items.json", ep / "candidates.json"
    if out_path.exists() and not force:
        print(f"[collect] {out_path.relative_to(ep.parent.parent)} var, atlanıyor (--force ile yenile)")
        return

    if raw_path.exists() and not force:
        raw = read_json(raw_path)
    else:
        sources = yaml.safe_load((CONFIG_DIR / "sources.yaml").read_text(encoding="utf-8"))["sources"]
        items, errors = fetch_all(sources, cfg["max_per_source"])
        start, end = week_window(week, cfg["days"])
        in_window = [
            it for it in items
            if it["title"] and it["url"]
            and (it["date"] is None or start <= dt.datetime.fromisoformat(it["date"]) <= end)
        ]
        merged = dedupe(in_window, cfg["dedupe_threshold"])
        raw = {"week": week, "window": [start.isoformat(), end.isoformat()], "fetched": len(items),
               "in_window": len(in_window), "errors": errors, "items": merged}
        write_json(raw_path, raw)
        print(f"[collect] {len(items)} haber çekildi, {len(in_window)} pencere içinde, "
              f"{len(merged)} tekrar sonrası; {len(errors)} kaynak hatası")
        for e in errors:
            print("  !", e)

    candidates = score(raw["items"], ep / "llm" / "score")
    write_json(out_path, {"week": week, "window": raw["window"], "candidates": candidates})
    print(f"[collect] {len(candidates)} aday puanlandı → candidates.json; ilk 5:")
    for c in candidates[:5]:
        print(f"  {c['rank_score']:>5}  {c['title'][:80]}  ({c['source']})")
