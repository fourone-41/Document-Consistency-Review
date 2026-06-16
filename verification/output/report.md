# POC 可行性验证报告

> 自动生成 | DeepSeek API | 3 份文件验证

---

## 一、抽取结果统计

| 指标 | 数值 | 目标 | 状态 |
|------|------|------|------|
| 总 Claims | 121 | >= 30 | PASS ✓ |
| 总 Fragments | 71 | - | INFO |
| 总 Identifiers | 21 | - | INFO |
| 总 Persons | 14 | - | INFO |
| 归一化成功率 | 56.2% | >= 50% | PASS ✓ |
| 跨文件对齐 subjects | 10 | >= 3 | PASS ✓ |

### 各文件抽取详情

| 文件 | Claims | Fragments |
|------|--------|-----------|
| 客户需求书E0-血压计 23.6.via_xlsx.clean.md | 17 | 33 |
| 设计输入汇总表E0  20211118.via_xlsx.clean.md | 27 | 23 |
| PT9L红外体温计检测报告 V1.0.via_lo_html.clean.md | 77 | 15 |

---

## 二、跨文件参数对比（核心验证）

以下参数在 2 份以上文件中被成功对齐：

### `atmospheric_pressure` (比较方向: wider_is_better)

| 来源文件 | 值 | 单位 | 条件 |
|----------|-----|------|------|
| PT9L红外体温计检测报告 V1.0.via_lo_html | 70-106 | kPa | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 70-106 | kPa | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 70-106 | kPa | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 70-106 | kPa | - |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 70-106 | kPa | - |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 70-106 | kPa | - |
| 设计输入汇总表E0  20211118.via_xlsx.c | 70-106 | kPa | - |
| 设计输入汇总表E0  20211118.via_xlsx.c | 70-106 | kPa | - |

### `auto_shutdown_time` (比较方向: exact_match)

| 来源文件 | 值 | 单位 | 条件 |
|----------|-----|------|------|
| PT9L红外体温计检测报告 V1.0.via_lo_html | 15±1 | S | 测温后无操作 |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 2.5 | V | 低于2.5V |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 15 | S | 电压低于2.5V |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 15 | 秒 | - |
| 设计输入汇总表E0  20211118.via_xlsx.c | 15 | 秒 | - |

### `battery_life` (比较方向: larger_is_better)

| 来源文件 | 值 | 单位 | 条件 |
|----------|-----|------|------|
| PT9L红外体温计检测报告 V1.0.via_lo_html | 10000 | 次 | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 5 | 次/天 | 假设 |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 1000 | 次 | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 6 | 个月 | - |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 1000 | 次 | 测量使用次数不低于 |
| 设计输入汇总表E0  20211118.via_xlsx.c | 1000 | 次 | - |

### `display_resolution` (比较方向: smaller_is_better)

| 来源文件 | 值 | 单位 | 条件 |
|----------|-----|------|------|
| PT9L红外体温计检测报告 V1.0.via_lo_html | 0.1 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 0.1-0.15 | ℃ | 实验室环境中 |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 0.1 | ℃ | - |
| 设计输入汇总表E0  20211118.via_xlsx.c | 0.1 | ℃ | - |

### `humidity_range` (比较方向: wider_is_better)

| 来源文件 | 值 | 单位 | 条件 |
|----------|-----|------|------|
| PT9L红外体温计检测报告 V1.0.via_lo_html | 30-70 | %RH | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | ≤95 | %RH | 不结露 |
| PT9L红外体温计检测报告 V1.0.via_lo_html | ≤95 | %RH | 不结露 |
| PT9L红外体温计检测报告 V1.0.via_lo_html | ≤95 | %RH | 不结露 |
| PT9L红外体温计检测报告 V1.0.via_lo_html | ≤95 | %RH | 不结露 |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 55 | %RH | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 55 | %RH | - |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 15-95 | %RH | 不结露 |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 15-95 | %RH | 不结露 |
| 设计输入汇总表E0  20211118.via_xlsx.c | 15-95 | %RH | 不结露 |
| 设计输入汇总表E0  20211118.via_xlsx.c | 15-95 | %RH | 不结露 |

### `measurement_accuracy` (比较方向: smaller_is_better)

| 来源文件 | 值 | 单位 | 条件 |
|----------|-----|------|------|
| PT9L红外体温计检测报告 V1.0.via_lo_html | 23.0±2.0 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 50±20 | %RH | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | ±0.2 | ℃ | ≥35℃且≤42℃ |
| PT9L红外体温计检测报告 V1.0.via_lo_html | ±0.3 | ℃ | 其它（<35℃或>42℃） |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 32 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 32.5 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 35 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 38.5 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 42 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 42.5 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 42.9 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 3 | 次 | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 2 | 次 | 测试结果不符合规定 |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | ±0.2 | ℃ | ≥35℃且≤42℃ |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | ±0.3 | ℃ | 其它（<35℃或>42℃） |
| 设计输入汇总表E0  20211118.via_xlsx.c | ±0.2 | ℃ | ≥35℃且≤42℃ |
| 设计输入汇总表E0  20211118.via_xlsx.c | ±0.3 | ℃ | 其它（<35℃或>42℃） |

### `measurement_range` (比较方向: wider_is_better)

| 来源文件 | 值 | 单位 | 条件 |
|----------|-----|------|------|
| PT9L红外体温计检测报告 V1.0.via_lo_html | 32-42.9 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 31.6 | ℃ | 低于32℃ |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 43.4 | ℃ | 高于42.9℃ |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 32.0-42.9 | ℃ | - |
| 设计输入汇总表E0  20211118.via_xlsx.c | 32.0-42.9 | ℃ | - |

### `operating_temperature` (比较方向: wider_is_better)

| 来源文件 | 值 | 单位 | 条件 |
|----------|-----|------|------|
| PT9L红外体温计检测报告 V1.0.via_lo_html | 24-26 | ℃ | - |
| PT9L红外体温计检测报告 V1.0.via_lo_html | 23 | ℃ | - |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 10-40 | ℃ | - |
| 设计输入汇总表E0  20211118.via_xlsx.c | 10-40 | ℃ | - |

### `service_life` (比较方向: larger_is_better)

| 来源文件 | 值 | 单位 | 条件 |
|----------|-----|------|------|
| PT9L红外体温计检测报告 V1.0.via_lo_html | 5 | 年 | - |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 5 | 年 | - |
| 客户需求书E0-血压计 23.6.via_xlsx.clea | 10000 | 次 | - |
| 设计输入汇总表E0  20211118.via_xlsx.c | 5 | 年 | - |
| 设计输入汇总表E0  20211118.via_xlsx.c | 10000 | 次 | - |

### `storage_temperature` (比较方向: wider_is_better)

| 来源文件 | 值 | 单位 | 条件 |
|----------|-----|------|------|
| 客户需求书E0-血压计 23.6.via_xlsx.clea | -20.0-55.0 | ℃ | - |
| 设计输入汇总表E0  20211118.via_xlsx.c | -20.0-55.0 | ℃ | - |

---

## 三、自动检出的潜在冲突

共检出 **7** 个潜在数值差异：

**冲突 1** — `auto_shutdown_time`

| | 文件 | 值 | 条件 |
|---|------|-----|------|
| A | PT9L红外体温计检测报告 V1.0.via_lo_html.clea | 15±1 S | 测温后无操作 |
| B | 客户需求书E0-血压计 23.6.via_xlsx.clean.md | 15 秒 | - |

**冲突 2** — `measurement_range`

| | 文件 | 值 | 条件 |
|---|------|-----|------|
| A | PT9L红外体温计检测报告 V1.0.via_lo_html.clea | 32-42.9 ℃ | - |
| B | 客户需求书E0-血压计 23.6.via_xlsx.clean.md | 32.0-42.9 ℃ | - |

**冲突 3** — `measurement_accuracy`

| | 文件 | 值 | 条件 |
|---|------|-----|------|
| A | PT9L红外体温计检测报告 V1.0.via_lo_html.clea | ±0.2 ℃ | ≥35℃且≤42℃ |
| B | 客户需求书E0-血压计 23.6.via_xlsx.clean.md | ±0.3 ℃ | 其它（<35℃或>42℃） |

**冲突 4** — `measurement_accuracy`

| | 文件 | 值 | 条件 |
|---|------|-----|------|
| A | PT9L红外体温计检测报告 V1.0.via_lo_html.clea | ±0.3 ℃ | 其它（<35℃或>42℃） |
| B | 客户需求书E0-血压计 23.6.via_xlsx.clean.md | ±0.2 ℃ | ≥35℃且≤42℃ |

**冲突 5** — `operating_temperature`

| | 文件 | 值 | 条件 |
|---|------|-----|------|
| A | PT9L红外体温计检测报告 V1.0.via_lo_html.clea | 24-26 ℃ | - |
| B | 客户需求书E0-血压计 23.6.via_xlsx.clean.md | 10-40 ℃ | - |

**冲突 6** — `humidity_range`

| | 文件 | 值 | 条件 |
|---|------|-----|------|
| A | PT9L红外体温计检测报告 V1.0.via_lo_html.clea | 30-70 %RH | - |
| B | 客户需求书E0-血压计 23.6.via_xlsx.clean.md | 15-95 %RH | 不结露 |

**冲突 7** — `battery_life`

| | 文件 | 值 | 条件 |
|---|------|-----|------|
| A | PT9L红外体温计检测报告 V1.0.via_lo_html.clea | 10000 次 | - |
| B | 客户需求书E0-血压计 23.6.via_xlsx.clean.md | 1000 次 | 测量使用次数不低于 |

---

## 四、验证结论

| 验证项 | 结果 | 说明 |
|--------|------|------|
| Claim 抽取 | **PASS** | 3份文件抽出 121 个 Claim，远超目标30个 |
| 术语归一化 | **PASS** | 归一化率 56.2%，10 个 subject 跨文件对齐 |
| 跨文件对齐 | **PASS** | measurement_accuracy 等核心参数在3份文件中均被正确识别 |
| 冲突检测 | **PASS** | 自动检出 7 个数值差异 |

**总体结论：技术路线可行，可以进入 MVP 开发阶段。**
