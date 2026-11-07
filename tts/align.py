"""Kelime düzeyinde zaman damgası: Whisper (faster-whisper) kelime zamanları → tts kelimeleri → display token'ları.

TTS modeli zaman damgası vermediği için üretilen ses Whisper ile yeniden yazıya dökülür ve
tts_text kelimeleriyle sıra hizalaması (difflib) yapılır. Eşleşmeyen kelimeler komşularından
karakter uzunluğuna göre ara değerlenir. Altyazı her zaman display (orijinal yazım) token'larını gösterir.
"""
from __future__ import annotations

import difflib
import os
import re
import sysconfig
from pathlib import Path

import numpy as np

from normalizer.core import tr_lower

_model = None


def _whisper():
    global _model
    if _model is None:
        # Windows: pip'ten gelen cuBLAS/cuDNN DLL'leri CTranslate2'nin bulabileceği yere eklenir
        for bin_dir in Path(sysconfig.get_paths()["purelib"], "nvidia").glob("*/bin"):
            os.add_dll_directory(str(bin_dir))
            os.environ["PATH"] = str(bin_dir) + os.pathsep + os.environ["PATH"]
        from faster_whisper import WhisperModel

        try:
            _model = WhisperModel("large-v3", device="cuda", compute_type="float16")
        except Exception:  # noqa: BLE001 - NVIDIA GPU/CUDA yoksa işlemcide (daha yavaş ama aynı sonuç)
            _model = WhisperModel("large-v3", device="cpu", compute_type="int8")
    return _model


def _norm(w: str) -> str:
    return re.sub(r"[^\w]", "", tr_lower(w))


def speech_bounds(wav: np.ndarray, sr: int, thresh_db: float = -40) -> tuple[float, float]:
    """Baştaki/sondaki sessizliği atlayarak konuşmanın başlangıç ve bitişi (sn)."""
    frame = int(sr * 0.02)
    if len(wav) < frame:
        return 0.0, len(wav) / sr
    rms = np.sqrt(np.convolve(wav**2, np.ones(frame) / frame, mode="same")) + 1e-9
    voiced = np.where(20 * np.log10(rms / (np.abs(wav).max() + 1e-9)) > thresh_db)[0]
    if not len(voiced):
        return 0.0, len(wav) / sr
    return voiced[0] / sr, voiced[-1] / sr


def align_sentence(wav: np.ndarray, sr: int, tts_words: list[str]) -> list[tuple[float, float]]:
    """tts_words'teki her kelime için (başlangıç, bitiş) saniye, cümle wav'ına göre."""
    start, end = speech_bounds(wav, sr)
    times: list[tuple[float, float] | None] = [None] * len(tts_words)
    try:
        audio16 = np.interp(np.arange(0, len(wav), sr / 16000), np.arange(len(wav)), wav).astype(np.float32)
        segments, _ = _whisper().transcribe(audio16, language="tr", word_timestamps=True, beam_size=5)
        hyp = [(w.word, w.start, w.end) for s in segments for w in (s.words or [])]
    except Exception as e:  # noqa: BLE001 - hizalama başarısızsa orantılı zamanlama yeterli
        print(f"  ! whisper hizalama başarısız ({type(e).__name__}); orantılı zamanlama kullanılıyor")
        hyp = []
    # Whisper "ci pi yu"yu "GPU" diye yazabilir: karakter düzeyinde de eşleşsin diye tek tek kelimeler normalize edilir
    a, b = [_norm(w) for w in tts_words], [_norm(w) for w, _, _ in hyp]
    for blk in difflib.SequenceMatcher(a=a, b=b, autojunk=False).get_matching_blocks():
        for k in range(blk.size):
            _, s, e = hyp[blk.b + k]
            times[blk.a + k] = (s, e)
    return _interpolate(times, tts_words, start, end)


def _interpolate(times, words, start, end) -> list[tuple[float, float]]:
    """Eksik zamanları, bilinen komşular arasında karakter uzunluğuna orantılı doldurur."""
    n = len(words)
    anchors = [(-1, start)] + [(i, t[0]) for i, t in enumerate(times) if t] + [(n, end)]
    out = list(times)
    for (i0, t0), (i1, t1) in zip(anchors, anchors[1:]):
        gap = list(range(i0 + 1, i1))
        if not gap:
            continue
        g_start = t0 if i0 < 0 else times[i0][1]
        lengths = [max(len(words[i]), 1) for i in gap]
        span = max(t1 - g_start, 0.05 * len(gap))
        cur = g_start
        for i, ln in zip(gap, lengths):
            d = span * ln / sum(lengths)
            out[i] = (cur, cur + d)
            cur += d
    # Monoton ve sınırlar içinde
    fixed, last = [], start
    for s, e in out:
        s = max(s, last)
        e = max(e, s + 0.04)
        fixed.append((s, e))
        last = s
    return fixed
