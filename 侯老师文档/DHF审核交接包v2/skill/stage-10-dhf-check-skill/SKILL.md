# Stage 10 DHF Check Skill - Trial Production Files

## Purpose

Audit Stage 10 trial-production files for DHF/DMR readiness.

Core principles:

- Always read Stage 02 development plan baseline first and map its `trial_production` and `design_transfer` expectations to Stage 10 evidence.
- Stage 10 may be actual trial production or exempted trial production. If exempted, the exemption rationale, approval, and equivalent acceptance-criteria coverage become critical evidence.
- A trial-production summary cannot be closed from a template alone. Final conclusion, issue disposition, DMR/design-output suitability, signatures, and dates must be verified.
- Verification/trial conclusions must be closed by body content. Do not accept file titles, filenames, document numbers, attachment names, checklist rows, or report existence as evidence unless the referenced body content has been read.
- Do not close downstream production readiness unless application, report/attachment, summary conclusion, and approvals are closed.

## Required Inputs

- Stage 02 development plan baseline and traceability matrix.
- Stage 09 design output baseline/check outputs.
- Stage 08 T1 baseline/check outputs if trial-production acceptance references T1/open items.
- Stage 10 converted folder, including trial-production application, reports, summary, attachments, and conversion manifests.

## Extract

- Evidence inventory and missing referenced attachments.
- Product identity: model, project number, product/project name.
- Trial mode: actual trial production vs exemption.
- Trial quantity and required completion date.
- Exemption rationale and approval evidence.
- Technical basis references: design output list 1, list 2, list 3/tooling, inspection/process/test methods.
- Personnel and responsibilities.
- Acceptance criteria.
- Trial issues, corrective actions, mass-production decision, re-trial decision.
- Final conclusion: passed, passed after correction, not passed.
- Design output and DMR rationality/suitability conclusions.
- Signatures, dates, approvals.
- Conversion quality, especially checkbox and visual evidence.
- Substantive body-content support for each claim: product identity, rationale/method, criteria, actual result/decision, conclusion, exclusions/limitations, and approval evidence.

## Check

- Stage 02 plan match.
- Application/report/summary completeness.
- Product identity consistency.
- Exemption rationale adequacy if applicable.
- Technical-basis traceability to Stage 09 design outputs and DMR.
- Personnel responsibility consistency with Stage 02.
- Acceptance criteria adequacy.
- Manufacturing-department report/attachment presence.
- Issue and corrective-action closure.
- Final conclusion and approval closure.
- Design output and DMR suitability conclusion closure.
- Conversion/manual visual review needs.
- Downstream validation and production-readiness support.
- Body-content support matrix separating `strong_support`, `partial_support`, `title_or_reference_only`, `not_supported_by_body_content`, and `evidence_gap`.

## Finding Rules

- If actual trial is exempted but rationale/approval is missing, mark `evidence_gap` or `open_gap`.
- If a referenced manufacturing trial report or attachment is missing, mark `open_gap`.
- If a report number, attachment name, or checklist row is present but the referenced body content was not read, mark `title_or_reference_only` or `partial_support`, not closed.
- If a template contains conclusion options but no selected state or supporting result is readable, mark `not_supported_by_body_content`.
- If checkboxes are decision evidence but not reliably represented in Markdown, mark `manual_visual_review_required`.
- If signature/date fields are blank in extracted text, mark `evidence_gap`.
- Do not close production readiness when final conclusion, attachment, and approvals are not verified.

## Required Outputs

- `stage_10_trial_production_baseline.md`
- `stage_10_check_items.md`
- `stage_10_findings.csv`
- `stage_10_traceability_matrix.csv`
- `stage_10_check_items_closure_matrix.csv`
- `stage_10_trial_production_content_audit.md`
- `stage_10_substantive_content_support_matrix.csv`
- `stage_10_trial_production_check_report.html`
