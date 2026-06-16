# Step2 关系抽取改造（AutoRE + HCRE）Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 [step2_extract_edges.py](../../../file_extractor/step2_extract_edges.py) 现有的一次性"19选N"关系抽取，改造成两阶段流程：先检测文档里可能存在哪些关系类型（AutoRE），再按分组分别做精细配对（HCRE），降低相近类型混淆、减少无效候选。

**Architecture:** 新增 `schema/relation_groups.yaml` 定义 5 个关系大类。`step2_extract_edges.py` 新增 `detect_relation_types_llm()`（Step2a，过滤候选类型）和 `match_within_group()`（Step2b，组内精细配对），用新函数 `extract_edges_llm_v2()` 串联两阶段并替换原有的 `extract_edges_llm()`。规则推导部分（`derive_rule_based_edges`）和去重逻辑（`deduplicate_edges`）不变。

**Tech Stack:** Python 3.11, openai SDK（裸 API 调用，无 instructor）, PyYAML, pytest（新引入，项目此前无测试框架）

---

## 文件结构

- **创建** `schema/relation_groups.yaml` — 19 种边类型的 5 组分类定义
- **创建** `file_extractor/tests/conftest.py` — pytest 路径配置，让测试能 import file_extractor 下的模块
- **创建** `file_extractor/tests/test_relation_groups.py` — 验证分组配置完整、无重复、无遗漏
- **创建** `file_extractor/tests/test_step2_extract_edges.py` — 验证新增函数的解析/过滤逻辑（mock LLM调用）
- **修改** `file_extractor/step2_extract_edges.py` — 移除 `EDGE_PROMPT`/`extract_edges_llm`，新增 `load_relation_groups`、`detect_relation_types_llm`、`match_within_group`、`extract_edges_llm_v2`，修改 `main()` 调用新函数
- **修改** `file_extractor/requirements.txt` — 新增 `pytest`

---

### Task 1: 新增关系类型分组配置

**Files:**
- Create: `schema/relation_groups.yaml`
- Create: `file_extractor/tests/conftest.py`
- Test: `file_extractor/tests/test_relation_groups.py`

- [ ] **Step 1: 创建 conftest.py，让测试能找到 file_extractor 模块**

```python
# file_extractor/tests/conftest.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
```

- [ ] **Step 2: 写失败的测试**

```python
# file_extractor/tests/test_relation_groups.py
import yaml
from pathlib import Path

RELATION_GROUPS_PATH = Path(__file__).parent.parent.parent / "schema" / "relation_groups.yaml"

# 与 step2_extract_edges.py 的 EDGE_PROMPT 中列出的19种类型保持一致
ALL_EDGE_TYPES = {
    "DERIVES_FROM", "CONSTRAINED_BY", "MITIGATED_BY", "VERIFIED_BY",
    "REPORTED_IN", "COVERS", "HAS_MEASUREMENT", "DEPENDS_ON", "SCHEDULES",
    "HAS_REVISION", "HAS_REVIEW_ITEM", "REVIEWS", "LISTS_FILE",
    "DESCRIBES_SOFTWARE", "SIGNED", "IMPLEMENTED_IN", "HAS_DETAIL",
    "RESPONSIBLE_FOR", "PRODUCES",
}


def load_relation_groups() -> dict:
    with open(RELATION_GROUPS_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["relation_groups"]


def test_relation_groups_file_exists():
    assert RELATION_GROUPS_PATH.exists()


def test_all_edge_types_covered_exactly_once():
    groups = load_relation_groups()
    seen = []
    for group_name, types in groups.items():
        seen.extend(types)

    seen_set = set(seen)
    assert seen_set == ALL_EDGE_TYPES, (
        f"分组缺失: {ALL_EDGE_TYPES - seen_set}, 分组多余: {seen_set - ALL_EDGE_TYPES}"
    )
    assert len(seen) == len(seen_set), "存在类型被分到多个组里"


def test_five_groups_defined():
    groups = load_relation_groups()
    assert set(groups.keys()) == {
        "structural", "traceability", "verification", "risk_control", "admin"
    }
```

- [ ] **Step 3: 运行测试确认失败**

Run: `cd file_extractor && python -m pytest tests/test_relation_groups.py -v`
Expected: FAIL，提示 `schema/relation_groups.yaml` 不存在（`test_relation_groups_file_exists` 失败）

- [ ] **Step 4: 创建 relation_groups.yaml**

```yaml
# schema/relation_groups.yaml
# Step2 关系类型层级分组（用于 HCRE 思路：先粗分组再细分类型）
relation_groups:
  structural:
    description: "结构/定位类关系"
    types: [LISTS_FILE, DESCRIBES_SOFTWARE, HAS_DETAIL]
  traceability:
    description: "追溯链关系"
    types: [DERIVES_FROM, CONSTRAINED_BY, IMPLEMENTED_IN]
  verification:
    description: "验证测试链关系"
    types: [VERIFIED_BY, REPORTED_IN, COVERS, HAS_MEASUREMENT]
  risk_control:
    description: "风险管控/计划链关系"
    types: [MITIGATED_BY, DEPENDS_ON, SCHEDULES, RESPONSIBLE_FOR]
  admin:
    description: "行政/评审类关系"
    types: [SIGNED, REVIEWS, HAS_REVIEW_ITEM, HAS_REVISION, PRODUCES]
```

> 注意：这里 `load_relation_groups` 期望的结构是 `{group_name: [type1, type2, ...]}`，但上面 yaml 写的是 `{group_name: {description: ..., types: [...]}}`。下一步统一改成测试里假设的扁平结构，去掉 description 字段，简化加载逻辑（YAGNI：先不需要描述文字，按需再加）。

- [ ] **Step 5: 简化 relation_groups.yaml 为扁平结构**

```yaml
# schema/relation_groups.yaml
# Step2 关系类型层级分组（用于 HCRE 思路：先粗分组再细分类型）
relation_groups:
  structural:    [LISTS_FILE, DESCRIBES_SOFTWARE, HAS_DETAIL]
  traceability:  [DERIVES_FROM, CONSTRAINED_BY, IMPLEMENTED_IN]
  verification:  [VERIFIED_BY, REPORTED_IN, COVERS, HAS_MEASUREMENT]
  risk_control:  [MITIGATED_BY, DEPENDS_ON, SCHEDULES, RESPONSIBLE_FOR]
  admin:         [SIGNED, REVIEWS, HAS_REVIEW_ITEM, HAS_REVISION, PRODUCES]
```

- [ ] **Step 6: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/test_relation_groups.py -v`
Expected: 3 passed

- [ ] **Step 7: Commit**

```bash
git add schema/relation_groups.yaml file_extractor/tests/conftest.py file_extractor/tests/test_relation_groups.py
git commit -m "feat: add relation_groups.yaml for HCRE-style hierarchical classification"
```

---

### Task 2: 实现 Step2a 关系类型检测函数

**Files:**
- Modify: `file_extractor/step2_extract_edges.py`
- Test: `file_extractor/tests/test_step2_extract_edges.py`

- [ ] **Step 1: 写失败的测试（mock LLM 响应）**

```python
# file_extractor/tests/test_step2_extract_edges.py
from unittest.mock import patch, MagicMock
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import step2_extract_edges as s2


def _mock_llm_response(content: str):
    """构造一个假的 OpenAI ChatCompletion 响应对象。"""
    mock_choice = MagicMock()
    mock_choice.message.content = content
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    return mock_response


@patch("step2_extract_edges.client.chat.completions.create")
def test_detect_relation_types_llm_parses_multiple_types(mock_create):
    mock_create.return_value = _mock_llm_response("MITIGATED_BY\nSIGNED\nHAS_DETAIL")
    data = {"risks": [{"risk_id": "R-01"}], "persons": [{"name": "张三", "signed": True}]}

    result = s2.detect_relation_types_llm(data)

    assert result == ["MITIGATED_BY", "SIGNED", "HAS_DETAIL"]


@patch("step2_extract_edges.client.chat.completions.create")
def test_detect_relation_types_llm_handles_none_found(mock_create):
    mock_create.return_value = _mock_llm_response("无")
    data = {"persons": [{"name": "张三"}]}

    result = s2.detect_relation_types_llm(data)

    assert result == []


@patch("step2_extract_edges.client.chat.completions.create")
def test_detect_relation_types_llm_filters_hallucinated_types(mock_create):
    # LLM 可能编造出列表外的类型名，必须被过滤掉
    mock_create.return_value = _mock_llm_response("MITIGATED_BY\nFAKE_TYPE\nSIGNED")
    data = {"risks": [{"risk_id": "R-01"}]}

    result = s2.detect_relation_types_llm(data)

    assert result == ["MITIGATED_BY", "SIGNED"]
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd file_extractor && python -m pytest tests/test_step2_extract_edges.py -v`
Expected: FAIL，提示 `module 'step2_extract_edges' has no attribute 'detect_relation_types_llm'`

- [ ] **Step 3: 实现 detect_relation_types_llm**

在 [step2_extract_edges.py](../../../file_extractor/step2_extract_edges.py) 中，紧跟 `EDGE_PROMPT` 定义之后（第 49 行后）新增：

```python
ALL_RELATION_TYPES = [
    "DERIVES_FROM", "CONSTRAINED_BY", "MITIGATED_BY", "VERIFIED_BY",
    "REPORTED_IN", "COVERS", "HAS_MEASUREMENT", "DEPENDS_ON", "SCHEDULES",
    "HAS_REVISION", "HAS_REVIEW_ITEM", "REVIEWS", "LISTS_FILE",
    "DESCRIBES_SOFTWARE", "SIGNED", "IMPLEMENTED_IN", "HAS_DETAIL",
    "RESPONSIBLE_FOR", "PRODUCES",
]

RELATION_TYPE_DETECTION_PROMPT = """你是医疗器械DHF文档一致性审查的关系抽取专家。

以下是从一份文档中抽取的节点信息摘要。请判断这份文档中，下面列出的19种关系类型，
哪些有可能存在（哪怕只有一处依据也算，不确定的也列出来，我们宁可多判断）。

===== 19种关系类型 =====
1. DERIVES_FROM: DesignInput → Requirement（设计输入来源于需求）
2. CONSTRAINED_BY: Requirement → Regulation（需求受法规约束）
3. MITIGATED_BY: Risk → RiskControl（风险被措施控制）
4. VERIFIED_BY: RiskControl/DesignInput → Test（被测试验证）
5. REPORTED_IN: Test → TestReport（测试结果记录在报告中）
6. COVERS: DesignInput/Requirement/Function → IntendedUseItem（覆盖预期用途）
7. HAS_MEASUREMENT: Test → TestMeasurement（测试包含实测数据）
8. DEPENDS_ON: PlanTask → PlanTask（任务前置依赖）
9. SCHEDULES: Document → PlanTask（计划文件包含任务）
10. HAS_REVISION: Document → RevisionRecord（文件的版本历史）
11. HAS_REVIEW_ITEM: Document/ReviewRecord → ReviewItem（评审包含检查项）
12. REVIEWS: ReviewItem → Requirement/DesignInput/Document（检查项评审对象）
13. LISTS_FILE: Document → DocIndexEntry（清单包含文件条目）
14. DESCRIBES_SOFTWARE: Document → SoftwareItem/SoftwareConfigItem
15. SIGNED: Person → Document/ReviewRecord（人员签署文件）
16. IMPLEMENTED_IN: Function → Document（功能在文件中实现）
17. HAS_DETAIL: 任意节点 → SemanticFragment（结构化节点的补充文本）
18. RESPONSIBLE_FOR: Person → PlanTask（人员负责该任务）
19. PRODUCES: PlanTask → Document/Identifier（任务产出文件）

===== 输出格式 =====
只输出存在可能性的关系类型名称（必须是上面19个名称之一），一行一个，不要解释、不要编号。
如果一个都不存在，输出"无"。
"""


def detect_relation_types_llm(data: dict) -> list[str]:
    """Step2a: 判断文档中可能存在哪些关系类型（AutoRE 任务1，低成本过滤）。"""
    node_summary = {}
    for key, val in data.items():
        if key.startswith("_"):
            continue
        if isinstance(val, list) and val:
            node_summary[key] = val[:10]
        elif isinstance(val, dict):
            node_summary[key] = val

    if not node_summary:
        return []

    user_msg = json.dumps(node_summary, ensure_ascii=False, indent=1)
    if len(user_msg) > 8000:
        user_msg = user_msg[:8000] + "\n...(truncated)"

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=300,
            messages=[
                {"role": "system", "content": RELATION_TYPE_DETECTION_PROMPT},
                {"role": "user", "content": user_msg},
            ],
        )
        content = response.choices[0].message.content or "无"
        lines = [l.strip() for l in content.strip().split("\n") if l.strip()]
        return [t for t in lines if t in ALL_RELATION_TYPES]
    except Exception as e:
        print(f"    detect_relation_types_llm ERROR: {e}", flush=True)
        return []
```

- [ ] **Step 4: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/test_step2_extract_edges.py -v`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add file_extractor/step2_extract_edges.py file_extractor/tests/test_step2_extract_edges.py
git commit -m "feat: add Step2a relation type detection (AutoRE task 1)"
```

---

### Task 3: 实现 Step2b 组内精细配对函数

**Files:**
- Modify: `file_extractor/step2_extract_edges.py`
- Test: `file_extractor/tests/test_step2_extract_edges.py`

- [ ] **Step 1: 追加失败的测试**

```python
# 追加到 file_extractor/tests/test_step2_extract_edges.py

@patch("step2_extract_edges.client.chat.completions.create")
def test_match_within_group_parses_valid_edges(mock_create):
    mock_create.return_value = _mock_llm_response(
        '[{"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}}]'
    )
    data = {"risks": [{"risk_id": "R-01"}], "risk_controls": [{"control_id": "CM-03"}]}

    result = s2.match_within_group(data, "risk_control", ["MITIGATED_BY", "DEPENDS_ON"])

    assert result == [{"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}}]


@patch("step2_extract_edges.client.chat.completions.create")
def test_match_within_group_filters_edges_outside_candidate_types(mock_create):
    # LLM 可能跑出候选范围之外的类型，必须被过滤
    mock_create.return_value = _mock_llm_response(
        '[{"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}},'
        '{"type": "SIGNED", "from": "张三", "to": "doc", "properties": {}}]'
    )
    data = {"risks": [{"risk_id": "R-01"}]}

    result = s2.match_within_group(data, "risk_control", ["MITIGATED_BY", "DEPENDS_ON"])

    assert result == [{"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}}]


@patch("step2_extract_edges.client.chat.completions.create")
def test_match_within_group_empty_candidates_skips_llm_call(mock_create):
    result = s2.match_within_group({"risks": []}, "risk_control", [])

    assert result == []
    mock_create.assert_not_called()
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd file_extractor && python -m pytest tests/test_step2_extract_edges.py -v`
Expected: FAIL，提示 `module 'step2_extract_edges' has no attribute 'match_within_group'`

- [ ] **Step 3: 实现 match_within_group**

在 `detect_relation_types_llm` 函数之后新增：

```python
GROUP_MATCH_PROMPT_TEMPLATE = """你是医疗器械DHF文档一致性审查的关系抽取专家。

以下是从一份文档中抽取的节点信息（JSON）。本次只需要在下面这些候选关系类型中判断：
{candidate_types}

===== 输出格式 =====
JSON数组：
[{{"type": "关系类型", "from": "起点标识", "to": "终点标识", "properties": {{}}}}]

===== 规则 =====
1. from/to 用节点的 id、name、seq、test_id、req_id 等唯一标识
2. 只能输出上面列出的候选关系类型，不要输出列表外的类型
3. 同一对节点可以有多条不同类型的边
4. 没有关系则输出 []
5. 严格输出 JSON，不要加 markdown 标记
"""


def match_within_group(data: dict, group_name: str, candidate_types: list[str]) -> list[dict]:
    """Step2b: 在某个关系大类的候选类型范围内做实体配对（HCRE 思路：组内细分类型判断）。"""
    if not candidate_types:
        return []

    node_summary = {}
    for key, val in data.items():
        if key.startswith("_"):
            continue
        if isinstance(val, list) and val:
            node_summary[key] = val[:25]
        elif isinstance(val, dict):
            node_summary[key] = val

    if not node_summary:
        return []

    user_msg = json.dumps(node_summary, ensure_ascii=False, indent=1)
    if len(user_msg) > 14000:
        user_msg = user_msg[:14000] + "\n...(truncated)"

    prompt = GROUP_MATCH_PROMPT_TEMPLATE.format(candidate_types=", ".join(candidate_types))

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=LLM_MAX_TOKENS,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user_msg},
            ],
        )
        content = response.choices[0].message.content or "[]"
        edges = try_parse_json(content)
        if not isinstance(edges, list):
            return []
        return [e for e in edges if e.get("type") in candidate_types]
    except Exception as e:
        print(f"    match_within_group ERROR ({group_name}): {e}", flush=True)
        return []
```

- [ ] **Step 4: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/test_step2_extract_edges.py -v`
Expected: 6 passed

- [ ] **Step 5: Commit**

```bash
git add file_extractor/step2_extract_edges.py file_extractor/tests/test_step2_extract_edges.py
git commit -m "feat: add Step2b within-group entity matching (HCRE-style)"
```

---

### Task 4: 串联两阶段并接入主流程

**Files:**
- Modify: `file_extractor/step2_extract_edges.py`
- Test: `file_extractor/tests/test_step2_extract_edges.py`

- [ ] **Step 1: 追加失败的测试**

```python
# 追加到 file_extractor/tests/test_step2_extract_edges.py

@patch("step2_extract_edges.match_within_group")
@patch("step2_extract_edges.detect_relation_types_llm")
def test_extract_edges_llm_v2_groups_candidates_and_merges_results(mock_detect, mock_match):
    mock_detect.return_value = ["MITIGATED_BY", "SIGNED"]

    def fake_match(data, group_name, candidate_types):
        if group_name == "risk_control":
            return [{"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}}]
        if group_name == "admin":
            return [{"type": "SIGNED", "from": "张三", "to": "doc", "properties": {}}]
        return []

    mock_match.side_effect = fake_match
    relation_groups = {
        "structural":    ["LISTS_FILE", "DESCRIBES_SOFTWARE", "HAS_DETAIL"],
        "traceability":  ["DERIVES_FROM", "CONSTRAINED_BY", "IMPLEMENTED_IN"],
        "verification":  ["VERIFIED_BY", "REPORTED_IN", "COVERS", "HAS_MEASUREMENT"],
        "risk_control":  ["MITIGATED_BY", "DEPENDS_ON", "SCHEDULES", "RESPONSIBLE_FOR"],
        "admin":         ["SIGNED", "REVIEWS", "HAS_REVIEW_ITEM", "HAS_REVISION", "PRODUCES"],
    }

    result = s2.extract_edges_llm_v2({"risks": [{"risk_id": "R-01"}]}, relation_groups)

    assert {"type": "MITIGATED_BY", "from": "R-01", "to": "CM-03", "properties": {}} in result
    assert {"type": "SIGNED", "from": "张三", "to": "doc", "properties": {}} in result
    assert len(result) == 2
    # 只命中的两个组（risk_control, admin）应该被调用，没命中的组不应该调用
    assert mock_match.call_count == 2


@patch("step2_extract_edges.detect_relation_types_llm")
def test_extract_edges_llm_v2_no_types_detected_skips_all_groups(mock_detect):
    mock_detect.return_value = []
    relation_groups = {"risk_control": ["MITIGATED_BY"]}

    result = s2.extract_edges_llm_v2({"risks": []}, relation_groups)

    assert result == []
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd file_extractor && python -m pytest tests/test_step2_extract_edges.py -v`
Expected: FAIL，提示 `module 'step2_extract_edges' has no attribute 'extract_edges_llm_v2'`

- [ ] **Step 3: 实现 extract_edges_llm_v2，并新增 load_relation_groups**

在文件顶部 import 区域（第 1-11 行）新增 `yaml` 导入：

```python
import json
import re
import time
import yaml
from pathlib import Path
from openai import OpenAI

from config import API_KEY, LLM_BASE_URL, LLM_MODEL, PER_FILE_DIR, LLM_MAX_TOKENS

client = OpenAI(api_key=API_KEY, base_url=LLM_BASE_URL)

RELATION_GROUPS_PATH = Path(__file__).parent.parent / "schema" / "relation_groups.yaml"
```

在 `match_within_group` 函数之后新增：

```python
def load_relation_groups() -> dict:
    """加载 schema/relation_groups.yaml 中的关系类型分组定义。"""
    with open(RELATION_GROUPS_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["relation_groups"]


def extract_edges_llm_v2(data: dict, relation_groups: dict) -> list[dict]:
    """两阶段关系抽取：Step2a 检测候选类型，Step2b 按组精细配对。"""
    detected_types = detect_relation_types_llm(data)
    if not detected_types:
        return []

    detected_set = set(detected_types)
    all_edges = []
    for group_name, group_types in relation_groups.items():
        candidate_types = [t for t in group_types if t in detected_set]
        if not candidate_types:
            continue
        edges = match_within_group(data, group_name, candidate_types)
        all_edges.extend(edges)

    return all_edges
```

- [ ] **Step 4: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/test_step2_extract_edges.py -v`
Expected: 8 passed

- [ ] **Step 5: 修改 main() 使用新的两阶段流程**

把 [step2_extract_edges.py:200-236](../../../file_extractor/step2_extract_edges.py#L200-L236) 的 `main()` 函数中：

```python
        # LLM-based edges
        print(f"    LLM extraction...", end="", flush=True)
        llm_edges = extract_edges_llm(data)
```

改为：

```python
        # LLM-based edges (two-stage: AutoRE detection + HCRE grouped matching)
        print(f"    LLM extraction...", end="", flush=True)
        llm_edges = extract_edges_llm_v2(data, relation_groups)
```

并在 `main()` 函数开头（[第 207 行](../../../file_extractor/step2_extract_edges.py#L207) `for i, fp in enumerate(...)` 循环之前）新增：

```python
    relation_groups = load_relation_groups()
```

- [ ] **Step 6: 删除旧的 EDGE_PROMPT 和 extract_edges_llm**

删除 [step2_extract_edges.py:13-49](../../../file_extractor/step2_extract_edges.py#L13-L49)（`EDGE_PROMPT` 常量定义）和 [第151-185行](../../../file_extractor/step2_extract_edges.py#L151-L185)（`extract_edges_llm` 函数），避免死代码。

- [ ] **Step 7: 运行全部单测确认通过**

Run: `cd file_extractor && python -m pytest tests/ -v`
Expected: 11 passed (3 个 relation_groups 测试 + 8 个 step2 测试)

- [ ] **Step 8: Commit**

```bash
git add file_extractor/step2_extract_edges.py file_extractor/tests/test_step2_extract_edges.py
git commit -m "feat: wire two-stage extraction into main(), remove old one-shot extract_edges_llm"
```

---

### Task 5: 样本数据人工验证

**Files:**
- No new files — 在已有的 `output/per_file/*.json` 样本上运行验证

- [ ] **Step 1: 备份现有 Step2 输出，用于前后对比**

```bash
cd file_extractor
cp -r output/per_file output/per_file_before_step2_refactor
```

- [ ] **Step 2: 在依赖 requirements.txt 中新增 pytest**

修改 `file_extractor/requirements.txt`，新增一行：

```
pytest>=7.0.0
```

- [ ] **Step 3: 重新运行 Step2 对所有样本文件**

Run: `cd file_extractor && python step2_extract_edges.py`
Expected: 命令正常结束，打印 `=== Step 2 Complete ===` 及边总数

- [ ] **Step 4: 对比前后边数量和具体内容**

```bash
cd file_extractor
python -c "
import json
from pathlib import Path

before_dir = Path('output/per_file_before_step2_refactor')
after_dir = Path('output/per_file')

for before_fp in sorted(before_dir.glob('*.json')):
    after_fp = after_dir / before_fp.name
    if not after_fp.exists():
        continue
    before_edges = json.loads(before_fp.read_text(encoding='utf-8')).get('_edges', [])
    after_edges = json.loads(after_fp.read_text(encoding='utf-8')).get('_edges', [])
    print(f'{before_fp.stem[:40]:40s} before={len(before_edges):3d} after={len(after_edges):3d}')
"
```

人工检查：抽 2-3 个文件，对比 `_edges` 字段里具体的边内容，确认新流程没有丢失明显应该存在的关系（比如风险分析文档里 MITIGATED_BY 类型的边数量不应该明显下降）。这一步不写自动化断言——按设计文档第7节"以人工抽样审查为主"的约定，需要你本人判断结果是否合理。

- [ ] **Step 5: 清理备份目录**

确认验证结果满意后：

```bash
cd file_extractor
rm -rf output/per_file_before_step2_refactor
```

- [ ] **Step 6: Commit**

```bash
git add file_extractor/requirements.txt
git commit -m "chore: add pytest to requirements.txt"
```

---

## 完成后

Step2 改造完成并验证后，下一步是为 Step4（跨文档四层候选生成 + KXDocRE 法规注入）单独写一份实现计划。
