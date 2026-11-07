# TTS Değerlendirme Raporu — Faz 1.3

Tarih: 2026-10-27 · Donanım: RTX 3060 Laptop (6 GB), Ryzen 7 6800H · ASR: Whisper large-v3 (faster-whisper, fp16, `language=tr`, beam 5)
Test seti: [`test_sentences.json`](test_sentences.json), 16 cümle × 2 varyant (`raw`, `phonetic`) · Ortak referans ses: Pocket TTS Turkish `female_1` (CC-BY-4.0, 3.9 sn)

> **Durum: karar verildi (2026-10-27) — Pocket TTS Turkish birincil, Chatterbox V3 yedek.** Gerekçe için bkz. §7 (kör test sonuçları).
> Trendyol-TTS (E) henüz ölçülmedi: Colab'da çalışması gerekiyor ([`eval/colab_voxcpm.ipynb`](eval/colab_voxcpm.ipynb)).

## 1. Metrikler

WER/CER, cümle ortalaması değil, toplam hata / toplam kelime üzerinden hesaplandı. Referans: `normalize(raw)` (rakamlar yazıya, kesme işareti ve noktalama atılır, terim varyantları birleştirilir; bkz. [`eval/textnorm.py`](eval/textnorm.py)). "Terim" sütunu, cümledeki İngilizce/kısaltma terimlerden kaçının Whisper çıktısında tanınabilir olduğunu gösterir.

| Model | Varyant | WER | CER | Terim isabeti | RTF (3060L) | Tepe VRAM | Yükleme |
|---|---|---:|---:|---:|---:|---:|---:|
| **A — Chatterbox Multilingual V3** | phonetic | **4.2%** | **0.7%** | **89%** | 1.15 | 3.4 GB | 224 sn* |
| | raw | 26.7% | 12.1% | 74% | | | |
| **B — Pocket TTS Turkish (wite-tech)** | phonetic | 4.9% | 1.1% | 85% | **0.27** | **0.5 GB** | 37 sn |
| | raw | 12.1% | 4.6% | 63% | | | |
| **C — Pocket TTS TR (kaanhgunay)** | phonetic | 4.9% | 1.5% | 89% | 0.92 (CPU) | — (CPU) | 67 sn |
| | raw | 38.8% | 26.0% | 63% | | | |
| **D — FreyaTTS-small** | phonetic | 26.7% | 13.1% | 59% | 0.26 | 1.5 GB | 156 sn* |
| | raw | 31.5% | 15.8% | 44% | | | |
| E — Trendyol-TTS | — | *Colab'da ölçülecek* | | | | | |

\* İlk çalıştırmadaki indirme süresi dahil. RTF < 1 gerçek zamandan hızlı demek. 90 saniyelik bir bölüm için en yavaş model (A) bile yaklaşık 1 dk 45 sn'de bitiriyor, yani hız seçimde belirleyici değil.
C, `pocket-tts` kütüphanesinin varsayılanıyla **CPU'da** çalıştı (VRAM ölçümü bu yüzden yok). CPU'da gerçek zamana yakın olması, GPU'su olmayan ekip üyeleri için bir artı.

### Zorluk türüne göre WER (cümle ortalaması)

| Model / varyant | İng. terim | Kısaltma (EN) | Kısaltma (TR) | Sürüm no. | Yüzde | Para | Uzun/eklemeli | Tarih |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| A phonetic | 0.02 | 0.03 | 0.19 | 0.00 | 0.00 | 0.00 | 0.05 | 0.08 |
| A raw | 0.29 | 0.29 | 0.34 | 0.41 | 0.36 | 0.41 | 0.00 | 0.36 |
| B phonetic | 0.07 | 0.15 | 0.08 | 0.04 | 0.00 | 0.00 | 0.00 | 0.09 |
| B raw | 0.16 | 0.23 | 0.23 | 0.16 | 0.08 | 0.10 | 0.00 | 0.19 |
| C phonetic | 0.06 | 0.11 | 0.13 | 0.00 | 0.00 | 0.05 | 0.00 | 0.05 |
| C raw | 0.44 | 0.34 | 0.35 | 0.74 | 0.43 | 0.76 | 0.00 | 0.48 |
| D phonetic | 0.31 | 0.23 | 0.08 | 0.11 | 0.11 | 0.44 | 0.51 | 0.39 |

## 2. Raw ve phonetic farkı

- **Fonetik metin her modelde açık ara kazanıyor.** Hata oranı Chatterbox'ta 6×, kaanhgunay modelinde 8×, wite-tech modelinde 2.5× azaldı. Faz 2.4'teki normalizer + telaffuz sözlüğü tasarımını doğruluyor: **`tts_text` olmadan hiçbir model haber metnini güvenilir okuyamıyor.**
- Raw metinde en büyük kayıp **rakam, yüzde, para ve sürüm numaralarında**. Chatterbox ve kaanhgunay bunları yazıya dökemiyor ("%12", "47,3", "3.14" bozuluyor). wite-tech modelinin raw sonucunun nispeten iyi olması, kendi paketindeki sayı normalizasyonundan kaynaklanıyor (bkz. kendi `normalize` komutu). Biz kendi normalizer'ımızı kullanacağımız için bu avantaj pratikte sıfırlanıyor.
- Uzun ve eklemeli Türkçe kelimeler (s10, s11) A, B ve C için sorun değil (WER 0–0.05).
- Fonetik yazımda da kalan hatalar:
  - `el-el-em'ler` (LLM) ve `vi-ram'li` (VRAM): B ve C heceleri bazen yutuyor. Sözlükte bu terimler için tirelerin yerine boşluk (`el el em'ler`) denenmeli.
  - `A-Be-De'li` (ABD'li): A'da "ab deri" olarak çıktı. Türkçe kısaltmalarda Chatterbox'ın en zayıf noktası bu (0.19).

## 3. Ölçüm sınırları (dürüst not)

- **Whisper kaynaklı hatalar** tüm modelleri eşit etkiliyor:
  - Whisper "Klod"u her modelde "cloud" yazıyor. "Claude" terimi bu yüzden hiçbir modelde isabet almıyor.
  - Normalizasyon "2209-A"yı "dokuz a", Whisper'ın çıktısını "dokuza" yapıyor. Bu durum s07'de her modele +%15 WER ekliyor.

  Mutlak değerler bu yüzden biraz kötümser; sıralamayı değiştirmiyor.
- **Referans ses B'nin kendi sesi.** B "klonlama" sırasında kendi eğitim sesini kullanıyor, diğerleri ise 3.9 saniyelik kısa ve sentetik bir referansı taklit ediyor. Bu, B lehine bir yanlılık. Chatterbox'ın kartı da 10 sn civarı referans öneriyor.
- 16 cümle küçük bir örneklem: A, B ve C arasındaki ~%1'lik WER farkı istatistiksel olarak anlamlı değil. Bu üçü anlaşılırlıkta **berabere** sayılmalı.
- **FreyaTTS beklenenden çok kötü çıktı.** Kendi kartında WER %8 diyor, bizde %27. Hatalar saf Türkçe uzun cümlelerde bile var (s11: "öneri sistemlerinin" → "annelerinin"). Freya-TR-Eval kısa konuşma cümlelerinden oluşuyor; haber tipi uzun cümleler modelin eğitim dağılımı dışında kalıyor gibi görünüyor. Ayrıca klonlama da olmadığı için **elendi**.

## 4. Öneri (kör test öncesi)

**1. tercih: Chatterbox Multilingual V3 (A)**
- Fonetik metinde en düşük WER/CER ve en yüksek terim isabeti; İngilizce terim ve rakam alt kümelerinde neredeyse hatasız.
- **Lisans en temiz olanı:** MIT, atıf zorunluluğu yok. Proje olgun (27k yıldız, aktif bakım).
- Klonlama ve `exaggeration` ile enerji ayarı var: "enerjik ama abartısız" haber tonuna ince ayar yapılabilir.
- Dikkat:
  - PyPI sürümü (0.1.7) V3'ü yükleyemiyor; GitHub'dan kurulmalı ve torch 2.6+cu124'e sabitlenmeli.
  - Çıktılarda Perth watermark var. Videoda zaten "AI ile üretildi" rozeti olduğu için uyumlu.
  - 3.4 GB VRAM istiyor; GPU'suz makinede yavaş çalışır.

**Yedek: Pocket TTS Turkish (B)**
- Anlaşılırlıkta A ile berabere. 10× daha az VRAM kullanıyor, 4× daha hızlı ve CPU'da da çalışıyor: GPU'su olmayan ekip üyesi bölüm üretebilir.
- Duygu etiketleri (`mutlu`, `sakin`) haber tonuna uygun.
- Dikkat:
  - CC-BY-4.0, yani **açıklamada atıf zorunlu** (`post.md`'ye otomatik eklenebilir).
  - Model bir aylık, indirme sayısı ~0; eğitim verisi tamamen sentetik.
  - Ses kimliği, hazır 6 sesten biri olmak zorunda değil, klonlanabiliyor.

**C (kaanhgunay)**, B ile aynı anlaşılırlıkta ama kendi kartı İngilizce terimleri desteklemediğini söylüyor ve deposunda belirtilen sürüm etiketi bile yok (yerel düzeltilmiş config ile çalıştı). B'nin gerisinde kalıyor; kör test sonucu çok iyi gelmezse elenecek.

**Nihai karar:** Kör testte A ile B arasında doğallık farkı **0.5 MOS'tan küçükse** pratik avantajları (CPU, hız) nedeniyle B'ye, büyükse kazanana gidilmeli. Trendyol-TTS (E) Colab sonuçları gelirse tabloya eklenip kör teste dahil edilecek.

## 5. Kör test

- Sayfa: [`research/blind_test.html`](blind_test.html) + yanındaki 64 `bt_*.mp3` (toplam 5.5 MB). 4 model × 16 cümle; her modelin daha iyi varyantı (hepsinde `phonetic`) seçildi.
- Klipler -16 LUFS'a eşitlendi; ham çıktıların ses düzeyi farklıydı (A -18.9, B -19.9, C -21.6, D -23.3 LUFS) ve bu fark puanları etkilerdi.
- Model–klip eşlemesi yalnızca `research/results/blind_key.json`'da. **Bu dosyayı dinleyicilere gönderme.**
- Akış: Klasörü (html + mp3'ler) ekibe gönder. Herkes sayfayı açar, puanlar, "JSON indir" der. Gelen dosyalar `research/results/blind_ratings/` altına konur ve `python research/eval/score_blind.py` çalıştırılır.
- 64 klip yaklaşık 12–15 dakika sürer. En az 5 dinleyici öneriyorum.

## 6. Yeniden üretme

Ortam kurulumu ve komutlar: [`eval/ENVIRONMENTS.md`](eval/ENVIRONMENTS.md). Kurulum sırasında karşılaşılan farklar:
- `kaanhgunay/pocket-tts-tr`: kartta geçen `@v0.1-base` etiketi repoda yok; config'in `@main` kopyası `eval/configs/` altında.
- Chatterbox: PyPI 0.1.7 yalnızca V2'yi yüklüyor; V3 için `git+https://github.com/resemble-ai/chatterbox.git` ve `torch==2.6.0` cu124 sürümü gerekiyor.
- FreyaTTS: paket kurulmuyor, `PYTHONPATH=research/.venvs/FreyaTTS-src` ile çalışıyor.
- faster-whisper: PyAV sürüm uyumsuzluğu ve Windows'ta cuBLAS DLL yolu sorunları `asr_eval.py` içinde çözüldü.

## 7. Kör test sonuçları ve nihai karar

1 dinleyici (Mert Yasin Yılmaz), 64 klip. Ham veri: `results/blind_ratings/`, özet: `results/blind_summary.json`.

| Model | MOS (1–5) | ±95% GA | z-skoru | Kazandığı cümle |
|---|---:|---:|---:|---:|
| **B — Pocket TTS Turkish** | **3.88** | 0.62 | +0.90 | 9 / 16 |
| A — Chatterbox V3 | 3.31 | 0.53 | +0.51 | 7 / 16 |
| C — Pocket TTS TR (kaanhgunay) | 2.12 | 0.43 | -0.32 | 0 |
| D — FreyaTTS | 1.00 | 0.00 | -1.10 | 0 |

- Fark 0.57 MOS, yani §4'teki 0.5 eşiğinin üzerinde. Eşik altında da B seçilecekti; iki kural da aynı sonuca çıkıyor.
- Chatterbox'ın düştüğü cümleler: s07 (TÜBİTAK 2209-A, 1 puan), s11, s13 ve s14 (uzun cümleler, 2 puan). Pocket'ın düştüğü cümleler: s08 (`A-Be-De'li`, 1 puan), s01 ve s03 (OpenAI, Anthropic, 2 puan). Pocket'ın zayıf noktası İngilizce terim okunuşları; bu, sözlük düzeltmeleriyle giderilebilecek türden bir hata.

**Nihai karar:**
- **Birincil: Pocket TTS Turkish (`wite-tech/pocket-tts-turkish`).** Lisansı CC-BY-4.0; `post.md`'ye atıf satırı otomatik eklenecek.
- **Yedek: Chatterbox Multilingual V3.** `config` içinde tek satırla geçilebilir.

**Kararın zayıf yanları:**
- Yalnızca 1 dinleyici var. Ekipten 3–4 kişi daha puan verirse karar teyit edilmeli.
- Referans ses B'nin kendi sesiydi (§3), bu B lehine.
- Trendyol-TTS kör teste girmedi.
