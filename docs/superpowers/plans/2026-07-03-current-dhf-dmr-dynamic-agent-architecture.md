# DHF/DMR 多智能体一致性审查最新技术方案

> 更新日期：2026-07-03
> 适用代码：`m-agent/run_pt9l_full_audit_langgraph.py`
> 架构可视化：`最新多智能体DHF-DMR流程架构可视化.html`

## 1. 方案定位

本方案描述当前 PT9L DHF/DMR 一致性审查系统的最新技术形态。核心变化是：系统不再把审查过程设计成固定顺序的机械 workflow，而是以 Orchestrator 为调度中心，由大模型动态决定下一步应调用哪些 Agent、需要补哪些证据、哪些结果进入人工复核。

当前方案的目标是：

- 保持高召回：不依赖机械词表决定候选问题。
- 保持可追溯：所有问题必须挂回原始 finding、证据路径和原文摘录。
- 保持动态调度：Orchestrator 读取项目画像、候选、历史 agent_runs 和路由策略后生成 route_plan。
- 保持可审阅：最终报告按问题组展示，支持人工勾选、备注、本地保存和 JSON 导出/导入。
- 保持报告可读：除原文件证据和路径外，报告页面中的 Agent 生成文字必须使用简体中文。

## 2. 当前总体架构

当前架构由三类能力组成：

1. 共享证据基础设施
   - `PageIndex`
   - `Relation Index`
   - `Full-text Search`
   - `File Reader`
   - `SSOT Parameters`

2. 大模型 Agent
   - `Project Scout Agent`
   - `Orchestrator / Task Router`
   - `Candidate Discovery Agent`
   - `Regulatory Agent`
   - `Hardware Agent`
   - `Software Agent`
   - `Risk Traceability Agent`
   - `V&V Agent`
   - `DMR/SOP Agent`
   - `Evidence Gate + Challenge Agent`
   - `Context Recovery Agent`
   - `Dedup/Grouping Agent`
   - `Report Agent`

3. 报告与人工审阅层
   - grouped finding JSON
   - grouped finding HTML
   - manual correction
   - browser localStorage
   - review decision JSON export/import

简化调度关系如下：

```text
Project Scout Agent
        |
        v
Evidence Tools <-> Orchestrator / Task Router <-> Candidate Discovery Agent
 PageIndex              ^       |
 RelationIndex          |       v
 Full-text              |   Candidate Hypotheses
 File Reader            |
        |               v
        |   Regulatory / Hardware / Software / Risk / V&V / DMR Agents
        |               |
        |               v
        |     Evidence Gate + Challenge Agent
        |               |
        |     confirm / dismiss / needs_more_context
        |               |
        |               +--> Dedup/Grouping Agent --> Report Agent
        |
        v
Context Recovery Agent
        |
        v
回到 Orchestrator 重新派发
```

这里的重点是：Evidence Tools 是取证能力，不直接裁决；Candidate Discovery Agent 只提出候选假设，不直接形成最终问题；Orchestrator 负责动态派发；领域 Agent 和 Challenge/Context Recovery 才负责把候选逐步变成可确认、可驳回或需人工复核的结果。

## 3. 动态 Orchestrator 调度机制

### 3.1 Orchestrator 的职责

Orchestrator 不是普通 workflow 节点，而是任务路由中心。它读取以下输入：

- `routing.yaml` 中的调度策略
- Project Scout 输出的项目画像
- 可用 Agent 列表
- 历史 `agent_runs`
- Candidate Discovery 结果
- Context Recovery 结果
- 必查矩阵覆盖状态

然后返回严格 JSON 格式的 `route_plan`，决定：

- 是否继续调度
- 调哪些 Agent
- 每个 Agent 的任务类型
- 每个任务的 review focus
- 需要哪些证据策略
- 哪些事项进入 human_review

### 3.2 Orchestrator 不做的事情

Orchestrator 只做路由，不做事实裁决：

- 不确认 finding。
- 不驳回 finding。
- 不直接生成最终问题。
- 不把工具命中结果当成 finding。
- 不执行固定硬编码路由。

### 3.3 LLM 调用规则

当前规则是：

- 只有 Orchestrator 动态派到的 Agent 才调用。
- 一旦派到 Agent，就必须真实调用 LLM。
- 被派到的 Agent 不读取旧 agent-output 缓存。
- 每次派发都会追加一条 `agent_runs[]` 运行记录。
- Orchestrator 会读取历史 `agent_runs[]`，避免重复派发或盲目继续。

相关产物：

- `05_agent_notes/agent_runs.jsonl`
- `05_agent_notes/agent_runs/RUN-xxxx_*.json`
- `10_task_packages/orchestrator_route_plans.json`

## 4. Agent 配置拆分

为便于后续修改，每个 Agent 的角色、检索策略、输入 schema、输出 schema 已拆到独立 YAML 文件中。

配置目录：

```text
m-agent/agent_configs/
```

当前主要配置：

```text
project_scout.yaml
orchestrator.yaml
routing.yaml
candidate_discovery.yaml
regulatory.yaml
hardware.yaml
software.yaml
risk_traceability.yaml
vv.yaml
dmr_sop.yaml
challenge.yaml
context_recovery.yaml
dedup_grouping.yaml
report.yaml
report_corrections.yaml
```

其中：

- `orchestrator.yaml` 定义 Orchestrator 的输入输出和动态派发职责。
- `routing.yaml` 不是代码路由表，而是给 Orchestrator LLM 读取的 policy package。
- 各领域 Agent YAML 定义其审查目标、检索策略和输出 schema。
- `dedup_grouping.yaml` 定义分组去重 Agent 的分组合并规则。
- `report.yaml` 定义 Report Agent 和报告输出规则。

## 5. Project Scout Agent

Project Scout Agent 负责建立项目画像，但必须避免把单个风险文件中的文字误当作产品真实功能。

当前已加入的关键约束是：

- 项目功能边界必须来自权威产品定义文件。
- 风险文件可以提出候选问题，但不能单独定义产品功能。
- 如果风险文件声称某功能存在，而设计输入、验证计划、验证报告显示不适用，应标记为范围冲突、模板残留或旧型号残留。

这一规则来自蓝牙问题的修正：PT9L 实际不具备蓝牙功能，风险文件中的 PT9L/PT3SBT 蓝牙句子应作为风险文件范围冲突或旧型号残留处理，而不是作为“PT9L 蓝牙功能缺少验证”的确认问题。

## 6. Candidate Discovery Agent

Candidate Discovery Agent 替代原先的机械词表候选发现思路。

当前原则是：

- 不由模式匹配工具决定候选。
- Candidate Discovery Agent 可以调用 PageIndex、RelationIndex、全文检索和文件读取取证。
- 候选假设必须回到 Orchestrator，由 Orchestrator 分配给合适的领域 Agent。
- Candidate Discovery Agent 不直接裁决问题真假。

候选输出统一写入：

```text
07_findings/candidate_discovery_results.jsonl
```

候选通常包含：

- candidate id
- candidate type
- claim
- evidence refs
- recommended agent
- review status

## 7. 领域 Agent 审查层

领域 Agent 包括：

- Regulatory Agent
- Hardware Agent
- Software Agent
- Risk Traceability Agent
- V&V Agent
- DMR/SOP Agent

Orchestrator 可按阶段轴和维度轴派发任务。当前 `routing.yaml` 中保留了必查矩阵，用于确保逻辑检查项不丢失：

- 设计输入到设计输出的参数一致性
- 风险到验证的追溯闭环
- 软件生命周期追溯
- DMR 链条一致性
- 全阶段文件控制完整性

领域 Agent 的输出不直接进入最终报告，而是先进入 Evidence Gate 和 Challenge 校验。

## 8. Evidence Gate 与 Challenge Agent

Evidence Gate + Challenge Agent 负责对 Agent 输出进行证据门控和反向质询。

核心判断结果包括：

- `confirm`
- `dismiss`
- `needs_more_context`
- `human_review`

如果 Challenge 后仍然是 `needs_more_context`，则进入 Context Recovery 循环。

## 9. Context Recovery 五轮补证循环

Context Recovery 的设计目标不是“把 prompt 加长再重跑”，而是每轮结构化判断缺什么证据，再由 Orchestrator 重新派发。

每一轮包含：

1. Context Recovery Agent 判断缺口类型。
2. Orchestrator 根据缺口重新选择 Agent。
3. 被派发 Agent 调用 PageIndex、全文检索、文件读取等能力补证。
4. 领域 Agent 再次复审。
5. 如果仍无法判断，进入下一轮。

最多 5 轮。5 轮后仍无法判断，则进入 `human_review`。

相关产物：

```text
14_context_recovery/context_recovery_tasks.json
14_context_recovery/context_recovery_results.jsonl
```

## 10. Dedup/Grouping Agent

Dedup/Grouping Agent 是新加入的问题归并层，位于 Challenge/Context Recovery 之后、Report Agent 之前。

它的职责是：

- 合并完全重复或近似重复 finding。
- 将同一根因的问题归为一个问题组。
- 对每个问题组重新判断组级严重等级。
- 保留所有原始 finding ID。
- 保留所有原始 finding 详情。
- 不新增事实指控。
- 不因为“话题类似”就强行合并。

合并原则：

- 同一证据位置、同一问题陈述：可合并。
- 同一文件控制缺陷被多个 Agent 提出：可合并。
- 同一型号/文件编号冲突由多个 Agent 发现：可合并。
- 同一主题但不同文件、不同整改动作：保持分开。

当前实现状态：

- 已实现离线分组报告入口。
- 已生成 v9 分组报告。
- 后续可将其正式接入全量审查主流程。

离线运行命令：

```powershell
python m-agent\run_pt9l_full_audit_langgraph.py --output magent-output\pt9l_full_audit_output_langgraph_v9 --offline-dedup-report
```

注意：该命令会调用 Dedup/Grouping LLM。如果只需要用已有 `grouping_results.json` 重新渲染 HTML，则不应使用该命令。

主要产物：

```text
15_dedup_grouping/grouping_candidates.json
15_dedup_grouping/grouping_results.json
07_findings/grouped_findings.jsonl
08_reports/grouped-findings-review.html
```

## 11. Report Agent

Report Agent 负责把分组后的 finding 生成为可审阅报告。

它绑定项目内 skill：

```text
.codex/skills/dhf-dmr-report-writer/SKILL.md
```

报告必须满足以下要求：

- 问题组优先展示。
- 每组下挂多个原始 finding。
- 原始 finding 不丢失。
- 原文证据必须展示。
- 人工修正必须可见。
- 组级严重等级必须独立判断。
- 除原文件证据和路径外，报告页面文字必须使用简体中文。
- Agent 原始英文 claim/rationale 不作为 HTML 正文展示。

### 11.1 中文显示边界

允许原样保留：

- 原文件证据摘录
- 文件路径、文件名、行号
- finding ID / group ID
- 文档编号、图号、版本号
- 产品型号
- 标准和法规名称
- 作为证据的受控文件标题

必须中文化：

- group title
- group claim
- group rationale
- root cause
- impact
- recommended action
- original finding 页面展示文字
- Agent 名称和状态标签
- 按钮、筛选器、导入导出提示
- 人工审阅选项

禁止在 HTML 正文展示：

- Agent 原始英文 claim
- Agent 原始英文 rationale
- Agent 原始英文 challenge_reason
- Agent 原始英文 root cause / impact / recommended action
- 会让浏览器搜索暴露英文正文的完整 hidden grouped JSON

### 11.2 人工审阅交互

当前 HTML 报告支持：

- 每个问题组旁边人工审阅：
  - 未审阅
  - 确认问题
  - 误报
  - 待补证
  - 暂缓
- 人工备注。
- 浏览器 localStorage 自动保存。
- JSON 导出审阅结果。
- JSON 导入审阅结果。
- 清空本页审阅状态。
- 审阅进度统计。

导出文件名：

```text
human-review-decisions.json
```

## 12. Manual Correction 机制

Manual Correction 用于处理人工确认的报告错误或错误前提。

当前典型案例是蓝牙问题：

- 原始报告中多个 finding 以“PT9L 具备蓝牙功能”为前提。
- 人工复核后确认 PT9L 没有蓝牙功能。
- 设计输入、设计验证计划、设计验证报告均显示蓝牙相关项不适用。
- 风险文件中的 PT9L/PT3SBT 蓝牙句子应归为范围冲突、模板残留或旧型号残留。

对应配置：

```text
m-agent/agent_configs/report_corrections.yaml
```

Manual Correction 不能删除原始 finding，而是将其重新归组，并保留：

- 原始 finding ID
- 原始 finding 详情
- 人工修正标题
- 修正理由
- 反证原文
- 建议整改动作

## 13. 运行方式

### 13.1 全量审查

```powershell
python m-agent\run_pt9l_full_audit_langgraph.py --input pt9l_markdown_output --output magent-output\pt9l_full_audit_output_langgraph_v9
```

全量审查会执行：

- bootstrap / manifest
- Project Scout
- Orchestrator 动态派发
- Agent LLM 调用
- Evidence Gate
- Challenge
- Context Recovery
- Report

### 13.2 Context Recovery 续跑

```powershell
python m-agent\run_pt9l_full_audit_langgraph.py --output magent-output\pt9l_full_audit_output_langgraph_v9 --resume-context-recovery
```

用于从已有 challenged findings 和 Context Recovery raw files 续跑补证与报告。

### 13.3 离线分组报告

```powershell
python m-agent\run_pt9l_full_audit_langgraph.py --output magent-output\pt9l_full_audit_output_langgraph_v9 --offline-dedup-report
```

用于不重跑全量审查，仅基于已有 challenged findings 生成分组报告。

## 14. 当前 v9 分组报告产物

当前 v9 已生成：

```text
magent-output/pt9l_full_audit_output_langgraph_v9/15_dedup_grouping/grouping_results.json
magent-output/pt9l_full_audit_output_langgraph_v9/07_findings/grouped_findings.jsonl
magent-output/pt9l_full_audit_output_langgraph_v9/08_reports/grouped-findings-review.html
```

报告页面已包含：

- 中文问题组
- 中文原始 finding 展示
- 原文件证据路径和摘录
- 人工修正原文证据
- 每组人工审阅控件
- localStorage 自动保存
- JSON 导入/导出
- 审阅进度统计

## 15. 架构边界与当前限制

当前已经实现：

- Agent YAML 配置拆分。
- Orchestrator 动态派发。
- assigned agent 才调用 LLM。
- agent_runs 运行记录。
- Candidate Discovery 由 Agent 语义提出候选。
- Evidence Tools 只取证不裁决。
- Context Recovery 最多 5 轮。
- Dedup/Grouping 离线分组报告。
- Report Agent 规则和 report writer skill。
- 中文报告显示边界。
- 人工审阅保存与导出。

当前仍需注意：

- Dedup/Grouping 目前作为离线报告入口已实现，尚未默认接入全量审查主流程的自动节点。
- 若需要只刷新 HTML，不应运行 `--offline-dedup-report`，因为它会重新调用 Dedup LLM。
- localStorage 保存依赖浏览器本地环境；跨机器共享需要导出 JSON。
- 人工修正不会删除原始 finding，只会重新解释和归组。
- 报告中的原文件证据不翻译，以避免篡改原始材料。

## 16. 最新技术基线总结

当前方案的核心技术基线可以概括为：

```text
动态 Orchestrator 调度
+ Agent-led candidate discovery
+ Evidence Tools 取证
+ 领域 Agent 复审
+ Challenge 反向质疑
+ Context Recovery 五轮补证
+ Dedup/Grouping 问题组收束
+ Report Agent 中文可审阅报告
+ 人工审阅持久化和导出
```

这套方案保留了原先阶段轴和维度轴的覆盖逻辑，同时避免把审查过程固化成一条线性 workflow。真正的审查判断由 Orchestrator 动态派发给合适 Agent 完成；工具只负责找证据，候选只负责提出疑点，最终报告以问题组和原文证据为中心服务人工审阅。
