# Ar-Ge Devir Rehberi: Haftalık Teknoloji Gündemi Videosu

> **Bu belge kimin için?** GDG on Campus Kastamonu Ar-Ge departmanı için. Haftalık videoyu artık siz, kendi bilgisayarınızda,
> kendi Claude Code hesabınız ve kendi API anahtarlarınızla üreteceksiniz.
>
> **Claude Code'a not:** Bu dosyayı okuyan Claude Code oturumu, projeyi kuran önceki oturumun devamı gibi çalışmalı.
> Aşağıdaki kararlar ekip içinde tartışılıp verildi. Gerekçeleri "Karar günlüğü" bölümünde. Kullanıcı açıkça istemedikçe bu kararları
> yeniden tartışma, değiştirme. Kullanıcının sana söylediği her şey bu belgenin önüne geçer.
>
> Son güncelleme: 2026-11-07 · Son üretilen bölüm: **2026-W45**

---

## İçindekiler

1. [Bu proje ne yapıyor?](#1-bu-proje-ne-yapıyor)
2. [İlk gün: kurulum (bir kez)](#2-ilk-gün-kurulum-bir-kez)
3. [API anahtarları: Gemini ve (isteğe bağlı) ElevenLabs](#3-api-anahtarları)
4. [Claude Code ile çalışma şekli](#4-claude-code-ile-çalışma-şekli)
5. [Her hafta: adım adım bölüm üretimi](#5-her-hafta-adım-adım-bölüm-üretimi)
6. [İçerik: haberler nereden geliyor, nasıl seçiliyor?](#6-içerik-haberler-nereden-geliyor-nasıl-seçiliyor)
7. [Senaryo kuralları](#7-senaryo-kuralları)
8. [Doğrulama ve onay kapısı](#8-doğrulama-ve-onay-kapısı)
9. [Ses (TTS)](#9-ses-tts)
10. [Görsel stil (video)](#10-görsel-stil-video)
11. [Instagram'da paylaşma](#11-instagramda-paylaşma)
12. [Sık karşılaşılan sorunlar ve çözümleri](#12-sık-karşılaşılan-sorunlar-ve-çözümleri)
13. [Karar günlüğü (neden böyle?)](#13-karar-günlüğü-neden-böyle)
14. [Açık işler ve fikirler](#14-açık-işler-ve-fikirler)
15. [Dosya haritası](#15-dosya-haritası)
16. [Claude Code'a ilk mesaj (kopyala-yapıştır)](#16-claude-codea-ilk-mesaj-kopyala-yapıştır)

---

## 1. Bu proje ne yapıyor?

Her hafta Instagram Reels için **dikey (1080×1920, 30 fps), Türkçe, ~90-105 saniyelik** bir teknoloji gündemi videosu üretir.
Kitle Türkiye'deki üniversite öğrencileri. İçerik bilgisayar, yazılım ve mühendislik ağırlıklı.

```
collect → write → normalize → verify → review ║ ONAY ║ → tts → assets → render → package
(haber)  (Claude) (fonetik)  (Claude)  (html)  (insan) (ses)  (görsel) (Remotion) (post.md)
```

- **Haber toplama, puanlama, senaryo ve doğrulama otomatik.** Claude adımlarını, bu repoda açtığınız Claude Code oturumu yapar
  (`config/pipeline.yaml` → `llm.mode: claude_code`). Anthropic API anahtarı **gerekmez**.
- **Yayından önce bir insan onayı zorunlu.** Pipeline onay sayfasında durur. Bir ekip üyesi okuyup "onaylıyorum" demeden ses ve video üretilmez.
- **Çıktılar** (`episodes/<hafta>/`):
  - `final.mp4`: Instagram'a yüklenecek video
  - `thumbnail.png`: kapak
  - `post.md`: açıklama metni ve yükleme kontrol listesi
  - `sources.json`: kaynaklar ve doğrulama sonuçları
- **Yayın:** Yalnızca Instagram Reels. Gelir yok, ticari değil. Bu yüzden ücretsiz planlar ve ticari olmayan lisanslar kabul edilebilir.

Bölüm yapısı (her hafta aynı):

| Sıra | Bölüm | Ne söyler |
|---|---|---|
| 1 | **Kanca** (hook) | Haftanın en çarpıcı gelişmesi, ≤8 kelime. İlk 3 saniye kaydırıp geçmeyi önler. |
| 2 | **Teaser** | "Dört haber var; sonuncusu …" ile sona kadar izletecek merak. ≤12 kelime. |
| 3-6 | **4 haber** | Her biri: köprü cümlesi (≤7 kelime) → anlatım (~20-26 kelime) → "Senin için ne demek?" notu (~8-12 kelime) |
| 7 | **Yorum sorusu** | İzleyicinin yorumda cevaplayacağı kolay, kişisel bir soru. ≤10 kelime. |
| 8 | **Kapanış** | Takip çağrısı. ≤8 kelime. Ekranda "Takip et" butonuna dokunma animasyonu. |

Haber sırası: **en çarpıcı haber başta, öğrencinin en çok işine yarayan haber (başvuru, burs, yarışma) en sonda.** Teaser o son habere işaret eder.

---

## 2. İlk gün: kurulum (bir kez)

### 2.1 Gereken programlar

| Program | Sürüm | Not |
|---|---|---|
| Windows 10/11 | — | Proje Windows'ta geliştirildi. macOS/Linux'ta da çalışır (komutlarda `.venv/Scripts/python` yerine `.venv/bin/python`). |
| Python | **3.12** | 3.13 denenmedi. |
| [uv](https://docs.astral.sh/uv/) | güncel | Sanal ortam ve paket kurulumu için. |
| Node.js | 20+ | Remotion için. Geliştirmede v26 kullanıldı. |
| ffmpeg | güncel | `PATH`'te olmalı (`ffmpeg -version` çalışmalı). Windows için gyan.dev "full build". |
| Git | — | Repo paylaşımı için. |
| Claude Code | — | Kendi hesabınızla. |

**Ekran kartı:** Gerekmez. Kelime zamanlarını çıkaran Whisper, NVIDIA GPU varsa onu, yoksa işlemciyi kullanır. İşlemcide yalnızca biraz yavaştır.
Ses Gemini'de (bulutta) üretildiği için GPU'ya ihtiyaç yok.

### 2.2 Repoyu almak

Repo şu an Ar-Ge'ye devredecek kişinin bilgisayarında. Önerilen yol: GDG hesabı altında **özel (private) bir GitHub reposuna** gönderilsin, Ar-Ge üyeleri collaborator olarak eklensin.

- `.gitignore` zaten `.env` dosyasını, sanal ortamları, `node_modules`'ü ve büyük medya dosyalarını (`*.mp4`, `*.wav`, ekran görüntüleri) dışarıda bırakıyor.
- **`.env` dosyasını asla paylaşmayın, repoya koymayın.** İçinde API anahtarları var. Herkes kendi anahtarını kendi `.env`'ine yazar.

### 2.3 Kurulum komutları

Repo klasöründe (PowerShell ya da Git Bash):

```bash
uv venv .venv --python 3.12
uv pip install -p .venv -r requirements.txt
.venv/Scripts/python -m playwright install chromium-headless-shell   # kaynak sayfa ekran görüntüleri için
cd video && npm ci && cd ..
cp .env.example .env                                                  # sonra anahtarları içine yazın (bölüm 3)
```

İlk çalıştırmada Whisper large-v3 modeli (~3 GB) bir kez indirilir. Kelime zamanlarını, yani altyazı senkronunu bu model çıkarır.

> `requirements.txt` içindeki `nvidia-cublas-cu12`, `nvidia-cudnn-cu12` paketleri GPU'su olmayan makinede de sorunsuz kurulur, sadece yer kaplar.
> `pocket-tts-turkish` paketi eski yerel ses modelinden kaldı. Yedek olarak duruyor, kullanılmıyor.

### 2.4 Kurulumu test etmek

```bash
.venv/Scripts/python -c "from tts.backends import BACKENDS; print(list(BACKENDS))"
ffmpeg -version
cd video && npx tsc --noEmit -p . && cd ..
```

Hata yoksa kurulum tamam. Gerçek bir uçtan uca test için bölüm 5'teki akışı bir hafta için çalıştırın.

---

## 3. API anahtarları

Anahtarlar **yalnızca** repo kökündeki `.env` dosyasına yazılır. `.env.example` şablondur.

```dotenv
GEMINI_API_KEY=...          # zorunlu (ses)
ELEVENLABS_API_KEY=         # isteğe bağlı (yedek ses)
ANTHROPIC_API_KEY=          # gerekmez (yalnızca llm.mode: api için)
HF_TOKEN=                   # gerekmez
```

> **Güvenlik kuralı:** Anahtarı Claude Code sohbetine, Discord'a, WhatsApp'a yapıştırmayın. Doğrudan `.env`'e yazın.
> Önceki ekip bu kuralı ihlal etti. Eski anahtarlar sohbet geçmişinde kaldığı için iptal edilmeli (bkz. bölüm 14).

### 3.1 Gemini API anahtarı (zorunlu, ücretsiz)

Ses Google'ın **Gemini TTS** modeliyle üretiliyor: `gemini-3.1-flash-tts-preview`.

1. https://aistudio.google.com/apikey adresine GDG'nin (ya da kendi) Google hesabınızla girin.
2. **"Create API key"** → bir Google Cloud projesi seçin ya da yeni proje oluşturun.
3. Anahtarı kopyalayıp `.env`'deki `GEMINI_API_KEY=` satırına yapıştırın.
   Anahtar `AIza…` ya da `AQ.…` ile başlayabilir, ikisi de çalışır.
4. Test:
   ```bash
   .venv/Scripts/python -c "import os,requests;from common.config import load_env;load_env();r=requests.post('https://generativelanguage.googleapis.com/v1beta/models/gemini-3.1-flash-tts-preview:generateContent',headers={'x-goog-api-key':os.environ['GEMINI_API_KEY']},json={'contents':[{'parts':[{'text':'Merhaba'}]}],'generationConfig':{'responseModalities':['AUDIO']}},timeout=60);print(r.status_code)"
   ```
   `200` görmelisiniz. Bu test günlük kotadan 1 istek harcar.

**Ücretsiz katman sınırı (önemli):** Gemini TTS ücretsiz katmanda **model başına günde ~10 istek** veriyor. 2026-10-28'de ölçüldü: `limit: 10, GenerateRequestsPerDayPerProjectPerModel-FreeTier`.
- Bir bölüm **~6 istek** harcar: giriş, 4 haber ve kapanış ayrı ayrı okunur.
- Seslendirme dosyaları önbelleğe alınır (`episodes/<hafta>/audio/sentences/`). Metin değişmedikçe `tts --force` yeni istek **atmaz**.
- Senaryoyu değiştirip yeniden seslendirirseniz yalnızca değişen parçalar yeniden istenir.
- Kota dolarsa `429 … retry in XXh` hatası gelir. Kod 429'da birkaç kez bekleyip dener, günlük kota dolduysa ertesi güne kalır.
  Kota Google'ın Pasifik saatine göre sıfırlanır, Türkiye'de öğleden sonra.
- Aynı gün ses denemesi yapacaksanız (farklı sesleri dinlemek gibi) kotayı bölüm için ayırın.

### 3.2 ElevenLabs anahtarı (isteğe bağlı, yedek ses)

Gemini çalışmazsa ya da kota dolarsa yedek. Kalitesi çok iyi ama ücretsiz kotası küçük.

1. https://elevenlabs.io → ücretsiz hesap → **Profile → API Keys → Create**.
2. **İzinler:** En azından **Text to Speech** açık olmalı. "Voices: Read" izni de verirseniz hesabınızdaki seslerin listesi okunur, vermezseniz kodda tanımlı hazır sesler kullanılır.
3. Anahtarı oluştururken **bir kez** gösterilir ve `sk_…` ile başlar. Listede görünen 64 karakterlik **"Key ID" anahtar değildir**; önceki ekip bu hatayı yaptı.
4. `.env` → `ELEVENLABS_API_KEY=sk_...`
5. Ücretsiz plan: **ayda ~10.000 karakter**. Bir bölüm ~1.500 karakter, yani ayda en fazla ~5 bölüm.
   Ticari olmayan kullanıma izin var, **açıklamada atıf zorunlu**. Bu sesi kullanırsanız `post.md`'ye "🎙️ Ses: elevenlabs.io" satırı otomatik eklenir.
6. Kullanmak için bir haftalık: `.venv/Scripts/python -m pipeline tts --week <hafta> --backend elevenlabs --voice Sarah --force`
   Beğenilen sesler: kadın **Sarah**, erkek **Brian** (model `eleven_v3`).

### 3.3 Claude: anahtar gerekmez

`llm.mode: claude_code` modunda puanlama, senaryo ve doğrulama adımlarını **sizin Claude Code oturumunuz** yapar. Ayrıntılar bölüm 4'te.
Tam otomatik çalıştırmak isterseniz (zamanlanmış görev gibi) `llm.mode: api` yapıp `.env`'e `ANTHROPIC_API_KEY` eklenebilir. Bu ücretlidir ve şu an kullanılmıyor.

---

## 4. Claude Code ile çalışma şekli

Repo kökünde Claude Code'u açın. `CLAUDE.md` her oturumda otomatik okunur, temel kurallar orada. Bu rehber ayrıntılı versiyonu.

**Claude Code'a yazmanız gereken tek cümle:**

> Bu haftanın bölümünü hazırla (2026-W46)

Hafta numarası ISO haftasıdır. Öğrenmek için: `python -c "import datetime;print(datetime.date.today().isocalendar())"`.
Hafta vermezseniz içinde bulunulan hafta kullanılır.

**Arka planda olan:** Claude Code `.venv/Scripts/python -m pipeline episode --week <hafta>` komutunu çalıştırır ve çıkış koduna göre devam eder:

| Çıkış kodu | Anlamı | Claude Code ne yapar |
|---|---|---|
| `4` | Bir Claude görevi bekleniyor | `episodes/<hafta>/llm/<görev>.prompt.md`'yi okur, yanıtı aynı klasöre `<görev>.response.json` olarak istemin sonundaki JSON şemasına uygun yazar, komutu tekrar çalıştırır. Görevler sırayla: `score` → `write` → `verify`. |
| `3` | **Onay kapısı** | `episodes/<hafta>/review.html`'i size gösterir ve **durur**. Onayı asla kendisi vermez. |
| `0` | Bölüm hazır | `final.mp4`, `thumbnail.png`, `post.md`, `sources.json` üretildi. |

**`verify` görevi bağımsız bir alt ajana verilir.** Claude kendi yazdığı senaryoyu doğrularsa taraflı olur. Bu yüzden doğrulamayı bağlamı temiz bir alt ajan (subagent) yapar: her iddia için kaynaktan birebir alıntı arar. Claude Code'a "doğrulamayı bağımsız bir alt ajana ver" demenize gerek yok, `CLAUDE.md`'de yazıyor.

**İstem ve yanıt dosyaları:** `episodes/<hafta>/llm/` altında saklanır.
- Senaryo yeniden yazılınca eski yanıt `*.response.stale.json` olarak kenara alınır. Böylece yeni isteme eski yanıt yanlışlıkla eşleşmez.
- Bir adımı baştan yaptırmak için: `.venv/Scripts/python -m pipeline <adım> --week <hafta> --force`

---

## 5. Her hafta: adım adım bölüm üretimi

### 5.1 Önerilen haftalık takvim

| Gün | İş |
|---|---|
| Çarşamba / Perşembe | Claude Code'a "bu haftanın bölümünü hazırla" de. Toplama, puanlama, senaryo ve doğrulama ~15-20 dk sürer. |
| Perşembe | Bir ekip üyesi `review.html`'i okur, düzeltme ister ya da onaylar. |
| Perşembe | Onaydan sonra ses ve video ~10-15 dk. Telefon sürümünü izleyin. |
| **Cuma** | Instagram'da paylaşım (bölüm 11). |

Haberde son başvuru tarihi varsa (burs, yarışma), videoyu o tarihten **birkaç gün önce** yayınlayın.

### 5.2 Akış

1. **Başlat:** Claude Code'a "Bu haftanın bölümünü hazırla (2026-Wxx)" yaz.
2. **Toplama (`collect`):** `config/sources.yaml`'daki ~18 kaynaktan son 7 günün haberleri çekilir. Tekrarlar birleştirilir.
   W45'te 241 haber çekildi, tekrarlar elendikten sonra 131 aday kaldı.
3. **Puanlama (`score`, Claude):** Her aday 0-10 puanlanır (ölçüt: bölüm 6.2). En iyi 12 aday senaryoya gider.
4. **Senaryo (`write`, Claude):**
   - 12 adayın kaynak metinleri indirilir, Claude 4 haber seçip senaryoyu yazar.
   - Kurallar bölüm 7'de. Kaynak metni çekilemeyen haber, `(metin alınamadı)`, **seçilmez**.
5. **Fonetik (`normalize`):**
   - Rakamlar, tarihler ve yüzdeler yazıya çevrilir.
   - İngilizce terimler `config/pronunciation.json` sözlüğüyle okunuşa çevrilir.
   - Sözlükte olmayan terim çıkarsa Claude Code sözlüğe ekler ve `normalize --force` çalıştırır.
6. **Doğrulama (`verify`, bağımsız alt ajan):** Her iddia kaynakla karşılaştırılır (bölüm 8).
7. **Onay sayfası (`review`):**
   - `review.html` açılır.
   - **Siz okursunuz.** Düzeltme isterseniz Claude Code'a söyleyin; senaryoyu düzeltir, yeniden doğrulatır, yeni onay sayfası çıkarır.
8. **Onay:** "Onaylıyorum" dersiniz. Claude Code `approve` çalıştırır.
   Kırmızı işaret varsa ve bilerek geçiyorsanız `--accept-flags` ile.
9. **Ses (`tts`):** Gemini bölümü 6 parçada okur. Whisper ile kelime zamanları çıkarılır, parçalar birleştirilir.
10. **Görseller (`assets`):** Kaynak sayfaların ekran görüntüleri alınır. Sayfadaki tüm görseller bulanıklaştırılır, çerez bantları gizlenir.
11. **Render (`render`):** Remotion ile `final.mp4` ve `thumbnail.png` üretilir. ~8-10 dk, 3D sahneler yüzünden.
12. **Paket (`package`):** `post.md` ve `sources.json` üretilir.
13. **Kontrol:** Videoyu telefonda izleyin. Claude Code'dan 720p telefon sürümü isteyebilirsiniz:
    `ffmpeg -i final.mp4 -vf scale=720:-2 -crf 28 telefon_720p.mp4`

### 5.3 Elle çalıştırmak (Claude Code olmadan, sadece adım tekrarı için)

```bash
.venv/Scripts/python -m pipeline episode  --week 2026-W46          # durduğu yere kadar ilerler
.venv/Scripts/python -m pipeline approve  --week 2026-W46          # insan onayından sonra
.venv/Scripts/python -m pipeline tts      --week 2026-W46 --force  # tek adım tekrar
.venv/Scripts/python -m pipeline render   --week 2026-W46 --force
```

Her adım tek başına çalışır. Çıktısı varsa atlanır, `--force` ile yeniden üretilir.

---

## 6. İçerik: haberler nereden geliyor, nasıl seçiliyor?

### 6.1 Kaynaklar (`config/sources.yaml`)

| Grup | Kaynaklar |
|---|---|
| Google / Android / Chrome | Google Blog, Google Developers Blog, Android Developers Blog, Chrome for Developers, Chromium Blog |
| Geliştirici platformları | GitHub Blog, Hugging Face Blog, Cloudflare Blog |
| Yapay zeka laboratuvarları | OpenAI News, Google DeepMind, Anthropic News (RSS'i yok, sayfadan çekilir) |
| Topluluk | Hacker News (100+ puan) |
| Türkçe teknoloji | Webrazzi, Webtekno, ShiftDelete.Net, DonanımHaber |
| Öğrenci fırsatları | TÜBİTAK Duyuruları, TEKNOFEST Duyuruları (sayfadan) |

`weight` 1'den büyükse kaynak puanlamada hafif öne çıkar. TÜBİTAK ve TEKNOFEST 1.3 ile en yüksek; öğrenci fırsatları önceliklidir.

**Kaynak eklemek:**

```yaml
- {name: Kaynak Adı, url: "https://.../feed.xml", lang: tr, weight: 1.2}   # RSS varsa
- name: Duyuru Sayfası                                                      # RSS yoksa
  type: html
  url: "https://ornek.org/duyurular/"
  link_pattern: '^/duyurular/[a-z0-9-]+/$'
  base: "https://ornek.org"
  lang: tr
```

Eklemeye değer adaylar (henüz eklenmedi): üniversitenin kendi duyuruları, YÖK/ÖSYM duyuruları, Google for Startups / GDG etkinlik sayfaları, Microsoft/AWS öğrenci programları, burs ilanı siteleri.

### 6.2 Puanlama ölçütü (Claude'a verilen talimatın özeti)

- **8-10:** Öğrencinin **bu hafta bir şey yapabileceği** haberler (başvuru, ücretsiz araç/kota, yarışma, staj, açık kaynak sürüm) ya da sektörü belirgin değiştiren büyük duyurular.
- **5-7:** Geliştiricilerin bilmesi gereken önemli ürün/teknoloji haberleri.
- **0-4:** Tüketici ürün incelemesi, kampanya, magazin, yatırım/borsa, otomobil, tekrar eden ya da belirsiz haber.
- Google / Android / Gemini geliştirici haberlerine **hafif** öncelik, çünkü kitle GDG. Önemsizi şişirme.

### 6.3 Haber seçerken ekibin tercihleri (deneyimle öğrenildi)

- Ekip **fazla teknik / niş haberi sevmiyor.** W45'te "kodlama ajanları eski TODO yorumlarına takılıyor" haberi "gereksiz" bulunup çıkarıldı.
  "Öğrenci bunu duyunca bir şey yapar mı, merak eder mi?" sorusunu sor.
- Konu çeşitliliği: dört haberin hepsi aynı şirketten olmasın.
- İyi çalışan karışım: **1 çarpıcı / gündem**, **1-2 "dene" haberi** (ücretsiz araç, yeni özellik), **1 fırsat** (burs, yarışma, okul, başvuru) **en sonda**.
- Örnek iyi bölüm (W45):
  1. Google Vids'te ayda 3 ücretsiz yapay zeka videosu
  2. Gemini ile kâğıttaki çizimi uygulamaya çevirmek
  3. GitHub Game Off oyun yarışması
  4. TÜBİTAK STAR lisans bursu, son başvuru tarihiyle

---

## 7. Senaryo kuralları

Kesin kurallar `writer/run.py` → `SYSTEM` isteminde. İhlal edilirse bölüm yayınlanmaz:

1. **Kaynak metinde olmayan hiçbir rakam, isim, tarih, sürüm ya da özellik yok.** Yuvarlama yok.
2. Anlatımdaki her olgusal ifade `claims` listesine, kaynağıyla birlikte yazılır.
3. Kaynağın açıkça söylemediği, çıkarım içeren iddia `uncertain: true` olur ya da hiç kullanılmaz.
4. "Senin için ne demek?" notu somut bir öneri olur, tarih ya da rakam uydurmaz.
5. Uzunluk: seslendirilen her şeyin toplamı **155-195 kelime**, yani ~1,9 kelime/sn ile 80-105 sn.
6. Rakamlar rakamla, İngilizce terimler orijinal yazımıyla yazılır (seslendirme için ayrı normalizasyon var).
7. Teaser, köprü cümleleri, soru ve kapanış **yeni olgu içermez.** Yalnızca haberlerde geçen bilgilere atıf yapar.

**Üslup:**
- Samimi "sen" dili, enerjik ama abartısız. Tıklama tuzağı yok.
- Kanca "Merhaba" ya da "Bu hafta" ile başlamaz.
- Klişe "İkinci haberimiz…" yerine anlamlı köprüler kurulur: "Kod demişken, bu ay oyun yapsana.", "Ve sona sakladığımız burs geldi."

**Seslendirmede sorun çıkaran kelimeler (deneyimle):**
- **"bedava":** Gemini tuhaf okudu. Yerine **"ücretsiz"** kullan.
- **Kısaltmalar:**
  - Harf harf okunan İngilizce kısaltmalar (PHP, CTF, API…) `config/pronunciation.json`'da olmalı. Yoksa Gemini Türkçe harflerle okur ("PHP" → "pehepe").
  - Sözlükteki ASCII kısaltmalar için sese otomatik olarak fonetik yazım gider, altyazıda orijinal yazım kalır.
  - Harf harf okunanlarda heceleri boşlukla ayır: `"PHP": "pi eyç pi"`. Tire kullanma.
- **Sayı + ek:** "Genie 4'ü" → "dördü" gibi ünsüz yumuşaması normalizer'da var. Yeni bir garip okuma duyarsanız sözlüğe ya da `normalizer/core.py`'ye ekleyin.

---

## 8. Doğrulama ve onay kapısı

### 8.1 Doğrulama (`verify`)

- Bağımsız alt ajan her iddia için kaynak metinden **birebir alıntı** arar: `supported` / `partial` / `not_found` / `contradicted`.
- Kanca, teaser, köprüler, soru ve kapanış da kontrol edilir: yeni olgu var mı, teaser'ın vaadi tutuluyor mu?
- Otomatik **rakam taraması:** senaryodaki her rakam kaynak metinde geçiyor mu?
- Doğrulama sonucu, senaryo dosyasının özetine (hash) bağlıdır. Senaryo değişince doğrulama otomatik olarak yeniden istenir.

**Bilinen yanlış alarm:** Rakam taraması, kaynakta yazıyla geçen sayıyı ("three") bulamaz ve kırmızı işaret verir.
W45'teki tek kırmızı işaret buydu: "3 video", kaynakta "up to three". Bu durumda alıntıyı kontrol edip `--accept-flags` ile bilerek onaylayın.

### 8.2 Onay sayfası (`review.html`): neye bakılır?

- **Kırmızı satırlar:** `uncertain` iddialar, kaynakta bulunamayan ya da çelişen iddialar.
- **Rakam taraması.**
- **Sözlükte olmayan terimler:** yanlış okunabilecek kelimeler.
- Senaryonun tamamı ve her haberin kaynak linki.

### 8.3 Kurallar

- **Onayı yalnızca insan verir.** Claude Code `approve` komutunu ancak kullanıcı açıkça "onaylıyorum" dediğinde çalıştırır.
  Bir butona tıklamak, stil seçmek ya da "A + B karışık" gibi başka bir cevap onay değildir. Önceki oturumda bu ayrım bilerek korundu.
- Onaydan sonra `script.json` ya da `normalized.json` değişirse ses ve render çalışmaz, **yeniden onay** gerekir.
  Sözlüğe terim eklemek de normalizasyonu değiştirir, yani yeniden onay ister.

---

## 9. Ses (TTS)

### 9.1 Güncel ayar

`config/pipeline.yaml` → `tts`:

```yaml
backend: gemini
gemini_model: gemini-3.1-flash-tts-preview
voices:
  gemini: [Kore, Algenib]     # çift ISO hafta Kore (kadın), tek hafta Algenib (erkek)
voice_styles:
  Algenib: "… tok, güven veren ve ciddiye alınan bir haber anlatıcısı gibi oku …"
```

| Hafta | Ses | Karakter |
|---|---|---|
| Çift (W46, W48…) | **Kore** | Kadın, net, enerjik Reels anlatıcısı. Varsayılan tarz: "arkadaşına anlatır gibi". |
| Tek (W47, W49…) | **Algenib** | Kalın, tok erkek sesi. "Ciddi haber anlatıcısı" tarzıyla (2026-11-07'de dinlenip seçildi). |

- Tek bir haftanın sesini değiştirmek için: `… tts --week <hafta> --voice Charon --force`
- Her hafta aynı sesi kullanmak için `voices.gemini` listesine tek ses yazın.
- Denenip **beğenilmeyen** sesler: **Fenrir** (erkek, "erkek sesi olmasın" denmesine yol açtı), Puck. Charon ve Orus fena değildi; Leda yedek kadın sesi.

### 9.2 Nasıl çalışıyor?

- Bölüm **6 parçada** okunur: giriş (kanca + teaser), her haber (köprü + anlatım + not) ve kapanış (soru + takip).
  Tüm bölümü tek istekte okutmak sonlara doğru sesi robotikleştiriyordu; cümle cümle okutmak ise tonlamayı bozuyordu.
- Gemini'ye orijinal yazım gider ("Google DeepMind", "1071"). Sözlükteki kısaltmalar fonetik yazımla gider.
- Whisper, üretilen sesi yazıya döker ve kelime zamanlarını çıkarır. Altyazı ve sahne zamanlaması buna göre kurulur.
- Haberler arasına kısa "nefes" sessizliği eklenir. **Kesim noktası kelime zamanına göre değil, sesteki gerçek sessizliğe göre seçilir.**
  Eski yöntem kelimenin sonunu bölüp "ücretsi… z" gibi bir kasma yaratıyordu, 2026-11-07'de düzeltildi.
- Ses yüksekliği -16 LUFS'a, müzikle karıştıktan sonra final -14 LUFS'a ayarlanır.

### 9.3 Ses denemesi yapmak (yeni ses seçmek)

Gemini'nin 30 hazır sesi var. Kalın erkek sesi arıyorsanız: Algenib, Charon, Orus, Alnilam, Rasalgethi. Kadın sesi: Kore, Leda, Aoede, Despina.
Karşılaştırma örnekleri `research/ses_karsilastirma/` klasöründe.

Deneme için Claude Code'dan isteyin, örneğin: "W45 açılışını Rasalgethi ve Alnilam ile okut, mp3 olarak ver". Her deneme 1 istek harcar.

### 9.4 Yedekler

| Backend | Ne zaman | Not |
|---|---|---|
| `elevenlabs` | Gemini kotası dolarsa | Bölüm 3.2. Atıf otomatik. |
| `pocket_tr` | İnternet/kota yoksa | Yerel model, ayrı ortam (`research/.venvs/pocket`). Ekip "robotik" buldu, son çare. |

---

## 10. Görsel stil (video)

`video/` bir **Remotion 4** projesi (React). Bileşenler `video/src/components/` altında.

### 10.1 Stil kararları (2026-11-07)

- **Editoryal / "kâğıt" tema:**
  - krem kâğıt dokulu zemin (`#F3EEE4`), siyah mürekkep yazı
  - kalın siyah çerçeve ve **sert (bulanıksız) ofset gölgeli** "çıkartma" kartlar
  - Google renkleri düz vurgu olarak
- **Neden:** Eski koyu zemin, neon parlama ve cam kartlar, ilk yapay zeka sitelerinin "cyberpunk" görünümüne benziyordu; video şablon gibi duruyordu.
- **3D (three.js, `@remotion/three`) yalnızca iki yerde:**
  - **kanca:** kancadaki sayı parlak 3D rakam olarak döner, etrafında Google renklerinde şekiller yüzer
  - **büyük sayılar:** `StatCounter`
  - Her sahnede 3D olursa o da şablon gibi durur. Bu sınırı koruyun.
- Altyazıda önemli kelimeler **fosforlu kalemle altı çizilmiş** gibi görünür. Parlama yok.
- **Tempo:**
  - Anlatımda önemli kelimeler (önce rakamlar) ekrana büyük "kelime kartı" olarak çarpar (`KeywordPunch`), böylece görüntü 2-3 saniyede bir değişir.
  - Ekran görüntüleri önce haber başlığına yakınlaşır (telefonda okunsun diye), sonra aşağı kayar.
  - Her haber girişinde konu ikonu var: kilit, bayrak, küre, takvim… Haber metninden otomatik seçilir (`media/run.py` → `ICON_RULES`).
- **Logo:** koyu yazılı GDG logosu (`assets/brand/gdg_logo_light.png`), sol üstte sabit, kapanışta büyük.

### 10.2 Değişmez kurallar

- **Şirket logosu yok, gerçek kişi fotoğrafı yok.** Ekran görüntülerindeki tüm görseller ve SVG'ler bulanıklaştırılır.
- **Konuşan avatar ya da sunucu figürü yok**, sunucunun adı yok.
- **"AI ile üretildi" rozeti videoda yok.** Yapay zeka bilgisi Instagram'ın kendi **AI etiketiyle** verilir (bölüm 11).

### 10.3 Önizleme ve stil denemesi

```bash
cd video
npx remotion studio --public-dir ../episodes/2026-W45     # props alanına episodes/2026-W45/render_props.json içeriğini yapıştırın
npx remotion still src/index.ts Episode kare.png --props ../episodes/2026-W45/render_props.json --public-dir ../episodes/2026-W45 --frame 120 --scale 0.4 --gl=angle
```

`--gl=angle` zorunlu: 3D sahneler başsız tarayıcıda WebGL ister. `media/run.py` bunu render'a kendisi ekliyor.
Stil denemesi için `video/src/preview/StylePreview.tsx`'teki kompozisyonlara bakın (`StyleAHook`, `StyleBHook`…).

**Değişiklik yaptıktan sonra:** `npx tsc --noEmit -p .` ile tip kontrolü yapın, birkaç kare `still` alıp görsel olarak kontrol edin, sonra tam render alın.

---

## 11. Instagram'da paylaşma

`post.md`'nin en üstünde kontrol listesi var:

- [ ] **Gelişmiş ayarlar → "AI etiketi ekle" anahtarını aç (zorunlu).** Videoda rozet olmadığı için tek yapay zeka bildirimi bu.
- [ ] Kapak olarak `thumbnail.png`'yi seç.
- [ ] "Instagram Reels açıklaması" bölümünü kopyalayıp yapıştır. Kaynaklar alan adıyla yazılıdır; tam linkler `post.md`'nin altındaki listede.
  Bunları bio linkine ya da hikâyeye koyun, Reels açıklamasında linkler tıklanmaz.
- [ ] ElevenLabs sesi kullanıldıysa açıklamada "🎙️ Ses: elevenlabs.io" satırı olmalı (otomatik eklenir, silmeyin).
- [ ] Videoda başvuru tarihi varsa yayını o tarihten birkaç gün önce yap.

İsteğe bağlı: `config/pipeline.yaml` → `video.instagram_handle` doldurulursa (ör. `"@gdgkastamonu"`) kapanışta gösterilir.

---

## 12. Sık karşılaşılan sorunlar ve çözümleri

Hepsi gerçekten yaşandı:

| Belirti | Sebep | Çözüm |
|---|---|---|
| `assets` adımı `Executable doesn't exist … chrome-headless-shell` hatası verir | Playwright tarayıcısı silinmiş (disk temizliği `%LOCALAPPDATA%\ms-playwright`'ı siliyor) | `.venv/Scripts/python -m playwright install chromium-headless-shell` |
| Render `You passed --props but it was neither valid JSON…` der | Asıl sorun önceki adımda: `assets` başarısız olduğu için `render_props.json` yok | `assets` hatasını çöz, sırayla tekrar çalıştır |
| Gemini `429 … quota … retry in 13h` | Günlük ücretsiz kota (model başına ~10 istek) doldu | Ertesi gün tekrar, ya da o hafta ElevenLabs. Önbellekteki parçalar tekrar istek atmaz. |
| ElevenLabs `api_key_id_used_as_api_key` | "Key ID" girilmiş | Yeni anahtar oluştur, `sk_…` ile başlayanı kopyala |
| ElevenLabs `missing the permission voices_read` | Anahtar kısıtlı | Sorun değil, kod hazır ses listesine düşer. Sadece Text to Speech izni yeterli. |
| ElevenLabs `voice_not_found` | O hazır ses hesabınızda yok (ör. Liam) | Sarah, Jessica, Brian, Chris gibi çalışan seslerden birini seçin |
| Ses "PHP"yi "pehepe" diye okur | Kısaltma sözlükte yok | `config/pronunciation.json`'a ekle, `normalize --force`, yeniden onay |
| Sahne geçişlerinde ses kasıyor ("ücretsi… z") | Eski kesim yöntemi kelime sonunu bölüyordu | 2026-11-07'de düzeltildi (kesim gerçek sessizliğe). Tekrar olursa `tts/run.py` → `_quiet_cut`. |
| Ekran görüntüsü bembeyaz | Site `<body>`'ye "cookie" sınıfı ekliyor (tubitak.gov.tr) ya da sayfa geç çiziliyor | Çerez gizleme kuralı html/body'yi hariç tutuyor. Boş görüntü 3 kez yeniden deneniyor. Yine boşsa o görüntü atlanır. |
| `deepmind.google` ekran görüntüsü hep `Error` | Site otomatik tarayıcıyı engelliyor | Çözülmedi. O haberin başka kaynağının (blog.google) görüntüsü kullanılıyor. |
| Kelime kartında "1.2" → "12" ya da "17.30" → "1730" | Eski noktalama temizliği | Düzeltildi (`Motion.tsx` → `core`). |
| Onay sayfasında "kaynakta bulunmayan rakam: 3" | Kaynakta sayı yazıyla ("three") | Yanlış alarm. Kontrol et, `--accept-flags`. |
| Doğrulama eski senaryonun sonucunu gösteriyor | Eski bir hata (önbellek kelime sayısına bakıyordu) | Düzeltildi: doğrulama senaryo hash'ine bağlı. Şüphedeysen `verify --force`. |
| Windows'ta `FileExistsError … .stale.json` | Eski bir hata | Düzeltildi (`common/llm.py`). |
| Konsolda Türkçe karakterler bozuk ya da `UnicodeEncodeError` | Windows konsol kodlaması | Komutlardan önce `PYTHONIOENCODING=utf-8` (Git Bash: `export PYTHONIOENCODING=utf-8`) |
| Video üretimi (Flow/Veo) "zararlı içerik politikası" ile reddeder | İstemde "tehditkâr", "masaya vurur" gibi ifadeler ya da gerçekçi böcek yakın çekimi | Sahneyi "lighthearted cartoon comedy" diye tarif et, sert kelimeleri çıkar |

---

## 13. Karar günlüğü (neden böyle?)

| Tarih | Karar | Gerekçe |
|---|---|---|
| 2026-10-27 | Pipeline Python + Remotion, Claude adımları Claude Code'da (`llm.mode: claude_code`) | Ayrı API anahtarı/ücreti yok. Her adım tek başına tekrarlanabilir. |
| 2026-10-27 | Yayından önce zorunlu insan onayı | Yanlış bilgi yayınlamak topluluğa zarar verir. |
| 2026-10-27 | Şirket logosu yok, gerçek kişi fotoğrafı yok, konuşan avatar yok, sunucu adı yok | Telif/kişilik hakkı riski ve "yapay zeka sunucu" yapaylığı |
| 2026-10-27 → 10-28 | Yerel TTS modelleri denendi (Pocket TTS Turkish, Ahenk, Chatterbox…) | GPU 6 GB, ücretsiz olsun istendi. Kör testte Pocket önde ama ekip "robotik" buldu. |
| 2026-10-28 | Bölüm akışı: kanca → teaser ("sona sakladık") → köprü cümleli haberler → yorum sorusu → takip | Reels'te izlenme süresi ve etkileşim için |
| 2026-10-28 | Bulut sese geçiş: Gemini (varsayılan), ElevenLabs (yedek) | Instagram'da tutan videolar insan gibi ses kullanıyor, yerel modeller yetmedi. "Ücretsiz olması önemli." |
| 2026-10-28 | "AI ile üretildi" rozeti videodan kaldırıldı, yerine Instagram AI etiketi | Rozet "çok AI duruyordu". Bildirim Instagram'ın kendi özelliğiyle yapılıyor. |
| 2026-10-28 | Bölüm 4 haber (önce 3'tü), ~80-105 sn | Ekip isteği |
| 2026-10-29 | Tempo: açılış ikon/3D, kelime kartları, okunur ekran görüntüleri, haber ikonları | Video "bir şey eksik" hissi veriyordu. Teşhis: ilk 3 sn boş, aynı görüntü 10-15 sn sabit. |
| 2026-11-07 | Erkek ses Fenrir reddedildi → önce sadece Kore, sonra **Kore/Algenib dönüşümü** | Fenrir beğenilmedi; Algenib "kalın, tok, ciddiye alınır" diye seçildi. |
| 2026-11-07 | Ses 6 parçada okunuyor, kesimler sessizliğe | Tek istek sonlara doğru robotikleşiyordu; geçişlerde kasma vardı. |
| 2026-11-07 | Görsel tema: editoryal kâğıt + seçici 3D | Koyu/neon tema yapay zeka şablonu gibi duruyordu. İki yön karşılaştırılıp karışımı seçildi. |
| 2026-11-07 | Hamam böceği meme skeç serisi denendi, **vazgeçildi** | Ekip sarmadı. Ayrıntı bölüm 14'te. |

Daha eski ayrıntılar: `research/tts_report.md` (ses modeli ölçümleri), `assets/LICENSES.md` (lisanslar).

---

## 14. Açık işler ve fikirler

- **Önceki API anahtarlarını iptal edin.** Kurulumu yapan kişinin Gemini ve ElevenLabs anahtarları sohbette açık yazıldı. Ar-Ge kendi anahtarlarını kullanacağı için eskiler AI Studio ve ElevenLabs panellerinden silinmeli.
- **Git:** Repo henüz hiç commit'lenmedi. Devirden önce ilk commit atılıp özel bir GitHub reposuna gönderilmeli (bölüm 2.2).
- **Yeni stile ekip geri bildirimi:** W45 ilk "editoryal + 3D" bölüm. Instagram istatistiklerine (izlenme süresi, tamamlama oranı) bakıp eski koyu temalı W44 ile karşılaştırın.
- **Algenib ilk kez tam bölümde W47'de çalışacak** (tek hafta). Sadece örnek açılışta dinlendi; tam bölümü dinleyip onaylayın.
- **DeepMind ekran görüntüsü** alınamıyor (bölüm 12).
- **Instagram kullanıcı adı** kapanışta gösterilmiyor: `video.instagram_handle` boş.
- **Kapak (`thumbnail.png`)** sade. 3D rakam ya da daha güçlü bir kanca görseli eklenebilir.
- **Yeni kaynak adayları:** bölüm 6.1.
- **Meme skeç fikri (rafta):**
  - Hamam böceği karakter "Buğra" (BUGra), vize haftası esprileri.
  - Flow + Omni 1.2 Flash ile 18 sn'lik klip üretildi, Türkçe diyalog iyi çıktı.
  - Klip `episodes/meme_vize/clip1.mp4`'te.
  - Ekip sarmadı, istenirse tekrar ele alınabilir.

---

## 15. Dosya haritası

```
CLAUDE.md                  Claude Code'un her oturumda okuduğu kısa kurallar
docs/ARGE_DEVIR_REHBERI.md bu belge
README.md                  genel kullanım ve kurulum
config/
  pipeline.yaml            tüm ayarlar (LLM modu, haber sayısı, kelime aralığı, TTS, video)
  sources.yaml             haber kaynakları
  pronunciation.json       okunuş sözlüğü (terim → okunuş)
collector/                 haber toplama (RSS + sayfa), tekrar birleştirme, puanlama görevi
writer/                    senaryo istemi (SYSTEM), şema (schema.py), kurallar (validate)
normalizer/                rakam/tarih/terim → fonetik metin
review/                    doğrulama görevi (verify.py), onay sayfası ve kapı (run.py, template.html)
tts/
  backends.py              ses modelleri (gemini, elevenlabs, pocket_tr, …)
  run.py                   parçalara bölme, sentez, birleştirme, sessizlik kesimi (_quiet_cut, _sections)
  align.py                 Whisper ile kelime zamanları
media/run.py               ekran görüntüleri (Playwright), ikon seçimi, render, post.md
video/src/
  Episode.tsx              bölüm kurgusu (sahnelerin zamanlaması)
  theme.ts                 renkler, editoryal tema yardımcıları (ink, onAccent)
  components/              Hook, Motion (geçiş, altyazı, kelime kartı), Cards, Flow (gündem, soru, takip), ThreeD, Icons
  preview/StylePreview.tsx stil deneme kompozisyonları
assets/                    müzik/efekt (ekip sentezi), marka (logo), lisanslar
episodes/<hafta>/          her bölümün tüm ara ve son çıktıları (llm/ istem-yanıtları, script.json, review.html, final.mp4 …)
research/                  TTS araştırması, ses karşılaştırma örnekleri (ses_karsilastirma/)
```

---

## 16. Claude Code'a ilk mesaj (kopyala-yapıştır)

Repoyu kurup `.env`'e kendi Gemini anahtarınızı yazdıktan sonra, repo klasöründe açtığınız ilk Claude Code oturumuna şunu yapıştırın:

```text
Merhaba. GDG on Campus Kastamonu'nun haftalık teknoloji gündemi videosunu artık Ar-Ge olarak biz üreteceğiz.
Önce docs/ARGE_DEVIR_REHBERI.md dosyasını baştan sona oku; projeyi kuran önceki oturumun devamı gibi çalış,
oradaki kararları ve kuralları koru (insan onayı, kaynak doğrulama, görsel kurallar, ses ayarları).
Sonra kurulumu kontrol et: .venv, playwright tarayıcısı, video/node_modules, ffmpeg ve .env'deki GEMINI_API_KEY
(anahtarın değerini bana yazma, sadece var mı ve çalışıyor mu söyle). Eksik bir şey varsa kurmama yardım et.
Her şey hazırsa bu haftanın bölümünü hazırla.
```

İyi yayınlar! 🎬
