---
name: stage-04-dhf-check-skill
description: Checks Stage 04 DHF design input evidence for requirement carry-forward, risk carry-forward, verifiability, document control, review adequacy, regulatory standard coverage, and downstream verification closure. Use when auditing design input summaries, design input review plans, review checklists, review records, regulation/standard lists, or Stage 04 to Stage 08/11 traceability.
---

# Stage 04 DHF Design Input Check Skill

## Purpose

Use this skill for Stage 04 design-input content audits.

Stage 04 is the design-input control baseline. It converts:

- Stage 01 product identity, customer requirements, market, and regulatory baseline;
- Stage 02 development plan, project team, and schedule baseline;
- Stage 03 risk management and risk controls;

into objective and verifiable design input requirements.

Core principle: Stage 04 design input must be greater than or equal to its source requirements. It must not narrow Stage 01 customer requirements, applicable regulatory/standard requirements, or Stage 03 risk-control requirements unless there is a controlled and justified rationale.

## Required Audit Order

1. Confirm AI-readable evidence exists.
2. Define extraction items.
3. Define check items.
4. Run checks.
5. Use the report and closure matrix to prove every check item was covered.
6. Human reviewers judge whether the conclusions are acceptable.

## Required Inputs

Read before concluding:

- Stage 01 check items, baseline, regulatory baseline, and customer requirement findings.
- Stage 02 check items, development plan baseline, project team baseline, and schedule baseline.
- Stage 03 check items, risk baseline, findings, and risk-control traceability.
- Stage 04 cover, design input summary, review plan, review checklist, review record.
- Stage 04 assets and conversion-loss reports.
- QP-7.3 procedure when checking design-input procedure requirements.

## Required Extraction Content

Extract:

- product identity and document numbers;
- five design input parts: general, function, performance, component, regulation/standard list;
- market/certification selection;
- measurable function and performance requirements;
- component, packaging, IFU, battery, labeling, and environmental requirements;
- selected/non-selected standards and regions;
- review plan participants, acceptance criteria, issue-closure rule, and schedule rule;
- review record conclusions, issues, signatures, and dates;
- conversion-loss and visual/manual review risks.

## Required Checks

Check:

- Stage 04 file completeness.
- Identity consistency with Stage 01/02/03.
- Document number control for all design input parts.
- Carry-forward from Stage 01 customer requirements and USA regulatory baseline.
- Carry-forward from Stage 03 risk controls.
- Whether every function, performance, component, packaging, labeling, IFU, regulatory, and risk-control input is greater than or equal to the source requirement.
- Requirement verifiability and objectivity.
- Performance requirement adequacy.
- Function requirement adequacy.
- Component and packaging adequacy.
- Regulation/standard list adequacy.
- Internal consistency across sheets.
- Review plan and review record adequacy.
- Signature and approval completeness.
- Conversion/manual review needs.
- Downstream closure to Stage 08 verification/DFMEA and Stage 11 validation.

## Finding Rules

- Treat blank signatures/dates as `evidence_gap` unless original/page evidence proves they are present.
- Treat high-risk Excel conversions as `manual_visual_review_required`.
- Treat checkboxes and visual-format semantics as requiring page/original review.
- Treat a design input as weak if it is not objective or not verifiable.
- Treat a design input as nonconforming if it narrows the source customer requirement, regulatory requirement, or risk-control requirement.
- If item-level source-to-design-input comparison has not been performed, classify the non-narrowing principle as `needs_item_level_matrix`, not as fully closed.
- Treat risk carry-forward as partial unless risk IDs or risk-control topics can be mapped to design inputs.
- Treat downstream closure as pending until Stage 08/11 evidence is checked.
- Every finding must include expected requirement, observed evidence, source evidence, status, and recommended action.

## Required Outputs

Under the mirrored Stage 04 check folder, create or update:

- `stage_04_check_items.md`
- `stage_04_check_items_closure_matrix.csv`
- `stage_04_design_input_baseline.md`
- `stage_04_findings.csv`
- `stage_04_traceability_matrix.csv`
- `stage_04_design_input_check_report.html`

## Closure Rule

The HTML report is complete only when every `CHK-04-*` item in `stage_04_check_items.md` has a corresponding conclusion in:

- the HTML report;
- `stage_04_findings.csv`;
- `stage_04_traceability_matrix.csv`;
- `stage_04_check_items_closure_matrix.csv`.

If a check item has no corresponding report/finding/matrix entry, mark the audit as incomplete.
