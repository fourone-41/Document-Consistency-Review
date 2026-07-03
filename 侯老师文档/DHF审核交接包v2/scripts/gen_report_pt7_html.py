# -*- coding: utf-8 -*-
import sys, os, csv, re, html, datetime as dt
from collections import defaultdict, Counter
sys.stdout.reconfigure(encoding="utf-8")

SRC = r"D:\AI_0415\03DHF\new_pt7_CHECK\PT7-错误总表.csv"
OUT = r"D:\AI_0415\03DHF\new_pt7_CHECK\PT7-DHF检测报告.html"
rows=list(csv.DictReader(open(SRC,encoding="utf-8-sig")))

SEV={"critical":0,"major":1,"minor":2,"待PM确认":3,"NEI":4}
SEVCN={"critical":"严重","major":"重要","minor":"一般","待PM确认":"待PM定","NEI":"无正文"}
def sev_norm(s): return (s or "").strip()

# 文件夹号 -> 短名 + 备注
STAGE_NOTES={
 "16 设变01-设计输出":"本文件夹物理位置在 <b>15 设计变更01\\设变01-设计输出-发给柯顿签字档\\</b>，内含 2 份：设计更改通知单.pdf + PT7红外体温计产品检验标准.pdf（柯顿签字档）。",
}
def stage_short(st):
    return re.sub(r"\s*\(.*$","",st or "").strip()  # 砍掉括号补充说明
def stage_key(st):
    m=re.match(r"\s*(\d+)",st or "")
    return (int(m.group(1)) if m else 98, st or "")

groups=defaultdict(list)
for r in rows:
    groups[stage_short(r["阶段"])].append(r)
order=sorted(groups, key=lambda g: stage_key(g))

DOCNAMES=["客户需求评审单","客户需求书","立项批准书","设计开发计划评审表","设计开发计划","开发计划表","开发计划","项目进度表","项目组成员名单",
 "风险管理计划","风险评价报告","风险控制措施","风险管理报告","风险评价","DFMEA",
 "设计输入汇总表","设计输入","通用要求","功能规格","性能规格","组件规格","法规标准清单","法规清单",
 "结构设计方案","硬件设计方案","原理图","软件质量策划","质量策划","软件需求规格","软件需求","软件方案","软件设计","软件流程图","软件构建","软件测试","系统测试","子程序测试",
 "结构图样","硬件图样","软件图样","PCB","网表","检验标准","缺陷定义","设计验证计划","设计验证报告","检测报告","验证报告","产品概述","工作原理","工艺说明","装配说明","新物料检验规范",
 "设计输出清单二","设计输出清单一","设计输出清单","转移文件清单","机芯类组件清单","总装类组件清单","包装类组件清单","EBOM","ABOM","PBOM","组件清单",
 "试产申请单","试产总结报告","试产总结","试产","标签审核表","operation guide","说明书","IFU","临床","软件确认报告","可追溯","软件配置清单","usability",
 "设计更改通知单","设计变更","变更评审","设计确认","上市批准","铭牌","彩盒","外箱","运输","评审记录","评审计划","评审表","目标代码","软件配置"]

def extract_files(ev):
    if not ev: return []
    found=[]
    for m in re.findall(r"[\w一-鿿\-＋\+．\.]+?\.(?:md|xls|xlsx|doc|docx|pdf|mpp|MTP|BIN|hex)", ev):
        if re.match(r"^(no|No|grep|matches)",m): m=re.sub(r"^[A-Za-z]*(?=[一-鿿A-Z])","",m)
        if m not in found: found.append(m)
    for m in re.findall(r"PT7-[A-Z]{2,6}\d{0,2}", ev):
        if m not in found: found.append(m)
    for m in re.findall(r"PT9[SL]-[A-Z]{2,6}\d{0,2}", ev):  # 残留引用他型号编号也显示
        if m not in found: found.append(m)
    for nm in DOCNAMES:
        if nm in ev and not any(nm in f or f in nm for f in found):
            found.append(nm)
    return found[:5]

def esc(t): return html.escape(t or "")
sev_all=Counter(sev_norm(r["严重度"]) for r in rows)
axis_all=Counter(r.get("轴","") for r in rows)

css="""
*{box-sizing:border-box}body{font-family:-apple-system,'Segoe UI','Microsoft YaHei',sans-serif;margin:0;background:#f4f5f7;color:#1d2530;line-height:1.6}
.wrap{max-width:1000px;margin:0 auto;padding:28px 20px 80px}
h1{font-size:25px;margin:0 0 4px}.sub{color:#5b6675;font-size:14px;margin-bottom:18px}
.note{background:#fff8e6;border:1px solid #f3d27a;border-radius:10px;padding:14px 16px;font-size:14px;margin-bottom:20px}
.badge{display:inline-block;padding:2px 9px;border-radius:20px;font-size:12px;font-weight:700;color:#fff;white-space:nowrap}
.b-critical{background:#c0392b}.b-major{background:#e67e22}.b-minor{background:#b7950b}.b-待PM确认{background:#2471a3}.b-NEI{background:#7f8c8d}
.axis{display:inline-block;padding:2px 9px;border-radius:6px;font-size:12px;font-weight:700;white-space:nowrap}
.ax-内部{background:#eaf3ff;color:#1f6feb;border:1px solid #cfe2ff}.ax-关联{background:#fdeef0;color:#c0392b;border:1px solid #f5c6cd}
.sumtbl{width:100%;border-collapse:collapse;font-size:13px;margin-bottom:8px;background:#fff;border-radius:10px;overflow:hidden;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.sumtbl th,.sumtbl td{padding:8px 10px;border-bottom:1px solid #eef0f3;text-align:left}.sumtbl th{background:#eef2f7}
.toc{background:#fff;border-radius:10px;padding:12px 16px;margin-bottom:24px;font-size:13.5px;box-shadow:0 1px 3px rgba(0,0,0,.06)}
.toc a{color:#1f6feb;text-decoration:none;margin-right:4px;white-space:nowrap;display:inline-block;margin-bottom:3px}
.stage{margin:26px 0 10px;padding:10px 14px;background:#1d2530;color:#fff;border-radius:9px;font-size:18px;font-weight:700;display:flex;justify-content:space-between;align-items:center}
.stage .cnt{font-size:13px;font-weight:500;opacity:.85}
.stagenote{background:#eef4ff;border:1px solid #cfe0ff;border-left:4px solid #2471a3;border-radius:0 8px 8px 0;padding:9px 13px;margin:-4px 0 8px;font-size:13px;color:#2a3b52}
.card{background:#fff;border-radius:10px;padding:14px 16px;margin:10px 0;box-shadow:0 1px 3px rgba(0,0,0,.06);border-left:5px solid #ccc}
.card.critical{border-left-color:#c0392b}.card.major{border-left-color:#e67e22}.card.minor{border-left-color:#b7950b}.card.待PM确认{border-left-color:#2471a3}.card.NEI{border-left-color:#7f8c8d}
.chead{display:flex;align-items:center;gap:9px;flex-wrap:wrap;margin-bottom:7px}
.num{font-weight:800;font-size:16px;color:#1d2530}.type{font-size:13px;color:#5b6675;font-weight:600}
.idtag{font-size:11px;color:#9aa5b1;font-family:monospace}.role{margin-left:auto;font-size:12px;background:#eef2f7;border-radius:20px;padding:2px 10px;color:#3a4654}
.vs{font-size:12px;background:#fdeef0;color:#c0392b;border:1px solid #f5c6cd;border-radius:6px;padding:1px 8px;font-weight:700}
.filerow{font-size:13px;margin:4px 0}.filechip{display:inline-block;background:#eaf3ff;color:#1f6feb;border:1px solid #cfe2ff;border-radius:6px;padding:1px 8px;font-family:monospace;font-size:12px;margin:1px 2px}
.field{margin:7px 0;font-size:14px}.field .k{font-weight:700;color:#3a4654;margin-right:6px}
.ev{background:#f7f8fa;border:1px solid #eceef1;border-radius:7px;padding:8px 11px;font-size:13px;color:#33404f;white-space:pre-wrap}
.fix{background:#eefaf0;border:1px solid #c8ebd0;border-radius:7px;padding:8px 11px;font-size:13.5px;color:#1e6b3a}
@media print{body{background:#fff}.card,.toc,.sumtbl{box-shadow:none;border:1px solid #e3e6ea}}
"""

parts=[f"""<!doctype html><html lang="zh-CN"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>PT7 DHF 检测报告</title><style>{css}</style></head><body><div class="wrap">
<h1>PT7 红外额温计 · DHF 检测报告</h1>
<div class="sub">美版（仅美国）· 项目号 30000059 · 生成 {dt.datetime.now().replace(microsecond=0)} · 共 {len(rows)} 条（增量审核：边写边审，按文件夹 01→20）</div>
<div class="note"><b>说明：</b>本产品 DHF 为首次编写，本报告用于一次性集中纠错。<b>按文件夹顺序 01→20 排列，每条含：问题、出处文件、原文证据、修改建议、责任人。</b>
每条标注属于 <span class="axis ax-内部">内部</span>（本文件夹自身问题）还是 <span class="axis ax-关联">关联</span>（与前面已写文件夹冲突／未承接，并标明 <span class="vs">→ 哪个前序</span>）。
<br>严重度：<span class="badge b-critical">严重</span> 必须改；<span class="badge b-major">重要</span> 应改；<span class="badge b-minor">一般</span> 建议改；<span class="badge b-待PM确认">待PM定</span> 需 PM 先拍板；<span class="badge b-NEI">无正文</span> 该项无正文/未产出（多为后段设计转换/确认未完成，需补做）。</div>
<table class="sumtbl"><tr><th>严重度</th><th>严重</th><th>重要</th><th>一般</th><th>待PM定</th><th>无正文</th><th>合计</th></tr>
<tr><td>条数</td><td>{sev_all.get('critical',0)}</td><td>{sev_all.get('major',0)}</td><td>{sev_all.get('minor',0)}</td><td>{sev_all.get('待PM确认',0)}</td><td>{sev_all.get('NEI',0)}</td><td><b>{len(rows)}</b></td></tr>
<tr><td>轴</td><td colspan="6">内部问题 {axis_all.get('内部',0)} 条　|　关联问题（跨文件夹）{axis_all.get('关联',0)} 条</td></tr></table>
"""]

toc=['<div class="toc"><b>目录：</b>']
for i,g in enumerate(order):
    toc.append(f'<a href="#s{i}">{esc(g)}（{len(groups[g])}）</a>')
toc.append("</div>")
parts.append(" ".join(toc))

for i,g in enumerate(order):
    items=sorted(groups[g], key=lambda r:(SEV.get(sev_norm(r["严重度"]),9), r.get("轴",""), r["原ID"]))
    sc=Counter(sev_norm(r["严重度"]) for r in items)
    cnttxt=" · ".join(f"{SEVCN[k]}{sc[k]}" for k in ["critical","major","minor","待PM确认","NEI"] if sc.get(k))
    parts.append(f'<div class="stage" id="s{i}"><span>{esc(g)}</span><span class="cnt">{len(items)} 条　{cnttxt}</span></div>')
    if g in STAGE_NOTES:
        parts.append(f'<div class="stagenote">📌 {STAGE_NOTES[g]}</div>')
    for n,r in enumerate(items,1):
        sv=sev_norm(r["严重度"]); axis=r.get("轴","内部"); files=extract_files(r["证据"])
        if files:
            chips=" ".join(f'<span class="filechip">{esc(x)}</span>' for x in files)
        else:
            chips=f'<span class="filechip" style="background:#f3f4f6;color:#6b7280;border-color:#e3e6ea">{esc(g)} 文件夹（详见证据）</span>'
        filechip=f'<div class="filerow">📄 出处文件：{chips}</div>'
        vs=f'<span class="vs">→ {esc(r["关联前序"])}</span>' if (axis=="关联" and r.get("关联前序")) else ''
        fix=f'<div class="field"><span class="k">改法</span><div class="fix">{esc(r["建议"])}</div></div>' if r.get("建议") else ''
        parts.append(f"""<div class="card {sv}">
<div class="chead"><span class="num">{n}</span><span class="badge b-{sv}">{SEVCN.get(sv,sv)}</span>
<span class="axis ax-{axis}">{esc(axis)}</span>{vs}
<span class="type">{esc(r['类型'])}</span><span class="idtag">{esc(r['原ID'])}</span>
<span class="role">{esc(r['责任工程师'])}</span></div>
{filechip}
<div class="field"><span class="k">问题</span>{esc(r['描述'])}</div>
<div class="field"><span class="k">证据</span><div class="ev">{esc(r['证据'])}</div></div>
{fix}
</div>""")

parts.append("</div></body></html>")
open(OUT,"w",encoding="utf-8").write("\n".join(parts))
print("[OK]",OUT)
print("文件夹数:",len(order),"| 总条数:",len(rows))
print("严重度:",dict(sev_all),"| 轴:",dict(axis_all))
