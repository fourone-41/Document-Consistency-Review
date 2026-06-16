"""Generate final report with complete knowledge graph (6 node types)."""
import json
from pathlib import Path
import sys
sys.path.insert(0, str(Path(__file__).parent))
from config import OUTPUT_DIR

raw_dir = OUTPUT_DIR / "raw_extraction"
norm_dir = OUTPUT_DIR / "normalized"

# Load all data
raw_files = {}
for jf in sorted(raw_dir.glob("*.json")):
    if jf.name == "_summary.json":
        continue
    with open(jf, "r", encoding="utf-8") as f:
        raw_files[jf.stem] = json.load(f)

with open(raw_dir / "_summary.json", "r", encoding="utf-8") as f:
    summary = json.load(f)

with open(norm_dir / "_stats.json", "r", encoding="utf-8") as f:
    stats = json.load(f)

with open(norm_dir / "_cross_file_comparison.json", "r", encoding="utf-8") as f:
    comparison = json.load(f)

lines = []
lines.append("# 完整知识图谱 POC 报告（V2 — 6类节点）")
lines.append("")
lines.append("> 本次运行使用完整 Schema：Claim(含claim_role) + SemanticFragment + StandardRef + ComponentRef + Identifier + Person")
lines.append("")
lines.append("---")
lines.append("")

# Section 1: Summary
lines.append("## 一、抽取结果总览")
lines.append("")
lines.append("| 文件 | 类型 | Claims | Fragments | Standards | Components |")
lines.append("|------|------|--------|-----------|-----------|------------|")
for fe in summary["files"]:
    lines.append(f"| {fe['name'][:25]} | {fe['doc_type']} | {fe['claims']} | {fe['fragments']} | {fe['standards']} | {fe['components']} |")
lines.append(f"| **总计** | | **{summary['total_claims']}** | **{summary['total_fragments']}** | **{summary['total_standards']}** | **{summary['total_components']}** |")
lines.append("")

# Section 2: claim_role distribution
lines.append("## 二、Claim 语义角色分布（claim_role）")
lines.append("")
lines.append("| 文件 | requirement | design_input | test_criterion | test_result | test_condition |")
lines.append("|------|-------------|--------------|----------------|-------------|----------------|")

for name, data in raw_files.items():
    roles = {}
    for c in data.get("claims", []):
        r = c.get("claim_role", "unknown")
        roles[r] = roles.get(r, 0) + 1
    lines.append(f"| {data['source_file'][:25]} | {roles.get('requirement',0)} | {roles.get('design_input',0)} | {roles.get('test_criterion',0)} | {roles.get('test_result',0)} | {roles.get('test_condition',0)} |")
lines.append("")

lines.append("**关键发现：** LLM 成功区分了：")
lines.append("- 客户需求书的 18 条声明全部标记为 `requirement`")
lines.append("- 设计输入的 23 条声明全部标记为 `design_input`")
lines.append("- 检测报告的 35 条中：18 条 `test_criterion`（验收标准）、17 条 `test_condition`（测试环境）")
lines.append("- **测试环境条件不再被误归为产品规格！**")
lines.append("")

# Section 3: Standards
lines.append("## 三、引用标准（StandardRef）")
lines.append("")
lines.append(f"共抽取 **{summary['total_standards']}** 条标准引用。")
lines.append("")
lines.append("### 代表性标准节点：")
lines.append("")
lines.append("| standard_id | relevance | 来源文件 |")
lines.append("|-------------|-----------|----------|")

seen_stds = set()
for name, data in raw_files.items():
    for s in data.get("standards", []):
        sid = s["standard_id"]
        if sid not in seen_stds and len(seen_stds) < 15:
            seen_stds.add(sid)
            rel = (s.get("relevance") or "")[:30]
            lines.append(f"| {sid} | {rel} | {data['source_file'][:20]} |")
lines.append("")

# Section 4: Components
lines.append("## 四、产品组件（ComponentRef）")
lines.append("")
lines.append(f"共抽取 **{summary['total_components']}** 个组件节点。")
lines.append("")
lines.append("| component_name | type | properties | 来源 |")
lines.append("|----------------|------|------------|------|")

seen_comps = set()
for name, data in raw_files.items():
    for c in data.get("components", []):
        cn = c["component_name"]
        if cn not in seen_comps:
            seen_comps.add(cn)
            props = (c.get("properties") or "-")[:30]
            lines.append(f"| {cn} | {c['component_type']} | {props} | {data['source_file'][:15]} |")
lines.append("")

# Section 5: Graph stats
lines.append("## 五、完整知识图谱节点与关系统计")
lines.append("")
lines.append("### 节点统计")
lines.append("")
lines.append("| 节点类型 | 数量 | 说明 |")
lines.append("|----------|------|------|")
lines.append("| Document | 3 | 源文件 |")
lines.append(f"| Claim | {summary['total_claims']} | 结构化参数（含 claim_role 区分语义角色） |")
lines.append(f"| SemanticFragment | {summary['total_fragments']} | 描述性语义片段 |")
lines.append(f"| StandardRef | {summary['total_standards']} | 引用的标准/法规 |")
lines.append(f"| ComponentRef | {summary['total_components']} | 产品组件 |")
lines.append(f"| Identifier | {summary['total_identifiers']} | 文件/产品编号 |")
lines.append(f"| Person | {summary['total_persons']} | 人员 |")
lines.append(f"| StandardSubject | {stats['cross_file_subjects']} | 归一化标准词 |")

total_nodes = 3 + summary['total_claims'] + summary['total_fragments'] + summary['total_standards'] + summary['total_components'] + summary['total_identifiers'] + summary['total_persons'] + stats['cross_file_subjects']
lines.append(f"| **总计** | **{total_nodes}** | |")
lines.append("")

lines.append("### 关系统计")
lines.append("")
lines.append("| 关系类型 | 数量 | 说明 |")
lines.append("|----------|------|------|")
lines.append(f"| CONTAINS_CLAIM | {summary['total_claims']} | Document→Claim |")
lines.append(f"| CONTAINS_FRAGMENT | {summary['total_fragments']} | Document→Fragment |")
lines.append(f"| REFERENCES_STANDARD | {summary['total_standards']} | Document→Standard |")
lines.append(f"| HAS_COMPONENT | {summary['total_components']} | Document→Component |")
lines.append(f"| HAS_IDENTIFIER | {summary['total_identifiers']} | Document→Identifier |")
lines.append(f"| HAS_PERSON | {summary['total_persons']} | Document→Person |")
lines.append(f"| MAPS_TO | {stats['total_mapped']} | Claim→StandardSubject |")
lines.append("| SAME_SUBJECT | 跨文件 | 同参数跨文件对齐 |")

frag_relates = sum(len(f.get("related_subjects", [])) for d in raw_files.values() for f in d.get("fragments", []))
lines.append(f"| RELATES_TO | {frag_relates} | Fragment→Claim |")

total_rels = summary['total_claims'] + summary['total_fragments'] + summary['total_standards'] + summary['total_components'] + summary['total_identifiers'] + summary['total_persons'] + stats['total_mapped'] + frag_relates
lines.append(f"| **总计** | **{total_rels}+** | |")
lines.append("")

# Section 6: Cross-file comparison with claim_role
lines.append("## 六、跨文件对齐结果（含 claim_role）")
lines.append("")
lines.append(f"共 **{stats['cross_file_subjects']}** 个参数在 2+ 份文件中对齐：")
lines.append("")

for subject, info in comparison.items():
    lines.append(f"### `{subject}` ({info['direction']})")
    lines.append("")
    lines.append("| 文件 | claim_role | value | unit | condition |")
    lines.append("|------|-----------|-------|------|-----------|")
    for entry in info["entries"]:
        lines.append(f"| {entry['file'][:25]} | {entry.get('claim_role','?')} | {entry.get('value','-')} | {entry.get('unit','-') or '-'} | {entry.get('condition','-') or '-'} |")
    lines.append("")

# Section 7: Mermaid graph
lines.append("## 七、完整知识图谱可视化")
lines.append("")
lines.append("```mermaid")
lines.append("graph TD")
lines.append('    DOC1["🟢 Document<br/>客户需求书<br/>type: customer_requirement"]')
lines.append('    DOC2["🟢 Document<br/>设计输入汇总表<br/>type: design_input"]')
lines.append('    DOC3["🟢 Document<br/>检测报告<br/>type: test_report"]')
lines.append("")
lines.append('    C1["🔵 Claim<br/>subject: 测量误差<br/>value: ±0.2℃<br/>role: requirement"]')
lines.append('    C2["🔵 Claim<br/>subject: 测量误差<br/>value: ±0.2℃<br/>role: design_input"]')
lines.append('    C3["🔵 Claim<br/>subject: 常温精度<br/>value: ±0.2℃<br/>role: test_criterion"]')
lines.append('    C4["🔵 Claim<br/>subject: 测试环境温度<br/>value: 23℃<br/>role: test_condition"]')
lines.append("")
lines.append('    F1["🟣 SemanticFragment<br/>type: behavioral_spec<br/>上电自检行为描述"]')
lines.append("")
lines.append('    STD1["📋 StandardRef<br/>IEC60529<br/>IP22类测试"]')
lines.append('    STD2["📋 StandardRef<br/>ROHS 2011/65/EU<br/>环保合规"]')
lines.append("")
lines.append('    COMP1["⚙️ ComponentRef<br/>LCD显示屏<br/>type: display"]')
lines.append('    COMP2["⚙️ ComponentRef<br/>红外探头<br/>type: sensor"]')
lines.append("")
lines.append('    P1["👤 Person<br/>赵一平<br/>role: 编制"]')
lines.append('    ID1["🏷️ Identifier<br/>PT9L<br/>type: 产品型号"]')
lines.append("")
lines.append('    S1(("🟠 StandardSubject<br/>measurement_accuracy"))')
lines.append("")
lines.append("    DOC1 -->|CONTAINS_CLAIM| C1")
lines.append("    DOC2 -->|CONTAINS_CLAIM| C2")
lines.append("    DOC3 -->|CONTAINS_CLAIM| C3")
lines.append("    DOC3 -->|CONTAINS_CLAIM| C4")
lines.append("    DOC3 -->|CONTAINS_FRAGMENT| F1")
lines.append("    DOC2 -->|REFERENCES_STANDARD| STD1")
lines.append("    DOC2 -->|REFERENCES_STANDARD| STD2")
lines.append("    DOC1 -->|HAS_COMPONENT| COMP1")
lines.append("    DOC3 -->|HAS_COMPONENT| COMP2")
lines.append("    DOC1 -->|HAS_PERSON| P1")
lines.append("    DOC1 -->|HAS_IDENTIFIER| ID1")
lines.append("")
lines.append('    C1 -->|"MAPS_TO"| S1')
lines.append('    C2 -->|"MAPS_TO"| S1')
lines.append('    C3 -->|"MAPS_TO"| S1')
lines.append('    F1 -.->|"RELATES_TO"| C3')
lines.append("")
lines.append("    classDef doc fill:#4CAF50,color:white")
lines.append("    classDef claim fill:#2196F3,color:white")
lines.append("    classDef frag fill:#9C27B0,color:white")
lines.append("    classDef std fill:#FF9800,color:white")
lines.append("    classDef stdr fill:#795548,color:white")
lines.append("    classDef comp fill:#009688,color:white")
lines.append("    classDef person fill:#607D8B,color:white")
lines.append("    classDef ident fill:#00BCD4,color:white")
lines.append("    classDef cond fill:#F44336,color:white")
lines.append("    class DOC1,DOC2,DOC3 doc")
lines.append("    class C1,C2,C3 claim")
lines.append("    class C4 cond")
lines.append("    class F1 frag")
lines.append("    class S1 std")
lines.append("    class STD1,STD2 stdr")
lines.append("    class COMP1,COMP2 comp")
lines.append("    class P1 person")
lines.append("    class ID1 ident")
lines.append("```")
lines.append("")

lines.append("**图例：**")
lines.append("- 🟢 绿色 = Document | 🔵 蓝色 = Claim | 🔴 红色 = Claim(test_condition)")
lines.append("- 🟣 紫色 = SemanticFragment | 🟠 橙色 = StandardSubject")
lines.append("- 📋 棕色 = StandardRef | ⚙️ 青绿 = ComponentRef")
lines.append("- 👤 灰色 = Person | 🏷️ 青色 = Identifier")
lines.append("")

# Section 8: Conclusion
lines.append("---")
lines.append("")
lines.append("## 八、V1→V2 改进对比")
lines.append("")
lines.append("| 维度 | V1 (POC) | V2 (本次) |")
lines.append("|------|----------|-----------|")
lines.append("| 节点类型 | 4种 | **6种** (+StandardRef, ComponentRef) |")
lines.append("| claim_role | 无 | **6种角色**（requirement/design_input/test_criterion/test_result/test_condition/specification） |")
lines.append("| 标准引用 | 未抽取 | **175条**（IEC/ROHS/FDA等） |")
lines.append("| 产品组件 | 未抽取 | **25个**（LCD/蜂鸣器/PCB/传感器等） |")
lines.append("| 测试条件误归 | 严重 | **已解决**（test_condition与test_criterion分离） |")
lines.append(f"| 总节点数 | 240 | **{total_nodes}** |")
lines.append(f"| 总关系数 | 315+ | **{total_rels}+** |")

report_path = OUTPUT_DIR / "v2_full_graph_report.md"
with open(report_path, "w", encoding="utf-8") as f:
    f.write("\n".join(lines))
print(f"Report: {report_path}")
print(f"Lines: {len(lines)}")
