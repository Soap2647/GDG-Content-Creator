# Faz 1 değerlendirme ortamları

Modellerin bağımlılıkları çakıştığı için (farklı torch/transformers sürümleri) her biri kendi `uv` sanal ortamında çalışır.
Ortamlar `research/.venvs/` altında durur (git'e girmez). Komutlar repo kökünden, PowerShell'de çalıştırılır.

| Ortam | Model(ler) | Yerel/Colab | Ağırlık indirmesi |
|---|---|---|---|
| `eval` | faster-whisper large-v3 (ASR), jiwer | Yerel | ~3.1 GB |
| `chatterbox` | Chatterbox Multilingual V3 | Yerel | ~3.2 GB (`ve.pt`, `t3_mtl23ls_v3`, `s3gen.pt`) |
| `pocket` | Pocket TTS Turkish (wite-tech) + Pocket TTS TR (kaanhgunay) | Yerel | 0.44 GB + 1.34 GB |
| `freya` | FreyaTTS-small | Yerel | 0.73 GB + AudioVAE2 ~0.38 GB |
| Colab | Trendyol-TTS (+ opsiyonel VoxCPM2 tabanı) | Colab T4 | 5.1 GB (+4.96 GB) |

Ayrıca her yerel ortama CUDA'lı PyTorch (~2.5 GB; uv önbelleği aynı sürümü ortamlar arasında paylaşır).

```powershell
# ASR / metrik ortamı
uv venv research/.venvs/eval --python 3.12
uv pip install -p research/.venvs/eval faster-whisper jiwer soundfile numpy

# Chatterbox: PyPI 0.1.7 yalnızca V2'yi yüklüyor, V3 için GitHub; torch 2.6.0'a sabit, CUDA sürümü ayrıca kurulur
uv venv research/.venvs/chatterbox --python 3.11
uv pip install -p research/.venvs/chatterbox "chatterbox-tts @ git+https://github.com/resemble-ai/chatterbox.git" soundfile
uv pip install -p research/.venvs/chatterbox torch==2.6.0 torchaudio==2.6.0 --index-url https://download.pytorch.org/whl/cu124 --reinstall-package torch --reinstall-package torchaudio

# Pocket TTS (iki Türkçe model aynı runtime)
uv venv research/.venvs/pocket --python 3.12
uv pip install -p research/.venvs/pocket pocket-tts-turkish pocket-tts soundfile
uv pip install -p research/.venvs/pocket torch --index-url https://download.pytorch.org/whl/cu128 --reinstall-package torch

# FreyaTTS (PyPI'da yok, GitHub'dan)
git clone https://github.com/freyavoiceai/FreyaTTS.git research/.venvs/FreyaTTS-src
uv venv research/.venvs/freya --python 3.12
uv pip install -p research/.venvs/freya -r research/.venvs/FreyaTTS-src/requirements.txt soundfile
uv pip install -p research/.venvs/freya torch torchaudio --index-url https://download.pytorch.org/whl/cu128 --reinstall-package torch --reinstall-package torchaudio
# Repo kurulabilir paket değil: çalıştırırken $env:PYTHONPATH = "research/.venvs/FreyaTTS-src"
```

## Çalıştırma sırası

```powershell
# 1) Sentez (her model kendi ortamında); REF = referans ses (bkz. aşağı)
research/.venvs/chatterbox/Scripts/python research/eval/synth.py --model chatterbox_v3 --ref $REF
research/.venvs/pocket/Scripts/python      research/eval/synth.py --model pocket_tr_wite --ref $REF
research/.venvs/pocket/Scripts/python      research/eval/synth.py --model pocket_tr_kaan --ref $REF
research/.venvs/freya/Scripts/python       research/eval/synth.py --model freya
# Colab çıktısı (research/audio/trendyol, research/results/synth_trendyol.json) buraya kopyalanır

# 2) Whisper ile geri yazıya dökme + WER/CER/terim isabeti
research/.venvs/eval/Scripts/python research/eval/asr_eval.py

# 3) Kör test sayfası
python research/eval/build_blind_test.py

# 4) Puanlar geldikten sonra (research/results/blind_ratings/*.json)
python research/eval/score_blind.py
```

## Referans ses

- Kullanıcı kaydı varsa: `research/reference/ref.wav` (10–20 sn, tek konuşmacı, gürültüsüz, mono) + `ref.txt` (metni).
- Yoksa: Pocket TTS Turkish'in CC-BY-4.0 sentetik sesi `female_1` (`hf://wite-tech/pocket-tts-turkish/voices/female_1.wav`)
  tüm klonlayan modellerde ortak referans olarak kullanılır. Böylece kör testte ses kimliği farkı azalır.

## Notlar

- `kaanhgunay/pocket-tts-tr`, `kyutai/pocket-tts` tabanını kullanıyor; taban repo HF'de "gated: auto". İndirme
  için Hugging Face girişi + koşul onayı gerekebilir (`HF_TOKEN`). Gerekirse bunu senden isteyeceğim.
- Whisper ve TTS aynı anda GPU'da tutulmaz; sentez ve ASR ayrı süreçlerde çalışır (6 GB VRAM).
