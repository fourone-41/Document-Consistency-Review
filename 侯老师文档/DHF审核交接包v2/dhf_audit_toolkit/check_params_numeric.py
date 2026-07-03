# -*- coding: utf-8 -*-
"""
Tier1 形式化算法 · 数值一致性检查器（确定性，无需 AI，近零误报）
================================================================
读"参数实例长表"(阶段,参数名,值,出处文件) → 对每个值做:
  单位归一(℃/℉、A/mA/µA、mm/cm/in、s/分/时、g/kg、mAh) → 解析成 区间/边界/容差/点/尺寸三元组
  → 按"规范参数名 + 限定词(温度段/模式)"分组 → 组内出现 ≥2 个**归一后仍不同**的取值 = 冲突
关键:34-43 vs 34~43 归一后都是 [34,43] → 同签名 → **不报**(剔写法误报);
      32~42.9 vs 34-43 → 不同 → 报,并给出每个取值+出处文件(可签字定位)。
只对能干净解析的高价值数值参数报;解析不了的跳过(保近零误报)。

用法: python check_params_numeric.py 参数明细.csv --product PT9S --out 冲突.csv
"""
import sys, os, csv, re, argparse
from collections import defaultdict
try: sys.stdout.reconfigure(encoding="utf-8")
except Exception: pass

# ---- 规范参数名(同义词→canonical) ----
CANON=[
 ("工作电流",["工作电流","动态电流","运行电流","工作功耗","动态功耗"]),
 ("静态电流",["静态电流","关机电流","休眠电流","待机电流","静态功耗"]),
 ("显示量程",["显示范围","温度显示范围","测温范围","量程","显示量程"]),
 # 注:测量精度/分辨率(带温度段+重复性歧义)确定性不可靠,移交LLM语义层,此处不做确定性比对
 ("工作温度",["工作环境温度","工作温度","使用环境温度"]),
 ("存储温度",["贮存环境温度","存储环境温度","存储温度","贮存温度"]),
 ("标定温度",["标定环境","标定温度","校准温度","常温标定","标定环境温度"]),
 ("自动关机时间",["自动关机时间","自动关机","关机时间","待机时间"]),
 ("低压阈值",["低电压","低电压阈值","低电压检出","低电符号","关机阈值","低电"]),
 ("电池容量",["电池容量","电池规格","mah"]),
 ("防护等级",["防护等级","防尘防水","防水等级","ip等级","防护"]),
 ("整机重量",["整机重量","重量","净重","产品重量"]),
 ("整机尺寸",["整机尺寸","外形尺寸","产品尺寸","整机外形"]),
 ("装箱数",["装箱数","装箱数量","每箱","装箱配比","外箱配比"]),
]
def canon(name):
    n=(name or "").lower().replace(" ","")
    for c,kws in CANON:
        if any(k.lower() in n for k in kws):
            # 负向护栏:整机重量/尺寸 不能匹配 箱/包装/运输/托盘 类
            if c in("整机重量","整机尺寸") and any(x in n for x in ["箱","包装","运输","托盘","整箱","外箱","内箱"]):
                return None
            return c
    return None

# ---- 单位归一 ----
def to_celsius(v,u):
    if "℉" in u or "f" == u.lower(): return round((v-32)*5/9,3)
    return v
def cur_mA(v,u):
    u=u.lower()
    if "ua" in u or "µa" in u: return round(v/1000,6)
    if u.strip()=="a": return round(v*1000,3)
    return v  # mA
def len_mm(v,u):
    u=u.lower()
    if u in("cm",): return v*10
    if u in("in","inch",'"',"英寸"): return round(v*25.4,2)
    return v
def time_s(v,u):
    if "分" in u or "min" in u: return v*60
    if "时" in u or u.lower()=="h": return v*3600
    return v  # s/秒
def wt_g(v,u):
    if u.lower()=="kg" or "千克" in u or "公斤" in u: return v*1000
    return v

NUM=r"[-+]?\d+(?:\.\d+)?"
def grab(s):  # 返回 [(num,unit_token)]
    out=[]
    for m in re.finditer(rf"({NUM})\s*(℃|℉|°c|°f|mah|mAh|uA|µA|mA|kg|mm|cm|颗|台|秒|分钟|小时|min|年|次|%|in|inch|A|g|S|s|h)?",s,re.I):
        try: out.append((float(m.group(1)), (m.group(2) or "").strip()))
        except: pass
    return out

def signature(cp, val):
    """把一个值串归一成可比签名;不可比→None(跳过,保近零误报)"""
    s=(val or "").strip()
    if not s: return None
    low=s.lower()
    # 防护等级:取 IPxx token
    if cp=="防护等级":
        m=re.search(r"ip\s*([0-9x]{2})",low)
        return ("IP",m.group(1)) if m else None
    nums=grab(s)
    if not nums: return None
    # 选择该参数的归一函数
    def conv(v,u):
        if cp in("工作温度","存储温度","标定温度","显示量程","测量精度","分辨率"): return to_celsius(v,u)
        if cp in("工作电流","静态电流","低压阈值"):
            if cp=="低压阈值": return v  # 低压是电压V,不换算
            return cur_mA(v,u)
        if cp=="电池容量": return v
        if cp=="整机重量": return wt_g(v,u)
        if cp=="整机尺寸": return len_mm(v,u)
        if cp=="自动关机时间": return time_s(v,u)
        return v
    # 尺寸:取数值三元组(排序)
    if cp=="整机尺寸":
        vals=sorted(round(conv(v,u),1) for v,u in nums if abs(v)>3)[:3]
        return ("DIM",tuple(vals)) if len(vals)>=3 else None
    # 最大X…最小Y (温度/量程) -> 区间,治"最大42.9最小32"vs"32~42.9"写法误报
    if cp in("显示量程","工作温度","存储温度"):
        mx=re.search(rf"(?:最大|最高|max|上限)\D{{0,4}}({NUM})",s,re.I)
        mn=re.search(rf"(?:最小|最低|min|下限)\D{{0,4}}({NUM})",s,re.I)
        if mx and mn:
            f=("℉" in s)
            a=to_celsius(float(mx.group(1)),"℉" if f else ""); b=to_celsius(float(mn.group(1)),"℉" if f else "")
            lo,hi=sorted([round(a,3),round(b,3)]); return ("RNG",lo,hi)
    # 容差 a±b
    m=re.search(rf"({NUM})\s*(℃|℉|mm|mA|s|秒|g|v|V)?\s*[±+]\s*-?\s*({NUM})",s)
    if m and cp not in("显示量程",):
        c=conv(float(m.group(1)),m.group(2) or ""); t=float(m.group(3))
        return ("TOL",round(c,3),round(t,3))
    # 边界 ≤/≥/</>
    mb=re.search(rf"(≤|<=|<|不超过|不大于|≥|>=|>|不低于|不少于|不小于)\s*({NUM})\s*(℃|℉|mah|mAh|uA|µA|mA|A|g|kg|mm|s|秒|v|V|台|颗|%)?",s,re.I)
    if mb:
        op="le" if mb.group(1)[0] in "≤<不" and ("不低" not in mb.group(1) and "不少" not in mb.group(1) and "不小" not in mb.group(1)) else "ge"
        return ("BND",op,round(conv(float(mb.group(2)),mb.group(3) or ""),4))
    # 区间 a~b / a-b (容许单位夹在中间: 32.0℃～42.9℃)
    mr=re.search(rf"({NUM})\s*(℃|℉|mA|mm|kpa|%)?\s*(?:~|～|-|—|–|至|到)\s*({NUM})\s*(℃|℉|mA|mm|kpa|%)?",s,re.I)
    if mr:
        u=mr.group(4) or mr.group(2) or ""; a=conv(float(mr.group(1)),u); b=conv(float(mr.group(3)),u)
        lo,hi=sorted([round(a,3),round(b,3)]); return ("RNG",lo,hi)
    # 单点(取第一个带相关单位或最显著的数)
    v,u=nums[0]
    return ("PT",round(conv(v,u),4))

def qualifier(val):
    m=re.search(r"[（(]([^)）]{1,16})[)）]",val or "")
    q=m.group(1) if m else ""
    for k in ["静态","动态","关机","休眠","低电","模式","物温","体温"]:
        if k in (val or "") and k not in q: q=(q+" "+k).strip()
    return q[:16]

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("csv"); ap.add_argument("--product",default=""); ap.add_argument("--out",default="数值冲突.csv")
    a=ap.parse_args()
    rows=list(csv.DictReader(open(a.csv,encoding="utf-8-sig")))
    # 列名兼容
    def col(r,*names):
        for n in names:
            if n in r: return r[n]
        return ""
    groups=defaultdict(list)  # (canon, qualifier) -> [(sig, rawval, file, stage)]
    parsed=0
    for r in rows:
        name=col(r,"参数名","名称","条目"); val=col(r,"值","取值","参数值","数值/要求","数值"); fil=col(r,"出处文件","来源文件","文件","来源位置","文档"); stg=col(r,"阶段","来源阶段","阶段角色")
        cp=canon(name)
        if not cp: continue
        # 过滤实测数据/装箱清单(不是spec参数,避免误报)
        if any(x in (val or "") for x in ["实测","水槽","号机","次测","逐次","measured"]): continue
        if cp=="电池容量" and any(x in (val or "") for x in ["说明书","保修卡","装箱","快纸","快速指南","一台","整机"]): continue
        sig=signature(cp,val)
        if sig is None: continue
        parsed+=1
        groups[(cp,qualifier(val))].append((sig,val.strip(),fil,stg,name))
    # 找冲突:区间+点合并(点落在某区间/容差内=一致不报;边界/区间/容差不同=报)
    INF=1e18; EPS=1e-6
    def to_iv(sig):
        k=sig[0]
        if k=="PT": return (sig[1],sig[1],"pt")
        if k=="TOL": return (sig[1]-sig[2],sig[1]+sig[2],"tol")
        if k=="RNG": return (sig[1],sig[2],"rng")
        if k=="BND": return (-INF,sig[2],"le") if sig[1]=="le" else (sig[2],INF,"ge")
        return None
    conflicts=[]
    for (cp,q),items in groups.items():
        specials={}; ivs=[]
        for sig,val,fil,stg,nm in items:
            if sig[0] in ("IP","DIM"): specials.setdefault(sig,(val,fil,stg))
            else:
                iv=to_iv(sig)
                if iv: ivs.append((iv[0],iv[1],iv[2],val,fil,stg))
        variants=[]
        if len(specials)>=2:
            variants=[{"val":v,"file":f,"stage":s} for _,(v,f,s) in specials.items()]
        else:
            nonpt=[v for v in ivs if v[2]!="pt"]
            reps={}
            for lo,hi,kind,val,fil,stg in ivs:
                if kind=="pt" and any(nlo-EPS<=lo<=nhi+EPS for nlo,nhi,nk,_,_,_ in nonpt):
                    continue  # 点落在某区间/容差内 -> 一致,不计
                reps.setdefault((round(lo,3),round(hi,3)),{"val":val,"file":fil,"stage":stg})
            if len(reps)>=2: variants=list(reps.values())
        if len(variants)>=2:
            conflicts.append({"参数":cp,"限定":q,"取值数":len(variants),"variants":variants})
    # 输出
    with open(a.out,"w",encoding="utf-8-sig",newline="") as f:
        w=csv.writer(f); w.writerow(["序号","规范参数","限定词","冲突取值数","取值A","出处A","取值B","出处B","其它取值"])
        for i,c in enumerate(sorted(conflicts,key=lambda x:-x["取值数"]),1):
            vs=c["variants"]
            a0=vs[0]; b0=vs[1] if len(vs)>1 else {"val":"","file":""}
            other=" || ".join(f'{v["val"]}@{os.path.basename(v["file"])}' for v in vs[2:])
            w.writerow([i,c["参数"],c["限定"],c["取值数"],a0["val"],a0["file"],b0["val"],b0["file"],other])
    print(f"[{a.product}] 长表 {len(rows)} 行,可解析数值参数实例 {parsed} 个,规范参数组 {len(groups)} 个")
    print(f"  确定性数值冲突: {len(conflicts)} 组 -> {a.out}")
    for c in sorted(conflicts,key=lambda x:-x["取值数"]):
        vs=c["variants"]
        print(f"  ▲ {c['参数']}{('['+c['限定']+']') if c['限定'] else ''}: " + " | ".join(f"{v['val']}" for v in vs))

if __name__=="__main__":
    main()
