"""
完整 Schema 定义——按技术文档4层14种节点类型设计

层1: 文档结构层（Document, Section）
层2: 标识与元数据层（Product, Identifier, Person）
层3: 领域实体层（Requirement, DesignInput, Risk, RiskControl, Test, TestReport, Regulation, Function, Component, ReviewRecord）
层4: 对齐与裁决层（Claim, Statement, SemanticFragment）
"""
from __future__ import annotations
from typing import Optional, Literal
from pydantic import BaseModel, Field


# ===== 层1：文档结构层 =====

class Document(BaseModel):
    """一份具体的文件"""
    doc_id: str = Field(description="唯一标识，如 'DHF-01-001'")
    title: str = Field(description="文件标题")
    doc_type: str = Field(description="文件类型：需求书/设计输入/测试报告/风险报告")
    dhf_stage: str = Field(description="DHF阶段：01_立项/03_风险/04_设计输入/11_T1样机")
    version: Optional[str] = Field(default=None, description="版本号")
    filename: str = Field(description="原始文件名")
    date: Optional[str] = Field(default=None, description="文件日期")


class Section(BaseModel):
    """文件中的一个章节/段落/表格行"""
    section_id: str = Field(description="唯一标识")
    doc_id: str = Field(description="所属文件 doc_id")
    heading_path: str = Field(description="层级路径，如 '第3章>3.2性能>表3-1>Row7'")
    order: int = Field(description="在文件中的出现顺序")


# ===== 层2：标识与元数据层 =====

class Product(BaseModel):
    """产品实体"""
    product_id: str = Field(description="产品编号，如 'PT9L'")
    model: Optional[str] = Field(default=None, description="型号")
    name: str = Field(description="产品名称")
    region: Optional[str] = Field(default=None, description="目标市场/地区")


class Identifier(BaseModel):
    """各类标识号"""
    id_type: Literal["产品编号", "项目号", "版本号", "需求编号", "设计输入编号", "风险编号", "测试编号", "文件编号"] = Field(
        description="标识类型"
    )
    value: str = Field(description="编号值")


class Person(BaseModel):
    """人员"""
    name: str = Field(description="姓名")
    dept: Optional[str] = Field(default=None, description="部门")
    title: Optional[str] = Field(default=None, description="职务/职称")
    role: Optional[str] = Field(default=None, description="在文件中的角色：编写人/审核/批准")


# ===== 层3：领域实体层 =====

class Requirement(BaseModel):
    """需求书中的一条需求条目"""
    req_id: Optional[str] = Field(default=None, description="需求编号，如 'REQ-PERF-007'（原文无编号则为None）")
    category: Literal["通用", "功能", "性能", "组件", "法规", "安全", "接口", "其他"] = Field(
        description="需求分类"
    )
    description: str = Field(description="需求描述原文")
    value: Optional[str] = Field(default=None, description="量化值（不含单位），如 '±0.2'、'32.0-42.9'")
    unit: Optional[str] = Field(default=None, description="单位，如 '℃'、'次'")
    condition: Optional[str] = Field(default=None, description="适用条件")
    verification_method: Optional[str] = Field(default=None, description="验证方法：测试/分析/检查/评审")
    source_section: str = Field(description="来源章节/表格行")


class DesignInput(BaseModel):
    """设计输入条目"""
    di_id: Optional[str] = Field(default=None, description="设计输入编号，如 'DI-P-012'（原文无编号则为None）")
    category: Literal["通用", "功能", "性能", "组件", "法规", "安全", "接口", "其他"] = Field(
        description="分类"
    )
    description: str = Field(description="设计输入描述原文")
    value: Optional[str] = Field(default=None, description="量化值（不含单位）")
    unit: Optional[str] = Field(default=None, description="单位")
    condition: Optional[str] = Field(default=None, description="适用条件")
    source_req_id: Optional[str] = Field(default=None, description="来源需求编号（追溯用）")
    source_section: str = Field(description="来源章节/表格行")


class Risk(BaseModel):
    """风险评估中的一条风险项"""
    risk_id: str = Field(description="风险编号如 'H-014'")
    hazard: str = Field(description="危险源")
    hazardous_situation: str = Field(description="危险情况")
    harm: str = Field(description="伤害")
    severity: int = Field(description="严重度 1-5")
    probability: str = Field(description="概率 A-E")
    risk_level: Literal["Acceptable", "ALARP", "Unacceptable"] = Field(description="风险等级")
    phase: Optional[str] = Field(default=None, description="pre-mitigation / post-mitigation")


class RiskControl(BaseModel):
    """风险控制措施"""
    risk_id: str = Field(description="关联的风险编号")
    measure: str = Field(description="措施描述")
    control_type: Literal["降低可能性", "降低危害", "信息安全", "其他"] = Field(description="措施类型")
    evidence_type: Optional[str] = Field(default=None, description="证据类型：测试报告/分析")


class Test(BaseModel):
    """一次具体的测试"""
    test_id: Optional[str] = Field(default=None, description="测试编号")
    item: str = Field(description="测试项目名称")
    condition: Optional[str] = Field(default=None, description="测试条件（环境温度、湿度等）")
    expected_value: Optional[str] = Field(default=None, description="预期结果/合格标准值（不含单位）")
    expected_unit: Optional[str] = Field(default=None, description="预期值单位")
    actual_result: Optional[str] = Field(default=None, description="实际测试结果值（不含单位）")
    actual_unit: Optional[str] = Field(default=None, description="实际值单位")
    pass_fail: Optional[Literal["PASS", "FAIL", "N/A"]] = Field(default=None, description="单项结论")
    source_section: str = Field(description="来源章节/表格行")


class TestReport(BaseModel):
    """测试报告整体信息"""
    report_id: Optional[str] = Field(default=None, description="报告编号")
    report_title: str = Field(description="报告标题")
    conclusion: Optional[Literal["PASS", "FAIL", "CONDITIONAL"]] = Field(default=None, description="整体结论")
    test_date: Optional[str] = Field(default=None, description="测试日期")
    equipment: Optional[str] = Field(default=None, description="使用设备")


class Regulation(BaseModel):
    """法规/标准条款"""
    std_id: str = Field(description="标准号，如 'IEC 80601-2-56:2017'、'GB/T 21417.1'")
    version: Optional[str] = Field(default=None, description="版本/年份")
    clause: Optional[str] = Field(default=None, description="条款号")
    requirement_text: Optional[str] = Field(default=None, description="法规要求描述")
    relevance: str = Field(description="与产品的关系：适用标准/合规要求/参考依据")


class Function(BaseModel):
    """产品功能项"""
    name: str = Field(description="功能名称")
    description: Optional[str] = Field(default=None, description="功能描述")


class Component(BaseModel):
    """BOM零部件/产品组件"""
    part_no: Optional[str] = Field(default=None, description="物料编号")
    name: str = Field(description="组件名称，如 'NTC传感器'、'LCD显示屏'")
    component_type: Literal[
        "sensor", "display", "structure", "pcb", "battery", "optical", "packaging", "other",
    ] = Field(description="组件分类")
    spec: Optional[str] = Field(default=None, description="规格/关键属性")


class ReviewRecord(BaseModel):
    """评审记录"""
    review_id: Optional[str] = Field(default=None)
    stage: str = Field(description="所属阶段")
    date: Optional[str] = Field(default=None)
    conclusion: Optional[str] = Field(default=None, description="评审结论")


# ===== 层4：对齐与裁决层 =====

class Claim(BaseModel):
    """归一化事实断言——整个系统的对齐主干"""
    subject: str = Field(description="标准化主题词（如 measurement_accuracy）")
    attribute: str = Field(description="具体方面：tolerance/range/threshold/count/value")
    value: Optional[str] = Field(default=None, description="数值（不含单位）")
    unit: Optional[str] = Field(default=None, description="单位")
    condition: Optional[str] = Field(default=None, description="适用条件/前提")
    raw_text: str = Field(description="原文片段")
    source_entity_type: str = Field(description="来源实体类型：Requirement/DesignInput/Test")
    source_doc: str = Field(description="来源文件名")
    source_section: str = Field(description="来源章节")


class SemanticFragment(BaseModel):
    """语义片段——无法结构化为Claim但包含审查相关信息的描述性段落"""
    fragment_type: Literal[
        "design_rationale",
        "working_principle",
        "constraint_statement",
        "behavioral_spec",
        "open_issue",
        "scope_limitation",
        "assumption",
    ] = Field(description="片段类型")
    content: str = Field(description="原文内容完整保留")
    topic_tags: list[str] = Field(description="2-5个主题标签")
    related_subjects: list[str] = Field(description="关联的标准化主题词")
    source_section: str = Field(description="来源章节")


# ===== 抽取阶段的关系 =====

class Relationship(BaseModel):
    """实体间关系"""
    source_type: str = Field(description="起点实体类型")
    source_id: str = Field(description="起点标识（名称或编号）")
    relation: Literal[
        "DERIVES_FROM",       # DesignInput → Requirement
        "CONSTRAINED_BY",     # Requirement → Regulation
        "VERIFIED_BY",        # DesignInput/RiskControl → Test
        "MITIGATED_BY",       # Risk → RiskControl
        "REPORTED_IN",        # Test → TestReport
        "REFERENCES",         # Document → Document
        "RELATES_TO",         # SemanticFragment → Claim subject
    ] = Field(description="关系类型")
    target_type: str = Field(description="终点实体类型")
    target_id: str = Field(description="终点标识（名称或编号）")


# ===== 按文档类型的抽取结果容器 =====

class RequirementDocExtraction(BaseModel):
    """客户需求书的抽取结果"""
    requirements: list[Requirement] = Field(default_factory=list)
    identifiers: list[Identifier] = Field(default_factory=list)
    persons: list[Person] = Field(default_factory=list)
    products: list[Product] = Field(default_factory=list)
    regulations: list[Regulation] = Field(default_factory=list)
    components: list[Component] = Field(default_factory=list)
    functions: list[Function] = Field(default_factory=list)
    fragments: list[SemanticFragment] = Field(default_factory=list)
    relationships: list[Relationship] = Field(default_factory=list)


class DesignInputDocExtraction(BaseModel):
    """设计输入汇总表的抽取结果"""
    design_inputs: list[DesignInput] = Field(default_factory=list)
    identifiers: list[Identifier] = Field(default_factory=list)
    persons: list[Person] = Field(default_factory=list)
    products: list[Product] = Field(default_factory=list)
    regulations: list[Regulation] = Field(default_factory=list)
    components: list[Component] = Field(default_factory=list)
    functions: list[Function] = Field(default_factory=list)
    fragments: list[SemanticFragment] = Field(default_factory=list)
    relationships: list[Relationship] = Field(default_factory=list)


class TestReportDocExtraction(BaseModel):
    """检测报告的抽取结果"""
    test_report: Optional[TestReport] = Field(default=None)
    tests: list[Test] = Field(default_factory=list)
    identifiers: list[Identifier] = Field(default_factory=list)
    persons: list[Person] = Field(default_factory=list)
    products: list[Product] = Field(default_factory=list)
    regulations: list[Regulation] = Field(default_factory=list)
    components: list[Component] = Field(default_factory=list)
    fragments: list[SemanticFragment] = Field(default_factory=list)
    relationships: list[Relationship] = Field(default_factory=list)
