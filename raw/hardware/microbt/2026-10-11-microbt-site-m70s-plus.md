# MicroBT — WhatsMiner M70S+ spec sheet

> Source: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM70S%2B_1775811518058.pdf
> Collected: 2026-10-11
> Published: Unknown
> Registry ID: microbt-site

Official spec-sheet PDF (Chinese edition 神马M70S+; cover dated December 2025 — "2025年12月"). Resolved via GET https://www.whatsminer.com/renren-fast/app/v2/presales/downloadFile?id=74&type=product from the official file index (getFileProductList: fileNameEn "WhatsMinerM70S+.pdf", fileNameCn "神马M70S+.pdf", tag 最新, coolingId 12 air, created 2026-04-10 16:58:40). HTTP 200. pdftotext -layout; form-feed and bookmark artifacts cleaned (digit splits such as "2 44T ～280 T" joined → 244T～280T). Not retail-listed on shop.whatsminer.com as of 2026-10-11 — no storefront price. Cooling class: air (风冷; coolingId 12).

## 规格 / Specification (verbatim values)

- 功耗比 / Power Ratio: 12.5J/T±5%@25°C
- 算力 / Hashrate: 244T～280T ±5%
- 重量 / Weight: 11.5kg （净重量/net）; 12.6kg （毛重量/gross）
- 尺寸 / Size: 430mm×155mm×226mm
- 工作温度 / Working temperature: -5°C～+35°C
- 风量 / Air flow: 350CFM
- 功率 / Power (on wall): 3140 W ～3500 W ±10%
- 电源线型号 / Power cable model: IEC C19，≥16A
- 输入电压 / Input voltage: AC220V～240V
- 网络连接 / Network connections: 以太网 (Ethernet)

## Gaps / notes

- No noise figure is stated in the manual (no noise data) — only the 350CFM air-flow figure.
- The downloadFile endpoint serves the Chinese edition only.
- Document footer: 深圳比特微电子科技有限公司 (Shenzhen MicroBT Electronics Technology Co.,Ltd.), www.whatsminer.com. Performance page: "样机数据仅供参考。"
- Arithmetic cross-check: 12.5 J/T × 262 T midpoint = 3,275 W, inside the 3140–3500 W band.
- Note: the retail shop catalog separately lists an M70S (248TH / 13.5J/TH card) — distinct SKU from this M70S+.
