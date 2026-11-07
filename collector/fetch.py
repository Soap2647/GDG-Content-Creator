"""Kaynaklardan ham haber listesini çeker (RSS ve RSS'i olmayan duyuru sayfaları)."""
from __future__ import annotations

import datetime as dt
import html
import re
from concurrent.futures import ThreadPoolExecutor
from email.utils import parsedate_to_datetime
from urllib.parse import urljoin, urlsplit, urlunsplit

import feedparser
import httpx

HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; GDG-Kastamonu-TechDigest/1.0)"}


def clean_text(s: str | None, limit: int = 600) -> str:
    s = re.sub(r"<[^>]+>", " ", s or "")
    s = re.sub(r"\s+", " ", html.unescape(s)).strip()
    return s[:limit]


def canonical_url(url: str) -> str:
    """Takip parametreleri ve sondaki / atılmış URL; tekrar tespiti için."""
    parts = urlsplit(url)
    query = "&".join(p for p in parts.query.split("&") if p and not p.startswith(("utm_", "ref=", "fbclid")))
    return urlunsplit((parts.scheme, parts.netloc.lower().removeprefix("www."), parts.path.rstrip("/"), query, ""))


def _parse_date(entry) -> dt.datetime | None:
    for key in ("published_parsed", "updated_parsed"):
        if entry.get(key):
            return dt.datetime(*entry[key][:6], tzinfo=dt.timezone.utc)
    for key in ("published", "updated"):
        if entry.get(key):
            try:
                d = parsedate_to_datetime(entry[key])
                return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)
            except (TypeError, ValueError):
                pass
    return None


def _page_date(url: str) -> dt.datetime | None:
    import trafilatura

    try:
        meta = trafilatura.extract_metadata(httpx.get(url, headers=HEADERS, timeout=20, follow_redirects=True).text)
        if meta and meta.date:
            return dt.datetime.fromisoformat(meta.date).replace(tzinfo=dt.timezone.utc)
    except (httpx.HTTPError, ValueError):
        pass
    return None


def fetch_rss(src: dict, limit: int) -> list[dict]:
    r = httpx.get(src["url"], headers=HEADERS, timeout=25, follow_redirects=True)
    r.raise_for_status()
    feed = feedparser.parse(r.content)
    items = []
    for e in feed.entries[:limit]:
        # Bazı akışlarda (ör. Google Developers Blog) tarih yok: sayfanın meta verisinden okunur
        date = _parse_date(e) or _page_date(e.get("link", ""))
        items.append({
            "title": clean_text(e.get("title"), 300),
            "url": e.get("link", ""),
            "source": src["name"],
            "lang": src.get("lang", "en"),
            "date": date.isoformat() if date else None,
            "summary": clean_text(e.get("summary") or e.get("description")),
            "weight": src.get("weight", 1.0),
        })
    return items


def fetch_html(src: dict, limit: int) -> list[dict]:
    """RSS'i olmayan sayfa: link_pattern'e uyan duyuru linklerini sırayla alır, her birinin meta verisini çeker."""
    import trafilatura

    r = httpx.get(src["url"], headers=HEADERS, timeout=25, follow_redirects=True)
    r.raise_for_status()
    hrefs = re.findall(r'href="([^"#?]+)"', r.text)
    pattern = re.compile(src["link_pattern"])
    exclude = set(src.get("exclude", []))
    links = [h for h in dict.fromkeys(hrefs) if pattern.search(h) and h not in exclude][: min(limit, 8)]
    items = []
    for href in links:
        url = urljoin(src.get("base", src["url"]), href)
        try:
            page = httpx.get(url, headers=HEADERS, timeout=25, follow_redirects=True)
            meta = trafilatura.extract_metadata(page.text)
        except httpx.HTTPError:
            continue
        date = None
        if meta and meta.date:
            date = dt.datetime.fromisoformat(meta.date).replace(tzinfo=dt.timezone.utc)
        items.append({
            "title": clean_text(meta.title if meta else href, 300),
            "url": url,
            "source": src["name"],
            "lang": src.get("lang", "en"),
            "date": date.isoformat() if date else None,
            "summary": clean_text(meta.description if meta else ""),
            "weight": src.get("weight", 1.0),
        })
    return items


def fetch_all(sources: list[dict], limit: int) -> tuple[list[dict], list[str]]:
    """Tüm kaynakları paralel çeker. Bozuk kaynak tüm adımı durdurmaz; hatalar ayrıca döner."""
    def one(src):
        try:
            fn = fetch_html if src.get("type") == "html" else fetch_rss
            return fn(src, limit), None
        except Exception as e:  # noqa: BLE001 - her kaynak hatası raporlanır, akış sürer
            return [], f"{src['name']}: {type(e).__name__}: {str(e)[:120]}"

    with ThreadPoolExecutor(max_workers=8) as pool:
        results = list(pool.map(one, sources))
    items = [i for its, _ in results for i in its]
    errors = [err for _, err in results if err]
    return items, errors


def fetch_article_text(url: str, max_chars: int = 12000) -> str:
    """Haber sayfasının ana metni (doğrulama ve senaryo için kaynak gerçeği)."""
    import trafilatura

    r = httpx.get(url, headers=HEADERS, timeout=30, follow_redirects=True)
    r.raise_for_status()
    text = trafilatura.extract(r.text, include_comments=False, include_tables=True, favor_precision=True) or ""
    return text[:max_chars]
