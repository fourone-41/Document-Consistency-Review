# Node And Relation Extraction Skill

## Purpose

按已确认 schema 从文档中抽取节点、关系和证据，生成可导入知识图谱的结构化 JSON。

## Inputs

- 最新 schema YAML 和 `models.py`。
- 文档 Markdown/JSON。
- LLM 配置。
- 可选：文档类型 profile。

## Outputs

- 每份文档一个抽取 JSON。
- extraction manifest。
- raw response 备份。
- extraction summary。

## Recommended Output Contract

每份文档至少包含：

```json
{
  "document": {
    "source_path": "string",
    "display_name": "string",
    "doc_type": "string"
  },
  "nodes": [
    {
      "id": "local id",
      "label": "Risk | Test | Claim | SoftwareItem | ReviewItem",
      "name": "string",
      "properties": {},
      "evidence": []
    }
  ],
  "edges": [
    {
      "source": "local id",
      "target": "local id",
      "type": "RELATION_TYPE",
      "confidence": "strong | candidate | weak",
      "evidence": []
    }
  ],
  "status": "ok | partial | failed"
}
```

## Workflow

1. 按文档长度切 chunk，保留文档名、章节、页码或段落索引。
2. 给 LLM 提供完整 schema 约束，而不是让模型自由发明类型。
3. 每个 chunk 抽取局部节点/关系。
4. 文档内做局部去重，保留 local id。
5. 合并 chunk 输出，保存 raw response。
6. 对输出做 schema validation。
7. 标记 failed / partial，不允许静默跳过。

## Long Document Strategy

对规律性强、很长的文档，优先加规则抽取：

- 表格型风险清单。
- 测试记录。
- 标签审核表。
- BOM/物料表。
- 设计开发计划表。

规则抽取与 LLM 抽取可以共存：

```text
rule extraction -> deterministic nodes
LLM extraction -> long-tail nodes/relations
merge -> validation
```

## Guardrails

- 不要只按少数 schema 抽取导致文档信息不全。
- 不要让 LLM 自造关系类型。
- Claim 必须保留原文表述和证据位置。
- 关系置信度必须区分 strong/candidate/weak。
- 跨文档聚合不在本阶段做，只在后续 canonical merge 做。
