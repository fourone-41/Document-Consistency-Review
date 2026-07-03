# -*- coding: utf-8 -*-
"""交互裁决版HTML:每条问题留 接受/不接受/待定 单选 + 原因框,浏览器localStorage本地存档,
顶部进度条+筛选+一键导出CSV。出处文件=可点开的本地链接;File0N自动翻译成真实文件名;每阶段File编号对照。
用法: python gen_report_review_html.py [PT7|PT9S|PT9L|all]
"""
import sys, os, csv, re, html, json, glob, urllib.parse, datetime as dt
from collections import defaultdict, Counter
sys.stdout.reconfigure(encoding="utf-8")

MAP_PT7={"id_":"原ID","stage":"阶段","sev":"严重度","axis":"轴","type":"类型","desc":"描述","ev":"证据","sug":"建议","link":"关联前序","linklabel":"关联前序"}
MAP_9 ={"id_":"原ID","stage":"阶段","sev":"严重度","axis":"轴","type":"类型","desc":"错误描述","ev":"证据位置","sug":"建议动作","link":"来源","linklabel":"来源/维度"}
MODELS={
 "PT7":{"csv":r"D:\AI_0415\03DHF\new_pt7_CHECK\PT7-错误总表.csv","map":MAP_PT7,"md":r"D:\AI_0415\03DHF\new_pt7_MD",
        "title":"PT7 红外额温计 · DHF 检测报告（工程师裁决版）","sub":"美版(仅美国) · 项目号 30000059 · 增量审核 01→20",
        "out":r"D:\AI_0415\03DHF\new_pt7_CHECK\PT7-DHF检测报告-裁决版.html","role":"责任工程师"},
 "PT9S":{"csv":r"D:\AI_0415\03DHF\PT9S_CHECK\PT9S-全链审核-错误总表-含维度轴.csv","map":MAP_9,"md":r"D:\AI_0415\03DHF\PT9S_MD",
        "title":"PT9S 红外体温计 · DHF 检测报告（工程师裁决版）","sub":"美版(仅美国) · 项目号 30000094 · 双轴(阶段+维度)",
        "out":r"D:\AI_0415\03DHF\PT9S_CHECK\PT9S-DHF检测报告-裁决版.html","role":"责任工程师"},
 "PT9L":{"csv":r"D:\AI_0415\03DHF\PT9L_CHECK\PT9L-错误总表.csv","map":MAP_PT7,"md":r"D:\AI_0415\03DHF\PT9L_MD",
        "title":"PT9L 红外额温计 · DHF 检测报告（工程师裁决版·全量复审）","sub":"美版(仅美国) · 项目号 30000078 · 增量复审(逐字原文证据)",
        "out":r"D:\AI_0415\03DHF\PT9L_CHECK\PT9L-DHF检测报告-裁决版.html","role":"责任工程师"},
 "M10":{"csv":r"D:\AI_0415\03DHF\m10_CHECK\M10-错误总表.csv","map":MAP_PT7,"md":r"D:\AI_0415\03DHF\m10_MD",
        "title":"M10 网式雾化器 · DHF/DMR/注册 检测报告（工程师裁决版）","sub":"仅中国 NMPA · 项目号 30000003 · 并行审24单元+5轴对账(雾化器,逐字原文证据)",
        "out":r"D:\AI_0415\03DHF\m10_CHECK\M10-检测报告-裁决版.html","role":"责任工程师"},
}

SEV={"critical":0,"major":1,"minor":2,"待PM确认":3,"NEI":4}
SEVCN={"critical":"严重","major":"重要","minor":"一般","待PM确认":"待PM定","NEI":"无正文"}
def sev_norm(s): return (s or "").strip()
def esc(t): return html.escape(t or "")
def snum(st):
    m=re.match(r"\s*(\d+)",st or ""); return int(m.group(1)) if m else -1
def stage_key(st): return (snum(st) if snum(st)>0 else 98, st or "")
def stage_short(st): return re.sub(r"\s*\(.*$","",st or "").strip()

# ---------- 文件解析/链接 ----------
def to_href(p): return "file:///"+urllib.parse.quote(p.replace("\\","/"), safe="/:")
def build_index(mdroot):
    files=[fp for fp in glob.glob(os.path.join(mdroot,"**","*.md"),recursive=True) if ".assets" not in fp.replace("\\","/").lower()]
    return files
def find_stage_folder(mdroot, stage):
    num=snum(stage)
    if num<0: return None
    for root,dirs,_ in os.walk(mdroot):
        for d in dirs:
            if d.endswith(".assets"): continue
            mm=re.match(r"\s*(\d+)",d)
            if mm and int(mm.group(1))==num: return os.path.join(root,d)
    return None
def list_stage_md(folder):
    if not folder or not os.path.isdir(folder): return []
    fs=[os.path.join(folder,f) for f in os.listdir(folder) if f.lower().endswith(".md")]
    return sorted(fs)
def short_name(fp):
    b=os.path.splitext(os.path.basename(fp))[0]
    b=re.sub(r"^PT\w*-{1,2}","",b); b=re.sub(r"^Attachment\s*\d+\s*","",b)
    return b[:34]
def resolve_token(tok, stage_fp, all_fp):
    t=(tok or "").strip(); ts=os.path.splitext(t)[0].lower()
    if len(ts)<3: return None
    cands=stage_fp+all_fp
    for fp in cands:
        bn=os.path.basename(fp)
        if t.lower()==bn.lower() or ts==os.path.splitext(bn)[0].lower(): return fp
    m=re.search(r"PT\w*-[A-Z]{2,6}\d{0,2}", t)
    if m:
        for fp in cands:
            if m.group(0).lower() in os.path.basename(fp).lower(): return fp
    for fp in stage_fp:
        if ts in os.path.basename(fp).lower(): return fp
    return None

FILE_RE=re.compile(r"File\s?0?\d+|[\w一-鿿\-＋\+．\.]+?\.(?:md|xls|xlsx|docx?|pdf|mpp|hex|MTP|BIN)|PT\w*-[A-Z]{2,6}\d{0,2}")
def extract_tokens(ev):
    out=[]
    for m in FILE_RE.findall(ev or ""):
        m=m.strip()
        if re.match(r"^(no|No|grep|matches)",m): continue
        if m and m not in out: out.append(m)
    return out[:6]

DOCNAMES=["客户需求评审单","客户需求书","立项批准书","设计开发计划评审表","设计开发计划","项目组成员名单","风险管理计划","风险评价报告","风险控制措施","风险管理报告",
 "设计输入","通用要求","功能规格","性能规格","组件规格","法规标准清单","结构设计方案","硬件设计方案","原理图","软件流程图","结构图样","硬件图样","软件图样",
 "检验标准","设计验证报告","检测报告","设计输出清单","转移文件清单","EBOM","ABOM","试产总结","标签审核表","设计确认","上市批准","设计更改通知单"]

CSS="""
*{box-sizing:border-box}body{font-family:-apple-system,'Segoe UI','Microsoft YaHei',sans-serif;margin:0;background:#f4f5f7;color:#1d2530;line-height:1.6}
.wrap{max-width:1040px;margin:0 auto;padding:20px 18px 90px}
h1{font-size:23px;margin:0 0 4px}.sub{color:#5b6675;font-size:13.5px;margin-bottom:14px}
.bar-wrap{position:sticky;top:0;z-index:50;background:#fffffff2;backdrop-filter:blur(6px);border:1px solid #e3e6ea;border-radius:12px;padding:11px 15px;margin-bottom:16px;box-shadow:0 2px 8px rgba(0,0,0,.06)}
.prog{height:9px;background:#eef0f3;border-radius:6px;overflow:hidden;margin:7px 0}
#bar{height:100%;width:0;background:linear-gradient(90deg,#27ae60,#2ecc71);transition:width .25s}
#cnt{font-size:13.5px}
.tools{display:flex;gap:7px;flex-wrap:wrap;margin-top:9px;align-items:center}
.fbtn{font-size:12.5px;padding:4px 11px;border:1px solid #cfd6df;background:#fff;border-radius:20px;cursor:pointer;color:#3a4654}
.fbtn.on{background:#1d2530;color:#fff;border-color:#1d2530}
.act{margin-left:auto;display:flex;gap:7px}
.btn{font-size:13px;padding:5px 14px;border:none;border-radius:8px;cursor:pointer;font-weight:600}
.btn-exp{background:#1f6feb;color:#fff}.btn-imp{background:#eef2f7;color:#3a4654}
.note{background:#fff8e6;border:1px solid #f3d27a;border-radius:10px;padding:11px 14px;font-size:13px;margin-bottom:16px}
.badge{display:inline-block;padding:2px 9px;border-radius:20px;font-size:12px;font-weight:700;color:#fff;white-space:nowrap}
.b-critical{background:#c0392b}.b-major{background:#e67e22}.b-minor{background:#b7950b}.b-待PM确认{background:#2471a3}.b-NEI{background:#7f8c8d}
.axis{display:inline-block;padding:1px 8px;border-radius:6px;font-size:11.5px;font-weight:700}
.ax-内部{background:#eaf3ff;color:#1f6feb;border:1px solid #cfe2ff}.ax-关联{background:#fdeef0;color:#c0392b;border:1px solid #f5c6cd}
.stage{margin:24px 0 8px;padding:9px 14px;background:#1d2530;color:#fff;border-radius:9px;font-size:17px;font-weight:700;display:flex;justify-content:space-between}
.stage .cnt{font-size:12.5px;font-weight:500;opacity:.85}
.fmap{background:#eef4ff;border:1px solid #cfe0ff;border-left:4px solid #2471a3;border-radius:0 8px 8px 0;padding:8px 13px;margin:0 0 8px;font-size:12.5px;color:#2a3b52}
.fmap a{color:#1f6feb;text-decoration:none}
.card{background:#fff;border-radius:10px;padding:13px 15px;margin:9px 0;box-shadow:0 1px 3px rgba(0,0,0,.06);border-left:5px solid #ccc}
.card.critical{border-left-color:#c0392b}.card.major{border-left-color:#e67e22}.card.minor{border-left-color:#b7950b}.card.待PM确认{border-left-color:#2471a3}.card.NEI{border-left-color:#7f8c8d}
.card[data-d="接受"]{background:#f1fbf4}.card[data-d="不接受"]{background:#fdf2f3}.card[data-d="待定"]{background:#fffdf0}
.chead{display:flex;align-items:center;gap:8px;flex-wrap:wrap;margin-bottom:6px}
.num{font-weight:800;font-size:15px}.type{font-size:12.5px;color:#5b6675;font-weight:600}
.idtag{font-size:11px;color:#9aa5b1;font-family:monospace}.role{margin-left:auto;font-size:11.5px;background:#eef2f7;border-radius:20px;padding:2px 10px;color:#3a4654}
.vs{font-size:11.5px;background:#fdeef0;color:#c0392b;border:1px solid #f5c6cd;border-radius:6px;padding:1px 8px;font-weight:700}
.filerow{font-size:12.5px;margin:3px 0}
.filechip{display:inline-block;background:#eaf3ff;color:#1f6feb;border:1px solid #cfe2ff;border-radius:6px;padding:1px 7px;font-size:11.5px;margin:1px 2px;text-decoration:none}
a.filechip:hover{background:#1f6feb;color:#fff}
.filechip.dim{background:#f3f4f6;color:#6b7280;border-color:#e3e6ea}
.field{margin:6px 0;font-size:13.5px}.field .k{font-weight:700;color:#3a4654;margin-right:6px}
.ev{background:#f7f8fa;border:1px solid #eceef1;border-radius:7px;padding:7px 10px;font-size:12.5px;color:#33404f;white-space:pre-wrap}
.fix{background:#eefaf0;border:1px solid #c8ebd0;border-radius:7px;padding:7px 10px;font-size:13px;color:#1e6b3a}
.review{margin-top:9px;padding-top:9px;border-top:1px dashed #e3e6ea;display:flex;gap:14px;flex-wrap:wrap;align-items:center}
.review label{font-size:13.5px;cursor:pointer;font-weight:600;display:inline-flex;align-items:center;gap:4px}
.review .reason{flex:1;min-width:200px;font-size:13px;padding:5px 9px;border:1px solid #cfd6df;border-radius:7px}
@media print{.bar-wrap{position:static}.review{display:none}}
"""

JS = r"""
const KEY='dhf_review::'+MODEL;
let store=JSON.parse(localStorage.getItem(KEY)||'{}');
let filter='全部';
function save(){localStorage.setItem(KEY,JSON.stringify(store));}
function updateBar(){
  let a=0,r=0,p=0;
  Object.values(store).forEach(v=>{if(v.c==='接受')a++;else if(v.c==='不接受')r++;else if(v.c==='待定')p++;});
  const dec=a+r+p, und=TOTAL-dec;
  document.getElementById('cnt').innerHTML='已裁决 <b>'+dec+'/'+TOTAL+'</b> &nbsp;·&nbsp; ✅接受 '+a+' &nbsp; ❌不接受 '+r+' &nbsp; 🕐待定 '+p+' &nbsp; ⬜未定 <b>'+und+'</b>';
  document.getElementById('bar').style.width=(TOTAL?dec/TOTAL*100:0)+'%';
}
function applyFilter(){
  document.querySelectorAll('.card').forEach(c=>{
    const d=c.dataset.d||''; let show=true;
    if(filter==='未定') show=(d==='');
    else if(filter!=='全部') show=(d===filter);
    c.style.display=show?'':'none';
  });
  document.querySelectorAll('.stage').forEach(s=>{
    let n=s.nextElementSibling, vis=false;
    while(n && !n.classList.contains('stage')){ if(n.classList.contains('card')&&n.style.display!=='none')vis=true; n=n.nextElementSibling;}
    s.style.display=vis?'':'none';
    if(s.nextElementSibling&&s.nextElementSibling.classList.contains('fmap'))s.nextElementSibling.style.display=vis?'':'none';
  });
}
function setFilter(f){filter=f;document.querySelectorAll('.fbtn').forEach(b=>b.classList.toggle('on',b.dataset.f===f));applyFilter();}
function applyAll(){
  document.querySelectorAll('.card').forEach(c=>{
    const id=c.dataset.id, d=store[id]||{};
    c.dataset.d=d.c||'';
    const r=c.querySelector('.reason'); if(r) r.value=d.r||'';
    c.querySelectorAll('input[type=radio]').forEach(rb=>rb.checked=(rb.value===d.c));
  });
  updateBar(); applyFilter();
}
document.addEventListener('change',e=>{
  if(e.target.matches('.review input[type=radio]')){
    const c=e.target.closest('.card'), id=c.dataset.id;
    store[id]=store[id]||{}; store[id].c=e.target.value; c.dataset.d=e.target.value; save(); updateBar(); applyFilter();
  }
});
document.addEventListener('input',e=>{
  if(e.target.matches('.reason')){const id=e.target.closest('.card').dataset.id; store[id]=store[id]||{}; store[id].r=e.target.value; save();}
});
function exportCSV(){
  let L=['型号,序号,阶段,原ID,严重度,类型,问题摘要,裁决,原因'];
  FINDINGS.forEach(f=>{const d=store[f.id]||{};
    L.push([MODEL,f.id,f.stage,f.oid,f.sev,f.type,f.desc,d.c||'',d.r||''].map(x=>'"'+String(x).replace(/"/g,'""')+'"').join(','));});
  const blob=new Blob(['﻿'+L.join('\n')],{type:'text/csv;charset=utf-8'});
  const a=document.createElement('a');a.href=URL.createObjectURL(blob);
  a.download=MODEL+'-裁决-'+new Date().toISOString().slice(0,10)+'.csv';a.click();
}
function importCSV(ev){
  const f=ev.target.files[0]; if(!f)return; const rd=new FileReader();
  rd.onload=()=>{ const txt=rd.result.replace(/^﻿/,''); const lines=txt.split(/\r?\n/).slice(1); let n=0;
    lines.forEach(ln=>{ if(!ln.trim())return;
      const m=ln.match(/("([^"]|"")*"|[^,]*)(,|$)/g); if(!m)return;
      const cells=m.map(x=>x.replace(/,$/,'').replace(/^"|"$/g,'').replace(/""/g,'"'));
      const id=cells[1], c=cells[7]||'', r=cells[8]||'';
      if(id&&(c||r)){store[id]={c:c,r:r};n++;}
    });
    save(); applyAll(); alert('已导入 '+n+' 条裁决');
  };
  rd.readAsText(f,'utf-8');
}
applyAll();
"""

def gen(model):
    cfg=MODELS[model]; m=cfg["map"]
    rows=list(csv.DictReader(open(cfg["csv"],encoding="utf-8-sig")))
    seen=set(); uniq=[]
    for r in rows:
        oid=r.get(m["id_"],"") or (r.get("序号","")+r.get(m["desc"],"")[:20])
        if oid in seen: continue
        seen.add(oid); uniq.append(r)
    rows=uniq
    all_fp=build_index(cfg["md"])
    groups=defaultdict(list)
    for r in rows: groups[stage_short(r[m["stage"]])].append(r)
    order=sorted(groups,key=stage_key)
    sev_all=Counter(sev_norm(r[m["sev"]]) for r in rows)
    findings=[]
    parts=[f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>{esc(model)} DHF 裁决版</title><style>{CSS}</style></head>
<body><div class="wrap"><h1>{esc(cfg['title'])}</h1><div class="sub">{esc(cfg['sub'])} · 共 {len(rows)} 条 · 生成 {dt.datetime.now().replace(microsecond=0)}</div>
<div class="bar-wrap"><div id="cnt"></div><div class="prog"><div id="bar"></div></div>
<div class="tools">
<span class="fbtn on" data-f="全部" onclick="setFilter('全部')">全部</span>
<span class="fbtn" data-f="未定" onclick="setFilter('未定')">⬜未定</span>
<span class="fbtn" data-f="接受" onclick="setFilter('接受')">✅接受</span>
<span class="fbtn" data-f="不接受" onclick="setFilter('不接受')">❌不接受</span>
<span class="fbtn" data-f="待定" onclick="setFilter('待定')">🕐待定</span>
<span class="act"><button class="btn btn-exp" onclick="exportCSV()">⬇ 导出裁决CSV</button>
<label class="btn btn-imp">⬆ 导入<input type="file" accept=".csv" style="display:none" onchange="importCSV(event)"></label></span>
</div></div>
<div class="note"><b>怎么用：</b>逐条点 <b>✅接受 / ❌不接受 / 🕐待定</b>，需要就写原因。选择<b>自动存在本浏览器</b>（关了再开还在）。全部过完点 <b>⬇导出裁决CSV</b> 发我复核；换电脑/分人填可 <b>⬆导入</b> 续上。
<br>📄 <b>出处文件可直接点开</b>（蓝色链接，点了在浏览器打开对应转换件）；<b>File01/02…</b> 已翻译成真实文件名，每阶段开头有对照。
<br>严重度：<span class="badge b-critical">严重</span><span class="badge b-major">重要</span><span class="badge b-minor">一般</span><span class="badge b-待PM确认">待PM定</span><span class="badge b-NEI">无正文</span></div>
"""]
    for i,g in enumerate(order):
        items=sorted(groups[g],key=lambda r:(SEV.get(sev_norm(r[m["sev"]]),9),r.get(m["id_"],"")))
        sc=Counter(sev_norm(r[m["sev"]]) for r in items)
        cnttxt=" · ".join(f"{SEVCN[k]}{sc[k]}" for k in SEV if sc.get(k))
        # 本阶段文件 + File0N映射
        folder=find_stage_folder(cfg["md"], g); stage_fp=list_stage_md(folder)
        file0n={f"File0{j+1}":fp for j,fp in enumerate(stage_fp)} if stage_fp else {}
        uses_f0n=any(re.search(r"File\s?0?\d",(r.get(m["ev"],"")+r.get(m["desc"],""))) for r in items)
        parts.append(f'<div class="stage" id="s{i}"><span>{esc(g)}</span><span class="cnt">{len(items)} 条 {cnttxt}</span></div>')
        if uses_f0n and file0n:
            leg=" · ".join(f'<b>File0{j+1}</b>=<a href="{to_href(fp)}" target="_blank" title="{esc(fp)}">{esc(short_name(fp))}</a>' for j,fp in enumerate(stage_fp[:6]))
            parts.append(f'<div class="fmap">📎 本阶段 File 编号对照：{leg}</div>')
        for n,r in enumerate(items,1):
            sv=sev_norm(r[m["sev"]]); axis=r.get(m.get("axis",""),"") or "内部"
            oid=r.get(m["id_"],""); key=oid or f'{g}#{n}'; ev=r.get(m["ev"],"")
            # chips
            toks=extract_tokens(ev); chips=[]
            for t in toks:
                fm=re.match(r"File\s?0?(\d+)",t); path=None; label=t
                if fm:
                    k=f"File0{int(fm.group(1))}"
                    if k in file0n: path=file0n[k]; label=f"{k}={short_name(path)}"
                if not path: path=resolve_token(t,stage_fp,all_fp)
                if path: chips.append(f'<a class="filechip" href="{to_href(path)}" target="_blank" title="{esc(path)}">📄 {esc(label)}</a>')
                else: chips.append(f'<span class="filechip dim">{esc(t)}</span>')
            if not chips:
                if folder: chips.append(f'<a class="filechip" href="{to_href(folder)}" target="_blank" title="{esc(folder)}">📂 打开 {esc(g)} 文件夹</a>')
                else: chips.append(f'<span class="filechip dim">{esc(g)}</span>')
            linkv=r.get(m.get("link",""),"")
            vs=f'<span class="vs">→ {esc(linkv)}</span>' if (axis=="关联" and linkv) else (f'<span class="vs" style="background:#eef2f7;color:#3a4654;border-color:#dde3ea">{esc(m["linklabel"])}:{esc(linkv)}</span>' if linkv else '')
            fix=f'<div class="field"><span class="k">改法</span><div class="fix">{esc(r.get(m["sug"],""))}</div></div>' if r.get(m["sug"]) else ''
            rolev=esc(r.get(cfg["role"],"") or r.get("系统性归类",""))
            findings.append({"id":key,"oid":oid,"stage":g,"sev":SEVCN.get(sv,sv),"type":r.get(m["type"],""),"desc":(r.get(m["desc"],"") or "")[:160]})
            parts.append(f"""<div class="card {sv}" data-id="{esc(key)}">
<div class="chead"><span class="num">{n}</span><span class="badge b-{sv}">{SEVCN.get(sv,sv)}</span>
<span class="axis ax-{axis}">{esc(axis)}</span>{vs}<span class="type">{esc(r.get(m["type"],""))}</span>
<span class="idtag">{esc(oid)}</span><span class="role">{rolev}</span></div>
<div class="filerow">📄 出处：{' '.join(chips)}</div>
<div class="field"><span class="k">问题</span>{esc(r.get(m["desc"],""))}</div>
<div class="field"><span class="k">证据</span><div class="ev">{esc(ev)}</div></div>
{fix}
<div class="review">
<label><input type="radio" name="d_{esc(key)}" value="接受">✅ 接受</label>
<label><input type="radio" name="d_{esc(key)}" value="不接受">❌ 不接受</label>
<label><input type="radio" name="d_{esc(key)}" value="待定">🕐 待定</label>
<input class="reason" type="text" placeholder="原因 / 备注（可选）">
</div></div>""")
    data=f'<script>const MODEL={json.dumps(model)};const TOTAL={len(rows)};const FINDINGS={json.dumps(findings,ensure_ascii=False)};</script>'
    parts.append(data+f"<script>{JS}</script></div></body></html>")
    open(cfg["out"],"w",encoding="utf-8").write("\n".join(parts))
    print(f"[OK] {model}: {len(rows)}条, 语料{len(all_fp)}件 -> {cfg['out']}")

target=sys.argv[1] if len(sys.argv)>1 else "all"
for mdl in (MODELS if target=="all" else [target]):
    gen(mdl)
