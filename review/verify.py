"""Adım 4a — doğrulama: her iddia kaynak metniyle karşılaştırılır (ikinci Claude çağrısı) + rakam taraması.

Çıktı: verification.json
"""
from __future__ import annotations

import re
from typing import Literal

from pydantic import BaseModel, Field

from common.config import episode_dir, file_hash, read_json, url_key, write_json
from common.llm import ask
from writer.run import source_text

Verdict = Literal["supported", "partial", "unsupported", "not_found"]


class ClaimCheck(BaseModel):
    segment: int
    claim_index: int
    verdict: Verdict = Field(description="supported: kaynak açıkça söylüyor; partial: kısmen/farklı ifade; unsupported: kaynakla çelişiyor; not_found: kaynakta yok")
    evidence: str = Field(description="Kaynaktan birebir alıntı, en fazla 30 kelime; yoksa boş")
    note: str = Field(description="Kısa açıklama, Türkçe")


class MissedClaim(BaseModel):
    segment: int
    text: str = Field(description="Anlatımda olup claims listesinde olmayan olgusal ifade")
    verdict: Verdict
    evidence: str


class Verification(BaseModel):
    checks: list[ClaimCheck]
    missed: list[MissedClaim]


SYSTEM = """Sen bağımsız bir doğrulama editörüsün (fact-checker). Bir teknoloji haber videosunun senaryosundaki iddiaları, verilen kaynak metinleriyle karşılaştırırsın.
- Yalnızca verilen kaynak metinlerine dayan; kendi bilgini kullanma. Kaynakta yoksa "not_found" de.
- Rakam, tarih, isim, sürüm numarası birebir eşleşmeli; yuvarlama veya birim farkı varsa "partial".
- evidence alanına kaynaktan birebir alıntı koy.
- Ayrıca anlatım (narration) ve student_take içinde olup claims listesinde bulunmayan olgusal ifadeleri "missed" listesine ekle ve onları da değerlendir.
- Hook, teaser, köprü (bridge), soru ve kapanışta segmentlerde desteklenmeyen bir olgu ya da sonda karşılığı olmayan bir vaat varsa onu da "missed" listesine (ilgili segmente) ekle.
- Her iddia için tam bir kayıt döndür."""

NUM_RE = re.compile(r"\d+(?:[.,]\d+)*")


def number_variants(n: str) -> set[str]:
    """'47,3' kaynakta '47.3' olarak geçebilir; '1.250' ↔ '1,250' ↔ '1250'."""
    return {n, n.replace(",", "."), n.replace(".", ","), n.replace(".", "").replace(",", "")}


def numbers_check(segment: dict, sources_text: str) -> list[dict]:
    texts = [segment["narration"], segment["student_take"], segment["headline"]]
    for v in segment["visuals"]:
        texts += [f"{x:g}" for x in (v.get("stat_value"), *(v.get("chart_values") or [])) if x is not None]
        texts += v.get("code_lines") or []
    found = []
    for num in sorted({m for t in texts for m in NUM_RE.findall(t)}, key=lambda s: (len(s), s)):
        ok = any(re.search(rf"(?<![\d.,]){re.escape(var)}(?![\d])", sources_text) for var in number_variants(num))
        found.append({"number": num, "in_source": ok})
    return found


def run(week: str, force: bool = False) -> None:
    ep = episode_dir(week)
    out = ep / "verification.json"
    script_file = read_json(ep / "script.json")
    # Kelime sayısı aynı kalan düzeltmeler de yeniden doğrulansın diye senaryo dosyasının özeti karşılaştırılır
    script_hash = file_hash(ep / "script.json")
    if out.exists() and not force and read_json(out).get("script_hash") == script_hash:
        print("[verify] verification.json güncel, atlanıyor")
        return
    script = script_file["script"]

    blocks, numbers = [], {}
    for i, seg in enumerate(script["segments"], 1):
        texts = {url: source_text(ep, url) for url in seg["sources"]}
        numbers[i] = numbers_check(seg, "\n".join(texts.values()))
        claims = "\n".join(f"  [{j}] {c['text']}  (kaynak: {c['source_url']})" for j, c in enumerate(seg["claims"]))
        srcs = "\n".join(f"<kaynak url=\"{u}\">\n{t or '(metin alınamadı)'}\n</kaynak>" for u, t in texts.items())
        blocks.append(f"<segment no=\"{i}\">\nBaşlık: {seg['headline']}\nKöprü: {seg.get('bridge', '')}\nAnlatım: {seg['narration']}\n"
                      f"Öğrenci notu: {seg['student_take']}\nİddialar:\n{claims}\n{srcs}\n</segment>")
    frame = (f"Hook: {script['hook']}\nTeaser: {script.get('teaser', '')}\nSoru: {script.get('question', '')}\n"
             f"Kapanış: {script['outro']}\n\n")
    result = ask(SYSTEM, frame + "\n\n".join(blocks), Verification, task=ep / "llm" / "verify", effort="high")

    write_json(out, {"week": week, "script_word_count": script_file["word_count"], "script_hash": script_hash,
                     "checks": [c.model_dump() for c in result.checks],
                     "missed": [m.model_dump() for m in result.missed],
                     "numbers": numbers,
                     "source_keys": {u: url_key(u) for s in script["segments"] for u in s["sources"]}})
    bad = [c for c in result.checks if c.verdict != "supported"] + [m for m in result.missed if m.verdict != "supported"]
    missing_nums = [n["number"] for ns in numbers.values() for n in ns if not n["in_source"]]
    print(f"[verify] {len(result.checks)} iddia kontrol edildi; {len(bad)} sorunlu/kısmi; "
          f"kaynakta bulunmayan rakam: {', '.join(missing_nums) or '-'}")
