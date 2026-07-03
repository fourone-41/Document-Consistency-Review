# Stage 09 DHF Check Skill - Design Output

## Purpose

Audit Stage 09 `design output` for DHF/DMR readiness.

Core principles:

- Stage 09 is design output, not trial production.
- Always read Stage 02 development plan baseline first and map its design-output/design-transfer expectations to Stage 09 evidence.
- Stage 09 outputs must be greater than or equal to Stage 04 design inputs, Stage 05 structural outputs, Stage 06 hardware outputs, Stage 07 software outputs, and Stage 08 verified/deferred T1 evidence.
- Output-list presence is not enough. Listed files must exist, be controlled, have identifiers/versions, and be traceable.
- Reused/reference outputs from other product families require controlled reuse/equivalence rationale.

## Required Inputs

- Stage 02 development plan baseline and traceability matrix.
- Stage 04 design-input baseline/check outputs.
- Stage 05 structural baseline/check outputs.
- Stage 06 hardware baseline/check outputs.
- Stage 07 software baseline/check outputs.
- Stage 08 T1 baseline/check outputs.
- Stage 09 converted folder, including design output list 1, design output list 2, BOMs, drawings, package/label files, and conversion manifests.

## Extract

- Evidence inventory and product identity.
- Stage 02 planned outputs relevant to design output/design transfer.
- Design output list 1 hardware/software outputs.
- Design output list 2 structure, assembly, packaging, label, and BOM outputs.
- EBOM and ABOM key components, ROHS status, importance levels, ratios, material codes.
- Document numbers, versions, reference document numbers, blank identifiers, reused references.
- Signature/date/approval fields.
- CAD/DWG/PDF conversion quality and manual review needs.

## Check

- Stage 02 plan match.
- Output list completeness.
- Document-number/version control.
- Listed file existence.
- Non-narrowing against Stages 04 to 08.
- Reuse/equivalence rationale for referenced outputs.
- EBOM and ABOM adequacy.
- Packaging and labeling output adequacy.
- Signature and release approval completeness.
- CAD/DWG/PDF readability.
- Downstream DMR/design-transfer readiness.

## Finding Rules

- If Stage 02 planned design-transfer output is not present or not traceable, mark `partially_closed` or `open_gap`.
- If a listed output is only a reused/reference document, mark `needs_reuse_rationale` unless controlled equivalence evidence is present.
- If DWG/CAD evidence cannot be converted, mark `manual_original_review_required`.
- If signatures/dates are absent in extracted text, mark `evidence_gap` pending original/page review.
- Do not claim DMR review or trial-production closure from Stage 09 alone.

## Required Outputs

- `stage_09_design_output_baseline.md`
- `stage_09_check_items.md`
- `stage_09_findings.csv`
- `stage_09_traceability_matrix.csv`
- `stage_09_check_items_closure_matrix.csv`
- `stage_09_design_output_check_report.html`
