"""Ortak yollar, ayarlar ve küçük G/Ç yardımcıları."""
from __future__ import annotations

import datetime as dt
import hashlib
import json
import os
import re
from functools import lru_cache
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
CONFIG_DIR = ROOT / "config"
EPISODES_DIR = ROOT / "episodes"
ASSETS_DIR = ROOT / "assets"


def load_env() -> None:
    """.env dosyasını ortam değişkenlerine yükler (var olanları ezmeden)."""
    env = ROOT / ".env"
    if not env.exists():
        return
    for line in env.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            k, v = line.split("=", 1)
            if v.strip():
                os.environ.setdefault(k.strip(), v.strip().strip('"'))


@lru_cache
def settings() -> dict[str, Any]:
    return yaml.safe_load((CONFIG_DIR / "pipeline.yaml").read_text(encoding="utf-8"))


def episode_dir(week: str) -> Path:
    if not re.fullmatch(r"\d{4}-W\d{2}", week):
        raise ValueError(f"WEEK biçimi YYYY-Www olmalı (ör. 2026-W44), gelen: {week!r}")
    d = EPISODES_DIR / week
    d.mkdir(parents=True, exist_ok=True)
    return d


def week_window(week: str, days: int) -> tuple[dt.datetime, dt.datetime]:
    """Haftanın haber penceresi: hafta sonu (Pazar 23:59) veya şimdi, hangisi önceyse; geriye `days` gün."""
    year, wk = int(week[:4]), int(week[6:])
    monday = dt.datetime.fromisocalendar(year, wk, 1).replace(tzinfo=dt.timezone.utc)
    end = min(monday + dt.timedelta(days=7), dt.datetime.now(dt.timezone.utc))
    return end - dt.timedelta(days=days), end


def current_week() -> str:
    y, w, _ = dt.date.today().isocalendar()
    return f"{y}-W{w:02d}"


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")


def file_hash(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()[:16]


def url_key(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]
