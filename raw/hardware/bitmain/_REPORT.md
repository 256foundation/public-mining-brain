# Capture report — Bitmain + MicroBT current-gen ASIC spec pages (capture-loop A7)

> Collected: 2026-10-10
> Scope: commercial ASIC manufacturers, phase cap 60
> Registry IDs: bitmain-site, microbt-site
> Method: curl --compressed with Chrome 126 UA; HTML stripped to text; SPA payloads/APIs reverse-engineered from JS bundles (≤1 req/s)

## Bitmain (bitmain-site) — 6 files

Posture confirmed: www.bitmain.com is a Nuxt JS shell (15.8 KB, nav only); shop.bitmain.com is a Vue SPA shell (~3 KB). Instead of fighting the shells, the data plane was reverse-engineered from the Nuxt app bundle:

- `shop-product-service.bitmain.com/api/carousel/get?type=wwwProduct` — home "Hot Products" list
- `shop-product-service.bitmain.com/api/productshow/getMainProductsWithFilter?language=en` — full live catalog (38 items)
- `shop-product-service.bitmain.com/api/product/getDetail?productId=...&language=en` — per-SKU listing JSON
- `shop-product-service.bitmain.com/api/product/getDetailMoreInfo?productId=...&language=en` — full Specifications/Performance/Warranty HTML sections per SKU (the real spec sheets)

Shop product URL pattern (discovered from Nuxt chunk): `https://shop.bitmain.com/product/detail?pid=<productId>`.

Files:
1. `2026-10-10-bitmain-site-s23-xp-hyd.md` — S23 XP Hyd., 600 TH/s, 5340 W, 8.9 J/T (full spec table)
2. `2026-10-10-bitmain-site-s23e-u2h.md` — S23e U2H, 865 T, 8650 W, 10 J/T, 2U rack (600*483*86 mm)
3. `2026-10-10-bitmain-site-s21-xp-plus-hyd.md` — S21 XP+ Hyd., 480 T, 5280 W, 11.0 J/T
4. `2026-10-10-bitmain-site-s21-xp-hyd.md` — S21 XP Hyd., 473 T, 5676 W, 12 J/T
5. `2026-10-10-bitmain-site-s21-xp.md` — S21 XP air, 270 T, 3645 W, 13.5 J/TH, 76 dBA
6. `2026-10-10-bitmain-site-product-catalog.md` — 12 live SHA256 SKUs + Hot Products carousel

Garbled / failed URLs:
- `https://www.bitmain.com/` — JS shell, no product data in HTML (only nav + Nuxt chunk URLs); product list fetched client-side.
- `https://www.bitmain.com/antminer`, `/products` — 404 (4.2 KB error page).
- `https://antminer.bitmain.com/` — connection failed (000, DNS/TLS no response).
- `https://shop.bitmain.com/product/detail?pid=...` — renders as ~3 KB shell for curl; content only via the JSON API documented above (used instead).
- `https://shop.bitmain.com/sitemap.xml`, `/robots.txt` — serve the SPA shell HTML, not real sitemap/robots.
- `shop-static.bitmain.com` webpack chunk path initially 403'd until exact publicPath `support/product.e2fb08edfd62.js` was derived from the manifest.

Not captured (priority list vs. live catalog): S21 (plain), S21 Pro, S21 Hyd., T21 are no longer listed in the 2026-10 shop catalog — prior-generation SKUs with no live spec page. Lower-priced S21 family members (S21 XP Imm., S21e XP Hyd., S21+ Hyd., S21 Imm., S21e Hyd., U3S21EXPH) are covered as catalog rows in the catalog file instead of individual pages (≤6-file cap).

Signal lines:
1. Live SKU ladder (2026-10): S23 XP Hyd. 8.9 J/T → S23e U2H 10 J/T → S21 XP+ Hyd. 11 J/T → S21j XP Hyd. / S21 XP Hyd. 12 J/T → U3S21EXPH / S21e XP Hyd. 13 J/T → S21 XP / S21 XP Imm. 13.5 J/T → S21+ Hyd. 15 J/T → S21 Imm. 16 J/T → S21e Hyd. 17 J/T.
2. 2026 S23 generation is real and shipping-soon: S23 XP Hyd. (600T-10, 8.9 J/T on wall @35℃, $15,300, "Shipping from November 2026") and S23e U2H (865T-10, 10 J/T, 8650 W, "Shipping from Q4 2026", 2U rack form for ANTSPACE HW7).
3. Hydro is the flagship track; air-cooled flagship tops out at S21 XP 13.5 J/TH (3645 W, 270 T, single-phase 220~277 V).
4. Efficiency claims are wall-side @35℃ for hydro units ("power efficiency on wall @35℃", ±5%) vs @25℃ for air-cooled S21 XP — not directly comparable across cooling classes.
5. Multi-unit/hydro ecosystem SKUs now on the same storefront: U3S21EXPH (860 T, 11180 W bundle), ANTSPACE HW7 (2000 kW, 242× S23e U2H slots, $169,000), ANTRACK AR30/AR31 (200 kW, 20× U2 Hydro).

## MicroBT (microbt-site) — 6 files

Posture confirmed: www.microbt.com is a Nuxt SPA with partial SSR (22.6 KB, company-values text only, zero `<a>` tags; nav is JS). Its "product center" button opens `www.whatsminer.com/src/views/product.html`, which now redirects into the official Nuxt shop at `shop.whatsminer.com` — which IS server-rendered. The whatsminer.com legacy Vue layer exposes a JSON API (`/renren-fast/app/...`) that yields the official spec-file list.

Data plane:
- `https://www.whatsminer.com/renren-fast/app/v2/site/getNavList` — nav (reveals shop path)
- `https://shop.whatsminer.com/products` — SSR catalog (17 SKU cards)
- `https://shop.whatsminer.com/products/details/<pid>?skuId=<sid>` — SSR detail pages
- `https://www.whatsminer.com/renren-fast/app/v2/presales/getFileProductList` — official spec-sheet file index (per cooling class)
- `https://www.whatsminer.com/renren-fast/app/v2/presales/downloadFile?id=<id>&type=product` — resolves official PDF URLs

Files:
1. `2026-10-10-microbt-site-m66s.md` — M66S immersion: 270–298 T ±10%, 18.5 J/T ±5%, 5291 W (shop), manual Oct 2024
2. `2026-10-10-microbt-site-m66s-plus.md` — M66S+ immersion: 280–318 T ±10%, 17 J/T ±5%, 18 kg net
3. `2026-10-10-microbt-site-m63s-plus.md` — M63S+ hydro: 390–450 T ±10%, 17 J/T ±5%, 86×482.6×663 mm, ≥10 L/min
4. `2026-10-10-microbt-site-m64.md` — M64 hydro: 180–206 T ±10%, 19.9 J/T ±5%, 371×290×109 mm compact, AC220–277 V 5 kW
5. `2026-10-10-microbt-site-m65s.md` — M65S hydro: 370–400 T ±10%, 18.5 J/T ±5%, 86×482.6×663 mm, ≥5 L/min
6. `2026-10-10-microbt-site-product-catalog.md` — 17 shop SKUs + full model/cooling map + M7x detail data

Garbled / failed URLs:
- `https://www.microbt.com/` — Nuxt SPA; SSR text is company-values + news only; no product specs anywhere in home HTML/payload; nav hrefs are JS-generated (no `<a>` tags in SSR output).
- `https://www.microbt.com/products|/product/...` — no such routes; Nuxt routes are only /about /advantage /careers /contact /news /newsDetail (verified in app bundle).
- `https://www.whatsminer.com/src/views/product.html` and `products.html` — legacy Vue pages replaced by redirect into the Nuxt shop app (196 KB identical shell).
- `https://www.whatsminer.com/renren-fast/app/v2/presales/downloadFile?id=28&type=1|0` — errors; correct param is `type=product` (or `install`), discovered from the page's JS.
- Shop card "Power on wall" for M70S renders literally as "No data" on the detail page (gap recorded in catalog file).
- MicroBT spec-sheet PDFs: PERFORMANCE section is always an embedded chart image ("prototype data for reference only") — hashrate-vs-temperature curves are image-only, no text values.

Not captured (priority list vs. sources): M66S+/Hyd has no shop retail page (spec sheet captured from official PDF instead, immersion class, not "Hyd" naming); M64S appears in no current official list (possible rename — noted as gap); M66S++ and M63S++ spec PDFs exist but were not downloaded (file cap).

Signal lines:
1. Current-gen flagship ladder visible on the official shop (efficiency J/TH, card data): M70S 248TH @13.5 → M73 512TH @14.5 → M63S++ 464TH @15.5 → M60S++ 218TH @15.5 → M60S+ 200TH @17 → M66S 286~290TH @18.5 → M63S 408T @18 → M60S 184~188TH @18.5 → M66/M63/M60 @19.9.
2. Official 2026 file list shows the next hydro generation already documented (created 2026-05-07): M7B/M7BS/M7BS+ and M6B/M6BS/M6BS+ (plus M7A/M6A family) — MicroBT has moved spec sheets ahead of retail availability.
3. Home-page hero (Dec 2025 edit) is "M73S+ — Born for mining": the M73S+ (hydro, same 86×482.6×663 mm 2U-class chassis) is the company's current banner SKU; M76/M76S/M76S+ immersion trio added to the official file list.
4. Efficiency ladder visible in official sheets: M66S+ 17 J/T and M63S+ 17 J/T are the best hydro numbers captured this run; M64 (compact) 19.9 J/T; immersion M66S 18.5 J/T — MicroBT's shipping flagships lag Bitmain's S23 XP Hyd. (8.9 J/T) by a wide margin on published wall efficiency.
5. Naming divergence to record: MicroBT retail cards quote ±10% hashrate ranges (e.g. 270–298 T) and J/TH ±5%; Bitmain quotes single typical TH/s (±3%) — cross-manufacturer comparisons should use the ± bands, not the headline numbers.
