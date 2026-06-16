"""
Step 2: 术语归一化 + 从领域实体生成 Claim + 跨文件对齐

核心逻辑：
1. 从 Requirement 生成 Claim (source_entity_type="Requirement")
2. 从 DesignInput 生成 Claim (source_entity_type="DesignInput")
3. 从 Test 生成 Claim (source_entity_type="Test", 分 expected/actual)
4. 对所有 Claim 的 subject 做术语归一化
5. 按 normalized_subject 做跨文件对齐

输入：output/raw_extraction/*.json
输出：output/normalized/claims.json + _cross_file_comparison.json + _stats.json
"""
import json
from pathlib import Path
from collections import defaultdict

import yaml

from config import OUTPUT_DIR


def load_terminology(yaml_path: Path) -> tuple[dict, dict]:
    """加载术语归一化表"""
    with open(yaml_path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f)

    alias_map = {}
    direction_map = {}
    for standard_key, info in raw.items():
        direction_map[standard_key] = info.get("direction", "exact_match")
        for alias in info.get("aliases", []):
            alias_map[alias.lower()] = standard_key

    return alias_map, direction_map


def normalize_subject(subject: str, alias_map: dict[str, str]) -> str:
    """将 subject 映射为标准词"""
    subject_lower = subject.lower().strip()
    if subject_lower in alias_map:
        return alias_map[subject_lower]
    for alias, std in alias_map.items():
        if alias in subject_lower or subject_lower in alias:
            return std
    return subject


def requirements_to_claims(data: dict, alias_map: dict) -> list[dict]:
    """从客户需求书的 Requirement 列表生成 Claims"""
    claims = []
    for req in data.get("requirements", []):
        if not req.get("value"):
            continue
        subject_raw = req.get("description", "")[:20]
        # 用 category + description 前缀构造 subject
        # 但更好的做法是从 description 中提取核心参数名
        subject_raw = extract_subject_from_description(req.get("description", ""), req.get("category", ""))
        std_subject = normalize_subject(subject_raw, alias_map)

        claims.append({
            "subject_raw": subject_raw,
            "subject": std_subject,
            "attribute": infer_attribute(req.get("value", "")),
            "value": req.get("value"),
            "unit": req.get("unit"),
            "condition": req.get("condition"),
            "raw_text": req.get("description", ""),
            "source_entity_type": "Requirement",
            "source_entity_id": req.get("req_id"),
            "source_doc": data["source_file"],
            "source_section": req.get("source_section", ""),
            "category": req.get("category"),
            "verification_method": req.get("verification_method"),
        })
    return claims


def design_inputs_to_claims(data: dict, alias_map: dict) -> list[dict]:
    """从设计输入汇总表的 DesignInput 列表生成 Claims"""
    claims = []
    for di in data.get("design_inputs", []):
        if not di.get("value"):
            continue
        subject_raw = extract_subject_from_description(di.get("description", ""), di.get("category", ""))
        std_subject = normalize_subject(subject_raw, alias_map)

        claims.append({
            "subject_raw": subject_raw,
            "subject": std_subject,
            "attribute": infer_attribute(di.get("value", "")),
            "value": di.get("value"),
            "unit": di.get("unit"),
            "condition": di.get("condition"),
            "raw_text": di.get("description", ""),
            "source_entity_type": "DesignInput",
            "source_entity_id": di.get("di_id"),
            "source_doc": data["source_file"],
            "source_section": di.get("source_section", ""),
            "category": di.get("category"),
            "source_req_id": di.get("source_req_id"),
        })
    return claims


def tests_to_claims(data: dict, alias_map: dict) -> list[dict]:
    """从检测报告的 Test 列表生成 Claims（每个 Test 可能产生2条：expected + actual）"""
    claims = []
    for test in data.get("tests", []):
        item = test.get("item", "")
        subject_raw = extract_subject_from_test_item(item)
        std_subject = normalize_subject(subject_raw, alias_map)

        # 合格标准 → Claim (attribute=criterion)
        if test.get("expected_value"):
            claims.append({
                "subject_raw": subject_raw,
                "subject": std_subject,
                "attribute": "criterion",
                "value": test["expected_value"],
                "unit": test.get("expected_unit"),
                "condition": test.get("condition"),
                "raw_text": f"{item}: 要求 {test['expected_value']}{test.get('expected_unit', '')}",
                "source_entity_type": "Test",
                "source_entity_id": test.get("test_id"),
                "source_doc": data["source_file"],
                "source_section": test.get("source_section", ""),
                "test_role": "expected",
            })

        # 实际结果 → Claim (attribute=actual)
        if test.get("actual_result"):
            claims.append({
                "subject_raw": subject_raw,
                "subject": std_subject,
                "attribute": "actual",
                "value": test["actual_result"],
                "unit": test.get("actual_unit"),
                "condition": test.get("condition"),
                "raw_text": f"{item}: 实测 {test['actual_result']}{test.get('actual_unit', '')}",
                "source_entity_type": "Test",
                "source_entity_id": test.get("test_id"),
                "source_doc": data["source_file"],
                "source_section": test.get("source_section", ""),
                "test_role": "actual",
                "pass_fail": test.get("pass_fail"),
            })

    return claims


def extract_subject_from_description(description: str, category: str = "") -> str:
    """从需求/设计输入描述中提取核心参数名作为 subject"""
    keywords = [
        "测量精度", "测量误差", "精度", "测量范围", "测温范围", "温度范围",
        "显示分辨率", "分辨率", "工作温度", "工作环境", "环境温度",
        "存储温度", "贮存温度", "电池寿命", "使用寿命", "产品寿命",
        "自动关机", "关机时间", "防水等级", "IP等级",
        "相对湿度", "湿度", "大气压力", "气压",
        "产品型号", "型号", "项目编号",
        "测量模式", "测量位置", "报警阈值", "发热报警",
        "低电压检测", "低电压检出", "错误显示", "温度单位",
        "跌落", "静电", "电磁兼容", "EMC",
    ]
    desc_lower = description.lower()
    for kw in keywords:
        if kw in description:
            return kw

    # 取描述前10个字作为 subject
    clean = description.replace("\n", "").strip()
    return clean[:15] if clean else category


def extract_subject_from_test_item(item: str) -> str:
    """从测试项目名称中提取 subject"""
    keywords = [
        "常温精度", "精度", "测量精度", "测量误差",
        "测量范围", "测温范围", "显示分辨率", "分辨率",
        "工作温度", "环境温度", "存储温度", "贮存温度",
        "电池寿命", "使用寿命", "自动关机",
        "跌落", "静电", "电磁兼容", "EMC",
        "防水", "密封", "IP",
    ]
    for kw in keywords:
        if kw in item:
            return kw
    return item[:15]


def infer_attribute(value: str) -> str:
    """根据 value 格式推断 attribute 类型"""
    if not value:
        return "value"
    if "±" in value or "+" in value or "-" in value:
        if "-" in value and "±" not in value and value[0] != "-":
            return "range"
        return "tolerance"
    if "~" in value or "-" in value.replace("-", "", 1):
        return "range"
    return "value"


def main():
    raw_dir = OUTPUT_DIR / "raw_extraction"
    norm_dir = OUTPUT_DIR / "normalized"
    norm_dir.mkdir(parents=True, exist_ok=True)

    terminology_path = Path(__file__).parent / "terminology.yaml"
    alias_map, direction_map = load_terminology(terminology_path)
    print(f"加载术语表: {len(alias_map)} 个别名 -> {len(direction_map)} 个标准词")

    all_claims = []
    all_file_stats = []

    json_files = sorted(raw_dir.glob("*.json"))
    json_files = [f for f in json_files if f.name != "_summary.json"]

    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            data = json.load(f)

        doc_type = data.get("doc_type", "unknown")
        source_file = data.get("source_file", jf.name)
        print(f"\n处理: {source_file} ({doc_type})")

        claims = []
        if doc_type == "customer_requirement":
            claims = requirements_to_claims(data, alias_map)
            print(f"  从 {len(data.get('requirements', []))} 个 Requirement 生成 {len(claims)} 个 Claims")
        elif doc_type == "design_input":
            claims = design_inputs_to_claims(data, alias_map)
            print(f"  从 {len(data.get('design_inputs', []))} 个 DesignInput 生成 {len(claims)} 个 Claims")
        elif doc_type == "test_report":
            claims = tests_to_claims(data, alias_map)
            print(f"  从 {len(data.get('tests', []))} 个 Test 生成 {len(claims)} 个 Claims")

        mapped_count = sum(1 for c in claims if c["subject_raw"] != c["subject"])
        print(f"  归一化: {mapped_count}/{len(claims)} 成功映射")

        all_claims.extend(claims)
        all_file_stats.append({
            "file": source_file,
            "doc_type": doc_type,
            "claims_generated": len(claims),
            "mapped": mapped_count,
            "unmapped": len(claims) - mapped_count,
        })

    # 保存所有 claims
    with open(norm_dir / "all_claims.json", "w", encoding="utf-8") as f:
        json.dump(all_claims, f, ensure_ascii=False, indent=2)

    # 跨文件对齐：按 normalized subject 分组
    subject_index = defaultdict(list)
    for claim in all_claims:
        subject_index[claim["subject"]].append(claim)

    comparison = {}
    for subject, claims in sorted(subject_index.items()):
        files_involved = set(c["source_doc"] for c in claims)
        if len(files_involved) >= 2:
            entries = []
            for c in claims:
                entries.append({
                    "source_doc": c["source_doc"][:35],
                    "source_entity_type": c["source_entity_type"],
                    "attribute": c.get("attribute"),
                    "value": c.get("value"),
                    "unit": c.get("unit"),
                    "condition": c.get("condition"),
                    "raw_text": c.get("raw_text", "")[:100],
                    "test_role": c.get("test_role"),
                })
            comparison[subject] = {
                "direction": direction_map.get(subject, "unknown"),
                "files_count": len(files_involved),
                "claims_count": len(claims),
                "entries": entries,
            }

    with open(norm_dir / "_cross_file_comparison.json", "w", encoding="utf-8") as f:
        json.dump(comparison, f, ensure_ascii=False, indent=2)

    # 打印跨文件对比
    print(f"\n{'='*60}")
    print(f"跨文件参数对齐（出现在 2+ 份文件）：")
    print(f"{'='*60}")
    for subject, info in comparison.items():
        print(f"\n  [{subject}] (方向: {info['direction']}, {info['files_count']} 份文件, {info['claims_count']} 条)")
        for entry in info["entries"]:
            val_str = f"{entry['value']} {entry['unit'] or ''}" if entry["value"] else "(无数值)"
            role = f" [{entry['test_role']}]" if entry.get("test_role") else ""
            print(f"    {entry['source_entity_type']:<13} {entry['source_doc']:<35} -> {val_str}{role}")

    # 统计
    stats = {
        "total_claims": len(all_claims),
        "total_mapped": sum(s["mapped"] for s in all_file_stats),
        "mapping_rate": round(sum(s["mapped"] for s in all_file_stats) / max(len(all_claims), 1), 3),
        "cross_file_subjects": len(comparison),
        "all_subjects": list(subject_index.keys()),
        "file_stats": all_file_stats,
    }

    with open(norm_dir / "_stats.json", "w", encoding="utf-8") as f:
        json.dump(stats, f, ensure_ascii=False, indent=2)

    print(f"\n{'='*60}")
    print(f"归一化统计:")
    print(f"  总 Claims: {stats['total_claims']}")
    print(f"  成功映射: {stats['total_mapped']} ({100*stats['mapping_rate']:.1f}%)")
    print(f"  跨文件对齐 subjects: {stats['cross_file_subjects']} 个")
    print(f"{'='*60}")


if __name__ == "__main__":
    main()
