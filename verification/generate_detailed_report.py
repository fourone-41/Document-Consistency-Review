"""生成详细过程报告"""
import json
from pathlib import Path
from config import OUTPUT_DIR


def main():
    raw_dir = OUTPUT_DIR / "raw_extraction"
    norm_dir = OUTPUT_DIR / "normalized"

    raw_files = {}
    for jf in sorted(raw_dir.glob("*.json")):
        if jf.name == "_summary.json":
            continue
        with open(jf, "r", encoding="utf-8") as f:
            raw_files[jf.stem] = json.load(f)

    norm_files = {}
    for jf in sorted(norm_dir.glob("*_normalized.json")):
        with open(jf, "r", encoding="utf-8") as f:
            norm_files[jf.stem] = json.load(f)

    with open(norm_dir / "_cross_file_comparison.json", "r", encoding="utf-8") as f:
        comparison = json.load(f)
    with open(norm_dir / "_stats.json", "r", encoding="utf-8") as f:
        stats = json.load(f)

    lines = []
    lines.append("# POC 详细过程报告")
    lines.append("")
    lines.append("> DeepSeek Chat API | 3 份文件 | 全流程验证")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === Section 1: Input Files ===
    lines.append("## 一、输入文件")
    lines.append("")
    lines.append("| # | 文件名 | 来源目录 | 大小 |")
    lines.append("|---|--------|----------|------|")
    for i, (name, data) in enumerate(raw_files.items(), 1):
        p = Path(data["source_path"])
        size = p.stat().st_size if p.exists() else 0
        lines.append(f"| {i} | {data['source_file']} | {p.parent.name} | {size:,} bytes |")
    lines.append("")
    lines.append("---")
    lines.append("")

    # === Section 2: Extraction Details ===
    lines.append("## 二、Step 1 信息抽取详细结果")
    lines.append("")

    for fname, data in raw_files.items():
        lines.append(f"### 文件: {data['source_file']}")
        lines.append("")
        lines.append(f"- Claims: **{data['total_claims']}** 个")
        lines.append(f"- SemanticFragments: **{data['total_fragments']}** 个")
        lines.append(f"- Identifiers: **{data['total_identifiers']}** 个")
        lines.append(f"- Persons: **{data['total_persons']}** 个")
        lines.append("")

        # Claims table
        lines.append("#### Claims 完整列表:")
        lines.append("")
        lines.append("| # | subject | attribute | value | unit | condition | source_section |")
        lines.append("|---|---------|-----------|-------|------|-----------|----------------|")
        for i, c in enumerate(data["claims"], 1):
            subj = c["subject"][:15]
            attr = c["attribute"][:12]
            val = (c.get("value") or "-")[:10]
            unit = (c.get("unit") or "-")[:5]
            cond = (c.get("condition") or "-")[:20]
            sec = c["source_section"][:25]
            lines.append(f"| {i} | {subj} | {attr} | {val} | {unit} | {cond} | {sec} |")
        lines.append("")

        # Fragments table
        lines.append("#### SemanticFragments 列表:")
        lines.append("")
        lines.append("| # | type | content(前50字) | topic_tags | related_subjects |")
        lines.append("|---|------|----------------|------------|------------------|")
        for i, frag in enumerate(data["fragments"], 1):
            content_short = frag["content"][:50].replace("|", "/").replace("\n", " ")
            tags = ", ".join(frag.get("topic_tags", [])[:3])
            related = ", ".join(frag.get("related_subjects", [])[:3])
            ftype = frag["fragment_type"][:20]
            lines.append(f"| {i} | {ftype} | {content_short} | {tags} | {related} |")
        lines.append("")

        # Identifiers
        if data["identifiers"]:
            lines.append("#### Identifiers:")
            lines.append("")
            lines.append("| id_type | value |")
            lines.append("|---------|-------|")
            for d in data["identifiers"]:
                lines.append(f"| {d['id_type']} | {d['value']} |")
            lines.append("")

        # Persons
        if data["persons"]:
            lines.append("#### Persons:")
            lines.append("")
            lines.append("| name | dept | title | role |")
            lines.append("|------|------|-------|------|")
            for p in data["persons"]:
                lines.append(f"| {p['name']} | {p.get('dept') or '-'} | {p.get('title') or '-'} | {p.get('role') or '-'} |")
            lines.append("")

        lines.append("---")
        lines.append("")

    # === Section 3: Normalization ===
    lines.append("## 三、Step 2 术语归一化详细结果")
    lines.append("")
    lines.append(f"- 术语表别名总数: **67** 个")
    lines.append(f"- 标准词总数: **18** 个")
    lines.append(f"- 总 Claims: **{stats['total_claims']}** 个")
    lines.append(f"- 成功归一化: **{stats['total_mapped']}** 个 ({stats['mapping_rate']*100:.1f}%)")
    lines.append(f"- 未归一化: **{stats['total_claims']-stats['total_mapped']}** 个 ({(1-stats['mapping_rate'])*100:.1f}%)")
    lines.append(f"- 跨文件对齐 subjects: **{stats['cross_file_subjects']}** 个")
    lines.append("")

    # Mapping examples
    lines.append("### 归一化映射详情（原始→标准词）")
    lines.append("")
    lines.append("| 原始 subject (文件中的写法) | 归一化为 (标准词) |")
    lines.append("|---------------------------|-----------------|")

    seen_mappings = set()
    for nf_data in norm_files.values():
        for c in nf_data.get("claims", []):
            orig = c.get("original_subject", "")
            norm = c.get("normalized_subject", "")
            if orig != norm and (orig, norm) not in seen_mappings:
                seen_mappings.add((orig, norm))

    for orig, norm in sorted(seen_mappings):
        lines.append(f"| {orig} | `{norm}` |")
    lines.append("")

    # Unmapped subjects
    lines.append("### 未归一化的 subjects（需要扩充术语表）")
    lines.append("")
    unmapped = []
    for nf_data in norm_files.values():
        for c in nf_data.get("claims", []):
            if c.get("original_subject") == c.get("normalized_subject"):
                subj = c["normalized_subject"]
                if subj not in unmapped:
                    unmapped.append(subj)

    for s in unmapped:
        lines.append(f"- `{s}`")
    lines.append("")

    # === Section 4: Cross-file alignment ===
    lines.append("---")
    lines.append("")
    lines.append("## 四、跨文件对齐详细结果")
    lines.append("")
    lines.append(f"共 **{stats['cross_file_subjects']}** 个参数在 2+ 份文件中被成功对齐:")
    lines.append("")

    for subject, info in comparison.items():
        lines.append(f"### `{subject}`")
        lines.append(f"- 比较方向: {info['direction']}")
        lines.append(f"- 涉及文件: {info['files_count']} 份")
        lines.append(f"- Claim 数: {info['claims_count']} 条")
        lines.append("")
        lines.append("| 来源文件 | value | unit | condition | raw_text |")
        lines.append("|----------|-------|------|-----------|----------|")
        for entry in info["entries"]:
            raw = (entry.get("raw_text") or "")[:45].replace("|", "/")
            f_name = entry["file"][:32]
            lines.append(f"| {f_name} | {entry.get('value') or '-'} | {entry.get('unit') or '-'} | {entry.get('condition') or '-'} | {raw} |")
        lines.append("")

    # === Section 5: Issues ===
    lines.append("---")
    lines.append("")
    lines.append("## 五、发现的问题与改进方向")
    lines.append("")
    lines.append("### 5.1 抽取质量问题")
    lines.append("")
    lines.append("1. **温度测试点误分类**: 检测报告中恒温水槽设定温度(32/35/42℃)被错误归入 measurement_accuracy，它们是测试条件不是精度值")
    lines.append("2. **attribute 不规范**: 同类参数 attribute 应统一(tolerance/range/threshold)，当前命名不一致")
    lines.append("3. **重复抽取**: 同一参数在不同测试条件出现时被多次抽取(如大气压力出现4次)")
    lines.append("4. **环境参数误归**: 测试环境温度(23℃)被归入 operating_temperature，实际是测试记录不是产品规格")
    lines.append("")
    lines.append("### 5.2 术语归一化问题")
    lines.append("")
    lines.append("1. **覆盖率 56.2%**: 还有 43.8% 未覆盖（测试条件类、电气参数类）")
    lines.append("2. **细粒度不足**: '电池寿命'和'产品寿命'被归为不同标准词，但检测报告中'五年或10000次'同时涉及两者")
    lines.append("3. **attribute 层面缺失**: 只对 subject 做了归一化，attribute 字段也需要标准化")
    lines.append("")
    lines.append("### 5.3 MVP 阶段改进计划")
    lines.append("")
    lines.append("| 改进项 | 优先级 | 预计效果 |")
    lines.append("|--------|--------|----------|")
    lines.append("| Prompt 增加'测试条件 vs 产品规格'区分指令 | HIGH | 减少误分类 50%+ |")
    lines.append("| 术语表扩展到 50+ 标准词 | HIGH | 归一化率提升到 80%+ |")
    lines.append("| 增加 attribute 归一化表 | MEDIUM | 跨文件匹配更精确 |")
    lines.append("| 冲突检测增加 condition 兼容性判断 | MEDIUM | 减少误报 |")
    lines.append("| 引入对齐引擎 Pairwise Verification | LOW(MVP后) | 精确判断数值关系 |")
    lines.append("")

    report_path = OUTPUT_DIR / "detailed_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"详细报告已生成: {report_path}")
    print(f"总行数: {len(lines)}")


if __name__ == "__main__":
    main()
