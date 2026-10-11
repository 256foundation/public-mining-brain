# MicroBT — WhatsMiner M63 spec sheet

> Source: https://shop.whatsminer.com/products/details/57?skuId=112
> Collected: 2026-10-11
> Published: Unknown
> Registry ID: microbt-site

Captured from the server-side-rendered official MicroBT shop detail page (HTTP 200, curl --compressed, Chrome 126 UA). Cooling class: hydro (page tag "WhatsMiner Hydro-cooling M63"; official file index coolingId 13).

## Storefront banner (verbatim)

- Title: MICROBT WhatsMiner M63
- Listing type: SPOT
- Hashrate: 372T
- Power efficiency: 19.9J/TH
- Power on wall: 7402.80W
- Price/T: $8 and $25/T (two values shown; the second belongs to the Partner channel — "Partner:" label on the card)
- Warehouse: HK, USA
- Unit price: $2976

Storefront (As-Of 2026-10-11): $2,976 unit price / $8 per TH retail, $25/T partner channel (HK & USA)

## Specification tab (verbatim)

- PSU: AC380~480V, 3W+ ground, input 10kw
- Size: 86mm*483mm*663mm with handle
- Weight: Net weight:27.5kg Gross Weight:30kg
- Coolant demand per machine: About 1L
- Power Cable Model: Custom made, ≥16A
- Internet Connections: Ethernet

- Product Introduction section on page: "For more product information, please click here" (link).

## Official manual attached to the page (WhatsMinerM63_*.pdf, English edition)

- Header: WHATSMINER M63, Product Manual, October 2024 — Hydro-Cooling (Outlet temperature reaches up to 70°C)
- Power Ratio: 19.9 J/T ± 5 %
- Hashrate: 334 T –366 T ± 10 % (raw pdftotext shows "3 34 T –366 T" from a bookmark artifact; joined, cross-checked: 19.9 J/T × 350 T ≈ 6,965 W, consistent with the 10 kW input limit)
- Weight: 27.5 kg (Net), 30 kg (Gross)
- Size with Handle: 86 mm × 482.6 mm × 663 mm
- Input Voltage: AC 380 V –480 V, Input 10 kW
- Power Cable Model: Custom made, ≥ 16 A
- Coolant Demand Per Machine: About 1 L
- Internet Connections: Ethernet
- ENVIRONMENTAL PARAMETERS:
  - Liquid Temperature: ① Working temperature (inlet): 25 °C –55 °C @ normal mode, 25 °C –45 °C @ high performance mode; ② Inlet temperature control accuracy: ± 2 °C; ③ Storage and transportation temperature: -40 °C –+70 °C
  - Liquid Flow: ① Rated flow : ≥ 10 L/min; ② Flow control accuracy: ± 10 %
  - Liquid Pressure: ≤ 400 Kpa
  - Liquid Medium: Special coolant: Pure water (or distilled water) + special corrosion inhibitor + antifreeze (select a ratio according to a freezing point)
  - Liquid PH: Control range: 7 –8.7
  - Humidity: ① Working humidity: 5 % RH –85 % RH (non -condensing); ② Storage humidity: 5 % RH –95 % RH (non -condensing); ③ Long -term storage humidity: 30 % RH –69 % RH (non -condensing)
- The manual has NO Power On Wall row; only "Input 10 kW". Power on wall appears only on the shop banner (7402.80W).
- Performance page marked "Prototype data for reference only."

Attachment links on page (page meta: "Created April 21,2025 — 0.58MB"):
- English: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/WhatsMinerM63_1766127870170.pdf
- Chinese: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/%E7%A5%9E%E9%A9%ACM63_1766127876288.pdf
- Older generic manual also linked from the page: https://aws-microbt-com-bucket.s3.us-west-2.amazonaws.com/1703829876206whatsminer%20product%20manual.pdf

## Gaps / notes

- No noise figure is stated anywhere (no noise data).
- The served HTML contains two literal "No data" strings inside hidden el-select dropdown empty-state templates; the visible banner stats are complete.
- Shop banner 372T sits above the manual range top (334 T –366 T ± 10 % ⇒ up to ~402 T at +10 %); shop Power on wall 7402.80W = 372T × 19.9 J/T exactly.
- Page tag verbatim: "WhatsMiner M63 360T" (tag says 360T while banner shows 372T; both preserved).
