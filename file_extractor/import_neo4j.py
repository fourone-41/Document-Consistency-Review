"""
Import extracted graph (merged_graph.json) into Neo4j.
V2: Fixed field mappings, added ReviewItem/DocIndexEntry/SemanticFragment support.
"""
import json
import argparse
from pathlib import Path
from neo4j import GraphDatabase

MERGED = Path(__file__).parent / "output" / "merged_graph.json"


def clear_db(tx):
    tx.run("MATCH (n) DETACH DELETE n")


def create_constraints(tx):
    for label in ["Document", "Requirement", "Risk", "RiskControl", "Function",
                  "Regulation", "Person", "Product", "DesignInput", "Test",
                  "PlanTask", "SoftwareItem", "Component", "Market", "IntendedUse",
                  "Identifier", "Claim", "ReviewItem", "DocIndexEntry", "SemanticFragment",
                  "TestReport", "TestMeasurement", "RevisionRecord"]:
        try:
            tx.run(f"CREATE INDEX IF NOT EXISTS FOR (n:{label}) ON (n.uid)")
        except:
            pass


def uid(node_type, data, source):
    """Generate a pseudo-unique id for matching."""
    if node_type == "Test":
        return f"{source}::test::{data.get('test_id', '')}"
    if node_type == "Requirement":
        return f"{source}::req::{data.get('req_id', '')}"
    if node_type == "PlanTask":
        return f"{source}::task::{data.get('name', '')[:40]}"
    if node_type == "ReviewItem":
        return f"{source}::ri::{data.get('seq', data.get('content', '')[:30])}"
    if node_type == "DocIndexEntry":
        return f"{source}::die::{data.get('seq', data.get('file_name', '')[:30])}"
    return ""


def batch_create_nodes(session, label, items, prop_map):
    """Create nodes of given label with property mapping."""
    for item in items:
        props = {}
        for neo_prop, json_keys in prop_map.items():
            if isinstance(json_keys, str):
                json_keys = [json_keys]
            val = None
            for k in json_keys:
                val = item.get(k)
                if val is not None and val != "":
                    break
            props[neo_prop] = str(val) if val is not None else ""

        props["source"] = item.get("_source", "")
        param_list = ", ".join(f"{k}: ${k}" for k in props)
        set_clause = ", ".join(f"n.{k} = ${k}" for k in props)
        query = f"MERGE (n:{label} {{{param_list}}}) SET {set_clause}"
        try:
            session.run(query, **props)
        except Exception as e:
            pass


def import_nodes(session, nodes, claims):
    print("Creating Document nodes...", flush=True)
    for doc in nodes.get("documents", []):
        session.run("""
            MERGE (d:Document {title: $title, source: $source})
            SET d.doc_type = $doc_type, d.version = $version, d.date = $date
        """, title=doc.get("title", ""), source=doc.get("_source", ""),
            doc_type=doc.get("doc_type", ""), version=doc.get("version") or "",
            date=doc.get("date") or "")

    print("Creating Requirement nodes...", flush=True)
    for r in nodes.get("requirements", []):
        session.run("""
            MERGE (n:Requirement {uid: $uid})
            SET n.req_id=$req_id, n.category=$category, n.description=$desc,
                n.value=$value, n.unit=$unit, n.condition=$cond, n.source=$source
        """, uid=f"{r.get('_source','')}::req::{r.get('req_id','')}",
            req_id=str(r.get("req_id", "")), category=r.get("category") or "",
            desc=r.get("description") or "", value=r.get("value") or "",
            unit=r.get("unit") or "", cond=r.get("condition") or "",
            source=r.get("_source", ""))

    print("Creating Risk nodes...", flush=True)
    for r in nodes.get("risks", []):
        session.run("""
            MERGE (n:Risk {uid: $uid})
            SET n.hazard=$hazard, n.situation=$situation, n.phase=$phase, n.source=$source
        """, uid=f"{r.get('_source','')}::risk::{r.get('hazard','')}::{r.get('hazardous_situation','')[:30]}",
            hazard=r.get("hazard", ""), situation=r.get("hazardous_situation") or "",
            phase=r.get("phase") or "", source=r.get("_source", ""))

    print("Creating RiskControl nodes...", flush=True)
    for rc in nodes.get("risk_controls", []):
        session.run("""
            MERGE (n:RiskControl {uid: $uid})
            SET n.measure=$measure, n.type=$type, n.source=$source
        """, uid=f"{rc.get('_source','')}::rc::{rc.get('measure','')[:40]}",
            measure=rc.get("measure") or rc.get("description", ""),
            type=rc.get("type") or "", source=rc.get("_source", ""))

    print("Creating Function nodes...", flush=True)
    for f in nodes.get("functions", []):
        session.run("""
            MERGE (n:Function {name: $name, source: $source})
            SET n.description=$desc, n.value=$value
        """, name=f.get("name", ""), source=f.get("_source", ""),
            desc=f.get("description") or "", value=f.get("value") or "")

    print("Creating Regulation nodes...", flush=True)
    for reg in nodes.get("regulations", []):
        session.run("""
            MERGE (n:Regulation {std_id: $std_id})
            SET n.version=$version, n.region=$region, n.source=$source
        """, std_id=reg.get("std_id") or reg.get("name", ""),
            version=reg.get("version") or "", region=reg.get("region") or "",
            source=reg.get("_source", ""))

    print("Creating Person nodes...", flush=True)
    for p in nodes.get("persons", []):
        name = p.get("name", "")
        if not name:
            continue
        session.run("""
            MERGE (n:Person {name: $name})
            SET n.title=$title, n.source=$source
        """, name=name, title=p.get("title") or p.get("role", ""),
            source=p.get("_source", ""))

    print("Creating Product nodes...", flush=True)
    for prod in nodes.get("products", []):
        session.run("""
            MERGE (n:Product {name: $name})
            SET n.model=$model, n.product_id=$pid, n.source=$source
        """, name=prod.get("name") or prod.get("model", ""),
            model=prod.get("model") or "", pid=prod.get("product_id") or "",
            source=prod.get("_source", ""))

    print("Creating DesignInput nodes...", flush=True)
    for di in nodes.get("design_inputs", []):
        session.run("""
            MERGE (n:DesignInput {uid: $uid})
            SET n.di_id=$di_id, n.category=$cat, n.description=$desc,
                n.value=$value, n.unit=$unit, n.source=$source
        """, uid=f"{di.get('_source','')}::di::{di.get('di_id') or di.get('item_id','')}",
            di_id=str(di.get("di_id") or di.get("item_id", "")),
            cat=di.get("category") or "", desc=di.get("description") or "",
            value=di.get("value") or "", unit=di.get("unit") or "",
            source=di.get("_source", ""))

    print("Creating Test nodes...", flush=True)
    for t in nodes.get("tests", []):
        session.run("""
            MERGE (n:Test {uid: $uid})
            SET n.test_id=$tid, n.item=$item, n.condition=$cond,
                n.expected_value=$expected, n.actual_result=$actual,
                n.pass_criteria=$criteria, n.source=$source
        """, uid=f"{t.get('_source','')}::test::{t.get('test_id','')}",
            tid=str(t.get("test_id", "")), item=t.get("item") or t.get("name", ""),
            cond=t.get("condition") or "", expected=t.get("expected_value") or "",
            actual=t.get("actual_result") or "", criteria=t.get("pass_criteria") or "",
            source=t.get("_source", ""))

    print("Creating PlanTask nodes...", flush=True)
    for task in nodes.get("plan_tasks", []):
        session.run("""
            MERGE (n:PlanTask {uid: $uid})
            SET n.name=$name, n.wbs=$wbs, n.owner=$owner, n.phase=$phase, n.source=$source
        """, uid=f"{task.get('_source','')}::task::{task.get('name','')[:40]}",
            name=task.get("name") or task.get("task_name", ""),
            wbs=task.get("wbs") or "", owner=task.get("owner") or "",
            phase=task.get("phase") or "", source=task.get("_source", ""))

    print("Creating SoftwareItem nodes...", flush=True)
    for sw in nodes.get("software_items", []):
        session.run("""
            MERGE (n:SoftwareItem {name: $name, source: $source})
            SET n.item_type=$itype, n.description=$desc, n.value=$value
        """, name=sw.get("name", ""), source=sw.get("_source", ""),
            itype=sw.get("item_type") or "", desc=sw.get("description") or "",
            value=sw.get("value") or "")

    print("Creating Component nodes...", flush=True)
    for c in nodes.get("components", []):
        session.run("""
            MERGE (n:Component {name: $name, source: $source})
            SET n.spec=$spec, n.qty=$qty
        """, name=c.get("name", ""), source=c.get("_source", ""),
            spec=c.get("spec") or "", qty=c.get("qty") or c.get("quantity", ""))

    print("Creating Market nodes...", flush=True)
    for m in nodes.get("markets", []):
        session.run("""
            MERGE (n:Market {region: $region})
            SET n.certification=$cert, n.source=$source
        """, region=m.get("region") or m.get("name", ""),
            cert=m.get("certification") or "", source=m.get("_source", ""))

    print("Creating IntendedUse nodes...", flush=True)
    for iu in nodes.get("intended_use_items", []):
        session.run("""
            MERGE (n:IntendedUse {content: $content, source: $source})
            SET n.seq=$seq
        """, content=iu.get("content") or iu.get("description", ""),
            source=iu.get("_source", ""), seq=str(iu.get("seq") or ""))

    print("Creating Identifier nodes...", flush=True)
    for ident in nodes.get("identifiers", []):
        session.run("""
            MERGE (n:Identifier {value: $value, id_type: $id_type})
            SET n.source=$source
        """, value=str(ident.get("value", "")), id_type=ident.get("id_type") or "",
            source=ident.get("_source", ""))

    print("Creating ReviewItem nodes...", flush=True)
    for ri in nodes.get("review_items", []):
        session.run("""
            MERGE (n:ReviewItem {uid: $uid})
            SET n.seq=$seq, n.content=$content, n.conclusion=$conclusion,
                n.actual_situation=$actual, n.improvement=$improvement, n.source=$source
        """, uid=f"{ri.get('_source','')}::ri::{ri.get('seq', ri.get('content','')[:30])}",
            seq=str(ri.get("seq") or ""), content=ri.get("content") or "",
            conclusion=ri.get("conclusion") or "",
            actual=ri.get("actual_situation") or "",
            improvement=ri.get("improvement") or "",
            source=ri.get("_source", ""))

    print("Creating DocIndexEntry nodes...", flush=True)
    for die in nodes.get("doc_index_entries", []):
        session.run("""
            MERGE (n:DocIndexEntry {uid: $uid})
            SET n.seq=$seq, n.file_name=$fname, n.file_no=$fno,
                n.stage=$stage, n.date=$date, n.source=$source
        """, uid=f"{die.get('_source','')}::die::{die.get('seq','')}",
            seq=str(die.get("seq") or ""), fname=die.get("file_name") or "",
            fno=die.get("file_no") or "", stage=die.get("stage") or "",
            date=die.get("date") or "", source=die.get("_source", ""))

    print("Creating SemanticFragment nodes...", flush=True)
    for sf in nodes.get("semantic_fragments", []):
        content_short = (sf.get("content") or "")[:200]
        session.run("""
            MERGE (n:SemanticFragment {uid: $uid})
            SET n.fragment_type=$ftype, n.content=$content,
                n.topic_tags=$tags, n.source=$source
        """, uid=f"{sf.get('_source','')}::sf::{content_short[:40]}",
            ftype=sf.get("fragment_type") or "",
            content=sf.get("content") or "",
            tags=str(sf.get("topic_tags") or []),
            source=sf.get("_source", ""))

    print("Creating TestReport nodes...", flush=True)
    for tr in nodes.get("test_reports", []):
        session.run("""
            MERGE (n:TestReport {uid: $uid})
            SET n.report_id=$rid, n.conclusion=$conclusion, n.source=$source
        """, uid=f"{tr.get('_source','')}::tr::{tr.get('report_id','')}",
            rid=tr.get("report_id") or "", conclusion=tr.get("conclusion") or "",
            source=tr.get("_source", ""))

    print("Creating RevisionRecord nodes...", flush=True)
    for rev in nodes.get("revision_records", []):
        session.run("""
            MERGE (n:RevisionRecord {uid: $uid})
            SET n.seq=$seq, n.version=$version, n.change_description=$desc,
                n.author=$author, n.date=$date, n.source=$source
        """, uid=f"{rev.get('_source','')}::rev::{rev.get('seq','')}",
            seq=str(rev.get("seq") or ""), version=rev.get("version") or "",
            desc=rev.get("change_description") or "", author=rev.get("author") or "",
            date=rev.get("date") or "", source=rev.get("_source", ""))

    print("Creating Claim nodes...", flush=True)
    for c in claims:
        session.run("""
            MERGE (n:Claim {uid: $uid})
            SET n.subject=$subject, n.attribute=$attr, n.value=$value,
                n.unit=$unit, n.tolerance=$tolerance, n.condition=$cond,
                n.raw_text=$raw, n.source=$source
        """, uid=f"{c.get('_source') or c.get('source_doc','')}::claim::{c.get('subject','')}::{c.get('attribute','')}",
            subject=c.get("subject", ""), attr=c.get("attribute", ""),
            value=str(c.get("value") or ""), unit=c.get("unit") or "",
            tolerance=c.get("tolerance") or "", cond=c.get("condition") or "",
            raw=c.get("raw_text") or "", source=c.get("_source") or c.get("source_doc", ""))


def import_edges(session, edges):
    """Import edges using flexible node matching."""
    print(f"Creating {len(edges)} edges...", flush=True)
    created = 0
    for e in edges:
        etype = e.get("type", "RELATED_TO")
        from_id = str(e.get("from", ""))
        to_id = str(e.get("to", ""))
        source = e.get("_source", "")

        if not from_id or not to_id:
            continue

        query = f"""
            OPTIONAL MATCH (a) WHERE
                a.name = $from_id OR a.title = $from_id OR a.req_id = $from_id
                OR a.test_id = $from_id OR a.uid CONTAINS $from_id
                OR a.content STARTS WITH $from_id OR a.file_name = $from_id
                OR a.std_id = $from_id OR a.measure STARTS WITH $from_id
            WITH a WHERE a IS NOT NULL
            LIMIT 1
            OPTIONAL MATCH (b) WHERE
                b.name = $to_id OR b.title = $to_id OR b.req_id = $to_id
                OR b.test_id = $to_id OR b.uid CONTAINS $to_id
                OR b.content STARTS WITH $to_id OR b.file_name = $to_id
                OR b.std_id = $to_id OR b.measure STARTS WITH $to_id
            WITH a, b WHERE b IS NOT NULL
            LIMIT 1
            MERGE (a)-[r:{etype}]->(b)
            SET r.source = $source
            RETURN count(r) as cnt
        """
        try:
            result = session.run(query, from_id=from_id, to_id=to_id, source=source)
            record = result.single()
            if record and record["cnt"] > 0:
                created += 1
        except Exception:
            pass

    print(f"  Successfully created {created}/{len(edges)} edges", flush=True)


def link_to_documents(session):
    """Link all nodes to source Document via EXTRACTED_FROM."""
    print("Linking nodes to source documents...", flush=True)
    session.run("""
        MATCH (n)
        WHERE n.source IS NOT NULL AND n.source <> '' AND NOT (n:Document)
        MATCH (d:Document)
        WHERE d.source = n.source
        MERGE (n)-[:EXTRACTED_FROM]->(d)
    """)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--uri", default="bolt://localhost:7687")
    parser.add_argument("--user", default="neo4j")
    parser.add_argument("--password", default="test1234")
    args = parser.parse_args()

    data = json.loads(MERGED.read_text(encoding="utf-8"))
    nodes = data.get("nodes", {})
    edges = data.get("edges", [])
    claims = data.get("claims", [])

    total_nodes = sum(len(v) for v in nodes.values() if isinstance(v, list))
    print(f"Data: {total_nodes} nodes, {len(edges)} edges, {len(claims)} claims", flush=True)

    driver = GraphDatabase.driver(args.uri, auth=(args.user, args.password))

    with driver.session() as session:
        print("Clearing database...", flush=True)
        session.execute_write(clear_db)
        session.execute_write(create_constraints)

        import_nodes(session, nodes, claims)
        import_edges(session, edges)
        link_to_documents(session)

    driver.close()
    print("\n=== Import complete! ===", flush=True)
    print("Open Neo4j Browser: http://localhost:7474", flush=True)
    print("Queries to try:", flush=True)
    print("  MATCH (n)-[r]->(m) RETURN n,r,m LIMIT 300", flush=True)
    print("  MATCH (d:Document)<-[:EXTRACTED_FROM]-(n) RETURN d,n LIMIT 200", flush=True)
    print("  MATCH (n:ReviewItem) RETURN n LIMIT 30", flush=True)
    print("  MATCH (n:SemanticFragment) RETURN n LIMIT 20", flush=True)
    print("  MATCH (n:DocIndexEntry) RETURN n LIMIT 50", flush=True)


if __name__ == "__main__":
    main()
