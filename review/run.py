"""Adım 4b — onay sayfası ve onay kapısı.

review.html: senaryo + iddia/kaynak/doğrulama tablosu; uncertain ve doğrulanamayan iddialar kırmızı.
approve: script.json + normalized.json özetlerini approval.json'a yazar. Sonraki adımlar (TTS, render)
`require_approval` ile bu özetleri kontrol eder: onaydan sonra senaryo değişirse yeniden onay gerekir.
"""
from __future__ import annotations

import datetime as dt
import getpass
import subprocess

from jinja2 import Environment, FileSystemLoader, select_autoescape

from common.config import ROOT, episode_dir, file_hash, read_json, settings, write_json


class ApprovalRequired(RuntimeError):
    pass


def _flags(script: dict, ver: dict) -> tuple[list[dict], int]:
    checks = {(c["segment"], c["claim_index"]): c for c in ver["checks"]}
    segs, n_flags = [], 0
    for i, seg in enumerate(script["segments"], 1):
        claims = []
        for j, c in enumerate(seg["claims"]):
            chk = checks.get((i, j), {"verdict": "not_found", "evidence": "", "note": "doğrulama sonucu yok"})
            flag = c["uncertain"] or chk["verdict"] not in ("supported",)
            n_flags += flag
            claims.append({**c, **chk, "flag": flag})
        missed = [m for m in ver["missed"] if m["segment"] == i]
        n_flags += sum(m["verdict"] != "supported" for m in missed)
        nums = ver["numbers"].get(str(i), [])
        n_flags += sum(not n["in_source"] for n in nums)
        segs.append({**seg, "claims": claims, "missed": missed, "numbers": nums})
    return segs, n_flags


def _visual_summary(v: dict) -> str:
    c = v["component"]
    if c == "StatCounter":
        return f"StatCounter: {v.get('stat_prefix') or ''}{v.get('stat_value')}{v.get('stat_suffix') or ''} — {v.get('stat_label')}"
    if c == "MiniChart":
        return f"MiniChart: {v.get('chart_title')} {list(zip(v.get('chart_labels') or [], v.get('chart_values') or []))}"
    if c in ("CodeBlock", "Terminal"):
        return f"{c}: {' / '.join(v.get('code_lines') or [])[:80]}"
    if c == "SourceScreenshot":
        return f"SourceScreenshot: {v.get('screenshot_url')}"
    return c


def render(week: str) -> None:
    ep = episode_dir(week)
    sf, ver, norm = read_json(ep / "script.json"), read_json(ep / "verification.json"), read_json(ep / "normalized.json")
    script = sf["script"]
    segs, n_flags = _flags(script, ver)
    units = {u["id"]: u for u in norm["units"]}
    for i, s in enumerate(segs, 1):
        s["tts_narration"] = units[f"s{i}_narration"]["tts_text"]
        s["tts_take"] = units[f"s{i}_take"]["tts_text"]
        for v in s["visuals"]:
            v["summary"] = _visual_summary(v)
    unknown_tts = {}
    for u in norm["units"]:
        for t in u["tokens"]:
            core = t["display"].strip(",.;:!?()\"'’").split("'")[0]
            if core in norm["unknown_terms"]:
                unknown_tts[core] = t["tts"].strip(",.;:!?")
    approval = ep / "approval.json"
    env = Environment(loader=FileSystemLoader(ROOT / "review"), autoescape=select_autoescape())
    html = env.get_template("template.html").render(
        week=week, generated_at=dt.datetime.now().strftime("%Y-%m-%d %H:%M"), hook=script["hook"], outro=script["outro"],
        teaser=script.get("teaser", ""), question=script.get("question", ""),
        segments=segs, word_count=sf["word_count"], est_seconds=sf["est_seconds"], n_flags=n_flags,
        unknown_terms=norm["unknown_terms"], unknown_tts=unknown_tts,
        approved=read_json(approval) if approval.exists() and _approval_valid(ep) else None,
    )
    (ep / "review.html").write_text(html, encoding="utf-8")
    write_json(ep / "review_status.json", {"flags": n_flags, "unknown_terms": len(norm["unknown_terms"])})
    status = "onaylı" if approval.exists() and _approval_valid(ep) else f"onay bekleniyor: make approve WEEK={week}"
    print(f"[review] review.html hazır ({n_flags} kırmızı işaret); {status}")


def _hashes(ep) -> dict:
    return {"script": file_hash(ep / "script.json"), "normalized": file_hash(ep / "normalized.json")}


def _approval_valid(ep) -> bool:
    p = ep / "approval.json"
    return p.exists() and read_json(p).get("hashes") == _hashes(ep)


def require_approval(week: str) -> None:
    """Onay kapısı. TTS ve sonrası her adım bunu çağırır."""
    ep = episode_dir(week)
    if not (ep / "approval.json").exists():
        raise ApprovalRequired(f"{week} onaylanmadı. episodes/{week}/review.html'i inceleyip `make approve WEEK={week}` çalıştırın.")
    if not _approval_valid(ep):
        raise ApprovalRequired(f"{week}: onaydan sonra senaryo veya normalizasyon değişmiş. review.html'i yeniden inceleyip tekrar onaylayın.")


def approve(week: str, accept_flags: bool = False) -> None:
    ep = episode_dir(week)
    for f in ("script.json", "normalized.json", "verification.json", "review.html"):
        if not (ep / f).exists():
            raise ApprovalRequired(f"{f} yok; önce `make episode WEEK={week}` çalıştırın.")
    flags = read_json(ep / "review_status.json")["flags"]
    if flags and not accept_flags:
        raise ApprovalRequired(f"review.html'de {flags} kırmızı işaret var. İnceleyip yine de onaylıyorsanız --accept-flags ekleyin "
                               f"(make approve WEEK={week} FLAGS=1), ya da `revise` ile düzeltin.")
    try:
        who = subprocess.run(["git", "config", "user.name"], capture_output=True, text=True, cwd=ROOT).stdout.strip()
    except OSError:
        who = ""
    write_json(ep / "approval.json", {
        "week": week, "approved_by": who or getpass.getuser(),
        "approved_at": dt.datetime.now().isoformat(timespec="seconds"),
        "accepted_flags": flags, "hashes": _hashes(ep), "tts_backend": settings()["tts"]["backend"],
    })
    render(week)
    print(f"[approve] {week} onaylandı. Devam: make episode WEEK={week}")
