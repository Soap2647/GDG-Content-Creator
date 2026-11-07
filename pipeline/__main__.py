"""Pipeline komut satırı.  python -m pipeline <adım> --week 2026-W44

episode   : collect → write → normalize → verify → review  ║ ONAY KAPISI ║ → tts → assets → render → package
            Onay yoksa kapıda durur; onaydan sonra aynı komut kaldığı yerden devam eder.
approve   : review.html incelendikten sonra bölümü onaylar
revise    : editör geri bildirimiyle senaryoyu yeniden yazar ve doğrulamayı tekrarlar
Diğer adımlar tek başına çalıştırılabilir; çıktısı olan adımlar --force verilmedikçe atlanır.
"""
from __future__ import annotations

import argparse
import sys
import time

from common.config import current_week, episode_dir, read_json, write_json
from common.llm import LLMError, LLMPending
from review.run import ApprovalRequired, _approval_valid


def _timed(week: str, name: str, fn, *args, **kwargs) -> None:
    t0 = time.perf_counter()
    fn(*args, **kwargs)
    path = episode_dir(week) / "timings.json"
    data = read_json(path) if path.exists() else {}
    data[name] = round(time.perf_counter() - t0, 1)
    write_json(path, data)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="python -m pipeline", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("step", choices=["episode", "collect", "write", "normalize", "verify", "review", "approve", "revise",
                                     "tts", "assets", "render", "package"])
    ap.add_argument("--week", default=current_week(), help="ISO hafta, ör. 2026-W44 (varsayılan: bu hafta)")
    ap.add_argument("--force", action="store_true", help="adımın çıktısı olsa bile yeniden üret")
    ap.add_argument("--accept-flags", action="store_true", help="approve: kırmızı işaretlere rağmen onayla")
    ap.add_argument("--feedback", help="revise: senaryo için editör notu")
    ap.add_argument("--voice", help="tts: bu haftanın sesini elle seç (ör. male_2); varsayılan haftalık dönüşüm")
    ap.add_argument("--backend", help="tts: bu haftanın ses modelini elle seç (ör. gemini); varsayılan tts.backend")
    a = ap.parse_args(argv)
    w, force = a.week, a.force

    from collector import run as collector
    from media import run as media
    from normalizer import run as normalizer
    from review import run as review
    from review import verify
    from tts import run as tts
    from writer import run as writer

    pre_gate = [("collect", collector.run), ("write", writer.run), ("normalize", normalizer.run),
                ("verify", verify.run), ("review", lambda wk, force=False: review.render(wk))]
    post_gate = [("tts", lambda wk, force=False: tts.run(wk, force=force, voice=a.voice, backend=a.backend)), ("assets", media.assets), ("render", media.render), ("package", media.package)]
    steps = dict(pre_gate + post_gate)

    try:
        if a.step == "episode":
            for name, fn in pre_gate:
                _timed(w, name, fn, w, force=force)
            if not _approval_valid(episode_dir(w)):
                print(f"\n■ ONAY KAPISI: episodes/{w}/review.html dosyasını inceleyin, ardından:\n"
                      f"    make approve WEEK={w}      (veya: python -m pipeline approve --week {w})\n"
                      f"  Sonra aynı komutu tekrar çalıştırın: make episode WEEK={w}")
                return 3
            for name, fn in post_gate:
                _timed(w, name, fn, w, force=force)
            print(f"\n✓ Bölüm hazır: episodes/{w}/final.mp4, thumbnail.png, post.md, sources.json")
        elif a.step == "approve":
            review.approve(w, accept_flags=a.accept_flags)
        elif a.step == "revise":
            if not a.feedback:
                ap.error("revise için --feedback gerekli")
            _timed(w, "revise", writer.run, w, feedback=a.feedback)
            for name, fn in pre_gate[2:]:
                _timed(w, name, fn, w, force=True)
        else:
            _timed(w, a.step, steps[a.step], w, force=force)
    except ApprovalRequired as e:
        print(f"■ {e}", file=sys.stderr)
        return 3
    except LLMPending as e:
        print(f"◆ {e}\n  Claude Code yanıtı yazdıktan sonra aynı komutu tekrar çalıştırın.", file=sys.stderr)
        return 4
    except LLMError as e:
        print(f"✗ Claude adımı başarısız: {e}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
