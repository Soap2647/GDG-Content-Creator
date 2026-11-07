# TTS Aday Modelleri — Türkçe Haber Sunumu

Doğrulama tarihi: **2026-10-27**. Kaynaklar: Hugging Face model kartları + HF API (`cardData.license`, dosya boyutları), GitHub API (kod lisansı, son push), PyPI.
Donanım hedefi: **RTX 3060 Laptop, 6 GB VRAM** (yerel), sığmayanlar için Colab T4 (16 GB).

> **Lisans kuralı:** Tabloda "Lisans" sütunu **model ağırlıklarının** lisansıdır. Kod lisansı ayrı sütunda. XTTS v2'yi dışarıda bırakma gerekçesiyle tutarlı olarak, ağırlıkları ticari olmayan kullanımla (NC) sınırlı modelleri eledim.

## Değerlendirmeye alınanlar (5)

| # | Model | Ağırlık lisansı | Kod lisansı | Türkçe | Boyut / VRAM | Hız (kart verisi) | Klonlama | Voice design | Notlar |
|---|---|---|---|---|---|---|---|---|---|
| A | **Chatterbox Multilingual V3** (`ResembleAI/chatterbox`, `t3_mtl23ls_v3`) | MIT | MIT | Var (23 dilden biri, genel model) | 0.5B, ~3 GB indirme (V3 dosyaları); VRAM tahmini 3–5 GB | Kartta RTF yok, ölçülecek | Var (zero-shot) | Yok; `exaggeration`/`cfg` ile duygu yoğunluğu | **Çıktılara Perth watermark ekleniyor** (duyulmaz, ama "AI ile üretildi" şeffaflığıyla uyumlu; kaldırmayacağız). PyPI `chatterbox-tts` 0.1.7. Referans kliple aynı dil olmazsa aksan kayması uyarısı var. |
| B | **Pocket TTS Turkish** (`wite-tech/pocket-tts-turkish`) | **CC-BY-4.0** (ticari OK, atıf zorunlu) | Apache-2.0 | Sadece Türkçe | 110M, 440 MB; CPU'da bile gerçek zamanın ~5× hızı | RTF 0.048 (RTX 5090); kart: T1 WER %1.9 | Var (birkaç sn kayıttan) | 6 hazır sentetik ses + 5 duygu etiketi (`mutlu`, `sakin`…) | Eğitim verisi **sentetik** (kendi TTS'leriyle üretilmiş 306 saat). Kendi paketi sayıları yazıya döküyor — biz kendi normalizer'ımızla karşılaştıracağız. Model 2026-09-28'de çıkmış, indirme sayısı ~0: olgunluğu düşük. |
| C | **Pocket TTS TR v0.1-base** (`kaanhgunay/pocket-tts-tr`) | **CC-BY-4.0** | (pocket-tts: MIT) | Sadece Türkçe | 24 katman, 1.34 GB; VRAM tahmini <2 GB | Ölçülecek | Var — **ses referansı zorunlu** (`--voice`) | Yok | 2.724 saatlik gerçek Türkçe sesli kitap verisiyle eğitilmiş. Kart açıkça yazıyor: **İngilizce kelimeler Türkçe okunuyor, code-switching desteklenmiyor** → phonetic sürüm burada kritik. Başta kısa artefakt olabiliyor. Referans ses olarak B'nin CC-BY hazır seslerinden birini kullanacağım. |
| D | **FreyaTTS-small** (`freyavoice/Freya-TTS`) | Apache-2.0 | Apache-2.0 | Sadece Türkçe | 183M, 733 MB; **1.5 GB VRAM** (kart) | RTF ~0.10 (RTX 4090); Freya-TR-Eval WER %8.0 / CER %3.0 | **Yok** (tek konuşmacı) | Yok | 48 kHz çıktı, karakter tabanlı (G2P yok). Ses kimliği sabit — kanal sesi olarak tutarlılık avantajı, değiştirilemezlik dezavantajı. Paket PyPI'da yok, GitHub'dan kurulum. |
| E | **Trendyol-TTS** (`Trendyol/Trendyol-TTS`, VoxCPM2 + Türkçe LoRA, birleştirilmiş) | MIT (taban VoxCPM2: Apache-2.0) | Apache-2.0 (voxcpm) | Türkçe fine-tune | 2B, 5.1 GB; **~8 GB VRAM** → **6 GB'a sığmaz, Colab T4** | VoxCPM2 tabanı RTF ~0.30 (4090); Pocket TTS raporunda T1 WER **%1.1** (en iyi) | VoxCPM2 üzerinden var | VoxCPM2 üzerinden var (parantez içinde tarif) | Kart "araştırma amaçlı, production değil" diyor; 20 saatlik özel veriyle eğitilmiş. Kıyas için temel **VoxCPM2** de aynı runtime'da opsiyonel olarak çalıştırılabilir. |

**Referans (ticari, opsiyonel):** Gemini TTS (Google AI Studio / Cloud TTS). Türkçe desteği ve ücretsiz kota durumu bu araştırmada **net doğrulanamadı**. Gemini API anahtarı verirsen 1 referans sütunu olarak eklerim; asıl seçim açık kaynaktan yapılacak.

## Elenenler ve gerekçeleri

| Model | Neden elendi |
|---|---|
| **OmniVoice** (`k2-fsa/OmniVoice`) | **Ön araştırmadaki "Apache 2.0" bilgisi yanlış.** Kod Apache-2.0, ancak model kartı açıkça yazıyor: *"The pre-trained model is licensed under the CC-BY-NC due to constraints from its training data (e.g., Emilia)."* XTTS v2'yi dışarıda bırakan kuralın aynısı uygulanınca elendi. (Teknik olarak güçlü: 600+ dil, voice design, RTF 0.025, ~3.3 GB.) GDG'nin yayınları ticari değil diye kabul edilse bile, sponsorlu içerik olursa belirsizlik doğar. |
| **KugelAudio-0-open** | Ağırlıklar MIT, Türkçe listede var, ancak **7B parametre / 18.7 GB** → ne 6 GB'a ne T4'e sığar. Kendi kartı da Türkçe dahil "diğer dillerde kalite belirgin şekilde düşük olabilir" uyarısı veriyor (veri ağırlığı de/fr/es/en). |
| **Qwen3-TTS** (resmi 0.6B / 1.7B) | Resmi destek 10 dil (zh, en, ja, ko, de, fr, ru, pt, es, it), **Türkçe yok**. Topluluk LoRA'sı `hcfk/qwen3-tts-turkish` kartında "experimental, yabancı aksan kalabilir" yazıyor, lisans belirtilmemiş. |
| **Higgs TTS 3 (4B)** — 2026 | Türkçe destekli ama lisansı **"research and non-commercial"**. |
| **MOSS-TTS v1.5** — 2026 | Apache-2.0, Türkçe destekli, ancak **17 GB ağırlık** → donanıma sığmaz. Ekip ileride büyük GPU'ya erişirse yeniden bakılabilir. |
| **Fun-CosyVoice3-0.5B**, **sanoTTS** | Türkçe desteği yok (sanoTTS ayrıca GPL-3.0). |
| **Piper Türkçe** (`99eren99/piper-turkish-tts`, `dfki-medium`) | Çok hızlı ama klonlama yok, Pocket TTS raporunda WER daha yüksek (%3.2); 99eren99 sürümünde lisans belirtilmemiş. Haber sunumu için doğallık yetersiz kalır. |
| Topluluk F5-TTS / Orpheus / SpeechT5 Türkçe fine-tune'ları | Düşük olgunluk (indirme sayısı <100), lisansları çoğunlukla belirtilmemiş veya taban lisans (F5: CC-BY-NC) kısıtlı. |
| **XTTS v2** | Brief gereği (CPML, ticari olmayan). |
| `kyutai/pocket-tts` (taban) | Türkçe yok; B ve C bunun Türkçe fine-tune'ları. |

## Notlar / varsayımlar

- VRAM değerleri: Freya ve VoxCPM2 için kart değeri; diğerleri tahmin. Faz 1.3'te `torch.cuda.max_memory_allocated` ile **ölçülecek**.
- RTF kart değerleri farklı GPU'larda (4090/5090) ölçülmüş; bizim 3060 Laptop'ta 2–4× daha yavaş beklenmeli. Haftada ~90 saniyelik ses için RTF < 1 olan her model yeterli; hız belirleyici kriter değil.
- Pocket TTS Turkish'in yayınladığı karşılaştırma (Trendyol %1.1, Qwen3 TR %1.7, Pocket %1.9 WER) model sahibinin kendi ölçümü; bizim test setimiz İngilizce terim ve rakam yoğun olduğu için sonuçlar farklı çıkabilir.
- Kör testte ses kimliği farkını azaltmak için klonlama destekleyen modellerde (A, B, C, E) **aynı referans ses** kullanılacak (senin kaydın gelirse o, gelmezse B'nin CC-BY `male_1` / `female_1` sesi).
