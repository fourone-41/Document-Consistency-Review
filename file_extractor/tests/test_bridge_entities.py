# file_extractor/tests/test_bridge_entities.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import bridge_entities as be


def test_extract_entity_mentions_finds_known_patterns():
    text = "本测试验证 PT9L 红外传感器在 ISO 80601-2-56 标准下的表现，由张三负责。"

    mentions = be.extract_entity_mentions(text)

    assert "PT9L" in mentions
    assert "ISO 80601-2-56" in mentions


def test_extract_entity_mentions_empty_text_returns_empty_set():
    assert be.extract_entity_mentions("") == set()
    assert be.extract_entity_mentions(None) == set()


def test_find_bridge_entities_pairs_nodes_sharing_entity_across_sources():
    nodes = {
        "risks": [
            {"risk_id": "R-01", "hazard": "PT9L 红外传感器漂移导致测量误差", "_source": "doc_a.md"},
        ],
        "tests": [
            {"test_id": "T-12", "item": "PT9L 在高温环境下的线性度验证", "_source": "doc_b.md"},
            {"test_id": "T-15", "item": "电池续航测试", "_source": "doc_b.md"},
        ],
    }

    pairs = be.find_bridge_entities(nodes)

    assert any(
        s.get("risk_id") == "R-01" and t.get("test_id") == "T-12"
        for s, t in pairs
    )
    assert not any(
        s.get("risk_id") == "R-01" and t.get("test_id") == "T-15"
        for s, t in pairs
    )


def test_find_bridge_entities_ignores_same_source_pairs():
    nodes = {
        "risks": [{"risk_id": "R-01", "hazard": "PT9L 传感器问题", "_source": "doc_a.md"}],
        "tests": [{"test_id": "T-12", "item": "PT9L 传感器测试", "_source": "doc_a.md"}],
    }

    pairs = be.find_bridge_entities(nodes)

    assert pairs == []
