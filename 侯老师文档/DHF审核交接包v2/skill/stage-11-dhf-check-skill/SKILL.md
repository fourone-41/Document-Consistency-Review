# Stage 11 DHF Check Skill - Design Validation

## Purpose

Audit Stage 11 design validation / design confirmation for final DHF readiness.

Core principles:

- Stage 11 proves the completed design is finally confirmed.
- Always check Stage 11 against Stage 02, Stage 04, Stage 03, and Stage 09.
- Do not close Stage 11 from one report or file presence. Use combined evidence.
- Verification/validation conclusions must be closed by report body content. Do not accept file titles, filenames, document numbers, report lists, checklist rows, or summary references as evidence unless the referenced body content has been read.
- External test reports often exclude clauses. Every exclusion must be covered by separate evidence or a justified non-applicability decision.
- Stage 11 must validate the released design output; version mismatches are critical gaps.

## Required Inputs

- Stage 02 development plan baseline and traceability matrix.
- Stage 03 risk baseline/check package.
- Stage 04 design input baseline/check package.
- Stage 09 design output baseline/check package.
- Stage 11 converted folder, including user field test, clinical study, software validation, usability evidence, design validation reports, review records, regulatory sheets, external test reports, and conversion manifests.

## Extract

- Evidence inventory and product identity.
- Stage 02 design-validation required outputs.
- Stage 04 design input validation targets.
- Stage 03 risk-control and residual-risk validation targets.
- Stage 09 released design outputs and versions.
- User field test scope, configuration, participants, and conclusion.
- Clinical study population, method, bias, repeatability, and conclusion.
- Software validation documents, software version, target code, and conclusion.
- Usability/human factors file, IEC 62366/60601-1-6 checklist results, summative evaluation.
- General validation and regulatory standard sheets.
- External test report identifiers, pass scope, and exclusions.
- Final cover conclusion, review records, signatures, dates, approvals.
- Conversion risks and page/original review needs.
- Substantive body-content support for each validation claim: product identity/configuration, objective, method/sample/setup, acceptance criteria, actual result, conclusion, exclusions/limitations, and approval evidence.

## Check

- Stage 02 plan match.
- Stage 04 input non-narrowing and final validation coverage.
- Stage 03 risk management/residual-risk closure.
- Stage 09 output-version consistency.
- User field test closure.
- Clinical study closure.
- Software validation closure.
- Usability closure.
- Electrical safety, EMC, clinical thermometer standard, label/IFU, biocompatibility, environment, packaging closure.
- External report exclusion coverage.
- Final design-validation conclusion and approval closure.
- Conversion/manual review needs.
- Final DHF readiness.
- Body-content support classification separating `strong_support`, `partial_support`, `title_or_reference_only`, `weak_support`, `not_supported_by_body_content`, and `evidence_gap`.

## Finding Rules

- If Stage 02 planned evidence is missing or only indirectly referenced, mark `partially_closed` or `needs_evidence_link`.
- If Stage 03 risk report is referenced but not present/readable, mark `evidence_gap`.
- If a report number, title, checklist row, or summary table says a requirement passed but the supporting report body has not been read, mark `title_or_reference_only` or `partial_support`, not closed.
- If Stage 09 output versions do not match Stage 11 validated versions, mark `open_gap`.
- If an external report excludes a clause, do not close that clause unless separate evidence covers it.
- If final conclusion or signatures are checkbox/image based and not reliably represented in Markdown, mark `manual_visual_review_required` or `evidence_gap`.
- Do not claim final DHF closure while critical gaps remain.

## Required Outputs

- `stage_11_design_validation_baseline.md`
- `stage_11_check_items.md`
- `stage_11_findings.csv`
- `stage_11_traceability_matrix.csv`
- `stage_11_check_items_closure_matrix.csv`
- `stage_11_report_content_audit.md`
- `stage_11_substantive_content_support_matrix.csv`
- `stage_11_design_validation_check_report.html`
