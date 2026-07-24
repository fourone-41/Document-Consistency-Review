# Extraction Quality Recovery Skill

## Purpose

对全量抽取中的失败文件、空抽取文件、JSON 解析失败、LLM 输出异常和长文档漏抽进行恢复，保证每份文档都有可解释状态。

## Inputs

- `extractions/` 抽取结果目录。
- `raw_errors/` 原始错误输出。
- recovery manifest。
- LLM raw response。
- 文档源文件。

## Outputs

- `recovery_manifest.json`
- 补跑后的 extraction JSON。
- failed / partial 文件清单。
- 失败原因统计。

## Failure Types

常见失败类型：

- LLM 超时。
- API 限流或余额不足。
- 输出不是 JSON。
- JSON 被截断。
- 文档过长导致 chunk 漏抽。
- Excel/表格结构丢失。
- OCR 或转换乱码。
- schema validation 失败。

## Workflow

1. 扫描 `extractions/`，统计 ok/partial/failed/missing。
2. 扫描 `raw_errors/`，识别失败原因。
3. 对 JSON 格式错误尝试 repair。
4. 对截断输出重新按更小 chunk 补跑。
5. 对规则性长表优先用规则抽取。
6. 对多次失败文件标记为 needs_manual_review。
7. 更新 recovery manifest。

## Current Project Paths

```text
_convert/company_full_run/extractions/
_convert/company_full_run/raw_errors/
_convert/company_full_run/recovery_manifest.json
```

## Quality Metrics

至少统计：

- total_documents
- ok_documents
- partial_documents
- failed_documents
- missing_documents
- nodes_total
- edges_total
- avg_nodes_per_document
- documents_with_no_edges

## Guardrails

- 不要因为 raw JSON repair 成功就默认语义正确。
- 不要覆盖原始 raw response。
- 每次补跑必须可追溯到原始文件和 chunk。
- 对失败文件要保留失败原因，而不是只说 failed。
