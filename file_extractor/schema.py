"""Pydantic models mirroring schema.yaml for structured LLM extraction."""
from __future__ import annotations
from typing import Optional, Literal
from pydantic import BaseModel, Field


# ============================================================
# Enums as Literals
# ============================================================
CategoryLit = Literal["通用", "功能", "性能", "组件", "法规"]
IdTypeLit = Literal[
    "产品编号", "项目号", "版本号", "文件编号", "需求编号",
    "设计输入编号", "风险编号", "测试编号", "物料编码", "表单号", "图纸号", "WBS号"
]
DirectionLit = Literal["smaller_is_better", "larger_is_better", "wider_is_better", "exact_match"]
RiskLevelLit = Literal["Acceptable", "ALARP", "Unacceptable"]
ConclusionLit = Literal["PASS", "FAIL", "CONDITIONAL"]
AnswerTypeLit = Literal["yes", "no", "descriptive", "quantitative", "n_a"]
CriticalityLit = Literal["A", "B", "C"]
FragmentTypeLit = Literal[
    "design_rationale", "working_principle", "constraint_statement",
    "behavioral_spec", "open_issue", "scope_limitation", "assumption"
]
ReviewConclusionLit = Literal["通过", "不通过", "待整改", "不适用"]
IssueStatusLit = Literal["open", "in_progress", "closed"]
SoftwareItemTypeLit = Literal["功能模块", "设计规格", "通信命令", "软硬件接口", "运行环境", "其它"]


# ============================================================
# Layer 1: Structure
# ============================================================
class Document(BaseModel):
    doc_id: Optional[str] = None
    title: str
    doc_type: str
    dhf_stage: Optional[str] = None
    version: Optional[str] = None
    filename: Optional[str] = None
    date: Optional[str] = None


class Section(BaseModel):
    section_id: str
    doc_id: str
    heading_path: Optional[str] = None
    order: Optional[int] = None


# ============================================================
# Layer 2: Anchors
# ============================================================
class Product(BaseModel):
    product_id: str
    model: Optional[str] = None
    name: str
    region: Optional[str] = None


class Identifier(BaseModel):
    id_type: IdTypeLit
    value: str


class Person(BaseModel):
    name: str
    dept: Optional[str] = None
    title: Optional[str] = None
    signed: Optional[bool] = None


class Market(BaseModel):
    market_id: Optional[str] = None
    region: Optional[str] = None
    certification: Optional[str] = None
    selected: Optional[bool] = None
    registrant: Optional[str] = None
    registration_path: Optional[str] = None


class IntendedUseItem(BaseModel):
    item_id: Optional[str] = None
    seq: Optional[int] = None
    content: str


# ============================================================
# Layer 3: Domain Entities
# ============================================================
class Requirement(BaseModel):
    req_id: Optional[str] = None
    category: Optional[CategoryLit] = None
    description: str
    value: Optional[str] = None
    unit: Optional[str] = None
    tolerance: Optional[str] = None
    condition: Optional[str] = None
    verification_method: Optional[str] = None


class DesignInput(BaseModel):
    di_id: Optional[str] = None
    category: Optional[CategoryLit] = None
    description: str
    value: Optional[str] = None
    unit: Optional[str] = None
    tolerance: Optional[str] = None
    condition: Optional[str] = None
    source_req_id: Optional[str] = None


class Risk(BaseModel):
    risk_id: Optional[str] = None
    hazard: str
    hazardous_situation: Optional[str] = None
    harm: Optional[str] = None
    severity: Optional[int] = None
    probability: Optional[str] = None
    risk_level: Optional[RiskLevelLit] = None
    phase: Optional[str] = None


class RiskControl(BaseModel):
    control_id: Optional[str] = None
    measure: str
    type: Optional[str] = None
    evidence_type: Optional[str] = None


class Test(BaseModel):
    test_id: Optional[str] = None
    item: str
    condition: Optional[str] = None
    expected_value: Optional[str] = None
    actual_result: Optional[str] = None
    pass_criteria: Optional[str] = None
    instrument: Optional[str] = None
    environment: Optional[str] = None


class TestReport(BaseModel):
    report_id: Optional[str] = None
    conclusion: Optional[ConclusionLit] = None
    evidence_level: Optional[str] = None


class Regulation(BaseModel):
    reg_id: Optional[str] = None
    std_id: str
    version: Optional[str] = None
    clause: Optional[str] = None
    region: Optional[str] = None
    applicable: Optional[bool] = None
    equivalent_std: Optional[str] = None
    requirement_value: Optional[str] = None
    requirement_text: Optional[str] = None


class Function(BaseModel):
    name: str
    description: Optional[str] = None
    value: Optional[str] = None
    exists: Optional[bool] = True


class Component(BaseModel):
    part_no: Optional[str] = None
    name: str
    spec: Optional[str] = None
    model: Optional[str] = None
    ref_des: Optional[str] = None
    qty: Optional[str] = None
    criticality: Optional[CriticalityLit] = None
    rohs: Optional[bool] = None
    board: Optional[str] = None


class ReviewRecord(BaseModel):
    review_id: Optional[str] = None
    stage: Optional[str] = None
    date: Optional[str] = None
    conclusion: Optional[str] = None


# ============================================================
# Layer 3 Supplement: Process/Record Types
# ============================================================
class RevisionRecord(BaseModel):
    rev_id: Optional[str] = None
    doc_id: Optional[str] = None
    seq: Optional[int] = None
    version: Optional[str] = None
    change_description: Optional[str] = None
    author: Optional[str] = None
    approver: Optional[str] = None
    date: Optional[str] = None


class ReviewItem(BaseModel):
    item_id: Optional[str] = None
    review_id: Optional[str] = None
    doc_id: Optional[str] = None
    seq: Optional[int] = None
    category: Optional[str] = None
    content: str
    actual_situation: Optional[str] = None
    conclusion: Optional[ReviewConclusionLit] = None
    improvement: Optional[str] = None
    note: Optional[str] = None


class DocIndexEntry(BaseModel):
    entry_id: Optional[str] = None
    index_doc_id: Optional[str] = None
    seq: Optional[int] = None
    file_name: str
    file_no: Optional[str] = None
    form: Optional[str] = None
    location: Optional[str] = None
    stage: Optional[str] = None
    signed: Optional[bool] = None
    applicable: Optional[bool] = None
    date: Optional[str] = None


class TestMeasurement(BaseModel):
    meas_id: Optional[str] = None
    test_id: Optional[str] = None
    doc_id: Optional[str] = None
    machine_no: Optional[str] = None
    test_point: Optional[str] = None
    reading: Optional[str] = None
    unit: Optional[str] = None
    reference_value: Optional[str] = None
    condition: Optional[str] = None


class SoftwareItem(BaseModel):
    sw_id: Optional[str] = None
    doc_id: Optional[str] = None
    item_type: Optional[SoftwareItemTypeLit] = None
    name: str
    description: Optional[str] = None
    value: Optional[str] = None
    run_environment: Optional[str] = None


class SoftwareConfigItem(BaseModel):
    sci_id: Optional[str] = None
    doc_id: Optional[str] = None
    phase: Optional[str] = None
    activity: Optional[str] = None
    config_item: Optional[str] = None
    version: Optional[str] = None


class IssueItem(BaseModel):
    issue_id: Optional[str] = None
    doc_id: Optional[str] = None
    seq: Optional[int] = None
    source: Optional[str] = None
    description: str
    cause: Optional[str] = None
    action: Optional[str] = None
    owner: Optional[str] = None
    status: Optional[IssueStatusLit] = None
    due_date: Optional[str] = None


class PlanTask(BaseModel):
    task_id: Optional[str] = None
    doc_id: Optional[str] = None
    wbs: Optional[str] = None
    name: str
    predecessor: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    owner: Optional[str] = None
    level: Optional[int] = None
    note: Optional[str] = None


class Resource(BaseModel):
    resource_id: Optional[str] = None
    doc_id: Optional[str] = None
    name: str
    type: Optional[str] = None
    standard: Optional[str] = None
    rate: Optional[str] = None
    note: Optional[str] = None


# ============================================================
# Layer 4: Adjudication
# ============================================================
class SemanticFragment(BaseModel):
    fragment_id: Optional[str] = None
    fragment_type: Optional[FragmentTypeLit] = None
    content: str
    topic_tags: Optional[list[str]] = None
    related_subjects: Optional[list[str]] = None
    source_doc: Optional[str] = None
    source_section: Optional[str] = None


class Claim(BaseModel):
    """归一化事实断言（第二步生成）"""
    claim_id: Optional[str] = None
    subject: str = Field(description="标准化主题词（自由文本，用文档中最自然的术语）")
    attribute: str = Field(description="该主题的具体方面（允差/范围/阈值/实测值/判据）")
    value: Optional[str] = None
    unit: Optional[str] = None
    tolerance: Optional[str] = None
    condition: Optional[str] = None
    raw_text: Optional[str] = Field(default=None, description="原文")
    source_doc: Optional[str] = None
    source_section: Optional[str] = None


# ============================================================
# Extraction Result Containers (per doc type)
# ============================================================
class BaseExtraction(BaseModel):
    """Base container that all doc type extractions share."""
    document: Optional[Document] = None
    persons: list[Person] = Field(default_factory=list)
    identifiers: list[Identifier] = Field(default_factory=list)
    products: list[Product] = Field(default_factory=list)
    regulations: list[Regulation] = Field(default_factory=list)
    revision_records: list[RevisionRecord] = Field(default_factory=list)
    semantic_fragments: list[SemanticFragment] = Field(default_factory=list)


class RequirementDocExtraction(BaseExtraction):
    requirements: list[Requirement] = Field(default_factory=list)
    markets: list[Market] = Field(default_factory=list)
    intended_use_items: list[IntendedUseItem] = Field(default_factory=list)
    functions: list[Function] = Field(default_factory=list)


class DesignInputDocExtraction(BaseExtraction):
    design_inputs: list[DesignInput] = Field(default_factory=list)
    markets: list[Market] = Field(default_factory=list)
    functions: list[Function] = Field(default_factory=list)
    components: list[Component] = Field(default_factory=list)


class RiskDocExtraction(BaseExtraction):
    risks: list[Risk] = Field(default_factory=list)
    risk_controls: list[RiskControl] = Field(default_factory=list)


class TestReportDocExtraction(BaseExtraction):
    tests: list[Test] = Field(default_factory=list)
    test_reports: list[TestReport] = Field(default_factory=list)
    test_measurements: list[TestMeasurement] = Field(default_factory=list)


class BOMDocExtraction(BaseExtraction):
    components: list[Component] = Field(default_factory=list)


class ReviewDocExtraction(BaseExtraction):
    review_records: list[ReviewRecord] = Field(default_factory=list)
    review_items: list[ReviewItem] = Field(default_factory=list)


class SoftwareDocExtraction(BaseExtraction):
    software_items: list[SoftwareItem] = Field(default_factory=list)
    software_config_items: list[SoftwareConfigItem] = Field(default_factory=list)
    functions: list[Function] = Field(default_factory=list)


class DevPlanDocExtraction(BaseExtraction):
    plan_tasks: list[PlanTask] = Field(default_factory=list)
    resources: list[Resource] = Field(default_factory=list)


class DHFIndexDocExtraction(BaseExtraction):
    doc_index_entries: list[DocIndexEntry] = Field(default_factory=list)


class GeneralDocExtraction(BaseExtraction):
    requirements: list[Requirement] = Field(default_factory=list)
    design_inputs: list[DesignInput] = Field(default_factory=list)
    tests: list[Test] = Field(default_factory=list)
    functions: list[Function] = Field(default_factory=list)
    components: list[Component] = Field(default_factory=list)
    review_items: list[ReviewItem] = Field(default_factory=list)
    software_items: list[SoftwareItem] = Field(default_factory=list)
    plan_tasks: list[PlanTask] = Field(default_factory=list)
    markets: list[Market] = Field(default_factory=list)
    intended_use_items: list[IntendedUseItem] = Field(default_factory=list)


# Map doc_type -> extraction model
DOC_TYPE_TO_MODEL = {
    "project_approval": RequirementDocExtraction,
    "requirement": RequirementDocExtraction,
    "design_input": DesignInputDocExtraction,
    "risk_analysis": RiskDocExtraction,
    "test_report": TestReportDocExtraction,
    "bom": BOMDocExtraction,
    "review_checklist": ReviewDocExtraction,
    "software_design": SoftwareDocExtraction,
    "dev_plan": DevPlanDocExtraction,
    "dhf_index": DHFIndexDocExtraction,
    "design_output": GeneralDocExtraction,
    "t1_prototype": TestReportDocExtraction,
    "structural_dhf": ReviewDocExtraction,
    "design_validation": TestReportDocExtraction,
    "general": GeneralDocExtraction,
}
