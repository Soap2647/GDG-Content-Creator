"""Arka plan müziği ve geçiş efektini sıfırdan sentezler (telif/lisans sorunu olmasın diye).

Çıktılar: assets/music/bed.mp3 (döngüye uygun ~96 sn), assets/sfx/whoosh.mp3, assets/sfx/pop.mp3
Kullanım: python assets/generate_audio.py   (bir kez yeterli; çıktılar repoda)
"""
from __future__ import annotations

import subprocess
import tempfile
from pathlib import Path

import numpy as np
import soundfile as sf

SR = 44100
HERE = Path(__file__).parent
rng = np.random.default_rng(44)


def lowpass(x: np.ndarray, alpha: float) -> np.ndarray:
    y = np.empty_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc += alpha * (v - acc)
        y[i] = acc
    return y


def note(freq: float, dur: float, kind: str = "pad") -> np.ndarray:
    t = np.arange(int(SR * dur)) / SR
    if kind == "pad":  # hafif detune'lu üç testere, yumuşak atak/bırakış
        w = sum(2 * ((t * freq * d) % 1) - 1 for d in (0.996, 1.0, 1.004)) / 3
        env = np.minimum(1, t / 0.4) * np.minimum(1, (dur - t) / 0.6)
    else:  # pluck/arp
        w = np.sin(2 * np.pi * freq * t) + 0.3 * np.sin(4 * np.pi * freq * t)
        env = np.exp(-t * 6)
    return (w * env).astype(np.float32)


def midi(n: int) -> float:
    return 440 * 2 ** ((n - 69) / 12)


def make_bed(bpm: int = 100, bars: int = 40) -> np.ndarray:
    beat = 60 / bpm
    bar = 4 * beat
    total = np.zeros(int(SR * bar * bars) + SR, np.float32)
    chords = [[57, 60, 64], [53, 57, 60], [48, 52, 55], [55, 59, 62]]  # Am F C G
    kick_t = np.arange(int(SR * 0.25)) / SR
    kick = (np.sin(2 * np.pi * (50 + 80 * np.exp(-kick_t * 25)) * kick_t) * np.exp(-kick_t * 12)).astype(np.float32)
    hat = (rng.standard_normal(int(SR * 0.05)) * np.exp(-np.arange(int(SR * 0.05)) / SR * 80)).astype(np.float32)
    hat = hat - lowpass(hat, 0.3)
    for b in range(bars):
        start = int(SR * b * bar)
        ch = chords[b % 4]
        pad = sum(note(midi(n), bar + 0.5) for n in ch) / 3
        total[start:start + len(pad)] += 0.35 * pad
        for k in range(8):  # sekizlik arpej
            n = ch[k % 3] + 12 * (1 + (k // 3) % 2)
            s = start + int(SR * k * beat / 2)
            p = note(midi(n), beat)
            total[s:s + len(p)] += 0.08 * p
        if 4 <= b < bars - 2:  # giriş/çıkışta ritim yok
            for k in range(4):
                s = start + int(SR * k * beat)
                total[s:s + len(kick)] += 0.35 * kick
                s2 = s + int(SR * beat / 2)
                total[s2:s2 + len(hat)] += 0.06 * hat
    total = lowpass(total, 0.25)
    fade = int(SR * 2)
    total[:fade] *= np.linspace(0, 1, fade)
    total[-fade:] *= np.linspace(1, 0, fade)
    return total / np.abs(total).max() * 0.7


def make_whoosh(dur: float = 0.6) -> np.ndarray:
    n = int(SR * dur)
    t = np.arange(n) / SR
    noise = rng.standard_normal(n).astype(np.float32)
    # Kesim frekansı yükselip alçalan gürültü: süpürme hissi
    alpha = 0.02 + 0.5 * np.sin(np.pi * t / dur) ** 2
    y = np.empty_like(noise)
    acc = 0.0
    for i in range(n):
        acc += alpha[i] * (noise[i] - acc)
        y[i] = acc
    env = np.sin(np.pi * t / dur) ** 1.5
    y = y * env
    return y / np.abs(y).max() * 0.6


def make_pop() -> np.ndarray:
    t = np.arange(int(SR * 0.12)) / SR
    y = np.sin(2 * np.pi * (900 - 2500 * t) * t) * np.exp(-t * 40)
    return (y / np.abs(y).max() * 0.5).astype(np.float32)


def save_mp3(wav: np.ndarray, out: Path) -> None:
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as d:
        tmp = Path(d) / "x.wav"
        sf.write(tmp, wav, SR)
        subprocess.run(["ffmpeg", "-loglevel", "error", "-y", "-i", str(tmp), "-ac", "1", "-b:a", "128k", str(out)], check=True)
    print("yazıldı:", out.relative_to(HERE.parent))


if __name__ == "__main__":
    save_mp3(make_bed(), HERE / "music" / "bed.mp3")
    save_mp3(make_whoosh(), HERE / "sfx" / "whoosh.mp3")
    save_mp3(make_pop(), HERE / "sfx" / "pop.mp3")
