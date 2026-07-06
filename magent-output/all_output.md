# magent-output 结果目录索引

> 用途：集中索引当前仓库中与 PT9L DHF/DMR 多智能体审查相关的输出结果、报告、日志和交接材料。
>
> 当前建议：优先看 v9 分组审阅报告；v5-v8 只作为历史对比和回溯材料。

## 1. 当前推荐结果：v9

| 类型 | 路径 | 说明 |
|---|---|---|
| 人工审阅主报告 | `pt9l_full_audit_output_langgraph_v9/08_reports/grouped-findings-review.html` | 当前最适合打开审阅的结果页；按问题组展示，包含原文证据、人工勾选、备注、导入/导出审阅结果。 |
| 分组结果 JSON | `pt9l_full_audit_output_langgraph_v9/15_dedup_grouping/grouping_results.json` | Dedup/Grouping Agent 的结构化输出；90 条原始确认问题收束为 61 个问题组。 |
| 分组 finding 明细 | `pt9l_full_audit_output_langgraph_v9/07_findings/grouped_findings.jsonl` | 分组后的 finding 明细，便于脚本继续处理。 |
| 全量运行摘要 | `pt9l_full_audit_output_langgraph_v9/08_reports/run_summary_full_langgraph.json` | v9 全量审查的统计口径来源。 |
| Markdown 全量报告 | `pt9l_full_audit_output_langgraph_v9/08_reports/PT9L_full_audit_report_langgraph.md` | 未分组前的 Markdown 审查报告。 |
| 高优先级语义问题 | `pt9l_full_audit_output_langgraph_v9/08_reports/PT9L_high_priority_semantic_findings.md` | 高优先级语义问题摘录。 |
| 二轮任务记录 | `pt9l_full_audit_output_langgraph_v9/08_reports/second_round_tasks.md` | 二轮复核或补证任务说明。 |

## 2. v9 关键统计

| 指标 | 数值 |
|---|---:|
| 审查文档数 | 470 |
| PageIndex 段落数 | 4,222 |
| 参数实例数 | 12,168 |
| RelationIndex 节点数 | 4,000 |
| RelationIndex 边数 | 189 |
| 证据工具命中数 | 366 |
| Agent 运行记录数 | 13 |
| Orchestrator 派发计划数 | 4 |
| LLM 语义 finding 数 | 98 |
| Challenge 后保留/修订数 | 90 |
| Context Recovery 处理数 | 29 |
| Context Recovery 确认数 | 25 |
| Context Recovery 驳回数 | 4 |
| 当前确认问题数 | 90 |
| 分组后问题组数 | 61 |
| 多 finding 合并组数 | 15 |
| 人工修正组数 | 1 |

## 3. v9 调度、补证与日志

| 类型 | 路径 | 说明 |
|---|---|---|
| Agent 运行总账 | `pt9l_full_audit_output_langgraph_v9/05_agent_notes/agent_runs.jsonl` | 每次 Orchestrator 派发后追加一条 Agent 运行记录。 |
| 单次 Agent 运行目录 | `pt9l_full_audit_output_langgraph_v9/05_agent_notes/agent_runs/` | RUN-0001 到 RUN-0013 的单次运行 JSON。 |
| Orchestrator 路由计划 | `pt9l_full_audit_output_langgraph_v9/10_task_packages/orchestrator_route_plans.json` | Orchestrator 动态生成的派发路线记录。 |
| Context Recovery 结果 | `pt9l_full_audit_output_langgraph_v9/14_context_recovery/context_recovery_results.jsonl` | needs_more_context 后的补证与复审结果。 |
| v9 全量运行 stdout | `pt9l_v9_run_stdout.log` | 全量审查标准输出日志。 |
| v9 全量运行 stderr | `pt9l_v9_run_stderr.log` | 全量审查错误/警告日志。 |
| v9 补证续跑 stdout | `pt9l_v9_resume_context_stdout.log` | Context Recovery 续跑输出日志。 |
| v9 补证续跑 stderr | `pt9l_v9_resume_context_stderr.log` | Context Recovery 续跑错误/警告日志。 |

## 4. 历史结果目录

| 版本 | 路径 | 当前定位 |
|---|---|---|
| v5 | `pt9l_full_audit_output_langgraph_v5/` | 早期 LangGraph 审查结果；保留用于对比旧统计、旧 finding 和旧报告。 |
| v6 | `pt9l_full_audit_output_langgraph_v6/` | 含 `audit-results.html`、`all-results-review.html`、`technical-route.html` 等旧版可视化结果。 |
| v7 | `pt9l_full_audit_output_langgraph_v7/` | 中间迭代结果；可用于比较证据门和二轮审查变化。 |
| v8 | `pt9l_full_audit_output_langgraph_v8/` | v9 前一版全量审查结果；可用于比较动态 Orchestrator 调整前后的差异。 |
| v9 | `pt9l_full_audit_output_langgraph_v9/` | 当前推荐版本；以后继续迭代时建议以此为基线。 |

## 5. 交接和技术说明材料

| 类型 | 路径 | 说明 |
|---|---|---|
| 项目交接文档 | `../PROJECT_HANDOVER.md` | 面向接手同事的项目总览、目录说明、运行方式和风险边界。 |
| 最新技术方案 | `../docs/superpowers/plans/2026-07-03-current-dhf-dmr-dynamic-agent-architecture.md` | 当前动态 Orchestrator、多 Agent、报告生成与分组审阅方案说明。 |
| 架构可视化网页 | `../最新多智能体DHF-DMR流程架构可视化.html` | 面向沟通展示的整体流程图和 Agent 调度关系。 |
| file_extractor 交接 | `../file_extractor/PROJECT_HANDOVER.md` | 旧方案/关联模块交接说明；当前主线不以该模块为核心。 |
| schema 配置 | `../schema/schema.yaml` | 旧方案或关联模块中的结构定义材料；保留为参考。 |

## 6. 当前阅读顺序

1. 打开 `pt9l_full_audit_output_langgraph_v9/08_reports/grouped-findings-review.html`，先看问题组和原文证据。
2. 如需核对统计口径，查看 `pt9l_full_audit_output_langgraph_v9/08_reports/run_summary_full_langgraph.json`。
3. 如需追踪重复项如何合并，查看 `pt9l_full_audit_output_langgraph_v9/15_dedup_grouping/grouping_results.json`。
4. 如需解释系统方案，查看 `../PROJECT_HANDOVER.md` 和 `../最新多智能体DHF-DMR流程架构可视化.html`。
5. 如需复盘历史演进，再看 v5-v8 目录。

## 7. 注意事项

- v9 分组审阅报告是当前主要交付物，但结果仍属于候选审查输出，需要人工确认后才能作为正式质量结论。
- `grouped-findings-review.html` 的人工勾选和备注默认保存在浏览器 localStorage；交接时应使用页面内导出功能保存 JSON。
- 报告正文除原文证据、路径、编号、标准名、型号名外，应尽量保持中文展示，便于人工审阅。
- 历史 v5-v8 不建议继续作为主结果引用，除非用于对比或追溯。
- 不要把 API Key、`.env` 或其他敏感配置写入报告和索引。
