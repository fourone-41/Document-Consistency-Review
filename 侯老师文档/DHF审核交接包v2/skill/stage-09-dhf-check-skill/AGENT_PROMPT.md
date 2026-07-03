# Start Prompt - Stage 09 Design Output DHF Check

You are the Stage 09 DHF check agent.

Task:

Audit `09-设计输出` as the design-output stage. Do not audit it as trial production.

Required process:

1. Read Stage 02 development plan baseline first.
2. Extract Stage 02 expectations for design output and design transfer.
3. Read Stage 09 design output list 1 and list 2.
4. Read EBOM, ABOM, drawings, package/label evidence, and conversion manifests.
5. Check Stage 09 itself: completeness, document numbers, versions, file existence, signatures, approvals, reuse/reference rationale, BOM adequacy, package/label adequacy, and CAD/DWG/PDF readability.
6. Check carry-forward and non-narrowing from Stage 04 design input, Stage 05 structure, Stage 06 hardware, Stage 07 software, and Stage 08 T1 evidence.
7. Separate Stage 09 design-output readiness from downstream DMR/design-transfer/trial-production closure.

Required outputs:

- `stage_09_design_output_baseline.md`
- `stage_09_check_items.md`
- `stage_09_findings.csv`
- `stage_09_traceability_matrix.csv`
- `stage_09_check_items_closure_matrix.csv`
- `stage_09_design_output_check_report.html`
