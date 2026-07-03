# Prompt Template - Stage 11 DHF Check

Audit Stage 11 design validation / design confirmation for product `{product_identity}`.

Inputs:

- Stage 02 baseline: `{stage_02_baseline}`
- Stage 03 risk package: `{stage_03_package}`
- Stage 04 design-input package: `{stage_04_package}`
- Stage 09 design-output package: `{stage_09_package}`
- Stage 11 converted folder: `{stage_11_folder}`
- Output folder: `{output_folder}`

Rules:

- First read Stage 02, Stage 03, Stage 04, and Stage 09.
- Treat Stage 11 as the final proof that all design work is completed and confirmed.
- Extract user field test, clinical study, software validation, usability evidence, general validation report, regulatory sheet, external test reports, review records, signatures, dates, approvals, and conversion risks.
- Check whether Stage 11 closes Stage 02 design-validation planned outputs.
- Check whether Stage 11 validates all relevant Stage 04 design inputs without narrowing them.
- Check whether Stage 11 closes Stage 03 risk management and residual-risk evidence.
- Check whether Stage 11 validates the same final outputs released in Stage 09.
- Map every external report exclusion to separate evidence.
- Flag final conclusion, signature, approval, conversion, and version gaps.
- Generate baseline, check items, findings, traceability matrix, closure matrix, and HTML report.
