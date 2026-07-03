---
name: stage-07-dhf-check-skill
description: Checks Stage 07 DHF software quality planning, software requirements, software design scheme, and software flowchart evidence for design-input carry-forward, risk-control carry-forward, hardware interface consistency, non-narrowing, configuration management, review adequacy, image/checkbox conversion risks, and downstream software verification closure.
---

# Stage 07 DHF Software Check Skill

## Purpose

Use this skill for Stage 07 software audits.

Stage 07 converts Stage 04 software-related design inputs, Stage 03 software-related risk controls, and Stage 06 hardware interfaces into software quality planning, SRS, software design scheme, and software flowcharts.

Core principle: Stage 07 outputs must be greater than or equal to source requirements. SRS must not narrow Stage 04 or Stage 03; software design must not narrow SRS; flowcharts must not narrow software design.

## Required Inputs

- Stage 04 design input baseline and traceability.
- Stage 03 risk findings and traceability.
- Stage 06 hardware baseline and interface evidence.
- Stage 07 quality planning, SRS, software design scheme, flowchart, review plans, checklists, records, assets, and conversion-loss files.

## Required Extraction Content

Extract lifecycle plan, validation/test planning, configuration management, problem reporting, SRS functions, performance links, inputs/outputs, errors, thresholds, safety requirements, runtime environment, design functions, pin/interface mapping, risk-reduction measures, flowchart coverage, review conclusions, signatures, dates, and conversion risks.

## Required Checks

Check file completeness, identity, four sub-stage control, Stage 04 carry-forward, Stage 03 risk carry-forward, Stage 06 interface carry-forward, non-narrowing, quality planning adequacy, configuration management, SRS adequacy, internal consistency, software design adequacy, hardware/software interface adequacy, flowchart adequacy, review adequacy, signatures, conversion risks, and Stage 08 software verification closure.

## Finding Rules

- Treat image-based flowcharts as `manual_visual_review_required` until visually reviewed.
- Treat checkbox-heavy review sheets as requiring page/original review.
- Treat missing review conclusions, signatures, or dates as `evidence_gap`.
- Treat memory/storage and MCU naming contradictions as `open_gap` until explained.
- Treat non-narrowing as open unless item-level source-to-output comparison exists.
- Treat downstream verification as pending until Stage 08 software tests are checked.

## Required Outputs

- `stage_07_software_baseline.md`
- `stage_07_check_items.md`
- `stage_07_findings.csv`
- `stage_07_traceability_matrix.csv`
- `stage_07_check_items_closure_matrix.csv`
- `stage_07_software_check_report.html`
