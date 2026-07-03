# -*- coding: utf-8 -*-
from __future__ import annotations

import csv
import datetime as dt
import re
from collections import Counter
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parent
CONVERTED_MD = ROOT / "converted_md"
STAGE_DIR = ROOT / "stage_checklist"
GENERATED_DIR = ROOT / "generated_docs"


def u(s: str) -> str:
    return s.encode("ascii").decode("unicode_escape")


CN = {
    "forehead": u("\\u989d\\u6e29"),
    "thermometer": u("\\u4f53\\u6e29\\u8ba1"),
    "infrared": u("\\u7ea2\\u5916"),
    "us": u("\\u7f8e\\u56fd"),
    "eu": u("\\u6b27\\u76df"),
    "china": u("\\u4e2d\\u56fd"),
    "domestic": u("\\u56fd\\u5185"),
    "design": u("\\u8bbe\\u8ba1"),
    "input": u("\\u8f93\\u5165"),
    "output": u("\\u8f93\\u51fa"),
    "risk": u("\\u98ce\\u9669"),
    "verification": u("\\u9a8c\\u8bc1"),
    "validation": u("\\u786e\\u8ba4"),
    "test": u("\\u6d4b\\u8bd5"),
    "report": u("\\u62a5\\u544a"),
    "drawing": u("\\u56fe\\u7eb8"),
    "structure": u("\\u7ed3\\u6784"),
    "hardware": u("\\u786c\\u4ef6"),
    "software": u("\\u8f6f\\u4ef6"),
    "process": u("\\u5de5\\u827a"),
    "sop": u("\\u4f5c\\u4e1a\\u6307\\u5bfc"),
    "inspection": u("\\u68c0\\u9a8c"),
    "production": u("\\u751f\\u4ea7"),
    "packaging": u("\\u5305\\u88c5"),
    "label": u("\\u6807\\u7b7e"),
    "ifu": u("\\u8bf4\\u660e\\u4e66"),
    "regulation": u("\\u6cd5\\u89c4"),
    "registration": u("\\u6ce8\\u518c"),
    "standard": u("\\u6807\\u51c6"),
    "accuracy": u("\\u7cbe\\u5ea6"),
    "biocompatibility": u("\\u751f\\u7269\\u76f8\\u5bb9"),
    "service_life": u("\\u5bff\\u547d"),
    "complaint": u("\\u6295\\u8bc9"),
    "review": u("\\u8bc4\\u4ef7"),
    "after_sales": u("\\u552e\\u540e"),
    "fixture": u("\\u5de5\\u88c5"),
    "jig": u("\\u6cbb\\u5177"),
}


BASELINE = {
    "project_id": "PT9L",
    "product_name": "Infrared Forehead Thermometer",
    "product_name_cn": CN["infrared"] + CN["forehead"] + CN["thermometer"],
    "product_type": "infrared forehead thermometer",
    "model_or_series": "PT9L",
    "target_market": "United States",
    "regulatory_region": "US",
    "regulatory_path": "FDA medical device pathway - exact route to be confirmed",
    "risk_class": "To be confirmed from regulatory strategy",
    "intended_use": "Intermittent measurement of human body temperature from the forehead skin surface",
    "intended_user": "Lay users and healthcare professionals - to be confirmed from IFU/design input",
    "intended_patient_population": "People of all ages - to be confirmed from IFU/design input",
    "use_environment": "Home healthcare and healthcare environments - to be confirmed",
    "applicable_general_standards": [
        "IEC 60601-1",
        "IEC 60601-1-2",
        "IEC 60601-1-11",
        "IEC 62304",
        "IEC 62366-1",
        "ISO 14971",
        "ISO 10993-1",
    ],
    "applicable_product_specific_standards": [
        "ISO 80601-2-56",
        "ASTM E1965 - if applicable to US infrared thermometer route",
    ],
    "key_performance_requirements": [
        "temperature measurement accuracy",
        "measurement range",
        "clinical accuracy",
        "service life",
        "EMC",
        "electrical safety",
        "software validation",
        "usability",
        "biocompatibility for forehead skin contact",
    ],
    "software_applicable": "yes",
    "electrical_safety_applicable": "yes",
    "emc_applicable": "yes",
    "owner_note": "First-pass baseline inferred from project context. Confirm market, route, risk class, intended use, and standards before final compliance review.",
}


STAGES = [
    ("01_initiation", "Initiation", ["initiation", "customer need", CN["customer"] if "customer" in CN else "", u("\\u7acb\\u9879"), u("\\u5ba2\\u6237\\u9700\\u6c42")]),
    ("02_regulatory_strategy", "Regulatory Strategy", ["FDA", "510", "MDR", "EU MDR", CN["regulation"], CN["registration"], CN["us"], u("\\u6807\\u51c6\\u6e05\\u5355")]),
    ("03_design_input", "Design Input", ["design input", CN["design"] + CN["input"], u("\\u9700\\u6c42"), u("\\u8d28\\u91cf\\u7b56\\u5212")]),
    ("04_risk_management", "Risk Management", ["risk", "FMEA", "hazard", CN["risk"]]),
    ("05_design_output", "Design Output", ["design output", CN["design"] + CN["output"], CN["drawing"], "BOM", "PCB", CN["structure"], CN["hardware"], CN["software"]]),
    ("06_verification_validation", "Verification and Validation", ["verification", "validation", "test", "report", CN["verification"], CN["validation"], CN["test"], CN["report"], "EMC", "80601", "10993"]),
    ("07_dmr_manufacturing", "DMR Manufacturing", ["DMR", "SOP", CN["sop"], CN["process"], CN["production"], CN["inspection"], CN["packaging"], CN["label"]]),
    ("08_registration_td", "Registration Technical Documentation", ["technical documentation", "GSPR", "submission", CN["registration"], u("\\u6280\\u672f\\u6587\\u6863")]),
    ("09_post_market_feedback", "Post-market Feedback", ["PMS", "PMCF", "PSUR", CN["complaint"], CN["review"], CN["after_sales"]]),
    ("10_patent_engineering", "Patent and Engineering Materials", ["patent", CN["fixture"], CN["jig"], CN["structure"], u("\\u4e13\\u5229")]),
]


CATEGORIES = [
    ("Regulatory/Registration", ["FDA", "MDR", "EU MDR", "510", CN["regulation"], CN["registration"], u("\\u6807\\u51c6\\u6e05\\u5355")]),
    ("Design Input", ["design input", CN["design"] + CN["input"], u("\\u9700\\u6c42")]),
    ("Risk Management", ["risk", "FMEA", "hazard", CN["risk"]]),
    ("Verification/Validation", ["verification", "validation", "test", "report", CN["verification"], CN["validation"], CN["test"], CN["report"], "EMC", "80601"]),
    ("BOM", ["BOM", u("\\u7ec4\\u4ef6\\u6e05\\u5355"), u("\\u7269\\u6599")]),
    ("SOP/Process", ["SOP", CN["sop"], CN["process"], u("\\u64cd\\u4f5c")]),
    ("Inspection", [CN["inspection"], u("\\u68c0\\u67e5")]),
    ("Design Output", ["design output", CN["design"] + CN["output"], CN["drawing"], "PCB", "BOM", CN["structure"], CN["hardware"]]),
    ("Packaging/Labeling", [CN["packaging"], CN["label"], "IFU", CN["ifu"], "label"]),
    ("Code/Software", ["source code", "firmware", CN["software"], u("\\u7a0b\\u5e8f"), u("\\u7f16\\u7801")]),
    ("Drawing/Structure/Electronics", [CN["drawing"], CN["structure"], "PCB", "DWG", "DXF", "STP", "STEP"]),
    ("Post-market Feedback", ["PMS", "PMCF", "PSUR", CN["complaint"], CN["review"], CN["after_sales"]]),
]


STANDARD_PATTERNS = [
    r"IEC\s*60601-1-11",
    r"IEC\s*60601-1-2",
    r"IEC\s*60601-1",
    r"IEC\s*62304",
    r"IEC\s*62366-1",
    r"ISO\s*14971",
    r"ISO\s*10993(?:-\d+)?",
    r"ISO\s*80601-2-56",
    r"ASTM\s*E1965",
    r"MDR",
    r"FDA",
    r"510\(k\)|510k",
]


def read_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_csv(path: Path, rows: list[dict[str, Any]], fields: list[str]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def read_text(path: Path, limit: int = 25000) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="ignore")[:limit]
    except Exception:
        return ""


def rel(path: str | Path) -> str:
    try:
        return str(Path(path).resolve().relative_to(ROOT))
    except Exception:
        return str(path)


def detect_first(blob: str, choices: list[tuple[str, str, list[str]]]) -> tuple[str, str]:
    low = blob.lower()
    for code, label, needles in choices:
        if any(n and n.lower() in low for n in needles):
            return code, label
    return "unknown", "Unclassified"


def detect_category(blob: str) -> str:
    low = blob.lower()
    for label, needles in CATEGORIES:
        if any(n.lower() in low for n in needles):
            return label
    return "Other"


def detect_dhf_dmr(category: str, blob: str) -> str:
    low = blob.lower()
    if category in {"BOM", "SOP/Process", "Inspection", "Packaging/Labeling"} or "03_mfg" in low:
        return "DMR"
    if category in {"Design Input", "Design Output", "Risk Management", "Verification/Validation", "Regulatory/Registration"} or "02_rnd" in low or "dhf" in low:
        return "DHF"
    return "unknown"


def detect_product(blob: str) -> str:
    low = blob.lower()
    if "pt9l" in low:
        return "PT9L"
    if "forehead thermometer" in low or CN["forehead"] in blob or (CN["infrared"] in blob and CN["thermometer"] in blob):
        return "Infrared Forehead Thermometer"
    if "thermometer" in low or CN["thermometer"] in blob:
        return "Thermometer"
    return "not_detected"


def detect_market(blob: str) -> str:
    low = blob.lower()
    markets = []
    if any(x in low for x in ["united states", "usa", "u.s.", "fda", "510(k)"]) or CN["us"] in blob:
        markets.append("United States")
    if any(x in low for x in ["europe", "eu ", "mdr", "ce"]) or CN["eu"] in blob:
        markets.append("EU")
    if any(x in low for x in ["china", "nmpa"]) or CN["china"] in blob or CN["domestic"] in blob:
        markets.append("China")
    return "; ".join(dict.fromkeys(markets)) or "not_detected"


def detect_standards(blob: str) -> list[str]:
    out = []
    for pat in STANDARD_PATTERNS:
        for m in re.findall(pat, blob, flags=re.I):
            value = m if isinstance(m, str) else "".join(m)
            value = re.sub(r"\s+", " ", value).strip().upper()
            if value:
                out.append(value)
    return sorted(dict.fromkeys(out))


def detect_requirements(blob: str) -> list[str]:
    low = blob.lower()
    checks = [
        ("accuracy", ["accuracy", CN["accuracy"], u("\\u8bef\\u5dee")]),
        ("biocompatibility", ["biocompatibility", CN["biocompatibility"], "10993"]),
        ("software", ["software", CN["software"], "62304", "firmware"]),
        ("electrical_safety", ["60601-1", "electrical safety", u("\\u5b89\\u89c4")]),
        ("emc", ["60601-1-2", "emc", u("\\u7535\\u78c1\\u517c\\u5bb9")]),
        ("usability", ["62366", "usability", u("\\u53ef\\u7528\\u6027")]),
        ("service_life", ["service life", CN["service_life"], u("\\u8001\\u5316")]),
        ("packaging_labeling", ["label", "ifu", CN["packaging"], CN["label"], CN["ifu"]]),
        ("risk", ["risk", CN["risk"], "fmea", "14971"]),
        ("manufacturing", ["sop", CN["production"], CN["process"], CN["inspection"]]),
    ]
    return [name for name, needles in checks if any(n.lower() in low for n in needles)]


def baseline_check(category: str, stage: str, product: str, market: str, standards: list[str], requirements: list[str]) -> tuple[str, str]:
    issues = []
    if product == "not_detected":
        issues.append("product/model not detected")
    if category in {"Regulatory/Registration", "Design Input", "Verification/Validation", "Packaging/Labeling"} or stage in {"02_regulatory_strategy", "03_design_input", "06_verification_validation", "08_registration_td"}:
        if market == "not_detected":
            issues.append("target market not detected for market-sensitive file")
        elif "United States" not in market:
            issues.append("detected market does not include United States baseline")
    if category in {"Regulatory/Registration", "Design Input", "Verification/Validation"} and requirements:
        if not any("80601-2-56" in s or "E1965" in s for s in standards):
            issues.append("product-specific thermometer standard not detected")
    if not issues:
        return "aligned_or_not_applicable", ""
    if len(issues) <= 2:
        return "needs_review", "; ".join(issues)
    return "likely_mismatch", "; ".join(issues)


def extract_refs(text: str) -> str:
    refs = []
    patterns = [r"Attachment\s+\d+(?:\.\d+)*", r"IEC\s*[\d\-]+", r"ISO\s*[\d\-]+", r"ASTM\s*E\d+", r"PT9L[-\w]*"]
    for pat in patterns:
        refs.extend(re.findall(pat, text, flags=re.I))
    return "; ".join(sorted(dict.fromkeys(refs))[:25])


def write_baseline() -> None:
    lines = ["# PT9L project baseline profile", f"created_at: {dt.datetime.now().replace(microsecond=0).isoformat(sep=' ')}"]
    for key, value in BASELINE.items():
        if isinstance(value, list):
            lines.append(f"{key}:")
            lines.extend([f"  - {item}" for item in value])
        else:
            lines.append(f"{key}: {value}")
    (ROOT / "baseline_project_profile.yaml").write_text("\n".join(lines) + "\n", encoding="utf-8")


def build_inventory() -> list[dict[str, Any]]:
    conversion = read_csv(ROOT / "conversion_report.csv")
    quality = read_csv(ROOT / "conversion_quality_report.csv")
    word_recovery = read_csv(ROOT / "markitdown_word_recovery_report.csv")
    q_by_md = {r.get("md_file_path", ""): r for r in quality}
    rows = []
    seen = set()
    for r in conversion:
        candidates = [r.get("output_md_path", "")]
        for part in r.get("output_auxiliary_files", "").split(";"):
            if part.strip().lower().endswith(".md"):
                candidates.append(part.strip())
        for md in candidates:
            if not md or md in seen:
                continue
            seen.add(md)
            q = q_by_md.get(md, {})
            rows.append({
                "file_id": r.get("file_id", ""),
                "original_file_path": r.get("original_file_path", ""),
                "original_file_name": r.get("original_file_name", ""),
                "file_extension": r.get("file_extension", ""),
                "normalized_md_path": md,
                "conversion_status": r.get("conversion_status", ""),
                "quality_level": q.get("quality_level", ""),
                "text_length": q.get("text_length", ""),
                "manual_review_required": r.get("manual_review_required", q.get("manual_review_required", "")),
                "evidence_type": "markdown",
                "source_traceability": "yes" if r.get("original_file_path") else "unknown",
            })
    for r in word_recovery:
        if r.get("conversion_status") != "success":
            continue
        md = r.get("output_md_path", "")
        if not md or md in seen:
            continue
        seen.add(md)
        q = q_by_md.get(md, {})
        rows.append({
            "file_id": r.get("file_id", ""),
            "original_file_path": r.get("original_file_path", ""),
            "original_file_name": r.get("original_file_name", ""),
            "file_extension": r.get("file_extension", ""),
            "normalized_md_path": md,
            "conversion_status": "markitdown_recovered",
            "quality_level": q.get("quality_level", ""),
            "text_length": r.get("text_length", q.get("text_length", "")),
            "manual_review_required": r.get("manual_review_required", "yes"),
            "evidence_type": "markitdown_word_markdown",
            "source_traceability": "yes" if r.get("original_file_path") else "unknown",
        })
    for md_path in sorted(CONVERTED_MD.rglob("*.md")) if CONVERTED_MD.exists() else []:
        md = str(md_path.resolve())
        if md in seen:
            continue
        q = q_by_md.get(md, {})
        rows.append({
            "file_id": "",
            "original_file_path": q.get("source_file", ""),
            "original_file_name": Path(q.get("source_file", "")).name if q.get("source_file") else "",
            "file_extension": q.get("source_type", ""),
            "normalized_md_path": md,
            "conversion_status": "existing_or_stage2",
            "quality_level": q.get("quality_level", ""),
            "text_length": q.get("text_length", ""),
            "manual_review_required": q.get("manual_review_required", ""),
            "evidence_type": "markdown",
            "source_traceability": "yes" if q.get("source_file") else "unknown",
        })
    return rows


def build_cards(inventory: list[dict[str, Any]]) -> list[dict[str, Any]]:
    cards = []
    for idx, r in enumerate(inventory, 1):
        md = Path(str(r.get("normalized_md_path", "")))
        text = read_text(md) if md.exists() else ""
        blob = " ".join([str(r.get("original_file_path", "")), str(r.get("original_file_name", "")), str(r.get("normalized_md_path", "")), text[:10000]])
        stage, stage_label = detect_first(blob, STAGES)
        category = detect_category(blob)
        if category in {"BOM", "SOP/Process", "Inspection", "Packaging/Labeling"}:
            stage, stage_label = "07_dmr_manufacturing", "DMR Manufacturing"
        dhf_dmr = detect_dhf_dmr(category, blob)
        product = detect_product(blob)
        market = detect_market(blob)
        standards = detect_standards(blob)
        reqs = detect_requirements(blob)
        status, issue = baseline_check(category, stage, product, market, standards, reqs)
        cards.append({
            "file_card_id": f"FC-{idx:04d}",
            "file_id": r.get("file_id", ""),
            "source_file": r.get("original_file_path", ""),
            "md_file": str(md.resolve()) if md else "",
            "file_category": category,
            "dhf_or_dmr": dhf_dmr,
            "project_stage": stage,
            "project_stage_label": stage_label,
            "product_or_model_detected": product,
            "market_detected": market,
            "standards_detected": "; ".join(standards),
            "key_requirements_detected": "; ".join(reqs),
            "referenced_files": extract_refs(text),
            "conversion_status": r.get("conversion_status", ""),
            "quality_level": r.get("quality_level", ""),
            "baseline_match_status": status,
            "issue_summary": issue,
            "manual_review_required": "yes" if issue else r.get("manual_review_required", ""),
        })
    return cards


def write_stage_checklists() -> None:
    STAGE_DIR.mkdir(exist_ok=True)
    data = {
        "01_initiation.md": ["product/model clear", "target market clear", "intended use/user/population clear", "key performance targets clear", "customer/market need traceable"],
        "02_regulatory_strategy.md": ["US route confirmed", "general standards identified", "thermometer product standard identified", "labeling/IFU market requirements identified", "regulatory requirements flow to design input"],
        "03_design_input.md": ["requirements trace to baseline", "accuracy/range/life/use environment clear", "software/hardware/structure/labeling inputs complete", "source evidence present", "verification mapping possible"],
        "04_risk_management.md": ["plan scope and method defined", "hazards cover use error/accuracy/software/electrical/materials", "controls trace to design outputs", "residual risk acceptable", "post-market feedback can update risk"],
        "05_design_output.md": ["code/schematic/PCB/drawings/BOM versioned", "outputs cover design inputs", "materials match biocompatibility assumptions", "software version/build traceable", "tooling and drawings support manufacturing"],
        "06_verification_validation.md": ["plan covers inputs and standards", "accuracy/EMC/safety/software/biocompatibility/usability/life evidence present", "methods/samples/criteria clear", "deviations handled", "conclusions support registration"],
        "07_dmr_manufacturing.md": ["BOM/SOP/inspection/labeling match design output", "critical processes and quality attributes covered", "fixtures and equipment controlled", "sampling/AQL justified", "DMR supports manufacturing and audit"],
        "08_registration_td.md": ["TD covers target market", "attachment list and versions complete", "regulatory matrix traceable", "clinical/PMS/PMCF/PSUR aligned", "TD matches DHF/DMR baseline"],
        "09_post_market_feedback.md": ["feedback categorized", "mapped to risk/design input/verification/PMS", "recurring issues identified", "design change triggers assessed", "evidence source traceable"],
    }
    for filename, items in data.items():
        lines = [f"# {filename[:-3]} checklist", "", "## Checks", ""]
        lines.extend([f"- [ ] {item}" for item in items])
        lines.extend(["", "## Review output format", "", "- issue", "- reason", "- source reference", "- recommended action"])
        (STAGE_DIR / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_index(cards: list[dict[str, Any]], inventory: list[dict[str, Any]]) -> None:
    stage_counts = Counter(c["project_stage_label"] for c in cards)
    cat_counts = Counter(c["file_category"] for c in cards)
    match_counts = Counter(c["baseline_match_status"] for c in cards)
    doc_table_rows = read_csv(ROOT / "doc_table_extraction_report.csv")
    doc_table_success = sum(1 for r in doc_table_rows if r.get("conversion_status") == "success")
    doc_table_count = sum(int(r.get("docx_table_count") or 0) for r in doc_table_rows)
    image_rows = read_csv(ROOT / "excel_image_evidence" / "image_evidence_index.csv")
    image_evidence_rows = [r for r in image_rows if r.get("image_path")]
    image_value_counts = Counter(r.get("evidence_value") or "unknown" for r in image_evidence_rows)
    image_manual_review = sum(1 for r in image_evidence_rows if (r.get("manual_review_required") or "").lower() == "yes")
    readiness_rows = read_csv(ROOT / "ai_readiness_report.csv")
    readiness_counts = Counter(r.get("ai_readiness_level") or "unknown" for r in readiness_rows)
    word_recovery_rows = read_csv(ROOT / "markitdown_word_recovery_report.csv")
    word_recovery_success = len({r.get("original_file_path", "") for r in word_recovery_rows if r.get("conversion_status") == "success" and r.get("original_file_path", "")})
    word_recovery_missing = sum(1 for r in word_recovery_rows if r.get("conversion_status") == "missing_source")
    loss_risk_rows = read_csv(ROOT / "conversion_loss_risk_report.csv")
    loss_risk_counts = Counter(r.get("loss_risk_level") or "unknown" for r in loss_risk_rows)
    lines = [
        "# PT9L DHF/DMR Knowledge Index",
        "",
        "This is the first AI-readable knowledge layer built from converted evidence files.",
        "",
        "## Baseline",
        f"- Product: {BASELINE['product_name']} / {BASELINE['model_or_series']}",
        f"- Target market: {BASELINE['target_market']}",
        "- Baseline file: `baseline_project_profile.yaml`",
        "",
        "## Assets",
        f"- Normalized evidence rows: {len(inventory)}",
        f"- File cards: {len(cards)}",
        "- Stage checklists: `stage_checklist/`",
        "- Generated draft docs: `generated_docs/`",
        f"- Recovered legacy DOC files: {doc_table_success}",
        f"- Recovered DOCX table count: {doc_table_count}",
        f"- Extracted Excel images: {len(image_evidence_rows)}",
        f"- High-value Excel image evidence: {image_value_counts.get('high', 0)}",
        f"- Excel images requiring review: {image_manual_review}",
        f"- MarkItDown Word recoveries: {word_recovery_success}",
        f"- Word files missing source for MarkItDown: {word_recovery_missing}",
        f"- Word conversion loss high risk: {loss_risk_counts.get('high', 0)}",
        f"- Word conversion loss medium risk: {loss_risk_counts.get('medium', 0)}",
        "",
        "## By stage",
    ]
    lines.extend([f"- {k}: {v}" for k, v in stage_counts.most_common()])
    lines.extend(["", "## By category"])
    lines.extend([f"- {k}: {v}" for k, v in cat_counts.most_common()])
    lines.extend(["", "## Baseline match status"])
    lines.extend([f"- {k}: {v}" for k, v in match_counts.most_common()])
    lines.extend(["", "## AI readiness"])
    lines.extend([f"- {k}: {v}" for k, v in readiness_counts.most_common()])
    lines.extend(["", "## Key files", "- `normalized_evidence_inventory.csv`", "- `file_cards.csv`", "- `baseline_consistency_report.md`", "- `ai_readiness_report.csv`", "- `ai_readiness_summary.md`", "- `markitdown_word_recovery_report.csv`", "- `markitdown_word_recovery_summary.md`", "- `conversion_loss_risk_report.csv`", "- `conversion_loss_risk_summary.md`", "- `excel_image_evidence/image_evidence_index.csv`", "- `excel_image_evidence/image_evidence.md`"])
    (ROOT / "knowledge_index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_baseline_report(cards: list[dict[str, Any]]) -> None:
    counts = Counter(c["baseline_match_status"] for c in cards)
    review = [c for c in cards if c["baseline_match_status"] != "aligned_or_not_applicable"]
    priority_cats = {"Regulatory/Registration", "Design Input", "Verification/Validation", "Packaging/Labeling", "Risk Management"}
    priority = [c for c in review if c["file_category"] in priority_cats]
    lines = [
        "# Baseline Consistency Report",
        "",
        "First-pass check against baseline: PT9L / infrared forehead thermometer / United States.",
        "",
        "## Summary",
    ]
    lines.extend([f"- {k}: {v}" for k, v in counts.most_common()])
    lines.extend(["", "## Priority review list"])
    for c in priority[:100]:
        lines.extend([
            f"### {c['file_card_id']} - {Path(c['md_file']).name}",
            f"- Category: {c['file_category']}",
            f"- Stage: {c['project_stage_label']}",
            f"- Product detected: {c['product_or_model_detected']}",
            f"- Market detected: {c['market_detected']}",
            f"- Issue: {c['issue_summary'] or 'manual review required'}",
            f"- File: `{rel(c['md_file'])}`",
            "",
        ])
    lines.extend(["## Next actions", "- Confirm baseline market and regulatory route.", "- Add market/product fields to sensitive files where missing.", "- Use stage_checklist files for manual review."])
    (ROOT / "baseline_consistency_report.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_generated_docs(cards: list[dict[str, Any]]) -> None:
    GENERATED_DIR.mkdir(exist_ok=True)
    standards = sorted(set(s.strip() for c in cards for s in c["standards_detected"].split(";") if s.strip()))
    reqs = Counter(r.strip() for c in cards for r in c["key_requirements_detected"].split(";") if r.strip())
    verification_cards = [c for c in cards if c["file_category"] == "Verification/Validation"]
    design_output_cards = [c for c in cards if c["file_category"] in {"Design Output", "Drawing/Structure/Electronics", "Code/Software"}]
    docs = {
        "regulatory_checklist_draft.md": ["# Regulatory Checklist Draft", "", f"- Target market: {BASELINE['target_market']}", f"- Product: {BASELINE['product_name']}", "", "## Detected standards", *[f"- {s}" for s in standards], "", "## Gaps", "- Confirm exact US route.", "- Confirm FDA-recognized standards.", "- Confirm labeling/IFU requirements."],
        "design_input_draft.md": ["# Design Input Draft", "", f"- Product type: {BASELINE['product_type']}", f"- Intended use: {BASELINE['intended_use']}", "", "## Requirement areas detected", *[f"- {k}: {v} evidence files" for k, v in reqs.most_common()]],
        "traceability_matrix_draft.md": ["# Traceability Matrix Draft", "", "| Baseline item | Evidence source | Next action |", "| --- | --- | --- |", "| US target market | Regulatory/labeling files | confirm route and standards |", "| Accuracy | verification/performance files | map to design input |", "| Biocompatibility | material/biocompatibility files | confirm contact type |", "| DMR controls | SOP/BOM/inspection files | map to design output |"],
        "verification_plan_draft.md": ["# Verification Plan Draft", "", "## Areas", "- Accuracy/performance", "- Electrical safety", "- EMC", "- Software", "- Usability", "- Biocompatibility", "- Service life/transport", "", "## Existing evidence to map", *[f"- {c['file_card_id']}: {Path(c['md_file']).name}" for c in verification_cards[:80]]],
        "technical_documentation_outline.md": ["# Technical Documentation Outline", "", "- Device description and specification", "- Intended use, user, patient population, use environment", "- Design and manufacturing information", "- Regulatory requirement checklist", "- Risk management", "- Verification and validation", "- Clinical/PMS/PMCF if applicable", "- Labeling and IFU"],
        "patent_materials_seed.md": ["# Patent Materials Seed", "", "## Evidence sources", *[f"- {c['file_card_id']}: {Path(c['md_file']).name}" for c in design_output_cards[:100]], "", "## Mining angles", "- structure and assembly", "- sensor compensation and measurement workflow", "- fixture/tooling improvements", "- software and calibration process", "- user feedback pain points"],
    }
    for filename, lines in docs.items():
        (GENERATED_DIR / filename).write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    write_baseline()
    inventory = build_inventory()
    write_csv(ROOT / "normalized_evidence_inventory.csv", inventory, ["file_id", "original_file_path", "original_file_name", "file_extension", "normalized_md_path", "conversion_status", "quality_level", "text_length", "manual_review_required", "evidence_type", "source_traceability"])
    cards = build_cards(inventory)
    write_csv(ROOT / "file_cards.csv", cards, ["file_card_id", "file_id", "source_file", "md_file", "file_category", "dhf_or_dmr", "project_stage", "project_stage_label", "product_or_model_detected", "market_detected", "standards_detected", "key_requirements_detected", "referenced_files", "conversion_status", "quality_level", "baseline_match_status", "issue_summary", "manual_review_required"])
    write_stage_checklists()
    write_index(cards, inventory)
    write_baseline_report(cards)
    write_generated_docs(cards)
    print("baseline_project_profile.yaml")
    print(f"normalized_evidence_inventory.csv rows={len(inventory)}")
    print(f"file_cards.csv rows={len(cards)}")
    print(f"stage_checklist files={len(list(STAGE_DIR.glob('*.md')))}")
    print(f"generated_docs files={len(list(GENERATED_DIR.glob('*.md')))}")
    print("knowledge_index.md")
    print("baseline_consistency_report.md")


if __name__ == "__main__":
    main()
