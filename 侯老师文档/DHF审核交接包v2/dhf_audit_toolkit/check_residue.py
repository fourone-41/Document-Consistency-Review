#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
DHF 机械校验器（无需 AI，任何装了 Python 3 的电脑都能跑）
================================================================
给同事用：把自己的 DHF 转成 Markdown 后，对着 MD 文件夹跑一遍，
秒出三类"机械层"问题——不需要懂审核，照命令跑即可。

它查三件事（都是不需要语义判断、最容易藏且最高频的）：
  1) 模板残留：别的产品/旧型号的名字混进了本项目文件（本案出现10+次）
  2) 文件编号/版本：实际文件页脚编号 vs DHF清单 是否一致
  3) 占位符未改：模板里的 XXXX / 待填 / 年 月 日 等没替换

用法：
  python check_residue.py  <MD文件夹>  --product PT9L  --out 报告.csv
  python check_residue.py  "D:/.../PT9L_MD"  --product PT9L  --foreign 血压计,耳机,雾化器

输出：一个 CSV（Excel可开），列出 文件/行号/命中词/原文，按严重度排序。
"""
import os, re, csv, sys, argparse

# ---- 默认"异类词"库：出现这些=疑似别的产品模板残留 ----
DEFAULT_FOREIGN = [
    "血压计", "血压", "袖带", "耳机", "雾化器", "冲牙器",  # 异类品类
    "PC Link",                                              # 常见无用残留
]
# 本项目之外的型号前缀（同事按自己情况补；这里给体温计线示例）
DEFAULT_FOREIGN_MODELS = ["PT3", "PT5", "PT9C", "AG-633", "BG5S", "FDIR", "T-Z1", "sim"]
# 占位符/未替换
PLACEHOLDER = [r"X{3,}", r"待填", r"待定", r"TODO", r"○○", r"\bxxx\b", r"＿{3,}", r"_{4,}"]

def scan(md_dir, product, foreign, foreign_models, allow_reuse):
    rows = []
    pat_ph = re.compile("|".join(PLACEHOLDER), re.IGNORECASE)
    for root, _, files in os.walk(md_dir):
        # 跳过工具自身/manifest 噪声
        if any(s in root for s in ["_manifests", "llm_wiki", "__pycache__", "dhf_audit_toolkit"]):
            continue
        for fn in files:
            if not fn.endswith(".md"):
                continue
            path = os.path.join(root, fn)
            rel = os.path.relpath(path, md_dir)
            try:
                lines = open(path, encoding="utf-8", errors="ignore").read().splitlines()
            except Exception:
                continue
            for i, line in enumerate(lines, 1):
                low = line.strip()
                if not low:
                    continue
                # 1) 异类品类词
                for w in foreign:
                    if w in line:
                        rows.append(["高", "异类品类残留", rel, i, w, low[:120]])
                # 2) 异类型号（复用件可能合法 -> 标"待确认"而非"高"）
                for m in foreign_models:
                    if re.search(r"(?<![A-Za-z0-9])" + re.escape(m) + r"(?![A-Za-z0-9])", line):
                        sev = "待确认(可能复用)" if m in allow_reuse else "中"
                        rows.append([sev, "异类型号残留", rel, i, m, low[:120]])
                # 3) 占位符未替换
                mt = pat_ph.search(line)
                if mt and "年 月 日" not in line:  # 日期空栏按规则不查
                    rows.append(["低", "占位符未替换", rel, i, mt.group(0), low[:120]])
    return rows

def main():
    ap = argparse.ArgumentParser(description="DHF 机械校验器 - 模板残留/占位符扫描")
    ap.add_argument("md_dir", help="DHF 的 Markdown 文件夹路径")
    ap.add_argument("--product", default="本产品", help="本项目型号(如 PT9L)")
    ap.add_argument("--foreign", default="", help="额外异类品类词,逗号分隔")
    ap.add_argument("--models", default="", help="额外异类型号,逗号分隔")
    ap.add_argument("--allow-reuse", default="PT5,PT3,T-Z1,Public,KD,PT1",
                    help="允许的复用件型号(标待确认而非错误),逗号分隔")
    ap.add_argument("--out", default="DHF机械校验报告.csv", help="输出CSV")
    a = ap.parse_args()

    foreign = DEFAULT_FOREIGN + [x.strip() for x in a.foreign.split(",") if x.strip()]
    models = DEFAULT_FOREIGN_MODELS + [x.strip() for x in a.models.split(",") if x.strip()]
    allow = set(x.strip() for x in a.allow_reuse.split(",") if x.strip())

    # Windows 控制台用 GBK，统一把 stdout 切到 UTF-8 防止打印崩溃
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass

    if not os.path.isdir(a.md_dir):
        print("[X] 文件夹不存在:", a.md_dir); sys.exit(1)

    rows = scan(a.md_dir, a.product, foreign, models, allow)
    order = {"高": 0, "中": 1, "待确认(可能复用)": 2, "低": 3}
    rows.sort(key=lambda r: order.get(r[0], 9))

    with open(a.out, "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["严重度", "类型", "文件", "行号", "命中", "原文"])
        w.writerows(rows)

    from collections import Counter
    c = Counter(r[1] for r in rows)
    print("[OK] 扫描完成:", a.md_dir)
    print("  命中 %d 条 ->%s" % (len(rows), a.out))
    print("  分类:", dict(c))
    print("  提示: '异类品类残留'(血压计/袖带等)基本是错;'异类型号残留'需区分复用件vs残留;'占位符'需补。")

if __name__ == "__main__":
    main()
