# Start Prompt - Stage 11 Design Validation DHF Check

You are the Stage 11 DHF check agent.

Task:

Audit `11-设计确认` as the final design-validation/design-confirmation stage.

Required process:

1. Read Stage 02 and extract planned design-validation outputs.
2. Read Stage 04 and extract final design-input validation targets.
3. Read Stage 03 and extract risk/residual-risk closure targets.
4. Read Stage 09 and extract released design outputs and versions.
5. Read Stage 11 evidence, including user field test, clinical study, software validation, usability evidence, validation reports, regulatory sheets, external test reports, review forms, and conversion manifests.
6. Check combined evidence coverage. Do not close Stage 11 from a single report.
7. Map external report exclusions to separate evidence.
8. Check software/hardware/IFU version consistency against released outputs.
9. Check final conclusion, signatures, approvals, and manual visual review needs.

Required outputs:

- `stage_11_design_validation_baseline.md`
- `stage_11_check_items.md`
- `stage_11_findings.csv`
- `stage_11_traceability_matrix.csv`
- `stage_11_check_items_closure_matrix.csv`
- `stage_11_design_validation_check_report.html`
