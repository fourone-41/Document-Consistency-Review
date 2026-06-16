"""Re-run extraction for test report only."""
import sys
sys.path.insert(0, r"D:\项目文档一致性审查\verification")
from step1_extract import process_file, OUTPUT_DIR
from pathlib import Path
import json

filepath = Path(r"D:\项目文档一致性审查\pt9l_markdown_output\11 T1样机\PT9L红外体温计检测报告 V1.0.via_lo_html.clean.md")
result = process_file(filepath)

out_file = OUTPUT_DIR / "raw_extraction" / f"{filepath.stem}.json"
with open(out_file, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print(f"\nDone: {out_file}")
print(f"Claims: {result['total_claims']}")
print(f"Fragments: {result['total_fragments']}")
print(f"Standards: {result['total_standards']}")
print(f"Components: {result['total_components']}")

# Update summary
summary_path = OUTPUT_DIR / "raw_extraction" / "_summary.json"
with open(summary_path, "r", encoding="utf-8") as f:
    summary = json.load(f)

# Update the test report entry
for file_entry in summary["files"]:
    if "检测报告" in file_entry["name"]:
        file_entry["claims"] = result["total_claims"]
        file_entry["fragments"] = result["total_fragments"]
        file_entry["standards"] = result["total_standards"]
        file_entry["components"] = result["total_components"]

summary["total_claims"] = sum(fe["claims"] for fe in summary["files"])
summary["total_fragments"] = sum(fe["fragments"] for fe in summary["files"])
summary["total_standards"] = sum(fe["standards"] for fe in summary["files"])
summary["total_components"] = sum(fe["components"] for fe in summary["files"])

with open(summary_path, "w", encoding="utf-8") as f:
    json.dump(summary, f, ensure_ascii=False, indent=2)
print("Summary updated.")
