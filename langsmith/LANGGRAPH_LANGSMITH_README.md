# DHF/DMR LangGraph + LangSmith

这套实现把 `最新多智能体DHF-DMR流程架构可视化.html` 里的调度图映射成真实 LangGraph：

- `project_scout`: 项目画像、审核范围、法规基线
- `orchestrator_router`: 必查任务矩阵、Agent/Skill 路由
- `evidence_tools`: PageIndex/Relation/全文检索的工具层占位
- `candidate_discovery`: 候选假设生成
- `candidate_router`: 候选标准化并回流 Router
- `domain_agents`: Regulatory/Hardware/Software/QA 等领域 Agent 复审
- `evidence_gate`: 证据校验与 Challenge
- `context_recovery`: 最多五轮补证并回到 Orchestrator
- `human_review`: 人工复核包
- `final_report`: Markdown 和 JSON 输出

## 安装

```powershell
cd D:\driven-ai\multi_agent_orchestration_system
python -m pip install -r requirements-langgraph.txt
```

## 本地运行

```powershell
python demo\run_langgraph_langsmith_demo.py
```

输出文件：

- `outputs/PT9L_full_audit_report_langgraph.md`
- `outputs/langgraph_dhf_dmr_run.json`

## 上传到 LangSmith

在运行前设置环境变量：

```powershell
$env:LANGSMITH_TRACING="true"
$env:LANGSMITH_API_KEY="lsv2_你的LangSmithKey"
$env:LANGSMITH_PROJECT="dhf-dmr-langgraph"
python demo\run_langgraph_langsmith_demo.py
```

LangSmith 里会看到每个 LangGraph 节点的执行轨迹、状态输入输出、条件边走向和补证循环。
