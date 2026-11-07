"""Adım 2 — senaryo: en yüksek puanlı adayların kaynak metinlerini çek, Claude ile 3-4 haberlik senaryo (config: episode.min_items/max_items) yaz.

Kaynak metinleri episodes/<week>/sources/<hash>.txt olarak saklanır; doğrulama adımı aynı metinleri kullanır.
Çıktı: script.json (Script şeması + meta).
"""
from __future__ import annotations

from concurrent.futures import ThreadPoolExecutor

from collector.fetch import fetch_article_text
from common.config import episode_dir, read_json, settings, url_key, write_json
from common.llm import LLMError, ask
from writer.schema import Script, word_count


def source_text(ep, url: str) -> str:
    """Kaynak metni diskten, yoksa web'den (ve diske yazar)."""
    path = ep / "sources" / f"{url_key(url)}.txt"
    if path.exists():
        return path.read_text(encoding="utf-8")
    try:
        text = fetch_article_text(url)
    except Exception as e:  # noqa: BLE001
        text = ""
        print(f"  ! kaynak metni alınamadı: {url} ({type(e).__name__})")
    path.parent.mkdir(exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return text


SYSTEM = """Sen GDG on Campus Kastamonu'nun haftalık, yapay zekâyla üretilen 80-105 saniyelik dikey teknoloji gündemi videosunun senaristisin.
Kitle: Türkiye'deki üniversite öğrencileri. Ton: enerjik ama abartısız, samimi "sen" dili, haber spikeri netliği. Tıklama tuzağı yok.

Görev: Verilen aday haberlerden {min_items}-{max_items} tanesini seç ve senaryoyu şemaya uygun üret.

Seçim:
- Öğrencinin işine yarayan (başvuru, ücretsiz araç, yarışma, açık kaynak sürüm) haberleri öne al; konu çeşitliliği gözet (hepsi aynı şirketten olmasın).
- Kaynak metni boş veya çok kısa olan haberi seçme.

KESİN KURALLAR (ihlal edilirse bölüm yayınlanmaz):
1. Kaynak metinlerde geçmeyen HİÇBİR rakam, isim, tarih, sürüm numarası veya özellik kullanma. Yuvarlama yapma; sayıyı kaynaktaki gibi ver.
2. Anlatımdaki ve "student_take"teki her olgusal ifadeyi `claims` listesine yaz ve kaynağını `source_url` ile bağla. source_url, o segmentin `sources` listesinde olmalı.
3. Kaynağın açıkça söylemediği, çıkarım/yorum içeren her iddiayı `uncertain: true` yap. Emin değilsen kullanma ya da uncertain işaretle.
4. student_take somut olsun: kaynakta bir başvuru tarihi, ücretsiz erişim, indirilebilir araç varsa onu söyle; yoksa genel ama doğru bir öneri ver (ör. "dokümanı incele", "projende dene") ve tarih/rakam uydurma.
5. Uzunluk: seslendirilen her şeyin (hook, teaser, bridge'ler, narration'lar, student_take'ler, question, outro) toplamı {min_words}-{max_words} kelime (Türkçe ~{wps} kelime/sn). Haber başına narration ~20-26 kelime, student_take ~8-12 kelime; kısa ve vurucu tut.
6. Metinlerde rakamları rakamla, İngilizce terimleri orijinal yazımıyla yaz (OpenAI, GPU, %12). Seslendirme için ayrı bir normalizasyon adımı var.
7. Şirket logosu veya gerçek kişi fotoğrafı isteme; görselleri yalnızca şemadaki component'lerle tarif et.

Akış ve izleyiciyi tutma (Instagram Reels; ilk 3 saniye ve "sona kadar izlenme" belirleyici):
- Sıra: en çarpıcı haber ilk sırada (hook onu anlatır), öğrencinin en çok işine yarayan haber EN SONDA.
- hook: haftanın en çarpıcı gelişmesi, tek cümle, en fazla 8 kelime; "Merhaba"yla veya "Bu hafta"yla başlama. Soru ya da şaşırtıcı bir olgu olabilir.
- teaser: hook'tan hemen sonra, en fazla 12 kelime. Kaç haber olduğunu ve sondaki haberin izleyiciyi doğrudan ilgilendirdiğini ima ederek merak boşluğu aç (ör. "Dört haber var; sonuncusu doğrudan senin bilgisayarını ilgilendiriyor."). Sonda gerçekten karşılığı olmalı; tıklama tuzağı yok.
- bridge: her haberin önünde, en fazla 7 kelime. Önceki haberden bir sonrakine anlamlı bir köprü kur ya da izleyiciye seslen ("Güvenlik demişken, asıl risk telefonunda.", "Şimdi sıra söz verdiğim habere."). Klişe "İkinci haberimiz..." kullanma. İlk haberin bridge'i boş olabilir. Son haberin bridge'i teaser'daki sözü hatırlatsın.
- narration içinde de kısa cümleler; her habere bir "neden önemli" anı koy.
- question: kapanıştan önce izleyiciye yorumda cevaplayacağı, kişisel ve kolay bir soru (en fazla 10 kelime; ör. "Sen Siri'yi Türkçe kullanır mıydın? Yorumlara yaz.").
- outro: en fazla 8 kelime, takip çağrısı (ör. "Takip et, haftaya yeni gündemle buradayız.").
- teaser, bridge, question ve outro YENİ olgu (rakam, isim, tarih) içermez; yalnızca segmentlerde geçen bilgilere atıf yapar.

Görseller (her segmentte 2-4, ilk görsel HeadlineCard):
- StatCounter: kaynakta çarpıcı tek bir sayı varsa.
- MiniChart: kaynakta karşılaştırılabilir en az 2 sayı varsa (ör. eski/yeni performans).
- CodeBlock / Terminal: geliştirici haberlerinde kaynaktaki kod/komut veya resmi kurulum komutu varsa (uydurma API çağrısı yazma).
- SourceScreenshot: duyuru sayfasının ekran görüntüsü; screenshot_url = ana kaynak URL. Her segmentte bir tane olması iyi."""


def run(week: str, force: bool = False, feedback: str | None = None) -> None:
    ep = episode_dir(week)
    out = ep / "script.json"
    if out.exists() and not force and not feedback:
        print("[write] script.json var, atlanıyor (--force veya --feedback ile yeniden yaz)")
        return
    cfg, ecfg = settings()["collector"], settings()["episode"]
    candidates = read_json(ep / "candidates.json")["candidates"][: cfg["shortlist"]]

    with ThreadPoolExecutor(max_workers=6) as pool:
        texts = list(pool.map(lambda c: source_text(ep, c["url"]), candidates))

    blocks = []
    for c, text in zip(candidates, texts):
        also = ", ".join(a["url"] for a in c.get("also_reported_by", []))
        blocks.append(
            f"<haber id=\"{c['id']}\" puan=\"{c['score']}\" kaynak=\"{c['source']}\" tarih=\"{(c['date'] or '')[:10]}\">\n"
            f"Başlık: {c['title']}\nURL: {c['url']}\n" + (f"Diğer kaynaklar: {also}\n" if also else "")
            + f"Özet: {c['summary_tr']}\n<kaynak_metni>\n{text or '(metin alınamadı)'}\n</kaynak_metni>\n</haber>"
        )
    system = SYSTEM.format(min_items=ecfg["min_items"], max_items=ecfg["max_items"], min_words=ecfg["min_words"],
                           max_words=ecfg["max_words"], wps=ecfg["words_per_second"])
    user = f"Hafta: {week}\n\n" + "\n\n".join(blocks)
    if feedback:
        prev = read_json(out)["script"] if out.exists() else None
        user += f"\n\nÖNCEKİ SENARYO:\n{prev}\n\nEDİTÖR GERİ BİLDİRİMİ (buna göre düzelt):\n{feedback}"

    task = ep / "llm" / ("revise" if feedback else "write")
    script = ask(system, user, Script, task=task, max_tokens=32000)
    n, problems = word_count(script), validate(script, ecfg)
    if problems and settings()["llm"].get("mode") == "api":
        # API modunda bir kez düzeltme istenir; claude_code modunda yanıt dosyası doğrudan düzeltilir
        user += f"\n\nÖnceki denemen şu kuralları ihlal etti, düzelt: {'; '.join(problems)}"
        script = ask(system, user, Script, task=task, max_tokens=32000)
        n, problems = word_count(script), validate(script, ecfg)
    if problems:
        raise LLMError(f"Senaryo kurallara uymadı ({task.name}.response.json'ı düzeltin): {'; '.join(problems)}")

    write_json(out, {"week": week, "word_count": n,
                     "est_seconds": round(n / ecfg["words_per_second"], 1),
                     "candidate_ids": [c["id"] for c in candidates],
                     "script": script.model_dump()})
    print(f"[write] {len(script.segments)} haber, {n} kelime (~{n / ecfg['words_per_second']:.0f} sn) → script.json")


def validate(script: Script, ecfg: dict) -> list[str]:
    problems = []
    n = word_count(script)
    if not ecfg["min_words"] <= n <= ecfg["max_words"]:
        problems.append(f"toplam {n} kelime, {ecfg['min_words']}-{ecfg['max_words']} olmalı")
    if not ecfg["min_items"] <= len(script.segments) <= ecfg["max_items"]:
        problems.append(f"{len(script.segments)} haber, {ecfg['min_items']}-{ecfg['max_items']} olmalı")
    for name, text, limit in [("hook", script.hook, 9), ("teaser", script.teaser, 13), ("question", script.question, 11),
                              ("outro", script.outro, 9)] + [(f"haber {i} bridge", s.bridge, 8) for i, s in enumerate(script.segments, 1)]:
        if len(text.split()) > limit:
            problems.append(f"{name} {len(text.split())} kelime, en fazla {limit - 1}")
    if not script.teaser or not script.question:
        problems.append("teaser ve question boş olamaz")
    for i, s in enumerate(script.segments, 1):
        if not s.sources:
            problems.append(f"haber {i} kaynaksız")
        orphan = [c.text for c in s.claims if c.source_url not in s.sources]
        if orphan:
            problems.append(f"haber {i}: kaynak listesinde olmayan URL'ye bağlı iddia: {orphan[:2]}")
        if not s.visuals or s.visuals[0].component != "HeadlineCard":
            problems.append(f"haber {i}: ilk görsel HeadlineCard olmalı")
    return problems
