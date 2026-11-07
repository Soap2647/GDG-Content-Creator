"""TTS adaptörleri. Model değiştirmek: config/pipeline.yaml → tts.backend.

Yeni model eklemek için TTSBackend'den türetip BACKENDS'e kaydedin. Importlar sınıf içinde yapılır:
her model kendi bağımlılıklarını yalnızca seçildiğinde yükler (ve gerekirse ayrı bir sanal ortamda çalışır).
"""
from __future__ import annotations

from abc import ABC, abstractmethod

import numpy as np


class TTSBackend(ABC):
    name: str
    license_note: str  # post.md'ye eklenecek atıf/lisans satırı

    def __init__(self, voice: str = "", emotion: str = "") -> None:
        self.voice, self.emotion = voice, emotion

    @abstractmethod
    def load(self) -> None: ...

    @abstractmethod
    def synth(self, text: str) -> np.ndarray:
        """Tek cümle → mono float32 dalga (self.sample_rate)."""

    sample_rate: int = 24000
    # Büyük bulut modelleri "Google DeepMind", "1071" gibi yazımları kendisi doğru okur; fonetik yazım
    # ("gugıl dip maynd") onları bozar. True ise sentezde ve hizalamada display metni kullanılır.
    reads_display: bool = False
    # Bulut modeli: ana .venv'de çalışır (tts.python yok sayılır) ve bütün bölümü tek istekte okur
    # (ücretsiz katmanlarda istek sınırı düşük; tek parça okuma tonlamayı da birimler arasında sürdürür).
    cloud: bool = False
    caption_credit: str = ""  # Instagram açıklamasına girmesi gereken atıf (lisans gereği)


class PocketTurkish(TTSBackend):
    """wite-tech/pocket-tts-turkish — Faz 1 kör testinin birincisi. CC-BY-4.0 (atıf zorunlu)."""

    name = "pocket_tr"
    license_note = ("Seslendirme: Pocket TTS Turkish (wite-tech, CC BY 4.0) — "
                    "https://huggingface.co/wite-tech/pocket-tts-turkish")

    def load(self) -> None:
        import torch
        from pocket_tts_turkish import TurkishTTS

        self.tts = TurkishTTS.from_pretrained(device="cuda" if torch.cuda.is_available() else "cpu")
        self.sample_rate = self.tts.sample_rate
        v = self.voice or "female_1"
        self._voice = self.tts.voice_from_file(v) if v.lower().endswith(".wav") else v

    def synth(self, text: str) -> np.ndarray:
        kwargs = {"voice": self._voice}
        if self.emotion:
            kwargs["emotion"] = self.emotion
        return np.asarray(self.tts.generate(text, **kwargs), dtype=np.float32)


class ChatterboxV3(TTSBackend):
    """ResembleAI Chatterbox Multilingual V3 — yedek model. MIT; çıktılar Perth watermark içerir.

    Ayrı ortam gerekir (torch 2.6 sabit): tts.python ile o ortamın python'unu gösterin.
    voice: referans kayıt .wav yolu (zorunlu; Türkçe referans kullanılmazsa aksan kayar).
    """

    name = "chatterbox_v3"
    license_note = "Seslendirme: Chatterbox Multilingual V3 (Resemble AI, MIT)"

    def load(self) -> None:
        from chatterbox.mtl_tts import ChatterboxMultilingualTTS

        if not self.voice.lower().endswith(".wav"):
            raise ValueError("chatterbox_v3 için tts.voice bir referans .wav yolu olmalı")
        self.model = ChatterboxMultilingualTTS.from_pretrained(device="cuda", t3_model="v3")
        self.sample_rate = self.model.sr

    def synth(self, text: str) -> np.ndarray:
        wav = self.model.generate(text, language_id="tr", audio_prompt_path=self.voice)
        return wav.squeeze(0).cpu().numpy().astype(np.float32)


class OmniVoiceBackend(TTSBackend):
    """k2-fsa/OmniVoice — model ağırlıkları CC-BY-NC (ticari olmayan kullanım; Instagram yayını, gelir yok).

    Ayrı ortam önerilir (torch 2.8): tts.python ile o ortamın python'unu gösterin.
    voice: referans .wav yolu (klonlama, en kararlı mod) veya "design:female, young adult, moderate pitch"
    (ses tasarımı; model kartına göre yalnızca zh/en verisiyle eğitildi, Türkçede daha az kararlı).
    """

    name = "omnivoice"
    license_note = "Seslendirme: OmniVoice (k2-fsa, model ağırlıkları CC BY-NC 4.0, ticari olmayan kullanım)"
    sample_rate = 24000

    def load(self) -> None:
        import torch
        from omnivoice import OmniVoice

        self.model = OmniVoice.from_pretrained("k2-fsa/OmniVoice", device_map="cuda:0", dtype=torch.float16)

    def synth(self, text: str) -> np.ndarray:
        kwargs: dict = {"text": text}
        if self.voice.startswith("design:"):
            kwargs["instruct"] = self.voice.removeprefix("design:").strip()
        elif self.voice:
            kwargs["ref_audio"] = self.voice
        return np.asarray(self.model.generate(**kwargs)[0], dtype=np.float32)


class AhenkCep(TTSBackend):
    """ozgurguler/ahenk-cep-tr — 8,6M parametre, CPU'da da çalışır, 48 kHz, tek tasarlanmış ses (f022). CC-BY-4.0.

    Ayrı ortam: research/.venvs/ahenk (ema-lightning + ahenk-turkish-tts/trnorm). emotion = üslup:
    neutral | cheerful | calm | surprised | empathetic | angry | sad. Metni kendi trnorm'u ile okunuşa çevirir.
    """

    name = "ahenk_cep"
    license_note = "Seslendirme: Ahenk Cep (ozgurguler, CC BY 4.0) — https://huggingface.co/ozgurguler/ahenk-cep-tr"

    def load(self) -> None:
        import sys

        import torch
        from huggingface_hub import snapshot_download

        d = snapshot_download("ozgurguler/ahenk-cep-tr", allow_patterns=["*.pt", "ahenk_cep.py"])
        sys.path.insert(0, d)
        from ahenk_cep import AhenkCep as _Cep

        self.tts = _Cep(f"{d}/student.pt", f"{d}/decoder.pt", device="cuda" if torch.cuda.is_available() else "cpu")

    def synth(self, text: str) -> np.ndarray:
        audio, sr = self.tts.say(text, style=self.emotion or "neutral")
        self.sample_rate = sr
        return np.asarray(audio, dtype=np.float32)


class Ahenk(TTSBackend):
    """ozgurguler/ahenk-tts-tr — VoxCPM2 (2B) + Türkçe LoRA, 48 kHz, tek tasarlanmış ses (f022), 6 duygu. CC-BY-4.0.

    Ayrı ortam: research/.venvs/ahenk (+ voxcpm). VoxCPM2 tabanı ~5 GB indirme, ~8 GB VRAM önerilir.
    emotion: boş (düz okuma) veya cheerful, calm, surprised, empathetic, angry, sad.
    """

    name = "ahenk"
    license_note = ("Seslendirme: Ahenk (ozgurguler, CC BY 4.0; taban model VoxCPM2, Apache-2.0) — "
                    "https://huggingface.co/ozgurguler/ahenk-tts-tr")

    def load(self) -> None:
        import json
        import sys
        from pathlib import Path

        from huggingface_hub import snapshot_download
        from voxcpm import VoxCPM
        from voxcpm.model.voxcpm import LoRAConfig

        d = snapshot_download("ozgurguler/ahenk-tts-tr", allow_patterns=["lora_*", "*.py", "instructions_tr.json"])
        sys.path.insert(0, d)
        from instruction_pick import compose, pick
        from pause_clean import clean

        self._compose, self._pick, self._clean = compose, pick, clean
        cfg = json.loads(Path(d, "lora_config.json").read_text(encoding="utf-8"))["lora_config"]
        self.tts = VoxCPM.from_pretrained("openbmb/VoxCPM2", load_denoiser=False, optimize=False,
                                          lora_config=LoRAConfig(**cfg), lora_weights_path=d)
        self.sample_rate = self.tts.tts_model.sample_rate

    def synth(self, text: str) -> np.ndarray:
        from trnorm import normalize

        instruction, model_text, _ = self._pick(self.emotion, normalize(text), "auto")
        wav = self.tts.generate(text=self._compose(instruction, model_text), cfg_value=2.0, inference_timesteps=16,
                                normalize=False)
        return np.asarray(self._clean(wav, self.sample_rate)[0], dtype=np.float32)


def _api_key(name: str) -> str:
    import os

    from common.config import load_env

    load_env()
    if not os.environ.get(name):
        raise RuntimeError(f"{name} yok: .env dosyasına ekleyin (bkz. .env.example)")
    return os.environ[name]


def _post(url: str, retries: int = 5, **kwargs):
    """Ücretsiz katmanlarda dakikalık sınır sık aşılır: 429/5xx'te bekleyip yeniden dener."""
    import time

    import requests

    for attempt in range(retries):
        r = requests.post(url, timeout=120, **kwargs)
        if r.status_code not in (429, 500, 502, 503) or attempt == retries - 1:
            break
        wait = 20 * (attempt + 1)
        print(f"  … {r.status_code}, {wait} sn bekleniyor", flush=True)
        time.sleep(wait)
    if not r.ok:
        raise RuntimeError(f"{r.status_code}: {r.text[:300]}")
    return r


class ElevenLabs(TTSBackend):
    """ElevenLabs bulut API'si (ELEVENLABS_API_KEY). Ücretsiz plan: ayda ~10 bin karakter, ticari olmayan
    kullanım, elevenlabs.io'ya atıf zorunlu (post.md'ye license_note ile girer).

    voice: hesabın ses listesindeki ad (ör. "Sarah") veya ses kimliği. emotion: kullanılmaz.
    Model: tts.elevenlabs_model (varsayılan eleven_multilingual_v2).
    """

    name = "elevenlabs"
    license_note = "Seslendirme: ElevenLabs (ücretsiz plan, ticari olmayan kullanım) — elevenlabs.io"
    caption_credit = "🎙️ Ses: elevenlabs.io"  # ücretsiz plan açıklamada atıf istiyor
    reads_display = cloud = True

    # Herkese açık hazır sesler: yalnızca "metinden sese" izni olan kısıtlı anahtarlar ses listesini okuyamaz
    PREMADE = {"sarah": "EXAVITQu4vr4xnSDxMaL", "laura": "FGY2WhTYpPnrIDTdsKH5", "alice": "Xb7hH8MSUJpSbSDYk0k2",
               "matilda": "XrExE9yKIg1WjnnlVkGX", "jessica": "cgSgspJ2msm6clMCkdW9", "lily": "pFZP5JQG7iQjIQuC4Bku",
               "charlie": "IKne3meq5aSn9XLyUdCD", "george": "JBFqnCBsd6RMkjVDRZzb",
               "daniel": "onwK4e9ZLuTAKqWW03F9", "brian": "nPczCjzI2devNBz1zQrb", "chris": "iP95p4xoKVk53GoZ742B",
               "eric": "cjVigY5qzO86Huf0OWal", "will": "bIHbv24MWmeRgasZH58o", "roger": "CwhRBWXzGAHq8TQ4Fs17",
               "river": "SAz9YHcvj6GT2YYXdXww", "callum": "N2lVS1w4EtoT3dr4eOWO", "adam": "pNInz6obpgDQGcFmaJgB"}

    def load(self) -> None:
        import requests

        from common.config import settings

        self.key = _api_key("ELEVENLABS_API_KEY")
        self.model = settings()["tts"].get("elevenlabs_model") or "eleven_multilingual_v2"
        voices = requests.get("https://api.elevenlabs.io/v1/voices", headers={"xi-api-key": self.key}, timeout=30)
        by_name = dict(self.PREMADE)
        if voices.ok:
            by_name |= {v["name"].split(" - ")[0].lower(): v["voice_id"] for v in voices.json()["voices"]}
        want = (self.voice or "Sarah").lower()
        self.voice_id = by_name.get(want) or self.voice
        if want not in by_name and len(self.voice) < 15:
            raise ValueError(f"ElevenLabs sesi bulunamadı: {self.voice!r}; mevcut: {', '.join(sorted(by_name))}")

    def synth(self, text: str) -> np.ndarray:
        body = {"text": text, "model_id": self.model,
                "voice_settings": {"stability": 0.4, "similarity_boost": 0.75, "style": 0.3}}
        if self.model != "eleven_multilingual_v2":  # v2 dil kodunu kabul etmiyor, Türkçeyi metinden anlıyor
            body["language_code"] = "tr"
        r = _post(f"https://api.elevenlabs.io/v1/text-to-speech/{self.voice_id}", params={"output_format": "pcm_24000"},
                  headers={"xi-api-key": self.key}, json=body)
        return np.frombuffer(r.content, "<i2").astype(np.float32) / 32768


class GeminiTTS(TTSBackend):
    """Gemini API konuşma üretimi (GEMINI_API_KEY, Google AI Studio'dan ücretsiz). 24 kHz.

    voice: hazır ses adı (ör. Kore, Leda, Aoede kadın; Puck, Fenrir, Charon erkek).
    emotion: okuma tarzı talimatı; boşsa enerjik Reels anlatıcısı. Model: tts.gemini_model.
    """

    name = "gemini"
    license_note = "Seslendirme: Google Gemini TTS (yapay zeka sesi)"
    reads_display = cloud = True
    STYLE = ("Aşağıdaki Türkçe metni, üniversite öğrencilerine teknoloji haberlerini anlatan enerjik ve samimi "
             "bir Instagram Reels anlatıcısı gibi oku. Haber spikeri gibi değil, arkadaşına anlatır gibi, "
             "doğal ve akıcı konuş. Yalnızca metni oku:")

    def load(self) -> None:
        from common.config import settings

        self.key = _api_key("GEMINI_API_KEY")
        self.model = settings()["tts"].get("gemini_model") or "gemini-2.5-flash-preview-tts"

    def synth(self, text: str) -> np.ndarray:
        import base64

        body = {"contents": [{"parts": [{"text": f"{self.emotion or self.STYLE}\n\n{text}"}]}],
                "generationConfig": {"responseModalities": ["AUDIO"], "speechConfig": {
                    "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": self.voice or "Kore"}}}}}
        r = _post(f"https://generativelanguage.googleapis.com/v1beta/models/{self.model}:generateContent",
                  headers={"x-goog-api-key": self.key}, json=body)
        data = r.json()["candidates"][0]["content"]["parts"][0]["inlineData"]["data"]
        return np.frombuffer(base64.b64decode(data), "<i2").astype(np.float32) / 32768


BACKENDS: dict[str, type[TTSBackend]] = {
    b.name: b for b in (PocketTurkish, ChatterboxV3, OmniVoiceBackend, AhenkCep, Ahenk, ElevenLabs, GeminiTTS)
}
