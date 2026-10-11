# MicroBT — WhatsMiner M60S+ spec sheet

> Source: https://shop.whatsminer.com/products/details/71?skuId=154
> Collected: 2026-10-11
> Published: Unknown
> Registry ID: microbt-site

Captured from the server-side-rendered official MicroBT shop detail page (HTTP 200, curl --compressed, Chrome 126 UA). Cooling class: air (page tag "WhatsMiner Air Cooling M60S+"; official file index coolingId 12).

## Storefront banner (verbatim)

- Title: MICROBT WhatsMiner M60S+
- Listing type: SPOT
- Hashrate: 200T
- Power efficiency: 17J/TH
- Power on wall: 3400.00W
- Price/T: $16
- Warehouse: HK, USA
- Unit price: $3200 — "Delivery within 7 days after 100% payment"

Storefront (As-Of 2026-10-11): $3,200 unit price / $16 per TH (HK & USA warehouses)

## Specification tab (verbatim)

- Working Temperature: -5° C ~ 35° C
- Size: 430mm*155mm*226mm
- Weight: 13.5KG
- Internet Connections: Ethernet
- Power Cable Model: IEC C19, ≥16A
- PSU Model: P221B/P222B AC220V ~ 240V

## Official spec file (page has no attachment section — gap filled from the official file index)

The shop page has NO "Attachment download" section (no manual linked). The official spec-file index (getFileProductList) lists WhatsMinerM60S+.pdf (id 42, coolingId 12, tag 最新, created 2025-10-20 16:25:52). Resolved via GET /renren-fast/app/v2/presales/downloadFile?id=42&type=product →
https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM60S%2B_1760948744068.pdf (Chinese edition 神马M60S+, product manual dated October 2024, "风冷" = air cooling). Values:

- 功耗比 (Power Ratio): 17J/T ±5%@25°C
- 算力 (Hashrate): 190T～210T ±5%
- 重量 (Weight): 11.5kg （净重量/net）; 12.6kg （毛重量/gross）
- 尺寸 (Size): 430mm×155mm×226mm
- 工作温度 (Working temperature): -5°C～+35°C
- 风量 (Air flow): 350CFM
- 墙上功率 (Power on wall — this older manual uses the label 墙上功率): 3230W～3570W ±10%
- 电源线型号 (Power cable): IEC C19，≥16A
- 输入电压 (Input voltage): AC220V～240V
- 网络连接 (Network): 以太网 (Ethernet)
- Performance page marked "样机数据仅供参考。" (prototype data for reference only).

## Gaps / notes

- No noise figure is stated anywhere (no noise data).
- No "Attachment download" section on the shop page; official spec sheet obtained via the file index instead.
- The served HTML contains two literal "No data" strings inside hidden el-select dropdown empty-state templates; the visible banner stats are complete.
- Shop "Weight: 13.5KG" vs manual 11.5 kg net / 12.6 kg gross — discrepancy between shop tab and manual; both preserved.
- Shop Power on wall 3400.00W falls inside the manual band 3230W～3570W ±10%.
- AC220V~240V input band (P221B/P222B PSU), not AC380~480V.
