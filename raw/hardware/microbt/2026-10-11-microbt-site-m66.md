# MicroBT — WhatsMiner M66 spec sheet

> Source: https://shop.whatsminer.com/products/details/68?skuId=134
> Collected: 2026-10-11
> Published: Unknown
> Registry ID: microbt-site

Captured from the server-side-rendered official MicroBT shop detail page (HTTP 200, curl --compressed, Chrome 126 UA). Cooling class: immersion (page tag "WhatsMiner Immersion Cooling M66"; official file index coolingId 14).

## Storefront banner (verbatim)

- Title: MICROBT WhatsMiner M66
- Listing type: SPOT
- Hashrate: 276T
- Power efficiency: 19.9J/TH
- Power on wall: 5492.40W
- Price/T: $8
- Partner (channel label shown on the card)
- Warehouse: HK, USA
- Unit price: $2208

Storefront (As-Of 2026-10-11): $2,208 unit price / $8 per TH (HK & USA warehouses)

## Specification tab (verbatim)

- PSU: AC380~480V
- Size: 267.5mmX147mmX401mm with handle
- Weight: Net weight: 16kg Weight with packaging materials: 17kg
- Power Cable Model: Custom made，≥16A (full-width comma as printed)
- Internet Connections: Ethernet

## Official manual attached to the page (WhatsMinerM66_*.pdf, English edition)

- Header: WHATSMINER M66, Product Manual, October 2024 — Immersion Cooling
- Power Ratio: 19.9 J/T ± 5 %
- Hashrate: 240 T –276 T ± 10 %
- Weight: 16 kg (Net), 17 kg (Gross)
- Size with Handle: 267.5 mm × 147 mm × 401 mm
- Input Voltage: AC 380 V – 480 V
- Power Cable Model: Custom made, ≥ 16 A
- Internet Connections: Ethernet
- ENVIRONMENTAL PARAMETERS:
  - Liquid Temperature: ① Working temperature (inlet): 25 °C –55 °C @ normal mode, 25 °C –45 °C @ high performance mode; ② Inlet temperature control accuracy: ± 2 °C; ③ Storage and transportation temperature: -40 °C –+70 °C
  - Liquid Flow: ① Rated flow : ≥ 24 L/min; ② Flow control accuracy: ± 10 %
  - Liquid Medium: Special coolant: Insulating liquid (S5X/S3X)
  - Humidity: ① Storage humidity: 5 % RH –95 % RH (non -condensing); ② Long -term storage humidity: 30 % RH –69 % RH (non -condensing)
- The manual has NO Power On Wall row (immersion edition); power on wall appears only on the shop banner (5492.40W).
- Performance page marked "Prototype data for reference only."

Attachment links on page (page meta: "Created April 21,2025 — 0.62MB"):
- English: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/WhatsMinerM66_1760947600855.pdf
- Chinese: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM66_1760947606205.pdf

## Gaps / notes

- No noise figure is stated anywhere (no noise data).
- No coolant demand ("About xL") figure for M66 on either source — the immersion manual gives rated flow ≥ 24 L/min instead; no per-machine coolant volume stated.
- The served HTML contains two literal "No data" strings inside hidden el-select dropdown empty-state templates; the visible banner stats are complete.
- Shop banner 276T matches the manual range top (240 T –276 T ± 10 %).
- Shop Power on wall 5492.40W = 276T × 19.9 J/T exactly.
