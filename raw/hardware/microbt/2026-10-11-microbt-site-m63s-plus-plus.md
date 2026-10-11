# MicroBT — WhatsMiner M63S++ spec sheet

> Source: https://shop.whatsminer.com/products/details/75?skuId=170
> Collected: 2026-10-11
> Published: Unknown
> Registry ID: microbt-site

Captured from the server-side-rendered official MicroBT shop detail page (HTTP 200, curl --compressed, Chrome 126 UA). Cooling class: hydro (page tag "WhatsMiner Hydro Cooling M63S++"; official file index coolingId 13).

## Storefront banner (verbatim)

- Title: MICROBT WhatsMiner M63S++
- Listing type: SPOT
- Hashrate: 464T
- Power efficiency: 15.5J/TH
- Power on wall: 7192.00W
- Price/T: $10
- Partner (channel label shown on the card)
- Warehouse: HK, USA
- Unit price: $4640 — "please contact onlineorder@microbt.com." ("Contact us to buy"; no direct checkout)

Storefront (As-Of 2026-10-11): $4,640 unit price / $10 per TH (HK & USA; partner channel — contact onlineorder@microbt.com)

## Specification tab (verbatim)

- PSU: AC380~480V, 3W+ ground, input 10kw
- Size: 86mm*483mm*663mm with handle
- Weight: Net weight:29.5kg Gross Weight:32kg
- Coolant demand per machine: About 1L
- Power Cable Model: Custom made, ≥16A
- Internet Connections: Ethernet

## Official spec file (page has no attachment section — gap filled from the official file index)

The shop page has NO "Attachment download" section (no manual linked). The official spec-file index (getFileProductList) lists WhatsMinerM63S++.pdf (id 27, coolingId 13, tag 最新, created 2025-04-21 14:54:18). Resolved via GET /renren-fast/app/v2/presales/downloadFile?id=27&type=product →
https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM63S%2B%2B_1766127950966.pdf (Chinese edition 神马M63S++, product manual dated December 2024, "水冷（出水温度达 70°C）" = hydro cooling, outlet temperature up to 70 °C). Verbatim values:

- 功耗比 (Power Ratio): 15.5J/T±5%
- 算力 (Hashrate): 434T～478T ±10%
- 重量 (Weight): 29.5kg （净重量/net weight）; 32kg （毛重量/gross weight）
- 尺寸（带把手）(Size with handle): 86mm×482.6mm×663mm
- 输入电压 (Input Voltage): AC380V～480V — 输入 10kW (input 10 kW)
- 电源线型号 (Power Cable Model): 定制，≥16A (custom made, ≥16A)
- 冷却液需求量（单台服务器）(Coolant demand per machine): 约 1L (about 1 L)
- 网络连接 (Internet Connections): 以太网 (Ethernet)
- The manual has NO 功率 (Power on wall) row — only "输入 10kW". No power-on-wall figure in the official PDF.
- 环境参数 (Environmental parameters): 液体温度 (liquid temperature) ①工作温度（进液）25°C～55°C@正常模式，25°C～45°C@高性能模式 (inlet 25–55 °C normal mode, 25–45 °C high-performance mode); ②进液温度控制精度：±2°C (inlet control accuracy ±2 °C); ③储运温度：-40°C～+70°C (storage/transport -40–+70 °C). 液体流量 (liquid flow) ①额定流量：≥10L/min (rated flow ≥10 L/min); ②流量控制精度：±10% (control accuracy ±10%). 液体压力 (liquid pressure): ≤400Kpa. 液体介质 (medium): 专用冷却液：纯水（或蒸馏水）+专用缓蚀剂+防冻液（根据冰点选择配比） (pure/distilled water + special corrosion inhibitor + antifreeze, ratio per freezing point). 液体PH: 控制范围：7～8.7 (control range 7–8.7). 湿度 (humidity): ①工作湿度：5%RH～85%RH（无冷凝）working 5–85 %RH non-condensing; ②存储湿度：5%RH～95%RH storage; ③长期存储湿度：30%RH～69%RH long-term storage.
- Performance page marked "样机数据仅供参考。" (prototype data for reference only).

## Gaps / notes

- No noise figure is stated anywhere (no noise data).
- The page's "Attachment download" tab is absent — no manual is linked from the shop page itself; the spec sheet above comes from the official file index (noted on the page as a gap and filled externally).
- The served HTML contains two literal "No data" strings inside hidden el-select dropdown empty-state templates; the visible banner stats are complete.
- Page title typo preserved: "WhatsMiner.com | Offical Website".
- pdftotext bookmark artifacts split some digits in the raw extraction (e.g. "2 9.5kg"); joins cross-checked against arithmetic (29.5 kg net / 32 kg gross matches the shop tab).
