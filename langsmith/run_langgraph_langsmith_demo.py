from __future__ import annotations

from pathlib import Path
import os
import sys


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent
sys.path.insert(0, str(ROOT))

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

from orchestrator.dhf_dmr_langgraph import run_dhf_dmr_graph


def main() -> None:
    if load_dotenv:
        load_dotenv(REPO_ROOT / ".env")

    idea = (
        "检查 PT9L 项目的 DHF/DMR 完整性、软件版本一致性、"
        "风险控制验证闭环、BOM/EMC 硬件证据和法规说明书声明。"
    )
    if len(sys.argv) > 1:
        idea = " ".join(sys.argv[1:])

    result = run_dhf_dmr_graph(ROOT, idea, project_scope="PT9L demo sample")
    tracing = os.getenv("LANGSMITH_TRACING") or os.getenv("LANGCHAIN_TRACING_V2")
    project = os.getenv("LANGSMITH_PROJECT") or os.getenv("LANGCHAIN_PROJECT") or "default"

    print("LangGraph run complete")
    print(f"Run ID: {result['run_id']}")
    print(f"Trace nodes: {' -> '.join(result.get('graph_trace', []))}")
    print(f"Selected agents: {', '.join(result.get('selected_agents', []))}")
    print(f"Findings: {len(result.get('findings', []))}")
    print(f"Recovery rounds: {result.get('recovery_round', 0)}")
    print(f"Report: {result.get('report_path')}")
    print(f"JSON: {result.get('json_path')}")
    if tracing:
        print(f"LangSmith tracing enabled. Check project: {project}")
    else:
        print("LangSmith tracing is not enabled. Set LANGSMITH_TRACING=true and LANGSMITH_API_KEY to upload traces.")


if __name__ == "__main__":
    main()
