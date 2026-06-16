"""
Step 3: 导入 Neo4j（完整 schema 版）

创建节点：Document, Requirement, DesignInput, Test, Regulation, Component, 
          Function, Identifier, Person, Product, Claim, SemanticFragment
创建边：STATED_IN, DERIVES_FROM, CONSTRAINED_BY, VERIFIED_BY, CORRESPONDS_TO, CONFLICTS_WITH

输入：output/raw_extraction/*.json + output/normalized/all_claims.json
输出：Neo4j 图数据库 + output/neo4j_report.md
"""
import json
from pathlib import Path

from neo4j import GraphDatabase

from config import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, OUTPUT_DIR


def clear_database(session):
    session.run("MATCH (n) DETACH DELETE n")
    print("  数据库已清空")


def create_constraints(session):
    constraints = [
        "CREATE CONSTRAINT IF NOT EXISTS FOR (d:Document) REQUIRE d.name IS UNIQUE",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (s:StandardSubject) REQUIRE s.name IS UNIQUE",
    ]
    for c in constraints:
        session.run(c)
    print("  约束已创建")


def import_documents(session, raw_dir: Path):
    """导入 Document 节点"""
    json_files = sorted(raw_dir.glob("*.json"))
    json_files = [f for f in json_files if f.name != "_summary.json"]

    doc_count = 0
    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            data = json.load(f)
        session.run(
            "MERGE (d:Document {name: $name}) SET d.doc_type = $doc_type, d.path = $path",
            name=data["source_file"],
            doc_type=data["doc_type"],
            path=data.get("source_path", ""),
        )
        doc_count += 1
    print(f"  Document 节点: {doc_count}")
    return doc_count


def import_requirements(session, raw_dir: Path):
    """导入 Requirement 节点"""
    count = 0
    jf = raw_dir / "客户需求书E0-血压计 23.6.via_xlsx.clean.json"
    if not jf.exists():
        return 0
    with open(jf, "r", encoding="utf-8") as f:
        data = json.load(f)
    source_file = data["source_file"]

    for i, req in enumerate(data.get("requirements", [])):
        req_id = req.get("req_id") or f"REQ-{i+1:03d}"
        session.run("""
            CREATE (r:Requirement {
                req_id: $req_id,
                category: $category,
                description: $description,
                value: $value,
                unit: $unit,
                condition: $condition,
                verification_method: $verification_method,
                source_section: $source_section
            })
            WITH r
            MATCH (d:Document {name: $doc_name})
            MERGE (r)-[:STATED_IN]->(d)
        """,
            req_id=req_id,
            category=req.get("category", "其他"),
            description=req.get("description", ""),
            value=req.get("value"),
            unit=req.get("unit"),
            condition=req.get("condition"),
            verification_method=req.get("verification_method"),
            source_section=req.get("source_section", ""),
            doc_name=source_file,
        )
        count += 1
    print(f"  Requirement 节点: {count}")
    return count


def import_design_inputs(session, raw_dir: Path):
    """导入 DesignInput 节点"""
    count = 0
    jf = raw_dir / "设计输入汇总表E0  20211118.via_xlsx.clean.json"
    if not jf.exists():
        return 0
    with open(jf, "r", encoding="utf-8") as f:
        data = json.load(f)
    source_file = data["source_file"]

    for i, di in enumerate(data.get("design_inputs", [])):
        di_id = di.get("di_id") or f"DI-{i+1:03d}"
        session.run("""
            CREATE (di:DesignInput {
                di_id: $di_id,
                category: $category,
                description: $description,
                value: $value,
                unit: $unit,
                condition: $condition,
                source_req_id: $source_req_id,
                source_section: $source_section
            })
            WITH di
            MATCH (d:Document {name: $doc_name})
            MERGE (di)-[:STATED_IN]->(d)
        """,
            di_id=di_id,
            category=di.get("category", "其他"),
            description=di.get("description", ""),
            value=di.get("value"),
            unit=di.get("unit"),
            condition=di.get("condition"),
            source_req_id=di.get("source_req_id"),
            source_section=di.get("source_section", ""),
            doc_name=source_file,
        )
        count += 1
    print(f"  DesignInput 节点: {count}")
    return count


def import_tests(session, raw_dir: Path):
    """导入 Test 节点"""
    count = 0
    jf = raw_dir / "PT9L红外体温计检测报告 V1.0.via_lo_html.clean.json"
    if not jf.exists():
        return 0
    with open(jf, "r", encoding="utf-8") as f:
        data = json.load(f)
    source_file = data["source_file"]

    for i, test in enumerate(data.get("tests", [])):
        test_id = test.get("test_id") or f"TEST-{i+1:03d}"
        session.run("""
            CREATE (t:Test {
                test_id: $test_id,
                item: $item,
                condition: $condition,
                expected_value: $expected_value,
                expected_unit: $expected_unit,
                actual_result: $actual_result,
                actual_unit: $actual_unit,
                pass_fail: $pass_fail,
                source_section: $source_section
            })
            WITH t
            MATCH (d:Document {name: $doc_name})
            MERGE (t)-[:STATED_IN]->(d)
        """,
            test_id=test_id,
            item=test.get("item", ""),
            condition=test.get("condition"),
            expected_value=test.get("expected_value"),
            expected_unit=test.get("expected_unit"),
            actual_result=test.get("actual_result"),
            actual_unit=test.get("actual_unit"),
            pass_fail=test.get("pass_fail"),
            source_section=test.get("source_section", ""),
            doc_name=source_file,
        )
        count += 1
    print(f"  Test 节点: {count}")
    return count


def import_regulations(session, raw_dir: Path):
    """导入 Regulation 节点（去重合并）"""
    all_regs = {}
    json_files = sorted(raw_dir.glob("*.json"))
    json_files = [f for f in json_files if f.name != "_summary.json"]

    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            data = json.load(f)
        source_file = data["source_file"]
        for reg in data.get("regulations", []):
            std_id = reg.get("std_id", "").strip()
            if not std_id:
                continue
            if std_id not in all_regs:
                all_regs[std_id] = {**reg, "source_docs": [source_file]}
            else:
                all_regs[std_id]["source_docs"].append(source_file)

    for std_id, reg in all_regs.items():
        session.run("""
            MERGE (reg:Regulation {std_id: $std_id})
            SET reg.version = $version,
                reg.clause = $clause,
                reg.requirement_text = $req_text,
                reg.relevance = $relevance
        """,
            std_id=std_id,
            version=reg.get("version"),
            clause=reg.get("clause"),
            req_text=reg.get("requirement_text"),
            relevance=reg.get("relevance", ""),
        )
        for doc in reg["source_docs"]:
            session.run("""
                MATCH (reg:Regulation {std_id: $std_id})
                MATCH (d:Document {name: $doc_name})
                MERGE (d)-[:REFERENCES]->(reg)
            """, std_id=std_id, doc_name=doc)

    print(f"  Regulation 节点: {len(all_regs)}")
    return len(all_regs)


def import_components(session, raw_dir: Path):
    """导入 Component 节点（去重合并）"""
    all_comps = {}
    json_files = sorted(raw_dir.glob("*.json"))
    json_files = [f for f in json_files if f.name != "_summary.json"]

    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            data = json.load(f)
        source_file = data["source_file"]
        for comp in data.get("components", []):
            name = comp.get("name", "").strip()
            if not name:
                continue
            if name not in all_comps:
                all_comps[name] = {**comp, "source_docs": [source_file]}
            else:
                all_comps[name]["source_docs"].append(source_file)

    for name, comp in all_comps.items():
        session.run("""
            MERGE (c:Component {name: $name})
            SET c.component_type = $comp_type,
                c.spec = $spec
        """,
            name=name,
            comp_type=comp.get("component_type", "other"),
            spec=comp.get("spec"),
        )
        for doc in comp["source_docs"]:
            session.run("""
                MATCH (c:Component {name: $name})
                MATCH (d:Document {name: $doc_name})
                MERGE (d)-[:MENTIONS]->(c)
            """, name=name, doc_name=doc)

    print(f"  Component 节点: {len(all_comps)}")
    return len(all_comps)


def import_claims_and_alignment(session, norm_dir: Path):
    """导入 Claim 节点 + StandardSubject 对齐节点"""
    claims_file = norm_dir / "all_claims.json"
    if not claims_file.exists():
        print("  [WARN] all_claims.json 不存在")
        return 0, 0

    with open(claims_file, "r", encoding="utf-8") as f:
        claims = json.load(f)

    claim_count = 0
    subjects_created = set()

    for i, claim in enumerate(claims):
        claim_id = f"CLAIM-{i+1:04d}"
        subject = claim.get("subject", "unknown")

        # 创建 Claim 节点
        session.run("""
            CREATE (c:Claim {
                claim_id: $claim_id,
                subject: $subject,
                attribute: $attribute,
                value: $value,
                unit: $unit,
                condition: $condition,
                raw_text: $raw_text,
                source_entity_type: $entity_type,
                source_doc: $source_doc,
                source_section: $source_section
            })
        """,
            claim_id=claim_id,
            subject=subject,
            attribute=claim.get("attribute", "value"),
            value=claim.get("value"),
            unit=claim.get("unit"),
            condition=claim.get("condition"),
            raw_text=claim.get("raw_text", "")[:200],
            entity_type=claim.get("source_entity_type", ""),
            source_doc=claim.get("source_doc", ""),
            source_section=claim.get("source_section", ""),
        )

        # 关联到 Document
        session.run("""
            MATCH (c:Claim {claim_id: $claim_id})
            MATCH (d:Document {name: $doc_name})
            MERGE (c)-[:STATED_IN]->(d)
        """, claim_id=claim_id, doc_name=claim.get("source_doc", ""))

        # 创建 StandardSubject 并关联
        if subject not in subjects_created:
            session.run("MERGE (s:StandardSubject {name: $name})", name=subject)
            subjects_created.add(subject)
        session.run("""
            MATCH (c:Claim {claim_id: $claim_id})
            MATCH (s:StandardSubject {name: $subject})
            MERGE (c)-[:MAPS_TO]->(s)
        """, claim_id=claim_id, subject=subject)

        claim_count += 1

    print(f"  Claim 节点: {claim_count}")
    print(f"  StandardSubject 节点: {len(subjects_created)}")
    return claim_count, len(subjects_created)


def import_relationships(session, raw_dir: Path):
    """导入抽取阶段识别的显式关系"""
    rel_count = 0
    json_files = sorted(raw_dir.glob("*.json"))
    json_files = [f for f in json_files if f.name != "_summary.json"]

    for jf in json_files:
        with open(jf, "r", encoding="utf-8") as f:
            data = json.load(f)
        for rel in data.get("relationships", []):
            relation = rel.get("relation", "")
            source_id = rel.get("source_id", "")
            target_id = rel.get("target_id", "")
            if not relation or not source_id or not target_id:
                continue
            # 存为通用 Relationship 节点关联（简化处理）
            session.run("""
                MERGE (rel:ExtractedRelation {
                    source_type: $source_type,
                    source_id: $source_id,
                    relation: $relation,
                    target_type: $target_type,
                    target_id: $target_id
                })
            """,
                source_type=rel.get("source_type", ""),
                source_id=source_id,
                relation=relation,
                target_type=rel.get("target_type", ""),
                target_id=target_id,
            )
            rel_count += 1

    print(f"  ExtractedRelation: {rel_count}")
    return rel_count


def run_verification_queries(session) -> list[dict]:
    """执行验证查询"""
    results = []

    # 查询1：跨文件同一 subject 的数值差异
    print("\n  === 查询1: 跨文件数值差异 ===")
    query_result = session.run("""
        MATCH (c1:Claim)-[:MAPS_TO]->(s:StandardSubject)<-[:MAPS_TO]-(c2:Claim)
        WHERE c1.source_doc <> c2.source_doc AND c1.value IS NOT NULL AND c2.value IS NOT NULL
        AND c1.value <> c2.value
        RETURN s.name AS subject, 
               c1.source_entity_type AS type1, c1.source_doc AS doc1, c1.value AS val1, c1.unit AS unit1,
               c2.source_entity_type AS type2, c2.source_doc AS doc2, c2.value AS val2, c2.unit AS unit2
        ORDER BY s.name
    """)
    conflicts = []
    for record in query_result:
        conflict = dict(record)
        conflicts.append(conflict)
        print(f"    {conflict['subject']}: {conflict['type1']}({conflict['val1']}{conflict['unit1'] or ''}) "
              f"vs {conflict['type2']}({conflict['val2']}{conflict['unit2'] or ''})")
    results.append({"query": "cross_file_value_diff", "count": len(conflicts), "data": conflicts})

    # 查询2：图谱统计
    print("\n  === 查询2: 图谱统计 ===")
    stats_result = session.run("""
        MATCH (n)
        RETURN labels(n)[0] AS label, count(n) AS count
        ORDER BY count DESC
    """)
    node_stats = []
    for record in stats_result:
        node_stats.append({"label": record["label"], "count": record["count"]})
        print(f"    {record['label']}: {record['count']}")
    results.append({"query": "node_stats", "data": node_stats})

    # 查询3：跨文件对齐的 subject 数量
    print("\n  === 查询3: 跨文件对齐 ===")
    align_result = session.run("""
        MATCH (s:StandardSubject)<-[:MAPS_TO]-(c:Claim)
        WITH s, count(DISTINCT c.source_doc) AS doc_count, collect(DISTINCT c.source_entity_type) AS types
        WHERE doc_count >= 2
        RETURN s.name AS subject, doc_count, types
        ORDER BY doc_count DESC
    """)
    alignments = []
    for record in align_result:
        alignments.append(dict(record))
        print(f"    {record['subject']}: {record['doc_count']} 份文件, 类型={record['types']}")
    results.append({"query": "alignment", "count": len(alignments), "data": alignments})

    return results


def generate_report(output_dir: Path, stats: dict, query_results: list[dict]):
    """生成导入报告"""
    report = []
    report.append("# Neo4j 知识图谱导入报告\n")
    report.append("## 节点统计\n")
    for item in query_results[1]["data"]:
        report.append(f"- **{item['label']}**: {item['count']}")
    report.append("")

    report.append("## 跨文件对齐\n")
    if len(query_results) > 2:
        for align in query_results[2].get("data", []):
            report.append(f"- **{align['subject']}**: {align['doc_count']} 份文件 (类型: {align['types']})")
    report.append("")

    report.append("## 跨文件数值差异（潜在冲突）\n")
    if query_results[0]["data"]:
        report.append("| Subject | 来源1 | 值1 | 来源2 | 值2 |")
        report.append("|---------|--------|-----|--------|-----|")
        seen = set()
        for c in query_results[0]["data"]:
            key = f"{c['subject']}-{c['doc1']}-{c['doc2']}"
            if key in seen:
                continue
            seen.add(key)
            report.append(f"| {c['subject']} | {c['type1']}@{c['doc1'][:20]} | {c['val1']}{c['unit1'] or ''} | {c['type2']}@{c['doc2'][:20]} | {c['val2']}{c['unit2'] or ''} |")
    else:
        report.append("未发现跨文件数值差异。")

    with open(output_dir / "neo4j_report.md", "w", encoding="utf-8") as f:
        f.write("\n".join(report))
    print(f"\n  报告已生成: {output_dir / 'neo4j_report.md'}")


def main():
    raw_dir = OUTPUT_DIR / "raw_extraction"
    norm_dir = OUTPUT_DIR / "normalized"

    print("连接 Neo4j...")
    driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))

    try:
        with driver.session() as session:
            print("\n[1/8] 清空数据库")
            clear_database(session)

            print("[2/8] 创建约束")
            create_constraints(session)

            print("[3/8] 导入 Document 节点")
            import_documents(session, raw_dir)

            print("[4/8] 导入 Requirement 节点")
            import_requirements(session, raw_dir)

            print("[5/8] 导入 DesignInput 节点")
            import_design_inputs(session, raw_dir)

            print("[6/8] 导入 Test 节点")
            import_tests(session, raw_dir)

            print("[7/8] 导入 Regulation + Component 节点")
            import_regulations(session, raw_dir)
            import_components(session, raw_dir)

            print("[8/8] 导入 Claim + StandardSubject")
            import_claims_and_alignment(session, norm_dir)
            import_relationships(session, raw_dir)

            print("\n" + "="*60)
            print("执行验证查询...")
            print("="*60)
            query_results = run_verification_queries(session)

            generate_report(OUTPUT_DIR, {}, query_results)

    finally:
        driver.close()
        print("\nNeo4j 连接已关闭。")


if __name__ == "__main__":
    main()
