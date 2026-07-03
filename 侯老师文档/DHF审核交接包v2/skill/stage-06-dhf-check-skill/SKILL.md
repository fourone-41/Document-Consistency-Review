---
name: stage-06-dhf-check-skill
description: Checks Stage 06 DHF hardware scheme and hardware drawing evidence for design-input carry-forward, risk-control carry-forward, power/battery, sensor, LCD/backlight/buttons, PCB drawing adequacy, structural cooperation, manufacturability, review adequacy, conversion risks, and downstream closure.
---

# Stage 06 DHF Hardware Check Skill

## Purpose

Use this skill for Stage 06 hardware scheme and hardware drawing audits.

Stage 06 converts Stage 04 design inputs, Stage 03 risk controls, and Stage 05 structural constraints into hardware design outputs.

Core principle: Stage 06 hardware outputs must be greater than or equal to source requirements. They must not narrow Stage 04 inputs, Stage 03 risk controls, or Stage 05 structural constraints without controlled rationale.

## Required Inputs

- Stage 04 design input baseline, findings, and traceability.
- Stage 03 risk findings when hardware controls are relevant.
- Stage 05 structural baseline when PCB/structure fit is relevant.
- Stage 06 hardware scheme, review plans, checklists, records, assets, and conversion-loss files.

## Required Extraction Content

Extract identity, hardware architecture, MCU, power, battery, low-voltage detection, sensor/ADC, LCD/backlight, buttons, programming, PCB drawing checks, structural cooperation, manufacturing/panelization checks, review conclusions, signatures, dates, and conversion risks.

## Required Checks

Check file completeness, identity, sub-stage separation, Stage 04 carry-forward, non-narrowing, hardware scheme adequacy, power/battery adequacy, sensor measurement support, UI hardware support, PCB drawing adequacy, structural cooperation, manufacturability, risk-control carry-forward, review plan/record adequacy, signatures, conversion risks, and downstream closure.

## Finding Rules

- Treat high-risk Excel and embedded images as `manual_visual_review_required`.
- Treat signatures/dates as `evidence_gap` unless original/page evidence proves approval.
- Treat EMC/electrical safety links as partial unless explicitly mapped.
- Treat non-narrowing as open unless item-level source-to-output comparison exists.
- Treat downstream closure as pending until Stage 07, Stage 08, EMC/electrical safety, and DFMEA evidence are checked.

## Required Outputs

- `stage_06_hardware_baseline.md`
- `stage_06_check_items.md`
- `stage_06_findings.csv`
- `stage_06_traceability_matrix.csv`
- `stage_06_check_items_closure_matrix.csv`
- `stage_06_hardware_check_report.html`
