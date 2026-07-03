# Stage 05 DHF Check Prompt Template

Use the `stage-05-dhf-check-skill`.

Audit the Stage 05 structural scheme and structural drawing folder for PT9L.

Inputs:

- Stage 04 design input baseline, findings, traceability, and check items.
- Stage 03 risk findings and traceability when structural risk controls are relevant.
- Stage 05 structural scheme.
- Stage 05 scheme review plan, scheme review checklist, and scheme review record.
- Stage 05 structural drawing review plan, drawing review checklist, and drawing review record.
- Stage 05 conversion assets, page evidence, and conversion-loss reports.

Rules:

- First define extraction items and check items.
- Extract structural scheme decisions and review evidence.
- Extract drawing checklist items, measured fields, conclusions, and review evidence.
- Check Stage 04 design-input carry-forward.
- Check the greater-than-or-equal principle: Stage 05 structural outputs must not narrow Stage 04 design inputs or Stage 03 risk controls.
- For each source requirement where possible, classify the structural output as equal, broader, narrower, or unclear.
- Any narrower item must be reported as nonconforming unless there is a controlled and justified rationale.
- Check scheme adequacy, T-Z1/PT5 reuse rationale, battery implementation, sensor/lens implementation, fit/fixation, dimensions/clearances, packaging/labeling, manufacturability, review plans, review records, signatures, and conversion risks.
- Generate a report that closes every `CHK-05-*` item and leaves human-review columns when useful.

Required outputs:

- `stage_05_structural_baseline.md`
- `stage_05_check_items.md`
- `stage_05_findings.csv`
- `stage_05_traceability_matrix.csv`
- `stage_05_check_items_closure_matrix.csv`
- `stage_05_structural_check_report.html`
