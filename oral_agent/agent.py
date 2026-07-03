import os

import httpx
from dotenv import load_dotenv
from openai import OpenAI

from scenarios import SCENARIOS

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

_API_KEY = os.getenv("GPT55_API_KEY") or ""
_BASE_URL = (os.getenv("GPT55_API_URL") or "").strip().rstrip("/")
_MODEL = os.getenv("GPT55_MODEL", "claude-sonnet-4-6")
_SSL_VERIFY = os.getenv("GPT55_DISABLE_SSL_VERIFY", "").lower() not in {"1", "true", "yes"}

if not _API_KEY:
    raise RuntimeError("未找到 GPT55_API_KEY，请先在 .env 中配置。")

_http = httpx.Client(verify=_SSL_VERIFY, timeout=60)
_client = OpenAI(api_key=_API_KEY, base_url=_BASE_URL, http_client=_http)


def chat(history: list[dict], user_text: str, scenario_key: str) -> tuple[str, str]:
    """
    Send user_text to the LLM in the context of the chosen scenario.
    Returns (english_response, chinese_feedback).
    history: list of {"role": "user"/"assistant", "content": "..."} dicts
    """
    scenario = SCENARIOS[scenario_key]
    messages = [{"role": "system", "content": scenario["system_prompt"]}]
    messages += [{"role": m["role"], "content": m["content"]} for m in history]
    messages.append({"role": "user", "content": user_text})

    raw: str = (
        _client.chat.completions.create(
            model=_MODEL,
            messages=messages,
            temperature=0.7,
            max_tokens=800,
        )
        .choices[0]
        .message.content
        or ""
    )

    if "---" in raw and "🎯" in raw:
        english, feedback = raw.split("---", 1)
        return english.strip(), feedback.strip()
    return raw.strip(), ""
