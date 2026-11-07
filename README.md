# GDG on Campus Kastamonu — AI ile Haftalık Teknoloji Gündemi

> **Ar-Ge ekibi:** Kurulumdan haftalık üretime, API anahtarlarından kararların gerekçesine kadar her şey
> [`docs/ARGE_DEVIR_REHBERI.md`](docs/ARGE_DEVIR_REHBERI.md)'de.

Her hafta ~90–105 saniyelik, 4 haberli, dikey (1080×1920, 30 fps), Türkçe bir teknoloji gündemi videosu üreten pipeline.
Haber toplama, senaryo, doğrulama, seslendirme ve video otomatik. **Yayından önce bir insan onayı zorunlu.**

```
collect → write → normalize → verify → review ║ ONAY ║ → tts → assets → render → package
(haber)  (Claude) (fonetik)  (Claude)  (html)        (ses)  (görsel) (Remotion) (post.md)
```

---

## Her hafta: Claude Code ile

Üretim bu repoda açılan bir Claude Code oturumundan yapılır. Ayrı bir Anthropic API anahtarı gerekmez.
Claude Code'a şunu yazmanız yeterli:

> Bu haftanın bölümünü hazırla (2026-W44)

Claude Code [`CLAUDE.md`](CLAUDE.md)'deki adımları izler:
1. Pipeline'ı çalıştırır.
2. Haber puanlama, senaryo ve doğrulama adımlarını kendisi yapar. Bu adımların istemleri ve yanıtları `episodes/<hafta>/llm/` altında saklanır.
3. **Onay sayfasında durur.**

Siz `review.html`'i inceleyip "onaylıyorum" dediğinizde seslendirme ve videoyu tamamlar.

Otomatik/zamanlanmış çalıştırma için `config/pipeline.yaml` → `llm.mode: api` yapıp `.env`'e `ANTHROPIC_API_KEY` ekleyebilirsiniz. O modda Claude adımları doğrudan API ile çalışır.

## Elle: 3 komut

```bash
make episode WEEK=2026-W44      # 1) haberleri topla, senaryoyu yaz, doğrula → onay sayfasında durur
make approve WEEK=2026-W44      # 2) episodes/2026-W44/review.html'i inceledikten sonra onayla
make episode WEEK=2026-W44      # 3) seslendirme + video: final.mp4, thumbnail.png, post.md, sources.json
```

`make` yoksa (Windows'ta varsayılan olarak yok) aynı komutlar:

```bash
.venv/Scripts/python -m pipeline episode --week 2026-W44
.venv/Scripts/python -m pipeline approve --week 2026-W44
.venv/Scripts/python -m pipeline episode --week 2026-W44
```

`WEEK` verilmezse içinde bulunulan ISO hafta kullanılır. Hafta numarasını öğrenmek için: `python -c "import datetime;print(datetime.date.today().isocalendar())"`.

### Onay sayfasında neye bakılır?

`episodes/<hafta>/review.html` dosyasını tarayıcıda açın:

- **Kırmızı satırlar:** `uncertain` işaretli iddialar, kaynakta bulunamayan ya da kaynakla çelişen iddialar.
- **Rakam taraması:** Senaryodaki her rakamın kaynak metinde birebir geçip geçmediği.
- **Sözlükte olmayan terimler:** Yanlış okunabilecek İngilizce kelimeler ve kısaltmalar. Bkz. "Sözlüğe terim ekleme".
- **TTS'e gidecek fonetik metin:** "TTS'e gidecek fonetik metin" başlığına tıklayınca açılır.

Kırmızı işaret varken onay vermek bilinçli bir karar olmalı: `make approve WEEK=... FLAGS=1` (`--accept-flags`).
Düzeltme istemek için senaryoyu geri bildirimle yeniden yazdırın. Bu komut doğrulamayı ve onay sayfasını da yeniler:

```bash
make revise WEEK=2026-W44 FEEDBACK="2. haberi çıkar, yerine TÜBİTAK duyurusunu koy"
```

**Onay kapısı:** Onaydan sonra `script.json` veya `normalized.json` değişirse TTS ve render çalışmaz, yeniden onay gerekir. Onay, bu iki dosyanın özetiyle (`approval.json`) kayıt altına alınır.

---

## Kurulum (bir kez)

Gereksinimler: Python 3.12, Node.js 20+, ffmpeg, [uv](https://docs.astral.sh/uv/). Önerilen: NVIDIA GPU (6 GB yeterli). GPU yoksa TTS ve Whisper CPU'da da çalışır, sadece daha yavaştır.

```bash
make setup            # veya aşağıdaki adımlar
```

```bash
uv venv .venv --python 3.12
uv pip install -p .venv -r requirements.txt
uv pip install -p .venv torch torchaudio --index-url https://download.pytorch.org/whl/cu128 --reinstall-package torch --reinstall-package torchaudio
.venv/Scripts/python -m playwright install chromium-headless-shell   # ekran görüntüleri için
cd video && npm ci && cd ..
cp .env.example .env                                     # yalnızca llm.mode: api için gerekli
```

Seslendirme modeli (Pocket TTS Turkish) kendi ortamında çalışır:

```bash
uv venv research/.venvs/pocket --python 3.12
uv pip install -p research/.venvs/pocket pocket-tts-turkish pocket-tts soundfile
uv pip install -p research/.venvs/pocket torch --index-url https://download.pytorch.org/whl/cu128 --reinstall-package torch
```

İlk çalıştırmada modeller indirilir: Pocket TTS Turkish (~0,44 GB) ve Whisper large-v3 (~3 GB, kelime zamanları için).

---

## Adımlar ve ara çıktılar

Her adım tek başına çalışır: `make <adım> WEEK=...` veya `python -m pipeline <adım> --week ...`.
Çıktısı olan adım yeniden çalıştırılmaz. Yeniden üretmek için `FORCE=1` (`--force`) ekleyin.
Bir adım bozulursa yalnızca o adımı tekrarlayın; öncekiler diskte durur.

| Adım | Ne yapar | Çıktı (`episodes/<hafta>/`) |
|---|---|---|
| `collect` | `config/sources.yaml`'daki RSS ve sayfalardan son 7 günü çeker, tekrarları birleştirir, Claude ile öğrenci ilgisi puanı verir | `raw_items.json`, `candidates.json` |
| `write` | En iyi 12 adayın kaynak metnini indirir, Claude ile 3–4 haberlik senaryo yazar (Pydantic şemasıyla doğrulanır) | `sources/*.txt`, `script.json` |
| `normalize` | Rakam, tarih, para, yüzde ve sürüm numaralarını yazıya döker, terimleri sözlükle fonetiğe çevirir | `normalized.json` |
| `verify` | İkinci Claude çağrısı her iddiayı kaynak metinle karşılaştırır; ayrıca rakam taraması yapar | `verification.json` |
| `review` | Onay sayfasını üretir | `review.html` |
| `approve` | Onay kaydı | `approval.json` |
| `tts` | Her paragrafı tek parça seslendirir (doğal tonlama), ses yüksekliğini ayarlar, Whisper ile kelime zamanlarını çıkarır | `audio/voice.wav`, `timeline.json` |
| `assets` | Kaynak sayfaların ekran görüntülerini alır, müzik/efektleri kopyalar | `screenshots/`, `media/`, `render_props.json` |
| `render` | Remotion ile videoyu üretir, sesi -14 LUFS'a ayarlar | `final.mp4`, `thumbnail.png` |
| `package` | Platform açıklaması ve kaynak listesi | `post.md`, `sources.json` |

Her adımın süresi `timings.json`'a yazılır.

---

## TTS modelini değiştirme

`config/pipeline.yaml`:

```yaml
tts:
  backend: gemini           # ← tek satır: gemini | elevenlabs | pocket_tr | ahenk | ahenk_cep | omnivoice | chatterbox_v3
  voices:                   # haftalık dönüşüm: çift ISO hafta ilk ses, tek hafta ikinci
    gemini: [Kore, Algenib]
    elevenlabs: [Sarah, Brian]
    pocket_tr: [female_1, male_1]
  voice: ""                 # doluysa her hafta bu ses
```

Haftalık kadın/erkek dönüşümü otomatiktir (W44 kadın, W45 erkek, ...). Tek bir haftayı elle değiştirmek için:
`python -m pipeline tts --week 2026-W45 --voice Puck --force`; modeli de değiştirmek için `--backend elevenlabs`.

- **`pocket_tr`** (yerel, GPU): Pocket TTS Turkish (wite-tech), Faz 1 kör testi birincisi. Paragraflar tek parça seslendirilir (doğal tonlama). 2026-10-28'de ekip bu modelle devam etme kararı aldı. CC BY 4.0; atıf satırı `post.md`'ye otomatik eklenir.
- **`ahenk`**: VoxCPM2 + Türkçe LoRA, tek kadın sesi (CC BY 4.0). Ortam: `research/.venvs/ahenk`; ~6 GB VRAM, bölüm başına ~8 dk.
- **`ahenk_cep`**: Ahenk'in 8,6M'lik küçük sürümü; işlemcide de çalışır.
- **`omnivoice`**: Ses tasarımı/klonlama; ağırlıklar CC-BY-NC (yalnızca ticari olmayan yayın). Ortam: `research/.venvs/omnivoice`.
- **`chatterbox_v3`** (yedek): MIT lisanslı. Ayrı bir ortam gerekir (torch 2.6'ya sabit). `research/eval/ENVIRONMENTS.md`'deki kurulumu yapın, sonra:
  ```yaml
  tts:
    backend: chatterbox_v3
    python: research/.venvs/chatterbox/Scripts/python
    voice: research/reference/ref.wav      # Türkçe referans kayıt (10-20 sn)
  ```
- **`gemini`** (varsayılan, model `gemini-3.1-flash-tts-preview`) / **`elevenlabs`** (yedek, model `eleven_v3`): 2026-10-28 ekip dinlemesinde yerel modellerden belirgin şekilde doğal bulundu. Bütün bölüm tek istekte okunur, birimler kelime zamanlarından ayrılır. GPU gerekmez, ses insan seslendirmesine çok daha yakın. Anahtar `.env`'e (`ELEVENLABS_API_KEY`, `GEMINI_API_KEY`; bkz. `.env.example`), `python: ""` bırakın. Bu iki model metnin orijinal yazımını okur (fonetik yazım kullanılmaz). `voices` ses adlarıdır: ElevenLabs'te hesabınızdaki ses adı (ör. `Sarah`), Gemini'de hazır ses (ör. `Kore`, `Puck`). Gemini'de `emotion` okuma tarzı talimatıdır. Ücretsiz planlar: Gemini günde model başına 10 istek (bölüm 1 istek); ElevenLabs ayda ~10 bin karakter (bölüm ~1.500), ticari olmayan kullanım ve açıklamada atıf (post.md'ye otomatik eklenir).
- **Yeni model eklemek:** `tts/backends.py`'de `TTSBackend`'den türeyen bir sınıf yazın (`load`, `synth`) ve `BACKENDS`'e ekleyin.

Modelin seçilme gerekçesi ve ölçümler: [`research/tts_report.md`](research/tts_report.md).

## Sözlüğe terim ekleme

`config/pronunciation.json` → `terms`. Anahtar ekranda görünen yazım, değer okunuş:

```json
"Kubernetes": "kubernetis",
"WWDC": "dabılyu dabılyu di si"
```

- Önce büyük/küçük harf duyarlı aranır, sonra duyarsız. Ekler otomatik eklenir (`GPU'da` → `ci pi yuda`).
- Harf harf okunan kısaltmalarda heceleri **boşlukla** ayırın. Tire kullanmayın: Faz 1'de tireli hecelerin bazen yutulduğu görüldü.
- Çok kelimeli terimler desteklenir (`"Hugging Face": "haging feys"`).
- Ekledikten sonra: `make normalize WEEK=... FORCE=1`. Onay sayfası yeniden üretilir ve **yeniden onay** gerekir.
- `review.html`'in sonundaki "Sözlükte olmayan terimler" bölümü, kopyalanıp düzeltilecek hazır satırlar verir.

## Haber kaynağı ekleme

`config/sources.yaml`:

```yaml
- {name: Kaynak Adı, url: "https://.../feed.xml", lang: tr, weight: 1.2}   # RSS
- name: Duyuru Sayfası                                                      # RSS yoksa
  type: html
  url: "https://ornek.org/duyurular/"
  link_pattern: '^/duyurular/[a-z0-9-]+/$'
  base: "https://ornek.org"
```

`weight` 1'den büyükse kaynağın haberleri puanlamada hafif öne çıkar.

## Video

`video/` bir Remotion projesidir. Bileşenler `video/src/components/` altında, her biri props ile beslenir:
Hook (3D sayı), SegmentIntro, KeywordPunch, StatCounter (3D sayı), MiniChart, CodeBlock/Terminal, SourceScreenshot, StudentTakeCard, KineticCaptions, Agenda, QuestionCTA, FollowOutro, ProgressBar, Logo. Tema: krem kâğıt zemin + çıkartma kartlar (`theme.ts`); 3D yalnızca kancada ve büyük sayılarda (`ThreeD.tsx`, render `--gl=angle` ister).

Önizleme: `cd video && npx remotion studio`. Gerçek bir bölümle önizlemek için Studio'da props alanına `episodes/<hafta>/render_props.json` içeriğini yapıştırın ve public klasörü olarak bölüm klasörünü verin: `npx remotion studio --public-dir ../episodes/<hafta>`.

GDG logosu: `assets/brand/gdg_logo_original.jpg`. `python assets/brand/make_dark_logo.py` hem açık zemin (`gdg_logo_light.png`, kullanılan) hem koyu zemin (`gdg_logo.png`) sürümünü üretir; video boyunca sol üstte, kapanışta büyük gösterilir.

## Lisanslar

- **Remotion:** [Remotion Lisansı](https://github.com/remotion-dev/remotion/blob/main/LICENSE.md). Ücretsiz lisans, bireyler, en fazla 3 çalışanı olan şirketler ve **kâr amacı gütmeyen kuruluşlar** için geçerli (2026-10-27'de doğrulandı). GDG on Campus Kastamonu kâr amacı gütmeyen bir öğrenci topluluğu olduğu için ücretsiz lisans kapsamında. Kâr amaçlı bir kuruluş bu repoyu kullanacaksa Company License gerekebilir. Remotion 5.0'da lisansın değişeceği duyuruldu; sürüm yükseltmeden önce tekrar kontrol edin.
- **Seslendirme modeli:** Pocket TTS Turkish (wite-tech), CC BY 4.0; atıf `post.md`'de.
- **Müzik ve efektler:** Ekip tarafından sentezlendi. Bkz. [`assets/LICENSES.md`](assets/LICENSES.md).
- **Claude API:** Senaryo (`claude-opus-5-5`). Anahtar `.env`'de durur, repoya girmez.

## Görsel ve içerik kuralları

- Konuşan insan avatarı ve sunucu figürü yok; kanalın görsel kimliği sol üstteki GDG Kastamonu logosu. Sunucunun adı yok.
- Şirket logoları ve gerçek kişi fotoğrafları kullanılmaz. Kaynak ekran görüntülerinde sayfadaki tüm görseller bulanıklaştırılır.
- Yapay zeka bilgisi Instagram'ın kendi "AI etiketi" ile verilir (paylaşırken açılır; post.md kontrol listesinde zorunlu madde). Videoda rozet yoktur.
- Kaynakta olmayan rakam, isim veya tarih kullanılmaz. Doğrulama adımı bunu kontrol eder, son kararı onaylayan kişi verir.

## Klasörler

```
config/       pipeline.yaml, sources.yaml, pronunciation.json
collector/    haber toplama          writer/    senaryo (Claude) + şema
normalizer/   fonetik metin          review/    doğrulama + onay sayfası + kapı
tts/          seslendirme adaptörü   media/     ekran görüntüsü, render, paketleme
video/        Remotion projesi       assets/    müzik, efekt, marka, lisanslar
pipeline/     komut satırı           research/  Faz 1 TTS araştırması
episodes/<hafta>/   her bölümün tüm ara ve son çıktıları
```
