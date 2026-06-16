"""
Step 1: 按文档类型做 LLM 结构化信息抽取（完整 schema 版）

对每种文档类型使用专属的 Pydantic 模型和 Prompt：
- customer_requirement → RequirementDocExtraction
- design_input → DesignInputDocExtraction
- test_report → TestReportDocExtraction

输出：output/raw_extraction/<filename>.json
"""
import json
import re
from pathlib import Path

import instructor
from openai import OpenAI

from config import API_KEY, LLM_BASE_URL, LLM_MODEL, SOURCE_FILES, OUTPUT_DIR, DOC_TYPE_MAP
from schema import (
    RequirementDocExtraction,
    DesignInputDocExtraction,
    TestReportDocExtraction,
)

client = instructor.from_openai(
    OpenAI(api_key=API_KEY, base_url=LLM_BASE_URL)
)

# ===== 针对不同文档类型的 System Prompt =====

PROMPT_REQUIREMENT = """你是医疗器械文档信息抽取专家。当前文档是【客户需求书】。

你需要从中抽取以下信息：

1. **Requirement（需求条目）** —— 核心抽取对象！每一条客户需求/性能/功能要求都必须抽取：
   - req_id: 需求编号（如有，否则 null）
   - category: 通用/功能/性能/组件/法规/安全/接口/其他
   - description: 需求描述原文（完整保留该行/该条的内容）
   - value: 量化值（只填数值部分，如 "±0.2"、"32.0-42.9"、"1000"）
   - unit: 单位（℃、次、年、%RH、kPa 等）
   - condition: 适用条件（如 "35-42℃范围内"）
   - verification_method: 验证方法（测试/分析/检查/评审，如有）
   - source_section: 来源位置（如 "Sheet:性能规格 > Row3"）

2. **Regulation（引用的标准/法规）**：
   - std_id: 标准编号（如 "IEC60529"、"ROHS(2011/65/EU)"）
   - version: 版本/年份
   - clause: 条款号
   - requirement_text: 法规要求
   - relevance: 与产品的关系

3. **Component（产品组件/部件）**：
   - name: 组件名称
   - component_type: sensor/display/structure/pcb/battery/optical/packaging/other
   - spec: 规格属性

4. **Function（产品功能）**：
   - name: 功能名称（如 "体温测量"、"发热报警"、"记忆功能"）
   - description: 功能描述

5. **Identifier（标识号）**：产品编号、项目号、版本号等
6. **Person（人员）**：姓名、部门、职务、角色
7. **Product（产品）**：产品编号、型号、名称、目标市场
8. **SemanticFragment（语义片段）**：无法量化但重要的描述性段落
9. **Relationship（关系）**：
   - Requirement → CONSTRAINED_BY → Regulation（需求引用了哪个标准）

**重要规则：**
- 表格中每一行如果包含技术参数，都必须单独抽取为一个 Requirement
- value 只填数值部分（不含单位）
- 如果一个参数有多个条件下的不同值，拆分为多个 Requirement
- 不要遗漏任何有技术含量的需求条目
"""

PROMPT_DESIGN_INPUT = """你是医疗器械文档信息抽取专家。当前文档是【设计输入汇总表】。

你需要从中抽取以下信息：

1. **DesignInput（设计输入条目）** —— 核心抽取对象！每一条设计输入都必须抽取：
   - di_id: 设计输入编号（如有，否则 null）
   - category: 通用/功能/性能/组件/法规/安全/接口/其他
   - description: 设计输入描述原文（完整保留）
   - value: 量化值（只填数值部分）
   - unit: 单位
   - condition: 适用条件
   - source_req_id: 来源需求编号（如果文档中注明了该设计输入来源于哪条需求）
   - source_section: 来源位置（如 "Sheet:性能 > Row5"）

2. **Regulation（引用的标准/法规）**
3. **Component（产品组件/部件）**
4. **Function（产品功能）**
5. **Identifier（标识号）**
6. **Person（人员）**
7. **Product（产品）**
8. **SemanticFragment（语义片段）**
9. **Relationship（关系）**：
   - DesignInput → DERIVES_FROM → Requirement（设计输入来源于哪条需求）
   - DesignInput → CONSTRAINED_BY → Regulation（设计输入引用了哪个标准）

**重要规则：**
- 表格中每一行如果包含设计输入参数，都必须单独抽取
- 注意区分"设计输入本身"和"其引用的来源需求"
- source_req_id 如果原文中有类似"来源：XXX"字样则填写
"""

PROMPT_TEST_REPORT = """你是医疗器械文档信息抽取专家。当前文档是【检测报告】。

你需要从中抽取以下信息：

1. **Test（单项测试）** —— 核心抽取对象！每一个测试项目都必须抽取：
   - test_id: 测试编号（如有，否则 null）
   - item: 测试项目名称（如 "常温精度测试"、"跌落测试"）
   - condition: 测试条件/环境（如 "室温23±2℃, 湿度55%RH"）
   - expected_value: 预期结果/合格标准值（只填数值，如 "±0.2"）
   - expected_unit: 预期值单位（如 "℃"）
   - actual_result: 实际测试结果值（只填数值，如 "0.1"、"-0.1~0.2"）
   - actual_unit: 实际值单位
   - pass_fail: 单项结论 PASS/FAIL/N/A
   - source_section: 来源位置

2. **TestReport（报告整体信息）**：
   - report_title: 报告标题
   - conclusion: 整体结论 PASS/FAIL/CONDITIONAL
   - test_date: 测试日期
   - equipment: 使用设备

3. **Regulation（引用的标准/法规）**
4. **Component（产品组件/部件）**
5. **Identifier（标识号）**
6. **Person（人员）**
7. **Product（产品）**
8. **SemanticFragment（语义片段）**
9. **Relationship（关系）**：
   - Test → VERIFIED_BY → Regulation（测试依据哪个标准）

**重要规则：**
- 严格区分 expected_value（标准要求/合格标准）和 actual_result（实际测到的值）
- condition 是测试环境条件（如室温23℃），不是产品规格
- 表格中"要求"列 → expected_value，"检测结果"列 → actual_result
- 如果同一测试项有多个测试机/多次测量，拆分为多个 Test
"""

DOC_TYPE_CONFIG = {
    "customer_requirement": {
        "prompt": PROMPT_REQUIREMENT,
        "model": RequirementDocExtraction,
    },
    "design_input": {
        "prompt": PROMPT_DESIGN_INPUT,
        "model": DesignInputDocExtraction,
    },
    "test_report": {
        "prompt": PROMPT_TEST_REPORT,
        "model": TestReportDocExtraction,
    },
}


def split_into_chunks(content: str, max_chars: int = 3500) -> list[dict]:
    """按 markdown 章节标题/表格拆分，每个 chunk 不超过 max_chars"""
    sections = re.split(r'(?=^## |\n\|[- ])', content, flags=re.MULTILINE)
    chunks = []
    current_chunk = ""
    current_heading = "文件开头"

    for section in sections:
        heading_match = re.match(r'^##\s+(.+)', section)
        if heading_match:
            current_heading = heading_match.group(1).strip()

        if len(current_chunk) + len(section) > max_chars and current_chunk:
            chunks.append({"heading": current_heading, "text": current_chunk})
            current_chunk = section
        else:
            current_chunk += section

    if current_chunk.strip():
        chunks.append({"heading": current_heading, "text": current_chunk})

    return chunks


def extract_from_chunk(chunk_text: str, source_file: str, chunk_heading: str, doc_type: str):
    """对单个 chunk 调用 LLM 做结构化抽取，返回对应文档类型的 Pydantic 模型实例"""
    config = DOC_TYPE_CONFIG[doc_type]

    user_prompt = f"""请从以下文档片段中抽取所有结构化信息。

**来源文件**：{source_file}
**当前章节**：{chunk_heading}

---
{chunk_text}
---

请严格按照 schema 输出 JSON。如果某类信息在本片段中不存在，返回空列表即可。"""

    result = client.chat.completions.create(
        model=LLM_MODEL,
        response_model=config["model"],
        messages=[
            {"role": "system", "content": config["prompt"]},
            {"role": "user", "content": user_prompt},
        ],
        temperature=0.1,
        max_retries=2,
    )
    return result


def merge_results(results: list, doc_type: str) -> dict:
    """合并多个 chunk 的抽取结果"""
    merged = {}

    if doc_type == "customer_requirement":
        merged["requirements"] = []
        merged["regulations"] = []
        merged["components"] = []
        merged["functions"] = []
        merged["identifiers"] = []
        merged["persons"] = []
        merged["products"] = []
        merged["fragments"] = []
        merged["relationships"] = []
        for r in results:
            merged["requirements"].extend([x.model_dump() for x in r.requirements])
            merged["regulations"].extend([x.model_dump() for x in r.regulations])
            merged["components"].extend([x.model_dump() for x in r.components])
            merged["functions"].extend([x.model_dump() for x in r.functions])
            merged["identifiers"].extend([x.model_dump() for x in r.identifiers])
            merged["persons"].extend([x.model_dump() for x in r.persons])
            merged["products"].extend([x.model_dump() for x in r.products])
            merged["fragments"].extend([x.model_dump() for x in r.fragments])
            merged["relationships"].extend([x.model_dump() for x in r.relationships])

    elif doc_type == "design_input":
        merged["design_inputs"] = []
        merged["regulations"] = []
        merged["components"] = []
        merged["functions"] = []
        merged["identifiers"] = []
        merged["persons"] = []
        merged["products"] = []
        merged["fragments"] = []
        merged["relationships"] = []
        for r in results:
            merged["design_inputs"].extend([x.model_dump() for x in r.design_inputs])
            merged["regulations"].extend([x.model_dump() for x in r.regulations])
            merged["components"].extend([x.model_dump() for x in r.components])
            merged["functions"].extend([x.model_dump() for x in r.functions])
            merged["identifiers"].extend([x.model_dump() for x in r.identifiers])
            merged["persons"].extend([x.model_dump() for x in r.persons])
            merged["products"].extend([x.model_dump() for x in r.products])
            merged["fragments"].extend([x.model_dump() for x in r.fragments])
            merged["relationships"].extend([x.model_dump() for x in r.relationships])

    elif doc_type == "test_report":
        merged["test_report"] = None
        merged["tests"] = []
        merged["regulations"] = []
        merged["components"] = []
        merged["identifiers"] = []
        merged["persons"] = []
        merged["products"] = []
        merged["fragments"] = []
        merged["relationships"] = []
        for r in results:
            if r.test_report and not merged["test_report"]:
                merged["test_report"] = r.test_report.model_dump()
            merged["tests"].extend([x.model_dump() for x in r.tests])
            merged["regulations"].extend([x.model_dump() for x in r.regulations])
            merged["components"].extend([x.model_dump() for x in r.components])
            merged["identifiers"].extend([x.model_dump() for x in r.identifiers])
            merged["persons"].extend([x.model_dump() for x in r.persons])
            merged["products"].extend([x.model_dump() for x in r.products])
            merged["fragments"].extend([x.model_dump() for x in r.fragments])
            merged["relationships"].extend([x.model_dump() for x in r.relationships])

    return merged


def process_file(filepath: Path) -> dict:
    """处理单个文件"""
    print(f"\n{'='*60}")
    print(f"处理文件: {filepath.name}")
    print(f"{'='*60}")

    doc_type = DOC_TYPE_MAP.get(filepath.name, "unknown")
    if doc_type not in DOC_TYPE_CONFIG:
        print(f"  [SKIP] 未知文档类型: {doc_type}")
        return None

    print(f"  文档类型: {doc_type}")
    print(f"  使用模型: {DOC_TYPE_CONFIG[doc_type]['model'].__name__}")

    content = filepath.read_text(encoding="utf-8")
    chunks = split_into_chunks(content)
    print(f"  拆分为 {len(chunks)} 个 chunks")

    chunk_results = []
    for i, chunk in enumerate(chunks):
        print(f"  处理 chunk {i+1}/{len(chunks)}: {chunk['heading'][:40]}...")
        try:
            result = extract_from_chunk(
                chunk["text"],
                filepath.name,
                chunk["heading"],
                doc_type,
            )
            chunk_results.append(result)

            # 打印该 chunk 的抽取统计
            stats = []
            if doc_type == "customer_requirement":
                stats.append(f"Reqs:{len(result.requirements)}")
            elif doc_type == "design_input":
                stats.append(f"DIs:{len(result.design_inputs)}")
            elif doc_type == "test_report":
                stats.append(f"Tests:{len(result.tests)}")
            stats.append(f"Regs:{len(result.regulations)}")
            stats.append(f"Comps:{len(result.components)}")
            stats.append(f"Rels:{len(result.relationships)}")
            print(f"    -> {' | '.join(stats)}")

        except Exception as e:
            print(f"    [ERROR] {e}")
            continue

    merged = merge_results(chunk_results, doc_type)
    merged["source_file"] = filepath.name
    merged["source_path"] = str(filepath)
    merged["doc_type"] = doc_type

    # 打印总结
    print(f"\n  === 抽取汇总 ===")
    for key, val in merged.items():
        if isinstance(val, list):
            print(f"    {key}: {len(val)}")
        elif isinstance(val, dict) and val:
            print(f"    {key}: (present)")

    return merged


def main():
    output_dir = OUTPUT_DIR / "raw_extraction"
    output_dir.mkdir(parents=True, exist_ok=True)

    all_results = []
    for filepath in SOURCE_FILES:
        if not filepath.exists():
            print(f"[WARN] 文件不存在: {filepath}")
            continue
        result = process_file(filepath)
        if result:
            all_results.append(result)
            out_file = output_dir / f"{filepath.stem}.json"
            with open(out_file, "w", encoding="utf-8") as f:
                json.dump(result, f, ensure_ascii=False, indent=2)
            print(f"  输出: {out_file}")

    # 生成摘要
    summary = {"total_files": len(all_results), "files": []}
    for r in all_results:
        file_summary = {"name": r["source_file"], "doc_type": r["doc_type"]}
        for key, val in r.items():
            if isinstance(val, list):
                file_summary[key] = len(val)
        summary["files"].append(file_summary)

    with open(output_dir / "_summary.json", "w", encoding="utf-8") as f:
        json.dump(summary, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print("全部抽取完成！")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
