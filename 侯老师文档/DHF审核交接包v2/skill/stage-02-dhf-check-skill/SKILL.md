---
name: stage-02-dhf-check-skill
description: Checks Stage 02 DHF development plan evidence for project team list, design and development plan, review record, schedule, document numbers, personnel consistency, stage applicability, QP-7.3 compliance, and relationship traceability. Use when auditing 02 development plan folders, QR-7.3-03, QR-7.3-04, project team list, development plan, project schedule, plan review, DHF stage relationships, or PT9L_CHECK Stage 02 outputs.
---

# Stage 02 DHF Check Skill

## Purpose

Use this skill for the Stage 02 DHF development-plan content audit.

Stage 02 checks whether the project team, development plan, plan review, and project schedule form a consistent planning baseline for later DHF/DMR stages.

Stage 02 also creates the downstream control baseline:

- the project team list fixes personnel and roles for later reviews, plans, approvals, and responsibility fields;
- the development plan table defines what each later stage must do, including required tasks, outputs, responsibilities, reviews, verification/validation activities, and approvals;
- the project schedule defines the time plan and milestone traceability that each later stage should follow.

## Required Inputs

Read before concluding:

- Stage 01 to Stage 02 link check table:
  - `D:/AI_0415/03DHF/PT9L_CHECK/stage_01_02_link_check_items.md`
  - `D:/AI_0415/03DHF/PT9L_CHECK/stage_01_02_link_check_items.csv`
- Converted Stage 02 Word Markdown files.
- Excel plan assets: sheet CSV/Markdown, text object manifest, page visual evidence, semantic findings, and conversion loss report.
- PDF schedule assets: ordered text, native text, page PNG, visual evidence manifest, semantic findings, and metadata.
- QP-7.3 procedure evidence for project team list and design development plan requirements.
- Stage 01 baseline when checking product identity and regulatory path consistency.

## Required Extraction Content

Extract:

- product model, project number, product/project name;
- document numbers and revisions from cover, headers, footers, and manifests;
- project leader, technical leader, professional engineers, certification, resource, customer, and transfer/import roles;
- design stages, applicability statements, outputs, responsibilities, interfaces, resources, review requirements, and schedule links;
- plan review participants, review criteria, review conclusion, signatures, and dates;
- project progress tasks, milestones, dependencies, and metadata.
- downstream control mappings from Stage 02 to later stages, for example T1 planned outputs, responsible roles, review requirements, verification work, and schedule coverage.

## Required Checks

For each Stage 02 folder, check:

- Stage 01 to Stage 02 carry-forward using `stage_01_02_link_check_items`.
- QR-7.3-03 project team list exists and is consistent with review participants.
- QR-7.3-04 design development plan exists and covers QP-7.3 required content: stages, work content, outputs, quality/responsibility, personnel/resources, authority, interfaces, schedule, review, and document control.
- cover file list matches actual files and document numbers.
- project leader and technical leader are consistent across all Stage 02 records.
- stage applicability is clear and does not conflict with later DHF folders or planned outputs.
- plan review covers all required review criteria and has conclusion, signatures, and dates.
- project schedule supports the plan and does not contain wrong-model metadata or template residue.
- later stages can trace back to Stage 02 controls:
  - personnel should match the fixed project team or have approved change evidence;
  - stage files should satisfy the tasks and outputs planned in the development plan table;
  - stage timing should have coverage in the project schedule or a documented schedule change.

## Finding Rules

- Do not mark missing until Word headers/footers, Excel text objects, PDF page images, and manifests are checked.
- Treat blank signatures/dates as `evidence_gap` unless page visuals prove they are present.
- Treat internal comments or shape text in released forms as `needs_explanation`.
- When finding an issue, include the expected requirement, observed evidence, status, source evidence, and recommended action.
- If a finding is caused by a plausible template reuse or historical regulatory path, mark `needs_explanation` rather than guessing nonconformance.

## Required Outputs

Under the mirrored Stage 02 check folder, create or update:

- `stage_02_development_plan_baseline.md`
- `stage_02_relationship_check_report.html`
- `stage_02_findings.csv`
- `stage_02_traceability_matrix.csv`

The traceability matrix must include control-baseline relationships for:

- project team list to later stage personnel;
- development plan table to later stage tasks and outputs;
- project schedule to later stage timing and milestones.

## Reuse For Other Models

For other product types or sales regions, keep the same Stage 02 structure. Change only the regulatory-path checks that depend on product type and market. The QP-7.3 planning checks still apply.
