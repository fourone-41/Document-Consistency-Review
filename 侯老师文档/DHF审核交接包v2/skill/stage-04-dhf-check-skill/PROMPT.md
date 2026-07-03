# Stage 04 DHF Design Input Check Prompt Template

Use this prompt when starting a Stage 04 DHF design input check for a new model.

```text
Run the Stage 04 DHF design input check.

Inputs:
- product_original_root: <path to product original DHF/DMR root>
- product_md_root: <path to converted AI-readable root>
- product_check_root: <path to mirrored check output root>
- stage_01_check_folder: <path to Stage 01 check outputs>
- stage_02_check_folder: <path to Stage 02 check outputs>
- stage_03_check_folder: <path to Stage 03 check outputs>
- qms_procedure_md: <path to QP-7.3 converted procedure>
- stage_04_md_folder: <path to converted Stage 04 design input folder>

Rules:
- Read the Stage 04 DHF design input check skill before acting.
- Start from check items, not conclusions.
- Do not recreate existing todos; update their statuses as work progresses.
- Read cover, design input summary, review plan, review checklist, review record, and assets.
- Extract design input baseline: identity, document numbers, general/function/performance/component/regulation inputs, review plan, review record, signatures, and conversion risks.
- Check Stage 01 requirement carry-forward.
- Check Stage 02 plan/team/schedule carry-forward.
- Check Stage 03 risk-control carry-forward.
- Check the greater-than-or-equal principle: Stage 04 design input must not narrow Stage 01 customer requirements, applicable regulations/standards, or Stage 03 risk controls.
- For each source requirement where possible, classify the design input as equal, broader, narrower, or unclear.
- Any narrower item must be reported as nonconforming unless there is a controlled and justified rationale.
- Check verifiability, internal consistency, standard coverage, review adequacy, and signature approval completeness.
- Check downstream closure path to Stage 08 verification/DFMEA and Stage 11 validation.
- Treat high-risk Excel conversion, checkbox semantics, and blank signatures/dates as evidence gaps requiring manual/original review.

Outputs:
- stage_04_check_items.md
- stage_04_check_items_closure_matrix.csv
- stage_04_design_input_baseline.md
- stage_04_findings.csv
- stage_04_traceability_matrix.csv
- stage_04_design_input_check_report.html

Do not stop until all requested outputs are generated and scanned for destructive mojibake.
```
