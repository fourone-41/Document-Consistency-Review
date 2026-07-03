---
name: stage-05-dhf-check-skill
description: Checks Stage 05 DHF structural scheme and structural drawing evidence for Stage 04 design-input carry-forward, non-narrowing, scheme adequacy, drawing fit/dimension/clearance adequacy, packaging/labeling implementation, manufacturability, review adequacy, signatures, conversion risks, and downstream verification closure. Use when auditing structural schemes, structural drawing review plans, structural review checklists, review records, or Stage 05 to Stage 08/DFMEA/transfer traceability.
---

# Stage 05 DHF Structural Scheme And Drawing Check Skill

## Purpose

Use this skill for Stage 05 structural scheme and structural drawing audits.

Stage 05 is the structural design-output control baseline. It converts:

- Stage 04 component, packaging, label/nameplate, battery, sensor/lens, size, weight, material/finish, and environmental design inputs;
- Stage 03 risk-control requirements that require structural implementation;
- Stage 02 review, schedule, design-change, and issue-closure process requirements;

into structural scheme decisions, structural drawing review evidence, manufacturability review evidence, and downstream verification inputs.

Core principle: Stage 05 structural outputs must be greater than or equal to Stage 04 design inputs and relevant Stage 03 risk-control requirements. They must not narrow the prior requirements unless there is controlled and justified rationale.

## Required Audit Order

1. Confirm AI-readable evidence exists.
2. Define extraction items.
3. Define check items.
4. Run checks.
5. Use the report and closure matrix to prove every check item was covered.
6. Human reviewers judge whether the conclusions are acceptable.

## Required Inputs

Read before concluding:

- Stage 04 check items, design input baseline, findings, and traceability matrix.
- Stage 03 risk baseline, findings, and risk-control traceability when structural controls are relevant.
- Stage 02 development plan/team/schedule baseline when checking review roles and timing.
- Stage 05 structural scheme.
- Stage 05 scheme review plan, scheme review checklist, and scheme review record.
- Stage 05 structural drawing review plan, drawing review checklist, and drawing review record.
- Stage 05 assets and conversion-loss reports.
- QP-7.3 procedure when checking design-output and review procedure requirements.

## Required Extraction Content

Extract:

- product identity and controlled document numbers;
- structural scheme decisions;
- reused or selected reference designs such as T-Z1 or PT5;
- sensor, lens, cover, button, battery cover, battery spring, LCD, battery, cable, packaging, and label decisions;
- scheme review checklist content and conclusion evidence;
- drawing review checklist content for fit, fixation, dimensions, clearances, packaging, manufacturability, nameplate, printing, and painting;
- review plan participants, roles, acceptance criteria, schedule rules, design-change rules, and issue-closure rules;
- review record conclusions, residual issues, new issues, signatures, and dates;
- conversion-loss and visual/manual review risks.

## Required Checks

Check:

- Stage 05 file completeness.
- Identity consistency with Stage 01/02/03/04.
- Separation of scheme review and drawing review sub-stages.
- Carry-forward from Stage 04 design inputs.
- Greater-than-or-equal principle against Stage 04 inputs and Stage 03 risk controls.
- Structural scheme adequacy.
- Reuse/selection rationale for T-Z1/PT5 or other reference designs.
- Battery implementation consistency.
- Sensor and lens implementation.
- Fit/fixation drawing adequacy.
- Dimensional and clearance adequacy.
- Packaging and labeling implementation.
- Manufacturability and transfer readiness.
- Review plan and review record adequacy.
- Signature and approval completeness.
- Conversion/manual review needs.
- Downstream closure to prototype build, Stage 08 verification, DFMEA, packaging, and transfer evidence.

## Finding Rules

- Treat high-risk Excel conversions as `manual_visual_review_required`.
- Treat checkboxes and visual-format semantics as requiring page/original review.
- Treat blank measured drawing fields as `open_gap` if no original drawing/CAD evidence is available.
- Treat blank signatures/dates as `evidence_gap` unless original/page evidence proves they are present.
- Treat reuse or selection decisions as `needs_rationale` unless equivalence or applicability evidence is present.
- Treat a Stage 05 output as nonconforming if it narrows Stage 04 design input or Stage 03 risk-control requirements.
- If item-level source-to-output comparison has not been performed, classify the non-narrowing principle as `needs_item_level_matrix`, not as fully closed.
- Treat downstream closure as pending until Stage 08/DFMEA/transfer evidence is checked.
- Every finding must include expected requirement, observed evidence, source evidence, status, and recommended action.

## Required Outputs

Under the mirrored Stage 05 check folder, create or update:

- `stage_05_check_items.md`
- `stage_05_check_items_closure_matrix.csv`
- `stage_05_structural_baseline.md`
- `stage_05_findings.csv`
- `stage_05_traceability_matrix.csv`
- `stage_05_structural_check_report.html`

## Closure Rule

The HTML report is complete only when every `CHK-05-*` item in `stage_05_check_items.md` has a corresponding conclusion in:

- the HTML report;
- `stage_05_findings.csv`;
- `stage_05_traceability_matrix.csv`;
- `stage_05_check_items_closure_matrix.csv`.

If a check item has no corresponding report/finding/matrix entry, mark the audit as incomplete.
