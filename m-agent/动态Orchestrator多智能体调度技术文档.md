# 动态 Orchestrator 多智能体 DHF/DMR 审查技术文档

## 1. 目标

本版本把 `m-agent` 从固定工作流改为 Orchestrator 驱动的动态多智能体调度。

核心目标是：

- Orchestrator LLM 真正决定下一步派发路线。
- `routing.yaml` 只作为 Orchestrator 的调度政策包，不再由 Python 直接执行路由。
- 只有被 Orchestrator 派到的 Agent 才调用 LLM。
- 一旦 Agent 被派到，必须真实调用 LLM，不读取旧缓存。
- 所有 Agent 运行记录统一进入 `agent_runs[]`，不再依赖固定的 `hardware_output`、`dmr_output` 等字段。

## 2. 新总体流程

```text
bootstrap
  -> scout_agent
  -> orchestrator(dynamic dispatch loop)
  -> evidence_gate
  -> challenge_agent
  -> context_recovery
  -> report
```

其中 `orchestrator(dynamic dispatch loop)` 是新流程的核心。它内部会反复调用 Orchestrator LLM，并根据 route_plan 动态调用 Candidate Discovery Agent 或领域 Agent。

## 3. 各阶段职责

### 3.1 bootstrap

`bootstrap` 仍然负责构建审查基础设施：

- Markdown manifest
- PageIndex
- 参数索引
- RelationIndex
- evidence tool hits
- evidence catalog 初始结构

这些内容是共享证据基础，不直接产生错误结论。

### 3.2 Project Scout Agent

`Project Scout Agent` 是初始画像 Agent，会真实调用 LLM。

输入包括：

- 项目范围证据
- 型号、法规、历史型号线索
- 主范围/辅助范围提示

输出形成 `project_profile`，供 Orchestrator 后续调度使用。

### 3.3 Orchestrator Agent

Orchestrator 是真正的任务调度者。

每一轮 Orchestrator LLM 读取：

- `project_profile`
- `routing.yaml` 中的 `orchestrator_policy`
- 可用 Agent 列表
- `mandatory_audit_matrix`
- 已有 `agent_runs[]`
- 已发现候选 `candidate_discovery_results`
- Context Recovery 结果

然后输出 `route_plan`：

```json
{
  "decision": "continue",
  "reason": "Need DMR and hardware review for product identity candidates.",
  "assignments": [
    {
      "assignment_id": "ASG-001-0001",
      "target_agent": "DMR/SOP Agent",
      "task_type": "domain_review",
      "review_focus": "Review BOM, packaging, process, and label consistency.",
      "input_refs": [],
      "evidence_strategy": {
        "use_page_index": true,
        "use_relation_index": true,
        "use_full_text": true,
        "read_files": []
      }
    }
  ]
}
```

`decision` 只允许三种：

- `continue`：继续派发 Agent。
- `stop`：自动审查已闭环，进入 Evidence Gate。
- `human_review`：继续自动审查收益低或风险高，转人工复核。

### 3.4 Candidate Discovery Agent

Candidate Discovery Agent 不再由固定节点自动执行。

只有 Orchestrator route_plan 中派发：

```json
{
  "target_agent": "Candidate Discovery Agent",
  "task_type": "candidate_discovery"
}
```

它才会被真实调用。

它的职责是提出候选假设，不确认真假。候选输出会写入：

```text
07_findings/candidate_discovery_results.jsonl
```

### 3.5 领域 Agent

领域 Agent 包括：

- Regulatory Agent
- Hardware Agent
- Software Agent
- Risk Traceability Agent
- V&V Agent
- DMR/SOP Agent

这些 Agent 不再固定全部执行。Orchestrator 派到谁，谁才运行。

领域 Agent 的输入由两部分组成：

- Agent 自己 YAML 中定义的检索策略和 schema。
- Orchestrator assignment 中定义的 `review_focus`、`input_refs`、`evidence_strategy`。

领域 Agent 输出 findings 后进入 `agent_runs[]`，再由 Evidence Gate 统一汇总。

## 4. routing.yaml 的新角色

`routing.yaml` 不再是 Python 的确定性路由表。

它现在是：

```text
Orchestrator 调度政策包
```

主要内容是：

- `hard_rules`：Orchestrator 不能裁决真假，只能派任务。
- `mandatory_coverage`：必须考虑覆盖的阶段轴和维度轴。
- `candidate_routing_guidance`：候选类型通常建议哪些 Agent 参与。
- `context_recovery_guidance`：补证后通常建议回流给哪些 Agent。
- `route_plan_schema`：Orchestrator 输出结构。

Python 只把这些内容交给 Orchestrator LLM，不再根据候选类型自己派发。

## 5. agent_runs[] 主线

新流程用 `agent_runs[]` 作为所有 Agent 调用的统一运行日志。

每一次 Orchestrator assignment 都会产生一条 run：

```json
{
  "run_id": "RUN-0001",
  "agent": "Hardware Agent",
  "assignment_id": "ASG-001-0001",
  "task_type": "domain_review",
  "assignment": {},
  "input_package": {},
  "llm_output": {},
  "findings": [],
  "status": "completed"
}
```

对应文件输出：

```text
05_agent_notes/agent_runs.jsonl
05_agent_notes/agent_runs/RUN-0001_hardware_agent.json
```

Evidence Gate 从 `agent_runs[]` 里的 `llm_output.findings` 收集语义 findings。

## 6. 默认不读缓存

本版本明确取消 Agent 输出缓存读取：

- `run_agent_llm()` 每次都会调用 LLM。
- `llm_json_call()` 每次都会调用 LLM。
- Challenge Agent 也不再读取已有 raw JSON。

旧输出仍会被写入文件，方便审阅和追溯，但不会作为下一次运行的缓存输入。

## 7. Context Recovery 回流

Challenge Agent 如果输出 `needs_more_context`，该项进入 Context Recovery。

Context Recovery 负责补证：

- 结构化缺什么证据。
- 读取 PageIndex / 参数索引 / 文件上下文。
- 生成可供复审的 context package。

补证后不是由 Context Recovery 自己裁决，而是重新交回 Orchestrator。Orchestrator 决定是否派给原领域 Agent、另一个领域 Agent，或者转人工复核。

## 8. 代码入口

主要代码位置：

```text
m-agent/run_pt9l_full_audit_langgraph.py
```

关键函数：

- `build_assignable_agent_registry()`：构建可被 Orchestrator 派发的 Agent 列表。
- `normalize_orchestrator_route_plan()`：校验并规范化 Orchestrator 输出。
- `call_orchestrator_route_plan()`：真实调用 Orchestrator LLM。
- `execute_agent_assignment()`：执行 Orchestrator 派发的 Agent。
- `run_agent_llm()`：真实调用 Agent LLM，不读缓存。
- `collect_semantic_findings()`：从 `agent_runs[]` 汇总 findings。

关键配置：

```text
m-agent/agent_configs/routing.yaml
m-agent/agent_configs/orchestrator.yaml
m-agent/agent_configs/*.yaml
```

## 9. 输出目录

常用输出：

```text
10_task_packages/orchestrator_route_plans.json
10_task_packages/orchestrator_route_plan_cycle_001.json
10_task_packages/mandatory_audit_matrix.json
10_task_packages/available_domain_agent_tasks.json
05_agent_notes/agent_runs.jsonl
05_agent_notes/agent_runs/*.json
07_findings/candidate_discovery_results.jsonl
07_findings/semantic_findings_llm_pre_challenge.jsonl
07_findings/semantic_findings_llm_challenged.jsonl
08_reports/PT9L_full_audit_report_langgraph.md
```

## 10. 当前边界

- Python 仍负责构建 PageIndex、参数索引、RelationIndex 等证据基础设施。
- Python 仍负责执行 Orchestrator 派发、校验 Agent 名称、记录 `agent_runs[]`。
- Orchestrator 负责路线组织，不负责真假裁决。
- 领域 Agent 负责复审，不负责全局调度。
- Challenge Agent 负责反证压制和待补证判断。
- Context Recovery 负责补证，不直接终局裁决。
