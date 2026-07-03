---
name: stage-08-dhf-check-skill
description: Checks Stage 08 T1 prototype verification evidence for design verification plan/report coverage, software test evidence, DFMEA/risk verification, BOM/label/packaging/transport/biocompatibility evidence, T1 review closure, conversion risks, and downstream design-confirmation boundaries.
---

# Stage 08 DHF T1 Prototype Verification Check Skill

## Purpose

Use this skill for Stage 08 T1 prototype verification audits.

Stage 08 verifies applicable Stage 04 design inputs and Stage 05/06/07 design outputs at T1. It must distinguish:

- items closed by T1 evidence;
- items supported but needing source/original review;
- items intentionally deferred to design confirmation, regulatory evidence, Stage 09/10/11/12/13, or validation.

Core principle: Stage 08 verification evidence must be greater than or equal to the planned T1 verification scope. Do not claim T1 closure for requirements that the plan assigns to later stages.

Stage 02 plan matching principle: before concluding Stage 08, read the Stage 02 development plan baseline. The T1 stage must be checked against Stage 02 planned outputs, responsibilities, review requirements, verification activities, approval requirements, and schedule control. If Stage 02 requires an inspection standard, verification plan, IFU draft, package draft, software test, or T1 verification, Stage 08 must provide corresponding evidence, a test conclusion, or a controlled evaluation/deferred closure path.

## Required Inputs

- Stage 04 design input baseline and traceability.
- Stage 02 development plan baseline, especially the T1/hand-sample planned outputs and downstream control notes.
- Stage 05 structural baseline and findings.
- Stage 06 hardware baseline and findings.
- Stage 07 software baseline and findings.
- Stage 08 verification plans, verification reports, software tests, DFMEA, inspection standard/report, life/battery reports, label/packaging/BOM evidence, transport/biocompatibility evidence, T1 review plan/checklist/record, assets, and conversion-loss files.

## Required Extraction Content

Extract evidence inventory, verification plan items, verification report results, software version, software test equipment and results, DFMEA categories, referenced reports, T1 review checklist items, T1 review conclusion, signatures/dates, and conversion risks.

## Required Checks

Check file completeness, identity, plan-to-report coverage, T1/later-stage boundary, Stage 04/05/06/07 verification closure, risk-control and DFMEA linkage, function/performance/component/general verification adequacy, software test evidence, T1 review closure, signatures, conversion/manual review needs, and downstream closure.
Also check Stage 02 development-plan matching: each planned T1 output and control requirement must map to Stage 08 evidence or a justified downstream closure path.

## Finding Rules

- Treat verification report rows as only partially closed if their referenced source record is missing, blank, unsigned, or conversion-risky.
- Treat a missing Stage 02 planned T1 output as `open_gap` unless there is a controlled evaluation, approved non-applicability rationale, or downstream closure path.
- Treat items assigned to design confirmation as `pending_downstream_check`, not T1 closed.
- Treat high-risk Excel/PDF/image evidence as `manual_visual_review_required`.
- Treat blank T1 review conclusions, signatures, or dates as `evidence_gap`.
- Treat DFMEA/risk closure as partial unless risk/DFMEA items map directly to verification evidence.

## Required Outputs

- `stage_08_t1_baseline.md`
- `stage_08_check_items.md`
- `stage_08_findings.csv`
- `stage_08_traceability_matrix.csv`
- `stage_08_check_items_closure_matrix.csv`
- `stage_08_t1_check_report.html`
