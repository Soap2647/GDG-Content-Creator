# Claude Code için: haftalık bölüm üretimi

Bu repo GDG on Campus Kastamonu'nun haftalık AI teknoloji gündemi videosunu üretir. Üretim bu repoda çalışan
Claude Code oturumundan yapılır; `config/pipeline.yaml` → `llm.mode: claude_code` (ayrı API anahtarı yok).

Ayrıntılı rehber, kararların gerekçeleri ve sorun giderme: [`docs/ARGE_DEVIR_REHBERI.md`](docs/ARGE_DEVIR_REHBERI.md). Yeni bir ekip üyesiyle ilk oturumda önce onu oku.

## "Bu haftanın bölümünü hazırla" dendiğinde

1. `.venv/Scripts/python -m pipeline episode --week <YYYY-Www>` çalıştır. Çıkış kodları:
   - `4`: Claude Code görevi bekleniyor. Çıktıda adı geçen `episodes/<hafta>/llm/<görev>.prompt.md`'yi oku,
     yanıtı aynı klasördeki `<görev>.response.json`'a istemin sonundaki JSON şemasına uygun yaz, komutu tekrar çalıştır.
     Görevler sırayla gelir: `score` → `write` → `verify`.
   - `3`: Onay kapısı. Kullanıcıya `episodes/<hafta>/review.html`'i göster ve **dur**. Onayı asla kendin verme;
     `approve` komutunu yalnızca kullanıcı açıkça onay verdiğinde çalıştır.
   - `0`: Bölüm hazır (`final.mp4`, `thumbnail.png`, `post.md`, `sources.json`).
2. `write` görevinde kesin kurallar istemin içinde: kaynak metinde olmayan rakam/isim/tarih yok, her iddia `claims`'e
   kaynağıyla, emin olunmayan `uncertain: true`. Kaynak metni "(metin alınamadı)" olan haberi seçme.
3. `verify` görevinde kendi yazdığın senaryoyu doğruluyorsun: her iddia için kaynaktan **birebir alıntı** bul;
   bulamıyorsan `not_found` de, yorumla destekleme. Mümkünse bu görevi bağlamı temiz bir alt ajana ver (bağımsız kontrol).
4. Senaryoda yeni İngilizce terim/kısaltma varsa `config/pronunciation.json`'a okunuşunu ekle (harf harf okunanlarda
   heceler boşlukla), sonra `normalize --force`.

## Notlar

- Her adım tek başına çalışır ve çıktısı varsa atlanır (`--force` ile yeniden). Ara çıktılar `episodes/<hafta>/`.
- TTS modeli: `config/pipeline.yaml` → `tts.backend` (varsayılan `gemini`, bulut; yedek `elevenlabs`, yerel `pocket_tr`). Anahtarlar `.env`'de. Bulut modelleri bölümü tek istekte okur (Gemini ücretsiz: günde 10 istek; ElevenLabs ücretsiz: ayda ~10 bin karakter, açıklamada atıf otomatik eklenir). Ses: çift ISO hafta Gemini Kore, tek hafta Gemini Algenib (`tts.voices`, Algenib'in okuma tarzı `tts.voice_styles`'ta); tek hafta için `tts --voice <ad> --force`. Bulut sesi bölüm başına ~6 istekte (giriş, her haber, kapanış) okunur.
- Senaryo akışı: kanca → teaser ("sona sakladık") → her haberin önünde köprü cümlesi → son haber fırsat/eylem → yorum sorusu → takip çağrısı. Bunlar yeni olgu içermez.
- Görsel kurallar: şirket logosu ve gerçek kişi fotoğrafı yok (ekran görüntülerinde görseller bulanıklaştırılır),
  konuşan avatar yok. Yapay zeka bilgisi videoya rozet olarak yazılmaz (2026-10-28 ekip kararı); paylaşırken Instagram'ın
  "AI etiketi" seçeneği açılır — bu `post.md`'deki kontrol listesinde zorunlu madde.
- Bölüm 4 haber (`episode.min_items/max_items`), ~80-105 sn.
