# file_extractor/tests/test_relation_groups.py
import yaml
from pathlib import Path

RELATION_GROUPS_PATH = Path(__file__).parent.parent.parent / "schema" / "relation_groups.yaml"

# 与 step2_extract_edges.py 的 ALL_RELATION_TYPES 中列出的19种类型保持一致
ALL_EDGE_TYPES = {
    "DERIVES_FROM", "CONSTRAINED_BY", "MITIGATED_BY", "VERIFIED_BY",
    "REPORTED_IN", "COVERS", "HAS_MEASUREMENT", "DEPENDS_ON", "SCHEDULES",
    "HAS_REVISION", "HAS_REVIEW_ITEM", "REVIEWS", "LISTS_FILE",
    "DESCRIBES_SOFTWARE", "SIGNED", "IMPLEMENTED_IN", "HAS_DETAIL",
    "RESPONSIBLE_FOR", "PRODUCES",
}


def load_relation_groups() -> dict:
    with open(RELATION_GROUPS_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["relation_groups"]


def test_relation_groups_file_exists():
    assert RELATION_GROUPS_PATH.exists()


def test_all_edge_types_covered_exactly_once():
    groups = load_relation_groups()
    seen = []
    for group_name, types in groups.items():
        seen.extend(types)

    seen_set = set(seen)
    assert seen_set == ALL_EDGE_TYPES, (
        f"分组缺失: {ALL_EDGE_TYPES - seen_set}, 分组多余: {seen_set - ALL_EDGE_TYPES}"
    )
    assert len(seen) == len(seen_set), "存在类型被分到多个组里"


def test_five_groups_defined():
    groups = load_relation_groups()
    assert set(groups.keys()) == {
        "structural", "traceability", "verification", "risk_control", "admin"
    }
