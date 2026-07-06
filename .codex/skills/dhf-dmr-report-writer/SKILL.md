---
name: dhf-dmr-report-writer
description: Use when writing, regenerating, reviewing, or correcting DHF/DMR audit reports for this repository, especially grouped finding reports, PT9L audit outputs, Report Agent work, Chinese report text, dedup/grouping, original evidence display, manual corrections, false-premise fixes, and traceable issue-group presentation.
---

# DHF/DMR Report Writer

Use this skill when producing final or intermediate audit reports from agent findings. The report is not just a pretty view: it is the final reviewer interface, so it must preserve traceability and make incorrect upstream assumptions visible.

## Report Contract

Always write report-generated text in 简体中文. Keep only these items as original text when needed: source document excerpts, file paths, finding IDs, product model names, document numbers, standards, and regulatory names.

Agent 原始英文输出不作为页面正文展示. If original finding `claim`, `rationale`, `challenge_reason`, root cause, impact, or recommended action is produced by an Agent, render a Chinese reviewer-facing statement instead. Preserve the raw Agent output only in machine-readable intermediate artifacts when needed; the HTML review page should show Chinese generated text plus original file evidence.

## 中文显示边界

The report viewer is for Chinese human review. 除了原文件内容和路径，其他报告页面文字都必须用简体中文。

允许原样保留:

- 原文件证据摘录: `actual_text`, `source_text`, table row text, copied source sentences
- 文件路径、文件名、行号
- finding ID, group ID, document number, drawing number, version, product model
- standards and regulation names such as ISO 14971, IEC 62366-1, FDA, MDR
- controlled document titles when the title itself is the evidence

必须中文化:

- group title, group claim, group rationale
- root cause, impact, recommended action
- original finding display text
- agent names and review status labels when shown to humans
- merge decision, challenge decision, correction decision
- toolbar, filters, counters, export/import labels, error messages
- manual review options and notes labels

禁止在 HTML 正文展示:

- Agent 原始英文 `claim`
- Agent 原始英文 `rationale`
- Agent 原始英文 `challenge_reason`
- Agent 原始英文 root cause, impact, recommended action
- hidden full grouped JSON that lets browser search expose the above English text

For each original finding shown in HTML, render a Chinese review-facing block:

- `问题陈述`: one Chinese sentence explaining what the finding means
- `判断依据`: one Chinese sentence explaining what evidence count/source should be reviewed
- `原文证据`: source excerpts remain unchanged and traceable

If a Chinese translation is uncertain, do not expose the English Agent paragraph as a fallback. Use a conservative Chinese placeholder such as `待人工补充` or `请以下方原文件证据为准复核`.

Prefer 问题组 first, 原始 finding second:

1. Show one consolidated issue group as the primary record.
2. Hang all related 原始 finding under that group.
3. Merge exact duplicates and near duplicates.
4. Keep materially different issues separate even if they share a broad topic.
5. Rejudge group-level severity from the group-level risk, not by blindly copying the highest source severity.

Every group must include:

- 中文 group title
- 中文 group claim
- group severity
- merge or correction decision
- group rationale
- root cause, impact, and recommended action when available
- all member finding IDs
- original finding details under the group
- evidence paths and 原文证据 excerpts

## Evidence Rules

Reports must show the actual source text that supports or corrects a conclusion. Do not summarize away evidence that a human reviewer needs to audit.

For each original finding, show:

- finding ID
- source agent
- original severity and status
- Chinese problem statement and Chinese rationale derived from the original finding
- evidence rel_path and line
- actual_text or source_text

For a manual correction, add a clearly labeled `人工修正原文证据` block before original findings. Include the exact original lines that changed the conclusion, such as design input rows, verification rows, risk report lines, or conflicting model/function statements.

## False-Premise Guard

不可只凭单一上游假设确认报告结论. When a finding depends on a product feature, project scope, market, model identity, applicable standard, or controlled version, check whether authoritative boundary evidence supports that premise.

Authoritative function or scope evidence should come from design input, user manual, software requirements/design, labeling, DMR controlled records, or other controlled product-definition documents. Risk files alone can raise a candidate issue, but they must not by themselves define the true product feature set.

If authoritative scope evidence conflicts with an upstream assumption:

1. Do not present the assumption-driven finding as confirmed.
2. Create or update an issue group as 人工修正 or human-review correction.
3. Preserve the original findings under that group.
4. Show the counter-evidence source text.
5. Rewrite the group claim around the actual issue, such as scope conflict, legacy/template residue, or unresolved evidence.

Example pattern:

- Bad: `PT9L has Bluetooth, but Bluetooth verification is missing.`
- Better: `设计输入和验证文件显示PT9L蓝牙不适用；风险文件出现PT9L/PT3SBT蓝牙句子，应报告为风险文件范围冲突或旧型号残留。`

## Grouping Rules

Use a group when findings share the same root issue, not merely the same keyword.

Merge:

- same evidence location and same claim
- same document-control defect across agents
- same model/document-number conflict expressed by multiple agents
- same missing approval/signature pattern in the same document family

Keep separate:

- same broad topic but different documents and different corrective actions
- one issue about feature existence and another about verification closure
- risk traceability gap vs DMR part-number gap
- suspected false premise vs confirmed document-control residue

When in doubt, keep separate unless a human reviewer would naturally fix them with one corrective action.

## Manual Corrections

Use manual corrections for reviewer-confirmed report errors or false premises. A manual correction should never erase history.

A correction group must:

- be clearly titled with `人工修正`
- list the original findings it replaces or reframes
- explain why the old conclusion is wrong or overstated
- show the exact counter-evidence lines
- preserve all original findings under the group
- keep output JSON/HTML traceable

Use a stable correction ID such as `MANUAL-BT-001`.

## HTML Review Page

The HTML report should be easy to audit:

- issue-group cards first
- compact top statistics
- per-group 人工审阅 controls with statuses: 未审阅, 确认问题, 误报, 待补证, 暂缓
- browser-side localStorage autosave for human review decisions
- JSON 导出/导入 for human review decisions, preserving group_id, group_title, group_severity, member_finding_ids, note, and updated_at
- visible 审阅进度 summary so reviewers can see reviewed, confirmed, false-positive, evidence-needed, and deferred counts
- visible severity label
- group claim near the title
- details/summary sections for original findings
- highlighted manual evidence blocks
- no nested cards
- no mojibake or replacement characters

Before delivery, verify:

- grouped JSON exists
- grouped JSONL exists
- HTML exists
- all generated headings are Chinese
- 人工审阅 controls appear for each issue group
- localStorage autosave, JSON export, JSON import, and clear-review controls are present
- `人工修正原文证据` appears when manual corrections exist
- source text is present in HTML, not only in embedded JSON
