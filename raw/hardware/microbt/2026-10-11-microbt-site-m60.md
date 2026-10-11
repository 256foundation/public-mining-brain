# MicroBT — WhatsMiner M60 spec sheet

> Source: https://shop.whatsminer.com/products/details/65?skuId=166
> Collected: 2026-10-11
> Published: Unknown
> Registry ID: microbt-site

Captured from the server-side-rendered official MicroBT shop detail page (HTTP 200, curl --compressed, Chrome 126 UA). Cooling class: air (official file index coolingId 12).

## Storefront banner (verbatim)

- Title: MICROBT WhatsMiner M60
- Listing type: SPOT
- Hashrate: 160T
- Power efficiency: 19.9J/TH
- Power on wall: 3184.00W
- Price/T: $8
- Warehouse: HK, USA
- Unit price: $1280 — "Delivery within 7 days after 100% payment"

Storefront (As-Of 2026-10-11): $1,280 unit price / $8 per TH (HK & USA warehouses)

## Specification tab (verbatim)

- Working Temperature: -5° C ~ 35° C
- Size: 430mm*155mm*226mm
- Weight: 13.5KG
- Internet Connections: Ethernet
- Power Cable Model: IEC C19, ≥16A
- PSU Model: P221B/P222B AC220V ~ 240V

## Official manual attached to the page (WhatsMinerM60_*.pdf, English edition)

- Header: WHATSMINER M60, Product Manual, October 2024 — Air Cooling
- Power Ratio: 19.9 J/T ± 5 % @ 25 °C
- Hashrate: 150 T –172 T ± 5 %
- Weight: 11.5 kg (Net), 12.6 kg (Gross)
- Size: 430 mm × 155 mm × 226 mm
- Working Temperature: -5 °C –+35 °C
- Air Flow: 350 CFM
- Power On Wall: 2985 W –3422 W ± 10 %
- Power Cable Model: IEC C19, ≥ 16 A
- Input Voltage: AC 220 V –240 V
- Internet Connections: Ethernet
- Performance page marked "Prototype data for reference only."

Attachment links on page (page meta: "Created April 21,2025 — 0.47MB"):
- English: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/WhatsMinerM60_1760948365793.pdf
- Chinese: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM60_1760948359225.pdf

## Gaps / notes

- No noise figure is stated anywhere (no noise data).
- The served HTML contains two literal "No data" strings inside hidden el-select dropdown empty-state templates; the visible banner stats are complete.
- Shop banner 160T inside manual range 150 T –172 T ± 5 %; shop Power on wall 3184.00W inside manual band 2985 W –3422 W ± 10 %.
- Shop "Weight: 13.5KG" vs manual 11.5 kg net / 12.6 kg gross — discrepancy; both preserved.
- AC220V~240V input band (P221B/P222B PSU), not AC380~480V.
- Page <title> verbatim: "Bitcoin Miner-WhatsMiner M60 - MicroBT Makes Perfect" (differs from the standard title pattern).
