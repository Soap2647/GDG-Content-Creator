# Varlık lisansları

Videoda kullanılan her ses/görsel varlığın kaynağı ve lisansı. Yeni varlık eklerken buraya satır ekleyin.

| Dosya | Kaynak | Lisans | Not |
|---|---|---|---|
| `music/bed.mp3` | `assets/generate_audio.py` ile sıfırdan sentezlendi (Am–F–C–G pad + arpej + yumuşak ritim, 100 BPM) | Ekip üretimi, telifsiz (CC0 olarak kabul edilebilir) | Harici örnek/sample kullanılmadı |
| `sfx/whoosh.mp3` | `assets/generate_audio.py` (filtrelenmiş gürültü süpürmesi) | Ekip üretimi, telifsiz | Haber geçişlerinde |
| `sfx/pop.mp3` | `assets/generate_audio.py` (sinüs "pop") | Ekip üretimi, telifsiz | Görsel değişimlerinde |
| `brand/gdg_logo_original.jpg` | GDG Kastamonu University bölüm logosu (ekipten) | Google Developer Groups marka kuralları | Kaynak dosya |
| `brand/gdg_logo.png` | `make_dark_logo.py` ile koyu zemin sürümü (beyaz zemin şeffaf, koyu yazı beyaz) | Aynı | Video boyunca sol üstte ve kapanışta |

## Diğer bileşenler

| Bileşen | Lisans | Not |
|---|---|---|
| Google Sans (font, `@remotion/google-fonts`) | SIL Open Font License 1.1 | Google Fonts üzerinden |
| Remotion | Remotion License — kâr amacı gütmeyen kuruluşlara ücretsiz | Bkz. README "Lisanslar" |
| Pocket TTS Turkish (seslendirme modeli, wite-tech/pocket-tts-turkish, kadın ve erkek sesleri) | CC BY 4.0 | Varsayılan TTS; `post.md`'ye atıf satırı otomatik eklenir |
| Ahenk (alternatif seslendirme modeli, ozgurguler/ahenk-tts-tr; taban VoxCPM2 Apache-2.0) | CC BY 4.0 | `tts.backend: ahenk` seçilirse |
| Kaynak sayfa ekran görüntüleri | İlgili sitenin | Haber/kaynak gösterimi amacıyla, küçük ölçekte ve kaynak adıyla; sayfadaki tüm görseller (logo, fotoğraf) bulanıklaştırılır |
