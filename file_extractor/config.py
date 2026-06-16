"""Configuration for the file_extractor pipeline."""
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).parent
PROJECT_ROOT = BASE_DIR.parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.getenv("GPT55_API_KEY", "")
LLM_BASE_URL = os.getenv("GPT55_API_URL", "https://ai-gateway.ailab.jiuan.com/v1")
LLM_MODEL = os.getenv("GPT55_MODEL", "claude-sonnet-4-6")
DASHSCOPE_API_KEY = os.getenv("DASHSCOPE_API_KEY", "")
DASHSCOPE_EMBEDDING_MODEL = os.getenv("DASHSCOPE_EMBEDDING_MODEL", "text-embedding-v3")
DASHSCOPE_BASE_URL = "https://dashscope.aliyuncs.com/compatible-mode/v1"
NEO4J_URI = "bolt://localhost:7687"
NEO4J_AUTH = ("neo4j", "test1234")

MARKDOWN_DIR = PROJECT_ROOT / "pt9l_markdown_output"
OUTPUT_DIR = BASE_DIR / "output"
PER_FILE_DIR = OUTPUT_DIR / "per_file"

MAX_CHUNK_CHARS = 6000
LLM_MAX_TOKENS = 16000

EXCLUDE_FOLDERS = {"历史记录"}

DOC_TYPE_MAP = {
    "01 立项批准书": "project_approval",
    "02 开发计划": "dev_plan",
    "03 风险分析": "risk_analysis",
    "04 设计输入": "design_input",
    "07 软件设计方案": "software_design",
    "11 T1样机": "t1_prototype",
    "12 设计输出": "design_output",
    "18 设计确认": "design_validation",
    "PT9结构DHF": "structural_dhf",
    "PT9L-DHF清单": "dhf_index",
}

def detect_doc_type(filepath: str) -> str:
    """Detect document type from file path."""
    fp = str(filepath).replace("\\", "/")
    fname = Path(filepath).stem.lower()
    # Filename-based detection takes priority for specific document types
    if "评审" in fname or "检查表" in fname:
        return "review_checklist"
    if "检测报告" in fname or ("测试" in fname and "报告" in fname):
        return "test_report"
    if "bom" in fname or "组件清单" in fname:
        return "bom"
    # Then check folder-based mapping
    for folder_key, doc_type in DOC_TYPE_MAP.items():
        if folder_key in fp:
            return doc_type
    # Remaining filename-based
    if "风险" in fname or "risk" in fname or "fmea" in fname:
        return "risk_analysis"
    if "需求" in fname:
        return "requirement"
    if "设计输入" in fname:
        return "design_input"
    if "软件" in fname or "software" in fname:
        return "software_design"
    if "计划" in fname or "plan" in fname:
        return "dev_plan"
    if "清单" in fname:
        return "dhf_index"
    return "general"
