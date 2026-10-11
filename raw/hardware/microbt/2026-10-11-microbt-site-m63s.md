# MicroBT — WhatsMiner M63S spec sheet

> Source: https://shop.whatsminer.com/products/details/67?skuId=132
> Collected: 2026-10-11
> Published: Unknown
> Registry ID: microbt-site

Captured from the server-side-rendered official MicroBT shop detail page (HTTP 200, curl --compressed, Chrome 126 UA). Cooling class: hydro (page tag "WhatsMiner Hydro Cooling M63S"; official file index coolingId 13).

## Storefront banner (verbatim)

- Title: MICROBT WhatsMiner M63S
- Listing type: SPOT
- Hashrate: 408T
- Power efficiency: 18J/T (as printed on the banner; "J/T" not "J/TH")
- Power on wall: 7344.00W
- Price/T: $9 and $28/T (two values shown; the second belongs to the Partner channel — "Partner:" label on the card)
- Warehouse: HK, USA
- Unit price: $3672

Storefront (As-Of 2026-10-11): $3,672 unit price / $9 per TH retail, $28/T partner channel (HK & USA)

## Specification tab (verbatim)

- PSU: AC380~480V, 3W+ ground, input 10kw
- Size: 86mm*483mm*663mm with handle
- Weight: Net weight:27.5kg Gross Weight:30kg
- Coolant demand per machine: About 1L
- Power Cable Model: Custom made, ≥16A
- Internet Connections: Ethernet

## Gaps / notes

- No noise figure is stated anywhere (no noise data).
- The shop page has NO "Attachment download" section (no manual linked) — recorded as a gap. The official file index does list WhatsMinerM63S.pdf (id 29, coolingId 13, created 2025-04-21); that file was not part of the A13 group-2 capture list and was not downloaded.
- No official spec-sheet section in this capture beyond the shop tab above; per-machine coolant "About 1L" is stated but no rated flow/pressure figure appears on the shop page (no flow data in this capture).
- The served HTML contains two literal "No data" strings inside hidden el-select dropdown empty-state templates; the visible banner stats are complete.
- Shop banner 408T; shop Power on wall 7344.00W = 408T × 18 J/T exactly.
- Page tags verbatim: "ASIC Miner WhatsMiner M63S WhatsMiner Hydro Cooling M63S Bitcoin Miner Bitcoin Mining".
