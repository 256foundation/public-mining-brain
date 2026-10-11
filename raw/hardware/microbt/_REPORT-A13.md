# Capture report — MicroBT current-gen SKU completion (capture-loop A13)

> Collected: 2026-10-11

Mission: capture detailed spec sheets for current-gen WhatsMiner SKUs lacking articles — 8 retail shop detail pages (SSR route, proven in A7/A12) and 17 official spec-file PDFs for SKUs not retail-listed. All 25 target SKUs were captured; 0 failures. All files in `raw/hardware/microbt/`, one per SKU, named `2026-10-11-microbt-site-<slug>.md`.

## Per-file table

| File | Model | Route | HTTP | Bytes |
|---|---|---|---|---|
| 2026-10-11-microbt-site-m60s-plus-plus.md | M60S++ | shop (pid 74 / skuId 169) | 200 | 2,737 |
| 2026-10-11-microbt-site-m63s-plus-plus.md | M63S++ | shop (pid 75 / skuId 170) + PDF id 27 | 200 / 200 | 4,265 |
| 2026-10-11-microbt-site-m60s-plus.md | M60S+ | shop (pid 71 / skuId 154) + PDF id 42 | 200 / 200 | 2,779 |
| 2026-10-11-microbt-site-m66.md | M66 | shop (pid 68 / skuId 134) | 200 | 2,984 |
| 2026-10-11-microbt-site-m63s.md | M63S | shop (pid 67 / skuId 132) | 200 | 2,026 |
| 2026-10-11-microbt-site-m63.md | M63 | shop (pid 57 / skuId 112) | 200 | 3,753 |
| 2026-10-11-microbt-site-m60s.md | M60S | shop (pid 66 / skuId 188) | 200 | 2,483 |
| 2026-10-11-microbt-site-m60.md | M60 | shop (pid 65 / skuId 166) | 200 | 2,425 |
| 2026-10-11-microbt-site-m73s-plus.md | M73S+ | PDF id 77 | 200 | 3,199 |
| 2026-10-11-microbt-site-m73s.md | M73S | PDF id 76 | 200 | 2,725 |
| 2026-10-11-microbt-site-m70.md | M70 | PDF id 72 | 200 | 1,882 |
| 2026-10-11-microbt-site-m70s-plus.md | M70S+ | PDF id 74 | 200 | 1,966 |
| 2026-10-11-microbt-site-m76s-plus.md | M76S+ | PDF id 80 | 200 | 2,760 |
| 2026-10-11-microbt-site-m76s.md | M76S | PDF id 79 | 200 | 2,563 |
| 2026-10-11-microbt-site-m76.md | M76 | PDF id 78 | 200 | 2,560 |
| 2026-10-11-microbt-site-m7bs-plus.md | M7BS+ | PDF id 91 | 200 | 2,978 |
| 2026-10-11-microbt-site-m7bs.md | M7BS | PDF id 90 | 200 | 2,818 |
| 2026-10-11-microbt-site-m7b.md | M7B | PDF id 89 | 200 | 2,803 |
| 2026-10-11-microbt-site-m6bs-plus-plus.md | M6BS++ | PDF id 88 | 200 | 2,787 |
| 2026-10-11-microbt-site-m6bs-plus.md | M6BS+ | PDF id 87 | 200 | 2,838 |
| 2026-10-11-microbt-site-m7as-plus.md | M7AS+ | PDF id 86 | 200 | 2,967 |
| 2026-10-11-microbt-site-m7as.md | M7AS | PDF id 85 | 200 | 2,684 |
| 2026-10-11-microbt-site-m7a.md | M7A | PDF id 84 | 200 | 2,707 |
| 2026-10-11-microbt-site-m6as-plus-plus.md | M6AS++ | PDF id 83 | 200 | 2,982 |
| 2026-10-11-microbt-site-m6as-plus.md | M6AS+ | PDF id 82 | 200 | 2,852 |

Every shop GET and every downloadFile/PDF GET returned HTTP 200 on first attempt. Total: 25 files, ~68.3 KB.

## Which models came from where

- **Shop detail pages only (6):** M60S++, M66, M63S, M63, M60S, M60 — SSR pages with the full spec tab; 5 of the 6 also carry an on-page "Attachment download" English manual (all missing on M63S).
- **Shop detail page + official file index supplement (2):** M63S++ and M60S+ have NO attachment section on their shop pages, so their spec sheets were pulled from the official file index (`downloadFile?id=27` / `id=42`) and folded into the shop-sourced file. These are the only shop-group files whose supplement is a Chinese edition.
- **Official spec-file PDFs only (17):** M73S+, M73S, M70, M70S+, M76S+, M76S, M76, M7BS+, M7BS, M7B, M6BS++, M6BS+, M7AS+, M7AS, M7A, M6AS++, M6AS+ — none are retail-listed on shop.whatsminer.com (no storefront price; each file states this).

## Cooling class per SKU

- **Air (coolingId 12):** M60S++, M60S+, M60S, M60, M70, M70S+ — manuals say "Air Cooling"/"风冷"; air units 350CFM, AC220–240V (shop PSU lines "P221B/P222B AC220V ~ 240V"), IEC C19 ≥16A, 430mm×155mm×226mm, 11.5/12.6 kg per manual (shop tabs say "13.5KG").
- **Hydro (coolingId 13):** M63, M63S, M63S++, M73S+, M73S, M7BS+, M7BS, M7B, M6BS++, M6BS+, M7AS+, M7AS, M7A, M6AS++, M6AS+ — manuals "水冷"; two hydro generations are visible: 70 °C-outlet class (M63/M63S/M63S++, M73S family, M7AS family, M6AS family) and a 90 °C-outlet class (M7B/M6B family, Feb 2026 manuals, with ④ max inlet–outlet Δ 40 °C and ⑤ outlet ≤90 °C rows).
- **Immersion/oil (coolingId 14):** M66, M76S+, M76S, M76 — M66 manual "Immersion Cooling" (insulating liquid S5X/S3X, ≥24 L/min); M76 family manuals say "油冷" (oil cooling) though the index classes them coolingId 14, same S5X/S3X medium and ≥24 L/min.

## Key spec literals (exact quotes)

Shop group (banner / spec tab, verbatim):

- M60S++: "218T" / "15.5J/TH" / "Power on wall 3379.00W" / "Price/T $10" / "$2180"; tab: "Working Temperature -5° C ~ 35° C", "Size 430mm*155mm*226mm", "Weight 13.5KG", "PSU Model P221B/P222B AC220V ~ 240V", "IEC C19, ≥16A". Manual (En, Dec 2024): "Power Ratio 15.5 J/T ± 5 % @ 25 °C", "Hashrate 200 T –226 T ± 5 %", "Power On Wall 3230 W –3570 W ± 10 %", "Air Flow 350 CFM", "Input Voltage AC 220 V –240 V", "11.5 kg (Net) / 12.6 kg (Gross)".
- M63S++: "464T" / "15.5J/TH" / "7192.00W" / "$10" / "$4640" / "please contact onlineorder@microbt.com."; tab: "PSU AC380~480V, 3W+ ground, input 10kw", "Size 86mm*483mm*663mm with handle", "Net weight:29.5kg Gross Weight:32kg", "Coolant demand per machine About 1L". Supplement (Cn, Dec 2024): "15.5J/T±5%", "434T～478T ±10%", "AC380V～480V 输入 10kW", "≥10L/min", "≤400Kpa", "液体PH 控制范围：7～8.7"; no 功率 row.
- M60S+: "200T" / "17J/TH" / "3400.00W" / "$16" / "$3200"; tab: same air spec block as M60S++. Supplement (Cn, Oct 2024): "17J/T ±5%@25°C", "190T～210T ±5%", "墙上功率 3230W～3570W ±10%" (older manuals label power-on-wall 墙上功率), "AC220V～240V", "350CFM".
- M66: "276T" / "19.9J/TH" / "5492.40W" / "$8" / "$2208"; tab: "PSU AC380~480V", "Size 267.5mmX147mmX401mm with handle", "Net weight: 16kg Weight with packaging materials: 17kg", "Custom made，≥16A" (full-width comma preserved). Manual (En, Oct 2024): "19.9 J/T ± 5 %", "240 T –276 T ± 10 %", "Rated flow : ≥ 24 L/min", "Insulating liquid (S5X/S3X)"; no Power On Wall row in manual.
- M63S: "408T" / "18J/T" / "7344.00W" / "$9 + $28/T" / "$3672"; tab: "AC380~480V, 3W+ ground, input 10kw", "86mm*483mm*663mm with handle", "Net weight:27.5kg Gross Weight:30kg", "Coolant demand per machine About 1L".
- M63: "372T" / "19.9J/TH" / "7402.80W" / "$8 + $25/T" / "$2976"; tab: same hydro block; tag "WhatsMiner M63 360T". Manual (En, Oct 2024): "19.9 J/T ± 5 %", "Hashrate 334 T –366 T ± 10 %" (bookmark-split "3 34 T" joined), "86 mm × 482.6 mm × 663 mm", "Rated flow : ≥ 10 L/min", "Liquid Pressure ≤ 400 Kpa", "Liquid PH Control range: 7 –8.7", "Hydro-Cooling (Outlet temperature reaches up to 70°C)"; no Power On Wall row in manual.
- M60S: hashrate select "188T / 186T / 184T" each at "18.5J/TH"; "Power on wall 3478.00W" / "$9" / "$1692". Manual (En, Oct 2024): "18.5 J/T ± 5 % @ 25 °C", "170 T –186 T ± 5 %", "Power On Wall 3145 W –3441 W ± 10 %", "350 CFM".
- M60: "160T" / "19.9J/TH" / "3184.00W" / "$8" / "$1280". Manual (En, Oct 2024): "19.9 J/T ± 5 % @ 25 °C", "150 T –172 T ± 5 %", "Power On Wall 2985 W –3422 W ± 10 %".

PDF group (Chinese editions, values verbatim; 功耗比 = power ratio, 算力 = hashrate, 功率 = power on wall):

- M73S+ (Dec 2025): "12.5J/T±5%", "540T～600T ±10%", "29.5kg（净）/32kg（毛）", "663mm×482.6mm×86mm", "AC380V～480V", "约 1L", "7200 W±10%@正常模式，10kW±10%@高性能模式", "额定流量：≥10L/min", "≤400Kpa", "PH 7～8.7".
- M73S (Dec 2025): "13.5J/T±5%", "500T～552T ±10%"; otherwise identical to M73S+.
- M70 (Dec 2025, 风冷): "14.5J/T±5%@25°C", "214T～236T ±5%", "11.5/12.6kg", "430mm×155mm×226mm", "-5°C～+35°C", "350CFM", "3140 W ～3500 W ±10%", "AC220V～240V", "IEC C19，≥16A".
- M70S+ (Dec 2025, 风冷): "12.5J/T±5%@25°C", "244T～280T ±5%"; otherwise identical to M70.
- M76S+ (Dec 2025, 油冷): "12.5J/T±5%", "390T～440T ±10%", "18/19kg", "401mm×267.5mm×147mm", "AC380V～480V", "5200W ±10%@正常模式；7000W ±10%@高性能模式", "额定流量：≥24 L/min", "绝缘液（S5X/S3X）".
- M76S: "13.5J/T±5%", "362T～406T ±10%". M76: "14.5J/T±5%", "336T～374T ±10%"; both otherwise identical to M76S+.
- M7BS+ / M7BS / M7B (Feb 2026, 水冷 90 °C outlet): "12.5 / 13.5 / 14.5J/T±5%", "540T～600T / 500T～552T / 470T～526T ±10%", "28.5/31kg", "663mm×482.6mm×86mm", "约 1.3L", "7200 W±10%@正常模式，10kW±10%@高性能模式", inlet "25°C～60°C@正常模式，25°C～50°C@高性能模式", "最大进出口液体温差：40°C", "出口液体温度：≤90°C", "≤400Kpa", "PH 7～8.7". All three omit the 液体流量 (rated flow) row.
- M6BS++ / M6BS+ (Feb 2026, 水冷 90 °C outlet): "15.5 / 17J/T±5%", "434T～478T / 390T～450T ±10%"; same chassis/environmental block as M7BS family; also omit the 液体流量 row.
- M7AS+ / M7AS / M7A (Apr 2026, 水冷 70 °C outlet): "12.5 / 13.5 / 14.5J/T±5%", same hashrate/weight/size/power rows as the M7BS twins, "约 1.3L", inlet "25°C～55°C@正常模式，25°C～45°C@高性能模式", "额定流量：≥10L/min", "≤400Kpa", "PH 7～8.7".
- M6AS++ / M6AS+ (Apr 2026, 水冷 70 °C outlet): "15.5 / 17J/T±5%", "434T～478T / 390T～450T ±10%", "28.5/31kg", "86mm×482.6mm×663mm" (order as printed), "AC380V～480V 输入 10kW", "约 1.3L", "≥10L/min", "≤400Kpa", "PH 7～8.7". Both omit the 功率 (power-on-wall) row.

## Gaps / failures

- **No failures.** All 25 SKUs resolved; no model in the A13 list is missing from the official file index, and no PDF download failed.
- **Noise:** no noise figure exists in any captured source (shop pages or manuals) for any of the 25 SKUs — noted per file.
- **"No data" strings:** every shop page's served HTML contains two literal "No data" strings, but all of them live inside hidden el-select dropdown empty-state templates (el-popper containers), not in the visible stats. After stripping the popper containers, zero "No data" occurrences remain — no visible stat is missing on any of the 8 pages. (This also retroactively explains the A12 note "M70S Power on wall shows No data".)
- **M63S shop page has no attachment/manual section** — recorded in its file; official index entry WhatsMinerM63S.pdf (id 29) exists but was out of the A13 group-2 list and not downloaded.
- **Manual rows missing per edition:** M63 (En) and M66 (En) manuals have no Power On Wall row (shop banner supplies it); M63S++/M60S+/M6AS++/M6AS+ supplements have no 功率 row; the entire M7B/M6B "90 °C" family omits the liquid-flow row.
- **Edition language:** the official `downloadFile` endpoint serves the Chinese (神马/Shenma) edition for every group-2 id regardless of Accept-Language; English S3 object names exist in the index metadata (fileNameEn) but are not resolvable (bucket listing returns 403, no untimestamped object names). Values were captured verbatim with English glosses.
- **Shop-vs-manual discrepancies preserved (not reconciled):** shop tabs say "Weight: 13.5KG" for M60S++/M60S+/M60S/M60 while manuals say 11.5/12.6 kg; M60S++ banner 218T vs manual 200–226T; M63 banner 372T vs manual 334–366T (372 × 19.9 = 7,402.8 W matches the shop power-on-wall exactly); M60S banner 188T vs manual 170–186T band with 3478.00W slightly above the manual's 3441 W max (inside ±10 %).
- **Out of scope, untouched:** M66S/M66S+/M63S+/M64/M65S/M70S/M73 (existing articles), M50/M30/M53/M54/M56 series, M6DS/M7DS.

## Method notes

- Shop route: `curl --compressed` with Chrome 126 UA against `https://shop.whatsminer.com/products/details/<pid>?skuId=<sid>`; the shop is Nuxt SSR so the full product data is in the HTML. 8 pages fetched sequentially, `sleep 1.2` between requests (≤1 req/s). Text extracted by stripping `<script>/<style>`, comments, and tags, then `html.unescape`; hidden `el-popper`/`el-popper-container` blocks stripped separately to test which "No data" strings are visible.
- PDF route: `GET /renren-fast/app/v2/presales/getFileProductList` (JSON, code 1, 50 entries) → matched each of the 17 target models by fileNameEn → `GET .../downloadFile?id=<fileId>&type=product` returns `{"data": "<S3 url>"}` → PDF downloaded from `aws-microbt-com-bucket.s3.us-west-2.amazonaws.com` → `pdftotext -layout` → form-feed and PDF-bookmark artifacts cleaned. Bookmark codes split some digits (e.g. "1 2.5J/T±5%", "2 8.5kg", "3 140 W ～35 00 W"); every join was cross-checked arithmetically against the 功率/功耗比 rows (e.g. 12.5 J/T × 576 T ≈ 7,200 W). Rate limit: ~1.1 s between all whatsminer.com and S3 requests.
- Two gap-fill supplements (M63S++ id 27, M60S+ id 42) were resolved+downloaded the same way and folded into their shop-group files with the resolved URLs recorded.
- Storefront prices captured as the single dated line `Storefront (As-Of 2026-10-11): ...` in shop-group files; PDF-group files state "Not retail-listed ... no storefront price".

## Final file list (raw/hardware/microbt/)

| File | Bytes |
|---|---|
| 2026-10-11-microbt-site-m60.md | 2,425 |
| 2026-10-11-microbt-site-m60s-plus-plus.md | 2,737 |
| 2026-10-11-microbt-site-m60s-plus.md | 2,779 |
| 2026-10-11-microbt-site-m60s.md | 2,483 |
| 2026-10-11-microbt-site-m63.md | 3,753 |
| 2026-10-11-microbt-site-m63s-plus-plus.md | 4,265 |
| 2026-10-11-microbt-site-m63s.md | 2,026 |
| 2026-10-11-microbt-site-m66.md | 2,984 |
| 2026-10-11-microbt-site-m6as-plus-plus.md | 2,982 |
| 2026-10-11-microbt-site-m6as-plus.md | 2,852 |
| 2026-10-11-microbt-site-m6bs-plus-plus.md | 2,787 |
| 2026-10-11-microbt-site-m6bs-plus.md | 2,838 |
| 2026-10-11-microbt-site-m70.md | 1,882 |
| 2026-10-11-microbt-site-m70s-plus.md | 1,966 |
| 2026-10-11-microbt-site-m73s-plus.md | 3,199 |
| 2026-10-11-microbt-site-m73s.md | 2,725 |
| 2026-10-11-microbt-site-m76.md | 2,560 |
| 2026-10-11-microbt-site-m76s-plus.md | 2,760 |
| 2026-10-11-microbt-site-m76s.md | 2,563 |
| 2026-10-11-microbt-site-m7a.md | 2,707 |
| 2026-10-11-microbt-site-m7as-plus.md | 2,967 |
| 2026-10-11-microbt-site-m7as.md | 2,684 |
| 2026-10-11-microbt-site-m7b.md | 2,803 |
| 2026-10-11-microbt-site-m7bs-plus.md | 2,978 |
| 2026-10-11-microbt-site-m7bs.md | 2,818 |
| **_REPORT-A13.md (this file)** | — |

25 SKU captures + 1 report. No pre-existing files (2026-10-10-*.md) were modified.
