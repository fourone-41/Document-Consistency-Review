# Prompt Template - Stage 09 DHF Check

Audit Stage 09 design output for product `{product_identity}`.

Inputs:

- Stage 02 development plan baseline: `{stage_02_baseline}`
- Stage 09 converted folder: `{stage_09_folder}`
- Prior stage baselines/check packages: `{prior_stage_packages}`
- Output folder: `{output_folder}`

Rules:

- First read Stage 02 and extract design-output/design-transfer requirements.
- Treat `09-设计输出` as design output, not trial production.
- Extract design output list 1, design output list 2, EBOM, ABOM, drawings, package/label files, document numbers, versions, references, signatures, dates, approvals, and conversion risks.
- Check whether Stage 09 is greater than or equal to Stage 04 to Stage 08 evidence and does not narrow prior requirements.
- Flag reused/reference outputs that lack controlled reuse/equivalence rationale.
- Flag missing signatures/dates and CAD/DWG conversion gaps.
- Generate baseline, check items, findings, traceability matrix, closure matrix, and HTML report.
