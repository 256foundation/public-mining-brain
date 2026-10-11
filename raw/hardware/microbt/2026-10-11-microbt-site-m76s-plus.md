# MicroBT — WhatsMiner M76S+ spec sheet

> Source: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM76S%2B_1775811809859.pdf
> Collected: 2026-10-11
> Published: Unknown
> Registry ID: microbt-site

Official spec-sheet PDF (Chinese edition 神马M76S+; cover dated December 2025 — "2025年12月"). Resolved via GET https://www.whatsminer.com/renren-fast/app/v2/presales/downloadFile?id=80&type=product from the official file index (getFileProductList: fileNameEn "WhatsMinerM76S+.pdf", fileNameCn "神马M76S+.pdf", tag 最新, coolingId 14, created 2026-04-10 17:03:43). HTTP 200. pdftotext -layout; form-feed chars cleaned. Not retail-listed on shop.whatsminer.com as of 2026-10-11 — no storefront price. Cooling class: immersion-class per the official index (coolingId 14); the manual itself says 油冷 (oil cooling).

## 规格 / Specification (verbatim values)

- 功耗比 / Power Ratio: 12.5J/T±5%
- 算力 / Hashrate: 390T～440T ±10%
- 重量 / Weight: 18 kg （净重量/net）; 19 kg （毛重量/gross）
- 尺寸（带把手） / Size (with handle): 401mm×267.5mm×147mm
- 输入电压 / Input voltage: AC380V～480V
- 电源线型号 / Power cable model: 定制，≥16A (custom made, ≥16A)
- 网络连接 / Network connections: 以太网 (Ethernet)
- 功率 / Power (on wall): 5200W ±10%@ 正常模式 (normal mode)；7000W ±10%@ 高性能模式 (high-performance mode)

## 环境参数 / Environmental parameters (verbatim values)

- 液体温度 / Liquid temperature: ① 工作温度（进液）25°C～55°C @ 正常模式，25°C～45°C @ 高性能模式; ② 进液温度控制精度：±2°C; ③ 储运温度：-40°C～+70°C
- 液体流量 / Liquid flow: ① 额定流量：≥24 L/min (rated flow ≥24 L/min); ② 流量控制精度：±10%
- 液体介质 / Liquid medium: 专用冷却液：绝缘液（S5X/S3X ） (special coolant: insulating liquid S5X/S3X)
- 湿度 / Humidity: ① 存储湿度：5%RH～95%RH（无冷凝）; ② 长期存储湿度：30 %RH～69 %RH（无冷凝）

## Gaps / notes

- No noise figure is stated in the manual (no noise data).
- No liquid-pressure row (≤400Kpa appears only in the hydro manuals) and no liquid-PH row in the M76 family manual.
- No working-humidity row (storage and long-term storage humidity only).
- No per-machine coolant demand figure (the immersion manual gives rated flow ≥24 L/min instead).
- The downloadFile endpoint serves the Chinese edition only.
- Document footer: 深圳比特微电子科技有限公司 (Shenzhen MicroBT Electronics Technology Co.,Ltd.), www.whatsminer.com. Performance page: "样机数据仅供参考。"
- Arithmetic cross-check: 12.5 J/T × 415 T midpoint = 5,187.5 W ≈ 5,200 W normal-mode rating.
