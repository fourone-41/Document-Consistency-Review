# 跨文件关系抽取：相关技术详解
> 针对 PT9L 红外体温计 DHF/DMR 文档一致性审查系统
> 生成日期：2026-06-12

---

## 导读：技术地图

```
你们的问题
├── 单文件内长距离关系       → A. Document-level RE
│   ├── ATLOP（2021）        理论基础，局部上下文思路
│   ├── DREEAM（2023）       证据句子 → 对应你们的精确定位需求
│   └── AutoRE（2024）       LLM做DocRE，有开源代码可直接参考
│
├── 跨文件实体-关系-实体     → B. Cross-document RE
│   ├── CodRED（2021）       领域奠基，文本路径构建代码可借鉴
│   ├── KXDocRE（2024）      领域知识注入 → 对应你们的ISO法规引导
│   ├── HCRE（2025）         层级树分类 → 直接改造Step4架构
│   └── MAQD（2025）         多角度证据召回 → 解决同义表述遗漏
│
└── 多文件图上的多跳推理      → C. GraphRAG系列
    ├── GraphRAG（微软2024）  社区检测 → 组织审查单元
    └── LightRAG（2024）      双层检索 → 你们规模更合适
```

---

## A. Document-level RE（文档级关系抽取）

### A1. ATLOP
**Document-Level Relation Extraction with Adaptive Thresholding and Localized Context Pooling**
Zhou et al., AAAI 2021 | [GitHub](https://github.com/wzhouad/ATLOP)

#### 解决的问题

传统关系抽取是句子级别的：给一句话，判断句子里两个实体是什么关系。但真实文档里，一对实体的关系往往需要跨多个句子甚至多个段落才能判断，比如：

```
第1段：Risk-01 涉及红外传感器在高温环境下的漂移问题
第3段：为确保测量精度，所有批次出厂前须完成校准流程
第7段：T-12 校准验证测试覆盖 35-42℃ 范围内的传感器线性度
```

这三段放在一起才能推断 Risk-01 VERIFIED_BY T-12，但没有一句话单独说明这个关系。

另外还有一个问题：同一个实体节点，和不同的实体配对时，需要的上下文是不一样的。比如"测量精度"这个节点，和"设计输入"配对时要看需求章节，和"测试报告"配对时要看验证章节——如果用同一个实体 embedding 来做所有配对，信息就错乱了。

#### 核心技术

**① 局部上下文池化（Localized Context Pooling）**

为每个实体对 (eₛ, eₒ) 单独计算一个上下文向量，而不是所有实体对共用同一个。

具体做法：

```
1. 用 BERT 对整个文档编码，得到每个 token 的向量 H 和注意力矩阵 A
2. 对实体对 (eₛ, eₒ)，计算它们之间的注意力分布 q(s,o)
   —— 这个分布告诉模型"判断这对实体的关系时，应该关注文档的哪些位置"
3. 用 q(s,o) 对 H 做加权求和，得到这对实体专属的上下文向量 c(s,o)
4. 最终的实体对表示 = 实体向量 + 专属上下文向量
```

直觉上就是：判断 Risk-01 和 T-12 的关系时，模型会自动把注意力集中在"校准""传感器漂移""验证"这些词上，而不是被文档里其他无关内容干扰。

**② 自适应阈值（Adaptive Thresholding）**

文档级 RE 是多标签问题——两个实体之间可能同时存在多种关系（比如 A 既 DERIVES_FROM B，又 REFERENCES B）。传统方法用固定阈值来决定"得分超过多少才算有这条关系"，但不同实体对的得分分布差异很大，一个固定阈值无法适应所有情况。

ATLOP 为每个实体对学习一个专属阈值：

```
对实体对 (eₛ, eₒ)：
  关系得分向量 = [score_r1, score_r2, ..., score_rN]  ← N种关系
  自适应阈值   = f(eₛ表示, eₒ表示)                   ← 这对实体专属的阈值
  输出关系集合 = { rᵢ | score_rᵢ > 自适应阈值 }
```

#### 和你们项目的结合

你们 Step2 做单文件内边抽取时，prompt 目前大概是：

```
给定节点A和节点B，判断它们之间的关系类型。
节点A：[description]
节点B：[description]
```

参考 ATLOP 的局部上下文思路，可以改成：

```
给定节点A和节点B，以及它们在文档中共同出现的上下文，判断关系类型。
节点A：[description]，出现在第X章第Y段
节点B：[description]，出现在第X章第Z段
共同上下文（两个节点周围的文本片段）：
  [节点A周围±3句]
  [节点B周围±3句]
  [两个节点之间的桥接段落（如有）]
```

这样 Claude 的判断依据更充分，尤其对于隐式关系（两个节点没有直接共现，但上下文里有逻辑联系）效果提升明显。

---

### A2. DREEAM
**Guiding Attention with Evidence for Improving Document-Level Relation Extraction**
Ma et al., EACL 2023

#### 解决的问题

做完关系抽取之后，还需要知道"凭什么说 A VERIFIED_BY B"——即支持这条关系的证据句子是哪几句。这有两个用途：一是提高可信度和可解释性，二是审查报告里需要精确定位。

之前做法是单独训练一个证据句子分类器，但这会导致内存消耗翻倍，而且证据标注数据很稀缺。

#### 核心技术

DREEAM 的核心洞察：ATLOP 里已经计算了"实体对在文档中应关注哪些位置"的注意力分布 q(s,o)，这个分布本身就蕴含了"哪些句子是证据"的信息——注意力权重高的位置，往往就是证据句子所在位置。

因此，不需要单独的证据分类器，只需要用已有的注意力分布来定位证据：

```
对实体对 (eₛ, eₒ)：
  q(s,o) = 注意力分布（已有）
  对每个句子 sᵢ，计算该句子的 token 的平均注意力权重
  注意力权重前 k 的句子 → 证据句子
```

训练时加一个辅助监督信号：让注意力分布在证据句子的 token 上有更高的权重。测试时直接用注意力权重排名来输出证据，不增加任何额外参数。

#### 和你们项目的结合

在 Step2 和 Step4 的输出 JSON 里，给每条边加一个 `evidence_spans` 字段：

```json
{
  "source": "Risk-01",
  "target": "Test-T12",
  "relation": "VERIFIED_BY",
  "confidence": 0.87,
  "evidence_spans": [
    {
      "doc_id": "06_硬件设计方案",
      "section": "3.2 校准流程",
      "text": "出厂前须完成传感器漂移校准，覆盖35-42℃范围",
      "char_offset": [1240, 1298]
    },
    {
      "doc_id": "12_测试报告",
      "section": "4.1 T-12 校准验证",
      "text": "T-12 测试验证了红外传感器在高温环境下的线性度",
      "char_offset": [334, 385]
    }
  ]
}
```

在 Step4 的 prompt 里，明确要求 Claude 输出支持关系判断的原文依据：

```
判断完关系类型后，请同时输出：
1. 支持这个判断的原文片段（来自源文档和目标文档各1-2句）
2. 原文所在的章节名称
这些将作为审查报告的精确定位依据。
```

这直接满足了你们"每条问题精确双向定位"的核心需求。

---

### A3. AutoRE
**Document-Level Relation Extraction with Large Language Models**
Xue et al., ACL 2024 | [GitHub](https://github.com/THUDM/AutoRE)

#### 解决的问题

现有 DocRE 方法大多预设"关系类型是固定的且已知的"，但实际场景里关系类型可能不完备，或者需要 LLM 来做。直接让 LLM 从大量关系类型里选择效果不好，需要一个结构化的方法。

#### 核心技术

**RHF（Relation-Head-Facts）范式**：把文档级 RE 分解为三个串行子任务：

```
任务1：Relation Detection（关系检测）
  输入：整个文档
  输出：这个文档里存在哪些关系类型？
  → 输出：[VERIFIED_BY, MITIGATED_BY, DERIVES_FROM]

任务2：Head Entity Identification（头实体识别）
  输入：文档 + 某种关系类型（比如 VERIFIED_BY）
  输出：哪些实体是这种关系的"发出方"（head entity）？
  → 输出：[Risk-01, Risk-03, DesignInput-07]

任务3：Tail Entity & Facts Prediction（尾实体和事实预测）
  输入：文档 + 关系类型 + 头实体
  输出：对应的尾实体是什么？有哪些补充事实？
  → 输出：Risk-01 VERIFIED_BY Test-T12（证据：第4章第3段）
```

每个子任务更聚焦，LLM 的错误率明显低于一步到位。三个任务可以用同一个 LLM（通过不同 prompt 或 fine-tuning 的不同 LoRA adapter 来区分）。

#### 和你们项目的结合

Step1 和 Step2 目前是两个独立步骤，但 Step2 仍然是"给节点A和节点B，判断关系"的模式，本质上还是一步到位。参考 AutoRE 可以改成：

```
Step2a（新）：关系类型枚举
  输入：文档全文 + 所有已抽取的节点列表
  问题：这个文档的节点之间，存在哪些 edges.yaml 里定义的关系类型？
  输出：[MITIGATED_BY, VERIFIED_BY, PART_OF] ← 只列出存在的类型

Step2b（新）：按关系类型逐一找实体对
  对每个识别出的关系类型：
    输入：文档 + 该关系类型的定义 + 所有节点
    问题：满足这种关系的实体对有哪些？
    输出：[(Risk-01, RiskControl-CM03), ...]
```

这样的好处是：Step2a 先过滤掉文档里根本不存在的关系类型，Step2b 只在有意义的关系类型上做配对，大幅减少无效的实体对枚举。

---

## B. Cross-document RE（跨文档关系抽取）

### B1. CodRED
**A Cross-Document Relation Extraction Dataset for Acquiring Knowledge in the Wild**
Yao et al., EMNLP 2021 | [GitHub](https://github.com/thunlp/CodRED)

#### 解决的问题

知识库（如 Wikidata）里超过一半的关系事实，涉及的两个实体并不共现于同一个文档。比如"某个风险控制措施验证了某个风险"，这条事实可能需要从风险分析文件和测试报告两个文档合起来才能推断。

#### 任务定义和数据结构

CodRED 定义的标准任务格式：

```
输入：
  头实体 eₕ（来自文档A）
  尾实体 eₜ（来自文档B）
  文本路径 P = [文档A的段落, 桥接文档C的段落, 文档B的段落]

输出：
  eₕ 和 eₜ 之间的关系类型（从276种预定义关系中选）
  或 NA（无直接关系）
```

**文本路径（Text Path）** 是核心概念：两个文档里的实体往往通过一个"桥接实体"相连，文本路径就是从头实体出发，经过桥接实体，到达尾实体的一条证据链。

比如：

```
文档A（风险分析）：Risk-01 涉及"红外传感器"的漂移
       ↓ 桥接实体："红外传感器"同时出现在两个文档
文档B（测试报告）："红外传感器"的校准验证由 T-12 完成
→ 文本路径：[Risk-01描述] + [红外传感器的桥接描述] + [T-12描述]
→ 推断：Risk-01 VERIFIED_BY T-12
```

**两种实验设定**：
- **Closed setting**：已知哪些文档路径是相关的（给你 gold path）
- **Open setting**：需要自己从大量文档里检索出相关路径，再推断关系

#### 基线模型结构

```
Step1（文档检索）：给定头尾实体，从文档库里找相关文档，构建候选文本路径
Step2（证据提取）：从候选路径中选择最相关的句子作为证据
Step3（关系分类）：基于证据做关系分类
```

#### 和你们项目的结合

你们的场景比 CodRED 更有利：文档集合已知（254份），不需要做 open setting 的检索，直接用 closed setting 的思路。

核心可借鉴的是**文本路径构建逻辑**：

```python
def build_text_path(node_a, node_b, merged_graph):
    """
    找到 node_a 和 node_b 之间的桥接路径
    桥接实体 = 同时被两个文档引用的 Product / Identifier / Person 节点
    """
    # 1. 找 node_a 所在文档引用的锚点实体
    anchors_a = get_anchor_entities(node_a.doc_id, merged_graph)
    # 2. 找 node_b 所在文档引用的锚点实体
    anchors_b = get_anchor_entities(node_b.doc_id, merged_graph)
    # 3. 找共同锚点（桥接实体）
    bridge_entities = anchors_a & anchors_b
    # 4. 构建文本路径
    path = [
        get_context(node_a),           # 节点A周围的文本
        get_bridge_context(bridge_entities),  # 桥接实体的描述
        get_context(node_b)            # 节点B周围的文本
    ]
    return path
```

把这个文本路径作为 Claude 的输入，而不只是两个节点的 description，关系判断的准确率会明显提升——因为 Claude 看到了完整的推理链，而不是两个孤立的节点。

---

### B2. KXDocRE
**Knowledge-Driven Cross-Document Relation Extraction**
Jain et al., arXiv 2405.13546, 2024

#### 解决的问题

跨文档 RE 的难点之一是：两个实体的描述可能非常简短或术语化，仅凭原文很难判断关系。如果模型能知道"这两个实体在领域知识里是什么"，判断会容易很多。

比如："Risk-01"和"T-12"这两个编号，LLM 光凭编号几乎无法判断关系。但如果告诉它"Risk-01 是 ISO 14971 框架下的风险项，T-12 是 ISO 13485 7.3.6 条款要求的设计验证测试"，那 ISO 14971 第8章明确规定了风险控制措施必须通过测试验证——关系就很清楚了。

#### 核心技术

**KXDocRE 框架的三个组件**：

```
组件1：实体知识嵌入（Entity Knowledge Embedding）
  对每个实体，除了原文描述，还注入：
  - 实体类型（Risk / Test / DesignInput ...）
  - 实体在领域知识库里的已知属性
  - 实体所属的标准框架（ISO 13485 / ISO 14971 ...）

组件2：跨文档上下文融合（Cross-document Context Fusion）
  把两个文档的相关段落编码后融合，让模型看到两个文档的"对话"
  而不是孤立地看每个文档

组件3：知识引导的关系分类（Knowledge-guided Relation Classification）
  在做关系分类时，把领域规则作为约束：
  "根据 ISO 14971，风险类实体和测试类实体之间
   最可能的关系是 VERIFIED_BY 或 MITIGATED_BY，
   请优先在这两种关系里判断"
```

#### 和你们项目的结合

你们已经有了最重要的资产：ISO 法规知识（体现在 Step4 的法规知识引导表里）。把这个思路系统化到 prompt 里：

```
【跨文档关系判断 Prompt 模板】

## 节点信息
节点A（来自：{doc_a_name}，类型：{node_a_type}）
描述：{node_a_description}
所属法规框架：{node_a_regulatory_context}  ← 新增

节点B（来自：{doc_b_name}，类型：{node_b_type}）
描述：{node_b_description}
所属法规框架：{node_b_regulatory_context}  ← 新增

## 法规知识引导
根据 {applicable_standard}，{node_a_type} 和 {node_b_type} 之间
常见的关系包括：{knowledge_guided_candidates}
具体条款：{standard_clause}

## 文本路径
{text_path_from_codred_method}

## 任务
从 edges.yaml 定义的关系类型中，判断节点A和节点B之间最可能的关系。
如果以上法规知识引导的关系与文本证据一致，优先选择该关系。
```

这比纯粹依赖原文描述判断精度高很多，尤其对于那些描述简短或者隐式引用的节点。

---

### B3. HCRE
**LLM-based Hierarchical Classification for Cross-Document Relation Extraction with a Prediction-then-Verification Strategy**
Ma et al., arXiv 2604.07937, 2025 年 4 月

#### 解决的问题

论文做了一个实验：直接让 LLM（GPT-4 等）从 CodRED 的 276 种关系里做分类，发现效果**不如**专门训练的小模型（BERT-based）。原因分析：关系种类太多，LLM 很难在一次推理里同时考虑所有候选关系的语义区别，特别是语义相近的关系之间容易混淆。

这和你们的情况完全一样——edges.yaml 里 30+ 种边类型，很多语义相近：

```
容易混淆的组：
  VERIFIED_BY vs COVERS vs REPORTED_IN
  MITIGATED_BY vs CONSTRAINED_BY vs ADDRESSED_IN
  DERIVES_FROM vs REFERENCES vs RELATES_TO
```

#### 核心技术

**层级关系树（Hierarchical Relation Tree）**：把所有关系类型按语义组织成树形结构，LLM 从根节点开始，每次只在当前节点的子节点里做选择，逐层向下。

**预测-验证策略（Prediction-then-Verification）**：每层分类后，不直接用分类结果，而是再做一次验证：

```
第1步（预测）：
  "节点A和节点B的关系属于哪个大类？
   选项：[结构类 / 业务语义类 / 验证测试类 / 对齐裁决类]"
  → 输出：验证测试类

第2步（验证）：
  "你刚才判断属于【验证测试类】，
   请确认：以下哪个描述更符合这两个节点的实际关系？
   A. 测试直接验证了某个风险或需求（VERIFIED_BY）
   B. 测试覆盖了某个功能需求（COVERS）
   C. 测试结果记录在某个报告里（REPORTED_IN）
   D. 测试对某个指标进行测量（MEASURES）"
  → 输出：A（VERIFIED_BY），置信度 0.91

第3步（跨层验证，仅低置信度时触发）：
  "你判断了 VERIFIED_BY，但请检查：
   是否有可能其实是 MITIGATED_BY（控制措施类）？
   判断依据：节点A是风险项还是控制措施？"
  → 输出：确认是 VERIFIED_BY（节点A是 Risk 类型，不是 RiskControl）
```

**关键细节：树的构建方式**

树的结构不是随意的，要基于**关系之间的混淆矩阵**来构建：

```
1. 先做小规模实验（用你们已有的10个样本文件）
2. 让 Claude 做一步到位的关系分类，记录所有分类结果
3. 分析哪些关系对之间最容易混淆
4. 把容易混淆的关系放在同一个子树里（让层级树把它们分开）
5. 不容易混淆的关系可以更早在树上分叉
```

#### 对你们项目的具体树结构建议

```
跨文件关系根节点
│
├── [Q1] 这条关系是关于"信息在哪里"还是"业务实体之间的关联"？
│
├── 结构/定位类（信息在哪里）
│   ├── [Q2] 是包含关系还是引用关系？
│   ├── 包含：PART_OF
│   └── 引用：STATED_IN / INDEXES / LISTS_FILE
│
└── 业务实体关联类
    ├── [Q2] 关系的方向是"派生/追溯"还是"验证/测试"还是"风险管控"？
    │
    ├── 追溯链
    │   ├── [Q3] 是直接派生还是松散引用？
    │   ├── 直接派生：DERIVES_FROM / IMPLEMENTS
    │   └── 松散引用：REFERENCES / RELATES_TO
    │
    ├── 验证测试链
    │   ├── [Q3] 验证的目标是什么？
    │   ├── 验证需求/风险：VERIFIED_BY
    │   ├── 覆盖功能：COVERS
    │   ├── 记录结果：REPORTED_IN
    │   └── 测量指标：MEASURES / HAS_MEASUREMENT
    │
    └── 风险管控链
        ├── [Q3] 是控制还是约束还是追踪？
        ├── 控制措施：MITIGATED_BY
        ├── 约束：CONSTRAINED_BY
        └── 响应：ADDRESSED_IN
```

每个 [Q] 节点对应一次 LLM 调用，每次只有 3-5 个选项，平均 2-3 次调用就能到达叶节点。

---

### B4. MAQD
**Evidence Selection via Multi-Aspect Query Diversification for Cross-Document Relation Extraction**
Springer JIIS, 2025

#### 解决的问题

在判断跨文档关系之前，需要先从长文档里找到"支持这条关系"的证据句子。直接用节点的 description 做向量检索存在一个问题：同一个事实可能用很多不同表述出现在不同文档里，单一查询只能命中其中一种表述，导致召回不全。

```
"传感器漂移导致测量误差"这个 Risk，
在不同文档里可能被表述为：
  风险分析：  "红外传感器在高温下的偏移量超出允许范围"
  控制措施：  "针对温度漂移问题的校准补偿方案"
  测试报告：  "高温环境传感器线性度验证"
  设计输入：  "体温计在35-42℃范围内的测量精度要求"
```

单一查询"传感器漂移"只能找到部分匹配，MAQD 用多个不同角度的查询来解决这个问题。

#### 核心技术

**多角度查询生成（Multi-Aspect Query Diversification）**：

```
对节点 Risk-01（"红外传感器偏移导致测量误差"），生成多个查询：

角度1（问题描述）："传感器漂移 偏移 误差"
角度2（影响对象）："测量精度 准确度 允差"
角度3（物理机制）："红外传感器 温度 线性度"
角度4（法规视角）："ISO 14971 风险 危害"
角度5（解决方向）："校准 补偿 验证"
```

用这 5 个查询分别检索，取结果的并集，再用重排模型（cross-encoder）对候选证据打分，选出最终的证据句子集合。

**重排与聚合（Reranking & Aggregation）**：

```
候选证据集合 = union(检索结果₁, 检索结果₂, ..., 检索结果₅)
重排分数 = cross_encoder(节点描述 + 候选句子)
最终证据 = top-k by 重排分数（去重后）
```

#### 和你们项目的结合

Step4 目前的候选节点召回，可以用这个方法替代单一的 description 相似度匹配：

```python
def multi_aspect_recall(node, all_nodes, terminology_yaml):
    """多角度召回候选节点"""
    queries = []

    # 角度1：节点描述本身
    queries.append(node.description)

    # 角度2：术语归一后的标准主题词
    normalized_subject = terminology_yaml.normalize(node.description)
    queries.append(normalized_subject)

    # 角度3：节点类型 + 关键属性
    queries.append(f"{node.type} {node.key_attributes}")

    # 角度4：法规框架角度（根据节点类型映射）
    regulatory_terms = REGULATORY_MAPPING[node.type]  # 如 Risk → ISO 14971
    queries.append(regulatory_terms)

    # 角度5：数值指标（如果有）
    if node.value:
        queries.append(f"{node.subject} {node.value} {node.unit}")

    # 分别检索，取并集
    candidates = set()
    for q in queries:
        results = vector_search(q, all_nodes, top_k=10)
        candidates.update(results)

    # 用 cross-encoder 重排
    scored = [(c, cross_encoder_score(node, c)) for c in candidates]
    return sorted(scored, key=lambda x: -x[1])[:20]  # 返回top-20候选
```

这个改动可以直接解决你们 6.3 节提到的"功能→测试 151% 误报"问题的另一面：不只是要减少误报，也要提高召回，让真正相关的节点对不被遗漏。

---

## C. GraphRAG 系列

### C1. Microsoft GraphRAG
**From Local to Global: A Graph RAG Approach to Query-Focused Summarization**
Edge et al., Microsoft Research, 2024 | [GitHub](https://github.com/microsoft/graphrag)

#### 解决的问题

传统 RAG 是"检索文本块 + 生成"，对于"跨多个文档的全局性问题"效果很差，因为：

1. 向量检索只找到局部相关的段落，看不到全局结构
2. 文档之间的关联关系被忽略了
3. 无法回答"这批文档里，关于X主题的整体情况是什么"这类问题

对你们来说，对应的场景是：审查人员问"这批 DHF 文档里，哪些风险控制措施没有对应的测试验证"——这需要跨越整个文档集合的全局视图，不是检索几个段落能回答的。

#### 核心技术

**三阶段流程**：

```
阶段1：实体和关系抽取
  用 LLM 对每个文档块抽取实体和关系
  → 得到大量 (实体A, 关系, 实体B) 三元组

阶段2：社区检测（Community Detection）
  用 Leiden 算法对实体图做聚类
  → 得到层级化的社区结构：
    社区L0（最细）：功能相近的几个实体
    社区L1（中等）：一个技术模块的所有相关实体
    社区L2（最粗）：整个风险管控体系的所有实体

阶段3：社区摘要生成
  对每个社区，让 LLM 生成该社区的主题摘要
  → 社区摘要是"跨文档全局视图"的基础单元

查询时：
  全局查询 → 检索相关社区摘要 → 聚合生成回答
  局部查询 → 直接检索具体实体和关系
```

**Leiden 算法**：一种图社区发现算法，比 Louvain 算法更能保证社区的内部连通性，适合有噪音的知识图谱。

#### 和你们项目的结合

你们的 Neo4j 图建好之后，Leiden 社区检测可以自动发现"哪些节点在语义上属于同一个审查单元"：

```
预期的社区结构（基于你们的图）：

社区A（测量精度审查单元）：
  Requirement("精度±0.2℃") + DesignInput("精度需求") +
  Risk("传感器偏移") + RiskControl("校准") + Test("T-12")

社区B（软件设计审查单元）：
  SoftwareItem("测温算法") + SoftwareConfigItem("v2.3") +
  Test("软件测试S-07") + Regulation("IEC 62304")

社区C（结构设计审查单元）：
  Component("外壳") + DesignInput("防护等级IP22") +
  Test("IP测试") + TestReport("TR-2026-03")
```

每个社区就是一个独立的一致性审查单元，审查报告可以按社区组织，而不是按文件对。

**实际接入**：Neo4j 有 Graph Data Science 库，直接支持 Leiden 算法：

```cypher
// 在 Neo4j 中运行 Leiden 社区检测
CALL gds.leiden.write('myGraph', {
  writeProperty: 'communityId',
  relationshipWeightProperty: 'confidence'
})
```

---

### C2. LightRAG
**LightRAG: Simple and Fast Retrieval-Augmented Generation**
Guo et al., 2024 | [GitHub](https://github.com/HKUDS/LightRAG)

#### 解决的问题

GraphRAG 虽然强大，但成本很高：
- 每个文档块都要调用 LLM 抽取实体关系，成本是传统 RAG 的数倍
- 社区检测和摘要生成需要大量计算
- 更新图时需要重新运行整个流程

对 254 份文件这个规模，完整 GraphRAG 的代价是合理的；但如果文件数量到达几千份，或者文件经常更新，就需要更轻量的方案。

#### 核心技术

**双层检索策略（Dual-level Retrieval）**：

```
低层（Low-level）检索：
  目标：找具体实体和它们的直接关系
  方法：用查询 embedding 直接匹配图里的节点和边
  适合：精确查找（"找 Risk-01 的所有控制措施"）

高层（High-level）检索：
  目标：找语义相关的主题描述
  方法：对每个实体生成简短描述，用 embedding 做语义匹配
  适合：模糊查找（"找和'传感器精度'相关的所有内容"）

查询时两层同时检索，结果合并后送给 LLM 生成回答。
```

**与 GraphRAG 的对比**：

```
                  GraphRAG          LightRAG
社区检测           需要              不需要
图构建成本         高               中等
查询延迟           高（需聚合摘要）  低
更新成本           高（重建图）      低（增量更新）
全局查询能力       强               中等
适合场景           大规模静态语料    中小规模/动态更新
```

#### 和你们项目的结合

你们目前用 Neo4j 存储图，可以在图上直接实现 LightRAG 的双层检索：

```
低层检索（精确）：
  Neo4j Cypher 查询 → 找特定节点类型和关系
  例："找所有没有 VERIFIED_BY 边的 RiskControl 节点"
  → 直接用于一致性规则检查

高层检索（语义）：
  对所有节点的 description 做向量索引（用 Neo4j Vector Index）
  例："找和'测量精度要求'语义相近的所有节点"
  → 用于跨文件关系的候选节点召回
```

Neo4j 5.x 原生支持向量索引，不需要引入额外向量数据库：

```cypher
// 创建节点描述的向量索引
CREATE VECTOR INDEX nodeDescriptionIndex
FOR (n:Claim) ON (n.embedding)
OPTIONS {indexConfig: {`vector.dimensions`: 768, `vector.similarity_function`: 'cosine'}}

// 语义检索
CALL db.index.vector.queryNodes('nodeDescriptionIndex', 10, $queryEmbedding)
YIELD node, score
RETURN node.description, score
```

---

## 总结：按阶段的行动建议

### 现在可以立刻做的

**改造 Step2 的 prompt（参考 ATLOP + DREEAM）**：
- 给 Claude 附上节点对在文档中的共现上下文
- 要求 Claude 输出 evidence_spans 字段

**改造 Step4 的 prompt（参考 KXDocRE）**：
- 在判断跨文件关系时，加入对应的 ISO 法规条款作为知识引导

### P1 阶段改造

**文本路径构建（参考 CodRED）**：
- 在 merge_results.py 里加入桥接实体查找逻辑
- 给 Step4 的每个节点对构建文本路径作为上下文

**层级树分类（参考 HCRE）**：
- 把 edges.yaml 里的关系类型整理成 4 层树结构
- Step4 改为多轮调用（粗分类 → 细分类 → 验证）

### P2 阶段改造

**多角度召回（参考 MAQD）**：
- 实现 multi_aspect_recall 函数
- 用 sentence-transformers + Neo4j Vector Index 替代当前的相似度计算

**Neo4j 双层检索（参考 LightRAG）**：
- 为所有节点建向量索引
- 实现精确 Cypher 查询 + 语义向量检索的混合检索

### 图建好之后（P3 阶段）

**Leiden 社区检测（参考 GraphRAG）**：
- 在 Neo4j GDS 里运行 Leiden 算法
- 按社区组织审查报告，替代按文件对的组织方式

---

## 参考文献

| 论文 | 链接 |
|------|------|
| DocRED (Yao et al., ACL 2019) | https://aclanthology.org/P19-1074/ |
| ATLOP (Zhou et al., AAAI 2021) | https://arxiv.org/abs/2010.11304 |
| CodRED (Yao et al., EMNLP 2021) | https://aclanthology.org/2021.emnlp-main.366/ |
| DREEAM (Ma et al., EACL 2023) | https://arxiv.org/abs/2302.08675 |
| AutoRE (Xue et al., ACL 2024) | https://arxiv.org/abs/2403.14888 |
| KXDocRE (Jain et al., 2024) | https://arxiv.org/abs/2405.13546 |
| GraphRAG (Edge et al., 2024) | https://arxiv.org/abs/2404.16130 |
| HCRE (Ma et al., 2025) | https://arxiv.org/abs/2604.07937 |
| MAQD (2025) | https://link.springer.com/article/10.1007/s10844-025-00952-6 |
| LightRAG (Guo et al., 2024) | https://github.com/HKUDS/LightRAG |

---

*本文档针对 PT9L 红外体温计 DHF/DMR 文档一致性审查系统整理，2026-06-12*




新增技术：
Graph-RAG 用于需求追溯和合规检查
远程监督闭环大规模无标注训练数据生成用 ISO 法规作为知识库，DHF 文档作为语料，自动生成领域训练数据
Think-on-Graph（ToG）——图上主动发现路径
KG Embedding + 链接预测