"""Adım 6 — görsel varlıklar ve render (onay kapısından sonra).

assets: kaynak sayfa ekran görüntüleri (Playwright), müzik/efekt kopyaları, render_props.json
render: Remotion ile final.mp4 (+ ses yüksekliği -14 LUFS), thumbnail.png
package: post.md, sources.json
"""
from __future__ import annotations

import io
import shutil
import subprocess
from urllib.parse import urlsplit

from PIL import Image, ImageStat

from common.config import ASSETS_DIR, ROOT, episode_dir, read_json, settings, url_key, write_json
from review.run import require_approval

VIDEO_DIR = ROOT / "video"
NPX = "npx.cmd" if shutil.which("npx.cmd") else "npx"


def domain(url: str) -> str:
    return urlsplit(url).netloc.removeprefix("www.")


# Haber konusu ikonu (video/src/components/Icons.tsx): başlık + anlatımda geçen ilk eşleşen kural kazanır.
ICON_RULES = [
    ("flag", ("ctf", "capture the flag", "yarışma", "hackathon", "ödül")),
    ("lock", ("şifre", "parola", "siber", "güvenlik açığı", "zafiyet", "hack")),
    ("shield", ("güvenlik", "gizlilik", "koruma")),
    ("calendar", ("başvuru", "kış okulu", "yaz okulu", "burs", "etkinlik", "staj", "son başvuru")),
    ("globe", ("dünya", "simülasyon", "harita", "küresel")),
    ("chip", ("gpu", "çip", "işlemci", "donanım")),
    ("code", ("kod", "api", "sürüm", "açık kaynak", "github", "python", "yazılım")),
    ("phone", ("telefon", "android", "ios", "uygulama")),
    ("rocket", ("uzay", "roket", "fırlatma")),
    ("spark", ("yapay zeka", "model", "gemini", "llm", "yapay zekâ")),
]


def topic_icon(seg: dict) -> str:
    text = f"{seg['headline']} {seg['narration']}".lower()
    return next((icon for icon, keys in ICON_RULES if any(k in text for k in keys)), "bolt")


def screenshots(ep, urls: list[str], force: bool = False) -> dict[str, dict]:
    """Her URL için 1080 genişlikte, sayfanın üst kısmının ekran görüntüsü. Başarısız olanlar atlanır."""
    from playwright.sync_api import sync_playwright

    out_dir = ep / "screenshots"
    out_dir.mkdir(exist_ok=True)
    done = {}
    todo = [u for u in urls if force or not (out_dir / f"{url_key(u)}.png").exists()]
    if todo:
        with sync_playwright() as p:
            browser = p.chromium.launch()
            page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=1, locale="tr-TR")
            for u in todo:
                try:
                    page.goto(u, wait_until="domcontentloaded", timeout=30000)
                    # JS ile çizilen sayfalar (ör. tubitak.gov.tr) domcontentloaded'da hâlâ boş olabiliyor
                    try:
                        page.wait_for_load_state("networkidle", timeout=15000)
                    except Exception:  # noqa: BLE001 - sürekli istek atan sayfalarda beklemeyi kes
                        pass
                    page.wait_for_timeout(1500)
                    if page.evaluate("document.body.innerText.trim().length") < 200:
                        print(f"  ! sayfa boş görünüyor, ekran görüntüsü atlandı: {u}")
                        continue
                    # Çerez bantlarını gizlemeyi dene (onay verilmez, yalnızca görünmez yapılır).
                    # Görsel kısıtı: şirket logosu ve gerçek kişi fotoğrafı olmasın diye sayfadaki tüm
                    # görseller bulanıklaştırılır; ekran görüntüsünde yalnızca metin okunur kalır.
                    page.add_style_tag(content=(
                        # body'ye "cookie" sınıfı ekleyen siteler var (tubitak.gov.tr): html/body hariç tutulur
                        ":is([id*=cookie i],[class*=cookie i],[id*=consent i],[class*=consent i]):not(html,body)"
                        "{display:none!important}"
                        "img,picture,video,svg,canvas,iframe{filter:blur(22px)!important}"))
                    # Makale başlığına kaydır (üstteki reklam/menü alanı yerine haberin kendisi görünsün) ve
                    # başlığın konumunu kaydet: videodaki fosforlu kalem tam bu satırın üstünden geçer.
                    box = page.evaluate("""() => {
                        const h = [...document.querySelectorAll('h1')].find(e => e.innerText.trim().length > 10);
                        if (!h) return null;
                        window.scrollTo(0, Math.max(0, h.getBoundingClientRect().top + window.scrollY - 140));
                        const r = h.getBoundingClientRect();
                        return {y: r.top, h: r.height, x: r.left, w: r.width};
                    }""")
                    page.wait_for_timeout(400)
                    # Bazı sayfalar (ör. tubitak.gov.tr) yüklenmiş görünse de bir süre beyaz çiziliyor:
                    # neredeyse tek renk çıkan görüntü 3 kez beklenip yeniden alınır.
                    for _ in range(3):
                        png = page.screenshot()
                        if ImageStat.Stat(Image.open(io.BytesIO(png)).convert("L")).stddev[0] > 12:
                            break
                        page.wait_for_timeout(2500)
                    else:
                        print(f"  ! sayfa boş çizildi, ekran görüntüsü atlandı: {u}")
                        continue
                    (out_dir / f"{url_key(u)}.png").write_bytes(png)
                    write_json(out_dir / f"{url_key(u)}.json", {"url": u, "title_box": box})
                except Exception as e:  # noqa: BLE001
                    print(f"  ! ekran görüntüsü alınamadı: {u} ({type(e).__name__})")
            browser.close()
    for u in urls:
        if (out_dir / f"{url_key(u)}.png").exists():
            meta = out_dir / f"{url_key(u)}.json"
            done[u] = {"path": f"screenshots/{url_key(u)}.png",
                       "title_box": read_json(meta).get("title_box") if meta.exists() else None}
    return done


def assets(week: str, force: bool = False) -> None:
    require_approval(week)
    ep = episode_dir(week)
    script = read_json(ep / "script.json")["script"]
    timeline = read_json(ep / "timeline.json")
    vcfg = settings()["video"]

    shot_urls = sorted({v["screenshot_url"] for s in script["segments"] for v in s["visuals"]
                        if v["component"] == "SourceScreenshot" and v.get("screenshot_url")})
    shots = screenshots(ep, shot_urls, force=force)

    media = ep / "media"
    media.mkdir(exist_ok=True)
    for src in (ASSETS_DIR / "music" / "bed.mp3", ASSETS_DIR / "sfx" / "whoosh.mp3", ASSETS_DIR / "sfx" / "pop.mp3"):
        shutil.copy2(src, media / src.name)
    logo = None
    # Video zemini açık (krem, 2026-11-07 editoryal tema): koyu yazılı logo; yoksa eski koyu zemin logosu
    for name in ("gdg_logo.png", "gdg_logo_light.png"):
        if (ASSETS_DIR / "brand" / name).exists():
            shutil.copy2(ASSETS_DIR / "brand" / name, media / name)
            logo = f"media/{name}"

    segments = []
    for i, s in enumerate(script["segments"], 1):
        visuals = []
        for v in s["visuals"]:
            v = dict(v)
            if v["component"] == "SourceScreenshot":
                shot = shots.get(v.get("screenshot_url") or "") or {}
                v["screenshot"] = shot.get("path")
                v["title_box"] = shot.get("title_box")
                v["domain"] = domain(v.get("screenshot_url") or "")
            visuals.append(v)
        segments.append({"index": i, "headline": s["headline"], "studentTake": s["student_take"], "bridge": s.get("bridge", ""), "icon": topic_icon(s),
                         "sourceLabel": "Kaynak: " + ", ".join(dict.fromkeys(domain(u) for u in s["sources"])),
                         "visuals": visuals})
    outro = next(u for u in timeline["units"] if u["id"] == "outro")
    total_s = max(timeline["duration"], outro["start"] + vcfg["outro_seconds"])
    fps = vcfg["fps"]
    write_json(ep / "render_props.json", {
        "week": week, "fps": fps, "durationInFrames": int(round(total_s * fps)),
        "voice": "audio/voice.wav", "music": "media/bed.mp3", "whoosh": "media/whoosh.mp3", "pop": "media/pop.mp3",
        "logo": logo, "hook": script["hook"], "outroText": script["outro"], "outroSeconds": vcfg["outro_seconds"],
        "teaser": script.get("teaser", ""), "question": script.get("question", ""), "handle": vcfg.get("instagram_handle", ""),
        "units": timeline["units"], "segments": segments,
        "musicVolume": vcfg["music_volume"], "duckVolume": vcfg["music_duck_volume"],
    })
    print(f"[assets] {len(shots)}/{len(shot_urls)} ekran görüntüsü, {total_s:.1f} sn → render_props.json")


def render(week: str, force: bool = False) -> None:
    require_approval(week)
    ep = episode_dir(week)
    final, thumb = ep / "final.mp4", ep / "thumbnail.png"
    if final.exists() and thumb.exists() and not force:
        print("[render] final.mp4 var, atlanıyor (--force ile yeniden render)")
        return
    if not (VIDEO_DIR / "node_modules").exists():
        subprocess.run([NPX.replace("npx", "npm"), "ci"], cwd=VIDEO_DIR, check=True)
    props = ep / "render_props.json"
    raw = ep / "render_raw.mp4"
    # --gl=angle: three.js (3D kanca/rakamlar) başsız Chromium'da WebGL ister
    common = ["--props", str(props), "--public-dir", str(ep), "--gl=angle"]
    subprocess.run([NPX, "remotion", "render", "src/index.ts", "Episode", str(raw), *common,
                    "--concurrency", "50%"], cwd=VIDEO_DIR, check=True)
    subprocess.run([NPX, "remotion", "still", "src/index.ts", "Thumbnail", str(thumb), *common], cwd=VIDEO_DIR, check=True)
    # Platformlar için hedef ses yüksekliği (-14 LUFS); video yeniden kodlanmaz
    lufs = settings()["tts"]["target_lufs"]
    subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(raw), "-c:v", "copy",
                    "-af", f"loudnorm=I={lufs}:TP=-1.5:LRA=11", "-c:a", "aac", "-b:a", "192k", "-ar", "48000",
                    "-movflags", "+faststart", str(final)], check=True)
    raw.unlink()
    print(f"[render] {final.relative_to(ROOT)} ve thumbnail.png hazır")


HASHTAGS = "#teknoloji #yapayzeka #yazılım #üniversite #GDG #GDGonCampus #Kastamonu #developer #haftalıkgündem"


def package(week: str, force: bool = False) -> None:
    require_approval(week)
    ep = episode_dir(week)
    script = read_json(ep / "script.json")["script"]
    ver = read_json(ep / "verification.json")
    timeline = read_json(ep / "timeline.json")
    checks = {(c["segment"], c["claim_index"]): c["verdict"] for c in ver["checks"]}

    sources = []
    for i, s in enumerate(script["segments"], 1):
        for u in s["sources"]:
            claims = [{"text": c["text"], "uncertain": c["uncertain"], "verdict": checks.get((i, j), "not_checked")}
                      for j, c in enumerate(s["claims"]) if c["source_url"] == u]
            sources.append({"segment": i, "headline": s["headline"], "url": u, "domain": domain(u), "claims": claims})
    write_json(ep / "sources.json", {"week": week, "sources": sources})

    # Yayın yalnızca Instagram Reels: açıklamadaki linkler tıklanamaz, kaynaklar alan adıyla yazılır
    caption = [script["hook"], ""]
    caption += [f"{i}. {s['headline']}" for i, s in enumerate(script["segments"], 1)]
    if script.get("question"):
        caption += ["", f"💬 {script['question']}"]
    caption += ["", "Kaynaklar: " + ", ".join(dict.fromkeys(domain(u) for s in script["segments"] for u in s["sources"]))
                + " (tam linkler bio'daki bağlantıda)",
                "Etkinliklerimiz ve kayıt linki bio'da.", ""]
    if timeline.get("caption_credit"):  # ör. ElevenLabs ücretsiz planı açıklamada atıf istiyor
        caption += [timeline["caption_credit"], ""]
    caption += [HASHTAGS]
    # "AI ile üretildi" bilgisi videoya yazılmaz; Instagram'ın kendi AI etiketiyle verilir (ekip kararı 2026-10-28)
    lines = [f"# GDG on Campus Kastamonu — Haftalık Teknoloji Gündemi ({week})", "",
             "## Yükleme kontrol listesi", "",
             "- [ ] Instagram'da paylaşmadan önce: Gelişmiş ayarlar → **\"AI etiketi ekle\"** anahtarını aç (zorunlu).",
             "- [ ] Kapak olarak thumbnail.png'yi seç.", "",
             "## Instagram Reels açıklaması (kopyala-yapıştır)", "", *caption, "",
             "## Tam kaynak listesi (bio linkine / hikâyeye)", ""]
    lines += [f"- {s['headline']}: {u}" for s in script["segments"] for u in s["sources"]]
    lines += ["", "## Üretim notu (iç kullanım)", "",
              "Haberler otomatik toplandı, senaryo Claude ile yazıldı ve kaynaklarla karşılaştırıldı, seslendirme yapay zeka sesidir.",
              timeline["license_note"], "Video: Remotion ile üretildi. Müzik ve efektler: ekip tarafından sentezlendi (telifsiz).", ""]
    (ep / "post.md").write_text("\n".join(lines), encoding="utf-8")
    print("[package] post.md ve sources.json hazır")
