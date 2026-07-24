from __future__ import annotations

from collections import defaultdict
from pathlib import Path
import hashlib
import json
import os
import shutil
import sys


ROOT = Path(__file__).resolve().parents[1]
REPO_ROOT = ROOT.parent
SOURCE_CORPUS = REPO_ROOT / "清洗后md文件" / "清洗后pt9l"
PILOT_ROOT = ROOT / "outputs" / "pilot_30"
PILOT_DOCS = PILOT_ROOT / "docs"
MANIFEST_PATH = PILOT_ROOT / "pilot_manifest.jsonl"

sys.path.insert(0, str(ROOT))

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

from orchestrator.dhf_dmr_langgraph import run_dhf_dmr_graph


STAGE_HINTS = [
    "01 立项",
    "02 开发计划",
    "03 风险",
    "04 设计输入",
    "05 结构设计",
    "06 硬件设计",
    "07 软件设计",
    "08 结构图样",
    "09 硬件图样",
    "11 T1样机",
    "12 设计输出",
    "13 试产文件",
    "18 设计确认",
    "19 上市批准",
    "实验报告",
]

IMPORTANT_TERMS = [
    "DHF",
    "DMR",
    "清单",
    "客户需求",
    "设计输入",
    "风险",
    "FMEA",
    "软件",
    "验证",
    "BOM",
    "EMC",
    "标签",
    "说明书",
    "检验",
    "确认",
]


def main() -> None:
    if load_dotenv:
        load_dotenv(REPO_ROOT / ".env")

    limit = int(os.getenv("PILOT_FILE_LIMIT", "28"))
    selected = select_pilot_files(limit)
    prepare_pilot_docs(selected)

    idea = (
        "对 PT9L 清洗后 DHF/DMR 文档做 Pilot 一致性审查，重点检查文件完整性、版本一致性、"
        "风险控制验证闭环、软件版本、BOM/EMC 硬件证据、标签说明书和 DMR 生产文件一致性。"
    )
    result = run_dhf_dmr_graph(
        ROOT,
        idea,
        project_scope="PT9L cleaned markdown pilot corpus",
        docs_dir=PILOT_DOCS,
        output_namespace="pilot_30",
        run_name="PT9L Pilot 30 DHF/DMR Multi-Agent Audit",
        tags=["pt9l", "pilot-30", "dhf-dmr", "multi-agent", "langgraph"],
        metadata={
            "source_corpus": str(SOURCE_CORPUS),
            "pilot_docs": str(PILOT_DOCS),
            "pilot_file_count": len(selected),
        },
    )

    tracing = os.getenv("LANGSMITH_TRACING") or os.getenv("LANGCHAIN_TRACING_V2")
    project = os.getenv("LANGSMITH_PROJECT") or os.getenv("LANGCHAIN_PROJECT") or "default"

    print("Pilot corpus run complete")
    print(f"Selected files: {len(selected)}")
    print(f"Manifest: {MANIFEST_PATH}")
    print(f"Run ID: {result['run_id']}")
    print(f"Trace nodes: {' -> '.join(result.get('graph_trace', []))}")
    print(f"Selected agents: {', '.join(result.get('selected_agents', []))}")
    print(f"Findings: {len(result.get('findings', []))}")
    print(f"Recovery rounds: {result.get('recovery_round', 0)}")
    print(f"Report: {result.get('report_path')}")
    print(f"JSON: {result.get('json_path')}")
    if tracing and os.getenv("LANGSMITH_API_KEY"):
        print(f"LangSmith tracing enabled. Check project: {project}")
    else:
        print("LangSmith tracing is not enabled in this shell. Set LANGSMITH_TRACING=true and LANGSMITH_API_KEY, then rerun.")


def select_pilot_files(limit: int) -> list[Path]:
    files = [path for path in SOURCE_CORPUS.rglob("*.md") if "_assets" not in path.parts]
    by_stage: dict[str, list[Path]] = defaultdict(list)
    for path in files:
        stage = stage_for(path)
        by_stage[stage].append(path)

    selected: list[Path] = []
    for stage in STAGE_HINTS:
        candidates = sorted(by_stage.get(stage, []), key=file_rank)
        for path in candidates[:2]:
            if path not in selected:
                selected.append(path)
            if len(selected) >= limit:
                return selected

    remaining = sorted((path for path in files if path not in selected), key=file_rank)
    for path in remaining:
        selected.append(path)
        if len(selected) >= limit:
            break
    return selected


def stage_for(path: Path) -> str:
    rel_parts = path.relative_to(SOURCE_CORPUS).parts
    folder = rel_parts[0] if len(rel_parts) > 1 else path.parent.name
    for stage in STAGE_HINTS:
        if stage in folder:
            return stage
    return folder


def file_rank(path: Path) -> tuple[int, int, str]:
    name = path.name.lower()
    term_score = sum(1 for term in IMPORTANT_TERMS if term.lower() in name)
    size = path.stat().st_size
    oversize_penalty = 1 if size > 180_000 else 0
    return (-term_score, oversize_penalty, size, str(path))


def prepare_pilot_docs(selected: list[Path]) -> None:
    PILOT_DOCS.mkdir(parents=True, exist_ok=True)
    for old in PILOT_DOCS.rglob("*"):
        if old.is_file():
            old.unlink()
    manifest_rows = []
    for idx, source in enumerate(selected, start=1):
        rel = source.relative_to(SOURCE_CORPUS)
        target = PILOT_DOCS / f"{idx:02d}_{safe_name(rel)}"
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source, target)
        digest = hashlib.sha1(source.read_bytes()).hexdigest()
        manifest_rows.append(
            {
                "pilot_id": f"PILOT-{idx:03d}",
                "source_path": str(source),
                "pilot_path": str(target),
                "stage": stage_for(source),
                "bytes": source.stat().st_size,
                "sha1": digest,
            }
        )
    MANIFEST_PATH.write_text(
        "\n".join(json.dumps(row, ensure_ascii=False) for row in manifest_rows) + "\n",
        encoding="utf-8",
    )


def safe_name(path: Path) -> str:
    raw = "__".join(path.parts)
    for char in '<>:"/\\|?*':
        raw = raw.replace(char, "_")
    return raw[:180]


if __name__ == "__main__":
    main()
