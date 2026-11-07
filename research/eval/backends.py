"""Faz 1 değerlendirmesi için TTS model sarmalayıcıları.

Her model kendi sanal ortamında çalışır (bağımlılıklar çakışıyor, bkz. ENVIRONMENTS.md);
bu yüzden importlar sınıfların içinde, ihtiyaç anında yapılır.
Ortak arayüz: load(ref_wav, ref_text) ve synth(text) -> (np.float32 mono, sample_rate).
"""
from __future__ import annotations

import numpy as np


class Backend:
    name = "base"
    supports_clone = False

    def load(self, ref_wav: str | None, ref_text: str | None) -> None:
        raise NotImplementedError

    def synth(self, text: str) -> tuple[np.ndarray, int]:
        raise NotImplementedError


class ChatterboxV3(Backend):
    """A — ResembleAI/chatterbox, t3_mtl23ls_v3 (MIT, Perth watermark)."""

    name = "chatterbox_v3"
    supports_clone = True

    def load(self, ref_wav, ref_text):
        from chatterbox.mtl_tts import ChatterboxMultilingualTTS

        self.model = ChatterboxMultilingualTTS.from_pretrained(device="cuda", t3_model="v3")
        self.ref_wav = ref_wav

    def synth(self, text):
        wav = self.model.generate(text, language_id="tr", audio_prompt_path=self.ref_wav)
        return wav.squeeze(0).cpu().numpy().astype(np.float32), self.model.sr


class PocketTurkish(Backend):
    """B — wite-tech/pocket-tts-turkish (CC-BY-4.0). Paket kendi sayı normalizasyonunu yapar."""

    name = "pocket_tr_wite"
    supports_clone = True

    def load(self, ref_wav, ref_text):
        from pocket_tts_turkish import TurkishTTS

        self.tts = TurkishTTS.from_pretrained(device="cuda")
        # Kendi hazır sesiyle de test edilir; referans verilmişse klonlama kullanılır
        self.voice = self.tts.voice_from_file(ref_wav) if ref_wav else "female_1"

    def synth(self, text):
        audio = self.tts.generate(text, voice=self.voice)
        return np.asarray(audio, dtype=np.float32), self.tts.sample_rate


class PocketTrKaan(Backend):
    """C — kaanhgunay/pocket-tts-tr v0.1-base (CC-BY-4.0). Ses referansı zorunlu."""

    name = "pocket_tr_kaan"
    supports_clone = True

    def load(self, ref_wav, ref_text):
        from pocket_tts import TTSModel

        if not ref_wav:
            raise ValueError("pocket_tr_kaan bir referans ses ister (--ref)")
        # Kartta geçen v0.1-base etiketi HF reposunda yok; config'in @main'e çevrilmiş kopyası kullanılıyor
        from pathlib import Path

        self.model = TTSModel.load_model(config=str(Path(__file__).parent / "configs" / "pocket_tr_kaan.yaml"))
        self.state = self.model.get_state_for_audio_prompt(ref_wav)

    def synth(self, text):
        audio = self.model.generate_audio(self.state, text)
        return np.asarray(audio.cpu() if hasattr(audio, "cpu") else audio, dtype=np.float32).squeeze(), self.model.sample_rate


class Freya(Backend):
    """D — freyavoice/Freya-TTS small (Apache-2.0). Tek konuşmacı (Leyla), klonlama yok."""

    name = "freya"

    def load(self, ref_wav, ref_text):
        from freyatts import FreyaTTS

        self.tts = FreyaTTS.from_pretrained("freyavoice/freya-tts", device="cuda")

    def synth(self, text):
        return np.asarray(self.tts.synthesize(text), dtype=np.float32), 48000


class VoxCPMBased(Backend):
    """E — Trendyol/Trendyol-TTS (VoxCPM2 + TR LoRA). ~8 GB VRAM: Colab T4'te çalıştırılır."""

    name = "trendyol"
    model_id = "Trendyol/Trendyol-TTS"
    supports_clone = True

    def load(self, ref_wav, ref_text):
        from voxcpm.core import VoxCPM

        self.model = VoxCPM.from_pretrained(hf_model_id=self.model_id, load_denoiser=False, optimize=True)
        self.ref_wav, self.ref_text = ref_wav, ref_text

    def synth(self, text):
        kwargs = dict(cfg_value=2.0, inference_timesteps=16, max_len=4096, normalize=False, denoise=False)
        if self.ref_wav:
            kwargs["reference_wav_path"] = self.ref_wav
        wav = self.model.generate(text=text, **kwargs)
        return np.asarray(wav, dtype=np.float32), self.model.tts_model.sample_rate


class VoxCPM2Base(VoxCPMBased):
    """Opsiyonel — openbmb/VoxCPM2 tabanı, Trendyol fine-tune'unun katkısını görmek için."""

    name = "voxcpm2"
    model_id = "openbmb/VoxCPM2"


BACKENDS: dict[str, type[Backend]] = {
    b.name: b for b in [ChatterboxV3, PocketTurkish, PocketTrKaan, Freya, VoxCPMBased, VoxCPM2Base]
}
