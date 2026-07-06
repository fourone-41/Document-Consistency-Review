# 项目文档一致性审查交接说明

本仓库用于对医疗器械项目文档进行一致性审查。当前主线是 `m-agent/` 下的 PT9L DHF/DMR 多智能体审查系统：它以 Markdown 化后的项目文档为输入，构建 PageIndex、参数实例、RelationIndex 等证据底座，再由 Orchestrator 动态派发多个领域 Agent 调用公司内部 GPT55/OpenAI-compatible API 完成候选发现、领域复审、证据质询、上下文补证、重复项归并和中文审阅报告生成。

当前最推荐的接手入口是：

- 主脚本：[m-agent/run_pt9l_full_audit_langgraph.py](m-agent/run_pt9l_full_audit_langgraph.py)
- Agent 配置：[m-agent/agent_configs/](m-agent/agent_configs)
- 最新技术方案：[docs/superpowers/plans/2026-07-03-current-dhf-dmr-dynamic-agent-architecture.md](docs/superpowers/plans/2026-07-03-current-dhf-dmr-dynamic-agent-architecture.md)
- 交接文档：[PROJECT_HANDOVER.md](PROJECT_HANDOVER.md)
- v9 结果索引：[magent-output/all_output.md](magent-output/all_output.md)
- 当前推荐审阅报告：`magent-output/pt9l_full_audit_output_langgraph_v9/08_reports/grouped-findings-review.html`

## 当前主线

当前应继续维护的是 `m-agent/`，不要再把早期 `file_extractor/` 或 `schema/` 当作主流程扩展。它们保留为历史方案、参考资产和排查材料。

主流程可以概括为：

```text
bootstrap
  -> Project Scout Agent
  -> Orchestrator dynamic dispatch loop
  -> Evidence Gate
  -> Challenge Agent
  -> Context Recovery
  -> Dedup/Grouping Agent
  -> Report Agent
```

关键设计边界：

- Orchestrator 只负责动态派发任务，不直接确认或驳回 finding。
- Evidence Tools 只负责取证，不直接决定候选或错误。
- Candidate Discovery Agent 只提出候选假设，问题是否成立交给领域 Agent、Challenge 和 Context Recovery 判断。
- 只有 Orchestrator 派到的 Agent 才真实调用 LLM；一旦派到，不读取旧 Agent 输出缓存。
- Dedup/Grouping 和 Report 是后处理节点，不由 Orchestrator 当普通领域 Agent 动态派发。

## 目录说明

| 路径 | 说明 |
|---|---|
| `m-agent/` | 当前主线，多智能体 DHF/DMR 一致性审查代码、配置、测试和技术文档。 |
| `m-agent/agent_configs/` | 每个 Agent 一个 YAML，包含角色、检索策略、输入 schema、输出 schema 和提示规则。 |
| `m-agent/tests/` | 当前主流程回归测试。 |
| `magent-output/pt9l_full_audit_output_langgraph_v9/` | 当前建议作为交接基线的 v9 审查输出。 |
| `magent-output/all_output.md` | 当前结果目录索引。 |
| `.codex/skills/dhf-dmr-report-writer/` | Report Agent 写报告相关规则沉淀，包括中文展示、原文证据、聚类、人工审阅和误前提修正。 |
| `docs/superpowers/plans/` | 技术方案、演进计划和架构说明。 |
| `file_extractor/` | 早期关系抽取/图谱方案，当前不作为主线。 |
| `schema/` | 早期 schema 设计资产，当前不作为主线运行依赖。 |
| `verification/` | 早期验证和报告生成脚本，作为参考保留。 |
| `pt9l_markdown_output/` | PT9L 输入文档的 Markdown 转换结果，体量较大，当前 `.gitignore` 默认不纳入提交。 |
| `data/` | 原始或中间数据目录，当前 `.gitignore` 默认不纳入提交。 |

## 环境准备

建议使用 Python 3.10+。依赖可以按需安装：

```powershell
pip install openai httpx pyyaml python-dotenv langgraph pytest
```

根目录需要本地 `.env`，但不要提交到 Git。常用环境变量如下：

```text
GPT55_API_KEY=通过公司安全渠道获取
GPT55_API_URL=公司内部 OpenAI-compatible base url
GPT55_MODEL=公司内部可用模型名
GPT55_DISABLE_SSL_VERIFY=false
```

也支持 OpenAI-compatible 命名：

```text
OPENAI_API_KEY=通过公司安全渠道获取
OPENAI_BASE_URL=公司内部 OpenAI-compatible base url
OPENAI_MODEL=公司内部可用模型名
```

## 常用命令

在仓库根目录执行。

全量审查：

```powershell
python -X utf8 m-agent\run_pt9l_full_audit_langgraph.py `
  --input pt9l_markdown_output `
  --output magent-output\pt9l_full_audit_output_langgraph_v9
```

从 Context Recovery 之后继续：

```powershell
python -X utf8 m-agent\run_pt9l_full_audit_langgraph.py `
  --input pt9l_markdown_output `
  --output magent-output\pt9l_full_audit_output_langgraph_v9 `
  --resume-context-recovery
```

基于已有 challenged findings 重跑离线分组报告：

```powershell
python -X utf8 m-agent\run_pt9l_full_audit_langgraph.py `
  --output magent-output\pt9l_full_audit_output_langgraph_v9 `
  --offline-dedup-report
```

测试与语法检查：

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py -q
python -X utf8 -m py_compile m-agent\run_pt9l_full_audit_langgraph.py
```

## v9 结果摘要

v9 是当前建议作为交接基线的结果版本。统计来源主要是：

- `magent-output/pt9l_full_audit_output_langgraph_v9/08_reports/run_summary_full_langgraph.json`
- `magent-output/pt9l_full_audit_output_langgraph_v9/15_dedup_grouping/grouping_results.json`

核心统计：

| 指标 | 数值 |
|---|---:|
| 输入 Markdown 文档数 | 470 |
| PageIndex 段落数 | 4,222 |
| 参数实例数 | 12,168 |
| RelationIndex 节点数 | 4,000 |
| RelationIndex 边数 | 189 |
| Evidence tool hits | 366 |
| Agent 真实运行次数 | 13 |
| Orchestrator route plans | 4 |
| LLM semantic findings | 98 |
| Challenge 后 keep | 55 |
| Challenge 后 revise | 35 |
| Challenge 后 drop | 8 |
| keep/revise 后确认问题 | 90 |
| Context Recovery 任务数 | 29 |
| Context Recovery confirm | 25 |
| Context Recovery dismiss | 4 |
| Dedup/Grouping 后问题组数 | 61 |
| 多 finding 合并组数 | 15 |
| 人工修正组数 | 1 |

当前最适合给人工审阅的页面是：

```text
magent-output/pt9l_full_audit_output_langgraph_v9/08_reports/grouped-findings-review.html
```

该页面支持按问题组审阅、查看原文证据、人工勾选判断、填写备注、使用浏览器 localStorage 保存状态，并导出/导入 `human-review-decisions.json`。

## 已知重要修正

v9 中沉淀了一个重要误前提修正：PT9L 没有蓝牙功能。早期报告曾把风险文件中的蓝牙/旧型号残留解释为“PT9L 具备蓝牙但缺少验证证据”。现在的正确处理是：

- 不能仅凭风险文件中的一句蓝牙描述确认 PT9L 具备蓝牙功能。
- 设计输入、说明书、软件需求、设计验证计划/报告等权威产品定义文件优先。
- 如风险文件中出现 PT9L/PT3SBT 蓝牙描述，应优先视为风险文件范围冲突、模板残留或旧型号残留，而不是 PT9L 蓝牙验证缺口。

相关配置和规则沉淀在：

- `m-agent/agent_configs/project_scout.yaml`
- `m-agent/agent_configs/report_corrections.yaml`
- `.codex/skills/dhf-dmr-report-writer/SKILL.md`

## 后续维护建议

优先级建议：

1. 先用 `grouped-findings-review.html` 做一次人工审阅，并导出 `human-review-decisions.json`。
2. 把确认的误报、待补证项和规则修正继续沉淀到 `report_corrections.yaml` 和 Report Agent skill。
3. 新增“只基于已有 grouping_results.json 重新渲染 HTML”的轻量入口，避免每次调报告样式都重跑 Dedup LLM。
4. 继续完善日志，让运行中能更清楚看到当前卡在哪个 Agent、哪个 batch、哪一轮 Context Recovery。
5. 主脚本稳定后再拆分模块，不建议为了拆分而拆分。

## 上传边界

本次交接上传按以下边界处理：

- 不提交 `.env`。
- 不提交临时日志，例如 `*.log`、`*_log.txt`、`*_err.txt`。
- 不提交同事仓库副本 `lyt_part/`。
- 保留代码、配置、技术文档、交接文档、v9 关键结果和可审阅 HTML。

如果后续需要提交新的运行结果，建议先确认其中是否包含敏感原文、API 响应或内部路径，再决定是否进入远程仓库。
