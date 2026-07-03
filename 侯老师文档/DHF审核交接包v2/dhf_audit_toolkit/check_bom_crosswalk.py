# -*- coding: utf-8 -*-
"""
Tier2 跨异构表对账 · BOM↔清单↔WI crosswalk（确定性核对核心）
================================================================
输入: 一张统一"零件记录表"(各来源已抽成同一schema):
      列 = 来源, 品名, 用量, 规格, 图号, 物料编码
      (BOM/清单 由确定性抽取; WI散文由 LLM 抽取; 都汇到这张表)
做: 品名规范化(同义词+模糊)→按零件聚合每个来源的 用量/规格/图号 →跨来源核对:
    ① 用量冲突(同零件各来源数量不一致, 含WI多工步求和)
    ② 规格/图号冲突(同零件 规格或图号 跨来源不同)
    ③ 仅部分来源出现(漏录候选)
输出 crosswalk矩阵 + 冲突表。列对齐用标准化schema, 故无需嵌入模型。

用法: python check_bom_crosswalk.py 记录表.csv --out 对账.csv
"""
import sys, os, csv, re, argparse
from difflib import SequenceMatcher
from collections import defaultdict
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

# 同义词归并(同一零件不同叫法)
SYN=[
 ("螺钉",["螺钉","螺丝","screw","自攻","机牙"]),
 ("传感器",["传感器","探头","测头","sensor","热电堆","红外传感"]),
 ("上盖",["上盖","前壳","面盖"]),
 ("下盖",["下盖","后壳","底壳"]),
 ("电池盖",["电池盖","电池门"]),
 ("按键",["按键","开机键","测量键"]),
 ("静音按键",["静音按键","静音键","静音"]),
 ("透镜",["透镜","镜片","lens"]),
 ("液晶",["液晶","显示屏","lcd","显示器"]),
 ("PCB",["pcb","主板","线路板","电路板"]),
 ("蜂鸣片",["蜂鸣片","蜂鸣器","buzzer","喇叭"]),
 # 弹簧按极性区分,勿合并(正极/负极/双联是不同件)
 ("正极弹簧",["正极弹簧","正极簧"]),
 ("负极弹簧",["负极弹簧","负极簧"]),
 ("双联弹簧",["双联弹簧","双联簧","联簧"]),
 ("支架",["支架"]),
 ("保护盖",["保护盖","保护膜"]),
 ("金属套",["金属套","铜套"]),
 ("缓冲垫",["缓冲垫","按键缓冲","垫"]),
 ("导光板",["导光板","导光"]),
 ("连接线",["连接线","导线","线材"]),
 ("说明书",["说明书","ifu","手册","operation guide"]),
 ("彩盒",["彩盒","彩包装","包装盒"]),
 ("电池",["电池","battery","aaa"]),
]
CN={"零":0,"一":1,"二":2,"两":2,"三":3,"四":4,"五":5,"六":6,"七":7,"八":8,"九":9,"十":10}
def norm(s): return re.sub(r"\s+","",(s or "").lower())
def canon_part(name):
    n=norm(name)
    for c,kws in SYN:
        if any(k in n for k in kws): return c
    return None  # 留给模糊归并
def parse_qty(s):
    s=s or ""
    m=re.search(r"(\d+(?:\.\d+)?)",s)
    if m: return float(m.group(1))
    for ch,v in CN.items():
        if ch+"颗" in s or ch+"个" in s or ch+"件" in s or ch+"根" in s or ch+"pcs" in s.lower(): return float(v)
    return None
def norm_spec(s):
    s=norm(s); s=s.replace("×","x").replace("*","x").replace("（","(").replace("）",")")
    s=re.sub(r"[mM]{2}$","",s); return s

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv"); ap.add_argument("--out",default="BOM对账.csv")
    a=ap.parse_args()
    rows=list(csv.DictReader(open(a.csv,encoding="utf-8-sig")))
    # 规范零件名(同义词→canonical; 未命中者按模糊归并到已有canonical)
    canons={}  # canonical -> set of raw names
    def assign(name):
        c=canon_part(name)
        if c: canons.setdefault(c,set()).add(name); return c
        nn=norm(name)
        for c in list(canons):
            if SequenceMatcher(None,nn,norm(c)).ratio()>=0.8 or nn in norm(c) or norm(c) in nn:
                canons[c].add(name); return c
        canons.setdefault(name.strip(),set()).add(name); return name.strip()
    # 聚合: (canon, 来源) -> {qty_sum, specs, drawings, codes, n}
    agg=defaultdict(lambda:{"qty":0.0,"qn":0,"spec":set(),"draw":set(),"code":set(),"raw":set()})
    sources=[]
    for r in rows:
        src=r.get("来源","").strip(); nm=r.get("品名","").strip()
        if not nm: continue
        if src not in sources: sources.append(src)
        cp=assign(nm)
        a0=agg[(cp,src)]
        q=parse_qty(r.get("用量",""))
        if q is not None: a0["qty"]+=q; a0["qn"]+=1
        for k,fld in [("规格","spec"),("图号","draw"),("物料编码","code")]:
            v=(r.get(k,"") or "").strip()
            if v and v.lower() not in("n/a","na","-","none"): a0[fld].add(v)
        a0["raw"].add(nm)
    parts=sorted({cp for (cp,s) in agg})
    # 冲突检测
    conflicts=[]; infos=[]
    for cp in parts:
        present=[s for s in sources if (cp,s) in agg]
        # 用量冲突
        qmap={s:round(agg[(cp,s)]["qty"],2) for s in present if agg[(cp,s)]["qn"]>0}
        if len(set(qmap.values()))>=2:
            conflicts.append({"零件":cp,"类型":"用量冲突","详情":" vs ".join(f"{s}={v}" for s,v in qmap.items())})
        # 图号冲突(归一后)
        for fld,lab in [("draw","图号"),("spec","规格")]:
            vals={}
            for s in present:
                vs={norm_spec(x) for x in agg[(cp,s)][fld]}
                if vs: vals[s]=vs
            allv=set().union(*vals.values()) if vals else set()
            if len(vals)>=2 and len(allv)>=2:
                # 仅当来源间无交集(真不一致)才报
                inter=set.intersection(*vals.values()) if len(vals)>=2 else set()
                if not inter:
                    conflicts.append({"零件":cp,"类型":lab+"冲突",
                        "详情":" vs ".join(f"{s}={'|'.join(sorted(agg[(cp,s)][fld]))[:40]}" for s in vals)})
        # 漏录(出现在部分来源)= 信息项,非冲突(异构表范围天然不同,如总装ABOM不含机芯件/WI不列全部件)
        if 1<=len(present)<len(sources):
            miss=[s for s in sources if s not in present]
            infos.append({"零件":cp,"类型":"仅部分来源(范围差异,人工看)","详情":f"有:{'/'.join(present)} 缺:{'/'.join(miss)}"})
    # 输出 crosswalk
    cw=a.out.replace(".csv","-crosswalk.csv")
    with open(cw,"w",encoding="utf-8-sig",newline="") as f:
        w=csv.writer(f); w.writerow(["零件"]+[f"{s}:用量" for s in sources]+[f"{s}:图号/规格" for s in sources])
        for cp in parts:
            row=[cp]
            for s in sources:
                a0=agg.get((cp,s)); row.append("" if not a0 else (round(a0["qty"],2) if a0["qn"] else ""))
            for s in sources:
                a0=agg.get((cp,s)); row.append("" if not a0 else " | ".join(sorted(a0["draw"]|a0["spec"]))[:50])
            w.writerow(row)
    with open(a.out,"w",encoding="utf-8-sig",newline="") as f:
        w=csv.writer(f); w.writerow(["序号","零件","冲突类型","详情"])
        for i,c in enumerate(conflicts,1): w.writerow([i,c["零件"],c["类型"],c["详情"]])
    info_out=a.out.replace(".csv","-info范围差异.csv")
    with open(info_out,"w",encoding="utf-8-sig",newline="") as f:
        w=csv.writer(f); w.writerow(["序号","零件","类型","详情"])
        for i,c in enumerate(infos,1): w.writerow([i,c["零件"],c["类型"],c["详情"]])
    print(f"来源: {sources}")
    print(f"零件(规范化后): {len(parts)} | 记录 {len(rows)}")
    print(f"★真冲突(用量/规格/图号): {len(conflicts)} 条 -> {a.out}")
    print(f" 信息项(范围差异,人工看): {len(infos)} 条 -> {info_out}")
    print(f" crosswalk矩阵 -> {cw}")
    for c in conflicts:
        print(f"  ▲ [{c['类型']}] {c['零件']}: {c['详情'][:90]}")

if __name__=="__main__":
    main()
