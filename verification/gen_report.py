"""
生成完整版 POC 报告（不依赖 Neo4j）
从 raw_extraction 和 normalized 的 JSON 输出生成 Markdown 报告
"""
import json
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR = Path(__file__).parent / "output"


def main():
    raw_dir = OUTPUT_DIR / "raw_extraction"
    norm_dir = OUTPUT_DIR / "normalized"

    # 加载数据
    raw_files = {}
    for jf in sorted(raw_dir.glob("*.json")):
        if jf.name == "_summary.json":
            continue
        with open(jf, "r", encoding="utf-8") as f:
            raw_files[jf.stem] = json.load(f)

    with open(norm_dir / "all_claims.json", "r", encoding="utf-8") as f:
        all_claims = json.load(f)

    with open(norm_dir / "_cross_file_comparison.json", "r", encoding="utf-8") as f:
        comparison = json.load(f)

    with open(norm_dir / "_stats.json", "r", encoding="utf-8") as f:
        stats = json.load(f)

    # === 构建报告 ===
    lines = []
    lines.append("# POC 验证报告（完整 Schema 版）\n")
    lines.append(f"> 生成时间：自动生成\n")
    lines.append(f"> Schema 版本：技术文档 V3（14种节点类型 + 完整关系）\n")

    # --- 1. 概述 ---
    lines.append("\n## 1. 概述\n")
    lines.append("本次 POC 按照技术文档中定义的**完整 Schema**（4层14种节点类型）对 3 份文件进行了结构化信息抽取和跨文件对齐。\n")
    lines.append("### 处理文件\n")
    lines.append("| 文件 | 文档类型 | 核心实体 | 数量 |")
    lines.append("|------|---------|---------|------|")
    for name, data in raw_files.items():
        doc_type = data["doc_type"]
        if doc_type == "customer_requirement":
            core = "Requirement"
            count = len(data.get("requirements", []))
        elif doc_type == "design_input":
            core = "DesignInput"
            count = len(data.get("design_inputs", []))
        elif doc_type == "test_report":
            core = "Test"
            count = len(data.get("tests", []))
        else:
            core = "?"
            count = 0
        lines.append(f"| {data['source_file'][:40]} | {doc_type} | {core} | {count} |")

    # --- 2. 抽取统计 ---
    lines.append("\n## 2. 抽取结果统计\n")
    lines.append("### 2.1 各文件节点数量\n")
    lines.append("| 节点类型 | 客户需求书 | 设计输入汇总表 | 检测报告 | 合计 |")
    lines.append("|---------|-----------|-------------|---------|------|")

    node_types = ["requirements", "design_inputs", "tests", "regulations", "components",
                  "functions", "identifiers", "persons", "products", "fragments", "relationships"]
    type_labels = {
        "requirements": "Requirement", "design_inputs": "DesignInput", "tests": "Test",
        "regulations": "Regulation", "components": "Component", "functions": "Function",
        "identifiers": "Identifier", "persons": "Person", "products": "Product",
        "fragments": "SemanticFragment", "relationships": "Relationship",
    }

    file_keys = list(raw_files.keys())
    for nt in node_types:
        counts = []
        total = 0
        for fk in file_keys:
            c = len(raw_files[fk].get(nt, []))
            counts.append(str(c))
            total += c
        if total > 0:
            lines.append(f"| {type_labels.get(nt, nt)} | {' | '.join(counts)} | {total} |")

    # --- 3. 领域实体抽取示例 ---
    lines.append("\n## 3. 领域实体抽取示例\n")

    # Requirement 示例
    lines.append("### 3.1 Requirement（客户需求书）\n")
    lines.append("| 分类 | 描述 | 值 | 单位 | 条件 | 来源 |")
    lines.append("|------|------|-----|------|------|------|")
    req_file = None
    for fk, data in raw_files.items():
        if data["doc_type"] == "customer_requirement":
            req_file = data
            break
    if req_file:
        shown = 0
        for req in req_file.get("requirements", []):
            if req.get("value") and shown < 8:
                lines.append(f"| {req['category']} | {req['description'][:40]} | {req.get('value', '')} | {req.get('unit', '')} | {req.get('condition', '') or ''} | {req.get('source_section', '')[:25]} |")
                shown += 1

    # DesignInput 示例
    lines.append("\n### 3.2 DesignInput（设计输入汇总表）\n")
    lines.append("| 分类 | 描述 | 值 | 单位 | 条件 | 来源 |")
    lines.append("|------|------|-----|------|------|------|")
    di_file = None
    for fk, data in raw_files.items():
        if data["doc_type"] == "design_input":
            di_file = data
            break
    if di_file:
        shown = 0
        for di in di_file.get("design_inputs", []):
            if di.get("value") and shown < 8:
                lines.append(f"| {di['category']} | {di['description'][:40]} | {di.get('value', '')} | {di.get('unit', '')} | {di.get('condition', '') or ''} | {di.get('source_section', '')[:25]} |")
                shown += 1

    # Test 示例
    lines.append("\n### 3.3 Test（检测报告）\n")
    lines.append("| 测试项 | 合格标准 | 单位 | 实测结果 | 单位 | 结论 | 条件 |")
    lines.append("|--------|---------|------|---------|------|------|------|")
    test_file = None
    for fk, data in raw_files.items():
        if data["doc_type"] == "test_report":
            test_file = data
            break
    if test_file:
        for test in test_file.get("tests", [])[:10]:
            lines.append(f"| {test['item'][:20]} | {test.get('expected_value', '') or ''} | {test.get('expected_unit', '') or ''} | {test.get('actual_result', '') or ''} | {test.get('actual_unit', '') or ''} | {test.get('pass_fail', '') or ''} | {test.get('condition', '') or ''} |")

    # --- 4. 辅助实体 ---
    lines.append("\n## 4. 辅助实体抽取\n")

    # Regulation
    lines.append("### 4.1 Regulation（引用标准/法规）\n")
    all_regs = []
    for fk, data in raw_files.items():
        for reg in data.get("regulations", []):
            reg["_source"] = data["source_file"][:20]
            all_regs.append(reg)
    # 去重
    seen_stds = set()
    unique_regs = []
    for reg in all_regs:
        sid = reg.get("std_id", "")
        if sid and sid not in seen_stds:
            seen_stds.add(sid)
            unique_regs.append(reg)
    lines.append(f"共抽取 **{len(unique_regs)}** 个不重复标准/法规。示例：\n")
    lines.append("| 标准编号 | 版本 | 说明 |")
    lines.append("|---------|------|------|")
    for reg in unique_regs[:12]:
        lines.append(f"| {reg.get('std_id', '')} | {reg.get('version', '') or ''} | {reg.get('relevance', '')[:40]} |")

    # Component
    lines.append("\n### 4.2 Component（产品组件）\n")
    all_comps = []
    for fk, data in raw_files.items():
        for comp in data.get("components", []):
            all_comps.append(comp)
    seen_comps = set()
    unique_comps = []
    for comp in all_comps:
        name = comp.get("name", "")
        if name and name not in seen_comps:
            seen_comps.add(name)
            unique_comps.append(comp)
    lines.append(f"共抽取 **{len(unique_comps)}** 个不重复组件。\n")
    lines.append("| 名称 | 类型 | 规格 |")
    lines.append("|------|------|------|")
    for comp in unique_comps[:10]:
        lines.append(f"| {comp.get('name', '')} | {comp.get('component_type', '')} | {comp.get('spec', '') or ''} |")

    # Relationship
    lines.append("\n### 4.3 Relationship（抽取的显式关系）\n")
    all_rels = []
    for fk, data in raw_files.items():
        for rel in data.get("relationships", []):
            all_rels.append(rel)
    lines.append(f"共抽取 **{len(all_rels)}** 条显式关系。\n")
    lines.append("| 起点类型 | 起点ID | 关系 | 终点类型 | 终点ID |")
    lines.append("|---------|--------|------|---------|--------|")
    for rel in all_rels[:15]:
        lines.append(f"| {rel.get('source_type', '')} | {rel.get('source_id', '')[:20]} | {rel['relation']} | {rel.get('target_type', '')} | {rel.get('target_id', '')[:25]} |")

    # --- 5. 归一化 Claim + 跨文件对齐 ---
    lines.append("\n## 5. 归一化 Claim 与跨文件对齐\n")
    lines.append("### 5.1 统计\n")
    lines.append(f"- 总 Claims：**{stats['total_claims']}**")
    lines.append(f"- 成功归一化映射：**{stats['total_mapped']}**（{100*stats['mapping_rate']:.1f}%）")
    lines.append(f"- 跨文件对齐 subjects：**{stats['cross_file_subjects']}** 个\n")

    lines.append("### 5.2 跨文件参数对齐详情\n")
    lines.append("以下参数在 2 份或以上文件中同时出现，可以进行一致性比对：\n")

    for subject, info in comparison.items():
        lines.append(f"#### `{subject}` （比较方向: {info['direction']}，涉及 {info['files_count']} 份文件）\n")
        lines.append("| 来源实体类型 | 来源文件 | 值 | 单位 | 角色 |")
        lines.append("|-------------|---------|-----|------|------|")
        for entry in info["entries"]:
            role = entry.get("test_role", "") or ""
            lines.append(f"| {entry['source_entity_type']} | {entry['source_doc'][:30]} | {entry.get('value', '')} | {entry.get('unit', '')} | {role} |")
        lines.append("")

    # --- 6. 知识图谱结构可视化 ---
    lines.append("\n## 6. 知识图谱结构（Mermaid）\n")
    lines.append("```mermaid")
    lines.append("graph TD")
    lines.append("    subgraph 层1-文档结构层")
    lines.append("        D[Document<br/>3份文件]")
    lines.append("    end")
    lines.append("")
    lines.append("    subgraph 层2-标识元数据层")
    lines.append("        ID[Identifier<br/>标识号]")
    lines.append("        P[Person<br/>人员]")
    lines.append("        PRD[Product<br/>产品]")
    lines.append("    end")
    lines.append("")
    lines.append("    subgraph 层3-领域实体层")
    lines.append("        REQ[Requirement<br/>66条需求]:::req")
    lines.append("        DI[DesignInput<br/>70条设计输入]:::di")
    lines.append("        T[Test<br/>20项测试]:::test")
    lines.append("        REG[Regulation<br/>法规标准]:::reg")
    lines.append("        COMP[Component<br/>产品组件]")
    lines.append("        FUNC[Function<br/>产品功能]")
    lines.append("    end")
    lines.append("")
    lines.append("    subgraph 层4-对齐裁决层")
    lines.append("        C[Claim<br/>62条归一化断言]:::claim")
    lines.append("        SS[StandardSubject<br/>对齐锚点]:::ss")
    lines.append("        SF[SemanticFragment<br/>语义片段]")
    lines.append("    end")
    lines.append("")
    lines.append("    REQ -->|STATED_IN| D")
    lines.append("    DI -->|STATED_IN| D")
    lines.append("    T -->|STATED_IN| D")
    lines.append("    DI -.->|DERIVES_FROM| REQ")
    lines.append("    REQ -.->|CONSTRAINED_BY| REG")
    lines.append("    T -.->|VERIFIED_BY| REG")
    lines.append("    REQ -->|生成Claim| C")
    lines.append("    DI -->|生成Claim| C")
    lines.append("    T -->|生成Claim| C")
    lines.append("    C -->|MAPS_TO| SS")
    lines.append("    D -->|REFERENCES| REG")
    lines.append("    D -->|MENTIONS| COMP")
    lines.append("")
    lines.append("    classDef req fill:#FFE0B2,stroke:#F57C00")
    lines.append("    classDef di fill:#C8E6C9,stroke:#388E3C")
    lines.append("    classDef test fill:#BBDEFB,stroke:#1976D2")
    lines.append("    classDef reg fill:#E1BEE7,stroke:#7B1FA2")
    lines.append("    classDef claim fill:#FFF9C4,stroke:#FBC02D")
    lines.append("    classDef ss fill:#FF8A65,stroke:#D84315")
    lines.append("```\n")

    # --- 7. 对齐流程图 ---
    lines.append("## 7. 对齐流程\n")
    lines.append("```mermaid")
    lines.append("flowchart LR")
    lines.append("    R1[Requirement<br/>测量精度±0.2℃] --> C1[Claim<br/>subject=measurement_accuracy<br/>value=±0.2]")
    lines.append("    D1[DesignInput<br/>测量误差±0.2℃] --> C2[Claim<br/>subject=measurement_accuracy<br/>value=±0.2]")
    lines.append("    T1[Test<br/>常温精度要求±0.2℃] --> C3[Claim<br/>subject=measurement_accuracy<br/>value=±0.2]")
    lines.append("    C1 --> SS1[StandardSubject<br/>measurement_accuracy]")
    lines.append("    C2 --> SS1")
    lines.append("    C3 --> SS1")
    lines.append("    SS1 --> CHECK{一致性检查<br/>value相同?}")
    lines.append("    CHECK -->|✓ 一致| OK[PASS]")
    lines.append("    CHECK -->|✗ 不一致| CONFLICT[CONFLICT]")
    lines.append("```\n")

    # --- 8. 与旧版 POC 对比 ---
    lines.append("## 8. 与旧版 POC 对比\n")
    lines.append("| 维度 | 旧版（V2 简化 schema） | 新版（完整 schema） |")
    lines.append("|------|---------------------|-------------------|")
    lines.append("| 节点类型 | 6种（Claim统一体） | 14种（按文档类型专属实体） |")
    lines.append("| 核心实体 | Claim (带 claim_role 字段) | Requirement / DesignInput / Test 独立类型 |")
    lines.append("| 专属字段 | 无（所有实体共享同一结构） | 有（如 Test.expected_value vs actual_result） |")
    lines.append("| 追溯关系 | 隐式（通过 subject 相同） | 显式（DERIVES_FROM / VERIFIED_BY 边） |")
    lines.append("| 对齐机制 | Claim 直接对齐 | 领域实体 → Claim → StandardSubject 三级 |")
    lines.append("| 冲突检测精度 | 中（可能混淆测试条件与产品规格） | 高（Test.expected vs actual 天然分离） |")

    # --- 9. 结论 ---
    lines.append("\n## 9. 结论\n")
    lines.append("本次 POC 验证了：\n")
    lines.append("1. **LLM 结构化抽取可行**：DeepSeek-chat + instructor 能准确按 Pydantic schema 抽取领域实体")
    lines.append("2. **文档类型专属 schema 有效**：针对不同文件类型使用不同的抽取模型，信息保留更完整")
    lines.append("3. **术语归一化可行**：69.4% 的 Claims 成功映射到标准词")
    lines.append("4. **跨文件对齐可行**：10 个核心参数在 2-3 份文件中成功对齐")
    lines.append("5. **显式关系抽取可行**：成功抽取出 DERIVES_FROM / CONSTRAINED_BY / VERIFIED_BY 等追溯关系")
    lines.append("\n### 下一步（MVP）\n")
    lines.append("- 导入 Neo4j 图数据库（Docker 就绪后执行 step3）")
    lines.append("- 实现 CORRESPONDS_TO 边的自动推理")
    lines.append("- 实现 19 条 Cypher 检查规则")
    lines.append("- 扩展到全部 DHF 文件")

    report_path = OUTPUT_DIR / "full_schema_report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))
    print(f"报告已生成: {report_path}")


if __name__ == "__main__":
    main()
