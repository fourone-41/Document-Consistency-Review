from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path
from typing import Any, Iterable, TypedDict

import httpx
import yaml
from dotenv import load_dotenv
from langgraph.graph import END, START, StateGraph
from openai import OpenAI


REPO_ROOT = Path(__file__).resolve().parents[1]
INPUT_ROOT_DEFAULT = REPO_ROOT / "pt9l_markdown_output"
OUTPUT_ROOT_DEFAULT = REPO_ROOT / "magent-output" / "pt9l_full_audit_output_langgraph_v9"
AGENT_CONFIG_ROOT = Path(__file__).resolve().parent / "agent_configs"
DOMAIN_AGENT_IDS = {
    "regulatory": "regulatory",
    "hardware": "hardware",
    "software": "software",
    "risk": "risk_traceability",
    "vv": "vv",
    "dmr": "dmr_sop",
}
ASSIGNABLE_AGENT_IDS = {
    "candidate_discovery": "candidate_discovery",
    **DOMAIN_AGENT_IDS,
}
ORCHESTRATOR_SAFETY_CYCLE_LIMIT = 50

EXCLUDED_PRIMARY_KEYWORDS = [
    "_assets",
    "鍘嗗彶璁板綍",
    "鑽夌",
    "鍘熺増 - 鍘嗗彶鏂囦欢",
    "2L椋庨櫓鏀?- 鍘嗗彶鏂囦欢",
    "妯℃澘",
    "搴熸涓庡浠?",
    "杞欢鏂囦欢搴曠",
    "鏃╂湡鍥剧焊",
]

RESIDUE_TERMS_FULL = [
    "???",
    "PT2L",
    "PT3",
    "PT3SBT",
    "PT9C",
    "BP3L",
    "TH30F",
    "???",
    "TODO",
    "??",
    "XXX",
    "??",
    "??",
]

PARAMETER_PATTERNS = [
    ("temperature_value", re.compile(r"[-+]?\d+(?:\.\d+)?\s*(?:\u00b1\s*\d+(?:\.\d+)?)?\s*(?:\u2103|\u00b0C|\u2109|\u00b0F)")),
    ("percent_value", re.compile(r"[-+]?\d+(?:\.\d+)?\s*\u00b1?\s*\d*(?:\.\d+)?\s*%")),
    ("voltage_value", re.compile(r"[-+]?\d+(?:\.\d+)?\s*(?:V|v|mV)")),
    ("time_value", re.compile(r"[-+]?\d+(?:\.\d+)?\s*(?:s|min|h|\u79d2|\u5206\u949f|\u5c0f\u65f6|\u6708|\u5e74)")),
    ("range_value", re.compile(r"[-+]?\d+(?:\.\d+)?\s*(?:-|~|\uff5e|\u81f3|\u5230)\s*[-+]?\d+(?:\.\d+)?")),
    ("tolerance_value", re.compile(r"\u00b1\s*\d+(?:\.\d+)?\s*(?:\u2103|\u00b0C|%|mm|cm|V)?")),
]

PARAMETER_KEYWORDS = {
    "measurement_accuracy": ["\u6d4b\u91cf\u7cbe\u5ea6", "\u6d4b\u91cf\u8bef\u5dee", "\u51c6\u786e\u5ea6", "\u7cbe\u5ea6", "accuracy", "maximum permissible error", "\u8bef\u5dee"],
    "measurement_range": ["\u6d4b\u91cf\u8303\u56f4", "temperature range", "range", "\u91cf\u7a0b"],
    "operating_environment": ["\u5de5\u4f5c\u73af\u5883", "\u8fd0\u884c\u73af\u5883", "operating", "temperature", "humidity", "\u6e7f\u5ea6"],
    "battery": ["\u7535\u6c60", "battery", "\u7535\u538b", "voltage", "\u5bff\u547d"],
    "software_version": ["\u8f6f\u4ef6\u7248\u672c", "software version", "version", "\u7248\u672c"],
    "model_name": ["PT9L", "\u578b\u53f7", "model"],
}

RELATION_KEYWORDS = {
    "requirement": ["\u9700\u6c42", "requirement", "shall", "\u5e94"],
    "design_input": ["\u8bbe\u8ba1\u8f93\u5165", "design input"],
    "risk": ["risk", "hazard", "\u98ce\u9669", "\u5371\u5bb3"],
    "control": ["control", "mitigation", "\u63a7\u5236", "\u63aa\u65bd"],
    "verification": ["verification", "\u9a8c\u8bc1", "\u6d4b\u8bd5", "test"],
    "report": ["report", "\u62a5\u544a", "record", "\u8bb0\u5f55"],
}

CONTEXT_RECOVERY_MAX_ROUNDS = 5


class FullAuditState(TypedDict, total=False):
    input_root: str
    output_root: str
    manifest: list[dict]
    readiness: list[dict]
    page_index: list[dict]
    params: list[dict]
    relation_nodes: list[dict]
    relation_edges: list[dict]
    evidence_tool_hits: list[dict]
    context_recovery_tasks: list[dict]
    context_recovery_results: list[dict]
    context_recovery_summary: dict
    evidence_catalog: dict[str, dict]
    task_packages: dict[str, dict]
    agent_runs: list[dict]
    orchestrator_route_plans: list[dict]
    project_profile: dict
    mandatory_audit_matrix: list[dict]
    candidate_discovery_results: list[dict]
    scout_output: dict
    semantic_findings: list[dict]
    all_findings: list[dict]
    challenge_output: dict
    summary: dict


def ensure_dirs(output_root: Path) -> None:
    for rel in [
        "00_manifest",
        "01_page_index",
        "02_blackboard",
        "03_ssot_parameters",
        "04_relation_index",
        "05_agent_notes",
        "06_evidence_tools",
        "07_findings",
        "08_reports",
        "09_evidence_gate",
        "10_task_packages",
        "11_llm_raw",
        "12_challenge",
        "14_context_recovery",
    ]:
        (output_root / rel).mkdir(parents=True, exist_ok=True)


def write_json(path: Path, obj: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def write_jsonl(path: Path, rows: Iterable[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="\n") as f:
        for row in rows:
            f.write(json.dumps(row, ensure_ascii=False) + "\n")


def read_json(path: Path, default: Any) -> Any:
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    rows = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        rows.append(json.loads(line))
    return rows


def read_text(path: Path) -> str:
    return path.read_text(encoding="utf-8", errors="replace")


def read_yaml(path: Path) -> dict:
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    if not isinstance(data, dict):
        raise ValueError(f"YAML config must be an object: {path}")
    return data


def load_agent_config(agent_id: str) -> dict:
    path = AGENT_CONFIG_ROOT / f"{agent_id}.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Agent config not found: {path}")
    config = read_yaml(path)
    config.setdefault("agent_id", agent_id)
    return config


def load_routing_config() -> dict:
    path = AGENT_CONFIG_ROOT / "routing.yaml"
    if not path.exists():
        raise FileNotFoundError(f"Routing config not found: {path}")
    return read_yaml(path)


def build_agent_task_from_config(config: dict, evidence_catalog: list[dict], **overrides) -> dict:
    task = {
        "role": config.get("role") or config.get("display_name") or config.get("agent_id", ""),
        "goal": config.get("goal", ""),
        "system_prompt": config.get("system_prompt", ""),
        "retrieval_strategy": config.get("retrieval_strategy", {}),
        "input_schema": config.get("input_schema", {}),
        "required_schema": config.get("output_schema", {}),
        "evidence_catalog": evidence_catalog,
    }
    task.update(overrides)
    return task


def build_domain_agent_specs() -> dict[str, dict]:
    return {key: load_agent_config(config_id) for key, config_id in DOMAIN_AGENT_IDS.items()}


def build_assignable_agent_registry() -> dict[str, dict]:
    registry: dict[str, dict] = {}
    for key, config_id in ASSIGNABLE_AGENT_IDS.items():
        config = load_agent_config(config_id)
        display_name = str(config.get("display_name") or config.get("role") or config_id)
        registry[display_name] = {
            "key": key,
            "config_id": config_id,
            "config": config,
        }
    return registry


def safe_name(text: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]+", "_", text).strip("_").lower() or "agent"


def collect_configured_evidence(catalog: dict[str, dict], manifest: list[dict], config: dict) -> list[dict]:
    strategy = config.get("retrieval_strategy") if isinstance(config.get("retrieval_strategy"), dict) else {}
    searches = strategy.get("searches") if isinstance(strategy.get("searches"), list) else []
    if not searches and strategy.get("patterns"):
        searches = [strategy]
    evidence: list[dict] = []
    for search in searches:
        if not isinstance(search, dict):
            continue
        patterns = search.get("patterns") if isinstance(search.get("patterns"), list) else []
        rel_contains = search.get("rel_contains") if isinstance(search.get("rel_contains"), list) else None
        max_hits = int(search.get("max_hits") or strategy.get("max_hits") or 100)
        prefix = str(search.get("prefix") or strategy.get("prefix") or config.get("agent_id", "AGENT")).upper()
        hits = find_lines(manifest, patterns, rel_contains=rel_contains, max_hits=max_hits)
        evidence.extend(add_evidence(catalog, prefix, hits))
    return evidence


def load_runtime_env() -> dict[str, str]:
    env_path = REPO_ROOT / ".env"
    if env_path.exists():
        load_dotenv(env_path)
    api_key = os.getenv("GPT55_API_KEY") or os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("GPT55_API_URL") or os.getenv("OPENAI_BASE_URL")
    model = os.getenv("GPT55_MODEL") or os.getenv("OPENAI_MODEL")
    if not api_key:
        raise RuntimeError("鏈壘鍒?GPT55_API_KEY 鎴?OPENAI_API_KEY銆傝鍏堝湪 .env 涓厤缃€?")
    if not model:
        raise RuntimeError("鏈壘鍒?GPT55_MODEL 鎴?OPENAI_MODEL銆傝鍏堝湪 .env 涓厤缃€?")
    return {
        "api_key": api_key,
        "base_url": normalize_base_url(base_url) if base_url else "",
        "model": model,
        "disable_ssl_verify": os.getenv("GPT55_DISABLE_SSL_VERIFY", "").lower() in {"1", "true", "yes"},
    }


def normalize_base_url(url: str) -> str:
    url = url.strip().rstrip("/")
    for suffix in ["/chat/completions", "/responses"]:
        if url.endswith(suffix):
            url = url[: -len(suffix)]
    return url


def make_client() -> tuple[OpenAI, str]:
    env = load_runtime_env()
    http_client = httpx.Client(verify=not env["disable_ssl_verify"], timeout=120)
    kwargs: dict[str, Any] = {"api_key": env["api_key"], "http_client": http_client}
    if env["base_url"]:
        kwargs["base_url"] = env["base_url"]
    return OpenAI(**kwargs), env["model"]


def path_has_any(rel_path: str, keywords: list[str]) -> bool:
    return any(keyword in rel_path for keyword in keywords)


def infer_stage(rel_path: str) -> str:
    top = rel_path.split("\\", 1)[0].split("/", 1)[0]
    if re.match(r"^\d{2}\s", top):
        return f"Stage {top[:2]}"
    if "瀹為獙鎶ュ憡" in top:
        return "External Test"
    if "wiki" in top.lower():
        return "Wiki/Derived"
    return top or "Unknown"


def infer_doc_type(rel_path: str) -> str:
    name = rel_path.lower()
    rules = [
        ("customer_needs", ["customer", "客户需求", "kehu"]),
        ("project_approval", ["立项", "approval"]),
        ("design_input", ["设计输入", "design input"]),
        ("risk_plan", ["risk management plan", "风险管理计划"]),
        ("risk_assessment", ["risk assessment", "风险评价", "风险评估"]),
        ("risk_control_verification", ["residual risk", "risk control", "风险控制"]),
        ("risk_report", ["risk management report", "风险管理报告"]),
        ("hardware_design", ["硬件", "hardware"]),
        ("software_requirements", ["软件需求", "需求规格", "software requirement"]),
        ("software_design", ["软件方案", "软件设计", "software design"]),
        ("software_test_plan", ["软件测试计划", "software test plan"]),
        ("software_test_record", ["软件系统测试记录", "子程序测试记录", "software test record"]),
        ("software_validation_report", ["软件确认报告", "software validation"]),
        ("traceability_analysis", ["追溯", "traceability"]),
        ("validation_plan", ["设计验证计划", "验证计划", "validation plan"]),
        ("validation_report", ["设计验证报告", "验证报告", "validation report"]),
        ("external_test_report", ["最终报告", "实验报告", "型式试验", "test report"]),
        ("bom", ["ebom", "abom", "bom", "组件清单"]),
        ("design_output_list", ["设计输出清单", "design output"]),
        ("assembly_instruction", ["装配", "assembly"]),
        ("sop", ["工艺", "作业指导", "sop"]),
        ("drawing_or_pdf_report", ["图纸", ".pdf.md"]),
        ("checklist", ["checklist", "检查表"]),
    ]
    for doc_type, keywords in rules:
        if any(keyword.lower() in name for keyword in keywords):
            return doc_type
    return "general_document"

def infer_agent(doc_type: str) -> str:
    if doc_type in {"customer_needs", "project_approval", "design_input"}:
        return "Market & Category Scout / Regulatory"
    if doc_type.startswith("risk"):
        return "Risk Traceability"
    if "software" in doc_type:
        return "Software"
    if "hardware" in doc_type:
        return "Hardware"
    if doc_type in {"validation_plan", "validation_report", "external_test_report", "traceability_analysis"}:
        return "V&V / Regulatory"
    if doc_type in {"bom", "design_output_list", "assembly_instruction", "sop"}:
        return "DMR/SOP"
    if doc_type == "drawing_or_pdf_report":
        return "Drawing / Mechanical Check"
    return "Document Intake & Coverage"


def make_full_manifest(input_root: Path) -> list[dict]:
    rows = []
    for i, path in enumerate(sorted(input_root.rglob("*.md")), start=1):
        rel_path = str(path.relative_to(input_root))
        text = read_text(path)
        doc_type = infer_doc_type(rel_path)
        excluded = path_has_any(rel_path, EXCLUDED_PRIMARY_KEYWORDS)
        rows.append(
            {
                "doc_id": f"F{i:04d}",
                "rel_path": rel_path,
                "path": str(path),
                "stage": infer_stage(rel_path),
                "doc_type": doc_type,
                "agent": infer_agent(doc_type),
                "exists": True,
                "size_bytes": path.stat().st_size,
                "line_count": len(text.splitlines()),
                "char_count": len(text),
                "excluded_from_primary_scope": excluded,
                "include_reason": "鍏ㄩ噺 Markdown 瑕嗙洊鍙拌处锛涘巻鍙?搴熸/搴曠鏂囦欢鍙綔涓烘畫鐣欏拰杈呭姪璇佹嵁銆?",
            }
        )
    return rows


def readiness_checks(manifest: list[dict]) -> list[dict]:
    rows = []
    pdf_dupes = defaultdict(list)
    for doc in manifest:
        normalized = re.sub(r"\.(via_lo_html\.clean|pdf)\.md$", "", doc["rel_path"], flags=re.I)
        pdf_dupes[normalized].append(doc["doc_id"])
    duplicate_ids = {doc_id for ids in pdf_dupes.values() if len(ids) > 1 for doc_id in ids}
    for doc in manifest:
        flags = []
        if doc["size_bytes"] == 0:
            flags.append("empty_file")
        if doc["char_count"] < 200:
            flags.append("very_short_text")
        if doc["excluded_from_primary_scope"]:
            flags.append("auxiliary_or_excluded_path")
        if doc["doc_id"] in duplicate_ids:
            flags.append("possible_pdf_html_duplicate")
        rows.append({**doc, "flags": flags, "readiness": "pass" if not flags else "review"})
    return rows


def extract_keywords(text: str) -> list[str]:
    tokens = re.findall(r"[A-Za-z][A-Za-z0-9_-]{1,}|PT\d+[A-Z]*|[\u4e00-\u9fff]{2,}", text)
    stop = {"?", "?", "??", "??", "??", "??", "??", "??", "the", "and", "for", "with"}
    counts = Counter(t for t in tokens if t.lower() not in stop and len(t.strip()) > 1)
    return [key for key, _ in counts.most_common(50)]


def extract_parameters(manifest: list[dict]) -> list[dict]:
    params = []
    for doc in manifest:
        path = Path(doc["path"])
        if not path.exists():
            continue
        lines = read_text(path).splitlines()
        for i, line in enumerate(lines, start=1):
            lower = line.lower()
            matched_slots = [
                slot
                for slot, words in PARAMETER_KEYWORDS.items()
                if any(word.lower() in lower for word in words)
            ]
            values = []
            for value_type, pattern in PARAMETER_PATTERNS:
                for match in pattern.finditer(line):
                    values.append({"value_type": value_type, "raw_value": match.group(0)})
            if matched_slots or values:
                if matched_slots or any(v["value_type"] in {"temperature_value", "tolerance_value", "voltage_value"} for v in values):
                    params.append(
                        {
                            "doc_id": doc["doc_id"],
                            "rel_path": doc["rel_path"],
                            "stage": doc["stage"],
                            "doc_type": doc["doc_type"],
                            "line": i,
                            "canonical_slots": matched_slots or ["unclassified_numeric"],
                            "values": values,
                            "source_text": line.strip()[:800],
                        }
                    )
    return params


def analyze_parameter_conflicts(params: list[dict]) -> list[dict]:
    evidence_rows: list[dict] = []
    by_slot: dict[str, list[dict]] = defaultdict(list)
    for row in params:
        for slot in row["canonical_slots"]:
            by_slot[slot].append(row)

    for slot in ["measurement_accuracy", "measurement_range", "battery", "software_version"]:
        rows = by_slot.get(slot, [])
        raw_values = []
        for row in rows:
            for value in row["values"]:
                raw_values.append((value["raw_value"], row))
        distinct = sorted(set(value for value, _ in raw_values))
        if len(distinct) >= 4 and len(rows) >= 2:
            sample = rows[0]
            evidence_rows.append(
                {
                    "evidence_type": "parameter_needs_alignment_signal",
                    "term": f"parameter_conflict:{slot}",
                    "doc_id": sample["doc_id"],
                    "rel_path": sample["rel_path"],
                    "line": int(sample["line"]),
                    "source_text": sample["source_text"],
                    "distinct_values": distinct[:8],
                    "signal_summary": f"{slot} appears with multiple numeric expressions: {', '.join(distinct[:8])}",
                }
            )
    return evidence_rows


def build_page_index(manifest: list[dict]) -> list[dict]:
    index_rows = []
    heading_re = re.compile(r"^\s{0,3}#{1,6}\s+(.+)$")
    for doc in manifest:
        path = Path(doc["path"])
        lines = read_text(path).splitlines()
        section_no = 0
        current_heading = "document_start"
        start = 1
        buffer: list[str] = []

        def flush(end_line: int) -> None:
            nonlocal buffer, start, section_no, current_heading
            if not buffer:
                return
            text = "\n".join(buffer)
            if not text.strip():
                buffer = []
                return
            section_no += 1
            index_rows.append(
                {
                    "doc_id": doc["doc_id"],
                    "section_id": f"{doc['doc_id']}#section_{section_no:03d}",
                    "path": doc["path"],
                    "rel_path": doc["rel_path"],
                    "stage": doc["stage"],
                    "doc_type": doc["doc_type"],
                    "heading": current_heading,
                    "line_start": start,
                    "line_end": end_line,
                    "keywords": extract_keywords(text)[:30],
                    "text_preview": text.strip()[:500],
                    "excluded_from_primary_scope": doc["excluded_from_primary_scope"],
                }
            )
            buffer = []

        for i, line in enumerate(lines, start=1):
            match = heading_re.match(line)
            if match and buffer:
                flush(i - 1)
                current_heading = match.group(1).strip()
                start = i
                buffer = [line]
            else:
                if not buffer:
                    start = i
                if match:
                    current_heading = match.group(1).strip()
                buffer.append(line)
            if len(buffer) >= 90:
                flush(i)
                start = i + 1
        flush(len(lines))
    return index_rows


def extract_parameters_full(manifest: list[dict]) -> list[dict]:
    return extract_parameters(manifest)


PARAMETER_ALIGNMENT_SLOTS = {
    "measurement_accuracy",
    "measurement_range",
    "operating_environment",
    "battery",
}


def parameter_unit_kind(value_type: str, raw_value: str) -> str:
    text = f"{value_type} {raw_value}".lower()
    if "temperature" in text or "℃" in text or "°c" in text:
        return "temperature"
    if "voltage" in text or re.search(r"\bmv\b|\bv\b", text):
        return "voltage"
    if "percent" in text or "%" in text:
        return "percent"
    if "time" in text or any(token in text for token in ["min", "hour", "second"]):
        return "time"
    if "range" in text:
        return "range"
    return value_type or "numeric"


def normalize_parameter_value(raw_value: object) -> str:
    text = str(raw_value or "").strip()
    numbers = re.findall(r"[-+]?\d+(?:[\.,]\d+)?", text)
    normalized_numbers = []
    for number in numbers:
        cleaned = number.replace(",", ".")
        if "." in cleaned:
            cleaned = cleaned.rstrip("0").rstrip(".")
        normalized_numbers.append(cleaned)
    tolerance = "tol" if any(token in text for token in ["±", "+/-"]) else "value"
    if not normalized_numbers:
        return f"{tolerance}:"
    return f"{tolerance}:{','.join(normalized_numbers)}"


def build_parameter_alignment_evidence_rows(params: list[dict], max_rows: int = 80) -> list[dict]:
    grouped: dict[tuple[str, str, str], list[dict]] = defaultdict(list)
    for row in params:
        slots = [slot for slot in row.get("canonical_slots", []) if slot in PARAMETER_ALIGNMENT_SLOTS]
        if not slots:
            continue
        for value in row.get("values", []):
            value_type = str(value.get("value_type") or "")
            raw_value = str(value.get("raw_value") or "").strip()
            normalized_value = normalize_parameter_value(raw_value)
            if not raw_value or normalized_value in {"value:", "tol:"}:
                continue
            unit_kind = parameter_unit_kind(value_type, raw_value)
            for slot in slots:
                grouped[(slot, value_type, unit_kind)].append(
                    {
                        "doc_id": row.get("doc_id", ""),
                        "rel_path": row.get("rel_path", ""),
                        "stage": row.get("stage", ""),
                        "doc_type": row.get("doc_type", ""),
                        "line": row.get("line", 0),
                        "slot": slot,
                        "value_type": value_type,
                        "unit_kind": unit_kind,
                        "raw_value": raw_value,
                        "normalized_value": normalized_value,
                        "source_text": row.get("source_text", ""),
                    }
                )

    evidence_rows = []
    for (slot, value_type, unit_kind), rows in grouped.items():
        values_by_norm: dict[str, list[dict]] = defaultdict(list)
        for row in rows:
            values_by_norm[row["normalized_value"]].append(row)
        if len(values_by_norm) < 2:
            continue
        rel_paths = {row["rel_path"] for row in rows if row.get("rel_path")}
        stages = {row["stage"] for row in rows if row.get("stage")}
        if len(rel_paths) < 2:
            continue
        evidence = []
        for normalized_value, value_rows in sorted(values_by_norm.items()):
            representative = sorted(value_rows, key=lambda item: (item.get("stage", ""), item.get("rel_path", ""), item.get("line", 0)))[0]
            evidence.append(
                {
                    "normalized_value": normalized_value,
                    "raw_value": representative.get("raw_value", ""),
                    "doc_id": representative.get("doc_id", ""),
                    "rel_path": representative.get("rel_path", ""),
                    "stage": representative.get("stage", ""),
                    "doc_type": representative.get("doc_type", ""),
                    "line": representative.get("line", 0),
                    "source_text": representative.get("source_text", "")[:500],
                    "same_value_count": len(value_rows),
                }
            )
        evidence = evidence[:8]
        first = evidence[0]
        raw_values = ", ".join(item["raw_value"] for item in evidence)
        stage_text = ", ".join(sorted(stages)[:8])
        evidence_rows.append(
            {
                "evidence_type": "parameter_alignment_signal",
                "doc_id": first.get("doc_id", ""),
                "rel_path": first.get("rel_path", ""),
                "line": first.get("line", 0),
                "source_text": f"{slot}/{value_type}/{unit_kind}: {raw_values}; stages: {stage_text}",
                "term": f"parameter_alignment:{slot}:{value_type}:{unit_kind}",
                "parameter_alignment_evidence": evidence,
                "parameter_alignment_distinct_values": len(values_by_norm),
                "parameter_alignment_doc_count": len(rel_paths),
            }
        )

    def sort_key(row: dict) -> tuple[int, int, str]:
        return (
            -int(row.get("parameter_alignment_distinct_values", 0)),
            -int(row.get("parameter_alignment_doc_count", 0)),
            str(row.get("term", "")),
        )

    return sorted(evidence_rows, key=sort_key)[:max_rows]


def scan_residue_full(manifest: list[dict]) -> tuple[list[dict], list[dict]]:
    rows = []
    evidence_rows = []
    per_doc_term_count: dict[tuple[str, str], int] = defaultdict(int)
    for doc in manifest:
        lines = read_text(Path(doc["path"])).splitlines()
        for i, line in enumerate(lines, start=1):
            for term in RESIDUE_TERMS_FULL:
                if term not in line:
                    continue
                key = (doc["doc_id"], term)
                if per_doc_term_count[key] >= 8:
                    continue
                per_doc_term_count[key] += 1
                row = {
                    "doc_id": doc["doc_id"],
                    "rel_path": doc["rel_path"],
                    "line": i,
                    "term": term,
                    "source_text": line.strip()[:500],
                    "excluded_from_primary_scope": doc["excluded_from_primary_scope"],
                }
                rows.append(row)
                evidence_rows.append(
                    {
                        "doc_id": doc["doc_id"],
                        "rel_path": doc["rel_path"],
                        "line": i,
                        "term": term,
                        "evidence_type": "residue_or_template_term_signal",
                        "source_text": line.strip()[:500],
                        "excluded_from_primary_scope": doc["excluded_from_primary_scope"],
                    }
                )
    return rows, evidence_rows


DOC_NUMBER_RE = re.compile(
    r"\b(?:PT9L|PT9C|PT3SBT|PT3|PT2L|BP3L|IFT|ETX|TX)[A-Z0-9锛堬級()缇庝簹_\-]*[A-Z]{2,}[A-Z0-9锛堬級()缇庝簹_\-]*\d{1,4}\b",
    re.I,
)
VERSION_RE = re.compile(r"\bV\s*(\d+(?:\.\d+)*)\b", re.I)


def normalize_doc_number(text: str) -> str:
    return re.sub(r"[\s_锛堬級()]+", "", text).upper()


def extract_doc_numbers(text: str) -> list[str]:
    seen = []
    for match in DOC_NUMBER_RE.findall(text):
        normalized = normalize_doc_number(match)
        if len(normalized) >= 5 and normalized not in seen:
            seen.append(normalized)
    return seen


def extract_version(text: str) -> str:
    match = VERSION_RE.search(text)
    if not match:
        return ""
    return f"V{match.group(1)}"


def build_relation_index_full(manifest: list[dict]) -> tuple[list[dict], list[dict]]:
    nodes = []
    edges = []
    type_hits: dict[str, list[dict]] = defaultdict(list)
    doc_number_nodes: dict[str, list[dict]] = defaultdict(list)
    doc_number_versions: dict[str, set[str]] = defaultdict(set)
    node_id = 1
    for doc in manifest:
        if doc["excluded_from_primary_scope"] and not doc["doc_type"].startswith("risk"):
            continue
        doc_numbers = extract_doc_numbers(doc["rel_path"])
        version = extract_version(doc["rel_path"])
        for doc_number in doc_numbers:
            doc_node = {
                "node_id": f"N{node_id:06d}",
                "node_type": "document_number",
                "label": doc_number,
                "doc_id": doc["doc_id"],
                "rel_path": doc["rel_path"],
                "line": 0,
                "source_text": doc["rel_path"][:500],
                "version": version,
            }
            nodes.append(doc_node)
            doc_number_nodes[doc_number].append(doc_node)
            if version:
                doc_number_versions[doc_number].add(version)
            node_id += 1
        lines = read_text(Path(doc["path"])).splitlines()
        doc_hit_count = 0
        for i, line in enumerate(lines, start=1):
            lower = line.lower()
            for doc_number in extract_doc_numbers(line):
                ref_node = {
                    "node_id": f"N{node_id:06d}",
                    "node_type": "document_reference",
                    "label": doc_number,
                    "doc_id": doc["doc_id"],
                    "rel_path": doc["rel_path"],
                    "line": i,
                    "source_text": line.strip()[:500],
                    "version": extract_version(line),
                }
                nodes.append(ref_node)
                doc_number_nodes[doc_number].append(ref_node)
                if ref_node["version"]:
                    doc_number_versions[doc_number].add(ref_node["version"])
                node_id += 1
                doc_hit_count += 1
                break
            for node_type, words in RELATION_KEYWORDS.items():
                if any(word.lower() in lower for word in words):
                    node = {
                        "node_id": f"N{node_id:06d}",
                        "node_type": node_type,
                        "label": line.strip()[:120],
                        "doc_id": doc["doc_id"],
                        "rel_path": doc["rel_path"],
                        "line": i,
                        "source_text": line.strip()[:500],
                    }
                    nodes.append(node)
                    type_hits[node_type].append(node)
                    node_id += 1
                    doc_hit_count += 1
                    break
            if doc_hit_count >= 25 or len(nodes) >= 4000:
                break
        if len(nodes) >= 4000:
            break

    for src_type, tgt_type, edge_type in [
        ("requirement", "design_input", "DERIVES_TO_CANDIDATE"),
        ("risk", "control", "MITIGATED_BY_CANDIDATE"),
        ("control", "verification", "VERIFIED_BY_CANDIDATE"),
        ("verification", "report", "EVIDENCED_BY_CANDIDATE"),
    ]:
        if type_hits.get(src_type) and type_hits.get(tgt_type):
            edges.append(
                {
                    "edge_id": f"E{len(edges)+1:06d}",
                    "source_id": type_hits[src_type][0]["node_id"],
                    "target_id": type_hits[tgt_type][0]["node_id"],
                    "edge_type": edge_type,
                    "evidence": "full-corpus keyword co-occurrence; needs agent confirmation",
                }
            )
    for doc_number, ref_nodes in doc_number_nodes.items():
        definition_nodes = [row for row in ref_nodes if row["node_type"] == "document_number"]
        reference_nodes = [row for row in ref_nodes if row["node_type"] == "document_reference"]
        for ref_node in reference_nodes[:80]:
            targets = [
                row for row in definition_nodes
                if row["doc_id"] != ref_node["doc_id"]
            ][:5]
            for target in targets:
                edges.append(
                    {
                        "edge_id": f"E{len(edges)+1:06d}",
                        "source_id": ref_node["node_id"],
                        "target_id": target["node_id"],
                        "edge_type": "REFERENCES_DOCUMENT",
                        "doc_number": doc_number,
                        "confidence": "medium",
                        "evidence": ref_node["source_text"],
                    }
                )
                versions = sorted(doc_number_versions.get(doc_number, set()))
                if ref_node.get("version") and versions and ref_node["version"] != versions[-1]:
                    edges.append(
                        {
                            "edge_id": f"E{len(edges)+1:06d}",
                            "source_id": ref_node["node_id"],
                            "target_id": target["node_id"],
                            "edge_type": "STALE_VERSION_REFERENCE_CANDIDATE",
                            "doc_number": doc_number,
                            "referenced_version": ref_node["version"],
                            "known_versions": versions,
                            "confidence": "low",
                            "evidence": ref_node["source_text"],
                        }
                    )
            if len(edges) >= 1200:
                return nodes, edges
    return nodes, edges


def find_lines(
    manifest: list[dict],
    patterns: list[str],
    rel_contains: list[str] | None = None,
    doc_types: set[str] | None = None,
    include_auxiliary: bool = True,
    max_hits: int = 80,
    per_doc_limit: int = 6,
) -> list[dict]:
    compiled = [re.compile(pattern, re.I) for pattern in patterns]
    hits = []
    ordered_manifest = sorted(manifest, key=lambda row: (row["excluded_from_primary_scope"], row["rel_path"]))
    for doc in ordered_manifest:
        rel_path = doc["rel_path"]
        if rel_contains and not any(token in rel_path for token in rel_contains):
            continue
        if doc_types and doc["doc_type"] not in doc_types:
            continue
        if not include_auxiliary and doc["excluded_from_primary_scope"]:
            continue
        doc_hits = 0
        for i, line in enumerate(read_text(Path(doc["path"])).splitlines(), start=1):
            if any(pattern.search(line) for pattern in compiled):
                hits.append(
                    {
                        "doc_id": doc["doc_id"],
                        "rel_path": rel_path,
                        "line": i,
                        "source_text": line.strip()[:800],
                        "excluded_from_primary_scope": doc["excluded_from_primary_scope"],
                    }
                )
                doc_hits += 1
                if len(hits) >= max_hits:
                    return hits
                if doc_hits >= per_doc_limit:
                    break
    return hits


def add_evidence(catalog: dict[str, dict], prefix: str, hits: list[dict]) -> list[dict]:
    rows = []
    seen = set()
    idx = sum(1 for key in catalog if key.startswith(prefix)) + 1
    for hit in hits:
        key = (hit["rel_path"], hit["line"], hit["source_text"])
        if key in seen:
            continue
        seen.add(key)
        evidence_id = f"{prefix}-{idx:03d}"
        idx += 1
        ref = {
            "evidence_id": evidence_id,
            "doc_id": hit["doc_id"],
            "rel_path": hit["rel_path"],
            "line": int(hit["line"]),
            "source_text": hit["source_text"][:800],
            "excluded_from_primary_scope": hit.get("excluded_from_primary_scope", False),
        }
        catalog[evidence_id] = ref
        rows.append(ref)
    return rows


def parse_json_object(text: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
    try:
        return json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.S)
        if not match:
            raise
        return json.loads(match.group(0))


def parse_agent_json_relaxed(text: str, agent_name: str) -> dict:
    text = text.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
        text = re.sub(r"```$", "", text).strip()
    result: dict[str, Any] = {"agent": agent_name, "summary": "", "review_notes": [], "findings": []}
    current: dict[str, Any] | None = None
    active_array: str | None = None
    inside_findings = False

    def line_value(line: str) -> str:
        if ":" not in line:
            return ""
        part = line.split(":", 1)[1].strip().rstrip(",")
        if part.startswith('"') and part.endswith('"'):
            part = part[1:-1]
        return part

    def array_item(line: str) -> str:
        part = line.strip().rstrip(",")
        if part.startswith('"') and part.endswith('"'):
            part = part[1:-1]
        return part

    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if re.match(r'"agent"\s*:', line):
            result["agent"] = line_value(line) or agent_name
        elif re.match(r'"summary"\s*:', line):
            result["summary"] = line_value(line)
        elif re.match(r'"review_notes"\s*:\s*\[', line):
            active_array = "review_notes"
        elif re.match(r'"findings"\s*:\s*\[', line):
            inside_findings = True
            active_array = None
        elif line.startswith("{") and inside_findings and current is None:
            current = {
                "finding_type": "",
                "severity": "P2",
                "claim": "",
                "rationale": "",
                "evidence_ids": [],
                "challenge_questions": [],
            }
        elif line.startswith("}") and current is not None:
            result["findings"].append(current)
            current = None
            active_array = None
        elif re.match(r'"finding_type"\s*:', line) and current is not None:
            current["finding_type"] = line_value(line)
        elif re.match(r'"severity"\s*:', line) and current is not None:
            current["severity"] = line_value(line)
        elif re.match(r'"claim"\s*:', line) and current is not None:
            current["claim"] = line_value(line)
        elif re.match(r'"rationale"\s*:', line) and current is not None:
            current["rationale"] = line_value(line)
        elif re.match(r'"evidence_ids"\s*:', line) and current is not None:
            active_array = "evidence_ids"
            if "[" in line and "]" in line:
                current["evidence_ids"] = re.findall(r'"([^"]+)"', line.split("[", 1)[1].rsplit("]", 1)[0])
                active_array = None
        elif re.match(r'"challenge_questions"\s*:', line) and current is not None:
            active_array = "challenge_questions"
            if "[" in line and "]" in line:
                current["challenge_questions"] = re.findall(r'"([^"]+)"', line.split("[", 1)[1].rsplit("]", 1)[0])
                active_array = None
        elif line.startswith("]"):
            if active_array is None and inside_findings and current is None:
                inside_findings = False
            active_array = None
        elif active_array == "review_notes":
            note = array_item(line)
            if note and not note.startswith("]"):
                result["review_notes"].append(note)
        elif active_array == "evidence_ids" and current is not None:
            current["evidence_ids"].extend(re.findall(r'"([^"]+)"', line))
        elif active_array == "challenge_questions" and current is not None:
            question = array_item(line)
            if question and not question.startswith("]"):
                current["challenge_questions"].append(question)

    if current is not None and (current.get("claim") or current.get("evidence_ids")):
        result["findings"].append(current)
    if not result["summary"] and not result["findings"]:
        raise json.JSONDecodeError("relaxed parser could not recover agent output", text, 0)
    return result


def complete_with_fallback(client: OpenAI, model: str, messages: list[dict], max_tokens: int = 6000):
    try:
        return client.chat.completions.create(
            model=model,
            messages=messages,
            temperature=0.1,
            max_tokens=max_tokens,
            response_format={"type": "json_object"},
        )
    except Exception as exc:
        message = str(exc).lower()
        unsupported_json_mode = "response_format" in message or "json_object" in message
        unsupported_temperature = "temperature" in message
        unsupported_tokens = "max_tokens" in message
        kwargs: dict[str, Any] = {"model": model, "messages": messages}
        if not unsupported_temperature:
            kwargs["temperature"] = 0.1
        if not unsupported_tokens:
            kwargs["max_tokens"] = max_tokens
        if unsupported_json_mode:
            return client.chat.completions.create(**kwargs)
        raise


def repair_json_with_llm(client: OpenAI, model: str, agent_name: str, broken_text: str) -> dict:
    repair_messages = [
        {"role": "system", "content": "浣犳槸 JSON 淇鍣ㄣ€傚彧杈撳嚭涓ユ牸 JSON锛屼笉瑕佽В閲婏紝涓嶈 Markdown銆?"},
        {
            "role": "user",
            "content": json.dumps(
                {
                    "task": "灏嗕笅闈㈣鎴柇鎴栨牸寮忎笉瀹屾暣鐨勫唴瀹逛慨澶嶆垚涓€涓畬鏁?JSON 瀵硅薄銆備笉瑕佹柊澧炶瘉鎹紝涓嶈鎵╁啓銆?",
                    "required_schema": {
                        "agent": agent_name,
                        "summary": "string",
                        "review_notes": ["string"],
                        "findings": [
                            {
                                "finding_type": "snake_case",
                                "severity": "P1/P2/P3",
                                "claim": "string",
                                "rationale": "string",
                                "evidence_ids": ["EV-ID"],
                                "challenge_questions": ["string"],
                            }
                        ],
                    },
                    "broken_text": broken_text[:12000],
                },
                ensure_ascii=False,
            ),
        },
    ]
    response = complete_with_fallback(client, model, repair_messages, max_tokens=4000)
    content = response.choices[0].message.content or "{}"
    return parse_json_object(content)


def llm_json(agent_name: str, task: dict, output_root: Path, raw_key: str | None = None) -> dict:
    client, model = make_client()
    system = (
        "You are a DHF/DMR consistency audit domain agent. "
        "Use only provided evidence IDs and do not invent files, line numbers, or facts. "
        "Return strict JSON only, with no Markdown."
    )
    user = {
        "agent_name": agent_name,
        "role": task["role"],
        "audit_goal": task["goal"],
        "rules": [
            "Every finding must cite evidence_ids.",
            "Allowed severity values are P0, P1, P2, P3.",
            "Write claim and rationale as reviewable conclusions.",
            "Use challenge_questions for follow-up audit questions.",
            "Return all real findings; do not pad to a fixed count.",
        ],
        "expected_json_schema": {
            "agent": agent_name,
            "summary": "one sentence summary",
            "review_notes": ["non-finding observations"],
            "findings": [
                {
                    "finding_type": "snake_case",
                    "severity": "P1/P2/P3",
                    "claim": "reviewable conclusion",
                    "rationale": "evidence-based reason",
                    "evidence_ids": ["EV-ID"],
                    "challenge_questions": ["question to ask during challenge"],
                }
            ],
        },
        "task_package": task,
    }
    safe_agent_name = safe_name(raw_key or agent_name)
    raw_path = output_root / "11_llm_raw" / f"{safe_agent_name}.json"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    messages = [
        {"role": "system", "content": system},
        {"role": "user", "content": json.dumps(user, ensure_ascii=False)},
    ]
    response = complete_with_fallback(client, model, messages, max_tokens=6000)
    content = response.choices[0].message.content or "{}"
    raw_path.write_text(content, encoding="utf-8")
    try:
        parsed = parse_json_object(content)
    except json.JSONDecodeError:
        try:
            parsed = parse_agent_json_relaxed(content, agent_name)
        except json.JSONDecodeError:
            try:
                parsed = repair_json_with_llm(client, model, agent_name, content)
            except json.JSONDecodeError:
                parsed = {
                    "agent": agent_name,
                    "summary": "妯″瀷杩斿洖浜嗕笉鍙В鏋?JSON锛屽師濮嬭緭鍑哄凡淇濆瓨鍒?11_llm_raw锛涙湰 Agent 鏈涓嶅啓鍏ヨ涔?finding銆?",
                    "review_notes": ["raw_output_parse_failed"],
                    "findings": [],
                }
        (output_root / "11_llm_raw" / f"{safe_agent_name}_repaired.json").write_text(
            json.dumps(parsed, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
    parsed.setdefault("agent", agent_name)
    parsed.setdefault("review_notes", [])
    parsed.setdefault("findings", [])
    parsed["findings"] = parsed["findings"][:20]
    for finding in parsed["findings"]:
        finding["evidence_ids"] = list(dict.fromkeys(finding.get("evidence_ids", [])))[:5]
    return parsed


def normalize_for_match(text: str) -> str:
    text = text.replace("?", "?C")
    text = re.sub(r"(?<=\d),(?=\d)", ".", text)
    return re.sub(r"\s+", "", text)


def verify_ref(input_root: Path, ref: dict) -> dict:
    path = input_root / ref["rel_path"]
    verified = False
    actual = ""
    if path.exists() and ref.get("line"):
        lines = read_text(path).splitlines()
        line_no = int(ref["line"])
        if 1 <= line_no <= len(lines):
            actual = lines[line_no - 1].strip()
            expected = str(ref.get("source_text", "")).strip()
            if expected:
                verified = normalize_for_match(expected[:120]) in normalize_for_match(actual)
            else:
                verified = bool(actual)
    return {**ref, "verified": verified, "actual_text": actual[:800]}


def run_agent_llm(output_root: Path, key: str, agent_name: str, task: dict) -> dict:
    result = llm_json(agent_name, task, output_root, raw_key=key)
    write_json(output_root / "05_agent_notes" / f"{safe_name(key)}_agent_llm.json", result)
    return result


def normalize_project_profile(raw: dict) -> dict:
    profile = raw.get("project_profile") if isinstance(raw.get("project_profile"), dict) else {}
    product_family = profile.get("product_family") if isinstance(profile.get("product_family"), list) else []
    document_id_patterns = profile.get("document_id_patterns") if isinstance(profile.get("document_id_patterns"), list) else []
    primary_scope_rules = profile.get("primary_scope_rules") if isinstance(profile.get("primary_scope_rules"), list) else []
    candidate_hints = profile.get("candidate_discovery_hints") if isinstance(profile.get("candidate_discovery_hints"), list) else []
    return {
        "profile_source": "Project Scout Agent",
        "target_model": str(profile.get("target_model") or raw.get("target_model") or "PT9L"),
        "product_family": product_family,
        "document_id_patterns": document_id_patterns,
        "primary_scope_rules": primary_scope_rules,
        "key_entities": profile.get("key_entities") if isinstance(profile.get("key_entities"), dict) else {},
        "regulatory_baseline": profile.get("regulatory_baseline") if isinstance(profile.get("regulatory_baseline"), list) else [],
        "candidate_discovery_hints": candidate_hints,
    }


def build_mandatory_audit_matrix(project_profile: dict) -> list[dict]:
    target_model = str(project_profile.get("target_model") or "PT9L")
    rows = []
    routing_policy = load_routing_config()["orchestrator_policy"]
    matrix = routing_policy["mandatory_coverage"]["audit_matrix"]
    for row in matrix:
        item = dict(row)
        item["check_goal"] = str(item.get("check_goal", "")).format(target_model=target_model)
        if "assigned_agent" not in item and item.get("suggested_agent"):
            item["assigned_agent"] = item["suggested_agent"]
        rows.append(item)
    return rows


def normalize_candidate_discovery_output(raw: dict, package_id: str) -> list[dict]:
    candidates = raw.get("candidates") if isinstance(raw.get("candidates"), list) else []
    rows: list[dict] = []
    for idx, item in enumerate(candidates, start=1):
        if not isinstance(item, dict):
            continue
        evidence_refs = item.get("evidence_refs") if isinstance(item.get("evidence_refs"), list) else []
        missing_context = item.get("missing_context") if isinstance(item.get("missing_context"), list) else []
        rows.append(
            {
                "candidate_id": f"CD-{package_id}-{idx:04d}",
                "source": "candidate_discovery_agent",
                "package_id": package_id,
                "candidate_type": str(item.get("candidate_type") or "semantic_candidate"),
                "claim": str(item.get("claim") or ""),
                "why_suspicious": str(item.get("why_suspicious") or ""),
                "recommended_agent": str(item.get("recommended_agent") or "Regulatory Agent"),
                "confidence": str(item.get("confidence") or "medium"),
                "evidence_refs": evidence_refs,
                "missing_context": missing_context,
                "review_status": "candidate",
            }
        )
    return rows


def normalize_evidence_tool_hit(row: dict, source_tool: str) -> dict:
    return {
        "record_type": "evidence_hit",
        "source_tool": source_tool,
        "matched_text": str(row.get("term") or row.get("matched_text") or ""),
        "rel_path": row.get("rel_path", ""),
        "line": row.get("line", ""),
        "source_text": row.get("source_text", ""),
        "raw_finding_type": row.get("finding_type", ""),
        "note": "Evidence retrieval output only; Candidate Discovery Agent must decide whether this becomes a candidate hypothesis.",
    }


def normalize_orchestrator_route_plan(parsed: dict, available_agents: set[str], cycle_no: int) -> dict:
    allowed_decisions = {"continue", "stop", "human_review"}
    allowed_task_types = {"candidate_discovery", "domain_review", "context_recheck"}
    decision = str(parsed.get("decision") or "human_review")
    if decision not in allowed_decisions:
        decision = "human_review"
    assignments = []
    raw_assignments = parsed.get("assignments") if isinstance(parsed.get("assignments"), list) else []
    for idx, item in enumerate(raw_assignments, start=1):
        if not isinstance(item, dict):
            continue
        target_agent = str(item.get("target_agent") or "")
        if target_agent not in available_agents:
            continue
        task_type = str(item.get("task_type") or "domain_review")
        if task_type not in allowed_task_types:
            task_type = "domain_review"
        assignment = {
            "assignment_id": str(item.get("assignment_id") or f"ASG-{cycle_no:03d}-{idx:04d}"),
            "target_agent": target_agent,
            "task_type": task_type,
            "review_focus": str(item.get("review_focus") or ""),
            "input_refs": item.get("input_refs") if isinstance(item.get("input_refs"), list) else [],
            "evidence_strategy": item.get("evidence_strategy") if isinstance(item.get("evidence_strategy"), dict) else {},
            "routing_source": "orchestrator_llm",
            "review_status": "candidate",
            "final_decision": None,
        }
        assignments.append(assignment)
    return {
        "cycle": cycle_no,
        "decision": decision,
        "reason": str(parsed.get("reason") or ""),
        "assignments": assignments,
        "stop_conditions_checked": parsed.get("stop_conditions_checked") if isinstance(parsed.get("stop_conditions_checked"), list) else [],
        "human_review_items": parsed.get("human_review_items") if isinstance(parsed.get("human_review_items"), list) else [],
    }


def summarize_agent_runs(agent_runs: list[dict]) -> list[dict]:
    return [
        {
            "run_id": row.get("run_id", ""),
            "agent": row.get("agent", ""),
            "task_type": row.get("task_type", ""),
            "assignment_id": row.get("assignment_id", ""),
            "summary": row.get("llm_output", {}).get("summary", ""),
            "finding_count": len(row.get("llm_output", {}).get("findings", [])),
            "candidate_count": len(row.get("llm_output", {}).get("candidates", [])),
        }
        for row in agent_runs
    ]


def call_orchestrator_route_plan(state: FullAuditState, cycle_no: int, output_root: Path) -> dict:
    config = load_agent_config("orchestrator")
    registry = build_assignable_agent_registry()
    payload = {
        "agent": config["display_name"],
        "cycle": cycle_no,
        "project_profile": state.get("project_profile", {}),
        "routing_policy": load_routing_config()["orchestrator_policy"],
        "available_agents": sorted(registry.keys()),
        "mandatory_audit_matrix": state.get("mandatory_audit_matrix", []),
        "agent_runs": summarize_agent_runs(state.get("agent_runs", [])),
        "candidate_discovery_results": state.get("candidate_discovery_results", []),
        "context_recovery_results": state.get("context_recovery_results", []),
        "required_schema": config.get("output_schema", {}),
    }
    parsed = llm_json_call(
        output_root / "11_llm_raw" / f"orchestrator_route_cycle_{cycle_no:03d}.json",
        config.get("system_prompt", "Return strict JSON route_plan only."),
        payload,
        max_tokens=5000,
    )
    return normalize_orchestrator_route_plan(parsed, set(registry.keys()), cycle_no)


def build_available_task_packages(manifest: list[dict], catalog: dict[str, dict], project_profile: dict, mandatory_audit_matrix: list[dict]) -> dict[str, dict]:
    packages: dict[str, dict] = {}
    for key, config in build_domain_agent_specs().items():
        agent_name = str(config.get("display_name") or config.get("role") or key)
        evidence = collect_configured_evidence(catalog, manifest, config)
        packages[key] = build_agent_task_from_config(
            config,
            evidence,
            project_profile=project_profile,
            mandatory_audit_matrix=[
                row for row in mandatory_audit_matrix if row.get("assigned_agent") == agent_name
            ],
            corpus_scope="full_markdown",
        )
    return packages


def filter_candidates_for_assignment(candidates: list[dict], input_refs: list) -> list[dict]:
    refs = {str(ref) for ref in input_refs if ref}
    if not refs:
        return candidates
    return [
        row for row in candidates
        if str(row.get("candidate_id", "")) in refs or str(row.get("package_id", "")) in refs
    ]


def build_assignment_task(
    assignment: dict,
    state: FullAuditState,
    registry_entry: dict,
    task_packages: dict[str, dict],
) -> dict:
    config = registry_entry["config"]
    agent_key = registry_entry["key"]
    if agent_key == "candidate_discovery":
        return build_agent_task_from_config(
            config,
            [],
            assignment=assignment,
            package_id=assignment["assignment_id"],
            project_profile=state.get("project_profile", {}),
            mandatory_audit_matrix=state.get("mandatory_audit_matrix", []),
            document_package={"available_domain_packages": task_packages},
            evidence_retrieval_tools={
                "page_index": "available through page_index evidence records",
                "relation_index": "available through relation_nodes and relation_edges",
                "full_text": "available through file snippets in evidence_catalog",
                "file_reader": "available to Context Recovery and follow-up review",
            },
            evidence_tool_hits_sample=state.get("evidence_tool_hits", [])[:80],
            agent_runs=summarize_agent_runs(state.get("agent_runs", [])),
            candidate_discovery_results=state.get("candidate_discovery_results", []),
        )

    task = dict(task_packages.get(agent_key, {}))
    task["assignment"] = assignment
    task["candidate_discovery_inputs"] = filter_candidates_for_assignment(
        state.get("candidate_discovery_results", []),
        assignment.get("input_refs", []),
    )
    task["agent_runs"] = summarize_agent_runs(state.get("agent_runs", []))
    return task


def execute_agent_assignment(
    state: FullAuditState,
    assignment: dict,
    task_packages: dict[str, dict],
    registry: dict[str, dict],
    output_root: Path,
) -> tuple[dict, list[dict]]:
    agent_name = assignment["target_agent"]
    registry_entry = registry[agent_name]
    agent_runs = list(state.get("agent_runs", []))
    run_id = f"RUN-{len(agent_runs) + 1:04d}"
    task = build_assignment_task(assignment, state, registry_entry, task_packages)
    output = run_agent_llm(output_root, f"{run_id}_{safe_name(agent_name)}", agent_name, task)
    run_record = {
        "run_id": run_id,
        "agent": agent_name,
        "assignment_id": assignment["assignment_id"],
        "task_type": assignment["task_type"],
        "assignment": assignment,
        "input_package": task,
        "llm_output": output,
        "findings": output.get("findings", []),
        "status": "completed",
    }
    write_json(output_root / "05_agent_notes" / "agent_runs" / f"{run_id}_{safe_name(agent_name)}.json", run_record)
    new_candidates: list[dict] = []
    if agent_name == "Candidate Discovery Agent":
        new_candidates = normalize_candidate_discovery_output(output, package_id=run_id)
    return run_record, new_candidates


def context_recovery_round_strategy(round_no: int) -> dict:
    strategies = {
        1: {
            "focus": "local_context",
            "instruction": "Expand the immediate local context around the cited evidence: nearby lines, full table rows and columns, section heading, and document metadata.",
        },
        2: {
            "focus": "same_entity_context",
            "instruction": "Search for the same model, material number, parameter, document number, requirement ID, or risk ID across the corpus.",
        },
        3: {
            "focus": "lifecycle_context",
            "instruction": "Expand upstream and downstream lifecycle evidence such as input-to-output, risk-to-control-to-verification, and BOM-to-process-to-inspection chains.",
        },
        4: {
            "focus": "document_control_context",
            "instruction": "Check controlled status and version context: cover pages, revision history, signatures, document lists, change records, archive and obsolete markers.",
        },
        5: {
            "focus": "counter_evidence_and_human_review_pack",
            "instruction": "Collect evidence for confirm, counter-evidence for dismiss, remaining gaps, and a concise human-review pack.",
        },
    }
    return strategies.get(round_no, strategies[5])


def bootstrap_node(state: FullAuditState) -> FullAuditState:
    input_root = Path(state["input_root"])
    output_root = Path(state["output_root"])
    ensure_dirs(output_root)

    manifest = make_full_manifest(input_root)
    readiness = readiness_checks(manifest)
    page_index = build_page_index(manifest)
    params = extract_parameters_full(manifest)
    residue_rows, residue_evidence_rows = scan_residue_full(manifest)
    parameter_conflict_evidence_rows = analyze_parameter_conflicts(params)
    parameter_alignment_evidence_rows = build_parameter_alignment_evidence_rows(params)
    relation_nodes, relation_edges = build_relation_index_full(manifest)
    evidence_tool_hits = [
        normalize_evidence_tool_hit(row, "legacy_residue_scan")
        for row in residue_evidence_rows
    ] + [
        normalize_evidence_tool_hit(row, "parameter_conflict_scan")
        for row in parameter_conflict_evidence_rows
    ] + [
        normalize_evidence_tool_hit(row, "parameter_alignment_evidence_scan")
        for row in parameter_alignment_evidence_rows
    ]

    write_jsonl(output_root / "00_manifest" / "full_manifest.jsonl", manifest)
    write_jsonl(output_root / "00_manifest" / "document_readiness.jsonl", readiness)
    write_jsonl(output_root / "01_page_index" / "page_index.jsonl", page_index)
    write_jsonl(output_root / "03_ssot_parameters" / "parameter_instances.jsonl", params)
    write_jsonl(output_root / "03_ssot_parameters" / "parameter_alignment_evidence_rows.jsonl", parameter_alignment_evidence_rows)
    write_jsonl(output_root / "03_ssot_parameters" / "parameter_conflict_evidence_rows.jsonl", parameter_conflict_evidence_rows)
    write_jsonl(output_root / "04_relation_index" / "nodes.jsonl", relation_nodes)
    write_jsonl(output_root / "04_relation_index" / "edges.jsonl", relation_edges)
    write_jsonl(output_root / "06_evidence_tools" / "residue_hits.jsonl", residue_rows)
    write_jsonl(output_root / "06_evidence_tools" / "evidence_tool_hits.jsonl", evidence_tool_hits)

    coverage = {
        "total_markdown_docs": len(manifest),
        "primary_scope_docs": sum(1 for row in manifest if not row["excluded_from_primary_scope"]),
        "auxiliary_scope_docs": sum(1 for row in manifest if row["excluded_from_primary_scope"]),
        "doc_type_counts": Counter(row["doc_type"] for row in manifest),
        "stage_counts": Counter(row["stage"] for row in manifest),
        "readiness_flag_counts": Counter(flag for row in readiness for flag in row["flags"]),
    }
    write_json(output_root / "00_manifest" / "coverage_ledger.json", coverage)

    return {
        **state,
        "manifest": manifest,
        "readiness": readiness,
        "page_index": page_index,
        "params": params,
        "relation_nodes": relation_nodes,
        "relation_edges": relation_edges,
        "evidence_tool_hits": evidence_tool_hits,
        "evidence_catalog": {},
    }


def scout_node(state: FullAuditState) -> FullAuditState:
    output_root = Path(state["output_root"])
    manifest = state["manifest"]
    catalog = dict(state["evidence_catalog"])
    config = load_agent_config("project_scout")
    evidence = collect_configured_evidence(catalog, manifest, config)
    task = build_agent_task_from_config(config, evidence, corpus_scope="full_markdown")
    write_json(output_root / "10_task_packages" / "scout_task.json", task)
    output = run_agent_llm(output_root, "scout", config["display_name"], task)
    project_profile = normalize_project_profile(output)
    write_json(output_root / "02_blackboard" / "project_profile.json", project_profile)
    return {**state, "evidence_catalog": catalog, "scout_output": output, "project_profile": project_profile}


def orchestrator_node(state: FullAuditState) -> FullAuditState:
    output_root = Path(state["output_root"])
    manifest = state["manifest"]
    catalog = dict(state["evidence_catalog"])
    project_profile = state.get("project_profile", {})
    mandatory_audit_matrix = build_mandatory_audit_matrix(project_profile)
    packages = build_available_task_packages(manifest, catalog, project_profile, mandatory_audit_matrix)
    registry = build_assignable_agent_registry()
    route_plans: list[dict] = []
    agent_runs: list[dict] = list(state.get("agent_runs", []))
    candidate_discovery_results: list[dict] = list(state.get("candidate_discovery_results", []))

    working_state: FullAuditState = {
        **state,
        "evidence_catalog": catalog,
        "task_packages": packages,
        "mandatory_audit_matrix": mandatory_audit_matrix,
        "agent_runs": agent_runs,
        "candidate_discovery_results": candidate_discovery_results,
        "orchestrator_route_plans": route_plans,
    }

    for cycle_no in range(1, ORCHESTRATOR_SAFETY_CYCLE_LIMIT + 1):
        raw_plan = call_orchestrator_route_plan(working_state, cycle_no, output_root)
        plan = normalize_orchestrator_route_plan(raw_plan, set(registry.keys()), cycle_no)
        route_plans.append(plan)
        write_json(output_root / "10_task_packages" / f"orchestrator_route_plan_cycle_{cycle_no:03d}.json", plan)

        if plan["decision"] in {"stop", "human_review"}:
            break
        if not plan["assignments"]:
            route_plans.append(
                {
                    "cycle": cycle_no,
                    "decision": "human_review",
                    "reason": "Orchestrator returned continue without assignments.",
                    "assignments": [],
                    "stop_conditions_checked": [],
                    "human_review_items": [],
                }
            )
            break

        for assignment in plan["assignments"]:
            run_record, new_candidates = execute_agent_assignment(
                working_state,
                assignment,
                packages,
                registry,
                output_root,
            )
            agent_runs.append(run_record)
            candidate_discovery_results.extend(new_candidates)
            working_state = {
                **working_state,
                "agent_runs": agent_runs,
                "candidate_discovery_results": candidate_discovery_results,
                "orchestrator_route_plans": route_plans,
            }
    else:
        route_plans.append(
            {
                "cycle": ORCHESTRATOR_SAFETY_CYCLE_LIMIT,
                "decision": "human_review",
                "reason": "Emergency safety cycle limit reached before Orchestrator returned stop.",
                "assignments": [],
                "stop_conditions_checked": [],
                "human_review_items": [],
            }
        )

    write_json(output_root / "10_task_packages" / "mandatory_audit_matrix.json", {"matrix": mandatory_audit_matrix})
    write_json(output_root / "10_task_packages" / "available_domain_agent_tasks.json", packages)
    write_json(output_root / "10_task_packages" / "orchestrator_route_plans.json", {"route_plans": route_plans})
    write_jsonl(output_root / "05_agent_notes" / "agent_runs.jsonl", agent_runs)
    write_jsonl(output_root / "07_findings" / "candidate_discovery_results.jsonl", candidate_discovery_results)
    return {
        **state,
        "evidence_catalog": catalog,
        "task_packages": packages,
        "mandatory_audit_matrix": mandatory_audit_matrix,
        "agent_runs": agent_runs,
        "candidate_discovery_results": candidate_discovery_results,
        "orchestrator_route_plans": route_plans,
    }


def collect_semantic_findings(state: FullAuditState) -> list[dict]:
    rows = []
    seq = 1
    output_sources = []
    if isinstance(state.get("scout_output"), dict):
        output_sources.append({"run_id": "SCOUT", "output": state.get("scout_output", {})})
    for run in state.get("agent_runs", []):
        if not isinstance(run, dict):
            continue
        output = run.get("llm_output") if isinstance(run.get("llm_output"), dict) else {}
        output_sources.append({"run_id": run.get("run_id", ""), "output": output})

    for source in output_sources:
        output = source["output"]
        agent = output.get("agent", "Unknown Agent")
        for finding in output.get("findings", []):
            row = dict(finding)
            row["finding_id"] = f"LLM-{seq:04d}"
            row["agent"] = agent
            row["source_run_id"] = source["run_id"]
            row.setdefault("finding_type", "semantic_review")
            row.setdefault("severity", "P2")
            row.setdefault("claim", "")
            row.setdefault("rationale", "")
            row.setdefault("challenge_questions", [])
            row["evidence_refs"] = [
                state["evidence_catalog"][eid]
                for eid in row.get("evidence_ids", [])
                if eid in state["evidence_catalog"]
            ]
            rows.append(row)
            seq += 1
    return rows


def nearby_context(input_root: Path, rel_path: str, line_no: int, radius: int = 4) -> str:
    path = input_root / rel_path
    if not path.exists() or line_no <= 0:
        return ""
    lines = read_text(path).splitlines()
    start = max(1, line_no - radius)
    end = min(len(lines), line_no + radius)
    return "\n".join(f"{i}: {lines[i - 1]}" for i in range(start, end + 1))


def evidence_gate_node(state: FullAuditState) -> FullAuditState:
    input_root = Path(state["input_root"])
    output_root = Path(state["output_root"])
    semantic = collect_semantic_findings(state)
    verified_semantic = []
    for row in semantic:
        refs = [verify_ref(input_root, ref) for ref in row.get("evidence_refs", [])]
        row["evidence_refs"] = refs
        if refs and all(ref["verified"] for ref in refs):
            row["evidence_status"] = "verified"
        elif refs and any(ref["verified"] for ref in refs):
            row["evidence_status"] = "partially_verified"
        else:
            row["evidence_status"] = "failed"
        row["challenge_status"] = "pending_challenge"
        verified_semantic.append(row)

    write_jsonl(output_root / "07_findings" / "semantic_findings_llm_pre_challenge.jsonl", verified_semantic)
    return {**state, "semantic_findings": verified_semantic, "all_findings": verified_semantic}


def challenge_json(findings: list[dict], output_root: Path) -> dict:
    def fallback_decision(row: dict, reason: str) -> dict:
        return {
            "finding_id": row["finding_id"],
            "decision": "needs_more_context",
            "reason": reason,
            "revised_severity": row.get("severity", "P2"),
        }

    def normalize_decision(decision: dict, source: dict) -> dict:
        allowed_decisions = {"keep", "revise", "drop", "needs_more_context"}
        allowed_severities = {"P0", "P1", "P2", "P3"}
        normalized = {
            "finding_id": str(decision.get("finding_id") or source["finding_id"]),
            "decision": str(decision.get("decision") or "needs_more_context"),
            "reason": str(decision.get("reason") or ""),
            "revised_severity": str(decision.get("revised_severity") or source.get("severity", "P2")),
        }
        if normalized["decision"] not in allowed_decisions:
            normalized["decision"] = "needs_more_context"
        if normalized["revised_severity"] not in allowed_severities:
            normalized["revised_severity"] = source.get("severity", "P2")
        return normalized

    def parse_challenge_json_relaxed(text: str, batch_findings: list[dict]) -> dict:
        text = text.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?", "", text).strip()
            text = re.sub(r"```$", "", text).strip()
        try:
            return parse_json_object(text)
        except json.JSONDecodeError:
            pass

        decision_region = text
        decisions_match = re.search(r'"decisions"\s*:\s*\[', text)
        if decisions_match:
            decision_region = text[decisions_match.end() :]

        decisions = []
        for row in batch_findings:
            fid = row["finding_id"]
            fid_pos = decision_region.find(fid)
            if fid_pos < 0:
                continue
            next_finding = decision_region.find('"finding_id"', fid_pos + len(fid))
            if next_finding > fid_pos:
                window = decision_region[fid_pos:next_finding]
            else:
                window = decision_region[fid_pos : fid_pos + 1400]
            decision_match = re.search(r'"decision"\s*:\s*"([^"]+)"', window)
            severity_match = re.search(r'"revised_severity"\s*:\s*"([^"]+)"', window)
            reason_match = re.search(r'"reason"\s*:\s*"((?:[^"\\]|\\.)*)"', window, flags=re.S)
            fallback_reason = "Challenge Agent JSON was incomplete; kept conservative needs_more_context."
            decisions.append(
                {
                    "finding_id": fid,
                    "decision": decision_match.group(1) if decision_match else "needs_more_context",
                    "reason": reason_match.group(1).replace("\\\"", '"').replace("\n", " ")[:300] if reason_match else fallback_reason,
                    "revised_severity": severity_match.group(1) if severity_match else row.get("severity", "P2"),
                }
            )
        if not decisions:
            raise json.JSONDecodeError("relaxed parser could not recover challenge decisions", text, 0)
        return {"agent": "Challenge Agent", "summary": "relaxed_parse_recovered", "decisions": decisions}

    def repair_challenge_json_with_llm(client, model: str, broken_text: str, batch_findings: list[dict]) -> dict:
        repair_messages = [
            {
                "role": "system",
                "content": "浣犳槸 JSON 淇鍣ㄣ€傚彧杈撳嚭涓ユ牸 JSON锛屼笉瑕佽В閲婏紝涓嶈 Markdown銆?",
            },
            {
                "role": "user",
                "content": json.dumps(
                    {
                        "task": "鎶婁笅闈?Challenge Agent 鐨勮緭鍑轰慨澶嶆垚涓ユ牸 JSON銆傚彧鑳戒繚鐣欏師鏈?finding_id 鐨勮鍐筹紝涓嶈鏂板 finding銆?",
                        "allowed_finding_ids": [row["finding_id"] for row in batch_findings],
                        "decision_values": ["keep", "revise", "drop", "needs_more_context"],
                        "required_schema": {
                            "agent": "Challenge Agent",
                            "summary": "string",
                            "decisions": [
                                {
                                    "finding_id": "LLM-0001",
                                    "decision": "keep/revise/drop/needs_more_context",
                                    "reason": "string",
                                    "revised_severity": "P0/P1/P2/P3",
                                }
                            ],
                        },
                        "broken_text": broken_text[:10000],
                    },
                    ensure_ascii=False,
                ),
            },
        ]
        response = complete_with_fallback(client, model, repair_messages, max_tokens=2500)
        repaired = response.choices[0].message.content or "{}"
        return parse_json_object(repaired)

    def run_batch(client, model: str, batch_findings: list[dict], batch_no: int) -> dict:
        payload = []
        for row in batch_findings:
            payload.append(
                {
                    "finding_id": row["finding_id"],
                    "agent": row.get("agent"),
                    "severity": row.get("severity"),
                    "finding_type": row.get("finding_type"),
                    "claim": row.get("claim"),
                    "rationale": row.get("rationale"),
                    "evidence": [
                        {
                            "rel_path": ref.get("rel_path"),
                            "line": ref.get("line"),
                            "text": (ref.get("actual_text") or ref.get("source_text", ""))[:220],
                        }
                        for ref in row.get("evidence_refs", [])[:3]
                    ],
                }
            )
        messages = [
            {
                "role": "system",
                "content": "浣犳槸鍖荤枟鍣ㄦ鏂囨。瀹℃煡鐨?Challenge Agent銆傚彧杈撳嚭涓ユ牸 JSON锛屼笉瑕?Markdown銆?",
            },
            {
                "role": "user",
                "content": json.dumps(
                    {
                        "task": "瀵规湰鎵瑰€欓€?finding 鍋氳瘉浼拰璇姤鍘嬪埗銆備笉鑳芥柊澧?finding锛屽彧鑳界粰姣忔潯 finding 鍋氳鍐炽€?",
                        "decision_values": ["keep", "revise", "drop", "needs_more_context"],
                        "decision_rules": [
                            "keep锛氳瘉鎹洿鎺ユ敮鎸佺粨璁猴紝涓斾笉鏄槑鏄捐鎶ャ€?",
                            "revise锛氭牳蹇冮棶棰樻垚绔嬶紝浣嗕弗閲嶅害鎴栬〃杩伴渶瑕佽皟鏁淬€?",
                            "drop锛氳瘉鎹笉鑳芥敮鎸佺粨璁猴紝鎴栨槑鏄炬槸璇姤/閲嶅銆?",
                            "needs_more_context锛氳瘉鎹湅璧锋潵鏈夊叧锛屼絾缂哄皯瓒冲涓婁笅鏂囷紝闇€浜哄伐澶嶆牳銆?",
                        ],
                        "required_schema": {
                            "agent": "Challenge Agent",
                            "summary": "string",
                            "decisions": [
                                {
                                    "finding_id": "LLM-0001",
                                    "decision": "keep/revise/drop/needs_more_context",
                                    "reason": "string",
                                    "revised_severity": "P0/P1/P2/P3",
                                }
                            ],
                        },
                        "findings": payload,
                    },
                    ensure_ascii=False,
                ),
            },
        ]
        raw_path = output_root / "11_llm_raw" / f"challenge_agent_batch_{batch_no:02d}.json"
        try:
            response = complete_with_fallback(client, model, messages, max_tokens=3000)
            content = response.choices[0].message.content or "{}"
        except Exception as exc:
            parsed = {
                "agent": "Challenge Agent",
                "summary": "challenge_agent_call_failed",
                "decisions": [
                    fallback_decision(row, f"Challenge Agent 璋冪敤澶辫触锛屽凡淇濆畧淇濈暀寰呰ˉ璇侊細{type(exc).__name__}: {exc}")
                    for row in batch_findings
                ],
            }
            content = json.dumps(parsed, ensure_ascii=False)
        raw_path.write_text(content, encoding="utf-8")
        try:
            parsed = parse_challenge_json_relaxed(content, batch_findings)
        except json.JSONDecodeError:
            try:
                parsed = repair_challenge_json_with_llm(client, model, content, batch_findings)
            except json.JSONDecodeError:
                parsed = {
                    "agent": "Challenge Agent",
                    "summary": "batch_parse_failed",
                    "decisions": [
                        fallback_decision(row, "Challenge Agent 鎵规杈撳嚭涓嶅彲瑙ｆ瀽锛屽凡淇濆畧淇濈暀鍊欓€?finding銆?")
                        for row in batch_findings
                    ],
                }
        parsed.setdefault("agent", "Challenge Agent")
        parsed.setdefault("summary", "")
        parsed.setdefault("decisions", [])
        by_id = {row["finding_id"]: row for row in batch_findings}
        normalized = []
        seen = set()
        for decision in parsed.get("decisions", []):
            fid = str(decision.get("finding_id") or "")
            if fid not in by_id or fid in seen:
                continue
            normalized.append(normalize_decision(decision, by_id[fid]))
            seen.add(fid)
        for row in batch_findings:
            if row["finding_id"] not in seen:
                normalized.append(fallback_decision(row, "Challenge Agent did not return a decision for this finding."))
        parsed["decisions"] = normalized
        return parsed

    client, model = make_client()
    batch_size = 5
    batches = [findings[i : i + batch_size] for i in range(0, len(findings), batch_size)]
    batch_results = [run_batch(client, model, batch, i + 1) for i, batch in enumerate(batches)]
    merged = {
        "agent": "Challenge Agent",
        "summary": f"Challenge completed for {len(findings)} semantic findings across {len(batch_results)} batches.",
        "batch_size": batch_size,
        "batch_count": len(batch_results),
        "decisions": [decision for batch in batch_results for decision in batch.get("decisions", [])],
        "batch_summaries": [
            {
                "batch_no": i + 1,
                "summary": batch.get("summary", ""),
                "decision_counts": Counter(decision.get("decision", "unknown") for decision in batch.get("decisions", [])),
            }
            for i, batch in enumerate(batch_results)
        ],
    }
    write_json(output_root / "11_llm_raw" / "challenge_agent_merged.json", merged)
    return merged


def is_weak_challenge_reason(decision: str, reason: str) -> bool:
    if decision not in {"keep", "revise"}:
        return False
    reason = str(reason or "").strip()
    if len(reason) < 36:
        return True
    if reason.endswith((":", ";", ",", "(", "[", "{")):
        return True
    if reason.count("(") != reason.count(")"):
        return True
    if reason.count("[") != reason.count("]"):
        return True
    if reason.count("{") != reason.count("}"):
        return True
    return False

def quality_guard_challenge_decision(decision: dict, source: dict) -> dict:
    guarded = dict(decision)
    status = guarded.get("decision", "needs_more_context")
    reason = str(guarded.get("reason") or "")
    if not is_weak_challenge_reason(status, reason):
        return guarded
    guarded["decision"] = "needs_more_context"
    guarded["challenge_reason_quality_flag"] = "truncated_or_weak_reason"
    guarded["original_decision"] = status
    guarded["original_reason"] = reason
    guarded["reason"] = (
        "Challenge Agent 鐨勫師濮嬭鍐崇悊鐢辫繃鐭垨鐤戜技琚埅鏂紝褰撳墠涓嶈兘绋冲仴鏀寔 "
        f"`{status}` 瑁佸喅锛屽凡淇濆畧杞负 needs_more_context锛涘師濮嬬悊鐢憋細{reason}"
    )
    guarded["revised_severity"] = guarded.get("revised_severity") or source.get("severity", "P2")
    return guarded


def load_adjudication_memory(output_root: Path) -> list[dict]:
    memory_path = output_root / "12_challenge" / "adjudication_memory.jsonl"
    if not memory_path.exists():
        return []
    rows = []
    for line in memory_path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        try:
            rows.append(json.loads(line))
        except json.JSONDecodeError:
            continue
    return rows


def apply_adjudication_memory(row: dict, memory: list[dict]) -> dict | None:
    rel_path = row.get("rel_path") or (row.get("evidence_refs") or [{}])[0].get("rel_path", "")
    finding_type = row.get("finding_type", "")
    source_text = row.get("source_text") or row.get("claim", "")
    for item in memory:
        if item.get("decision") not in {"rejected", "scope_excluded", "duplicate"}:
            continue
        if item.get("finding_type") and item.get("finding_type") != finding_type:
            continue
        if item.get("rel_path") and item.get("rel_path") != rel_path:
            continue
        needle = str(item.get("source_text", ""))[:80]
        if needle and needle not in source_text and needle not in row.get("claim", ""):
            continue
        return {
            "finding_id": row["finding_id"],
            "decision": "drop",
            "reason": f"Matched historical adjudication: {item.get('decision')}. {item.get('reason', '')}",
            "revised_severity": row.get("severity", "P2"),
        }
    return None


def challenge_node(state: FullAuditState) -> FullAuditState:
    output_root = Path(state["output_root"])
    semantic = state["semantic_findings"]
    challenge = challenge_json(semantic, output_root)
    decisions = {row.get("finding_id"): row for row in challenge.get("decisions", [])}
    memory = load_adjudication_memory(output_root)
    challenged = []
    guarded_decisions = []
    for row in semantic:
        decision = apply_adjudication_memory(row, memory) or decisions.get(row["finding_id"], {})
        decision = quality_guard_challenge_decision(decision, row)
        if decision:
            guarded_decisions.append({**decision, "finding_id": row["finding_id"]})
        row = dict(row)
        row["challenge_status"] = decision.get("decision", "needs_more_context")
        row["challenge_reason"] = decision.get("reason", "")
        if decision.get("challenge_reason_quality_flag"):
            row["challenge_reason_quality_flag"] = decision["challenge_reason_quality_flag"]
            row["challenge_original_status"] = decision.get("original_decision", "")
            row["challenge_original_reason"] = decision.get("original_reason", "")
        if decision.get("revised_severity"):
            row["severity"] = decision["revised_severity"]
        challenged.append(row)

    all_findings = challenged
    if guarded_decisions:
        challenge = {**challenge, "quality_guarded_decisions": guarded_decisions}
    write_json(output_root / "12_challenge" / "challenge_results.json", challenge)
    write_jsonl(output_root / "07_findings" / "semantic_findings_llm_challenged.jsonl", challenged)
    write_jsonl(output_root / "07_findings" / "candidate_findings_merged_full.jsonl", all_findings)
    write_jsonl(output_root / "09_evidence_gate" / "evidence_verified_all_findings.jsonl", [row for row in all_findings if row.get("evidence_status") == "verified"])
    return {**state, "semantic_findings": challenged, "all_findings": all_findings, "challenge_output": challenge}


def infer_context_need_type(row: dict) -> str:
    finding_type = str(row.get("finding_type", ""))
    term = str(row.get("term", ""))
    claim = str(row.get("claim", ""))
    text = f"{finding_type} {term} {claim}".lower()
    if "parameter_alignment" in text:
        return "parameter_semantics"
    if "traceability" in text or "杩芥函" in claim or "trace" in text:
        return "traceability_context"
    if "risk" in text or "椋庨櫓" in claim:
        return "risk_control_verification_context"
    if "model" in text or "鍨嬪彿" in claim or re.search(r"PT\d|BP\d|PT9C|PT3SBT", claim, flags=re.I):
        return "product_identity_context"
    if "blank" in text or "绌虹櫧" in claim or "寰呭～" in claim:
        return "document_control_context"
    return "neighboring_evidence_context"


def context_retrieval_plan(need_type: str) -> list[str]:
    plans = {
        "parameter_semantics": [
            "same_slot_parameter_instances",
            "same_document_neighbor_lines",
            "same_stage_and_cross_stage_parameter_context",
            "requirement_vs_test_condition_classification",
        ],
        "traceability_context": [
            "same_document_neighbor_lines",
            "upstream_downstream_traceability_docs",
            "same_topic_page_index_hits",
            "relation_index_references",
        ],
        "risk_control_verification_context": [
            "risk_plan_assessment_report_and_validation_refs",
            "relation_index_references",
            "same_risk_term_page_index_hits",
        ],
        "product_identity_context": [
            "same_term_occurrences",
            "document_control_scope",
            "same_model_page_index_hits",
            "relation_index_references",
        ],
        "document_control_context": [
            "same_document_neighbor_lines",
            "signature_and_revision_sections",
            "same_template_family_docs",
        ],
    }
    return plans.get(
        need_type,
        ["same_document_neighbor_lines", "same_topic_page_index_hits", "relation_index_references"],
    )


def build_context_recovery_tasks(state: FullAuditState) -> list[dict]:
    tasks: list[dict] = []
    for row in state.get("semantic_findings", []):
        if row.get("challenge_status") != "needs_more_context":
            continue
        need_type = infer_context_need_type(row)
        tasks.append(
            {
                "task_id": f"CTX-S-{len(tasks) + 1:04d}",
                "gap_source": "semantic",
                "source_id": row.get("finding_id", ""),
                "target_agent": row.get("agent", "Domain Agent"),
                "context_need_type": need_type,
                "retrieval_plan": context_retrieval_plan(need_type),
                "original_status": row.get("challenge_status", "needs_more_context"),
                "claim": row.get("claim", ""),
                "severity": row.get("severity", "P2"),
                "source_row": row,
            }
        )
    return tasks


def parameter_slot_from_term(term: str) -> str:
    if not term.startswith("parameter_alignment:"):
        return ""
    parts = term.split(":")
    return parts[1] if len(parts) > 1 else ""


def collect_parameter_context(task: dict, params: list[dict]) -> list[dict]:
    row = task.get("source_row", {})
    slot = parameter_slot_from_term(str(row.get("term", "")))
    if not slot:
        return []
    evidence = []
    for param in params:
        if slot not in param.get("canonical_slots", []):
            continue
        for value in param.get("values", []):
            evidence.append(
                {
                    "doc_id": param.get("doc_id", ""),
                    "rel_path": param.get("rel_path", ""),
                    "stage": param.get("stage", ""),
                    "doc_type": param.get("doc_type", ""),
                    "line": param.get("line", 0),
                    "raw_value": value.get("raw_value", ""),
                    "value_type": value.get("value_type", ""),
                    "source_text": param.get("source_text", ""),
                }
            )
    return evidence[:30]


def collect_page_context(task: dict, page_index: list[dict]) -> list[dict]:
    row = task.get("source_row", {})
    needles = [
        str(row.get("term", "")),
        str(row.get("finding_type", "")),
        str(row.get("claim", ""))[:80],
    ]
    tokens = [token for token in re.split(r"\W+", " ".join(needles), flags=re.I) if len(token) >= 3]
    results = []
    for page in page_index:
        haystack = f"{page.get('rel_path', '')} {page.get('title', '')} {page.get('text', '')}"
        if any(token and token in haystack for token in tokens[:8]):
            results.append(
                {
                    "doc_id": page.get("doc_id", ""),
                    "rel_path": page.get("rel_path", ""),
                    "line_start": page.get("line_start", page.get("line", "")),
                    "title": page.get("title", ""),
                    "text": str(page.get("text", ""))[:700],
                }
            )
    return results[:12]


def collect_context_package(task: dict, state: FullAuditState) -> dict:
    row = task.get("source_row", {})
    context = {
        "same_item_evidence": row.get("evidence_refs")
        or row.get("parameter_alignment_evidence")
        or [
            {
                "doc_id": row.get("doc_id", ""),
                "rel_path": row.get("rel_path", ""),
                "line": row.get("line", ""),
                "source_text": row.get("source_text", ""),
            }
        ],
        "parameter_context": [],
        "page_context": [],
    }
    if task.get("context_need_type") == "parameter_semantics":
        context["parameter_context"] = collect_parameter_context(task, state.get("params", []))
    context["page_context"] = collect_page_context(task, state.get("page_index", []))
    return context


def parse_context_loop_json(content: str) -> dict:
    try:
        return parse_json_object(content)
    except json.JSONDecodeError:
        text = content.strip()
        if text.startswith("```"):
            text = re.sub(r"^```(?:json)?", "", text).strip()
            text = re.sub(r"```$", "", text).strip()
        match = re.search(r"\{.*\}", text, flags=re.S)
        if not match:
            raise
        return json.loads(match.group(0))


def llm_json_call(raw_path: Path, system_prompt: str, payload: dict, max_tokens: int = 3500) -> dict:
    if raw_path.exists():
        try:
            return parse_context_loop_json(raw_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            pass

    client, model = make_client()
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
    ]
    response = complete_with_fallback(client, model, messages, max_tokens=max_tokens)
    content = response.choices[0].message.content or "{}"
    raw_path.parent.mkdir(parents=True, exist_ok=True)
    raw_path.write_text(content, encoding="utf-8")
    return parse_context_loop_json(content)


def normalize_context_recovery_llm(parsed: dict, task: dict, context: dict, round_no: int) -> dict:
    return {
        "task_id": task["task_id"],
        "round": round_no,
        "context_summary": str(parsed.get("context_summary") or parsed.get("summary") or ""),
        "evidence_gaps": parsed.get("evidence_gaps") if isinstance(parsed.get("evidence_gaps"), list) else [],
        "additional_search_queries": parsed.get("additional_search_queries") if isinstance(parsed.get("additional_search_queries"), list) else [],
        "agent_instruction": str(parsed.get("agent_instruction") or "Review again using recovered context."),
        "context_package": parsed.get("context_package") if isinstance(parsed.get("context_package"), dict) else context,
    }


def retrieve_file_context_for_task(task: dict, input_root: Path) -> dict:
    """鐪熷疄璇诲彇璇佹嵁鏂囦欢锛屾浛浠ｅ師 call_context_recovery_llm 鐨勫够瑙夋绱€?"""
    row = task.get("source_row", {})
    evidence_refs = row.get("evidence_refs", [])

    file_snippets = []
    files_read: list[str] = []

    for ref in evidence_refs[:6]:
        rel_path = ref.get("rel_path", "")
        line_no = int(ref.get("line") or ref.get("line_no") or 0)
        if not rel_path:
            continue
        content = nearby_context(input_root, rel_path, line_no, radius=25)
        if not content:
            continue
        file_snippets.append(
            {
                "rel_path": rel_path,
                "line_no": line_no,
                "content": content[:3000],
                "source_text": (ref.get("actual_text") or ref.get("source_text", ""))[:300],
            }
        )
        if rel_path not in files_read:
            files_read.append(rel_path)

    summary = f"鐪熷疄璇诲彇 {len(files_read)} 涓瘉鎹枃浠讹紝{len(file_snippets)} 涓墖娈?"
    return {
        "task_id": task["task_id"],
        "round": 1,
        "context_summary": summary,
        "evidence_gaps": [],
        "additional_search_queries": [],
        "agent_instruction": "璇峰畬鍏ㄥ熀浜庝笅鏂瑰凡璇诲彇鍒扮殑鐪熷疄鏂囦欢鍐呭杩涜瑁佸喅锛屼笉寰楁帹娴嬫垨鍑┖鐢熸垚浠讳綍鍐呭銆?",
        "context_package": {
            "same_item_evidence": file_snippets,
            "parameter_context": [],
            "page_context": [],
            "recovered_context": [],
            "files_read": files_read,
        },
    }


def call_context_recovery_llm(task: dict, context: dict, round_no: int, output_root: Path) -> dict:
    """宸插簾寮冿細鍘?LLM 骞昏妫€绱紝淇濈暀浠ラ槻澶栭儴寮曠敤銆傚疄闄呮祦绋嬫敼鐢?retrieve_file_context_for_task銆?"""
    raw_path = output_root / "11_llm_raw" / f"context_recovery_{task['task_id']}_round_{round_no:02d}.json"
    payload = {
        "agent": "Context Recovery Agent",
        "task": "涓轰竴涓?needs_more_context 椤硅ˉ鍏呭彲渚涘瀹?Agent 浣跨敤鐨勪笂涓嬫枃璇佹嵁鍖呫€傚繀椤荤湡瀹炲垎鏋愮己浠€涔堣瘉鎹紝涓嶈鐩存帴瑁佸喅闂鐪熷亣銆?",
        "round": round_no,
        "round_strategy": context_recovery_round_strategy(round_no),
        "source_task": {k: v for k, v in task.items() if k != "source_row"},
        "current_context": context,
        "required_schema": {
            "context_summary": "涓枃鎬荤粨鏈疆琛ュ埌浜嗗摢浜涜瘉鎹€佷粛缂轰粈涔?",
            "evidence_gaps": ["浠嶇己澶辩殑涓婁笅鏂囨垨璇佹嵁"],
            "additional_search_queries": ["涓嬩竴杞簲妫€绱㈢殑鍏抽敭璇嶆垨鏂囦欢"],
            "agent_instruction": "缁欏鏌ュ瓙 Agent 鐨勫瀹℃寚浠?",
            "context_package": {
                "same_item_evidence": [],
                "parameter_context": [],
                "page_context": [],
                "recovered_context": [],
            },
        },
    }
    parsed = llm_json_call(
        raw_path,
        "浣犳槸鍖荤枟鍣ㄦ DHF/DMR 涓€鑷存€у鏌ョ郴缁熶腑鐨?Context Recovery Agent銆傚彧杈撳嚭涓ユ牸 JSON锛屼笉瑕?Markdown銆?",
        payload,
        max_tokens=5000,
    )
    return normalize_context_recovery_llm(parsed, task, context, round_no)


def normalize_context_orchestrator_llm(parsed: dict, task: dict, recovery: dict, round_no: int) -> dict:
    assigned_agent = str(parsed.get("assigned_agent") or task.get("target_agent") or "Domain Review Agent")
    return {
        "task_id": task["task_id"],
        "round": round_no,
        "assigned_agent": assigned_agent,
        "review_focus": str(parsed.get("review_focus") or "Decide whether the recovered context supports a real issue."),
        "agent_input": parsed.get("agent_input") if isinstance(parsed.get("agent_input"), dict) else recovery,
    }


def call_context_orchestrator_llm(task: dict, recovery: dict, round_no: int, output_root: Path) -> dict:
    raw_path = output_root / "11_llm_raw" / f"context_orchestrator_{task['task_id']}_round_{round_no:02d}.json"
    payload = {
        "agent": "Context Recovery Orchestrator",
        "task": "鏍规嵁琛ュ厖璇佹嵁鍖咃紝鎶婁笉纭畾椤归噸鏂板垎娲剧粰鏈€鍚堥€傜殑瀹℃煡瀛?Agent銆備笉瑕佽嚜宸辫鍐崇湡鍋囥€?",
        "round": round_no,
        "source_task": {k: v for k, v in task.items() if k != "source_row"},
        "context_recovery_output": recovery,
        "available_agents": [
            "Product Identity Agent",
            "Regulatory Agent",
            "Hardware Agent",
            "Software Agent",
            "Risk Traceability Agent",
            "V&V Agent",
            "DMR/SOP Agent",
            "Document Control Agent",
        ],
        "required_schema": {
            "assigned_agent": "涓婅堪 available_agents 涔嬩竴",
            "review_focus": "澶嶅閲嶇偣",
            "agent_input": {
                "claim": "鍘熼棶棰樻弿杩?",
                "context_summary": "琛ヨ瘉涓婁笅鏂囨憳瑕?",
                "evidence": [],
                "decision_values": ["confirm", "dismiss", "needs_more_context"],
            },
        },
    }
    parsed = llm_json_call(
        raw_path,
        "浣犳槸鍖荤枟鍣ㄦ DHF/DMR 澶氭櫤鑳戒綋绯荤粺鐨?Orchestrator銆傚彧杈撳嚭涓ユ牸 JSON锛屼笉瑕?Markdown銆?",
        payload,
        max_tokens=3000,
    )
    return normalize_context_orchestrator_llm(parsed, task, recovery, round_no)


def normalize_context_review_agent_llm(parsed: dict, task: dict, assignment: dict, round_no: int) -> dict:
    allowed = {"confirm", "dismiss", "needs_more_context"}
    decision = str(parsed.get("decision") or "needs_more_context")
    if decision not in allowed:
        decision = "needs_more_context"
    severity = str(parsed.get("severity") or task.get("severity", "P2"))
    if severity not in {"P0", "P1", "P2", "P3"}:
        severity = task.get("severity", "P2")
    return {
        "task_id": task["task_id"],
        "round": round_no,
        "agent": str(parsed.get("agent") or assignment.get("assigned_agent") or task.get("target_agent") or "Domain Review Agent"),
        "decision": decision,
        "severity": severity,
        "error_type": str(parsed.get("error_type") or task.get("context_need_type") or "context_recovery_review"),
        "claim": str(parsed.get("claim") or task.get("claim") or ""),
        "reason": str(parsed.get("reason") or "Agent did not provide a clear reason; keep needs_more_context."),
    }


def call_context_review_agent_llm(task: dict, assignment: dict, recovery: dict, round_no: int, output_root: Path, is_final_round: bool = False) -> dict:
    raw_path = output_root / "11_llm_raw" / f"context_review_agent_{task['task_id']}_round_{round_no:02d}.json"
    if is_final_round:
        decision_values = ["confirm", "dismiss"]
        decision_rules = [
            "confirm: direct evidence shows a real issue in controlled in-scope DHF/DMR documents.",
            "dismiss: evidence shows false positive, historical/auxiliary scope, reasonable reference, or insufficient proof.",
            "Final round must decide confirm or dismiss; do not return needs_more_context.",
            "Numeric inconsistency can be confirmed only when values have the same semantic role and controlled scope.",
        ]
        schema_decision = "confirm/dismiss"
        schema_reason = "decision reason based only on recovered evidence"
    else:
        decision_values = ["confirm", "dismiss", "needs_more_context"]
        decision_rules = [
            "confirm: recovered evidence is enough to prove a real controlled-document issue.",
            "dismiss: recovered evidence shows a false positive or insufficient proof.",
            "needs_more_context: recovered evidence is still missing a specific key context.",
            "Numeric inconsistency can be confirmed only when values have the same semantic role and controlled scope.",
        ]
        schema_decision = "confirm/dismiss/needs_more_context"
        schema_reason = "decision reason; for needs_more_context, state the missing context"
    payload = {
        "agent": assignment.get("assigned_agent", task.get("target_agent", "Domain Review Agent")),
        "task": "Review the uncertain item again using the recovered context package.",
        "round": round_no,
        "source_task": {k: v for k, v in task.items() if k != "source_row"},
        "orchestrator_assignment": assignment,
        "context_recovery_output": recovery,
        "decision_values": decision_values,
        "decision_rules": decision_rules,
        "required_schema": {
            "agent": "string",
            "decision": schema_decision,
            "severity": "P0/P1/P2/P3",
            "error_type": "snake_case",
            "claim": "reviewable conclusion",
            "reason": schema_reason,
        },
    }
    parsed = llm_json_call(
        raw_path,
        "You are a DHF/DMR domain review agent. Return strict JSON only, no Markdown.",
        payload,
        max_tokens=3500,
    )
    return normalize_context_review_agent_llm(parsed, task, assignment, round_no)


def context_llm_failure(stage: str, task: dict, round_no: int, error: Exception, context: dict | None = None) -> dict:
    reason = f"{stage} 绗?{round_no} 杞?LLM 杈撳嚭涓嶅彲瑙ｆ瀽鎴栬皟鐢ㄥけ璐ワ細{type(error).__name__}: {error}"
    if stage == "context_recovery":
        return {
            "task_id": task["task_id"],
            "round": round_no,
            "context_summary": reason,
            "evidence_gaps": [reason],
            "additional_search_queries": [],
            "agent_instruction": "鏈疆琛ヨ瘉杈撳嚭涓嶅彲瑙ｆ瀽锛岀户缁笅涓€杞ˉ璇侊紱鑻ヨ繛缁け璐ュ垯杞汉宸ュ鏍搞€?",
            "context_package": context or {},
            "error_type": "llm_parse_or_call_failed",
            "error_stage": stage,
            "reason": reason,
        }
    if stage == "orchestrator":
        return {
            "task_id": task["task_id"],
            "round": round_no,
            "assigned_agent": task.get("target_agent", "Domain Review Agent"),
            "review_focus": "Orchestrator 杈撳嚭涓嶅彲瑙ｆ瀽锛屼繚瀹堜氦鍥炲師鐩爣 Agent 缁х画澶嶅銆?",
            "agent_input": {"error_type": "llm_parse_or_call_failed", "reason": reason},
            "error_type": "llm_parse_or_call_failed",
            "error_stage": stage,
            "reason": reason,
        }
    return {
        "task_id": task["task_id"],
        "round": round_no,
        "agent": task.get("target_agent", "Domain Review Agent"),
        "decision": "needs_more_context",
        "severity": task.get("severity", "P2"),
        "error_type": "llm_parse_or_call_failed",
        "claim": task.get("claim", ""),
        "reason": reason,
        "error_stage": stage,
    }


def run_context_recovery_loop(
    task: dict,
    initial_context: dict,
    output_root: Path,
    input_root: Path | None = None,
    max_rounds: int = CONTEXT_RECOVERY_MAX_ROUNDS,
) -> dict:
    max_rounds = max(1, int(max_rounds or CONTEXT_RECOVERY_MAX_ROUNDS))
    current_context = dict(initial_context)
    if input_root is not None:
        file_recovery = retrieve_file_context_for_task(task, input_root)
        file_context = file_recovery.get("context_package", {})
        current_context = {
            **current_context,
            "same_item_evidence": current_context.get("same_item_evidence", []) + file_context.get("same_item_evidence", []),
            "parameter_context": current_context.get("parameter_context", []) + file_context.get("parameter_context", []),
            "page_context": current_context.get("page_context", []) + file_context.get("page_context", []),
            "files_read": file_context.get("files_read", []),
        }

    rounds: list[dict] = []
    final_status = "human_review"
    final_reason = ""
    final_review: dict = {}
    last_recovery_error: dict | None = None

    for round_no in range(1, max_rounds + 1):
        round_context = {**current_context, "round_strategy": context_recovery_round_strategy(round_no)}
        try:
            recovery = call_context_recovery_llm(task, round_context, round_no, output_root)
        except Exception as exc:
            recovery = context_llm_failure("context_recovery", task, round_no, exc, round_context)
        recovery["round_strategy"] = context_recovery_round_strategy(round_no)
        if recovery.get("error_type") == "llm_parse_or_call_failed":
            last_recovery_error = recovery

        try:
            assignment = call_context_orchestrator_llm(task, recovery, round_no, output_root)
        except Exception as exc:
            assignment = context_llm_failure("orchestrator", task, round_no, exc)

        try:
            try:
                review = call_context_review_agent_llm(
                    task,
                    assignment,
                    recovery,
                    round_no,
                    output_root,
                    is_final_round=(round_no == max_rounds),
                )
            except TypeError as exc:
                if "is_final_round" not in str(exc):
                    raise
                review = call_context_review_agent_llm(task, assignment, recovery, round_no, output_root)
        except Exception as exc:
            review = context_llm_failure("review_agent", task, round_no, exc)

        rounds.append({"round": round_no, "context_recovery": recovery, "orchestrator": assignment, "review": review})
        final_review = review
        decision = review.get("decision", "needs_more_context")
        if decision in {"confirm", "dismiss"}:
            final_status = decision
            final_reason = review.get("reason", "")
            break

        recovered_context = recovery.get("context_package")
        if isinstance(recovered_context, dict):
            current_context = recovered_context

    if final_status not in {"confirm", "dismiss"}:
        final_status = "human_review"
        if last_recovery_error:
            final_review = {
                **final_review,
                "error_type": last_recovery_error.get("error_type"),
                "reason": last_recovery_error.get("reason", ""),
            }
            final_reason = last_recovery_error.get("reason", "")
        else:
            final_reason = f"Context Recovery reached {len(rounds)} round(s) without a confirm/dismiss decision. Last reason: {final_review.get('reason', '')}"

    final_context = current_context if isinstance(current_context, dict) else {}
    return {
        "task_id": task["task_id"],
        "gap_source": task["gap_source"],
        "source_id": task["source_id"],
        "target_agent": task["target_agent"],
        "context_need_type": task.get("context_need_type", ""),
        "final_status": final_status,
        "severity": final_review.get("severity", task.get("severity", "P2")),
        "claim": final_review.get("claim") or task.get("claim", ""),
        "reason": final_reason,
        "rounds_used": len(rounds),
        "max_rounds": max_rounds,
        "final_review_decision": final_review,
        "rounds": rounds,
        "context_counts": {
            "same_item_evidence": len(final_context.get("same_item_evidence", [])),
            "parameter_context": len(final_context.get("parameter_context", [])),
            "page_context": len(final_context.get("page_context", [])),
        },
    }

def context_recovery_node(state: FullAuditState) -> FullAuditState:
    output_root = Path(state["output_root"])
    input_root = Path(state["input_root"])
    tasks = build_context_recovery_tasks(state)
    packages = []
    results = []
    for task in tasks:
        context = collect_context_package(task, state)
        package = {k: v for k, v in task.items() if k != "source_row"}
        package["context_package"] = context
        package["max_rounds"] = CONTEXT_RECOVERY_MAX_ROUNDS
        package["round_strategies"] = [
            context_recovery_round_strategy(round_no)
            for round_no in range(1, CONTEXT_RECOVERY_MAX_ROUNDS + 1)
        ]
        packages.append(package)
        results.append(run_context_recovery_loop(task, context, output_root, input_root=input_root, max_rounds=CONTEXT_RECOVERY_MAX_ROUNDS))

    result_by_source = {row["source_id"]: row for row in results}
    semantic = []
    for row in state.get("semantic_findings", []):
        row = dict(row)
        result = result_by_source.get(row.get("finding_id", ""))
        if result and row.get("challenge_status") == "needs_more_context":
            mapped = {
                "confirm": "keep",
                "dismiss": "drop",
                "human_review": "human_review",
            }[result["final_status"]]
            row["challenge_status"] = mapped
            row["context_recovery_status"] = result["final_status"]
            row["context_recovery_reason"] = result["reason"]
            row["context_recovery_rounds_used"] = result.get("rounds_used", 0)
            row["context_recovery_agent"] = result.get("final_review_decision", {}).get("agent", result.get("target_agent", ""))
        semantic.append(row)

    semantic_recovery_status = Counter(
        row.get("final_status", "unknown") for row in results if row.get("gap_source") == "semantic"
    )
    recovery_status = Counter(row.get("final_status", "unknown") for row in results)
    context_recovery_summary = {
        "total": len(results),
        "max_rounds": CONTEXT_RECOVERY_MAX_ROUNDS,
        "rounds_executed": max((row.get("rounds_used", 0) for row in results), default=0),
        "by_final_status": dict(recovery_status),
        "semantic": dict(semantic_recovery_status),
    }

    write_json(output_root / "14_context_recovery" / "context_recovery_tasks.json", {"tasks": packages})
    write_jsonl(output_root / "14_context_recovery" / "context_recovery_results.jsonl", results)
    write_json(output_root / "14_context_recovery" / "context_recovery_loop_trace.json", {"results": results})
    write_jsonl(output_root / "14_context_recovery" / "semantic_after_context_recovery.jsonl", semantic)
    write_jsonl(output_root / "07_findings" / "semantic_findings_llm_challenged.jsonl", semantic)

    all_findings = semantic
    write_jsonl(output_root / "07_findings" / "candidate_findings_merged_full.jsonl", all_findings)

    return {
        **state,
        "context_recovery_tasks": tasks,
        "context_recovery_results": results,
        "context_recovery_summary": context_recovery_summary,
        "semantic_findings": semantic,
        "all_findings": all_findings,
    }


def esc(text: object) -> str:
    return str(text).replace("|", "\\|").replace("\n", " ")


def display_challenge_reason(row: dict) -> str:
    reason = str(row.get("challenge_reason") or "").strip()
    if len(reason) >= 40:
        return reason
    status = row.get("challenge_status")
    if status == "keep":
        return "Challenge Agent kept this finding because the evidence supports the claim."
    if status == "revise":
        return "Challenge Agent kept the core issue but revised severity or wording."
    if status == "drop":
        return "Challenge Agent dropped this finding because evidence was insufficient or it looked like a false positive."
    if status == "human_review":
        return "Context Recovery could not decide automatically; send to human review."
    return "Challenge Agent requires more context before a final decision."


SECOND_ROUND_HINTS = {
    "LLM-0001": "Retrieve the full source file and nearby model references.",
    "LLM-0010": "Retrieve revision history and document-control records.",
    "LLM-0012": "Search all occurrences of the referenced material number.",
    "LLM-0019": "Retrieve related software review records and alternate versions.",
    "LLM-0020": "Retrieve traceability, build, design, and test records.",
    "LLM-0025": "Retrieve full risk-management report and EMC-related risk entries.",
    "LLM-0030": "Retrieve design-review plan, verification plan, reports, and meeting records.",
}

def write_second_round_tasks(output_root: Path, semantic: list[dict], generated_at: str) -> None:
    rows = [row for row in semantic if row.get("challenge_status") in {"needs_more_context", "human_review"}]
    lines = [
        "# Second Round Context Tasks",
        "",
        f"> generated_at: {generated_at}",
        f"> unresolved_count: {len(rows)}",
        "",
        "## Tasks",
        "",
    ]
    for row in rows:
        hint = SECOND_ROUND_HINTS.get(row.get("finding_id"), "Retrieve upstream/downstream files, same-topic records, revision history, and controlled versions.")
        lines.extend(
            [
                f"### {row.get('finding_id')} {esc(row.get('claim'))}",
                "",
                f"- Agent: {esc(row.get('agent'))}",
                f"- Severity: `{row.get('severity')}`",
                f"- Type: `{esc(row.get('finding_type'))}`",
                f"- Suggested retrieval: {esc(hint)}",
                "- Current evidence:",
            ]
        )
        for ref in row.get("evidence_refs", [])[:3]:
            text = esc(ref.get("actual_text") or ref.get("source_text", ""))[:180]
            lines.append(f"  - `{esc(ref.get('rel_path'))}:{ref.get('line')}` {text}")
        lines.append("")
    (output_root / "08_reports" / "second_round_tasks.md").write_text("\n".join(lines), encoding="utf-8")

def build_result_count_summary(
    semantic_rows: list[dict],
    all_findings: list[dict],
) -> dict:
    semantic_status = Counter(row.get("challenge_status", "unknown") for row in semantic_rows)
    semantic_confirmed = semantic_status.get("keep", 0) + semantic_status.get("revise", 0)
    return {
        "semantic_total": len(semantic_rows),
        "semantic_keep": semantic_status.get("keep", 0),
        "semantic_revise": semantic_status.get("revise", 0),
        "semantic_confirmed_keep_revise": semantic_confirmed,
        "semantic_needs_more_context": semantic_status.get("needs_more_context", 0),
        "semantic_human_review": semantic_status.get("human_review", 0),
        "semantic_dropped": semantic_status.get("drop", 0),
        "semantic_challenge_status_counts": dict(semantic_status),
        "merged_findings_rows": len(all_findings),
        "current_confirmed_error_total": semantic_confirmed,
    }


def report_node(state: FullAuditState) -> FullAuditState:
    output_root = Path(state["output_root"])
    manifest = state["manifest"]
    semantic = state["semantic_findings"]
    all_findings = state["all_findings"]
    severity = Counter(row.get("severity", "unknown") for row in all_findings)
    by_agent = Counter(row.get("agent", "Unknown") for row in all_findings)
    evidence = Counter(row.get("evidence_status", "unknown") for row in all_findings)
    challenge = Counter(row.get("challenge_status", "unknown") for row in semantic)
    context_recovery_summary = state.get("context_recovery_summary", {})
    result_counts = build_result_count_summary(semantic, all_findings)
    challenge_reason_quality_flags = sum(1 for row in semantic if row.get("challenge_reason_quality_flag"))

    summary = {
        "run_mode": "full_langgraph_llm",
        "llm_provider": "GPT55 via OpenAI-compatible SDK",
        "manifest_docs": len(manifest),
        "primary_scope_docs": sum(1 for row in manifest if not row["excluded_from_primary_scope"]),
        "auxiliary_scope_docs": sum(1 for row in manifest if row["excluded_from_primary_scope"]),
        "page_index_sections": len(state["page_index"]),
        "parameter_instances": len(state["params"]),
        "relation_nodes": len(state["relation_nodes"]),
        "relation_edges": len(state["relation_edges"]),
        "evidence_tool_hits": len(state.get("evidence_tool_hits", [])),
        "agent_runs": len(state.get("agent_runs", [])),
        "orchestrator_route_plans": len(state.get("orchestrator_route_plans", [])),
        "candidate_discovery_results": len(state.get("candidate_discovery_results", [])),
        "mandatory_audit_matrix_items": len(state.get("mandatory_audit_matrix", [])),
        "llm_semantic_findings": len(semantic),
        "merged_findings": len(all_findings),
        "merged_findings_rows": result_counts["merged_findings_rows"],
        "semantic_keep": result_counts["semantic_keep"],
        "semantic_revise": result_counts["semantic_revise"],
        "semantic_confirmed_keep_revise": result_counts["semantic_confirmed_keep_revise"],
        "semantic_needs_more_context": result_counts["semantic_needs_more_context"],
        "semantic_human_review": result_counts["semantic_human_review"],
        "semantic_dropped": result_counts["semantic_dropped"],
        "context_recovery_total": context_recovery_summary.get("total", 0),
        "context_recovery_max_rounds": context_recovery_summary.get("max_rounds", CONTEXT_RECOVERY_MAX_ROUNDS),
        "context_recovery_rounds_executed": context_recovery_summary.get("rounds_executed", 0),
        "context_recovery_confirm": context_recovery_summary.get("by_final_status", {}).get("confirm", 0),
        "context_recovery_dismiss": context_recovery_summary.get("by_final_status", {}).get("dismiss", 0),
        "context_recovery_human_review": context_recovery_summary.get("by_final_status", {}).get("human_review", 0),
        "current_confirmed_error_total": result_counts["current_confirmed_error_total"],
        "challenge_reason_quality_flags": challenge_reason_quality_flags,
        "evidence_verified": evidence.get("verified", 0),
        "generated_at": datetime.now().isoformat(timespec="seconds"),
    }
    write_json(output_root / "08_reports" / "run_summary_full_langgraph.json", summary)
    write_jsonl(
        output_root / "12_challenge" / "adjudication_log_template.jsonl",
        (
            {
                "finding_id": row["finding_id"],
                "human_decision": "",
                "human_comment": "",
                "owner": "",
                "due_date": "",
            }
            for row in all_findings
        ),
    )

    lines = [
        "# PT9L Full Markdown Consistency Audit Report",
        "",
        f"> generated_at: {summary['generated_at']}",
        "> Candidate hypotheses are proposed by agents. Evidence tools only provide retrievable context.",
        "",
        "## Execution Summary",
        "",
        f"- Markdown docs: {summary['manifest_docs']}",
        f"- Primary-scope docs: {summary['primary_scope_docs']}",
        f"- Auxiliary/history docs: {summary['auxiliary_scope_docs']}",
        f"- PageIndex sections: {summary['page_index_sections']}",
        f"- Parameter instances: {summary['parameter_instances']}",
        f"- Relation nodes/edges: {summary['relation_nodes']} / {summary['relation_edges']}",
        f"- Evidence Tool hits: {summary['evidence_tool_hits']}",
        f"- Agent runs: {summary['agent_runs']}",
        f"- Orchestrator route plans: {summary['orchestrator_route_plans']}",
        f"- Candidate Discovery results: {summary['candidate_discovery_results']}",
        f"- LLM semantic findings: {summary['llm_semantic_findings']}",
        f"- Challenge keep / revise / needs_more_context / human_review / drop: {summary['semantic_keep']} / {summary['semantic_revise']} / {summary['semantic_needs_more_context']} / {summary['semantic_human_review']} / {summary['semantic_dropped']}",
        f"- Context Recovery total / confirm / dismiss / human_review: {summary['context_recovery_total']} / {summary['context_recovery_confirm']} / {summary['context_recovery_dismiss']} / {summary['context_recovery_human_review']}",
        f"- Merged finding rows: {summary['merged_findings_rows']}",
        f"- Current confirmed error total: {summary['current_confirmed_error_total']} (semantic keep/revise)",
        f"- Evidence verified: {summary['evidence_verified']}",
        "",
        "## LangGraph Nodes",
        "",
        "`bootstrap -> scout_agent -> orchestrator(dynamic dispatch loop) -> evidence_gate -> challenge_agent -> context_recovery -> report`",
        "",
        "## Severity Counts",
        "",
        "| Severity | Count |",
        "|---|---:|",
    ]
    for key in ["P0", "P1", "P2", "P3", "unknown"]:
        if severity.get(key, 0):
            lines.append(f"| {key} | {severity[key]} |")

    lines.extend(["", "## Agent Counts", "", "| Agent | Count |", "|---|---:|"])
    for agent, count in by_agent.most_common():
        lines.append(f"| {esc(agent)} | {count} |")

    lines.extend(["", "## Challenge Counts", "", "| Status | Count |", "|---|---:|"])
    for status, count in challenge.most_common():
        lines.append(f"| {esc(status)} | {count} |")

    lines.extend(["", "## Semantic Findings", "", "| ID | Severity | Agent | Type | Challenge | Claim | Evidence |", "|---|---|---|---|---|---|---|"])
    for row in semantic:
        refs = "<br>".join(
            f"`{esc(ref.get('rel_path'))}:{ref.get('line')}` {esc(ref.get('actual_text') or ref.get('source_text'))[:160]}"
            for ref in row.get("evidence_refs", [])[:3]
        )
        lines.append(
            f"| {row['finding_id']} | {row.get('severity')} | {esc(row.get('agent'))} | {esc(row.get('finding_type'))} | {esc(row.get('challenge_status'))} | {esc(row.get('claim'))} | {refs} |"
        )

    lines.extend(["", "## Boundaries", ""])
    lines.append("- This report is an audit candidate set, not a final quality conclusion.")
    lines.append("- `verified` means evidence is traceable to Markdown text, not that a human accepted the issue.")
    lines.append("- Evidence Tool hits do not directly become candidates or errors.")

    report_path = output_root / "08_reports" / "PT9L_full_audit_report_langgraph.md"
    report_path.write_text("\n".join(lines), encoding="utf-8")

    high_priority = [
        row
        for row in semantic
        if row.get("severity") == "P1" and row.get("challenge_status") in {"keep", "revise"}
    ]
    high_lines = [
        "# PT9L High Priority Semantic Findings",
        "",
        f"> generated_at: {summary['generated_at']}",
        "",
        "## Summary",
        "",
        f"- High priority findings: {len(high_priority)}",
        f"- keep: {sum(1 for row in high_priority if row.get('challenge_status') == 'keep')}",
        f"- revise: {sum(1 for row in high_priority if row.get('challenge_status') == 'revise')}",
        "",
        "## Findings",
        "",
    ]
    for idx, row in enumerate(high_priority, start=1):
        high_lines.extend(
            [
                f"### {idx}. {esc(row.get('claim'))}",
                "",
                f"- Finding ID: `{row.get('finding_id')}`",
                f"- Agent: {esc(row.get('agent'))}",
                f"- Type: `{esc(row.get('finding_type'))}`",
                f"- Challenge: `{esc(row.get('challenge_status'))}`",
                f"- Reason: {esc(display_challenge_reason(row))}",
                "- Evidence:",
            ]
        )
        for ref in row.get("evidence_refs", [])[:3]:
            text = esc(ref.get("actual_text") or ref.get("source_text", ""))[:220]
            high_lines.append(f"  - `{esc(ref.get('rel_path'))}:{ref.get('line')}` {text}")
        high_lines.append("")
    (output_root / "08_reports" / "PT9L_high_priority_semantic_findings.md").write_text(
        "\n".join(high_lines),
        encoding="utf-8",
    )
    write_second_round_tasks(output_root, semantic, summary["generated_at"])
    return {**state, "summary": summary}

def build_graph():
    graph = StateGraph(FullAuditState)
    graph.add_node("bootstrap", bootstrap_node)
    graph.add_node("scout_agent", scout_node)
    graph.add_node("orchestrator", orchestrator_node)
    graph.add_node("evidence_gate", evidence_gate_node)
    graph.add_node("challenge_agent", challenge_node)
    graph.add_node("context_recovery", context_recovery_node)
    graph.add_node("report", report_node)

    graph.add_edge(START, "bootstrap")
    graph.add_edge("bootstrap", "scout_agent")
    graph.add_edge("scout_agent", "orchestrator")
    graph.add_edge("orchestrator", "evidence_gate")
    graph.add_edge("evidence_gate", "challenge_agent")
    graph.add_edge("challenge_agent", "context_recovery")
    graph.add_edge("context_recovery", "report")
    graph.add_edge("report", END)
    return graph.compile()


def run(input_root: Path, output_root: Path) -> dict:
    app = build_graph()
    final_state = app.invoke(
        {"input_root": str(input_root), "output_root": str(output_root)},
        config={"max_concurrency": 2},
    )
    return final_state["summary"]


def load_context_recovery_resume_state(input_root: Path, output_root: Path) -> FullAuditState:
    semantic = read_jsonl(output_root / "07_findings" / "semantic_findings_llm_challenged.jsonl")
    if not semantic:
        raise FileNotFoundError(
            "Cannot resume Context Recovery: missing or empty "
            f"{output_root / '07_findings' / 'semantic_findings_llm_challenged.jsonl'}"
        )
    route_plans = read_json(output_root / "10_task_packages" / "orchestrator_route_plans.json", {"route_plans": []})
    mandatory_matrix = read_json(output_root / "10_task_packages" / "mandatory_audit_matrix.json", {"matrix": []})
    return {
        "input_root": str(input_root),
        "output_root": str(output_root),
        "manifest": read_jsonl(output_root / "00_manifest" / "full_manifest.jsonl"),
        "readiness": read_jsonl(output_root / "00_manifest" / "document_readiness.jsonl"),
        "page_index": read_jsonl(output_root / "01_page_index" / "page_index.jsonl"),
        "params": read_jsonl(output_root / "03_ssot_parameters" / "parameter_instances.jsonl"),
        "parameter_alignment_evidence_rows": read_jsonl(output_root / "03_ssot_parameters" / "parameter_alignment_evidence_rows.jsonl"),
        "parameter_conflict_evidence_rows": read_jsonl(output_root / "03_ssot_parameters" / "parameter_conflict_evidence_rows.jsonl"),
        "relation_nodes": read_jsonl(output_root / "04_relation_index" / "nodes.jsonl"),
        "relation_edges": read_jsonl(output_root / "04_relation_index" / "edges.jsonl"),
        "residue_rows": read_jsonl(output_root / "06_evidence_tools" / "residue_hits.jsonl"),
        "evidence_tool_hits": read_jsonl(output_root / "06_evidence_tools" / "evidence_tool_hits.jsonl"),
        "agent_runs": read_jsonl(output_root / "05_agent_notes" / "agent_runs.jsonl"),
        "orchestrator_route_plans": route_plans.get("route_plans", []) if isinstance(route_plans, dict) else [],
        "candidate_discovery_results": read_jsonl(output_root / "07_findings" / "candidate_discovery_results.jsonl"),
        "mandatory_audit_matrix": mandatory_matrix.get("matrix", []) if isinstance(mandatory_matrix, dict) else [],
        "semantic_findings": semantic,
        "all_findings": semantic,
        "evidence_catalog": {},
        "scout_output": {},
        "project_profile": read_json(output_root / "02_blackboard" / "project_profile.json", {}),
    }


def run_context_recovery_resume(input_root: Path, output_root: Path) -> dict:
    state = load_context_recovery_resume_state(input_root, output_root)
    recovered_state = context_recovery_node(state)
    final_state = report_node(recovered_state)
    return final_state["summary"]


def main() -> None:
    parser = argparse.ArgumentParser(description="Run full PT9L Markdown audit with LangGraph and GPT55 agents.")
    parser.add_argument("--input", default=str(INPUT_ROOT_DEFAULT), help="PT9L markdown output root")
    parser.add_argument("--output", default=str(OUTPUT_ROOT_DEFAULT), help="Full audit output root")
    parser.add_argument(
        "--resume-context-recovery",
        action="store_true",
        help="Resume from existing challenged findings and raw Context Recovery files, then generate reports.",
    )
    args = parser.parse_args()
    if args.resume_context_recovery:
        summary = run_context_recovery_resume(Path(args.input), Path(args.output))
    else:
        summary = run(Path(args.input), Path(args.output))
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    sys.exit(main())
