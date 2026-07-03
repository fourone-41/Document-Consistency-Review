---
name: dmr-mfg-sop-check-skill
description: Checks PT9L DMR / manufacturing SOP files under 03_Mfg_SOP. Use when auditing DMR, master record detail, PT9L-DMR01, manufacturing SOP, WI operation instructions, QI inspection instructions, process control plan, PFMEA, component list, BOM transfer, DHR readiness, or DHF-to-DMR traceability.
---

# DMR Manufacturing SOP Check Skill

## Mandatory General Skill

Before using this skill, load and follow:

- `D:\AI_0415\03DHF\skill\SKILL.md`

This means user-facing replies must end with the required `喵` heartbeat.

## Purpose

Audit PT9L DMR / manufacturing SOP files under `03_Mfg_SOP`.

DMR is the controlled manufacturing record set derived from DHF design outputs and shop-floor actual operation. The master record detail is the DMR order and file-list baseline.

## Core Principles

- Read `PT9L 主记录明细` first. Treat `PT9L-DMR01 V1.0` as the DMR sequence and completeness baseline.
- DMR must map back to DHF: Stage 02 design-transfer plan, Stage 09 design outputs/BOM/package/software/process outputs, Stage 10 trial-production DMR suitability criteria, Stage 11 validated configuration and claims, and Stage 03 risk controls where relevant.
- DMR must also map to shop-floor reality: process sequence, station method, material input, tooling/equipment, environment, inspection method, acceptance criteria, records, traceability, and release controls.
- Do not close a DMR item from a title, filename, document number, master-list row, or file existence alone. Close only from body content.
- Distinguish DMR from DHR. DMR defines controlled manufacturing instructions and records; DHR later proves a batch followed them.
- For high-risk Excel/image-heavy SOPs, require page/original review for diagrams, pictures, visual warnings, signatures, and checkbox/selection evidence.

## Required Inputs

- `PT9L_MD/03_Mfg_SOP` converted DMR folder.
- `PT9L_CHECK/02_RnD_DHF/09-设计输出` baseline, findings, and traceability outputs.
- `PT9L_CHECK/02_RnD_DHF/10-试产文件` baseline and substantive content matrix.
- `PT9L_CHECK/02_RnD_DHF/11-设计确认` baseline/content audit and substantive support matrix.
- Stage 03/04 evidence if checking risk/design-input closure in detail.

## Extract

- Master record identity, file number, version, effective date, rows, and approvals.
- Full master record file list: part/category, file name, file number, version, effective date, remarks.
- DMR document groups: WI operation instructions, QI inspection instructions, process control plan, PFMEA, component list, incoming/system procedures.
- Process route and station sequence.
- Material/component inputs and BOM links.
- Tooling/equipment/environment and calibration requirements.
- Operation method, key quality characteristics, acceptance criteria, and record outputs.
- PFMEA risks, RPNs, existing controls, recommended actions, and action results.
- Label, IFU, package, UDI, serial/lot and traceability controls.
- Document control evidence: signatures, dates, approvals, effective status.
- Conversion risks and page/original review needs.

## Check

- Master record completeness and document-control consistency.
- File presence and readability for every master-record row.
- DHF-to-DMR transfer: design outputs, BOM, software/target code, process/tooling, assembly, labels, IFU, packaging.
- Stage 10 DMR suitability criteria: design output rationality/suitability and DMR suitability/completeness.
- Stage 11 validated configuration: no narrowing of validated performance, labeling, software, safety, usability, and risk claims.
- Component list vs EBOM/ABOM/PBOM/package outputs.
- Process control plan coverage vs WI/QI rows.
- PFMEA-to-control closure in WI/QI/control plan.
- Special process controls: soldering, programming, grease/glue/coating, torque, calibration, label printing, packaging.
- Inspection coverage: incoming, in-process, main unit, finished goods, outgoing, visual, functional, electrical, accuracy, label/package.
- Records/DHR readiness.

## Finding Rules

- If a master-record row is listed but the file body is not located/read, mark `title_or_reference_only` or `open_gap`.
- If a DMR file exists but lacks body content for method, criteria, controls, records, or approvals, mark `partial` or `evidence_gap`.
- If DMR narrows or contradicts DHF outputs or validated configuration, mark `open_gap` or `critical`.
- If Stage 10 DMR suitability is not substantively closed, do not claim overall DMR readiness.
- If high-risk conversion is used for final decisions, mark `manual_original_review_required`.
- If PFMEA identifies a control but no WI/QI/control-plan implementation is found, mark `open_gap`.

## Required Outputs

- `dmr_mfg_sop_baseline.md`
- `dmr_check_items.md`
- `dmr_findings.csv`
- `dmr_dhf_traceability_matrix.csv`
- `dmr_check_items_closure_matrix.csv`
- `dmr_mfg_sop_check_report.html`

Optional deeper outputs:

- `dmr_master_file_presence_matrix.csv`
- `dmr_bom_transfer_matrix.csv`
- `dmr_pfmea_control_closure_matrix.csv`
- `dmr_wi_qi_group_audit.md`
- `dmr_dhr_record_readiness_matrix.csv`
