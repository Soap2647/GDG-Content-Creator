"""Türkçe sayı → yazı. Faz 1'deki research/eval/textnorm.py'den türetildi."""
from __future__ import annotations

ONES = ["", "bir", "iki", "üç", "dört", "beş", "altı", "yedi", "sekiz", "dokuz"]
TENS = ["", "on", "yirmi", "otuz", "kırk", "elli", "altmış", "yetmiş", "seksen", "doksan"]
SCALES = [(10**12, "trilyon"), (10**9, "milyar"), (10**6, "milyon"), (10**3, "bin")]
MONTHS = ["Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]


def _below_1000(n: int) -> list[str]:
    words = []
    h, rest = divmod(n, 100)
    if h:
        words += ["yüz"] if h == 1 else [ONES[h], "yüz"]
    t, o = divmod(rest, 10)
    if t:
        words.append(TENS[t])
    if o:
        words.append(ONES[o])
    return words


def number_to_words(n: int) -> str:
    """2026 -> 'iki bin yirmi altı'."""
    if n == 0:
        return "sıfır"
    if n < 0:
        return "eksi " + number_to_words(-n)
    words: list[str] = []
    for value, name in SCALES:
        q, n = divmod(n, value)
        if q:
            words += [name] if (q == 1 and name == "bin") else _below_1000(q) + [name]
    words += _below_1000(n)
    return " ".join(words)


def digits_to_words(s: str) -> str:
    """Ondalık/sürüm kısmı okunduğu gibi: '14' -> 'on dört', '05' -> 'sıfır beş'."""
    rest = s.lstrip("0")
    zeros = ["sıfır"] * (len(s) - len(rest))
    return " ".join(zeros + ([number_to_words(int(rest))] if rest else []))
