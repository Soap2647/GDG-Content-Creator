"""WER/CER öncesi metin normalizasyonu (referans ve Whisper çıktısına aynı kurallar uygulanır).

Rakamlar Türkçe yazıya dökülür, yüzde/ondalık/sürüm kalıpları açılır, kesme işaretleri
ve noktalama kaldırılır, bilinen terimlerin yazım varyantları tek forma indirilir.
Faz 2'deki normalizer'ın sayı→yazı kısmı buradan türetilecek.
"""
from __future__ import annotations

import re

ONES = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
TENS = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
SCALES = [(10**12, "trilyon"), (10**9, "milyar"), (10**6, "milyon"), (10**3, "bin")]


def _below_1000(n: int) -> list[str]:
    words = []
    h, rest = divmod(n, 100)
    if h:
        words += (["yüz"] if h == 1 else [ONES[h], "yüz"])
    t, o = divmod(rest, 10)
    if t:
        words.append(TENS[t])
    if o:
        words.append(ONES[o])
    return words


def number_to_words(n: int) -> str:
    """Tam sayıyı Türkçe yazıya çevirir: 2026 -> 'iki bin yirmi altı'."""
    if n == 0:
        return "sıfır"
    if n < 0:
        return "eksi " + number_to_words(-n)
    words: list[str] = []
    for value, name in SCALES:
        q, n = divmod(n, value)
        if q:
            # "bir bin" denmez, "bin" denir
            words += ([name] if (q == 1 and name == "bin") else _below_1000(q) + [name])
    words += _below_1000(n)
    return " ".join(words)


def digits_to_words(s: str) -> str:
    """Ondalık kısmı okunduğu gibi: '14' -> 'on dört', '05' -> 'sıfır beş'."""
    lead = len(s) - len(s.lstrip("0"))
    rest = s.lstrip("0")
    return " ".join(["sıfır"] * lead + ([number_to_words(int(rest))] if rest else []))


def tr_lower(s: str) -> str:
    return s.replace("I", "ı").replace("İ", "i").lower()


# Whisper'ın aynı terimi yazabileceği varyantlar -> kanonik form (küçük harf, boşluksuz)
TERM_ALIASES: dict[str, list[str]] = {
    "openai": [r"open\s*ai", r"open-ai"],
    "github": [r"git\s*hub"],
    "copilot": [r"co\s*pilot"],
    "iphone": [r"i\s*phone", r"ayfon"],
    "nvidia": [r"n\s*vidia", r"envidya", r"nvidya"],
    "anthropic": [r"antropik", r"entropik", r"anthropik", r"entropic"],
    "kubernetes": [r"kubernetis", r"kübernetis"],
    "chatgpt": [r"chat\s*gpt"],
    "llm": [r"l\s*l\s*m"],
    "tübitak": [r"tubitak"],
    "teknofest": [r"tekno\s*fest"],
}

_SUFFIX = r"(?:['’]?([a-zçğıöşü]+))?"


def _attach(words: str, suffix: str | None) -> str:
    return words + (suffix or "")


def normalize(text: str) -> str:
    s = text.replace("’", "'")
    # %12'ye -> yüzde on ikiye ; %47,3 -> yüzde kırk yedi virgül üç
    s = re.sub(
        r"%\s*(\d+)(?:,(\d+))?" + _SUFFIX,
        lambda m: "yüzde "
        + _attach(
            number_to_words(int(m.group(1))) + (" virgül " + digits_to_words(m.group(2)) if m.group(2) else ""),
            m.group(3),
        ),
        s,
        flags=re.IGNORECASE,
    )
    # 47,3 -> kırk yedi virgül üç
    s = re.sub(
        r"(\d+),(\d+)" + _SUFFIX,
        lambda m: _attach(number_to_words(int(m.group(1))) + " virgül " + digits_to_words(m.group(2)), m.group(3)),
        s,
        flags=re.IGNORECASE,
    )
    # 3.14 -> üç nokta on dört (sürüm numaraları; binlik ayırıcı noktalı sayılar haberlerde nadir)
    s = re.sub(
        r"(\d+)\.(\d+)" + _SUFFIX,
        lambda m: _attach(number_to_words(int(m.group(1))) + " nokta " + digits_to_words(m.group(2)), m.group(3)),
        s,
        flags=re.IGNORECASE,
    )
    s = s.replace("-", " ")
    # 17'nin -> on yedinin
    s = re.sub(
        r"(\d+)" + _SUFFIX,
        lambda m: _attach(number_to_words(int(m.group(1))), m.group(2)),
        s,
        flags=re.IGNORECASE,
    )
    # Terimler küçük harfe çevirmeden önce: tr_lower İngilizce "I"yı "ı" yapar (OpenAI -> openaı)
    for canon, patterns in TERM_ALIASES.items():
        for p in [canon, *patterns]:
            s = re.sub(r"\b" + p, canon, s, flags=re.IGNORECASE)
    s = tr_lower(s)
    s = s.replace("'", "")
    s = re.sub(r"[^\w\s]", " ", s)
    return re.sub(r"\s+", " ", s).strip()


if __name__ == "__main__":
    for t in [
        "OpenAI, yeni modeli GPT-6'yı 15 Kasım'da tanıttı.",
        "Nvidia'nın çeyreklik geliri 47,3 milyar dolara ulaştı.",
        "GPU paylaşımı %12 daha verimli; %30'a varan hız.",
        "Python 3.14 sürümü, TÜBİTAK 2209-A, 2026'da 65 milyar dolar.",
        "Open AI ve Git Hub, i Phone'daki CPU",
    ]:
        print(normalize(t))
