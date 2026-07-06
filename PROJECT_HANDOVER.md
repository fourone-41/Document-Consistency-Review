# 项目交接文档：文档一致性审查 / DHF-DMR 多智能体审查系统

> 交接日期：2026-07-06
> 当前主线：`m-agent/`
> 当前推荐入口：`m-agent/run_pt9l_full_audit_langgraph.py`
> 当前推荐输出：`magent-output/pt9l_full_audit_output_langgraph_v9/`
> 目标读者：接手开发/运行的技术同事，以及需要了解成果、风险和边界的项目/质量负责人。

## 1. 一句话概述

本项目用于对 PT9L DHF/DMR Markdown 文档进行一致性审查。当前推荐方案不是早期的固定流水线或模式匹配方案，而是 `m-agent` 下的动态多智能体审查系统：由 Orchestrator 调度多个 Agent 调用公司内部 GPT55 API 审查文档，经过证据门控、质询、最多 5 轮 Context Recovery 补证、Dedup/Grouping 问题归并，最后生成可人工审阅的中文 HTML 报告。

当前交接时应把 `m-agent` 视为主线。`file_extractor`、`schema`、历史输出目录和部分早期文档主要作为历史方案、参考资产或排查材料，不建议作为新的开发主线继续扩展。

## 2. 当前主线和历史方案边界

### 当前应继续维护的主线

| 位置 | 定位 |
|---|---|
| `m-agent/run_pt9l_full_audit_langgraph.py` | 当前全量审查主脚本。包含证据索引、Agent 调度、Challenge、Context Recovery、Dedup/Grouping、报告生成。 |
| `m-agent/agent_configs/*.yaml` | 每个 Agent 的角色、检索策略、输入 schema、输出 schema 和提示词规则。优先在这里改 Agent 行为。 |
| `m-agent/tests/test_v6_audit_semantics.py` | 当前主流程语义回归测试。改代码后先跑这里。 |
| `.codex/skills/dhf-dmr-report-writer/` | Report Agent 的报告写作规则沉淀，包括中文展示、原文证据、人工审阅、误前提修正等。 |
| `docs/superpowers/plans/2026-07-03-current-dhf-dmr-dynamic-agent-architecture.md` | 最新技术方案说明。注意该文件在部分终端里可能显示乱码，必要时以本交接文档和代码为准。 |
| `最新多智能体DHF-DMR流程架构可视化.html` | 架构可视化页面，面向演示和沟通。 |

### 关联但不建议作为主线扩展的模块

| 位置 | 当前建议 |
|---|---|
| `file_extractor/` | 早期图谱/关系抽取方案，包含 Step1-Step4、Neo4j、跨文档关系发现等。可以参考思路或旧实验结果，但不建议作为当前主线继续开发。 |
| `schema/` | 早期 LinkML/Pydantic schema 设计资产。可以参考节点/关系建模，但当前 `m-agent` 主线没有依赖它运行。 |
| `magent-output/pt9l_full_audit_output_langgraph_v5-v8/` | 历史审查输出，用于追溯演进，不建议作为当前结果对外交付。 |
| `magent-output/all_output.md`、根目录 `all_output.md`、`m-agent/all_output.md` | 历史结果汇总/迭代记录，阅读时注意版本和时间。 |
| `file_extractor/PROJECT_HANDOVER.md` | 早期 file_extractor 方案交接文档，其中一些环境/API示例可能已经过时，不应照搬到当前主线。 |

## 3. 仓库目录地图

```text
D:\项目文档一致性审查
├─ m-agent/                         当前主线代码
│  ├─ run_pt9l_full_audit_langgraph.py
│  ├─ agent_configs/
│  ├─ tests/test_v6_audit_semantics.py
│  └─ README.md / AGENT.md
├─ pt9l_markdown_output/             已转换为 Markdown 的 PT9L 文档输入
├─ magent-output/                    多轮审查输出目录
│  ├─ pt9l_full_audit_output_langgraph_v9/
│  ├─ pt9l_full_audit_output_langgraph_v5-v8/
│  └─ *.log / all_output.md
├─ .codex/skills/                    项目内 Codex 技能
│  └─ dhf-dmr-report-writer/
├─ docs/superpowers/plans/           技术方案和设计记录
├─ schema/                           早期 schema 资产
├─ file_extractor/                   早期图谱/关系抽取方案
└─ 最新多智能体DHF-DMR流程架构可视化.html
```

## 4. 当前架构

当前主流程以动态 Orchestrator 为核心，不是固定 workflow。简化链路如下：

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

更详细地说：

1. `bootstrap` 建立文档清单、PageIndex、参数实例、RelationIndex、证据工具命中等基础数据。
2. `Project Scout Agent` 建立项目画像，但不能只凭风险文件判断真实产品功能。
3. `Orchestrator / Task Router` 读取 `routing.yaml`、项目画像、历史 `agent_runs[]`、候选和补证状态，动态决定派发哪些 Agent。
4. `Candidate Discovery Agent` 只提出候选假设，不直接裁决问题真假。
5. 领域 Agent 包括 Regulatory、Hardware、Software、Risk Traceability、V&V、DMR/SOP。
6. `Evidence Gate` 检查 finding 是否有可追溯证据。
7. `Challenge Agent` 对 finding 做质询，输出 keep / revise / drop / needs_more_context / human_review。
8. `Context Recovery Agent` 对 `needs_more_context` 项进行最多 5 轮补证和复审，仍无法判断则进入人工复核。
9. `Dedup/Grouping Agent` 按问题组归并重复或重合 finding，重新判断组级严重等级。
10. `Report Agent` 生成中文、可审阅、可导出审阅结果的 HTML 报告。

关键原则：

- Orchestrator 只派任务，不确认或驳回 finding。
- Evidence Tools 只取证，不直接生成候选或错误。
- 只有 Orchestrator 动态派到的 Agent 才调用 LLM；一旦派到，必须真实调用 LLM，不读旧 Agent 输出缓存。
- Dedup/Grouping 和 Report 是后处理节点，不由 Orchestrator 当普通领域 Agent 动态派发。
- 报告中的 Agent 生成文本应中文展示；原文证据、路径、编号、标准名、型号可以保留原文。

## 5. Agent 配置说明

Agent 配置位于：

```text
m-agent/agent_configs/
```

当前主要配置文件：

| 文件 | 作用 |
|---|---|
| `project_scout.yaml` | 项目画像和产品功能边界确认规则。 |
| `orchestrator.yaml` | Orchestrator 角色、输入输出 schema。 |
| `routing.yaml` | 给 Orchestrator LLM 阅读的调度 policy，不是 Python 确定性路由表。 |
| `candidate_discovery.yaml` | 候选发现 Agent 规则。 |
| `regulatory.yaml` | 法规/文件控制审查 Agent。 |
| `hardware.yaml` | 硬件/参数一致性审查 Agent。 |
| `software.yaml` | 软件生命周期审查 Agent。 |
| `risk_traceability.yaml` | 风险追溯审查 Agent。 |
| `vv.yaml` | 验证确认审查 Agent。 |
| `dmr_sop.yaml` | DMR/SOP/BOM/图纸/工艺一致性审查 Agent。 |
| `challenge.yaml` | Challenge Agent 质询规则。 |
| `context_recovery.yaml` | Context Recovery 补证规则。 |
| `dedup_grouping.yaml` | 问题组归并、组级严重等级规则。 |
| `report.yaml` | Report Agent 输出规则。 |
| `report_corrections.yaml` | 人工修正规则，目前包含蓝牙错误前提修正。 |

后续如果只想改某个 Agent 的审查方式，优先改对应 YAML；只有需要改变运行机制、输出文件或节点连接时才改 Python 主脚本。

## 6. 环境准备

当前主脚本依赖 Python 和 OpenAI 兼容 SDK。建议使用已有的 Miniconda/Python 环境。

常用依赖：

```powershell
pip install openai httpx pyyaml python-dotenv langgraph pytest
```

`.env` 放在仓库根目录，不要提交到 Git。需要配置公司内部 GPT55 API，支持两套变量名：

```text
GPT55_API_KEY=通过公司安全渠道获取
GPT55_API_URL=公司内部 OpenAI-compatible base url
GPT55_MODEL=公司内部可用模型名
GPT55_DISABLE_SSL_VERIFY=false
```

或：

```text
OPENAI_API_KEY=通过公司安全渠道获取
OPENAI_BASE_URL=公司内部 OpenAI-compatible base url
OPENAI_MODEL=公司内部可用模型名
```

注意：

- 不要把 `.env`、API key、内部网关 token 写入交接文档或提交到仓库。
- 运行全量审查会把 PT9L 文档内容发送给公司内部 GPT55 API。
- 如果公司网络、证书或代理有变化，优先检查 `.env`、API URL、SSL 配置和网络策略。

## 7. 如何运行

以下命令在仓库根目录执行。

### 7.1 全量审查

```powershell
python -X utf8 m-agent\run_pt9l_full_audit_langgraph.py `
  --input pt9l_markdown_output `
  --output magent-output\pt9l_full_audit_output_langgraph_v9
```

全量审查会真实调用 LLM，耗时较长。当前会走到 Dedup/Grouping 和 Report。

### 7.2 只续跑 Context Recovery 之后的流程

```powershell
python -X utf8 m-agent\run_pt9l_full_audit_langgraph.py `
  --input pt9l_markdown_output `
  --output magent-output\pt9l_full_audit_output_langgraph_v9 `
  --resume-context-recovery
```

用途：

- 已经有 challenged findings；
- 想从 Context Recovery 继续补证；
- 补证后会继续跑 Dedup/Grouping 和 Report。

### 7.3 只基于已有 challenged findings 重跑分组报告

```powershell
python -X utf8 m-agent\run_pt9l_full_audit_langgraph.py `
  --output magent-output\pt9l_full_audit_output_langgraph_v9 `
  --offline-dedup-report
```

注意：这个命令也会调用 Dedup/Grouping LLM。它不是“只刷新 HTML”。如果只想用已有 `grouping_results.json` 重新渲染 HTML，需要单独写轻量脚本或补一个不调用 LLM 的参数。

### 7.4 跑测试

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py -q
python -X utf8 -m py_compile m-agent\run_pt9l_full_audit_langgraph.py
```

最近一次验证结果：`41 passed, 1 warning`。warning 是 pytest cache 写入权限问题，不是测试失败。

## 8. 当前 v9 输出看哪里

推荐先看这几个文件：

| 输出 | 用途 |
|---|---|
| `magent-output/pt9l_full_audit_output_langgraph_v9/08_reports/grouped-findings-review.html` | 当前最重要的人审报告。按问题组展示，可勾选、备注、导入导出审阅结果。 |
| `magent-output/pt9l_full_audit_output_langgraph_v9/15_dedup_grouping/grouping_results.json` | Dedup/Grouping 后的结构化问题组结果。 |
| `magent-output/pt9l_full_audit_output_langgraph_v9/07_findings/grouped_findings.jsonl` | 每行一个问题组，便于脚本处理。 |
| `magent-output/pt9l_full_audit_output_langgraph_v9/08_reports/run_summary_full_langgraph.json` | 本轮运行摘要。 |
| `magent-output/pt9l_full_audit_output_langgraph_v9/05_agent_notes/agent_runs.jsonl` | 每次 Orchestrator 派发后的 Agent 运行记录。 |
| `magent-output/pt9l_full_audit_output_langgraph_v9/10_task_packages/orchestrator_route_plans.json` | Orchestrator 每轮 route_plan。 |
| `magent-output/pt9l_full_audit_output_langgraph_v9/14_context_recovery/context_recovery_results.jsonl` | Context Recovery 补证结果。 |
| `magent-output/pt9l_v9_run_stdout.log` / `pt9l_v9_run_stderr.log` | v9 全量运行日志。 |
| `magent-output/pt9l_v9_resume_context_stdout.log` / `pt9l_v9_resume_context_stderr.log` | v9 resume 运行日志。 |

历史输出 `v5-v8` 只用于追溯演进，不作为当前正式交付结果。

## 9. HTML 报告审阅方式

打开：

```text
magent-output/pt9l_full_audit_output_langgraph_v9/08_reports/grouped-findings-review.html
```

报告特点：

- 以“问题组”为主，不是简单罗列单条 finding。
- 每个问题组下面保留原始 finding、来源 Agent、严重等级、复审状态和原文证据。
- 每组旁边有人工审阅选项：未审阅、确认问题、误报、待补证、暂缓。
- 可填写人工备注。
- 浏览器 `localStorage` 自动保存本机审阅状态。
- 可导出 `human-review-decisions.json`，用于跨机器或归档。
- 可导入审阅 JSON 恢复人工审阅状态。

审阅注意：

- localStorage 只保存在当前浏览器和当前机器；正式交接或归档必须导出 JSON。
- 原文证据和路径保持原样，不翻译，以便追溯。
- 除原文证据和路径外，报告页面上的 Agent 生成说明应使用中文。
- 报告仍是审查候选结果，不等于质量最终结论；所有高风险问题必须人工确认。

## 10. 已知关键问题和风险

### 10.1 全量审查慢

慢主要来自多轮 LLM 调用：

- Project Scout 调用；
- Orchestrator 动态派发；
- 被派发的 Candidate/领域 Agent 调用；
- Challenge 调用；
- Context Recovery 最多 5 轮；
- Dedup/Grouping 分批调用。

如果只是看重复项收束效果，优先用 `--offline-dedup-report`。如果只是调整报告样式，最好新增“只重渲染 HTML”的脚本或参数，避免重新调用 Dedup LLM。

### 10.2 输出仍需人工复核

当前系统可以提高发现和归并效率，但不能替代最终质量判断。重点风险：

- Agent 可能基于不完整上下文形成误判。
- Dedup/Grouping 可能把相似但整改动作不同的问题合并，或没有合并应合并的问题。
- 组级严重等级是辅助判断，最终仍需质量/法规人员确认。
- HTML 人工审阅状态默认在本地浏览器保存，不导出就无法交接。

### 10.3 蓝牙问题是重要修正案例

曾经报告中出现过“PT9L 具备蓝牙功能，但缺少专项危害分析与验证关闭证据”的结论。用户人工确认后，PT9L 实际没有蓝牙功能。因此现在规则应理解为：

- 不能只凭风险文件中的一句蓝牙描述确认 PT9L 有蓝牙功能。
- 设计输入、验证计划、验证报告等权威产品定义文件优先。
- 风险文件中出现 PT9L/PT3SBT 蓝牙句子时，应报告为“风险文件范围冲突、旧型号残留或模板残留”，而不是“PT9L 蓝牙验证缺口”。

相关沉淀位置：

```text
m-agent/agent_configs/project_scout.yaml
m-agent/agent_configs/report_corrections.yaml
.codex/skills/dhf-dmr-report-writer/SKILL.md
```

### 10.4 旧方案不要误当主线

`file_extractor` 和 `schema` 中有早期大量设计，但当前已经转向 `m-agent` 多智能体审查。接手同事如果继续开发，应优先从 `m-agent` 走，不建议回到：

- 纯模式匹配决定候选；
- 固定 workflow 线性审查；
- Neo4j 图谱作为主审查入口；
- file_extractor Step1-Step4 作为当前正式主流程。

### 10.5 文档编码显示

部分旧 Markdown 在终端里会显示乱码，通常是历史写入、控制台编码或路径字符造成。当前新写文件建议：

```powershell
python -X utf8 ...
```

代码里读写文件统一使用 UTF-8。

## 11. 修改指南

### 改某个 Agent 的判断规则

优先改：

```text
m-agent/agent_configs/<agent>.yaml
```

例如：

- 改硬件参数一致性：`hardware.yaml`
- 改风险追溯：`risk_traceability.yaml`
- 改 DMR/SOP：`dmr_sop.yaml`
- 改质询逻辑：`challenge.yaml`
- 改补证策略：`context_recovery.yaml`
- 改报告语言/字段要求：`report.yaml` 和 `.codex/skills/dhf-dmr-report-writer/SKILL.md`

### 改 Orchestrator 调度规则

优先改：

```text
m-agent/agent_configs/routing.yaml
m-agent/agent_configs/orchestrator.yaml
```

注意：`routing.yaml` 是给 Orchestrator LLM 阅读的 policy package，不应在 Python 里把它变成机械确定性路由表。

### 改主流程节点、文件输出或 CLI 参数

改：

```text
m-agent/run_pt9l_full_audit_langgraph.py
```

改完至少运行：

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py -q
python -X utf8 -m py_compile m-agent\run_pt9l_full_audit_langgraph.py
```

### 改报告展示

相关函数主要在主脚本里：

- `write_grouped_findings_html`
- `group_title_for_html`
- `group_claim_for_html`
- `group_rationale_for_html`
- `chinese_original_finding_statement`
- `chinese_original_finding_rationale`
- `apply_report_corrections`

相关规则沉淀在：

```text
.codex/skills/dhf-dmr-report-writer/SKILL.md
m-agent/agent_configs/report.yaml
m-agent/agent_configs/report_corrections.yaml
```

## 12. 推荐后续工作

### P0：先稳定交付和审阅

1. 用 `grouped-findings-review.html` 做一次人工审阅，导出 `human-review-decisions.json`。
2. 人工标记明显误报、待补证、确认问题。
3. 根据人工审阅结果继续补充 `report_corrections.yaml`。
4. 如果报告页面仍有英文 Agent 生成文本，继续沉淀到 Report Agent/skill 和 HTML 渲染逻辑。

### P1：减少重跑成本

1. 新增“只用已有 `grouping_results.json` 重渲染 HTML”的参数或脚本。
2. 将 Dedup/Grouping 的 batch 大小、重试和失败 fallback 做成更清晰配置。
3. 在日志里更明确显示当前卡在哪个 Agent / 哪个 batch / 哪一轮 Context Recovery。

### P2：拆分主脚本

当前 `run_pt9l_full_audit_langgraph.py` 已经很大。稳定后可以考虑拆分为：

- `evidence_tools.py`
- `agent_runtime.py`
- `orchestrator.py`
- `context_recovery.py`
- `dedup_grouping.py`
- `report_writer.py`
- `cli.py`

但不要为了“好看”先拆；建议在测试覆盖稳定后再拆。

### P3：提高审查质量

1. 建立人工 gold set，用确认结果评估误报和漏报。
2. 针对高频误报继续补充 Project Scout、Challenge、Report Correction 规则。
3. 让 Context Recovery 更明确地区分“缺什么证据”和“证据已经否定原前提”。
4. 保持 Candidate Discovery 为 Agent-led，不回退到机械词表决定候选。

## 13. 接手第一天建议流程

1. 先阅读本文件。
2. 打开 `最新多智能体DHF-DMR流程架构可视化.html` 理解总体架构。
3. 阅读 `m-agent/README.md` 和 `m-agent/AGENT.md`，但以当前主脚本和本交接文档为准。
4. 打开 `m-agent/run_pt9l_full_audit_langgraph.py`，重点看：
   - `FullAuditState`
   - `build_graph`
   - `call_orchestrator_route_plan`
   - `execute_agent_assignment`
   - `context_recovery_node`
   - `dedup_grouping_node`
   - `report_node`
5. 打开 `m-agent/agent_configs/routing.yaml` 和各 Agent YAML。
6. 跑测试：

```powershell
python -X utf8 -m pytest m-agent\tests\test_v6_audit_semantics.py -q
```

7. 打开当前报告：

```text
magent-output/pt9l_full_audit_output_langgraph_v9/08_reports/grouped-findings-review.html
```

8. 不要一上来重跑全量审查。先确认 `.env`、API、输出目录、当前报告诉求，再决定是否重跑。

## 14. 交接提醒

- `.env` 不应进入 Git。API key 通过公司安全渠道交接。
- 当前 v9 报告是审查候选，不是最终质量结论。
- 接手人应优先维护 `m-agent`，不要把 `file_extractor` 或 `schema` 当作当前正式流程。
- 如果要对外展示，优先展示架构 HTML 和 `grouped-findings-review.html`，并说明结果需要人工复核。
- 如果要继续开发，先写/改测试，再改主脚本或配置。
