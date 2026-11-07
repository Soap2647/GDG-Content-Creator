"""TTS işçisi: bir iş dosyasındaki cümleleri seçili backend ile wav'a çevirir.

Ana süreçten ya doğrudan (aynı ortam) ya da backend'in kendi sanal ortamındaki python ile çağrılır:
    <python> -m tts.worker job.json
job.json: {"backend", "voice", "emotion", "items": [{"text", "out"}]}
Var olan çıktılar atlanır; yarıda kalan iş kaldığı yerden sürer.
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

import soundfile as sf

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from tts.backends import BACKENDS  # noqa: E402


def run_job(job: dict) -> int:
    todo = [it for it in job["items"] if not Path(it["out"]).exists()]
    if not todo:
        return 0
    backend = BACKENDS[job["backend"]](voice=job.get("voice", ""), emotion=job.get("emotion", ""))
    backend.load()
    for it in todo:
        wav = backend.synth(it["text"])
        Path(it["out"]).parent.mkdir(parents=True, exist_ok=True)
        sf.write(it["out"], wav, backend.sample_rate)
        print(f"  ♪ {Path(it['out']).name}: {len(wav) / backend.sample_rate:.1f} sn", flush=True)
    return len(todo)


if __name__ == "__main__":
    run_job(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
