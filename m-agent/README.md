# m-agent 最终版多智能体审查

本目录只保留当前最终版 DHF/DMR 一致性审查代码、Agent 配置、测试和技术文档。

## 文件说明

| 文件/目录 | 用途 |
|---|---|
| `run_pt9l_full_audit_langgraph.py` | 全量审查主脚本，包含证据工具、Project Scout、Orchestrator、Candidate Discovery、领域 Agent、Evidence Gate、Challenge、Context Recovery 和报告生成。 |
| `agent_configs/*.yaml` | 每个 Agent 的检索策略、输入 schema、输出 schema 和提示原则。改单个 Agent 优先改这里。 |
| `agent_configs/routing.yaml` | Orchestrator 路由规则、阶段轴/维度轴强制审查矩阵、候选分派规则和 Context Recovery 回流规则。 |
| `tests/test_v6_audit_semantics.py` | 主流程语义回归测试。 |
| `动态Orchestrator多智能体调度技术文档.md` | 动态 Orchestrator 调度、`agent_runs[]`、route_plan 和默认不读缓存的最新技术说明。 |
| `最新多智能体DHF-DMR一致性审查技术文档.md` | 当前技术方案文档。 |
| `动态Orchestrator流程架构可视化候选.html` | 动态 Orchestrator 调度架构可视化候选页。 |

## 运行全量审查

```powershell
python -X utf8 m-agent/run_pt9l_full_audit_langgraph.py `
  --input pt9l_markdown_output `
  --output magent-output/pt9l_full_audit_output_langgraph_v9
```

## 运行测试

```powershell
python -X utf8 -m pytest m-agent/tests/test_v6_audit_semantics.py
```

## 当前原则

- 工具只负责定位证据，不直接生成候选或错误。
- 候选假设由 `Candidate Discovery Agent` 提出。
- `Orchestrator` 只做任务拆解和路由分配，不裁决真假。
- `Orchestrator` 通过 LLM 动态生成 `route_plan`，Python 只执行和记录。
- 默认每次都真实调用 LLM，不读取旧 Agent 输出缓存。
- 领域 Agent 复审后进入 `Evidence Gate`、`Challenge Agent` 和 `Context Recovery`。
- 非显式要求，不为旧逻辑保留兼容分支。
