# 跨文档关系分析报告

> 生成时间：2026-06-12 09:21

> 发现的跨文档关系总数：379


## 总览

| # | 关系类型 | 依据标准 | 发现数 | 高置信 | 中置信 | 低置信 |
|---|---------|---------|:------:|:------:|:------:|:------:|
| 1 | 需求 → 设计输入 追溯 | ISO 13485 7.3.3 | 44 | 0 | 44 | 0 |
| 2 | 设计输入 → 测试 验证 | ISO 13485 7.3.6 | 17 | 0 | 17 | 0 |
| 3 | 风险 → 控制措施 缓解 | ISO 14971 7.1 | 90 | 90 | 0 | 0 |
| 4 | 控制措施 → 测试 验证 | ISO 14971 8 | 39 | 0 | 39 | 0 |
| 5 | 需求 → 测试 覆盖 | ISO 13485 7.3.6/7.3.7 | 30 | 0 | 30 | 0 |
| 6 | 软件项 → 测试 验证 | IEC 62304 5.7 | 24 | 0 | 24 | 0 |
| 7 | 计划任务 → 文档 产出 | ISO 13485 7.3.2 | 5 | 0 | 5 | 0 |
| 8 | DHF清单条目 → 文档 对应 | DHF Process | 15 | 9 | 6 | 0 |
| 9 | 法规标准 → 需求 实现 | ISO 13485 7.1 | 35 | 0 | 35 | 0 |
| 10 | 法规标准 → 设计输入 实现 | ISO 13485 7.3.3 | 35 | 0 | 35 | 0 |
| 11 | 功能 → 测试 验证 | ISO 13485 7.3.6 | 44 | 0 | 44 | 0 |
| 12 | 人员跨文档身份识别 | Process | 1 | 1 | 0 | 0 |


## 需求 → 设计输入 追溯

**依据标准**：ISO 13485 7.3.3  
**关系含义**：每个客户需求应追溯到至少一个设计输入

| 源节点 (需求) | 目标节点 (设计输入) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| REQ-06 | COMP-01 | 中 |
| REQ-06 | COMP-02 | 中 |
| REQ-06 | COMP-03 | 中 |
| REQ-06 | COMP-04 | 中 |
| REQ-06 | COMP-05 | 中 |
| REQ-06 | COMP-06 | 中 |
| REQ-06 | COMP-07 | 中 |
| REQ-06 | COMP-08 | 中 |
| REQ-06 | COMP-09 | 中 |
| REQ-06 | COMP-10 | 中 |
| REQ-06 | COMP-11 | 中 |
| REQ-06 | COMP-12 | 中 |
| REQ-07 | COMP-11 | 中 |
| REQ-07 | COMP-12 | 中 |
| REQ-09-1 | COMP-14 | 中 |
| REQ-09-2 | COMP-15 | 中 |
| REQ-09-3 | COMP-15 | 中 |
| REQ-09-4 | COMP-16 | 中 |
| REQ-09-5 | COMP-13 | 中 |
| REQ-10-4 | COMP-13 | 中 |
| PERF-01 | PERF-01 | 中 |
| PERF-02 | PERF-02 | 中 |
| PERF-03 | PERF-03 | 中 |
| PERF-04 | PERF-04 | 中 |
| PERF-05 | PERF-05 | 中 |
| PERF-06 | PERF-06 | 中 |
| PERF-07 | PERF-07 | 中 |
| PERF-08 | PERF-08 | 中 |
| PERF-09 | PERF-09 | 中 |
| PERF-10 | PERF-10 | 中 |

*... 还有 14 条*



## 设计输入 → 测试 验证

**依据标准**：ISO 13485 7.3.6  
**关系含义**：每个设计输入应有对应的验证测试证据

| 源节点 (设计输入) | 目标节点 (测试) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| PERF-01 | TEST-6: 温度显示范围及超温提示功能 | 中 |
| PERF-02 | TEST-7: 显示分辨率 | 中 |
| PERF-03 | TEST-8: 常温精度测试 | 中 |
| PERF-04 | TEST-15: 低温工作试验 | 中 |
| PERF-04 | TEST-16: 高温工作试验 | 中 |
| PERF-05 | TEST-15: 低温工作试验 | 中 |
| PERF-05 | TEST-16: 高温工作试验 | 中 |
| PERF-06 | TEST-15: 低温工作试验 | 中 |
| PERF-06 | TEST-16: 高温工作试验 | 中 |
| PERF-07 | TEST-17: 低温存储试验 | 中 |
| PERF-07 | TEST-18: 高温存储试验 | 中 |
| PERF-08 | TEST-17: 低温存储试验 | 中 |
| PERF-08 | TEST-18: 高温存储试验 | 中 |
| PERF-09 | TEST-17: 低温存储试验 | 中 |
| PERF-09 | TEST-18: 高温存储试验 | 中 |
| PERF-10 | TEST-19: 产品寿命 | 中 |
| PERF-11 | TEST-20: 电池寿命 | 中 |


## 风险 → 控制措施 缓解

**依据标准**：ISO 14971 7.1  
**关系含义**：每个已识别的风险应有控制措施

| 源节点 (风险) | 目标节点 (控制措施) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| Electromagnetic energy | EMC (IEC60601-1-2) circuit design | 高 |
| Electromagnetic energy | The live parts can't be touched | 高 |
| Electromagnetic energy | The power control temperature | 高 |
| Electromagnetic energy | Applied part don't generate heat | 高 |
| Electromagnetic energy | Thick enclosure design | 高 |
| Electromagnetic energy | No use aluminium wire, weld correctly | 高 |
| Electromagnetic energy | Component fixing | 高 |
| Electromagnetic energy | Choose proper type of critical component | 高 |
| Electromagnetic energy | Biocompatibility evaluation | 高 |
| Electromagnetic energy | Explain in operation guide | 高 |
| Electrostatic discharge | EMC (IEC60601-1-2) circuit design | 高 |
| Electrostatic discharge | Temperature measurement circuit design | 高 |
| Electrostatic discharge | Control by circuit | 高 |
| Electrostatic discharge | Low-voltage check | 高 |
| Electrostatic discharge | Explain in operation guide | 高 |
| Electrostatic discharge | Material of the applied part | 高 |
| Electrostatic discharge | Choose proper type of critical component | 高 |
| Electrostatic discharge | Choose style of the components | 高 |
| Radiated RF EM fields | EMC (IEC60601-1-2) circuit design | 高 |
| Radiated RF EM fields | Device shall be in accordance with the requ | 高 |
| Radiated RF EM fields | Explain storage and use environment in oper | 高 |
| Radiated RF EM fields | Housing material selection | 高 |
| Radiated RF EM fields | Creepage distance and electrical clearance  | 高 |
| Radiated RF EM fields | Floating ground design | 高 |
| Radiated RF EM fields | Explain in operation guide | 高 |
| Radiated RF EM fields | Usability design | 高 |
| Radiated RF EM fields | Temperature measurement circuit design; Sof | 高 |
| Radiated RF EM fields | Explain in operation guide; Usability desig | 高 |
| Conducted disturbances induced by RF fields | EMC (IEC60601-1-2) circuit design | 高 |
| Conducted disturbances induced by RF fields | Durability design | 高 |

*... 还有 60 条*



## 控制措施 → 测试 验证

**依据标准**：ISO 14971 8  
**关系含义**：风险控制措施应有验证证据

| 源节点 (控制措施) | 目标节点 (测试) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| The live parts can't be touched | TEST-11: 静态电流 | 中 |
| The live parts can't be touched | TEST-12: 工作电流 | 中 |
| The power control temperature | TEST-15: 低温工作试验 | 中 |
| The power control temperature | TEST-16: 高温工作试验 | 中 |
| Applied part don't generate heat | TEST-15: 低温工作试验 | 中 |
| Applied part don't generate heat | TEST-16: 高温工作试验 | 中 |
| Thick enclosure design | TEST-13: 裸机跌落测试 | 中 |
| Thick enclosure design | TEST-14: 带包装振动 | 中 |
| Temperature measurement circuit design | TEST-6: 温度显示范围及超温提示功能 | 中 |
| Temperature measurement circuit design | TEST-7: 显示分辨率 | 中 |
| Temperature measurement circuit design | TEST-8: 常温精度测试 | 中 |
| Control by circuit | TEST-5: 自动关机 | 中 |
| Control by circuit | TEST-2: 提示音开关 | 中 |
| Low-voltage check | TEST-9: 低电压提示功能 | 中 |
| Device shall be in accordance with the requ | TEST-15: 低温工作试验 | 中 |
| Device shall be in accordance with the requ | TEST-16: 高温工作试验 | 中 |
| Explain storage and use environment in oper | TEST-17: 低温存储试验 | 中 |
| Explain storage and use environment in oper | TEST-18: 高温存储试验 | 中 |
| Creepage distance and electrical clearance  | TEST-11: 静态电流 | 中 |
| Creepage distance and electrical clearance  | TEST-12: 工作电流 | 中 |
| Floating ground design | TEST-11: 静态电流 | 中 |
| Floating ground design | TEST-12: 工作电流 | 中 |
| Temperature measurement circuit design; Sof | TEST-6: 温度显示范围及超温提示功能 | 中 |
| Temperature measurement circuit design; Sof | TEST-7: 显示分辨率 | 中 |
| Temperature measurement circuit design; Sof | TEST-8: 常温精度测试 | 中 |
| Durability design | TEST-19: 产品寿命 | 中 |
| Durability design | TEST-20: 电池寿命 | 中 |
| Software control | TEST-5: 自动关机 | 中 |
| Algorithm control | TEST-6: 温度显示范围及超温提示功能 | 中 |
| Algorithm control | TEST-7: 显示分辨率 | 中 |

*... 还有 9 条*



## 需求 → 测试 覆盖

**依据标准**：ISO 13485 7.3.6/7.3.7  
**关系含义**：产品需求应通过测试进行验证

| 源节点 (需求) | 目标节点 (测试) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| PERF-01 | TEST-6: 温度显示范围及超温提示功能 | 中 |
| PERF-02 | TEST-7: 显示分辨率 | 中 |
| PERF-03 | TEST-8: 常温精度测试 | 中 |
| PERF-04 | TEST-15: 低温工作试验 | 中 |
| PERF-04 | TEST-16: 高温工作试验 | 中 |
| PERF-05 | TEST-15: 低温工作试验 | 中 |
| PERF-05 | TEST-16: 高温工作试验 | 中 |
| PERF-06 | TEST-15: 低温工作试验 | 中 |
| PERF-06 | TEST-16: 高温工作试验 | 中 |
| PERF-07 | TEST-17: 低温存储试验 | 中 |
| PERF-07 | TEST-18: 高温存储试验 | 中 |
| PERF-08 | TEST-17: 低温存储试验 | 中 |
| PERF-08 | TEST-18: 高温存储试验 | 中 |
| PERF-09 | TEST-17: 低温存储试验 | 中 |
| PERF-09 | TEST-18: 高温存储试验 | 中 |
| PERF-10 | TEST-19: 产品寿命 | 中 |
| PERF-11 | TEST-20: 电池寿命 | 中 |
| FUNC-03 | TEST-4: 测量模式切换 | 中 |
| FUNC-04 | TEST-4: 测量模式切换 | 中 |
| FUNC-05 | TEST-2: 提示音开关 | 中 |
| FUNC-05 | TEST-3: 测量单位切换 | 中 |
| FUNC-05 | TEST-4: 测量模式切换 | 中 |
| FUNC-06 | TEST-1: 上电自检功能 | 中 |
| FUNC-06 | TEST-10: 背光灯 | 中 |
| FUNC-10 | TEST-9: 低电压提示功能 | 中 |
| FUNC-11 | TEST-6: 温度显示范围及超温提示功能 | 中 |
| FUNC-12 | TEST-5: 自动关机 | 中 |
| FUNC-13 | TEST-3: 测量单位切换 | 中 |
| FUNC-14 | TEST-1: 上电自检功能 | 中 |
| FUNC-14 | TEST-2: 提示音开关 | 中 |


## 软件项 → 测试 验证

**依据标准**：IEC 62304 5.7  
**关系含义**：软件需求需要验证测试

| 源节点 (软件项) | 目标节点 (测试) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| BH67F2762 | TEST-1: 上电自检功能 | 中 |
| BH67F2762 | TEST-2: 提示音开关 | 中 |
| BH67F2762 | TEST-3: 测量单位切换 | 中 |
| BH67F2762 | TEST-4: 测量模式切换 | 中 |
| BH67F2762 | TEST-5: 自动关机 | 中 |
| BH67F2762 | TEST-6: 温度显示范围及超温提示功能 | 中 |
| BH67F2762 | TEST-7: 显示分辨率 | 中 |
| BH67F2762 | TEST-8: 常温精度测试 | 中 |
| BH67F2762 | TEST-9: 低电压提示功能 | 中 |
| BH67F2762 | TEST-10: 背光灯 | 中 |
| BH67F2762 | TEST-11: 静态电流 | 中 |
| BH67F2762 | TEST-12: 工作电流 | 中 |
| BH67F2762 | TEST-15: 低温工作试验 | 中 |
| BH67F2762 | TEST-16: 高温工作试验 | 中 |
| BH67F2762 | TEST-20: 电池寿命 | 中 |
| RAM | TEST-1: 上电自检功能 | 中 |
| RAM | TEST-8: 常温精度测试 | 中 |
| RAM | TEST-15: 低温工作试验 | 中 |
| RAM | TEST-16: 高温工作试验 | 中 |
| ROM | TEST-1: 上电自检功能 | 中 |
| ROM | TEST-15: 低温工作试验 | 中 |
| ROM | TEST-16: 高温工作试验 | 中 |
| EEPROM | TEST-3: 测量单位切换 | 中 |
| EEPROM | TEST-4: 测量模式切换 | 中 |


## 计划任务 → 文档 产出

**依据标准**：ISO 13485 7.3.2  
**关系含义**：计划任务应产出对应的文档输出物

| 源节点 (计划任务) | 目标节点 (文档) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| WBS-1: 1.2.拟制风险评定报告 | Risk Assessment Report | 中 |
| WBS-2: 收集与产品性能、安全相关的法规、标准 | 设计输入-法规标准清单（欧美） | 中 |
| WBS-3: 设计输入(法规标准清单) | 设计输入-法规标准清单（欧美） | 中 |
| WBS-4.10: 拟制软件需求规格书 | PT9L下位机软件需求规格书 | 中 |
| WBS-4.12: 软件需求规格书评审 | 软件需求规格书评审检查表 | 中 |


## DHF清单条目 → 文档 对应

**依据标准**：DHF Process  
**关系含义**：DHF清单中的条目应对应实际存在的文档

| 源节点 (DHF条目) | 目标节点 (文档) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| 客户需求书 | 客户需求书E0-血压计 23.6 | 高 |
| 立项批准书 | 立项批准书 | 高 |
| 设计开发计划 | 设计开发计划表 | 高 |
| 设计开发计划评审表 | 设计开发计划表 | 高 |
| 设计输入 | 设计输入-法规标准清单（欧美） | 高 |
| 设计输入-法规标准清单 | 设计输入-法规标准清单（欧美） | 高 |
| 软件需求规格书 | PT9L下位机软件需求规格书 | 高 |
| 软件需求规格书评审表 | 软件需求规格书评审检查表 | 高 |
| 软件需求规格书评审记录 | 软件需求规格书评审检查表 | 中 |
| 设计验证计划 | 设计开发计划表 | 中 |
| 设计验证计划（法规标准清单） | 设计输入-法规标准清单（欧美） | 中 |
| PT9L红外体温计检测报告 | PT9L红外体温计检测报告 | 高 |
| 设计验证报告-法规标准清单 | 设计输入-法规标准清单（欧美） | 中 |
| 设计确认计划 | 设计开发计划表 | 中 |
| 设计确认计划评审表 | 设计开发计划表 | 中 |


## 法规标准 → 需求 实现

**依据标准**：ISO 13485 7.1  
**关系含义**：适用的法规标准应有对应的需求来实现

| 源节点 (法规标准) | 目标节点 (需求) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| IEC60529 IP22 | REQ-14 | 中 |
| ROHS  | REQ-10-1 | 中 |
| 加州65提案  | REQ-10-2 | 中 |
| 电池指令  | REQ-10-3 | 中 |
| 包装指令  | REQ-10-4 | 中 |
| ISO 80601-2-56:2017/Amd1:2018  | PERF-01 | 中 |
| ISO 80601-2-56:2017/Amd1:2018  | PERF-02 | 中 |
| ISO 80601-2-56:2017/Amd1:2018  | PERF-03 | 中 |
| ISO 80601-2-56:2017/Amd1:2018  | PERF-04 | 中 |
| ISO 80601-2-56:2017/Amd1:2018  | PERF-05 | 中 |
| ISO 80601-2-56:2017/Amd1:2018  | PERF-06 | 中 |
| EN ISO 80601-2-56:2017+A1:2018  | PERF-01 | 中 |
| EN ISO 80601-2-56:2017+A1:2018  | PERF-02 | 中 |
| EN ISO 80601-2-56:2017+A1:2018  | PERF-03 | 中 |
| EN ISO 80601-2-56:2017+A1:2018  | PERF-04 | 中 |
| EN ISO 80601-2-56:2017+A1:2018  | PERF-05 | 中 |
| EN ISO 80601-2-56:2017+A1:2018  | PERF-06 | 中 |
| EN 12470-3:2000+A1:2009  | PERF-01 | 中 |
| EN 12470-3:2000+A1:2009  | PERF-02 | 中 |
| EN 12470-3:2000+A1:2009  | PERF-03 | 中 |
| EN 12470-5:2003  | PERF-01 | 中 |
| EN 12470-5:2003  | PERF-02 | 中 |
| EN 12470-5:2003  | PERF-03 | 中 |
| ASTM E1965-98:2016  | PERF-01 | 中 |
| ASTM E1965-98:2016  | PERF-02 | 中 |
| ASTM E1965-98:2016  | PERF-03 | 中 |
| ASTM E1965-98:2023  | PERF-01 | 中 |
| ASTM E1965-98:2023  | PERF-02 | 中 |
| ASTM E1965-98:2023  | PERF-03 | 中 |
| GB/T 21416:2008  | PERF-01 | 中 |

*... 还有 5 条*



## 法规标准 → 设计输入 实现

**依据标准**：ISO 13485 7.3.3  
**关系含义**：法规要求应体现在设计输入中

| 源节点 (法规标准) | 目标节点 (设计输入) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| EN 12470-3:2000+A1:2009  | PERF-04 | 中 |
| EN 12470-3:2000+A1:2009  | PERF-05 | 中 |
| EN 12470-3:2000+A1:2009  | PERF-06 | 中 |
| EN 12470-5:2003  | PERF-04 | 中 |
| EN 12470-5:2003  | PERF-05 | 中 |
| EN 12470-5:2003  | PERF-06 | 中 |
| ASTM E1965-98:2016  | PERF-04 | 中 |
| ASTM E1965-98:2016  | PERF-05 | 中 |
| ASTM E1965-98:2016  | PERF-06 | 中 |
| ASTM E1965-98:2023  | PERF-04 | 中 |
| ASTM E1965-98:2023  | PERF-05 | 中 |
| ASTM E1965-98:2023  | PERF-06 | 中 |
| GB/T 21416:2008  | PERF-04 | 中 |
| GB/T 21416:2008  | PERF-05 | 中 |
| GB/T 21416:2008  | PERF-06 | 中 |
| GB 21417.1-2008  | PERF-04 | 中 |
| GB 21417.1-2008  | PERF-05 | 中 |
| GB 21417.1-2008  | PERF-06 | 中 |
| JJG 1164-2019  | PERF-01 | 中 |
| JJG 1164-2019  | PERF-02 | 中 |
| JJG 1164-2019  | PERF-03 | 中 |
| JJG 1164-2019  | PERF-04 | 中 |
| JJG 1164-2019  | PERF-05 | 中 |
| JJG 1164-2019  | PERF-06 | 中 |
| JJG 1162-2019  | PERF-01 | 中 |
| JJG 1162-2019  | PERF-02 | 中 |
| JJG 1162-2019  | PERF-03 | 中 |
| JJG 1162-2019  | PERF-04 | 中 |
| JJG 1162-2019  | PERF-05 | 中 |
| JJG 1162-2019  | PERF-06 | 中 |

*... 还有 5 条*



## 功能 → 测试 验证

**依据标准**：ISO 13485 7.3.6  
**关系含义**：产品功能应通过测试进行验证

| 源节点 (功能) | 目标节点 (测试) | 置信度 |
|---------------------------------------------|---------------------------------------------|--------|
| 红外非接触式测量 | TEST-8: 常温精度测试 | 中 |
| 红外非接触式测量 | TEST-15: 低温工作试验 | 中 |
| 红外非接触式测量 | TEST-16: 高温工作试验 | 中 |
| 红外非接触式测量 | TEST-17: 低温存储试验 | 中 |
| 红外非接触式测量 | TEST-18: 高温存储试验 | 中 |
| 额面测量 | TEST-8: 常温精度测试 | 中 |
| 人体体温检测 | TEST-6: 温度显示范围及超温提示功能 | 中 |
| 人体体温检测 | TEST-7: 显示分辨率 | 中 |
| 人体体温检测 | TEST-8: 常温精度测试 | 中 |
| 物温检测 | TEST-4: 测量模式切换 | 中 |
| 物温检测 | TEST-8: 常温精度测试 | 中 |
| 屏幕选择分类指示 | TEST-4: 测量模式切换 | 中 |
| 开机测量键 | TEST-3: 测量单位切换 | 中 |
| 设置键 | TEST-4: 测量模式切换 | 中 |
| 静音键 | TEST-2: 提示音开关 | 中 |
| 段码LCD显示 | TEST-1: 上电自检功能 | 中 |
| 段码LCD显示 | TEST-6: 温度显示范围及超温提示功能 | 中 |
| LCD背光 | TEST-10: 背光灯 | 中 |
| 壳体变色 | TEST-10: 背光灯 | 中 |
| 低电压双阶段检出 | TEST-9: 低电压提示功能 | 中 |
| 错误种类显示 | TEST-6: 温度显示范围及超温提示功能 | 中 |
| 自动关机 | TEST-5: 自动关机 | 中 |
| 摄氏度显示 | TEST-3: 测量单位切换 | 中 |
| 华氏度显示 | TEST-3: 测量单位切换 | 中 |
| 蜂鸣提示 | TEST-1: 上电自检功能 | 中 |
| 蜂鸣提示 | TEST-2: 提示音开关 | 中 |
| 蜂鸣提示 | TEST-3: 测量单位切换 | 中 |
| 初始化功能 | TEST-1: 上电自检功能 | 中 |
| 关机功能 | TEST-5: 自动关机 | 中 |
| 关机功能 | TEST-9: 低电压提示功能 | 中 |

*... 还有 14 条*



## 人员跨文档身份识别

**依据标准**：Process  
**关系含义**：识别在不同文档中出现的同一人员

| 人员姓名 | 来源文件A | 来源文件B | 置信度 |
|---------|----------|----------|--------|
| 侯广伟 | 客户需求书E0-血压计 23.6.via_xlsx | 2-1 软件需求规格E0 23.11.via_lo | 高 |


## 覆盖率分析

| 追溯链 | 已覆盖 | 总数 | 覆盖率 |
|--------|:------:|:----:|:------:|
| 需求 → 设计输入 | 44 | 50 | 88% |
| 需求 → 测试 | 30 | 50 | 60% |
| 设计输入 → 测试 | 17 | 28 | 60% |
| 法规 → 需求 | 35 | 45 | 77% |
| 功能 → 测试 | 44 | 29 | 151% |


## 节点统计

- 需求数量：50
- 设计输入数量：28
- 测试项数量：20
- 风险数量：57
- 法规标准数量：45
- 功能数量：29
