"""
全局 Schema 的 Pydantic 实现（与 schema.yaml 等价）。

⚠️ 此文件应由 `gen-pydantic schema.yaml > models.py` 自动生成。
   原型阶段先手写一份等价模型，便于抽取代码立即 import 使用。
   一旦安装 LinkML，请改用自动生成以保持单一可信源。

节点分 4 层：
  层1 结构层：Document, Section
  层2 锚点层：Product, Identifier, Person          （同一身份合并为 1 个节点，MERGE）
  层3 领域层：Requirement, DesignInput, Risk, RiskControl, Test, TestReport,
              Regulation, Function, Component, ReviewRecord, IntendedUseItem, Market
  层3补充 (v0.2)：RevisionRecord, ReviewItem, DocIndexEntry, TestMeasurement,
              SoftwareItem, SoftwareConfigItem, IssueItem, PlanTask, Resource
  层4 裁决层：Claim, Statement, SemanticFragment    （各自独立成节点，CREATE，绝不合并）
"""
from __future__ import annotations

from typing import Literal, Optional

from pydantic import BaseModel, Field

# ---------------------------------------------------------------------
# 受控词表
# ---------------------------------------------------------------------
Category = Literal["通用", "功能", "性能", "组件", "法规"]

IdType = Literal[
    "产品编号", "项目号", "版本号", "文件编号",
    "需求编号", "设计输入编号", "风险编号", "测试编号", "物料编码",
    "表单号", "图纸号", "WBS号",  # 🆕 v0.2
]

Direction = Literal["smaller_is_better", "larger_is_better", "wider_is_better", "exact_match"]

Subject = Literal[
    "measurement_accuracy", "display_range", "operating_temperature", "storage_temperature",
    "display_resolution", "service_life", "battery_life", "product_dimensions",
    "product_weight", "package_dimensions", "package_weight", "ip_rating",
    "response_time", "fever_alarm_threshold", "humidity_range", "pressure_range",
    "auto_off_time",
    "measuring_distance", "clinical_repeatability",  # 🆕 v0.2
]

RiskLevel = Literal["Acceptable", "ALARP", "Unacceptable"]
Conclusion = Literal["PASS", "FAIL", "CONDITIONAL"]
AnswerType = Literal["yes", "no", "descriptive", "quantitative", "n_a"]
Criticality = Literal["A", "B", "C"]
FragmentType = Literal[
    "design_rationale", "working_principle", "constraint_statement",
    "behavioral_spec", "open_issue", "scope_limitation", "assumption",
]
ReviewConclusion = Literal["通过", "不通过", "待整改", "不适用"]  # 🆕 v0.2
IssueStatus = Literal["open", "in_progress", "closed"]  # 🆕 v0.2
SoftwareItemType = Literal[
    "功能模块", "设计规格", "通信命令", "软硬件接口", "运行环境", "其它",
]  # 🆕 v0.2


# ---------------------------------------------------------------------
# 层1：结构层
# ---------------------------------------------------------------------
class Document(BaseModel):
    doc_id: str
    title: str
    doc_type: str
    dhf_stage: Optional[str] = None
    version: Optional[str] = None
    filename: Optional[str] = None
    format: Optional[str] = None
    path: Optional[str] = None
    date: Optional[str] = None
    lang: Optional[str] = None
    confidence: Optional[str] = None


class Section(BaseModel):
    section_id: str
    doc_id: str
    heading_path: Optional[str] = None
    page: Optional[int] = None
    order: Optional[int] = None


# ---------------------------------------------------------------------
# 层2：锚点层（合并去重）
# ---------------------------------------------------------------------
class Product(BaseModel):
    product_id: str
    model: Optional[str] = None
    name: str
    region: Optional[str] = None


class Identifier(BaseModel):
    id_type: IdType
    value: str


class Person(BaseModel):
    name: str
    dept: Optional[str] = None
    title: Optional[str] = None
    signed: Optional[bool] = None  # 🆕


# ---------------------------------------------------------------------
# 层3：领域层
# ---------------------------------------------------------------------
class Requirement(BaseModel):
    req_id: str
    category: Optional[Category] = None
    description: str
    value: Optional[str] = None
    unit: Optional[str] = None
    tolerance: Optional[str] = None  # 🆕
    condition: Optional[str] = None
    verification_method: Optional[str] = None


class DesignInput(BaseModel):
    di_id: str
    category: Optional[Category] = None
    description: str
    value: Optional[str] = None
    unit: Optional[str] = None
    tolerance: Optional[str] = None  # 🆕
    condition: Optional[str] = None
    source_req_id: Optional[str] = None


class Risk(BaseModel):
    risk_id: str
    hazard: str
    hazardous_situation: Optional[str] = None
    harm: Optional[str] = None
    severity: Optional[int] = None
    probability: Optional[str] = None
    risk_level: Optional[RiskLevel] = None
    phase: Optional[str] = None


class RiskControl(BaseModel):
    control_id: str
    measure: str
    type: Optional[str] = None
    evidence_type: Optional[str] = None


class Test(BaseModel):
    test_id: str
    item: str
    condition: Optional[str] = None
    expected_value: Optional[str] = None
    actual_result: Optional[str] = None
    pass_criteria: Optional[str] = None
    instrument: Optional[str] = None    # 🆕 v0.2
    environment: Optional[str] = None   # 🆕 v0.2


class TestReport(BaseModel):
    report_id: str
    conclusion: Optional[Conclusion] = None
    evidence_level: Optional[str] = None


class Regulation(BaseModel):
    reg_id: str
    std_id: str
    version: Optional[str] = None
    clause: Optional[str] = None
    region: Optional[str] = None          # 🆕
    applicable: Optional[bool] = None     # 🆕
    equivalent_std: Optional[str] = None  # 🆕
    requirement_value: Optional[str] = None
    requirement_text: Optional[str] = None


class Function(BaseModel):
    name: str
    description: Optional[str] = None
    value: Optional[str] = None
    exists: bool = True


class Component(BaseModel):
    name: str
    part_no: Optional[str] = None
    spec: Optional[str] = None
    model: Optional[str] = None
    ref_des: Optional[str] = None             # 🆕
    qty: Optional[str] = None
    criticality: Optional[Criticality] = None  # 🆕
    rohs: Optional[bool] = None
    board: Optional[str] = None


class ReviewRecord(BaseModel):
    review_id: str
    stage: Optional[str] = None
    date: Optional[str] = None
    conclusion: Optional[str] = None


class IntendedUseItem(BaseModel):  # 🆕
    item_id: str
    seq: Optional[int] = None
    content: str


class Market(BaseModel):  # 🆕
    market_id: str
    region: Optional[str] = None
    certification: Optional[str] = None
    selected: Optional[bool] = None
    registrant: Optional[str] = None
    registration_path: Optional[str] = None


# ---------------------------------------------------------------------
# 层4：裁决层（独立成节点，绝不合并）
# ---------------------------------------------------------------------
class Claim(BaseModel):
    claim_id: str
    subject: Subject
    attribute: str
    value: Optional[str] = None
    unit: Optional[str] = None
    tolerance: Optional[str] = None  # 🆕 v0.2 公差与 condition 分开
    condition: Optional[str] = None
    raw_text: str
    source_doc: str
    source_section: str


class Statement(BaseModel):
    statement_id: str
    standard_clause: Optional[str] = None
    question_summary: Optional[str] = None
    answer: str
    answer_type: Optional[AnswerType] = None
    source_doc: str
    source_section: str


class SemanticFragment(BaseModel):
    fragment_id: str
    fragment_type: FragmentType
    content: str
    topic_tags: list[str] = Field(default_factory=list)
    related_subjects: list[Subject] = Field(default_factory=list)
    source_doc: str
    source_section: str


# ---------------------------------------------------------------------
# 层3补充：流程/记录类（v0.2 数据驱动新增，见 _convert/gap_report.md）
# ---------------------------------------------------------------------
class RevisionRecord(BaseModel):  # 🆕
    rev_id: str
    doc_id: str
    seq: Optional[int] = None
    version: Optional[str] = None
    change_description: Optional[str] = None
    author: Optional[str] = None
    approver: Optional[str] = None
    date: Optional[str] = None


class ReviewItem(BaseModel):  # 🆕 最大缺口
    item_id: str
    review_id: Optional[str] = None
    doc_id: str
    seq: Optional[int] = None
    category: Optional[str] = None
    content: str
    actual_situation: Optional[str] = None
    conclusion: Optional[ReviewConclusion] = None
    improvement: Optional[str] = None
    note: Optional[str] = None


class DocIndexEntry(BaseModel):  # 🆕 DHF/设计输出清单条目
    entry_id: str
    index_doc_id: str
    seq: Optional[int] = None
    file_name: str
    file_no: Optional[str] = None
    form: Optional[str] = None
    location: Optional[str] = None
    stage: Optional[str] = None
    signed: Optional[bool] = None
    applicable: Optional[bool] = None
    date: Optional[str] = None


class TestMeasurement(BaseModel):  # 🆕 实测数据行
    meas_id: str
    test_id: Optional[str] = None
    doc_id: str
    machine_no: Optional[str] = None
    test_point: Optional[str] = None
    reading: Optional[str] = None
    unit: Optional[str] = None
    reference_value: Optional[str] = None
    condition: Optional[str] = None


class SoftwareItem(BaseModel):  # 🆕 软件条目
    sw_id: str
    doc_id: str
    item_type: SoftwareItemType
    name: str
    description: Optional[str] = None
    value: Optional[str] = None
    run_environment: Optional[str] = None


class SoftwareConfigItem(BaseModel):  # 🆕 软件配置/生命周期行
    sci_id: str
    doc_id: str
    phase: Optional[str] = None
    activity: Optional[str] = None
    config_item: Optional[str] = None
    version: Optional[str] = None


class IssueItem(BaseModel):  # 🆕 问题项
    issue_id: str
    doc_id: str
    seq: Optional[int] = None
    source: Optional[str] = None
    description: str
    cause: Optional[str] = None
    action: Optional[str] = None
    owner: Optional[str] = None
    status: Optional[IssueStatus] = None
    due_date: Optional[str] = None


class PlanTask(BaseModel):  # 🆕 计划任务
    task_id: str
    doc_id: str
    wbs: Optional[str] = None
    name: str
    predecessor: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    owner: Optional[str] = None
    level: Optional[int] = None
    note: Optional[str] = None


class Resource(BaseModel):  # 🆕 资源行
    resource_id: str
    doc_id: str
    name: str
    type: Optional[str] = None
    standard: Optional[str] = None
    rate: Optional[str] = None
    note: Optional[str] = None
