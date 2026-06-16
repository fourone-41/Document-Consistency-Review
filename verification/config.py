import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

API_KEY = os.getenv("GPT55_API_KEY", "")
LLM_BASE_URL = os.getenv("GPT55_API_URL", "https://ai-gateway.ailab.jiuan.com/v1")
LLM_MODEL = os.getenv("GPT55_MODEL", "claude-sonnet-4-6")

MARKDOWN_ROOT = PROJECT_ROOT / "pt9l_markdown_output"
OUTPUT_DIR = Path(__file__).resolve().parent / "output"

SOURCE_FILES = [
    MARKDOWN_ROOT / "01 立项批准书E0 23.11" / "客户需求书E0-血压计 23.6.via_xlsx.clean.md",
    MARKDOWN_ROOT / "04 设计输入E0 23.11" / "设计输入汇总表E0  20211118.via_xlsx.clean.md",
    MARKDOWN_ROOT / "11 T1样机" / "PT9L红外体温计检测报告 V1.0.via_lo_html.clean.md",
]

# 文件→文档类型映射（决定 Claim 的 claim_role）
DOC_TYPE_MAP = {
    "客户需求书E0-血压计 23.6.via_xlsx.clean.md": "customer_requirement",
    "设计输入汇总表E0  20211118.via_xlsx.clean.md": "design_input",
    "PT9L红外体温计检测报告 V1.0.via_lo_html.clean.md": "test_report",
}

NEO4J_URI = "bolt://localhost:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "test1234"
