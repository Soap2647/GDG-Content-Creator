"""Claude çağrıları: Pydantic şemasıyla doğrulanmış yapılandırılmış çıktı.

İki mod (config/pipeline.yaml → llm.mode):
- claude_code (varsayılan): Pipeline istemi episodes/<hafta>/llm/<görev>.prompt.md'ye yazar ve durur.
  Claude Code (bu repoda çalışan oturum) istemi okuyup yanıtı <görev>.response.json'a yazar;
  adım yeniden çalıştırıldığında yanıt aynı şemayla doğrulanır. Ayrı API anahtarı gerekmez.
- api: Anthropic API ile doğrudan çağrı (ANTHROPIC_API_KEY gerekir); otomasyon/zamanlanmış çalışma için.
"""
from __future__ import annotations

import json
import os
from pathlib import Path
from typing import TypeVar

from pydantic import BaseModel, ValidationError

from common.config import ROOT, load_env, settings

T = TypeVar("T", bound=BaseModel)


class LLMError(RuntimeError):
    pass


class LLMPending(RuntimeError):
    """claude_code modunda: istem dosyası yazıldı, yanıt bekleniyor."""


def ask(system: str, user: str, schema: type[T], *, task: Path, effort: str | None = None, max_tokens: int = 32000) -> T:
    """task: uzantısız görev yolu, ör. episodes/2026-W44/llm/score"""
    if settings()["llm"].get("mode", "claude_code") == "api":
        return _ask_api(system, user, schema, effort=effort, max_tokens=max_tokens)
    return _ask_claude_code(system, user, schema, task)


def _ask_claude_code(system: str, user: str, schema: type[T], task: Path) -> T:
    prompt_path = task.with_suffix(".prompt.md")
    response_path = task.with_suffix(".response.json")
    prompt = (
        f"# Görev: {task.name}\n\n"
        f"Yanıtı `{response_path.relative_to(ROOT).as_posix()}` dosyasına, aşağıdaki JSON şemasına uyan TEK bir JSON nesnesi olarak yaz.\n\n"
        f"## Sistem talimatı\n\n{system}\n\n## Girdi\n\n{user}\n\n"
        f"## Yanıt şeması (JSON Schema)\n\n```json\n{json.dumps(schema.model_json_schema(), ensure_ascii=False, indent=1)}\n```\n"
    )
    task.parent.mkdir(parents=True, exist_ok=True)
    stale = prompt_path.exists() and prompt_path.read_text(encoding="utf-8") != prompt
    # Eski yanıt, yeni istem yazılmadan ÖNCE kenara alınır: arada hata olursa eski yanıt yeni isteme eşleşmiş görünmesin
    if stale and response_path.exists():
        response_path.replace(response_path.with_suffix(".stale.json"))  # replace: Windows'ta hedef varsa da yazar
    prompt_path.write_text(prompt, encoding="utf-8")
    if response_path.exists() and not stale:
        try:
            return schema.model_validate_json(response_path.read_text(encoding="utf-8"))
        except ValidationError as e:
            raise LLMError(f"{response_path.name} şemaya uymuyor:\n{e}") from e
    raise LLMPending(f"Claude Code görevi bekleniyor: {prompt_path.relative_to(ROOT).as_posix()} → "
                     f"{response_path.relative_to(ROOT).as_posix()}")


def _ask_api(system: str, user: str, schema: type[T], *, effort: str | None, max_tokens: int) -> T:
    load_env()
    import anthropic

    if not os.environ.get("ANTHROPIC_API_KEY"):
        raise LLMError("llm.mode=api ama ANTHROPIC_API_KEY yok. .env.example → .env, ya da llm.mode: claude_code kullanın.")
    cfg = settings()["llm"]
    response = anthropic.Anthropic(timeout=600).messages.parse(
        model=cfg["model"],
        max_tokens=max_tokens,
        system=[{"type": "text", "text": system, "cache_control": {"type": "ephemeral"}}],
        messages=[{"role": "user", "content": user}],
        output_format=schema,
        output_config={"effort": effort or cfg["effort"]},
        # Güvenlik sınıflandırıcısı reddederse istek sunucu tarafında önerilen modele yönlendirilir
        extra_headers={"anthropic-beta": "server-side-fallback-2026-07-01"},
        extra_body={"fallbacks": "default"},
    )
    if response.stop_reason == "refusal":
        details = getattr(response, "stop_details", None)
        raise LLMError(f"Claude isteği reddetti: {getattr(details, 'category', None)} {getattr(details, 'explanation', '')}")
    if response.stop_reason == "max_tokens":
        raise LLMError("Yanıt max_tokens sınırında kesildi; max_tokens değerini artırın.")
    if response.parsed_output is None:
        raise LLMError("Claude yanıtı şemaya uygun ayrıştırılamadı.")
    return response.parsed_output
