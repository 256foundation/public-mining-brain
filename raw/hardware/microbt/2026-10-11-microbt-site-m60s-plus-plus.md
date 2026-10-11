# MicroBT — WhatsMiner M60S++ spec sheet

> Source: https://shop.whatsminer.com/products/details/74?skuId=169
> Collected: 2026-10-11
> Published: Unknown
> Registry ID: microbt-site

Captured from the server-side-rendered official MicroBT shop detail page (HTTP 200, curl --compressed, Chrome 126 UA). Cooling class: air.

## Storefront banner (verbatim)

- Title: MICROBT WhatsMiner M60S++
- Listing type: SPOT
- Hashrate (banner select, single option): 218T
- Power efficiency: 15.5J/TH
- Power on wall: 3379.00W
- Price/T: $10
- Warehouse: HK, USA
- Unit price: $2180 — "Delivery within 7 days after 100% payment"

Storefront (As-Of 2026-10-11): $2,180 unit price / $10 per TH (HK & USA warehouses)

## Specification tab (verbatim)

- Working Temperature: -5° C ~ 35° C
- Size: 430mm*155mm*226mm
- Weight: 13.5KG
- Internet Connections: Ethernet
- Power Cable Model: IEC C19, ≥16A
- PSU Model: P221B/P222B AC220V ~ 240V

## Official manual attached to the page (WhatsMinerM60S++_*.pdf, English edition)

- Header: WHATSMINER M60S++, Product Manual, December 2024 — Air Cooling
- Power Ratio: 15.5 J/T ± 5 % @ 25 °C
- Hashrate: 200 T –226 T ± 5 %
- Weight: 11.5 kg (Net), 12.6 kg (Gross)
- Size: 430 mm × 155 mm × 226 mm
- Working Temperature: -5 °C – +35 °C
- Air Flow: 350 CFM
- Power On Wall: 3230 W –3570 W ± 10 %
- Power Cable Model: IEC C19, ≥ 16 A
- Input Voltage: AC 220 V –240 V
- Internet Connections: Ethernet
- Performance page marked "Prototype data for reference only."

Attachment links on page (page meta: "Created April 21,2025 — 0.49MB"):
- English: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/WhatsMinerM60S%2B%2B_1760948259244.pdf
- Chinese: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM60S%2B%2B_1760948253449.pdf

## Gaps / notes

- No noise figure is stated on the page or in the manual (no noise data).
- The served HTML contains two literal "No data" strings, but both sit inside hidden el-select dropdown empty-state templates (el-popper containers); the visible banner stats are complete. No visible "No data" gap.
- Shop banner hashrate 218T is inside the manual range 200 T –226 T ± 5 %; shop Power on wall 3379.00W is inside the manual band 3230 W –3570 W ± 10 %.
- Shop "Weight: 13.5KG" vs manual 11.5 kg (Net) / 12.6 kg (Gross) — unexplained discrepancy between shop tab and manual; both preserved verbatim.
- Shop PSU line gives an AC220V~240V band (P221B/P222B), consistent with the manual "AC 220 V –240 V" — this SKU is not an AC380~480V unit.
- Page tags verbatim: "WhatsMiner M60S++ WhatsMiner Air Cooling M60S++ WhatsMiner M60S++ 15.5J/H Bitcoin Miner Bitcoin Mining ASIC Miner" ("15.5J/H" typo preserved).
