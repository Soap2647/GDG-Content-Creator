"""Metin normalizasyonu: display_text (orijinal yazım) → tts_text (fonetik), kelime düzeyinde eşlemeyle.

Her görüntü kelimesi (veya çok kelimeli sözlük terimi) bir `Token`'dır: {display, tts}.
Altyazı display'i gösterir; TTS'e tts gider; zaman damgaları tts kelimelerinden display'e taşınır.
"""
from __future__ import annotations

import json
import re
from dataclasses import asdict, dataclass, field
from functools import lru_cache

from common.config import CONFIG_DIR
from normalizer.numbers import MONTHS, digits_to_words, number_to_words

LETTERS = {
    "a": "a", "b": "be", "c": "ce", "ç": "çe", "d": "de", "e": "e", "f": "fe", "g": "ge", "ğ": "yumuşak ge",
    "h": "he", "ı": "ı", "i": "i", "j": "je", "k": "ke", "l": "le", "m": "me", "n": "ne", "o": "o", "ö": "ö",
    "p": "pe", "q": "kü", "r": "re", "s": "se", "ş": "şe", "t": "te", "u": "u", "ü": "ü", "v": "ve",
    "w": "dabılyu", "x": "iks", "y": "ye", "z": "ze",
}
CURRENCY = {"$": "dolar", "€": "avro", "£": "sterlin", "₺": "lira"}
TRAIL = ",.;:!?)\"»…”'’"
LEAD = "(\"«“'‘"
SCALE_WORDS = {"bin", "milyon", "milyar", "trilyon"}
TR_LOWER = str.maketrans({"I": "ı", "İ": "i"})
# İngilizce görünümlü kelime sezgisi (yalnızca onay sayfasında listelemek için; yanlış pozitif zararsız)
EN_HINT = re.compile(r"(th|sh|ck|ph|oo|ee|ea|ou|ow|w|q|x|tion|ing$|[a-z][A-Z])")


@dataclass
class Token:
    display: str
    tts: str
    unknown: bool = False


@dataclass
class Normalized:
    display_text: str
    tts_text: str
    tokens: list[Token] = field(default_factory=list)
    unknown_terms: list[str] = field(default_factory=list)

    def to_dict(self) -> dict:
        return asdict(self)


@lru_cache
def dictionary() -> dict[str, str]:
    return json.loads((CONFIG_DIR / "pronunciation.json").read_text(encoding="utf-8"))["terms"]


def tr_lower(s: str) -> str:
    return s.translate(TR_LOWER).lower()


def spell(s: str) -> str:
    return " ".join(LETTERS.get(ch, ch) for ch in tr_lower(s) if ch.isalnum())


def lookup(term: str) -> str | None:
    d = dictionary()
    if term in d:
        return d[term]
    low = {tr_lower(k): v for k, v in d.items()}
    return low.get(tr_lower(term))


def number_word(s: str, prev: str = "") -> str | None:
    """Sayısal bir çekirdeği yazıya çevirir; sayı değilse None."""
    if re.fullmatch(r"\d{1,3}(\.\d{3})+", s):  # 1.250 / 47.300.000 (Türkçe binlik ayırıcı)
        return number_to_words(int(s.replace(".", "")))
    if m := re.fullmatch(r"(\d{1,2})\.(\d{1,2})\.(\d{4})", s):  # 15.10.2026
        d, mo, y = map(int, m.groups())
        if 1 <= mo <= 12:
            return f"{number_to_words(d)} {MONTHS[mo - 1]} {number_to_words(y)}"
    if m := re.fullmatch(r"(\d{1,2})[:.](\d{2})", s) and (":" in s or tr_lower(prev) == "saat"):  # 14:30, saat 14.00
        h, mi = re.split(r"[:.]", s)
        return number_to_words(int(h)) + ("" if mi == "00" else " " + number_to_words(int(mi)))
    if m := re.fullmatch(r"(\d+),(\d+)", s):  # 47,3
        return f"{number_to_words(int(m.group(1)))} virgül {digits_to_words(m.group(2))}"
    if re.fullmatch(r"\d+(\.\d+)+", s):  # 3.14 / 2.0.1 (sürüm)
        return " nokta ".join(digits_to_words(p) if i else number_to_words(int(p)) for i, p in enumerate(s.split(".")))
    if re.fullmatch(r"\d+", s):
        return number_to_words(int(s))
    return None


def convert_core(core: str, prev: str = "") -> tuple[str, bool]:
    """Tek bir kelime çekirdeğini (noktalama ayrılmış) fonetik metne çevirir. (tts, bilinmeyen_mi)"""
    base, suffix = core, ""
    if m := re.fullmatch(r"(.+?)['’]([a-zçğıöşüâîû]+)", core):
        base, suffix = m.groups()

    if (tts := lookup(base)) is not None:
        return tts + suffix, False
    if m := re.fullmatch(r"%(\d+(?:[.,]\d+)?)", base):
        return "yüzde " + number_word(m.group(1)) + suffix, False
    if base and base[0] in CURRENCY and (n := number_word(base[1:])):
        return f"{n} {CURRENCY[base[0]]}" + suffix, False
    if (n := number_word(base, prev)) is not None:
        if n.endswith("dört") and suffix[:1] in "aeıioöuü" and suffix:  # ünsüz yumuşaması: 4'ü -> dördü
            n = n[:-1] + "d"
        return n + suffix, False
    if "-" in base.strip("-") and not base.isalpha():
        parts = [convert_core(p) for p in base.split("-") if p]
        return " ".join(p for p, _ in parts) + suffix, any(u for _, u in parts)
    if re.search(r"\d", base) and re.search(r"[^\W\d_]", base):  # RTX5090, M5, 8GB
        runs = re.findall(r"\d+(?:[.,]\d+)?|[^\W\d_]+", base)
        parts = [convert_core(r) for r in runs]
        return " ".join(p for p, _ in parts) + suffix, any(u for _, u in parts)
    if re.fullmatch(r"[A-ZÇĞİÖŞÜ]{2,6}", base):  # sözlükte olmayan kısaltma: harf harf
        return spell(base) + suffix, True
    plain = base + suffix  # kesme işareti TTS'e gitmez: "Kasım'da" -> "Kasımda"
    if base.isalpha() and EN_HINT.search(base):
        return plain, True
    return plain, False


def normalize(text: str) -> Normalized:
    words = text.split()
    d = dictionary()
    multi = sorted((k for k in d if " " in k), key=lambda k: -len(k.split()))
    tokens: list[Token] = []
    unknown: list[str] = []
    pending_currency = ""
    i = 0
    while i < len(words):
        # Çok kelimeli sözlük terimleri (ör. "Hugging Face") tek token olur
        hit = None
        for term in multi:
            n = len(term.split())
            chunk = " ".join(words[i:i + n])
            core = chunk.strip(TRAIL).lstrip(LEAD)
            if tr_lower(core.split("'")[0]) == tr_lower(term):
                hit = (n, chunk, d[term] + (core.split("'", 1)[1] if "'" in core else ""))
                break
        if hit:
            n, chunk, tts = hit
            tokens.append(Token(chunk, tts))
            i += n
            continue
        w = words[i]
        lead = w[: len(w) - len(w.lstrip(LEAD))]
        rest = w[len(lead):]
        core = rest.rstrip(TRAIL)
        trail = rest[len(core):]
        # Son nokta bir sayının parçası değil cümle sonudur ("2026." → "2026" + ".")
        tts_core, unk = convert_core(core, words[i - 1].strip(TRAIL) if i else "") if core else ("", False)
        # "$47,3 milyar" -> "kırk yedi virgül üç milyar dolar": para birimi ölçek kelimesinden sonra okunur
        nxt = words[i + 1].strip(TRAIL) if i + 1 < len(words) else ""
        if core[:1] in CURRENCY and number_word(core[1:]) and tr_lower(nxt) in SCALE_WORDS:
            tts_core = number_word(core[1:])
            pending_currency = CURRENCY[core[0]]
        elif pending_currency:
            tts_core, pending_currency = f"{tts_core} {pending_currency}", ""
        tokens.append(Token(w, (lead.replace("'", "") + tts_core + trail.replace("'", "").replace("’", "")).strip(), unk))
        if unk:
            unknown.append(re.split(r"['’]", core)[0])
        i += 1
    tts_text = re.sub(r"\s+", " ", " ".join(t.tts for t in tokens if t.tts)).strip()
    return Normalized(text, tts_text, tokens, sorted(set(unknown)))


def split_sentences(tokens: list[Token]) -> list[list[Token]]:
    """Cümle sonu: display'i . ! ? ile biten token (sayı içi noktalar zaten çekirdekte kalır)."""
    out, cur = [], []
    for t in tokens:
        cur.append(t)
        if t.display.rstrip("\"”»')").endswith((".", "!", "?", "…")):
            out.append(cur)
            cur = []
    if cur:
        out.append(cur)
    return out


if __name__ == "__main__":
    for s in [
        "OpenAI, yeni modeli GPT-6'yı 15 Kasım'da tanıttı.",
        "Nvidia'nın geliri $47,3 milyar oldu; GPU payı %12'ye çıktı.",
        "TÜBİTAK 2209-A başvuruları 15.10.2026'da, saat 14.00'te başlıyor.",
        "Python 3.14 ile 1.250 TL tasarruf, RTX5090 ve 8GB VRAM'li sistemler.",
        "Hugging Face'in yeni SmolLM modeli WWDC'de değil, GitHub Student Developer Pack'te.",
    ]:
        n = normalize(s)
        print(n.tts_text, "| bilinmeyen:", n.unknown_terms)
