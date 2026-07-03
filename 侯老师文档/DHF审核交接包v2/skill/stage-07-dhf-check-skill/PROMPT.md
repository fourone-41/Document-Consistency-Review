# Stage 07 DHF Check Prompt Template

Use the `stage-07-dhf-check-skill`.

Audit PT9L Stage 07 software evidence.

Rules:

- Define extraction items and check items first.
- Treat quality planning, SRS, software design scheme, and software flowchart as four controlled sub-stages.
- Check that SRS is greater than or equal to Stage 04 inputs and Stage 03 software risks.
- Check that software design is greater than or equal to SRS.
- Check that software flowcharts are greater than or equal to software design.
- Check Stage 06 hardware interface consistency.
- Flag EEPROM/storage and MCU naming inconsistencies.
- Require visual review for flowchart images and checkbox-heavy review sheets.
- Generate baseline, findings, traceability, closure matrix, and HTML report.
