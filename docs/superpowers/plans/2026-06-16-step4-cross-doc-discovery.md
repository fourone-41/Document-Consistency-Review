# Step4 跨文档关系发现（四层候选生成）Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** 把 [step4_cross_doc_edges.py](../../../file_extractor/step4_cross_doc_edges.py) 现有"仅靠 12 条人工预定义规则"的跨文档关系发现，扩展成四层互补候选生成（规则匹配+条款注入、图模式传播、向量召回、桥接实体）+ 开放式 LLM 验证，既提升规则内判断准确率，又能发现规则外的关系。

**Architecture:** 保留现有 `REGULATORY_GUIDES` 驱动的逐 guide 匹配作为「层①」，只追加 ISO 条款文本注入。新增三个独立模块产出未经验证的候选对：`bridge_entities.py`（层④，纯 Python，无 LLM）、`embedding_retrieval.py`（层③，调用阿里云 DashScope 生成向量 + 写入 Neo4j 向量索引检索）、`graph_pattern_propagation.py`（层②，基于已有边的频次统计，依赖层①已产出的边）。所有层④③②候选去重合并后，统一送入新的开放式 LLM 验证函数，输出标注 `discovery_layer` 字段。`main()` 按层①→④→③→②→合并验证的顺序编排。

**Tech Stack:** Python 3.11, openai SDK（同时用于现有 LLM Gateway 和阿里云 DashScope，两个不同 base_url/key）, neo4j Python driver（已是依赖）, pytest

---

## 文件结构

- **创建** `file_extractor/regulatory_clauses.yaml` — ISO 条款转述要点库
- **创建** `file_extractor/bridge_entities.py` — 层④：共享实体发现（CodRED）
- **创建** `file_extractor/embedding_retrieval.py` — 层③：DashScope 向量化 + Neo4j 向量索引检索（MAQD）
- **创建** `file_extractor/graph_pattern_propagation.py` — 层②：图模式传播（Think-on-Graph）
- **创建** `file_extractor/tests/test_bridge_entities.py`
- **创建** `file_extractor/tests/test_embedding_retrieval.py`
- **创建** `file_extractor/tests/test_graph_pattern_propagation.py`
- **创建** `file_extractor/tests/test_step4_cross_doc_edges.py`（新增测试，复用同名旧文件名但项目里之前没有，新建）
- **修改** `file_extractor/config.py` — 新增 DashScope 相关配置
- **修改** `file_extractor/step4_cross_doc_edges.py` — 注入条款文本、新增开放式验证函数、新增候选合并编排、`main()` 接入四层
- **修改** `file_extractor/requirements.txt` — 无需新增（DashScope 走 openai SDK，neo4j 驱动已存在）

---

### Task 1：ISO 条款转述要点库 + 层①条款注入（KXDocRE）

**Files:**
- Create: `file_extractor/regulatory_clauses.yaml`
- Modify: `file_extractor/step4_cross_doc_edges.py:354-403`（`match_llm_semantic`，当前未被调用，可保留不动）和 `file_extractor/step4_cross_doc_edges.py:527-548`（`_llm_match_batch` 的 prompt 构建部分）
- Test: `file_extractor/tests/test_step4_cross_doc_edges.py`

- [ ] **Step 1: 创建条款转述要点库**

```yaml
# file_extractor/regulatory_clauses.yaml
# ISO 13485/14971/IEC 62304 条款转述要点（基于公开资料整理，非逐字引用标准原文）
clauses:
  "ISO 13485 7.3.3":
    summary: >
      设计输入应基于预期用途确定功能、性能、可用性和安全要求，
      并需经评审确认完整、明确、可验证、不自相矛盾。
  "ISO 13485 7.3.6":
    summary: >
      设计验证用于确认设计输出满足设计输入的要求，应制定验证计划
      （方法、接收准则），并保留验证记录。
  "ISO 13485 7.3.6/7.3.7":
    summary: >
      设计验证确认输出满足输入要求，设计确认确保产品满足预期用途
      和使用者要求。
  "ISO 14971 7.1":
    summary: >
      针对评估为不可接受的风险，应采取风险控制措施降低风险，
      控制措施应与风险产生原因相对应。
  "ISO 14971 8":
    summary: >
      风险控制措施实施后，应验证其有效性，确认剩余风险是否
      降到可接受水平。
  "IEC 62304 5.7":
    summary: >
      软件系统测试阶段应针对软件需求规格中的功能、性能要求执行测试，
      确认软件实现满足需求。
  "ISO 13485 7.3.2":
    summary: >
      设计开发策划应规定开发阶段、评审/验证/确认活动、职责和接口关系，
      并形成文件。
  "ISO 13485 7.1":
    summary: >
      组织应确定适用的法规要求，并将其融入质量管理体系和产品实现过程。
```

- [ ] **Step 2: 写失败的测试**

```python
# file_extractor/tests/test_step4_cross_doc_edges.py
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

import step4_cross_doc_edges as s4


def _mock_llm_response(content: str):
    mock_choice = MagicMock()
    mock_choice.message.content = content
    mock_response = MagicMock()
    mock_response.choices = [mock_choice]
    return mock_response


def test_load_regulatory_clauses_returns_dict_keyed_by_standard():
    clauses = s4.load_regulatory_clauses()

    assert "ISO 13485 7.3.3" in clauses
    assert "summary" in clauses["ISO 13485 7.3.3"]
    assert len(clauses["ISO 13485 7.3.3"]["summary"]) > 10


@patch("step4_cross_doc_edges.client.chat.completions.create")
def test_llm_match_batch_injects_clause_summary_into_prompt(mock_create):
    mock_create.return_value = _mock_llm_response("无")
    guide = {
        "name": "Requirement -> DesignInput traceability",
        "standard": "ISO 13485 7.3.3",
        "rationale": "Each customer requirement should trace to at least one design input",
    }
    src_batch = [(0, "[R-01] 体温测量范围 35-42℃")]
    tgt_batch = [(0, "[DI-01] 温度显示范围 32-42.9℃")]

    s4._llm_match_batch(src_batch, tgt_batch, [{"req_id": "R-01"}], [{"di_id": "DI-01"}], guide, "requirements", "design_inputs")

    sent_prompt = mock_create.call_args.kwargs["messages"][0]["content"]
    assert "设计输入应基于预期用途确定功能" in sent_prompt
```

- [ ] **Step 3: 运行测试确认失败**

Run: `cd file_extractor && python -m pytest tests/test_step4_cross_doc_edges.py -v`
Expected: FAIL，`AttributeError: module 'step4_cross_doc_edges' has no attribute 'load_regulatory_clauses'`

- [ ] **Step 4: 实现 load_regulatory_clauses 并注入条款文本**

在 [step4_cross_doc_edges.py](../../../file_extractor/step4_cross_doc_edges.py) 顶部 import 区域新增 `import yaml`，把：

```python
import json
import re
import time
import sys
from pathlib import Path
from difflib import SequenceMatcher
from openai import OpenAI
```

改为：

```python
import json
import re
import time
import sys
import yaml
from pathlib import Path
from difflib import SequenceMatcher
from openai import OpenAI
```

在 `OUTPUT_DIR` 定义之后（第 22 行后）新增：

```python
REGULATORY_CLAUSES_PATH = Path(__file__).parent / "regulatory_clauses.yaml"


def load_regulatory_clauses() -> dict:
    """加载 regulatory_clauses.yaml 中的 ISO 条款转述要点，按标准编号索引。"""
    with open(REGULATORY_CLAUSES_PATH, encoding="utf-8") as f:
        data = yaml.safe_load(f)
    return data["clauses"]
```

修改 [`_llm_match_batch`](../../../file_extractor/step4_cross_doc_edges.py#L527-L548) 的 prompt 构建部分，把：

```python
    prompt = f"""你是医疗器械文档关系分析专家。

任务：根据 {guide['standard']} 的要求，找出【源列表】和【目标列表】之间存在"{guide['name']}"关系的配对。

{guide['rationale']}

【源列表 ({src_type})】:
"""
```

改为：

```python
    clauses = load_regulatory_clauses()
    clause_summary = clauses.get(guide['standard'], {}).get('summary', '').strip()
    clause_block = f"\n法规条款要点：{clause_summary}\n" if clause_summary else ""

    prompt = f"""你是医疗器械文档关系分析专家。

任务：根据 {guide['standard']} 的要求，找出【源列表】和【目标列表】之间存在"{guide['name']}"关系的配对。

{guide['rationale']}
{clause_block}
【源列表 ({src_type})】:
"""
```

- [ ] **Step 5: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/test_step4_cross_doc_edges.py -v`
Expected: 2 passed

- [ ] **Step 6: Commit**

```bash
git add file_extractor/regulatory_clauses.yaml file_extractor/step4_cross_doc_edges.py file_extractor/tests/test_step4_cross_doc_edges.py
git commit -m "feat: inject ISO clause summaries into Step4 regulatory matching (KXDocRE)"
```

---

### Task 2：层④ 桥接实体发现（CodRED）

**Files:**
- Create: `file_extractor/bridge_entities.py`
- Test: `file_extractor/tests/test_bridge_entities.py`

- [ ] **Step 1: 写失败的测试**

```python
# file_extractor/tests/test_bridge_entities.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import bridge_entities as be


def test_extract_entity_mentions_finds_known_patterns():
    text = "本测试验证 PT9L 红外传感器在 ISO 80601-2-56 标准下的表现，由张三负责。"

    mentions = be.extract_entity_mentions(text)

    assert "PT9L" in mentions
    assert "ISO 80601-2-56" in mentions


def test_extract_entity_mentions_empty_text_returns_empty_set():
    assert be.extract_entity_mentions("") == set()
    assert be.extract_entity_mentions(None) == set()


def test_find_bridge_entities_pairs_nodes_sharing_entity_across_sources():
    nodes = {
        "risks": [
            {"risk_id": "R-01", "hazard": "红外传感器漂移导致测量误差", "_source": "doc_a.md"},
        ],
        "tests": [
            {"test_id": "T-12", "item": "红外传感器在高温环境下的线性度验证", "_source": "doc_b.md"},
            {"test_id": "T-15", "item": "电池续航测试", "_source": "doc_b.md"},
        ],
    }

    pairs = be.find_bridge_entities(nodes)

    assert any(
        s.get("risk_id") == "R-01" and t.get("test_id") == "T-12"
        for s, t in pairs
    )
    assert not any(
        s.get("risk_id") == "R-01" and t.get("test_id") == "T-15"
        for s, t in pairs
    )


def test_find_bridge_entities_ignores_same_source_pairs():
    nodes = {
        "risks": [{"risk_id": "R-01", "hazard": "PT9L 传感器问题", "_source": "doc_a.md"}],
        "tests": [{"test_id": "T-12", "item": "PT9L 传感器测试", "_source": "doc_a.md"}],
    }

    pairs = be.find_bridge_entities(nodes)

    assert pairs == []
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd file_extractor && python -m pytest tests/test_bridge_entities.py -v`
Expected: FAIL，`ModuleNotFoundError: No module named 'bridge_entities'`

- [ ] **Step 3: 实现 bridge_entities.py**

```python
# file_extractor/bridge_entities.py
"""Step4 候选生成层④：桥接实体发现（CodRED 思路）。

扫描节点文本字段，找出被两个以上不同来源文档共同提及的实体名
（产品型号、标准编号等），把共同提及该实体的节点两两配对，
作为不依赖文字相似度的候选关系来源。
"""
import re
from itertools import combinations

# 产品型号：大写字母+数字组合（如 PT9L）
PRODUCT_PATTERN = re.compile(r'\b[A-Z]{2,}[0-9]+[A-Z0-9]*\b')
# 标准编号：ISO/IEC/ASTM 等 + 数字
STANDARD_PATTERN = re.compile(r'\b(?:ISO|IEC|ASTM|GB|YY)\s?[\d\-\.]+(?:[:\-]\d+)?\b')

NODE_TEXT_FIELDS = {
    "risks": ["hazard", "hazardous_situation"],
    "risk_controls": ["measure"],
    "tests": ["item", "expected_value"],
    "requirements": ["description"],
    "design_inputs": ["description"],
    "regulations": ["requirement_text"],
}


def extract_entity_mentions(text: str) -> set:
    """从文本中提取候选桥接实体（产品型号、标准编号）。"""
    if not text:
        return set()
    mentions = set()
    mentions.update(PRODUCT_PATTERN.findall(text))
    mentions.update(m.strip() for m in STANDARD_PATTERN.findall(text))
    return mentions


def find_bridge_entities(nodes: dict) -> list[tuple]:
    """找出被两个以上不同来源文档共同提及实体的节点对。

    返回 [(node_a, node_b), ...]，只包含来源文档不同的配对。
    """
    # entity -> list of (node, node_type)
    entity_to_nodes = {}

    for node_type, fields in NODE_TEXT_FIELDS.items():
        for node in nodes.get(node_type, []):
            text = " ".join(str(node.get(f, "") or "") for f in fields)
            mentions = extract_entity_mentions(text)
            for entity in mentions:
                entity_to_nodes.setdefault(entity, []).append(node)

    pairs = []
    seen = set()
    for entity, node_list in entity_to_nodes.items():
        if len(node_list) < 2:
            continue
        for a, b in combinations(node_list, 2):
            if a.get("_source") == b.get("_source"):
                continue
            key = (id(a), id(b))
            if key in seen:
                continue
            seen.add(key)
            pairs.append((a, b))

    return pairs
```

- [ ] **Step 4: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/test_bridge_entities.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add file_extractor/bridge_entities.py file_extractor/tests/test_bridge_entities.py
git commit -m "feat: add bridge entity discovery for Step4 (CodRED-style candidate layer)"
```

---

### Task 3：层③ 向量召回（DashScope + Neo4j 向量索引，MAQD）

**Files:**
- Modify: `file_extractor/config.py`
- Create: `file_extractor/embedding_retrieval.py`
- Test: `file_extractor/tests/test_embedding_retrieval.py`

- [ ] **Step 1: 在 config.py 新增 DashScope 配置**

在 [config.py](../../../file_extractor/config.py) 的 `LLM_MODEL` 定义之后（第 12 行后）新增：

```python
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
DASHSCOPE_EMBEDDING_MODEL = os.getenv("DASHSCOPE_EMBEDDING_MODEL", "text-embedding-v3")
DASHSCOPE_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
NEO4J_URI = "bolt://localhost:7687"
NEO4J_AUTH = ("neo4j", "test1234")
```

- [ ] **Step 2: 写失败的测试**

```python
# file_extractor/tests/test_embedding_retrieval.py
import sys
from pathlib import Path
from unittest.mock import patch, MagicMock

sys.path.insert(0, str(Path(__file__).parent.parent))

import embedding_retrieval as er


def _mock_embedding_response(vectors: list[list[float]]):
    mock_response = MagicMock()
    mock_response.data = [MagicMock(embedding=v) for v in vectors]
    return mock_response


def test_build_multi_aspect_queries_includes_description_and_value():
    node = {"description": "体温测量范围", "value": "35-42", "unit": "℃"}

    queries = er.build_multi_aspect_queries(node, "requirements")

    assert "体温测量范围" in queries
    assert any("35-42" in q for q in queries)


def test_build_multi_aspect_queries_dedupes_empty_aspects():
    node = {"description": "", "value": "", "unit": ""}

    queries = er.build_multi_aspect_queries(node, "requirements")

    assert queries == []


@patch("embedding_retrieval.dashscope_client.embeddings.create")
def test_get_embeddings_batch_calls_dashscope_with_correct_model(mock_create):
    mock_create.return_value = _mock_embedding_response([[0.1, 0.2, 0.3]])

    result = er.get_embeddings_batch(["体温测量范围"])

    assert result == [[0.1, 0.2, 0.3]]
    call_kwargs = mock_create.call_args.kwargs
    assert call_kwargs["model"] == er.DASHSCOPE_EMBEDDING_MODEL
    assert call_kwargs["input"] == ["体温测量范围"]


@patch("embedding_retrieval.dashscope_client.embeddings.create")
def test_get_embeddings_batch_respects_batch_size_limit(mock_create):
    mock_create.return_value = _mock_embedding_response([[0.1]] * 10)

    texts = [f"text-{i}" for i in range(15)]
    er.get_embeddings_batch(texts)

    # DashScope text-embedding-v3 单批最多 10 条
    assert mock_create.call_count == 2
    assert len(mock_create.call_args_list[0].kwargs["input"]) == 10
    assert len(mock_create.call_args_list[1].kwargs["input"]) == 5


@patch("embedding_retrieval.GraphDatabase")
@patch("embedding_retrieval.get_embeddings_batch")
def test_find_similar_pairs_queries_neo4j_vector_index_and_maps_results_back(
    mock_get_embeddings, mock_graph_db
):
    node_a = {"hazard": "传感器漂移", "_source": "doc_a.md"}
    node_b = {"item": "高温线性度验证", "_source": "doc_b.md"}
    nodes = {"risks": [node_a], "tests": [node_b]}

    mock_get_embeddings.return_value = [[0.1, 0.2], [0.1, 0.2]]

    mock_session = MagicMock()
    mock_graph_db.driver.return_value.session.return_value.__enter__.return_value = mock_session

    risk_key = "risks::0::0"
    test_key = "tests::0::0"

    # 按调用顺序预设向量索引查询的返回结果：
    # 第1次查询（risks::0::0 的检索）命中 tests::0::0；
    # 第2次查询（tests::0::0 的检索）命中 risks::0::0 —— 这一对应该与第1次去重为同一对，不是两对。
    queryNodes_results = [
        [{"key": test_key, "score": 0.9}],
        [{"key": risk_key, "score": 0.9}],
    ]

    def run_side_effect(query, **kwargs):
        mock_result = MagicMock()
        if "CALL db.index.vector.queryNodes" in query:
            records = queryNodes_results.pop(0) if queryNodes_results else []
            mock_result.__iter__.return_value = iter(records)
        else:
            mock_result.__iter__.return_value = iter([])
        return mock_result

    mock_session.run.side_effect = run_side_effect

    pairs = er.find_similar_pairs(nodes, top_k=10, threshold=0.5)

    assert len(pairs) == 1
    assert pairs[0] in [(node_a, node_b), (node_b, node_a)]
    # 确认创建了向量索引
    create_index_calls = [
        c for c in mock_session.run.call_args_list
        if "CREATE VECTOR INDEX" in c.args[0]
    ]
    assert len(create_index_calls) == 1


@patch("embedding_retrieval.GraphDatabase")
@patch("embedding_retrieval.get_embeddings_batch")
def test_find_similar_pairs_returns_empty_when_no_candidate_nodes(mock_get_embeddings, mock_graph_db):
    result = er.find_similar_pairs({"requirements": []})

    assert result == []
    mock_get_embeddings.assert_not_called()
    mock_graph_db.driver.assert_not_called()
```

- [ ] **Step 3: 运行测试确认失败**

Run: `cd file_extractor && python -m pytest tests/test_embedding_retrieval.py -v`
Expected: FAIL，`ModuleNotFoundError: No module named 'embedding_retrieval'`

- [ ] **Step 4: 实现 embedding_retrieval.py**

```python
# file_extractor/embedding_retrieval.py
"""Step4 候选生成层③：向量召回（MAQD 多角度查询 + 阿里云 DashScope embedding + Neo4j 向量索引检索）。"""
from openai import OpenAI
from neo4j import GraphDatabase

from config import (
    DASHSCOPE_API_KEY, DASHSCOPE_EMBEDDING_MODEL, DASHSCOPE_BASE_URL,
    NEO4J_URI, NEO4J_AUTH,
)

dashscope_client = OpenAI(api_key=DASHSCOPE_API_KEY, base_url=DASHSCOPE_BASE_URL)

EMBEDDING_BATCH_SIZE = 10  # text-embedding-v3 单批最多 10 条文本
EMBEDDING_DIMENSIONS = 1024
SIMILARITY_THRESHOLD = 0.5
TOP_K = 10

NODE_SUMMARY_FIELDS = {
    "requirements": ["description"],
    "design_inputs": ["description"],
    "risks": ["hazard", "hazardous_situation"],
    "risk_controls": ["measure"],
    "tests": ["item", "expected_value"],
}


def build_multi_aspect_queries(node: dict, node_type: str) -> list[str]:
    """为节点生成多角度查询文本（MAQD：原描述 + 数值指标）。"""
    fields = NODE_SUMMARY_FIELDS.get(node_type, [])
    queries = []

    desc_parts = [str(node.get(f, "") or "") for f in fields]
    desc = " ".join(p for p in desc_parts if p).strip()
    if desc:
        queries.append(desc)

    value = str(node.get("value", "") or "")
    unit = str(node.get("unit", "") or "")
    if value:
        queries.append(f"{desc} {value}{unit}".strip())

    return [q for q in queries if q]


def get_embeddings_batch(texts: list[str]) -> list[list[float]]:
    """调用 DashScope text-embedding-v3，按 10 条/批分批请求。"""
    if not texts:
        return []
    all_embeddings = []
    for i in range(0, len(texts), EMBEDDING_BATCH_SIZE):
        batch = texts[i:i + EMBEDDING_BATCH_SIZE]
        response = dashscope_client.embeddings.create(
            model=DASHSCOPE_EMBEDDING_MODEL,
            input=batch,
        )
        all_embeddings.extend([item.embedding for item in response.data])
    return all_embeddings


def find_similar_pairs(nodes: dict, top_k: int = TOP_K,
                        threshold: float = SIMILARITY_THRESHOLD) -> list[tuple]:
    """对所有节点生成多角度查询向量，写入 Neo4j 向量索引，再用该索引检索语义相近的跨文档候选对。

    每个节点的每个查询角度对应一个临时 :EmbeddingRef 节点（key 格式
    "{node_type}::{node_index}::{query_index}"），查询时用 key 反查回
    Python 端的原始节点对象。每次运行先清空上一轮的 :EmbeddingRef 节点，
    避免跨运行残留干扰检索结果。
    """
    entries = []  # (key, node, query_text)
    for node_type in NODE_SUMMARY_FIELDS:
        for idx, node in enumerate(nodes.get(node_type, [])):
            for q_idx, query in enumerate(build_multi_aspect_queries(node, node_type)):
                entries.append((f"{node_type}::{idx}::{q_idx}", node, node_type, query))

    if not entries:
        return []

    texts = [e[3] for e in entries]
    embeddings = get_embeddings_batch(texts)
    key_to_node = {e[0]: e[1] for e in entries}

    driver = GraphDatabase.driver(NEO4J_URI, auth=NEO4J_AUTH)
    try:
        with driver.session() as session:
            session.run("""
                CREATE VECTOR INDEX embeddingRefIndex IF NOT EXISTS
                FOR (n:EmbeddingRef) ON (n.embedding)
                OPTIONS {indexConfig: {`vector.dimensions`: %d, `vector.similarity_function`: 'cosine'}}
            """ % EMBEDDING_DIMENSIONS)
            session.run("MATCH (n:EmbeddingRef) DETACH DELETE n")

            for (key, _node, node_type, _query), embedding in zip(entries, embeddings):
                session.run(
                    "CREATE (n:EmbeddingRef {key: $key, node_type: $node_type, embedding: $embedding})",
                    key=key, node_type=node_type, embedding=embedding,
                )

            pairs = []
            seen = set()
            for (key, node, _node_type, _query), embedding in zip(entries, embeddings):
                result = session.run(
                    """
                    CALL db.index.vector.queryNodes('embeddingRefIndex', $top_k, $embedding)
                    YIELD node, score
                    RETURN node.key AS key, score
                    """,
                    top_k=top_k + 1, embedding=embedding,  # +1 因为会查到自己
                )
                for record in result:
                    other_key, score = record["key"], record["score"]
                    if other_key == key or score < threshold:
                        continue
                    other_node = key_to_node.get(other_key)
                    if other_node is None or other_node.get("_source") == node.get("_source"):
                        continue
                    pair_id = tuple(sorted([id(node), id(other_node)]))
                    if pair_id in seen:
                        continue
                    seen.add(pair_id)
                    pairs.append((node, other_node))
    finally:
        driver.close()

    return pairs
```

- [ ] **Step 5: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/test_embedding_retrieval.py -v`
Expected: 6 passed

- [ ] **Step 6: Commit**

```bash
git add file_extractor/config.py file_extractor/embedding_retrieval.py file_extractor/tests/test_embedding_retrieval.py
git commit -m "feat: add DashScope embedding retrieval for Step4 (MAQD-style candidate layer)"
```

---

### Task 4：层② 图模式传播（Think-on-Graph）

**Files:**
- Create: `file_extractor/graph_pattern_propagation.py`
- Test: `file_extractor/tests/test_graph_pattern_propagation.py`

- [ ] **Step 1: 写失败的测试**

```python
# file_extractor/tests/test_graph_pattern_propagation.py
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

import graph_pattern_propagation as gpp


def test_count_two_hop_patterns_counts_type_sequences():
    edges = [
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-01", "to_id": "CM-01"},
        {"type": "VERIFIED_BY", "from_type": "risk_controls", "to_type": "tests", "from_id": "CM-01", "to_id": "T-01"},
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-02", "to_id": "CM-02"},
        {"type": "VERIFIED_BY", "from_type": "risk_controls", "to_type": "tests", "from_id": "CM-02", "to_id": "T-02"},
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-03", "to_id": "CM-03"},
    ]

    patterns = gpp.count_two_hop_patterns(edges)

    assert patterns[("MITIGATED_BY", "VERIFIED_BY")] == 2


def test_find_missing_next_hop_finds_node_without_second_hop():
    edges = [
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-01", "to_id": "CM-01"},
        {"type": "VERIFIED_BY", "from_type": "risk_controls", "to_type": "tests", "from_id": "CM-01", "to_id": "T-01"},
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-02", "to_id": "CM-02"},
        {"type": "VERIFIED_BY", "from_type": "risk_controls", "to_type": "tests", "from_id": "CM-02", "to_id": "T-02"},
        {"type": "MITIGATED_BY", "from_type": "risks", "to_type": "risk_controls", "from_id": "R-03", "to_id": "CM-03"},
        # CM-03 没有 VERIFIED_BY 出边 -> 缺失的下一跳
    ]
    nodes = {
        "risk_controls": [{"control_id": "CM-01"}, {"control_id": "CM-02"}, {"control_id": "CM-03"}],
        "tests": [{"test_id": "T-01"}, {"test_id": "T-02"}, {"test_id": "T-03"}],
    }

    missing = gpp.find_missing_next_hop(nodes, edges, min_frequency=2)

    cm03_candidates = [m for m in missing if m["from_id"] == "CM-03"]
    assert len(cm03_candidates) == 1
    assert cm03_candidates[0]["expected_relation"] == ("MITIGATED_BY", "VERIFIED_BY")
    assert len(cm03_candidates[0]["candidate_targets"]) == 3  # 全部 Test 节点作为候选


def test_find_missing_next_hop_ignores_low_frequency_patterns():
    edges = [
        {"type": "SCHEDULES", "from_type": "documents", "to_type": "plan_tasks", "from_id": "D1", "to_id": "P1"},
        {"type": "DEPENDS_ON", "from_type": "plan_tasks", "to_type": "plan_tasks", "from_id": "P1", "to_id": "P2"},
    ]
    nodes = {"plan_tasks": [{"name": "P1"}, {"name": "P2"}]}

    missing = gpp.find_missing_next_hop(nodes, edges, min_frequency=3)

    assert missing == []
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd file_extractor && python -m pytest tests/test_graph_pattern_propagation.py -v`
Expected: FAIL，`ModuleNotFoundError: No module named 'graph_pattern_propagation'`

- [ ] **Step 3: 实现 graph_pattern_propagation.py**

```python
# file_extractor/graph_pattern_propagation.py
"""Step4 候选生成层②：图模式传播（Think-on-Graph 思路）。

从已有边（文档内边 + 层①已发现的跨文档边）出发，统计高频二跳模式，
对只完成第一跳、缺第二跳的节点，把该类型全部候选目标节点纳入候选对。
"""
from collections import defaultdict

NODE_ID_FIELD = {
    "requirements": "req_id",
    "design_inputs": "di_id",
    "risks": "risk_id",
    "risk_controls": "control_id",
    "tests": "test_id",
    "plan_tasks": "name",
    "documents": "title",
}


def count_two_hop_patterns(edges: list[dict]) -> dict:
    """统计二跳边类型序列出现频次：(edge1_type, edge2_type) -> count。

    二跳指：edge1 的 to_id 等于某条 edge2 的 from_id（同一个中间节点）。
    """
    by_from = defaultdict(list)
    for e in edges:
        by_from[e["from_id"]].append(e)

    pattern_counts = defaultdict(int)
    for e1 in edges:
        for e2 in by_from.get(e1["to_id"], []):
            if e1 is e2:
                continue
            pattern_counts[(e1["type"], e2["type"])] += 1

    return dict(pattern_counts)


def find_missing_next_hop(nodes: dict, edges: list[dict], min_frequency: int = 3) -> list[dict]:
    """对高频二跳模式，找出只完成第一跳、缺第二跳的节点，把第二跳候选目标节点纳入候选。

    返回格式：[{"from_id": ..., "from_type": ..., "expected_relation": (type1, type2),
                "candidate_targets": [node, ...], "target_type": ...}, ...]
    """
    pattern_counts = count_two_hop_patterns(edges)
    high_freq_patterns = {p: c for p, c in pattern_counts.items() if c >= min_frequency}
    if not high_freq_patterns:
        return []

    # 为每个高频模式找出 edge1/edge2 的实际 from_type/to_type
    pattern_types = {}
    for e1 in edges:
        for e2 in edges:
            key = (e1["type"], e2["type"])
            if key in high_freq_patterns and key not in pattern_types:
                if e1["to_id"] == e2["from_id"]:
                    pattern_types[key] = (e1["to_type"], e2["to_type"])

    # 找出已完成第一跳的中间节点
    has_second_hop = set()
    for e in edges:
        pass
    second_hop_from_ids = {e["from_id"] for e in edges}

    completed_first_hop_by_pattern = defaultdict(set)
    for e in edges:
        for (t1, t2), count in high_freq_patterns.items():
            if e["type"] == t1:
                completed_first_hop_by_pattern[(t1, t2)].add(e["to_id"])

    results = []
    for pattern, intermediate_ids in completed_first_hop_by_pattern.items():
        if pattern not in pattern_types:
            continue
        intermediate_type, target_type = pattern_types[pattern]
        target_id_field = NODE_ID_FIELD.get(target_type, "name")
        candidate_targets = nodes.get(target_type, [])

        for mid_id in intermediate_ids:
            if mid_id in second_hop_from_ids:
                continue  # 第二跳已存在，不缺
            results.append({
                "from_id": mid_id,
                "from_type": intermediate_type,
                "expected_relation": pattern,
                "candidate_targets": candidate_targets,
                "target_type": target_type,
            })

    return results
```

- [ ] **Step 4: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/test_graph_pattern_propagation.py -v`
Expected: 3 passed

- [ ] **Step 5: Commit**

```bash
git add file_extractor/graph_pattern_propagation.py file_extractor/tests/test_graph_pattern_propagation.py
git commit -m "feat: add graph pattern propagation for Step4 (Think-on-Graph candidate layer)"
```

---

### Task 5：开放式 LLM 验证函数

**Files:**
- Modify: `file_extractor/step4_cross_doc_edges.py`
- Test: `file_extractor/tests/test_step4_cross_doc_edges.py`

- [ ] **Step 1: 追加失败的测试**

```python
# 追加到 file_extractor/tests/test_step4_cross_doc_edges.py

@patch("step4_cross_doc_edges.client.chat.completions.create")
def test_verify_candidates_open_llm_parses_known_and_new_relations(mock_create):
    mock_create.return_value = _mock_llm_response(
        "1. VERIFIED_BY\n2. 无关系\n3. 新关系：COMPONENT_OF"
    )
    candidates = [
        ({"control_id": "CM-01", "measure": "校准补偿"}, {"test_id": "T-12", "item": "线性度验证"}, "graph_pattern"),
        ({"control_id": "CM-02", "measure": "无关措施"}, {"test_id": "T-15", "item": "电池续航"}, "embedding"),
        ({"name": "下盖"}, {"name": "主机壳体"}, "bridge"),
    ]

    result = s4.verify_candidates_open_llm(candidates)

    assert result[0]["type"] == "VERIFIED_BY"
    assert result[0]["discovery_layer"] == "graph_pattern"
    assert len(result) == 2  # 第2条"无关系"被过滤
    assert result[1]["type"] == "COMPONENT_OF"
    assert result[1]["discovery_layer"] == "bridge"


def test_verify_candidates_open_llm_empty_candidates_returns_empty():
    assert s4.verify_candidates_open_llm([]) == []
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd file_extractor && python -m pytest tests/test_step4_cross_doc_edges.py -v`
Expected: FAIL，`AttributeError: module 'step4_cross_doc_edges' has no attribute 'verify_candidates_open_llm'`

- [ ] **Step 3: 实现 verify_candidates_open_llm**

在 [step4_cross_doc_edges.py](../../../file_extractor/step4_cross_doc_edges.py) 的 `_llm_match_batch` 函数之后（[第 575 行](../../../file_extractor/step4_cross_doc_edges.py#L575) 后）新增：

```python
OPEN_VERIFY_BATCH_SIZE = 20


def verify_candidates_open_llm(candidates: list[tuple]) -> list[dict]:
    """对层②③④产出的候选对做开放式 LLM 验证。

    candidates: [(node_a, node_b, discovery_layer), ...]
    未命中已知规则的候选，允许 LLM 直接给出"新关系：XXX"，不强制套用预定义类型。
    返回 [{"from": node_a, "to": node_b, "type": ..., "discovery_layer": ...}, ...]
    """
    if not candidates:
        return []

    all_results = []
    for i in range(0, len(candidates), OPEN_VERIFY_BATCH_SIZE):
        batch = candidates[i:i + OPEN_VERIFY_BATCH_SIZE]
        all_results.extend(_verify_batch_open_llm(batch))
    return all_results


def _verify_batch_open_llm(batch: list[tuple]) -> list[dict]:
    prompt = """你是医疗器械文档关系分析专家。

以下每一对节点是候选关系对，请判断它们之间是否存在关系：
- 如果存在已知关系类型（如 VERIFIED_BY、MITIGATED_BY、COVERS 等），直接输出该类型
- 如果存在关系但不属于已知类型，输出"新关系：你认为合适的类型名"
- 如果没有关系，输出"无关系"

按顺序逐条判断，格式：编号. 判断结果

"""
    for idx, (node_a, node_b, _layer) in enumerate(batch):
        desc_a = node_a.get("description") or node_a.get("measure") or node_a.get("item") or node_a.get("hazard") or node_a.get("name") or str(node_a)[:60]
        desc_b = node_b.get("description") or node_b.get("measure") or node_b.get("item") or node_b.get("hazard") or node_b.get("name") or str(node_b)[:60]
        prompt += f"{idx + 1}. [{desc_a[:80]}] <-> [{desc_b[:80]}]\n"

    try:
        response = client.chat.completions.create(
            model=LLM_MODEL,
            max_tokens=1000,
            messages=[{"role": "user", "content": prompt}],
        )
        content = response.choices[0].message.content or ""
    except Exception as e:
        print(f"    verify_candidates_open_llm ERROR: {e}", flush=True)
        return []

    results = []
    for line in content.strip().split("\n"):
        line = line.strip()
        if not line:
            continue
        m = re.match(r'(\d+)\.\s*(.+)', line)
        if not m:
            continue
        idx = int(m.group(1)) - 1
        verdict = m.group(2).strip()
        if idx < 0 or idx >= len(batch):
            continue
        if "无关系" in verdict:
            continue
        node_a, node_b, layer = batch[idx]
        if "新关系" in verdict:
            rel_type = verdict.split("：", 1)[-1].split(":", 1)[-1].strip()
        else:
            rel_type = verdict
        if not rel_type:
            continue
        results.append({
            "from": node_a,
            "to": node_b,
            "type": rel_type,
            "discovery_layer": layer,
        })

    return results
```

- [ ] **Step 4: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/test_step4_cross_doc_edges.py -v`
Expected: 4 passed

- [ ] **Step 5: Commit**

```bash
git add file_extractor/step4_cross_doc_edges.py file_extractor/tests/test_step4_cross_doc_edges.py
git commit -m "feat: add open-ended LLM verification for layer②③④ candidates"
```

---

### Task 6：候选合并编排，接入 main()

**Files:**
- Modify: `file_extractor/step4_cross_doc_edges.py`
- Test: `file_extractor/tests/test_step4_cross_doc_edges.py`

- [ ] **Step 1: 追加失败的测试**

```python
# 追加到 file_extractor/tests/test_step4_cross_doc_edges.py

def test_build_id_to_type_index_maps_ids_to_node_types():
    nodes = {
        "risk_controls": [{"control_id": "CM-01"}],
        "tests": [{"test_id": "T-12"}],
    }

    index = s4._build_id_to_type_index(nodes)

    assert index["CM-01"] == "risk_controls"
    assert index["T-12"] == "tests"


def test_normalize_step2_edges_resolves_types_and_skips_unresolvable():
    id_to_type = {"CM-01": "risk_controls", "T-12": "tests"}
    existing_edges = [
        {"type": "VERIFIED_BY", "from": "CM-01", "to": "T-12", "properties": {}},
        {"type": "SIGNED", "from": "某个查不到类型的标识符", "to": "也查不到", "properties": {}},
    ]

    normalized = s4._normalize_step2_edges(existing_edges, id_to_type)

    assert len(normalized) == 1
    assert normalized[0] == {
        "type": "VERIFIED_BY",
        "from_id": "CM-01", "from_type": "risk_controls",
        "to_id": "T-12", "to_type": "tests",
    }


@patch("step4_cross_doc_edges.verify_candidates_open_llm")
@patch("step4_cross_doc_edges.gpp.find_missing_next_hop")
@patch("step4_cross_doc_edges.er.find_similar_pairs")
@patch("step4_cross_doc_edges.be.find_bridge_entities")
def test_discover_open_candidates_merges_and_dedupes_all_layers(
    mock_bridge, mock_embedding, mock_graph_pattern, mock_verify
):
    node_a = {"control_id": "CM-01"}
    node_b = {"test_id": "T-12"}
    node_c = {"test_id": "T-15"}

    mock_bridge.return_value = [(node_a, node_b)]
    mock_embedding.return_value = [(node_a, node_b)]  # 与桥接层产出同一对，去重后应只算一次
    mock_graph_pattern.return_value = [
        {"from_id": "CM-01", "from_type": "risk_controls",
         "expected_relation": ("MITIGATED_BY", "VERIFIED_BY"),
         "candidate_targets": [node_c], "target_type": "tests"},  # 指向不同节点，应保留为独立候选
    ]
    mock_verify.return_value = [
        {"from": node_a, "to": node_b, "type": "VERIFIED_BY", "discovery_layer": "bridge"},
        {"from": node_a, "to": node_c, "type": "VERIFIED_BY", "discovery_layer": "graph_pattern"},
    ]

    result = s4.discover_open_candidates(
        {"risk_controls": [node_a], "tests": [node_b, node_c]}, []
    )

    assert len(result) == 2
    # 验证函数应收到去重后的候选：(a,b) 桥接+向量召回重复算1对，(a,c) 图模式单独1对，共2对，不是3对
    verify_call_candidates = mock_verify.call_args.args[0]
    assert len(verify_call_candidates) == 2
```

- [ ] **Step 2: 运行测试确认失败**

Run: `cd file_extractor && python -m pytest tests/test_step4_cross_doc_edges.py -v`
Expected: FAIL，`AttributeError: module 'step4_cross_doc_edges' has no attribute '_build_id_to_type_index'`（以及 `discover_open_candidates` 同理未定义）

- [ ] **Step 3: 实现 discover_open_candidates 并接入 main()**

在 `step4_cross_doc_edges.py` 顶部 import 区域（[第 8-17 行](../../../file_extractor/step4_cross_doc_edges.py#L8-L17)）新增：

```python
import bridge_entities as be
import embedding_retrieval as er
import graph_pattern_propagation as gpp
```

在 `verify_candidates_open_llm`/`_verify_batch_open_llm` 之后新增：

```python
def _node_id_field_for(node_type: str) -> str:
    return gpp.NODE_ID_FIELD.get(node_type, "name")


def _build_id_to_type_index(nodes: dict) -> dict:
    """构建 id值 -> node_type 的反查表。

    Step2 产出的文档内边（existing_edges）只有 {type, from, to}，没有携带
    节点类型信息；图模式传播需要知道每条边两端是什么类型才能统计模式，
    这里通过节点的唯一标识字段反查回类型。
    """
    index = {}
    for node_type, items in nodes.items():
        id_field = gpp.NODE_ID_FIELD.get(node_type)
        if not id_field:
            continue
        for item in items:
            id_val = str(item.get(id_field, "") or "")
            if id_val:
                index[id_val] = node_type
    return index


def _normalize_step2_edges(existing_edges: list[dict], id_to_type: dict) -> list[dict]:
    """把 Step2 的 {type, from, to} 边转换成图模式传播需要的
    {type, from_id, from_type, to_id, to_type} 形状。两端标识符查不到类型的边跳过
    （查不到通常是因为 from/to 不是某个已知节点类型的唯一标识，无法参与模式统计）。
    """
    normalized = []
    for e in existing_edges:
        from_id = str(e.get("from", "") or "")
        to_id = str(e.get("to", "") or "")
        from_type = id_to_type.get(from_id)
        to_type = id_to_type.get(to_id)
        if not from_type or not to_type:
            continue
        normalized.append({
            "type": e.get("type", ""),
            "from_id": from_id, "from_type": from_type,
            "to_id": to_id, "to_type": to_type,
        })
    return normalized


def discover_open_candidates(nodes: dict, layer1_edges: list[dict]) -> list[dict]:
    """合并层②③④候选，去重后送开放式 LLM 验证，返回最终边列表。

    每一层独立失败不应中断整体流程（设计文档第6节降级策略）：
    某层抛异常时跳过该层，记录警告，继续用其余层的候选。
    """
    raw_candidates = []  # (node_a, node_b, layer)

    try:
        for a, b in be.find_bridge_entities(nodes):
            raw_candidates.append((a, b, "bridge"))
    except Exception as e:
        print(f"    [WARN] bridge_entities layer failed, skipping: {e}", flush=True)

    try:
        for a, b in er.find_similar_pairs(nodes):
            raw_candidates.append((a, b, "embedding"))
    except Exception as e:
        print(f"    [WARN] embedding_retrieval layer failed, skipping: {e}", flush=True)

    try:
        missing_hops = gpp.find_missing_next_hop(nodes, layer1_edges, min_frequency=3)
    except Exception as e:
        print(f"    [WARN] graph_pattern_propagation layer failed, skipping: {e}", flush=True)
        missing_hops = []

    for m in missing_hops:
        from_node = next(
            (n for n in nodes.get(m["from_type"], [])
             if str(n.get(_node_id_field_for(m["from_type"]), "")) == str(m["from_id"])),
            None,
        )
        if from_node is None:
            continue
        for target in m["candidate_targets"]:
            raw_candidates.append((from_node, target, "graph_pattern"))

    # 去重：同一对节点（不分先后顺序）只保留一次，优先保留先出现的层标签
    seen = set()
    deduped = []
    for a, b, layer in raw_candidates:
        key = tuple(sorted([id(a), id(b)]))
        if key in seen:
            continue
        seen.add(key)
        deduped.append((a, b, layer))

    return verify_candidates_open_llm(deduped)
```

修改 [`main()`](../../../file_extractor/step4_cross_doc_edges.py#L619-L686) 的开头部分，把：

```python
def main():
    print("=== Step 4: Cross-Document Relationship Discovery ===")
    print(f"Loading {MERGED_PATH.name}...")
    nodes, existing_edges, claims = load_graph()

    all_cross_edges = []
    for i, guide in enumerate(REGULATORY_GUIDES):
```

改为：

```python
def main():
    print("=== Step 4: Cross-Document Relationship Discovery ===")
    print(f"Loading {MERGED_PATH.name}...")
    nodes, existing_edges, claims = load_graph()

    all_cross_edges = []
    for i, guide in enumerate(REGULATORY_GUIDES):
```

（层①循环本身不变）在层①循环结束、去重之前（[第 639 行](../../../file_extractor/step4_cross_doc_edges.py#L639) `# Deduplicate` 之前）插入开放式候选发现：

```python
    # Open-ended candidate discovery (layers ②③④)
    print(f"\n=== Open candidate discovery (graph pattern + embedding + bridge entities) ===")
    id_to_type = _build_id_to_type_index(nodes)
    layer1_edges_for_pattern = [
        {
            "type": guide["edge_type"],
            "from_id": get_node_id(s, guide["source_type"]),
            "from_type": guide["source_type"],
            "to_id": get_node_id(t, guide["target_type"]),
            "to_type": guide["target_type"],
        }
        for guide, s, t, conf in all_cross_edges
    ] + _normalize_step2_edges(existing_edges, id_to_type)
    open_edges = discover_open_candidates(nodes, layer1_edges_for_pattern)
    print(f"    Found {len(open_edges)} edges from open candidate discovery")
```

- [ ] **Step 4: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/test_step4_cross_doc_edges.py -v`
Expected: 7 passed

- [ ] **Step 5: 把 open_edges 并入最终输出**

修改 `main()` 中保存结果的部分（[第 658-673 行](../../../file_extractor/step4_cross_doc_edges.py#L658-L673)），把：

```python
    # Save results
    output_edges = []
    for guide, s, t, conf in unique_edges:
        output_edges.append({
            "type": guide["edge_type"],
            "from_type": guide["source_type"],
            "from_id": get_node_id(s, guide["source_type"]),
            "from_source": s.get("_source", ""),
            "to_type": guide["target_type"],
            "to_id": get_node_id(t, guide["target_type"]),
            "to_source": t.get("_source", ""),
            "confidence": conf,
            "cross_doc": True,
            "standard": guide["standard"],
            "guide_name": guide["name"],
        })
```

改为：

```python
    # Save results
    output_edges = []
    for guide, s, t, conf in unique_edges:
        output_edges.append({
            "type": guide["edge_type"],
            "from_type": guide["source_type"],
            "from_id": get_node_id(s, guide["source_type"]),
            "from_source": s.get("_source", ""),
            "to_type": guide["target_type"],
            "to_id": get_node_id(t, guide["target_type"]),
            "to_source": t.get("_source", ""),
            "confidence": conf,
            "cross_doc": True,
            "standard": guide["standard"],
            "guide_name": guide["name"],
            "discovery_layer": "rule",
        })

    for oe in open_edges:
        from_node, to_node = oe["from"], oe["to"]
        output_edges.append({
            "type": oe["type"],
            "from_type": "",
            "from_id": str(from_node.get("description") or from_node.get("measure") or from_node.get("item") or from_node.get("hazard") or from_node.get("name") or "")[:80],
            "from_source": from_node.get("_source", ""),
            "to_type": "",
            "to_id": str(to_node.get("description") or to_node.get("measure") or to_node.get("item") or to_node.get("hazard") or to_node.get("name") or "")[:80],
            "to_source": to_node.get("_source", ""),
            "confidence": "medium",
            "cross_doc": True,
            "standard": "",
            "guide_name": f"开放发现（{oe['discovery_layer']}）",
            "discovery_layer": oe["discovery_layer"],
        })
```

- [ ] **Step 6: 运行测试确认通过**

Run: `cd file_extractor && python -m pytest tests/ -v`
Expected: 全部通过

- [ ] **Step 7: Commit**

```bash
git add file_extractor/step4_cross_doc_edges.py file_extractor/tests/test_step4_cross_doc_edges.py
git commit -m "feat: merge layer②③④ candidates and wire into Step4 main()"
```

---

### Task 7：样本数据人工验证

**Files:**
- 无新文件 — 在已有的 `output/merged_graph.json` 上运行验证

- [ ] **Step 1: 备份现有 Step4 输出**

```bash
cd file_extractor
cp output/cross_doc_edges.json output/cross_doc_edges_before.json
cp output/cross_doc_report.md output/cross_doc_report_before.md
```

- [ ] **Step 2: 确认 Neo4j 容器运行中**

```bash
docker ps --filter "name=neo4j-poc" --format "{{.Names}}: {{.Status}}"
```
Expected: `neo4j-poc: Up ...`（如未运行，`docker start neo4j-poc`）

- [ ] **Step 3: 重新运行 Step4**

Run: `cd file_extractor && python step4_cross_doc_edges.py`
Expected: 命令正常结束，打印 `=== Step 4 Complete! ===`，日志里能看到"Open candidate discovery"部分的发现数量

- [ ] **Step 4: 对比新旧跨文档边数量和 discovery_layer 分布**

```bash
cd file_extractor
python -c "
import json
before = json.loads(open('output/cross_doc_edges_before.json', encoding='utf-8').read())
after = json.loads(open('output/cross_doc_edges.json', encoding='utf-8').read())
print(f'旧版总数: {len(before)}')
print(f'新版总数: {len(after)}')
from collections import Counter
print('新版 discovery_layer 分布:', Counter(e.get('discovery_layer', 'rule') for e in after))
"
```

人工检查：抽 5-10 条 `discovery_layer` 为 `graph_pattern`/`embedding`/`bridge` 的边，确认这些是规则表里没有、但确实合理的新发现关系，而不是噪音。这一步不写自动化断言，按设计文档"人工抽样审查"的约定来判断。

- [ ] **Step 5: 清理备份文件**

确认验证结果满意后：

```bash
cd file_extractor
rm output/cross_doc_edges_before.json output/cross_doc_report_before.md
```

- [ ] **Step 6: Commit（如有为修复发现问题产生的代码改动）**

视验证结果决定是否需要额外修复提交。

---

## 完成后

Step4 四层候选生成改造完成并验证后，PT9L 文档一致性审查系统的 P0 改造（Step2 + Step4）全部完成，可以考虑评估是否对全部 254 份文件全量重跑管线。
