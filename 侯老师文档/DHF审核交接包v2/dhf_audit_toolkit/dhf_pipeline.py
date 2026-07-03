# -*- coding: utf-8 -*-
"""
DHF 审核流水线（一条命令跑前处理 + 机械检查）—— 加新型号只改顶部 MODELS。
================================================================
分两段(中间夹一段 Claude AI 语义审核):
  python dhf_pipeline.py <型号> setup       # ① 转换 ② 覆盖台账 ③ 残留扫描  (前处理,纯确定性)
  --- 这里用 Claude 跑 AI 语义审核(阶段轴+维度轴 workflow),产出参数明细/错误总表 ---
  python dhf_pipeline.py <型号> mechanical   # ④ 数值一致 ⑤(可选)表diff/对账  (机械层,确定性)

依赖:本目录 check_residue.py / check_params_numeric.py / check_table_diff.py / check_bom_crosswalk.py
本机需:Windows + Office(Word COM) + python 包 xlrd/openpyxl/PyMuPDF(fitz)
"""
import sys, os, csv, re, glob, json, subprocess, argparse, datetime as dt
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

HERE = os.path.dirname(os.path.abspath(__file__))
BASE = r"D:\AI_0415\03DHF"   # 工作根;新机器改这里

# ================= 加新型号:复制一段改路径+根决策 =================
MODELS = {
 "PT9S": {
   "raw":  BASE+r"\PT9S\PT9S_DHF",
   "md":   BASE+r"\PT9S_MD",
   "check":BASE+r"\PT9S_CHECK",
   "dhf_list_glob": "*DHF清单*.xls",          # 清单(分母)在 raw 下的名字
   "market":"仅美国", "category":"红外体温计",
   "foreign":"血压计,袖带,耳机,雾化器,冲牙器",  # 异类品类(残留扫描)
   "models":"PT3,PT5,PT7,PT9C,PT9L,AG-633,BG5S,FDIR,T-Z1,KD",  # 异类型号
   "params": BASE+r"\PT9S_CHECK\PT9S-参数明细.csv",  # AI审核后产出(机械层数值检查用)
 },
 "PT9L": {
   "raw":  BASE+r"\PT9L",
   "md":   BASE+r"\PT9L_MD",
   "check":BASE+r"\PT9L_CHECK",
   "dhf_list_glob": "*DHF清单*.xls",
   "market":"仅美国", "category":"红外额温计",
   "foreign":"血压计,袖带,耳机,雾化器,冲牙器",
   "models":"PT3,PT5,PT7,PT9C,PT9S,AG-633,BG5S,FDIR,T-Z1,KD",
   "params": BASE+r"\PT9L_CHECK\PT9L_408参数抽取明细.csv",
 },
 "PT7": {
   "raw":  BASE+r"\new_pt7",
   "md":   BASE+r"\new_pt7_MD",
   "check":BASE+r"\new_pt7_CHECK",
   "dhf_list_glob": "*DHF清单*.xls",
   "market":"待立项确认", "category":"红外额温计",
   "foreign":"血压计,袖带,耳机,雾化器,冲牙器",
   "models":"PT3,PT5,PT9C,PT9L,PT9S,AG-633,BG5S,FDIR,T-Z1,KD",
   "params": BASE+r"\new_pt7_CHECK\PT7-参数明细.csv",
 },
 # "M10": {... 复制上面一段, 改 raw/md/check/market/category/foreign/models ...},
}

def now(): return dt.datetime.now().replace(microsecond=0).isoformat(sep=" ")
def clean(t):
    if not t: return ""
    t=t.replace("\x07"," | ").replace("\x0b","\n").replace("\r","\n")
    t=re.sub(r"[\x00-\x08\x0e-\x1f]","",t); t=re.sub(r"[ \t]+"," ",t); t=re.sub(r"\n{3,}","\n\n",t)
    return t.strip()
def md_table(rows,max_rows=400,max_cols=20):
    rows=[r[:max_cols] for r in rows[:max_rows]]
    if not rows: return ""
    w=max(len(r) for r in rows); rows=[list(r)+[""]*(w-len(r)) for r in rows]
    def c(x): return clean(str(x)).replace("\n"," ").replace("|","\\|")[:200]
    out=["| "+" | ".join(c(x) for x in rows[0])+" |","| "+" | ".join("---" for _ in rows[0])+" |"]
    for r in rows[1:]: out.append("| "+" | ".join(c(x) for x in r)+" |")
    return "\n".join(out)

# -------- ① 转换 --------
def convert(cfg):
    SRC,DST=cfg["raw"],cfg["md"]; os.makedirs(DST,exist_ok=True)
    man=os.path.join(DST,"_manifest_conversion.csv")
    files=[p for p in glob.glob(os.path.join(SRC,"**","*"),recursive=True)
           if os.path.isfile(p) and not os.path.basename(p).startswith("~$")
           and os.path.splitext(p)[1].lower() in {".doc",".docx",".xls",".xlsx",".pdf"}]
    files.sort(); print(f"[转换] 待转 {len(files)} 个 -> {DST}",flush=True)
    word=None; rows=[]
    def header(rel,src,typ,st,loss):
        return ("---\n"+f"source_file: {src}\nsource_relative: {rel}\nsource_type: {typ}\n"
                f"conversion_status: {st}\nloss_flags: {';'.join(loss)}\nconverted_at: {now()}\n---\n\n")
    for i,f in enumerate(files,1):
        rel=os.path.relpath(f,SRC); ext=os.path.splitext(f)[1].lower()
        md=os.path.join(DST,os.path.splitext(rel)[0]+".md"); assets=os.path.join(DST,os.path.splitext(rel)[0]+".assets")
        body="";loss=[];st="failed";err=""
        try:
            if ext in (".doc",".docx"):
                import pythoncom,win32com.client
                if word is None:
                    pythoncom.CoInitialize(); word=win32com.client.DispatchEx("Word.Application"); word.Visible=False; word.DisplayAlerts=0
                doc=word.Documents.Open(os.path.abspath(f),ReadOnly=True,AddToRecentFiles=False,ConfirmConversions=False)
                try:
                    text=clean(str(doc.Range().Text or "")); ntab=int(doc.Tables.Count); cb=cbc=ole=0
                    try:
                        for k in range(1,int(doc.FormFields.Count)+1):
                            try:
                                v=doc.FormFields.Item(k).CheckBox; cb+=1; cbc+=1 if bool(v.Value) else 0
                            except Exception: pass
                    except Exception: pass
                    if cb: loss.append(f"checkbox={cb}(checked={cbc})")
                    body=f"> 表格数:{ntab} 勾选框:{cb}(勾{cbc})\n\n{text}"
                finally: doc.Close(False)
            elif ext==".xls":
                import xlrd; wb=xlrd.open_workbook(f); parts=[]
                for nm in wb.sheet_names():
                    sh=wb.sheet_by_name(nm)
                    if sh.nrows: parts.append(f"### sheet: {nm}\n\n"+md_table([[sh.cell_value(r,c) for c in range(sh.ncols)] for r in range(sh.nrows)]))
                body="\n\n".join(parts)
            elif ext==".xlsx":
                import openpyxl; wb=openpyxl.load_workbook(f,read_only=True,data_only=True); parts=[]
                for nm in wb.sheetnames:
                    rs=[[("" if v is None else v) for v in row] for row in wb[nm].iter_rows(values_only=True)]
                    rs=[r for r in rs if any(str(x).strip() for x in r)]
                    if rs: parts.append(f"### sheet: {nm}\n\n"+md_table(rs))
                wb.close(); body="\n\n".join(parts)
            elif ext==".pdf":
                import fitz; d=fitz.open(f); parts=[]; low=0
                for pi in range(d.page_count):
                    t=d[pi].get_text().strip()
                    if len(t)<40:
                        low+=1; os.makedirs(assets,exist_ok=True); png=os.path.join(assets,f"page_{pi+1:03d}.png")
                        try: d[pi].get_pixmap(dpi=150).save(png); parts.append(f"### page {pi+1}(少字,渲PNG)\n\n![p]({os.path.relpath(png,os.path.dirname(assets))})\n\n```\n{t}\n```")
                        except Exception: parts.append(f"### page {pi+1}\n\n```\n{t}\n```")
                    else: parts.append(f"### page {pi+1}\n\n{clean(t)}")
                if low: loss.append(f"pdf_low_text={low}")
                d.close(); body="\n\n".join(parts)
            st="ok" if body and body.strip() else "empty"
        except Exception as e: err=repr(e)[:200]; loss.append("convert_error")
        if st=="ok":
            os.makedirs(os.path.dirname(md),exist_ok=True); open(md,"w",encoding="utf-8").write(header(rel,f,ext.lstrip("."),st,loss)+body)
        rows.append({"rel":rel,"type":ext.lstrip("."),"status":st,"text_len":len(body),"loss_flags":";".join(loss),"md":md if st=="ok" else "","error":err})
        if i%20==0 or i==len(files): print(f"  {i}/{len(files)} {st} {rel[:55]}",flush=True)
    if word:
        try: word.Quit()
        except Exception: pass
    with open(man,"w",encoding="utf-8-sig",newline="") as fh:
        w=csv.DictWriter(fh,fieldnames=["rel","type","status","text_len","loss_flags","md","error"]); w.writeheader(); w.writerows(rows)
    from collections import Counter
    print("[转换] 完成:",dict(Counter(r["status"] for r in rows)),"| 台账:",man)
    fails=[r for r in rows if r["status"]!="ok"]
    if fails: print("  失败/空:",[r["rel"] for r in fails[:20]])

# -------- ② 覆盖台账 --------
def coverage(cfg):
    from difflib import SequenceMatcher
    import xlrd
    SRC,DST,CHK=cfg["raw"],cfg["md"],cfg["check"]; os.makedirs(CHK,exist_ok=True)
    lst=glob.glob(os.path.join(SRC,"**",cfg["dhf_list_glob"]),recursive=True)
    if not lst: print("[台账] 未找到DHF清单:",cfg["dhf_list_glob"]); return
    DHF=lst[0]
    def nn(t):
        t=(t or "").lower().replace("（","(").replace("）",")"); t=re.sub(r"\s+","",t)
        t=re.sub(r"[._\-–—/\\+]+","",t); t=re.sub(r"v\d+(\.\d+)*","",t); t=re.sub(r"e\d+$","",t)
        return t.replace("封面","").replace("首页","")
    wb=xlrd.open_workbook(DHF); sh=wb.sheet_by_index(0); items=[]; stage=""
    for r in range(2,sh.nrows):
        row=[str(sh.cell_value(r,c)).strip() for c in range(sh.ncols)]+["",""]*4
        if row[0]: stage=row[0]
        seq,name,no,form=row[1],row[2],row[3],row[4]
        if not name: continue
        items.append({"stage":stage,"seq":seq,"name":name,"no":no,"form":form})
    files=[os.path.relpath(p,SRC) for p in glob.glob(os.path.join(SRC,"**","*"),recursive=True)
           if os.path.isfile(p) and not os.path.basename(p).startswith("~$")]
    rows=[]; from collections import Counter
    for it in items:
        nm=nn(it["name"]); best=(0,"")
        for rel in files:
            sc=SequenceMatcher(None,nm,nn(os.path.splitext(os.path.basename(rel))[0])).ratio()
            if nm and nm in nn(rel): sc=max(sc,0.9)
            if sc>best[0]: best=(sc,rel)
        status="ok" if best[0]>=0.55 else ("paper" if "纸" in it["form"] else "review")
        if best[0]<0.45 and "纸" not in it["form"]: status="missing"
        rows.append({**it,"status":status,"match":os.path.basename(best[1]),"score":round(best[0],2)})
    out=os.path.join(CHK,"coverage_ledger.csv")
    with open(out,"w",encoding="utf-8-sig",newline="") as f:
        w=csv.DictWriter(f,fieldnames=["stage","seq","name","no","form","status","match","score"]); w.writeheader(); w.writerows(rows)
    c=Counter(r["status"] for r in rows)
    print(f"[台账] 清单{len(items)}项 | ok{c.get('ok',0)} review{c.get('review',0)} missing{c.get('missing',0)} 纸档{c.get('paper',0)} -> {out}")

def run(cmd):
    print("  $",cmd); subprocess.run(cmd,shell=True)

def residue(cfg):
    out=os.path.join(cfg["check"],"机械校验-残留.csv")
    run(f'python "{os.path.join(HERE,"check_residue.py")}" "{cfg["md"]}" --product {CUR} --foreign {cfg["foreign"]} --models {cfg["models"]} --out "{out}"')

def numeric(cfg):
    if not os.path.exists(cfg["params"]):
        print("[数值] 参数明细不存在(先跑AI审核产出):",cfg["params"]); return
    out=os.path.join(cfg["check"],"数值冲突-确定性.csv")
    run(f'python "{os.path.join(HERE,"check_params_numeric.py")}" "{cfg["params"]}" --product {CUR} --out "{out}"')

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("model"); ap.add_argument("phase",choices=["setup","mechanical","convert","coverage","residue","numeric"])
    a=ap.parse_args(); CUR=a.model
    if a.model not in MODELS: print("未知型号,在MODELS里加一段:",list(MODELS)); sys.exit(1)
    cfg=MODELS[a.model]
    print(f"=== {a.model} ({cfg['market']}/{cfg['category']}) · {a.phase} ===")
    if a.phase in ("setup","convert"): convert(cfg)
    if a.phase in ("setup","coverage"): coverage(cfg)
    if a.phase in ("setup","residue"): residue(cfg)
    if a.phase in ("mechanical","numeric"): numeric(cfg)
    if a.phase=="setup":
        print("\n>>> 前处理完成。下一步用 Claude 跑 AI 语义审核(阶段轴+维度轴 workflow),产出参数明细/错误总表,再 python dhf_pipeline.py %s mechanical"%a.model)
