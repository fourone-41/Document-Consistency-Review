# 最新多智能体 DHF/DMR 一致性审查技术文档

> 当前版本采用动态 Orchestrator 调度架构。更详细的技术说明见：`m-agent/动态Orchestrator多智能体调度技术文档.md`。

## 1. 方案定位

本系统用于对 PT9L DHF/DMR Markdown 文档集进行一致性审查。当前版本不采用固定工作流逐个运行所有领域 Agent，而是由 Orchestrator LLM 根据项目画像、调度政策、已有 Agent 运行结果和待处理候选动态生成 `route_plan`。

Python 代码只负责：

- 构建证据基础设施。
- 调用 Orchestrator LLM。
- 校验 route_plan。
- 执行被派发的 Agent。
- 记录 `agent_runs[]`。
- 汇总 Evidence Gate、Challenge、Context Recovery 和报告。

## 2. 总体流程

```text
bootstrap
  -> Project Scout Agent
  -> Orchestrator dynamic dispatch loop
  -> Evidence Gate
  -> Challenge Agent
  -> Context Recovery
  -> Report
```

Orchestrator dynamic dispatch loop 内部会反复执行：

```text
Orchestrator LLM reads current blackboard
  -> outputs route_plan
  -> Python executes assigned Agent calls
  -> Agent results append to agent_runs[]
  -> Orchestrator reads updated agent_runs[]
  -> continue / stop / human_review
```

## 3. Agent 与配置

每个 Agent 使用一个 YAML 文件定义：

```text
m-agent/agent_configs/project_scout.yaml
m-agent/agent_configs/orchestrator.yaml
m-agent/agent_configs/candidate_discovery.yaml
m-agent/agent_configs/regulatory.yaml
m-agent/agent_configs/hardware.yaml
m-agent/agent_configs/software.yaml
m-agent/agent_configs/risk_traceability.yaml
m-agent/agent_configs/vv.yaml
m-agent/agent_configs/dmr_sop.yaml
m-agent/agent_configs/challenge.yaml
m-agent/agent_configs/context_recovery.yaml
```

每个 Agent YAML 包含：

- `role`
- `goal`
- `system_prompt`
- `retrieval_strategy`
- `input_schema`
- `output_schema`

## 4. routing.yaml 的角色

`routing.yaml` 现在是 Orchestrator 的调度政策包：

```text
m-agent/agent_configs/routing.yaml
```

它提供：

- 可选决策值：`continue`、`stop`、`human_review`
- 强制覆盖的审查轴
- 候选分派建议
- Context Recovery 回流建议
- route_plan 输出 schema

它不再由 Python 直接执行。Python 不根据候选类型自行决定派发对象。

## 5. agent_runs[] 主线

所有被 Orchestrator 派发的 Agent 调用都会写入：

```text
05_agent_notes/agent_runs.jsonl
05_agent_notes/agent_runs/*.json
```

每条记录包含：

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

Evidence Gate 从 `agent_runs[]` 汇总所有 Agent 的 findings。

## 6. 输出

关键输出包括：

```text
10_task_packages/orchestrator_route_plans.json
10_task_packages/orchestrator_route_plan_cycle_001.json
10_task_packages/mandatory_audit_matrix.json
10_task_packages/available_domain_agent_tasks.json
05_agent_notes/agent_runs.jsonl
07_findings/candidate_discovery_results.jsonl
07_findings/semantic_findings_llm_pre_challenge.jsonl
07_findings/semantic_findings_llm_challenged.jsonl
08_reports/PT9L_full_audit_report_langgraph.md
```

## 7. 运行命令

```powershell
python -X utf8 m-agent/run_pt9l_full_audit_langgraph.py `
  --input pt9l_markdown_output `
  --output magent-output/pt9l_full_audit_output_langgraph_v9
```

## 8. 验证命令

```powershell
python -X utf8 -m pytest m-agent/tests/test_v6_audit_semantics.py
python -X utf8 -m py_compile m-agent/run_pt9l_full_audit_langgraph.py
```
