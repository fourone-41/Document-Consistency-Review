# -*- coding: utf-8 -*-
"""
PT9S 覆盖台账：DHF清单(分母) vs 实物文件 vs 转换状态。
回答三个问题，保证"没有一个被悄悄漏掉"：
 Q1 清单 vs 实物：每个清单文件实际存在吗？ -> 缺失 / 未受控(多余)
 Q2 可读性：存在的文件转换成功了吗？        -> 转换失败需补
 Q3 存在形式：纸档文件无电子版属预期，不算硬缺失
输出 coverage_ledger.csv + coverage_ledger.md。
"""
import sys, os, csv, glob, re, xlrd, datetime as dt
from difflib import SequenceMatcher
sys.stdout.reconfigure(encoding="utf-8")

ROOT = r"D:\AI_0415\03DHF\PT9S"
SRC  = os.path.join(ROOT, "PT9S_DHF")
DST  = r"D:\AI_0415\03DHF\PT9S_MD"
DHF_LIST = os.path.join(SRC, "PT9S-DHF清单-常规.xls")
CONV_MANIFEST = os.path.join(DST, "_manifest_conversion.csv")
OUT_CSV = os.path.join(ROOT, "coverage_ledger.csv")
OUT_MD  = os.path.join(ROOT, "coverage_ledger.md")

def norm_name(t):
    t=(t or "").lower().replace("（","(").replace("）",")")
    t=re.sub(r"\s+","",t); t=re.sub(r"[._\-–—/\\+]+","",t)
    t=re.sub(r"v\d+(\.\d+)*","",t); t=re.sub(r"e\d+$","",t)
    for w in ["封面","首页"]: t=t.replace(w,"")
    return t
def norm_no(t):
    t=(t or "").upper().replace("－","-").replace("—","-").replace("–","-")
    t=re.sub(r"\s+","",t).replace("_","-"); return t

def parse_list():
    wb=xlrd.open_workbook(DHF_LIST); sh=wb.sheet_by_index(0)
    out=[]; stage=""
    for r in range(2, sh.nrows):
        row=[str(sh.cell_value(r,c)).strip() for c in range(sh.ncols)]
        while len(row)<7: row.append("")
        if row[0]: stage=row[0]
        seq,name,no,form,date,maker=row[1],row[2],row[3],row[4],row[5],row[6]
        if not name: continue
        # doc number without trailing version
        no_core=re.sub(r"\s*V\d+(\.\d+)*\s*$","",no, flags=re.I)
        out.append({"stage":stage,"seq":seq,"name":name,"doc_no":no,"doc_no_core":no_core,
                    "form":form,"date":date,"maker":maker})
    return out

def actual_files():
    files=[]
    for p in glob.glob(os.path.join(SRC,"**","*"), recursive=True):
        if os.path.isfile(p) and not os.path.basename(p).startswith("~$"):
            files.append(os.path.relpath(p, SRC))
    return files

def load_conv():
    m={}
    if os.path.exists(CONV_MANIFEST):
        with open(CONV_MANIFEST, encoding="utf-8-sig") as f:
            for row in csv.DictReader(f): m[row["rel"]]=row
    return m

def md_text_for(rel, conv):
    r=conv.get(rel)
    if not r or not r.get("md") or not os.path.exists(r["md"]): return ""
    try: return open(r["md"], encoding="utf-8", errors="ignore").read()[:60000]
    except Exception: return ""

def best_match(item, files, conv):
    nm=norm_name(item["name"]); no=norm_no(item["doc_no_core"]); stg=norm_name(item["stage"])
    best=None
    for rel in files:
        stem=os.path.splitext(os.path.basename(rel))[0]
        snorm=norm_name(stem); pnorm=norm_name(rel)
        score=SequenceMatcher(None,nm,snorm).ratio()
        if nm and nm in pnorm: score=max(score,0.9)
        # doc number in path or converted content
        doc_in_path = bool(no and no in norm_no(rel))
        doc_in_text = bool(no and no in norm_no(md_text_for(rel,conv)))
        if stg and stg[:3] and stg[:3] in norm_name(rel): score+=0.15
        if doc_in_path: score+=0.4
        if doc_in_text: score+=0.5
        cand={"rel":rel,"score":round(score,3),"name_score":round(SequenceMatcher(None,nm,snorm).ratio(),3),
              "doc_in_path":doc_in_path,"doc_in_text":doc_in_text}
        if best is None or cand["score"]>best["score"]: best=cand
    return best or {}

def main():
    items=parse_list(); files=actual_files(); conv=load_conv()
    used=set(); rows=[]
    for it in items:
        m=best_match(it, files, conv)
        ns=m.get("name_score",0); doc_ok=m.get("doc_in_path") or m.get("doc_in_text")
        if ns>=0.55 or doc_ok:
            status="ok" if (ns>=0.55 and (doc_ok or True)) else "review"
            if ns<0.55 and not doc_ok: status="review"
        else:
            status="missing"
        rel=m.get("rel","")
        if status!="missing": used.add(rel)
        cstat=conv.get(rel,{}).get("status","") if rel else ""
        note=""
        if status=="missing" and "纸" in it["form"]:
            status="paper_only_no_ecopy"; note="清单标纸档,无电子版属预期"
        if status in("ok","review") and cstat and cstat!="ok":
            note=f"匹配上但转换{cstat},需补读"
        rows.append({**it,"match_status":status,"matched_file":rel,"match_score":m.get("score",""),
                     "name_score":ns,"doc_found":doc_ok,"conv_status":cstat,"note":note})
    # 实物有 清单无
    extra=[f for f in files if f not in used and os.path.splitext(f)[1].lower() in
           (".doc",".docx",".xls",".xlsx",".pdf")]
    # 只报正文类多余(排除图纸/签字档可能合理)
    with open(OUT_CSV,"w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f, fieldnames=["stage","seq","name","doc_no","form","date","maker",
                         "match_status","matched_file","match_score","name_score","doc_found","conv_status","note"],
                         extrasaction="ignore")
        w.writeheader(); w.writerows(rows)
    from collections import Counter
    c=Counter(r["match_status"] for r in rows)
    covered=c.get("ok",0); review=c.get("review",0); missing=c.get("missing",0); paper=c.get("paper_only_no_ecopy",0)
    convfail=sum(1 for r in rows if r["conv_status"] not in ("ok","") )
    total=len(rows)
    lines=[f"# PT9S 覆盖台账（清单 vs 实物 vs 转换）",
        f"- generated_at: {dt.datetime.now().replace(microsecond=0)}",
        f"- 清单条目(分母): **{total}**",
        f"- ✅匹配上(ok): {covered}",
        f"- ⚠️需人工确认(review): {review}",
        f"- ❌缺失(missing): {missing}",
        f"- 📄纸档无电子版(预期): {paper}",
        f"- 🔧匹配上但转换失败需补: {convfail}",
        f"- ➕实物有清单无(多余/未受控正文件): {len(extra)}",
        f"- **有效覆盖率: {covered+review}/{total-paper} = "
        f"{round(100*(covered+review)/max(1,total-paper),1)}% (剔除纸档后)**","",
        "## ❌缺失 / ⚠️review / 🔧转换失败 (需处理)",""]
    lines.append("| 序号 | 阶段 | 文件名 | 编号 | 状态 | 匹配到 | 备注 |")
    lines.append("|---|---|---|---|---|---|---|")
    for r in rows:
        if r["match_status"] in ("ok",) and r["conv_status"]=="ok": continue
        if r["match_status"]=="paper_only_no_ecopy": continue
        lines.append(f"| {r['seq']} | {r['stage']} | {r['name']} | {r['doc_no']} | {r['match_status']} | {os.path.basename(r['matched_file'])} | {r['note']} |")
    if extra:
        lines+=["","## ➕实物有·清单无（正文类，可能未受控/残留/多版本）",""]
        for e in extra[:60]: lines.append(f"- {e}")
    open(OUT_MD,"w",encoding="utf-8").write("\n".join(lines)+"\n")
    print(f"清单 {total} | ok {covered} | review {review} | missing {missing} | 纸档 {paper} | 转换失败 {convfail} | 多余 {len(extra)}")
    print("CSV:",OUT_CSV); print("MD :",OUT_MD)

if __name__=="__main__":
    raise SystemExit(main())
