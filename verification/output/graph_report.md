# POC 详细报告（含原文对照与知识图谱）

---

## 一、原文与抽取结果对照

以下展示原始文档片段与 LLM 结构化抽取结果的逐项对照，
验证抽取准确性。

### 1.1 客户需求书 — 性能规格部分

**原文内容：**

```markdown
## Sheet: 性能规格部分
| 序号 | 条目 | 要求 | 备注 |
|------|------|------|------|
| 1 | 温度显示范围 | 32.0℃～42.9℃ |  |
| 2 | 显示分辨率 | 0.1℃ |  |
| 3 | 测量误差 | ≥35℃且≤42℃：±0.2℃，其它：±0.3℃ |  |
| 4 | 工作环境 | 温度：10℃～40℃ 相对湿度：不窄于15-95%RH，不结露 大气压力：70kPa～106kPa |  |
| 5 | 存储环境 | 温度：-20.0℃―55.0℃ 相对湿度：不窄于15-95%RH，不结露 大气压力：70kPa～106kPa |  |
| 6 | 产品寿命 | 五年或10000次 |  |
| 7 | 电池寿命 | 测量使用次数不低于1000次 |  |
```

**抽取结果（Claims）：**

| # | subject | value | unit | condition | raw_text |
|---|---------|-------|------|-----------|----------|
| 1 | 温度显示范围 | 32.0-42.9 | ℃ | - | 32.0℃～42.9℃ |
| 2 | 显示分辨率 | 0.1 | ℃ | - | 0.1℃ |
| 3 | 测量误差 | ±0.2 | ℃ | ≥35℃且≤42℃ | ≥35℃且≤42℃：±0.2℃ |
| 4 | 测量误差 | ±0.3 | ℃ | 其它（<35℃或>42℃） | 其它：±0.3℃ |
| 5 | 工作温度 | 10-40 | ℃ | - | 温度：10℃～40℃ |
| 6 | 工作湿度 | 15-95 | %RH | 不结露 | 相对湿度：不窄于15-95%RH，不结露 |
| 7 | 工作大气压力 | 70-106 | kPa | - | 大气压力：70kPa～106kPa |
| 8 | 存储温度 | -20.0-55.0 | ℃ | - | 温度：-20.0℃―55.0℃ |
| 9 | 存储湿度 | 15-95 | %RH | 不结露 | 相对湿度：不窄于15-95%RH，不结露 |
| 10 | 存储大气压力 | 70-106 | kPa | - | 大气压力：70kPa～106kPa |

**对照分析：** 原文7行表格 → 成功抽取为17条结构化Claim，
其中"工作环境"一行被正确拆分为温度、湿度、气压3条独立Claim。

### 1.2 检测报告 — 测试项目

**原文内容（节选）：**

```markdown
| 5 | 自动关机 | 测温后无操作 15±1S 自动转入待机模式。 |
| 6 | 温度显示范围及超温提示功能 | 要求：32℃~42.9℃ |
| 7 | 显示分辨率 | 要求：0.1℃ |
| 8 | 常温精度测试 | 精度要求：≥35℃且≤42℃：±0.2℃，其它：±0.3℃ |

测试环境：23℃，湿度55%，正常大气压；
测试样机数量：2台（编号为1号和2号）
```

**抽取结果（Claims 节选）：**

| # | subject | value | unit | condition | raw_text |
|---|---------|-------|------|-----------|----------|
| 1 | 自动关机时间 | 15±1 | S | 测温后无操作 | 测温后无操作 15±1S 自动转入待机模式。 |
| 2 | 温度显示范围 | 32-42.9 | ℃ | - | 要求：32℃~42.9℃ |
| 3 | 显示分辨率 | 0.1 | ℃ | - | 要求：0.1℃ |
| 4 | 常温精度 | ±0.2 | ℃ | ≥35℃且≤42℃ | 精度要求：≥35℃且≤42℃：±0.2℃ |
| 5 | 常温精度 | ±0.3 | ℃ | 其它（<35℃或>42℃） | 其它：±0.3℃ |
| 6 | 测试环境温度 | 23 | ℃ | - | 测试环境：23℃ |
| 7 | 测试环境湿度 | 55 | %RH | - | 湿度55% |
| 8 | 测试样机数量 | 2 | 台 | - | 测试样机数量：2台（编号为1号和2号） |

**抽取的 SemanticFragments（节选）：**

| # | type | content | related_subjects |
|---|------|---------|-----------------|
| 1 | scope_limitation | PT9L进行到T1阶段，此次测试对PT9L的性能进行测试，测试依据为"PT9L红外体温计产品检验标准"。 |  |
| 2 | scope_limitation | 恒温水槽、黑体辐射源。其中恒温水槽、黑体辐射源都需要符合"PT9L红外体温计产品检验标准"内的要求。 |  |
| 3 | scope_limitation | 测试方法：见《PT9L红外体温计产品检验标准》 |  |
| 4 | behavioral_spec | 产品上电后会进入上电自检：白色背光灯点亮，LCD显示屏全显，此时检查显示内容是否正确，是否有乱显，多显，少显现象，同时蜂 | 上电自检功能 |
| 5 | behavioral_spec | 通过机器侧面静音键控制提示音，当静音键置于关时，屏幕出现静音符号，此时提示音关；当静音键置于开时，屏幕上静音符号消失，此 | 提示音开关 |

**对照分析：** 检测报告中的表格行被精确拆解——
数值性内容→Claim（如15±1S），描述性内容→SemanticFragment（如上电自检行为描述）。

---

## 二、知识图谱（实体与关系）

### 2.1 图谱节点统计

| 节点类型 | 数量 | 说明 |
|----------|------|------|
| Document | 3 | 源文件 |
| Claim | 121 | 结构化参数声明 |
| SemanticFragment | 71 | 描述性语义片段 |
| Identifier | 21 | 文件/产品编号 |
| Person | 14 | 人员 |
| StandardSubject | 10 | 归一化标准词 |
| **总计** | **240** | |

### 2.2 图谱关系统计

| 关系类型 | 数量 | 说明 |
|----------|------|------|
| CONTAINS_CLAIM (Document→Claim) | 121 | 文件包含声明 |
| CONTAINS_FRAGMENT (Document→Fragment) | 71 | 文件包含片段 |
| HAS_IDENTIFIER (Document→Identifier) | 21 | 文件拥有标识 |
| HAS_PERSON (Document→Person) | 14 | 文件关联人员 |
| MAPS_TO (Claim→StandardSubject) | 68 | 归一化映射 |
| RELATES_TO (Fragment→Claim.subject) | 20 | 语义关联 |
| SAME_SUBJECT (Claim↔Claim) | 跨文件 | 同参数跨文件 |
| **总计** | **315+** | |

### 2.3 知识图谱结构图（Mermaid）

> **图例说明：**
> - 🟢 绿色 = **Document**（源文件）
> - 🔵 蓝色 = **Claim**（结构化参数声明，含 subject/value/unit）
> - 🟣 紫色 = **SemanticFragment**（描述性语义片段）
> - 🟠 橙色圆形 = **StandardSubject**（归一化标准词，跨文件对齐桥梁）
> - ⬜ 灰色 = **Person**（人员）
> - 🔷 青色 = **Identifier**（文件/产品编号）

#### 图 A：一份文件的完整实体展示（所有节点类型）

```mermaid
graph TD
    DOC["🟢 Document<br/>─────────────<br/>filename: 客户需求书E0<br/>doc_type: customer_requirement<br/>phase: 01 立项批准书"]

    C1["🔵 Claim #1<br/>─────────────<br/>subject: 测量误差<br/>attribute: tolerance<br/>value: ±0.2<br/>unit: ℃<br/>condition: ≥35℃且≤42℃"]
    C2["🔵 Claim #2<br/>─────────────<br/>subject: 工作温度<br/>attribute: range<br/>value: 10-40<br/>unit: ℃"]
    C3["🔵 Claim #3<br/>─────────────<br/>subject: 自动关机时间<br/>attribute: value<br/>value: 15<br/>unit: 秒"]

    F1["🟣 SemanticFragment<br/>─────────────<br/>type: scope_limitation<br/>content: 本品主要采用红外<br/>测温方式测量人体额头温度<br/>topic_tags: 预期用途,测量原理<br/>related_subjects: 测量原理"]
    F2["🟣 SemanticFragment<br/>─────────────<br/>type: constraint_statement<br/>content: 应符合IEC60529<br/>的IP22类测试<br/>topic_tags: 防尘防水,IP等级"]

    P1["⬜ Person<br/>─────────────<br/>name: 赵一平<br/>role: 编制"]
    P2["⬜ Person<br/>─────────────<br/>name: 丛明<br/>role: 批准"]

    ID1["🔷 Identifier<br/>─────────────<br/>id_type: 版本号<br/>value: V1.0"]

    DOC -->|"CONTAINS_CLAIM"| C1
    DOC -->|"CONTAINS_CLAIM"| C2
    DOC -->|"CONTAINS_CLAIM"| C3
    DOC -->|"CONTAINS_FRAGMENT"| F1
    DOC -->|"CONTAINS_FRAGMENT"| F2
    DOC -->|"HAS_PERSON"| P1
    DOC -->|"HAS_PERSON"| P2
    DOC -->|"HAS_IDENTIFIER"| ID1

    classDef doc fill:#4CAF50,color:white,stroke:#333
    classDef claim fill:#2196F3,color:white,stroke:#333
    classDef frag fill:#9C27B0,color:white,stroke:#333
    classDef person fill:#607D8B,color:white,stroke:#333
    classDef ident fill:#00BCD4,color:white,stroke:#333
    class DOC doc
    class C1,C2,C3 claim
    class F1,F2 frag
    class P1,P2 person
    class ID1 ident
```

#### 图 B：跨文件归一化对齐（核心机制）

```mermaid
graph LR
    DOC1["🟢 Document<br/>客户需求书"]
    DOC2["🟢 Document<br/>设计输入汇总表"]
    DOC3["🟢 Document<br/>检测报告"]

    C1_1["🔵 Claim<br/>subject: 测量误差<br/>value: ±0.2℃<br/>来源: 客户需求书"]
    C2_1["🔵 Claim<br/>subject: 测量误差<br/>value: ±0.2℃<br/>来源: 设计输入"]
    C3_1["🔵 Claim<br/>subject: 常温精度<br/>value: ±0.2℃<br/>来源: 检测报告"]

    C1_2["🔵 Claim<br/>subject: 工作温度<br/>value: 10-40℃<br/>来源: 客户需求书"]
    C2_2["🔵 Claim<br/>subject: 工作温度<br/>value: 10-40℃<br/>来源: 设计输入"]
    C3_2["🔵 Claim<br/>subject: 背光灯测试-环境温度<br/>value: 24-26℃ ⚠️<br/>来源: 检测报告"]

    S1(("🟠 StandardSubject<br/>measurement_accuracy<br/>direction: smaller_is_better"))
    S2(("🟠 StandardSubject<br/>operating_temperature<br/>direction: wider_is_better"))

    DOC1 -->|CONTAINS_CLAIM| C1_1
    DOC2 -->|CONTAINS_CLAIM| C2_1
    DOC3 -->|CONTAINS_CLAIM| C3_1
    DOC1 -->|CONTAINS_CLAIM| C1_2
    DOC2 -->|CONTAINS_CLAIM| C2_2
    DOC3 -->|CONTAINS_CLAIM| C3_2

    C1_1 -->|"MAPS_TO<br/>(测量误差→)"| S1
    C2_1 -->|"MAPS_TO<br/>(测量误差→)"| S1
    C3_1 -->|"MAPS_TO<br/>(常温精度→)"| S1
    C1_2 -->|"MAPS_TO<br/>(工作温度→)"| S2
    C2_2 -->|"MAPS_TO<br/>(工作温度→)"| S2
    C3_2 -->|"MAPS_TO<br/>(背光灯测试-环境温度→)"| S2

    classDef doc fill:#4CAF50,color:white,stroke:#333
    classDef claim fill:#2196F3,color:white,stroke:#333
    classDef std fill:#FF9800,color:white,stroke:#333
    classDef warn fill:#F44336,color:white,stroke:#333
    class DOC1,DOC2,DOC3 doc
    class C1_1,C2_1,C3_1,C1_2,C2_2 claim
    class C3_2 warn
    class S1,S2 std
```

#### 图解总结

```
Document ──CONTAINS_CLAIM──→ Claim ──MAPS_TO──→ StandardSubject ←──MAPS_TO── Claim ←──CONTAINS_CLAIM── Document
    │                                                                                                        │
    │──CONTAINS_FRAGMENT──→ SemanticFragment ──RELATES_TO──→ Claim                                           │
    │──HAS_PERSON──→ Person                                                                                  │
    │──HAS_IDENTIFIER──→ Identifier                                                                          │
    └─────────────── 通过 StandardSubject 实现跨文件对齐，发现数值冲突 ──────────────────────────────────────────┘
```

### 2.4 跨文件冲突检测图

```mermaid
graph LR
    subgraph "operating_temperature 工作温度"
        A1["客户需求书: 10-40℃"] -->|一致| A2["设计输入: 10-40℃"]
        A3["检测报告: 24-26℃"] -->|⚠️ 范围窄| A1
    end
    subgraph "auto_shutdown_time 自动关机"
        B1["客户需求书: 15秒"] -->|一致| B2["设计输入: 15秒"]
        B3["检测报告: 15±1S"] -->|含容差| B1
    end
    subgraph "measurement_accuracy 精度"
        C1["客户需求书: ±0.2℃"] -->|一致| C2["设计输入: ±0.2℃"]
        C2 -->|一致| C3["检测报告: ±0.2℃"]
    end
    subgraph "humidity_range 湿度"
        D1["客户需求书: 15-95%RH"] -->|一致| D2["设计输入: 15-95%RH"]
        D3["检测报告: 30-70%RH"] -->|⚠️ 范围窄| D1
    end

    style A3 fill:#F44336,color:white
    style B3 fill:#FF9800,color:white
    style D3 fill:#F44336,color:white
```

### 2.5 图谱节点详细示例

以下展示图谱中实际存储的节点属性格式（Neo4j 导入用）：

**Claim 节点示例：**
```json
{
  "node_type": "Claim",
  "subject": "测量误差",
  "normalized_subject": "measurement_accuracy",
  "attribute": "tolerance",
  "value": "±0.2",
  "unit": "℃",
  "condition": "≥35℃且≤42℃",
  "raw_text": "≥35℃且≤42℃：±0.2℃",
  "source_doc": "客户需求书E0-血压计 23.6.via_xlsx.clean.md",
  "source_section": "Sheet: 性能规格部分 > Row3"
}
```

**SemanticFragment 节点示例：**
```json
{
  "node_type": "SemanticFragment",
  "fragment_type": "behavioral_spec",
  "content": "产品上电后会进入上电自检：白色背光灯点亮，LCD显示屏全显...",
  "topic_tags": [
    "上电自检",
    "开机行为",
    "LCD显示"
  ],
  "related_subjects": [
    "上电自检功能"
  ],
  "source_doc": "PT9L红外体温计检测报告 V1.0.via_lo_html.clean.md",
  "source_section": "文件开头 > 四、测试项目及结果 > 常温检验"
}
```

**Document 节点示例：**
```json
{
  "node_type": "Document",
  "filename": "客户需求书E0-血压计 23.6.via_xlsx.clean.md",
  "doc_type": "customer_requirement",
  "phase": "01 立项批准书E0 23.11",
  "claims_count": 17,
  "fragments_count": 33
}
```

**关系示例（Cypher 语句）：**
```cypher
// Document CONTAINS Claim
(doc:Document {filename:"客户需求书E0"})-[:CONTAINS_CLAIM]->(c:Claim {subject:"测量误差"})

// Claim MAPS_TO StandardSubject
(c:Claim {subject:"测量误差"})-[:MAPS_TO]->(s:StandardSubject {name:"measurement_accuracy"})
(c:Claim {subject:"常温精度"})-[:MAPS_TO]->(s:StandardSubject {name:"measurement_accuracy"})

// Cross-file alignment query
MATCH (d1:Document)-[:CONTAINS_CLAIM]->(c1:Claim)-[:MAPS_TO]->(s:StandardSubject)
MATCH (d2:Document)-[:CONTAINS_CLAIM]->(c2:Claim)-[:MAPS_TO]->(s)
WHERE d1 <> d2 AND c1.value <> c2.value
RETURN s.name, d1.filename, c1.value, d2.filename, c2.value
```

---

## 三、总结

本次 POC 构建的知识图谱包含：
- **240** 个节点
- **315+** 条关系
- **10** 个跨文件对齐的标准参数
- **4** 组检出的潜在冲突/差异

图谱结构验证了从非结构化文档到结构化知识表示的完整链路可行性。