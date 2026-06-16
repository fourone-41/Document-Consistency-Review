"""Step 3: Generate Claims from domain entities (Requirement, DesignInput, Test).
Claims use free-text subject (not restricted to controlled vocabulary)."""
import json
import sys
import re
import time
from pathlib import Path
from openai import OpenAI

from config import API_KEY, LLM_BASE_URL, LLM_MODEL, PER_FILE_DIR, LLM_MAX_TOKENS

client = OpenAI(api_key=API_KEY, base_url=LLM_BASE_URL)

CLAIM_PROMPT = """你是医疗器械文档一致性审查专家。请从以下已抽取的领域实体中生成"归一化事实断言"（Claim）。

Claim 定义：
- subject: 主题词（自由文本，用最自然的术语，如"测量精度"、"工作环境温度"、"显示分辨率"）
- attribute: 该主题的具体方面（如"范围"、"允差"、"阈值"、"数量"、"等级"）
- value: 量化值
- unit: 单位
- tolerance: 公差（如 ±0.2℃）
- condition: 适用条件
- raw_text: 来源原文摘要

生成规则：
1. 只从含有量化信息或明确规格要求的条目生成 Claim
2. 一个实体可能生成多条 Claim（如一条设计输入同时规定了范围和精度）
3. subject 用中文技术术语，尽量简洁（2-6字）
4. 纯功能描述型（如"测量原理：红外非接触式"）也生成 Claim
5. 没有量化信息且无明确规格的条目不生成

输出格式（JSON数组）：
[
  {"subject": "...", "attribute": "...", "value": "...", "unit": "...", "tolerance": "...", "condition": "...", "raw_text": "..."},
  ...
]

严格输出 JSON，不要加 markdown 代码块标记。"""


def try_parse_json(text: str) -> list:
    """Parse JSON array from LLM response."""
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r'^```\w*\n?', '', text)
        text = re.sub(r'\n?```$', '', text)
        text = text.strip()
    try:
        result = json.loads(text)
        return result if isinstance(result, list) else []
    except json.JSONDecodeError:
        for suffix in [']', '"}]', '}]']:
            try:
                result = json.loads(text + suffix)
                return result if isinstance(result, list) else []
            except json.JSONDecodeError:
                continue
    return []


def generate_claims_for_file(filepath: Path) -> list[dict]:
    """Generate claims from extracted entities in a file."""
    data = json.loads(filepath.read_text(encoding="utf-8"))

    entities = []
    for key in ["requirements", "design_inputs", "tests", "functions", "components"]:
        if key in data and isinstance(data[key], list):
            for item in data[key][:40]:
                entities.append({"_type": key, **item})

    if not entities:
        return []

    user_msg = json.dumps(entities, ensure_ascii=False, indent=1)
    if len(user_msg) > 14000:
        user_msg = user_msg[:14000] + "\n...(truncated)"

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=LLM_MAX_TOKENS,
            messages=[
                {"role": "system", "content": CLAIM_PROMPT},
                {"role": "user", "content": user_msg},
            ],
        )
        content = response.choices[0].message.content or "[]"
        claims = try_parse_json(content)
        return claims
    except Exception as e:
        print(f"    ERROR: {e}", flush=True)
        return []


def main():
    json_files = sorted(PER_FILE_DIR.glob("*.json"))
    print(f"=== Step 3: Generate Claims ===", flush=True)
    print(f"Processing {len(json_files)} files\n", flush=True)

    total_start = time.time()

    for i, fp in enumerate(json_files, 1):
        print(f"[{i}/{len(json_files)}] {fp.stem}...", end="", flush=True)
        t0 = time.time()
        claims = generate_claims_for_file(fp)
        elapsed = time.time() - t0
        print(f" {len(claims)} claims ({elapsed:.1f}s)", flush=True)

        data = json.loads(fp.read_text(encoding="utf-8"))
        data["_claims"] = claims
        fp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")

    total_elapsed = time.time() - total_start
    print(f"\n=== Step 3 Complete === ({total_elapsed:.0f}s)", flush=True)


if __name__ == "__main__":
    main()
