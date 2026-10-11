# MicroBT — WhatsMiner M6AS+ spec sheet

> Source: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM6AS%2B_1778122976176.pdf
> Collected: 2026-10-11
> Published: Unknown
> Registry ID: microbt-site

Official spec-sheet PDF (Chinese edition 神马M6AS+; cover dated April 2026 — "2026年4月"). Resolved via GET https://www.whatsminer.com/renren-fast/app/v2/presales/downloadFile?id=82&type=product from the official file index (getFileProductList: fileNameEn "WhatsMinerM6AS+.pdf", fileNameCn "神马M6AS+.pdf", tag 最新, coolingId 13 hydro, created 2026-05-07 11:03:03). HTTP 200. pdftotext -layout; form-feed and bookmark artifacts cleaned (digit splits such as "2 8.5kg" joined; cross-check: 17 J/T × 420 T midpoint = 7,140 W). Not retail-listed on shop.whatsminer.com as of 2026-10-11 — no storefront price. Cooling class: hydro (水冷（出水温度达 70°C） — water cooling, outlet temperature up to 70 °C; coolingId 13).

## 规格 / Specification (verbatim values)

- 功耗比 / Power Ratio: 17J/T ±5%
- 算力 / Hashrate: 390T～450T ±10%
- 重量 / Weight: 28.5kg （净重量/net）; 31kg （毛重量/gross）
- 尺寸（带把手） / Size (with handle): 86mm×482.6mm×663mm (as printed — dimension order differs from the M7AS sheets, same physical dims)
- 输入电压 / Input voltage: AC380V～480V — 输入 10kW (input 10 kW)
- 电源线型号 / Power cable model: 定制，≥16A (custom made, ≥16A)
- 冷却液需求量（单台服务器） / Coolant demand per machine: 约 1.3L (about 1.3 L)
- 网络连接 / Network connections: 以太网 (Ethernet)
- The manual has NO 功率 (Power on wall) row — only "输入 10kW". No power-on-wall figure in this edition (gap).

## 环境参数 / Environmental parameters (verbatim values)

- 液体温度 / Liquid temperature: ① 工作温度（进液）25°C～55°C@正常模式，25°C～45°C@高性能模式; ② 进液温度控制精度：±2°C; ③ 储运温度：-40°C～+70°C
- 液体流量 / Liquid flow: ① 额定流量：≥10L/min; ② 流量控制精度：±10%
- 液体压力 / Liquid pressure: ≤400Kpa
- 液体介质 / Liquid medium: 专用冷却液：纯水（或蒸馏水）+专用缓蚀剂+防冻液（根据冰点选择配比）
- 液体PH: 控制范围：7～8.7
- 湿度 / Humidity: ① 工作湿度：5%RH～85%RH（无冷凝）; ② 存储湿度：5%RH～95%RH（无冷凝）; ③ 长期存储湿度：30%RH～69%RH（无冷凝）

## Gaps / notes

- No 功率 (Power on wall) row in the manual (gap; only 输入 10kW).
- No noise figure is stated (no noise data).
- The downloadFile endpoint serves the Chinese edition only.
- Document footer: 深圳比特微电子科技有限公司 (Shenzhen MicroBT Electronics Technology Co.,Ltd.), www.whatsminer.com. Performance page: "样机数据仅供参考。"
