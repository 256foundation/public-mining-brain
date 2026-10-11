# Capture report — Bitmain current-gen SKU completion (capture-loop A13)

> Collected: 2026-10-11
> Scope: the 7 live-catalog Bitmain SHA256 SKUs that had catalog rows but no dedicated spec page after A7 (12-SKU live catalog of 2026-10-10); registry bitmain-site
> Method: same API trio as A7 — `getMainProductsWithFilter` (catalog) → `getDetail` (listing rows) → `getDetailMoreInfo` (Specifications/Performance/Warranty HTML) — via `curl --compressed`, Chrome 126 UA, sleep 1.05 s between calls. HTML stripped to text with tables rendered as markdown rows; automated post-check confirmed every table cell, paragraph, image URL and link href from the served HTML appears in the output files (0 missing across all 7).
> Files: 7 (one per SKU), all new; `_REPORT.md` and the 2026-10-10-* files untouched.

## Per-file capture table

| File | Model (API `name`) | productId | HTTP | Size (bytes) |
|---|---|---|---|---|
| 2026-10-11-bitmain-site-s21j-xp-hyd.md | Bitcoin Miner S21j XP Hyd. | 00020251222142202843CFQByJe40662 | 200 (all 3 endpoints) | 5053 |
| 2026-10-11-bitmain-site-u3s21exph.md | Bitcoin Miner U3S21EXPH | 00020260810155841382oE3e7NdL0679 | 200 (all 3 endpoints) | 5036 |
| 2026-10-11-bitmain-site-s21e-xp-hyd.md | Bitcoin Miner S21e XP Hyd. | 000202608101645025339zMWHzD70684 | 200 (all 3 endpoints) | 4961 |
| 2026-10-11-bitmain-site-s21-xp-imm.md | Bitcoin Miner S21 XP Imm. | 00020260910170551697xvID9SCf06AD | 200 (all 3 endpoints) | 4437 |
| 2026-10-11-bitmain-site-s21-plus-hyd.md | Bitcoin Miner S21+ Hyd. | 00020260924145421522Rn7yNQxW06D1 | 200 (all 3 endpoints) | 4991 |
| 2026-10-11-bitmain-site-s21-imm.md | Bitcoin Miner S21 Imm. | 00020260323183503788h9IhgEK8067E | 200 (all 3 endpoints) | 4435 |
| 2026-10-11-bitmain-site-s21e-hyd.md | Bitcoin Miner S21e Hyd. | 00020260326155752868PjYMOON00680 | 200 (all 3 endpoints) | 6705 |

## Model → productId map (12-SKU live SHA256 catalog, re-pulled 2026-10-11)

Catalog API re-fetched this run and matched the 2026-10-10 snapshot row-for-row (same 12 SHA256 SKUs, same hashrate/power/efficiency/price values — no catalog drift in 24 h). A7 had dedicated pages for the first 5; A13 adds the remaining 7.

| Model | productId | A7 file | A13 file |
|---|---|---|---|
| S23 XP Hyd. | 000202608201636197889T3Y4SxC0660 | ✔ | — |
| S23e U2H | 000202601010841411189UJk1mK10645 | ✔ | — |
| S21 XP+ Hyd. | 000202509301221500115U8GHT3J0604 | ✔ | — |
| S21j XP Hyd. | 00020251222142202843CFQByJe40662 | — | ✔ |
| S21 XP Hyd. | 00020260818135755111661061ap05FD | ✔ | — |
| U3S21EXPH | 00020260810155841382oE3e7NdL0679 | — | ✔ |
| S21e XP Hyd. | 000202608101645025339zMWHzD70684 | — | ✔ |
| S21 XP Imm. | 00020260910170551697xvID9SCf06AD | — | ✔ |
| S21 XP (air) | 00020260330165744306Qb3RQT100632 | ✔ | — |
| S21+ Hyd. | 00020260924145421522Rn7yNQxW06D1 | — | ✔ |
| S21 Imm. | 00020260323183503788h9IhgEK8067E | — | ✔ |
| S21e Hyd. | 00020260326155752868PjYMOON00680 | — | ✔ |

All 12 live SHA256 SKUs now have dedicated spec pages (5 from A7 + 7 from A13); the catalog-row-only gap from A7 is closed.

## Storefront price rows (As-Of 2026-10-11, one line per SKU as captured in each file)

- S21j XP Hyd. — Storefront (As-Of 2026-10-11): price 8415 USD, pricePerunit 17 USD/T, product status 2 (on sale); shipping "Shipping from October 2026"
- U3S21EXPH — Storefront (As-Of 2026-10-11): price 7740 USD, pricePerunit 9 USD/T, product status 2 (on sale); shipping "Shipping from October 2026"
- S21e XP Hyd. — Storefront (As-Of 2026-10-11): price 3870 USD, pricePerunit 9 USD/T, product status 2 (on sale); shipping "Shipping from Q4 2026"
- S21 XP Imm. — Storefront (As-Of 2026-10-11): price 2400 USD, pricePerunit 8 USD/T, product status 2 (on sale); shipping "Shipping in 7 working days after fully paid"
- S21+ Hyd. — Storefront (As-Of 2026-10-11): price 2864 USD, pricePerunit 8 USD/T, product status 2 (on sale); shipping "Shipping in 7 working days after fully paid"
- S21 Imm. — Storefront (As-Of 2026-10-11): price 1290 USD, pricePerunit 6 USD/T, product status 2 (on sale); shipping "Shipping in 7 working days after fully paid"
- S21e Hyd. — Storefront (As-Of 2026-10-11): price 1728 USD, pricePerunit 6 USD/T, product status 2 (on sale); shipping "Shipping in 20 working days after fully paid"

All seven are status 2 (on sale); no pre-sell among the A13 set. All prices/rows identical to the 2026-10-10 catalog snapshot.

## Key spec literals (exact quotes from the captured tables)

**S21j XP Hyd.** — Version `495T-10`; `| Typical Hashrate, TH/s(1-1) | 495 |`; `| Power on wall @35℃(1-2), Watt(1-1) | 5940 |`; `| Power efficiency on wall@35℃(1-2), J/TH(1-1) | 12.0 |` (spec table spells J/TH where the listing row says 12J/T); 380~415 V 3~, 12 A; 430*176*208 mm w/o package; 16.2/18.3 kg; coolant 8.0~10.0 L/min, ≤3.5 bar, OD10; pH cell served with the typo `Prue water: 6.5~7.5` and full-width colon `Deionized water：8.5~9.5`; working coolant value `Antifreeze/ Pure water/Deionized water` (stray space as served).

**U3S21EXPH** — rows `Sub | 860T` and `Version | 10`; `| Power on wall @35℃(1-2), Watt(1-1) | 11,180 |` (thousands comma as served); `| Power efficiency on wall@35℃(1-2), J/T(1-1) | 13.0 |`; `Input max current, Amp | 24`; `Power port | LP34`; `900*482.6*130` mm w/o package (3U), `1,150*640*260` with package (comma as served); 42.7/48.6 kg; `Coolant flow, L/min | 16.0~20.0`; OD14; footnote ref `Working coolant(3-2)`; `SHA256|BTC/BCH/BSV` (no spaces, as served).

**S21e XP Hyd.** — no Version row; footnote numbering runs (2-1)/(2-2)/(3-1)/(3-2) and one row mixes bands: `| Power on wall @35℃(1-2), Watt(2-1) | 5590 |`; `| Power efficiency on wall@35℃(2-2), J/T(2-1) | 13 |` (integer, J/T); `339*173*207` mm; 13.8/15.7 kg; OD10; 8.0~10.0 L/min.

**S21 XP Imm.** — section heading served as `Perfermance Curve` (typo preserved, incl. in file heading); dual-mode table flattened from the served nested sub-table: `| Working mode(1-1) | NEM \| HEM |`, `| Typical hashrate, TH/s(1-2) | 300 \| 380 |`, `| Power on wall @30℃(1-3) , Watt(1-2) | 4050 \| 5700 |`, `| Power efficiency on wall @30℃, J/TH(1-2) | 13.5 \| 15.0 |` — @30℃ oil (not @35℃ water); `Inlet oil temperature, °C | 20~50`; `Oil flow, m3/h | 1` (served as m<sup>3</sup>/h); `364(2-2)*236*293` mm with note `(2-2) The height includes a 44mm handle.`; `Storage temperature,°C` (no space, as served); 16.8/18.5 kg; Version `300T-10`.

**S21+ Hyd.** — no Version row; footnote band shifted to (2-x)/(3-x): `| Power on wall @35℃(1-2), Watt(2-1) | 5370 |`, `| Power efficiency on wall@35℃(2-2), J/T(2-1) | 15 |` (integer); `339*173*207` mm; 14.5/16.4 kg; OD10; 8.0~10.0 L/min; note (3-2) served with missing space: `instructions,please refer`.

**S21 Imm.** — Version `10` (plain); dual-mode: `| Typical hashrate, TH/s(1-2) | 215 \| 301 |`, `| Power on wall @30℃(1-3) , Watt(1-2) | 3440 \| 5569 |`, `| Power efficiency on wall @30℃, J/TH(1-2) | 16.0 \| 18.5 |` (HEM: 301 T, 5569 W, 18.5 J/TH); `Inlet oil temperature, °C | 30~55` (tighter band than S21 XP Imm.'s 20~50); `293*236*364(2-2)` mm (dimension order differs from S21 XP Imm. as served); 17.15/20.45 kg; `Oil flow, m3/h | 1`.

**S21e Hyd.** — uses `°C` where siblings use `℃`: `| Power on wall @35°C(2-2), Watt(2-1) | 4896 |`, `| Power efficiency on wall @35°C(2-2), J/TH(2-1) | 17 |`; hash/power rows served with an empty second sub-column (`| 288 \|  |`, `| 4896 \|  |`) — legacy NEM/HEM template, captured as served; no Version row; row labels vary: `Maximum input current, Amp`, `Input voltage(3-1) , Volt` (footnote before unit), `Coolant Flow`, `Working Coolant(2-2)`, `Diameter of Coolant pipe connector`; `339*176*208` mm; 14.3/16.2 kg; OD10; only SKU in this set with a live `Payment` section (USDT(TRC20), USDT(ERC20), BTC, ETC and USD accepted "in this batch"; 48-h proof-of-transfer rule; scam/Skype warning; "Refund requests based on price changes WILL NOT be honored").

## Gaps / failures

- None. All 21 API calls (1 catalog + 7×2 detail) returned HTTP 200 with valid JSON (`code 0`); no retries needed. No fabricated values; every number above is byte-quoted from the API responses.
- API exposes no publish date (`pubTime` empty) — "Published: Unknown" in all files.
- Performance Curve sections are image-only (chart PNGs; URLs preserved in files) — hashrate/efficiency-vs-temperature values are not available as text from this endpoint (mirrors the MicroBT A7 finding).
- S21e Hyd.'s empty NEM/HEM second sub-column is a source-side gap (served empty), recorded as served rather than normalized.
- Minor HTML→text conventions (documented for future citation): `<sup>` footnote markers inlined after their anchor text (e.g. `TH/s(1-1)`); multi-paragraph cells joined with `<br>`; nested NEM/HEM sub-tables flattened to `A \| B` in served column order (NEM first); whitespace collapsed per HTML rendering semantics (preserves quirks like `wall@35℃`, `temperature,°C`, `SHA256\|BTC/BCH/BSV`, `11,180`); section-banner paragraphs (`| Specifications`) dropped only where they duplicate the section heading — kept where the served banner text differs from the (typo'd) section name (`| Performance Curve` under `## Perfermance Curve` on both Imm. SKUs).

## Method notes

1. Endpoints (unchanged from A7): `shop-product-service.bitmain.com/api/productshow/getMainProductsWithFilter?language=en` (38 items), `/api/product/getDetail?productId=…&language=en`, `/api/product/getDetailMoreInfo?productId=…&language=en`. Shop page pattern: `https://shop.bitmain.com/product/detail?pid=<productId>`.
2. All requests: `curl --compressed` + Chrome 126 UA; ≥1.05 s spacing (14 detail calls ≈ 15 s); zero retries needed.
3. `getDetailMoreInfo` returns a list of section objects `{id, modelName, moreInfo}` — section names and their order vary per SKU (S21e Hyd. has 5 sections incl. `Payment`; both Imm. SKUs name the curve section `Perfermance Curve`).
4. Immersion SKUs structure the Product Glance values as a nested borderless 2-column sub-table (NEM | HEM); hydro SKUs use plain single-value cells; S21e Hyd. mixes both (2-col sub-table with one empty column).
5. Fidelity gate: an automated harvester re-parsed the raw HTML and checked every non-empty table cell, paragraph (split on `<br>`), image src and link href for presence in the generated markdown (modulo pipe-escaping/link-markup normalization) — result 0 missing across all 7 files (394 cells, 259 paragraphs, 14 images, 15 links).
6. Cooling-flag code from `getDetail.coolingFlag`: 1=air, 2=hydro, 3=immersion; `productStatus`: 1=pre-sell, 2=on sale.

## Signal lines

1. The 2026-10 live-catalog efficiency ladder now has full spec sheets end-to-end: S23 XP Hyd. 8.9 → S23e U2H 10 → S21 XP+ Hyd. 11 → S21j XP Hyd. 12 / S21 XP Hyd. 12 → U3S21EXPH 13.0 / S21e XP Hyd. 13 → S21 XP 13.5 / S21 XP Imm. 13.5 (NEM) → S21+ Hyd. 15 → S21 Imm. 16.0 (NEM) → S21e Hyd. 17 J/TH — hydro values on wall @35℃, immersion on wall @30℃ (oil), air-cooled S21 XP @25℃ (A7 file): the temperature bands are not comparable across cooling classes.
2. HEM economics: both immersion SKUs expose a High Energy Mode worth ~+25% hashrate for ~+38% power (S21 XP Imm. 300→380 T, 4050→5700 W, 13.5→15.0 J/TH; S21 Imm. 215→301 T, 3440→5569 W, 16.0→18.5 J/TH) — the S21 XP Imm. row even prices both modes in one table.
3. U3S21EXPH is the density play: 3U 900*482.6*130 mm, 860 T at 13.0 J/T, 24 A + LP34 power port, 16.0~20.0 L/min coolant, OD14 fittings, and per-T pricing of 9 USD/T vs 17 USD/T for the 2U S21j/S21 XP Hyd. — Bitmain is discounting multi-unit hydro bundles by ~47% per TH.
4. Chassis reuse across the value ladder: 339*173*207 mm (S21e XP Hyd., S21+ Hyd., and A7's S21 XP Hyd.) and 339*176*208 mm (S21e Hyd.) vs 430*176*208 mm (S21j XP Hyd.) — same 2U hydro chassis family, different hashrate bins (288–495 T) purely via binning/version.
5. Version strings are inconsistent by design: `495T-10` (S21j), `10` (U3S21EXPH, S21 Imm.), `300T-10` (S21 XP Imm.), absent (S21e XP Hyd., S21+ Hyd., S21e Hyd.) — any cross-SKU version join must key on model+productId, not Version.
6. S21e Hyd. is the only current SHA256 SKU whose page still carries a per-batch Payment section (USDT/BTC/ETC/USD, 48-h transfer proof, difficulty-adjustment refund disclaimer) — evidence it is sold on batch terms rather than continuous stock.
