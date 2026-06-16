"""Merge all per-file JSONs into one unified graph JSON."""
import json
from pathlib import Path
from config import PER_FILE_DIR, OUTPUT_DIR


def main():
    json_files = sorted(PER_FILE_DIR.glob("*.json"))
    print(f"=== Merge Results ===", flush=True)
    print(f"Merging {len(json_files)} files\n", flush=True)

    all_nodes = {}
    all_edges = []
    all_claims = []
    file_index = []

    for fp in json_files:
        data = json.loads(fp.read_text(encoding="utf-8"))
        meta = data.get("_meta", {})
        edges = data.pop("_edges", [])
        claims = data.pop("_claims", [])
        data.pop("_meta", None)

        source = meta.get("source_file", fp.stem)

        for key, val in data.items():
            if isinstance(val, list):
                if key not in all_nodes:
                    all_nodes[key] = []
                for item in val:
                    item["_source"] = source
                    all_nodes[key].append(item)
            elif isinstance(val, dict) and key == "document":
                if "documents" not in all_nodes:
                    all_nodes["documents"] = []
                val["_source"] = source
                all_nodes["documents"].append(val)

        for edge in edges:
            edge["_source"] = source
            all_edges.append(edge)

        for claim in claims:
            claim["_source"] = source
            all_claims.append(claim)

        file_index.append(meta)

    merged = {
        "summary": {
            "files_processed": len(json_files),
            "node_counts": {k: len(v) for k, v in all_nodes.items()},
            "edge_count": len(all_edges),
            "claim_count": len(all_claims),
        },
        "nodes": all_nodes,
        "edges": all_edges,
        "claims": all_claims,
        "file_index": file_index,
    }

    out_path = OUTPUT_DIR / "merged_graph.json"
    out_path.write_text(json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8")

    print(f"Node types: {len(all_nodes)}", flush=True)
    for k, v in all_nodes.items():
        print(f"  {k}: {len(v)}", flush=True)
    print(f"Edges: {len(all_edges)}", flush=True)
    print(f"Claims: {len(all_claims)}", flush=True)
    print(f"\nSaved to: {out_path}", flush=True)
    print(f"=== Merge Complete ===", flush=True)


if __name__ == "__main__":
    main()
