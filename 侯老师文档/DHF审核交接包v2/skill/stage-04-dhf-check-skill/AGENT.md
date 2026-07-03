# Stage 04 DHF Design Input Check Agent

## Agent Name

`stage-04-dhf-check-agent`

## Purpose

This agent audits Stage 04 design input evidence and builds the design-input baseline used by verification, DFMEA, validation, labeling, IFU, packaging, and regulatory checks.

## Required Reading

Before acting, read and follow:

- `D:/AI_0415/03DHF/skill/stage-04-dhf-check-skill/SKILL.md`
- Stage 01/02/03 check items and baseline files.
- QP-7.3 procedure evidence when checking procedure compliance.

## Required Inputs

- Original product root.
- Converted evidence root.
- Check output root.
- Stage 01, Stage 02, and Stage 03 check output folders.
- Stage 04 converted design input folder.
- QP-7.3 converted procedure path.

## Mandatory Workflow

1. Confirm product model and Stage 04 folder.
2. Read existing check outputs before overwriting.
3. Read Stage 04 cover, design input summary, review plan, review checklist, review record, and assets.
4. Extract product identity, document numbers, design input parts, requirements, standards, review criteria, review conclusions, signatures, and conversion quality.
5. Build or update `stage_04_check_items.md`.
6. Check Stage 01/02/03 carry-forward into Stage 04.
7. Check the non-narrowing principle: each design input must be greater than or equal to the source customer requirement, applicable regulation/standard, and risk-control requirement.
8. If item-level proof is missing, mark it as `needs_item_level_matrix`.
9. Check requirement verifiability and internal consistency.
10. Check Stage 04 downstream closure path to Stage 08 and Stage 11.
11. Write baseline, findings CSV, traceability matrix CSV, closure matrix CSV, and Chinese HTML report.
12. Verify report readability and absence of destructive mojibake.

## Status Reporting

For long checks, report:

- evidence being read;
- baseline fields extracted;
- check item coverage;
- carry-forward checks completed;
- downstream closure checks completed;
- findings by severity;
- next action.
