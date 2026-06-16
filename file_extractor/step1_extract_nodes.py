"""Step 1: Extract nodes from markdown files using LLM (per doc type prompts).
Uses raw OpenAI API + manual JSON parsing to handle token truncation gracefully."""
import json
import sys
import re
import time
from pathlib import Path
from openai import OpenAI

from config import (
    API_KEY, LLM_BASE_URL, LLM_MODEL, MARKDOWN_DIR,
    PER_FILE_DIR, MAX_CHUNK_CHARS, LLM_MAX_TOKENS,
    EXCLUDE_FOLDERS, detect_doc_type,
)
from schema import DOC_TYPE_TO_MODEL

client = OpenAI(api_key=API_KEY, base_url=LLM_BASE_URL)

# ============================================================
# Document-type-specific system prompts
# ============================================================
BASE_INSTRUCTION = """严格输出 JSON，不要加 markdown 代码块标记。
字段为 null 或空数组时省略该字段。只抽取文档中明确存在的信息，不要编造。

【重要-SemanticFragment兜底规则】：
对于文档中有实质信息但无法放入上述结构化字段的长段落（如预期用途描述、质量要求、接口说明、工作流程描述等），
请整段放入 semantic_fragments 数组，格式：
{fragment_type, content, topic_tags: [关键词], related_subjects: [关联的其他节点名称]}
fragment_type 取值：design_rationale/working_principle/constraint_statement/behavioral_spec/open_issue/scope_limitation/assumption
不要遗漏有意义的长文本！签名栏、空行等无信息内容可跳过。"""

PROMPTS = {
    "project_approval": """你是医疗器械DHF文档信息抽取专家。当前文件是【立项批准书/客户需求书】。
请从中抽取以下字段（JSON格式）：
- document: {title, doc_type, dhf_stage, version, date}
- requirements: [{req_id, category, description, value, unit, tolerance, condition}]
- markets: [{region, certification, selected, registrant, registration_path}]
- intended_use_items: [{seq, content}]
- functions: [{name, value, exists}]
- persons: [{name, title, signed}]
- identifiers: [{id_type, value}]
- products: [{product_id, model, name, region}]
- regulations: [{std_id, version, clause, region, applicable, requirement_text}]（最多抽取20条最重要的）
- revision_records: [{seq, version, change_description, author, approver, date}]
- semantic_fragments: [{fragment_type, content, topic_tags, related_subjects}]
  对于"预期用途"等长段落描述，若无法拆成结构化字段，请整段放入 semantic_fragments。
""" + BASE_INSTRUCTION,

    "requirement": """你是医疗器械DHF文档信息抽取专家。当前文件是【需求书】。
请从中抽取（JSON格式）：
- document: {title, doc_type, dhf_stage, version, date}
- requirements: [{req_id, category, description, value, unit, tolerance, condition}]
- markets: [{region, certification, selected}]
- intended_use_items: [{seq, content}]
- functions: [{name, value}]
- persons: [{name, title}]
- identifiers: [{id_type, value}]
- products: [{product_id, model, name}]
- regulations: [{std_id, version, region, applicable}]（最多20条）
- revision_records: [{seq, version, change_description, author, date}]
""" + BASE_INSTRUCTION,

    "design_input": """你是医疗器械DHF文档信息抽取专家。当前文件是【设计输入】。
请从中抽取（JSON格式）：
- document: {title, doc_type, version}
- design_inputs: [{di_id, category, description, value, unit, tolerance, condition, source_req_id}]
- markets: [{region, certification, selected}]
- functions: [{name, value}]
- components: [{name, spec, model}]
- persons: [{name, title}]
- identifiers: [{id_type, value}]
- products: [{product_id, model, name}]
- regulations: [{std_id, version, region, applicable}]（最多20条）
- revision_records: [{seq, version, change_description, author, date}]
""" + BASE_INSTRUCTION,

    "risk_analysis": """你是医疗器械DHF文档信息抽取专家。当前文件是【风险分析报告】。
请从中抽取（JSON格式）：
- document: {title, doc_type, version}
- risks: [{risk_id, hazard, hazardous_situation, harm, severity, probability, risk_level, phase}]
- risk_controls: [{control_id, measure, type, evidence_type}]
- persons: [{name, title}]
- identifiers: [{id_type, value}]
- products: [{product_id, name}]
- revision_records: [{seq, version, change_description, author, date}]
""" + BASE_INSTRUCTION,

    "test_report": """你是医疗器械DHF文档信息抽取专家。当前文件是【检测报告/测试报告】。
请从中抽取（JSON格式）：
- document: {title, doc_type, version}
- tests: [{test_id, item, condition, expected_value, actual_result, pass_criteria, instrument, environment}]
- test_reports: [{report_id, conclusion}]
- test_measurements: [{machine_no, test_point, reading, unit, reference_value, condition}]
- persons: [{name, title}]
- identifiers: [{id_type, value}]
- products: [{product_id, name}]
- revision_records: [{seq, version, change_description, author, date}]
""" + BASE_INSTRUCTION,

    "bom": """你是医疗器械DHF文档信息抽取专家。当前文件是【BOM/组件清单】。
请从中抽取（JSON格式）：
- document: {title, doc_type, version}
- components: [{part_no, name, spec, model, ref_des, qty, criticality, rohs, board}]
- persons: [{name, title}]
- identifiers: [{id_type, value}]
- products: [{product_id, name}]
- revision_records: [{seq, version, change_description, author, date}]
""" + BASE_INSTRUCTION,

    "review_checklist": """你是医疗器械DHF文档信息抽取专家。当前文件是【评审检查表/评审记录】。
请从中抽取（JSON格式）：
- document: {title, doc_type, version}
- review_records: [{review_id, stage, date, conclusion}]
- review_items: [{seq, category, content, actual_situation, conclusion, improvement, note}]
  【重要】：必须抽取表格中的每一行评审条目，包括未勾选/未填写的！
  未勾选的条目 conclusion 填 null，actual_situation 填 null。
  这样后续可以检测"未完成"的检查项。
- persons: [{name, title}]
- identifiers: [{id_type, value}]
- products: [{product_id, name}]
- revision_records: [{seq, version, change_description, author, date}]
- semantic_fragments: [{fragment_type, content, topic_tags, related_subjects}]
""" + BASE_INSTRUCTION,

    "software_design": """你是医疗器械DHF文档信息抽取专家。当前文件是【软件设计文档】。
请从中抽取（JSON格式）：
- document: {title, doc_type, version}
- software_items: [{item_type, name, description, value, run_environment}]
- software_config_items: [{phase, activity, config_item, version}]
- functions: [{name, description, value}]
- persons: [{name, title}]
- identifiers: [{id_type, value}]
- products: [{product_id, name}]
- revision_records: [{seq, version, change_description, author, date}]
- semantic_fragments: [{fragment_type, content, topic_tags, related_subjects}]
  对于软件架构描述、接口说明、算法原理等长段落，放入 semantic_fragments。
""" + BASE_INSTRUCTION,

    "dev_plan": """你是医疗器械DHF文档信息抽取专家。当前文件是【开发计划/项目计划】。
请从中抽取（JSON格式）：
- document: {title, doc_type, version}
- plan_tasks: [{wbs, name, predecessor, start_date, end_date, owner, level, note}]
  每一行计划阶段/任务都应抽取为一条 plan_task。name = "主要工作内容"列，owner = "人员及资源配置"列。
- resources: [{name, type, standard, rate}]
- persons: [{name, title}]
- identifiers: [{id_type, value}]
- products: [{product_id, name}]
- revision_records: [{seq, version, change_description, author, date}]
- semantic_fragments: [{fragment_type, content, topic_tags, related_subjects}]
  【重要】：每行计划中的"质量要求"和"组织和技术接口"列内容很长，无法放入 plan_task 字段，
  请把它们整段作为 semantic_fragment 存入，fragment_type="constraint_statement"，
  在 related_subjects 中写上对应 plan_task 的 name，方便后续关联。
""" + BASE_INSTRUCTION,

    "dhf_index": """你是医疗器械DHF文档信息抽取专家。当前文件是【DHF清单/设计输出清单】。
请从中抽取（JSON格式）：
- document: {title, doc_type, version}
- doc_index_entries: [{seq, file_name, file_no, form, location, stage, signed, applicable, date}]
  【重要】：清单中每一行文件条目都必须完整抽取，不可遗漏！
  seq = 序号列，file_name = 文件名称列，file_no = 文件编号列，
  stage = 阶段列，date = 签字日期列，form = 存在形式列。
- persons: [{name, title}]
- identifiers: [{id_type, value}]
- products: [{product_id, name}]
- revision_records: [{seq, version, change_description, author, date}]
""" + BASE_INSTRUCTION,

    "general": """你是医疗器械DHF文档信息抽取专家。请从文件中抽取所有能识别的结构化信息。
输出JSON格式，可能包含的字段：
document, requirements, design_inputs, tests, functions, components,
review_items, software_items, plan_tasks, markets, intended_use_items,
persons, identifiers, products, regulations, revision_records, semantic_fragments
请根据文件实际内容判断哪些存在并抽取。
""" + BASE_INSTRUCTION,
}

PROMPTS["t1_prototype"] = PROMPTS["test_report"]
PROMPTS["design_output"] = PROMPTS["general"]
PROMPTS["structural_dhf"] = PROMPTS["review_checklist"]
PROMPTS["design_validation"] = PROMPTS["test_report"]


def chunk_text(text: str, max_chars: int = MAX_CHUNK_CHARS) -> list[str]:
    """Split text into chunks at heading or table-row boundaries."""
    if len(text) <= max_chars:
        return [text]

    # First try splitting at ## headings
    parts = re.split(r'(?=\n## )', text)

    # If no good split points, try splitting at any heading or blank line
    if len(parts) == 1 and len(text) > max_chars:
        parts = re.split(r'(?=\n(?:#{1,4} |\| ))', text)

    # Force-split any oversized parts by lines
    final_parts = []
    for part in parts:
        if len(part) <= max_chars:
            final_parts.append(part)
        else:
            lines = part.split("\n")
            sub = ""
            for line in lines:
                if len(sub) + len(line) + 1 > max_chars and sub:
                    final_parts.append(sub)
                    sub = line
                else:
                    sub = sub + "\n" + line if sub else line
            if sub:
                final_parts.append(sub)

    chunks = []
    current = ""
    for part in final_parts:
        if len(current) + len(part) > max_chars and current:
            chunks.append(current)
            current = part
        else:
            current += part
    if current:
        chunks.append(current)
    if not chunks:
        chunks = [text[:max_chars]]
    return chunks


def try_parse_json(text: str) -> dict:
    """Try to parse JSON, handling markdown wrapping, unescaped chars, and truncation."""
    if not text or not text.strip():
        return {}
    text = text.strip()

    # Strategy 1: extract content between ```json ... ``` using regex
    m = re.search(r'```(?:json|JSON)?\s*\r?\n(.*?)```', text, re.DOTALL)
    if m:
        text = m.group(1).strip()
    elif text.startswith("```"):
        first_nl = text.find("\n")
        if first_nl > 0:
            text = text[first_nl + 1:]
        if text.rstrip().endswith("```"):
            text = text.rstrip()[:-3].rstrip()
        text = text.strip()

    # Ensure text starts with {
    first_brace = text.find("{")
    if first_brace < 0:
        return {}
    if first_brace > 0:
        text = text[first_brace:]

    # Attempt 1: direct parse
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        pass

    # Attempt 2: fix unescaped control chars AND unescaped quotes in string values
    text_fixed = _fix_json_string_issues(text)
    try:
        return json.loads(text_fixed)
    except json.JSONDecodeError:
        pass

    # Attempt 3: repair truncated JSON
    for suffix in ['"}]}', '"}]', '"]', '"}', '}]', ']', '}', '"}]}}}',
                   '"}]}}', '"]}}}', ']}}}', '}}}', '}}', '"]}}',
                   '"\n    }\n  ]\n}', '"\n  ]\n}']:
        try:
            return json.loads(text_fixed + suffix)
        except json.JSONDecodeError:
            continue

    # Attempt 4: find the last valid top-level JSON object by brace counting
    brace_count = 0
    last_valid_pos = 0
    in_string = False
    escape_next = False
    for i, ch in enumerate(text_fixed):
        if escape_next:
            escape_next = False
            continue
        if ch == '\\' and in_string:
            escape_next = True
            continue
        if ch == '"' and not escape_next:
            in_string = not in_string
            continue
        if in_string:
            continue
        if ch == '{':
            brace_count += 1
        elif ch == '}':
            brace_count -= 1
            if brace_count == 0:
                last_valid_pos = i + 1
    if last_valid_pos > 0:
        try:
            return json.loads(text_fixed[:last_valid_pos])
        except json.JSONDecodeError:
            pass

    return {}


def _fix_json_string_issues(text: str) -> str:
    """Fix unescaped newlines, tabs and quotes inside JSON string values.
    
    Uses a state machine that tracks whether we're inside a JSON string.
    When inside a string, unescaped quotes that don't look like string terminators
    are escaped.
    """
    result = []
    i = 0
    in_string = False
    
    while i < len(text):
        ch = text[i]
        
        if not in_string:
            result.append(ch)
            if ch == '"':
                in_string = True
            i += 1
        else:
            # We're inside a JSON string
            if ch == '\\':
                # Escaped character - pass through both chars
                result.append(ch)
                if i + 1 < len(text):
                    result.append(text[i + 1])
                    i += 2
                else:
                    i += 1
            elif ch == '\n':
                result.append('\\n')
                i += 1
            elif ch == '\r':
                result.append('\\r')
                i += 1
            elif ch == '\t':
                result.append('\\t')
                i += 1
            elif ch == '"':
                # Is this quote a real string terminator or unescaped content?
                # Look ahead: if followed by valid JSON structure tokens, it's a terminator
                rest = text[i + 1:].lstrip()
                if not rest or rest[0] in ':,}]\n\r':
                    # Likely a real string terminator
                    result.append(ch)
                    in_string = False
                    i += 1
                else:
                    # Likely an unescaped quote inside string content
                    result.append('\\"')
                    i += 1
            else:
                result.append(ch)
                i += 1
    
    return ''.join(result)


def extract_file(filepath: Path) -> dict:
    """Extract nodes from a single file."""
    doc_type = detect_doc_type(str(filepath))
    prompt_key = doc_type if doc_type in PROMPTS else "general"
    system_prompt = PROMPTS[prompt_key]

    text = filepath.read_text(encoding="utf-8")
    chunks = chunk_text(text)

    all_results = []
    for i, chunk in enumerate(chunks):
        user_msg = f"【文件片段 {i+1}/{len(chunks)}】\n\n{chunk}"
        print(f"    chunk {i+1}/{len(chunks)} ({len(chunk)} chars)...", end="", flush=True)
        t0 = time.time()
        try:
            response = client.chat.completions.create(
                model=LLM_MODEL,
                max_tokens=LLM_MAX_TOKENS,
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_msg},
                ],
            )
            content = response.choices[0].message.content or ""
            truncated = response.choices[0].finish_reason == "length"
            parsed = try_parse_json(content)
            elapsed = time.time() - t0

            if truncated:
                print(f" TRUNCATED→partial ({elapsed:.1f}s)", flush=True)
            else:
                print(f" OK ({elapsed:.1f}s)", flush=True)

            if not parsed and content:
                print(f"    [WARN] parse failed, content len={len(content)}, first 150: {repr(content[:150])}", flush=True)

            if parsed:
                all_results.append(parsed)
        except Exception as e:
            elapsed = time.time() - t0
            print(f" ERROR ({elapsed:.1f}s): {e}", flush=True)

    return merge_dicts(all_results, doc_type)


def merge_dicts(results: list[dict], doc_type: str) -> dict:
    """Merge multiple chunk result dicts into one."""
    if not results:
        return {}
    if len(results) == 1:
        return results[0]

    merged = {}
    for r in results:
        for key, val in r.items():
            if isinstance(val, list):
                if key not in merged:
                    merged[key] = []
                merged[key].extend(val)
            elif isinstance(val, dict):
                if key not in merged:
                    merged[key] = val
                else:
                    merged[key].update({k: v for k, v in val.items() if v is not None})
            else:
                if key not in merged or merged[key] is None:
                    merged[key] = val
    return merged


def select_sample_files() -> list[Path]:
    """Select diverse sample files from different folders."""
    samples = [
        MARKDOWN_DIR / "01 立项批准书E0 23.11" / "客户需求书E0-血压计 23.6.via_xlsx.clean.md",
        MARKDOWN_DIR / "04 设计输入E0 23.11" / "设计输入汇总表E0  20211118.via_xlsx.clean.md",
        MARKDOWN_DIR / "11 T1样机" / "PT9L红外体温计检测报告 V1.0.via_lo_html.clean.md",
        MARKDOWN_DIR / "11 T1样机" / "PT9L包装BOM.via_xlsx.clean.md",
        MARKDOWN_DIR / "02 开发计划E0 23.11" / "设计开发计划表E0  23.11.via_xlsx.clean.md",
        MARKDOWN_DIR / "03 风险分析" / "PT9L--Attachment 7 02 Risk Assessment Report IFT-FXPJ01 V2.0 20240530--All applicable.via_lo_html.clean.md",
        MARKDOWN_DIR / "07 软件设计方案E0 23.11" / "软件需求E0 23.11" / "2-1 软件需求规格E0 23.11.via_lo_html.clean.md",
        MARKDOWN_DIR / "07 软件设计方案E0 23.11" / "软件需求E0 23.11" / "软件需求规格书评审检查表E0 23.11.via_xlsx.clean.md",
        MARKDOWN_DIR / "01 立项批准书E0 23.11" / "立项批准书E0 23.11.via_lo_html.clean.md",
        MARKDOWN_DIR / "PT9L-DHF清单-常规.via_xlsx.clean.md",
    ]
    return [f for f in samples if f.exists()]


def main():
    files = select_sample_files()
    print(f"=== Step 1: Extract Nodes (v2 - no instructor) ===", flush=True)
    print(f"Selected {len(files)} diverse sample files", flush=True)
    print(f"Model: {LLM_MODEL} | max_tokens: {LLM_MAX_TOKENS} | chunk_size: {MAX_CHUNK_CHARS}\n", flush=True)

    total_start = time.time()
    for i, filepath in enumerate(files, 1):
        rel = filepath.relative_to(MARKDOWN_DIR)
        doc_type = detect_doc_type(str(filepath))
        print(f"[{i}/{len(files)}] {rel}", flush=True)
        print(f"  doc_type: {doc_type}", flush=True)

        file_start = time.time()
        result = extract_file(filepath)
        file_elapsed = time.time() - file_start
        node_counts = {k: (len(v) if isinstance(v, list) else 1)
                       for k, v in result.items() if v}
        print(f"  nodes: {node_counts}", flush=True)

        rel_path = str(rel).replace("\\", "/")
        result["_meta"] = {
            "source_file": rel_path,
            "doc_type": doc_type,
        }

        out_name = str(rel).replace("/", "__").replace("\\", "__")
        out_name = re.sub(r'\.md$', '.json', out_name)
        out_path = PER_FILE_DIR / out_name
        out_path.write_text(json.dumps(result, ensure_ascii=False, indent=2),
                           encoding="utf-8")

        total_elapsed = time.time() - total_start
        avg_per_file = total_elapsed / i
        eta = avg_per_file * (len(files) - i)
        print(f"  done ({file_elapsed:.0f}s) | progress: {i}/{len(files)} | ETA: ~{eta:.0f}s\n", flush=True)

    total_elapsed = time.time() - total_start
    print(f"=== Step 1 Complete === ({total_elapsed:.0f}s total)", flush=True)


if __name__ == "__main__":
    main()
