from pathlib import Path

import generate_all_results_review as gen


def test_build_records_keeps_all_review_buckets():
    records = gen.build_records(Path("."))
    buckets = {row["bucket"] for row in records}
    assert {"confirmed", "needs_context", "dismissed"}.issubset(buckets)
    assert len(records) == 582


def test_render_html_contains_filters_and_embedded_records():
    html = gen.render_html(
        records=[
            {
                "id": "T-001",
                "bucket": "confirmed",
                "status": "keep",
                "severity": "P1",
                "agent": "Agent",
                "finding_type": "type",
                "claim": "claim",
                "reason": "reason",
                "evidence": [],
            }
        ],
        summary={"current_confirmed_error_total": 1},
    )
    assert "id=\"statusFilter\"" in html
    assert "id=\"searchBox\"" in html
    assert "const REVIEW_RECORDS" in html
    assert "T-001" in html


def test_render_html_prevents_side_content_overlap():
    html = gen.render_html(records=[], summary={})
    assert ".layout { display: block;" in html
    assert ".side { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr));" in html
    assert ".result-pane" in html
    assert "min-width: 0" in html
    assert "</aside>\n      <div class=\"result-pane\">" in html
