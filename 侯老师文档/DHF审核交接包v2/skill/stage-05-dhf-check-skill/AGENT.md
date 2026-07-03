# stage-05-dhf-check-agent

## Purpose

Audit Stage 05 DHF structural scheme and structural drawing evidence.

The agent checks whether Stage 05:

- receives Stage 04 design inputs and Stage 03 risk controls;
- converts them into structural scheme and drawing outputs without narrowing them;
- provides adequate review plan/checklist/record evidence;
- creates a human-readable report that closes every Stage 05 check item.

## Required Reading

1. `stage-05-dhf-check-skill/SKILL.md`
2. Stage 04 baseline, findings, traceability, and check items.
3. Stage 05 converted structural scheme, review plans, checklists, records, assets, and conversion-loss files.
4. QP-7.3 procedure when checking design-output and review process requirements.

## Mandatory Workflow

1. Confirm Stage 05 AI-readable files and assets exist.
2. Extract product identity and file completeness.
3. Extract structural scheme decisions.
4. Extract scheme review checklist scope, evidence, and conclusion state.
5. Extract drawing review checklist scope, measured fields, evidence, and conclusion state.
6. Extract review plan acceptance criteria, participants, roles, schedule, issue closure, and design-change rules.
7. Extract review record conclusions, residual issues, new issues, signatures, and dates.
8. Check Stage 04 design-input carry-forward into Stage 05 structural outputs.
9. Check the non-narrowing principle: each Stage 05 structural output must be greater than or equal to Stage 04 design input and relevant Stage 03 risk-control requirements.
10. If item-level proof is missing, mark it as `needs_item_level_matrix`.
11. Check scheme adequacy, reuse rationale, battery, sensor/lens, fit/fixation, dimensions/clearances, packaging/labeling, and manufacturability.
12. Check downstream closure path to Stage 08 verification, DFMEA, packaging, and transfer evidence.
13. Write baseline, findings CSV, traceability matrix CSV, closure matrix CSV, and Chinese HTML report.
14. Verify report readability and absence of destructive mojibake.

## Required Output

Write outputs under the mirrored Stage 05 check folder:

- `stage_05_structural_baseline.md`
- `stage_05_check_items.md`
- `stage_05_findings.csv`
- `stage_05_traceability_matrix.csv`
- `stage_05_check_items_closure_matrix.csv`
- `stage_05_structural_check_report.html`
