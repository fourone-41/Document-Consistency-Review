# Prompt Template - Stage 10 DHF Check

Audit Stage 10 trial-production files for product `{product_identity}`.

Inputs:

- Stage 02 development plan baseline: `{stage_02_baseline}`
- Stage 09 design output package: `{stage_09_package}`
- Stage 10 converted folder: `{stage_10_folder}`
- Output folder: `{output_folder}`

Rules:

- First read Stage 02 and extract trial-production and design-transfer requirements.
- Read Stage 09 to understand design-output and DMR/design-transfer pending items.
- Extract trial-production application, summary, reports, attachments, product identity, trial mode, exemption rationale, quantity, completion date, technical basis, responsible persons, acceptance criteria, problems, corrective actions, conclusions, signatures, dates, and conversion risks.
- If actual trial production is exempted, audit the exemption rationale and approval as a required evidence item.
- Flag missing manufacturing reports/attachments.
- Flag checkbox/signature evidence that is not AI-readable.
- Generate baseline, check items, findings, traceability matrix, closure matrix, and HTML report.
