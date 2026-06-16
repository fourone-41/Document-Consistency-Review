# 全局 Schema（文档一致性审查系统）

> 版本：v0.2 ｜ 日期：2026-06-10 ｜ 项目：PT9L 红外体温计 DHF/DMR
> 配套技术路线见根目录 `1schema技术文档.md`。
>
> **v0.2 变更**：基于对全部 470 份文件分层抽样(42 份)的「无约束抽取」(见 `_convert/gap_report.md`)，
> 补全了 9 个高频但 v0.1 缺失的节点、3 个枚举、`Claim.tolerance` 字段、单位换算规则，
> 并新增 `profiles.yaml`(14 类文档的抽取视图)，使 schema 从「3 份验证的主干」升级为「覆盖全部 14 类文档」。

## 这个文件夹是什么

整个系统"认卡片"的**唯一标准**。所有文件抽取、建图、检查都以这里为准。

| 文件 | 是什么 | 谁来改 |
|---|---|---|
| `schema.yaml` | **唯一可信源**：所有节点类型（卡片）+ 字段 + 枚举（LinkML 格式） | 人工维护，改这里 |
| `edges.yaml` | 边（关系）目录：谁连谁、边上带什么属性 | 人工维护 |
| `terminology.yaml` | 术语归一表：把"精度/accuracy/误差"归到同一个标准词 + 好坏方向 + 单位换算 | 人工维护 |
| `profiles.yaml` | 🆕 14 类文档的抽取 profile：每类该激活哪些节点/边 + 抽取重点 + 易错点 | 人工维护 |
| `models.py` | 可直接用的 Pydantic 模型（与 schema.yaml 等价，给抽取代码 import） | **自动生成，别手改** |

## 节点分 4 层

- **层1 结构层**（定位溯源）：`Document` `Section`
- **层2 锚点层**（确定性身份，可合并去重）：`Product` `Identifier` `Person`
- **层3 领域层**（业务实体）：`Requirement` `DesignInput` `Risk` `RiskControl` `Test` `TestReport` `Regulation` `Function` `Component` `ReviewRecord` `IntendedUseItem`🆕 `Market`🆕
- **层3 补充**（v0.2 数据驱动新增）：`RevisionRecord` `ReviewItem` `DocIndexEntry` `TestMeasurement` `SoftwareItem` `SoftwareConfigItem` `IssueItem` `PlanTask` `Resource`
- **层4 裁决层**（对齐主干，不合并）：`Claim` `Statement` `SemanticFragment`

🆕 = 由真实文件采样逼出、`技术文档(3)` 原本没有的卡型。

## 一条铁律：什么合并成一个节点、什么不合并

- **锚点类**（Identifier/Product/Person/有唯一编号的 Requirement…）：同一个东西在多份文件出现 → **合并成 1 个节点**，各文件连边过来。建图用 `MERGE`。
- **断言类**（Claim/SemanticFragment）：哪怕说的是同一件事，也 **各自独立成节点**，用 `CORRESPONDS_TO` 边连起来，**绝不合并**（否则 ±0.2 vs ±0.3 的冲突会消失）。建图用 `CREATE`。

## 这套 schema 是怎么长出来的（分类 + 抽样方法论）

> 写给后来人：为什么不是"读完 470 份再设计"，而是"分类→抽样→无约束抽取→回填"。
> 全部脚本与中间产物在根目录 `_convert/`。

### 为什么先分类、再抽样，而不是逐份读

- 470 份逐份设计 schema 既不现实也重复——**同类文档结构高度相似**（同一套 Word/Excel 模板批量产生）。
- 正确的工程结构是 **1 套全局 schema + 每类一份抽取 profile**，而不是 470 套。
- 所以只要把文件聚成**有限的类**，每类挑几份代表，就能暴露该类需要的字段。

### 怎么分类的（13 类 + 兜底"其它"）

- **依据**：文件名关键词。清洗后的文件名保留了强信号（`评审检查表 / 设计输入 / FMEA / BOM / 软件 / 说明书…`）。
- **规则**：按优先级**从具体到通用**匹配，命中即定类，一个文件只归一个主类（见 `_convert/classify_sample.py` 的 `RULES`）。
  优先级用来解决多关键词冲突——例如"结构图样评审检查表"同时含"图样"和"评审"，因"评审检查表"优先级更高 → 归评审检查表（它本质是检查表）。
- **兜底**：都没命中 → `其它`。
- **归一主类后的分布**（470 份）：评审检查表 ~85、测试/记录 ~32、软件 ~31、说明书/包装 ~20、设计验证 ~20、开发计划 ~14、设计确认 ~13、立项需求/设计输入/BOM/FMEA 各 ~8、图样方案 ~6、**其它 ~209**。
- 来源格式：`lo_html` 220、`xlsx` 101、其它 149。

### 为什么每类只抽 2–3 份

- 目标是**发现"该类需要哪些字段"**，不是做统计 → 每类少量代表就够。
- **去重**：同名文件（同一份散在多个目录）只取一份，省 token。
- **避超大**：>60KB 的（如 23 万字的开发计划表）先跳过，避免爆上下文；发现字段看文档头部即可。
- **覆盖格式**：尽量同时取 `lo_html` 和 `xlsx` 两种来源（两种转换的噪声不同）。
- **取中位体积**：同格式里挑中位大小的文件——太小多是封面没内容，太大超长。
- 最终：14 类共抽 **42 份**（`_convert/sample.json`）。

### 关键一步：无约束抽取（自底向上找盲点）

- 给 LLM 文档但**故意不给 schema**，让它自己提出"看到哪些记录类型、各有哪些字段"。
- 这能暴露**自上而下设计的盲点**——人工预设的 schema 容易漏掉真实业务字段。
- 42 份的结果汇总成 `_convert/gap_report.md`，据此补全本目录的 schema（v0.1 → v0.2 共加了 9 个节点）。

### 局限与后续

- 关键词分类有 **~209 份的"其它"长尾**，上线前需回看并把高频新类型升成正式 profile。
- 发现阶段用单模型（qwen-max）单样本，**召回率还需用人工 gold set 验证**（每类挑 1 份标注，测精确率/召回率后迭代）。

## 用法

```bash
# 安装（任选）
pip install linkml

# 校验 schema 是否合法
linkml-validate --schema schema.yaml <数据文件>

# 从 schema.yaml 重新生成 Pydantic（覆盖 models.py）
gen-pydantic schema.yaml > models.py
```

原型阶段也可以先不装 LinkML，直接 `from schema.models import Claim, Risk, ...` 使用。
