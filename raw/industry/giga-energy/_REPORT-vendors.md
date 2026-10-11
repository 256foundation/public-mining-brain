# A10 Vendor Fetch Report — Crusoe / Upstream Data / Giga Energy

> Registry IDs: crusoe, upstream-data, giga-energy
> Collected: 2026-10-10 (all fetches same day, curl, browser UA, --compressed)
> Posture: extract (assessment memo; raw extracts in sibling files)
> As-Of: 2026-10-10

## 1. Files captured (10 extracts + this report)

**raw/industry/crusoe/**
1. `2026-10-10-crusoe-home.md` — https://www.crusoe.ai/ — HTTP 200, 114,496 B
2. `2026-10-10-crusoe-about-company.md` — https://www.crusoe.ai/about/company — HTTP 200, 68,236 B
3. `2026-10-10-crusoe-newsroom-nydig-bitcoin-exit.md` — /resources/newsroom/nydig-to-acquire-crusoes-bitcoin-mining-operation-crusoe-to-scale-vertically — HTTP 200, 62,208 B

**raw/industry/upstream-data/**
4. `2026-10-10-upstream-home.md` — https://www.upstreamdata.ca (301 → https://upstreamdata.com/) — HTTP 200, 33,915 B (234,695 B decompressed)
5. `2026-10-10-upstream-black-box.md` — https://upstreamdata.com/bitcoin-mining/black-box — HTTP 200, 14,983 B
6. `2026-10-10-upstream-hash-generator.md` — https://upstreamdata.com/bitcoin-mining/hash-generator — HTTP 200, 17,305 B

**raw/industry/giga-energy/**
7. `2026-10-10-giga-home.md` — https://www.gigaenergy.com/ — HTTP 200, 64,455 B (289,096 B decompressed)
8. `2026-10-10-giga-blog-index.md` — https://www.gigaenergy.com/blog — HTTP 200, 59,394 B
9. `2026-10-10-giga-cost-of-mining-a-bitcoin.md` — /blog/cost-of-mining-a-bitcoin — HTTP 200, 51,897 B (demand-charge economics post)
10. `2026-10-10-giga-bitcoin-mining-demand-response.md` — /blog/bitcoin-mining-demand-response — HTTP 200, 52,424 B

## 2. SSR vs JS-shell assessment

- **crusoe.ai — SSR.** Webflow-hosted (cdn.prod.website-files.com) + intellimize personalization; full mission, timeline, and press-release text in raw HTML. No shell parks.
- **upstreamdata.com — SSR.** Next.js; all product copy and the Black Box spec table present in HTML. One caveat: `/resources/faq` is an accordion whose answer text is JS-loaded (only 21 question titles in HTML) — FAQ answers not captured; not needed given spec pages are open.
- **gigaenergy.com — SSR.** Full copy on home, blog index, and both blog posts in HTML. `sitemap.xml` (200, 8,299 B) lists only shop/transformer SKUs; 404s: `/wp-sitemap.xml`, `/blog-sitemap.xml`, `/post-sitemap.xml`, `/blog/demand-charges`, `/blog/understanding-demand-charges`.

No site required headless rendering; every key quote below is from raw HTML captured 2026-10-10.

## 3. Key facts by vendor

### crusoe — wasted-energy computing → AI factories (full pivot)
- Positioning NOW (home): title "Crusoe | The AI factory company"; hero "The AI factory company — We build the foundation. You build the future."; banner "Crusoe raises $3.9B Series F for its vertically-integrated AI infrastructure platform." No bitcoin/mining nav item — heritage survives only as newsroom slugs. [file 1]
- Scale figures on homepage teasers: "Crusoe and ON Energy to deploy 5 GW of AI UPS™ at Multiple Hyperscale Campuses"; link to "crusoes-contracted-ai-infrastructure-capacity-approaches-5-gigawatts-across-data-centers-and-cloud". [file 1]
- Origin, verbatim (company timeline): 2018 — "Crusoe is founded with an energy-first approach, pioneering technology to convert wasted natural gas into energy for high-performance computing."; 2021 — "$128M Series B to expand our patented Digital Flare Mitigation® technology nationwide". [file 2]
- Pivot line, verbatim: 2025 — "Divest our bitcoin mining business to NYDIG to focus exclusively on AI infrastructure." Same page: 2024 "Broke ground on Stargate, our 1.2 gigawatt data center campus in Abilene, Texas"; 2026 "$3.9B+ Series F… 1.0 Gigawatt AI data center campus in Childress, Texas with Lancium… 900 MW AI factory campus in Abilene… support Microsoft AI infrastructure… Invest $200M+ in new Crusoe Spark Factory in Brighton, Colorado." [file 2]
- Mining exit + flare-gas heritage (press release, 2025-03-25): DFM = "captures natural gas from oil fields that would have otherwise been burned off into the air as a 'flare' and converts this stranded energy into electricity to power modular data centers co-located onsite in the oilfield." At exit: "more than 425 modular data centers (250+ MWs) in the field across seven states and two countries"; "mitigated 2.7 million metric tons of greenhouse gas emissions, and prevented nearly 22 billion cubic feet of natural gas from being flared"; "approximately 135 Crusoe employees will join the team at NYDIG." [file 3]

### upstream-data — BlackBox containers, field-gas mining (still mining-first)
- Domain moved: www.upstreamdata.ca → upstreamdata.com (301). Positioning: "Distributed power and computing systems for upstream oil and gas facilities… monetize sources of stranded gas." Stranded-gas economics: "For operators dealing with flared, vented, or otherwise uneconomic gas, our integrated power and compute systems are a practical way to turn wasted fuel into revenue." Heritage: "We've been building modular loadcenters since 2016." [file 4]
- Black Box specs (no pricing; quote-request only): "Small, quiet, weatherproof loadcenters for applications up to 45 kW"; 3 models — Black Box 28/48/96: 8/20/40 kW rated, 2/6/12 server slots, 28×32×36 / 50×40×48 / 100×40×48 inches, "3-phase, 416Y240V or single phase 240V"; "Tortuous air flow path reduces sound up to 30 dB"; fanless, weatherproof, fireproof; PDU options 240V/415V/480V; "Engineered in Canada / Manufactured in the USA." [file 5]
- Hash Generator (gas + mining in one skid): "50–325 kW Power range | 10–100 mcf/d Fuel consumption | 415–480 V Voltage range"; gensets "in 50, 80, 160 and 325 kWe continuous power ratings"; "new Mesa and PSI engines, or with rebuilt GM small block engines"; "monetize sweet natural gas by converting vented, flared, or stranded sources into cash — instantly"; patented LoadSync™ controller + Universal Smart PDU; "Field-proven since 2017." [file 6]
- Economics note: no public pricing on any product page; FAQ carries the econ questions ("How much power can I generate from my natural gas?") but answers are JS-loaded. Sitemap also lists /bitcoin-mining/white-box and /bitcoin-mining/stealth-container (not fetched — file cap).

### giga-energy — mining containers + blog, repositioned as AI data center developer
- Positioning NOW: "Build AI data centers faster. Giga is the modular AI data center developer. We cut the labor, lead times, and handoffs that slow deployment."; "GigaBase — A turnkey, modular AI data center. Built in 9 months." Mining still active in nav: "Giga Box Air™ Air-cooled mining container · Giga Box Hydro™ Liquid-cooled mining container"; customer story "Energized 10MW in West Texas." [file 7]
- Blog actively published through Oct 2026 ("The Giga Blog. For those building what's next."); 82 post slugs on index; categories include Power Markets; mining-era posts still live (Simple Mining 20,000 miners, Satokie mining containers, transformers-for-crypto posts). [file 8]
- DEMAND-CHARGE ECONOMICS (the handoff's flagged post → /blog/cost-of-mining-a-bitcoin, 2026-01-08, Clay Holliday, Power Markets; no /demand-charges/ slug exists — probed 404):
  - "At $10 to $20 per kilowatt of demand, that's $50,000 to $100,000 in demand charges for that month alone" (5 MW peak example).
  - "your demand charges can represent a whopping 30-50% of your overall bill… you're adding $0.02 to $0.04/kWh on top of your base energy rate."
  - Capacity/transmission: "add another $0.01 to $0.03 per kilowatt-hour."
  - Worked example: "$0.05/kWh… + $0.025/kWh… + $0.015/kWh. Added together, your all-in cost is $0.09/kWh; an 80% increase."
  - "if you shave $0.01/kWh off a 10 MW operation, you'll save over $870,000 a year."
  - DR mitigation: "reduce their all-in electricity costs from $0.08-$0.12/kWh to around $0.06-$0.09/kWh… an additional $20,000 to $80,000 per MW per year." [file 9]
- Companion demand-response post (2026-01-01): "Electricity can account for up to 80% of your operating costs"; "miners can offer 50%, 75%, or even 100% curtailment"; "95% monthly uptime is common"; Giga's own scale: "175+ MW of flexible load sites across the U.S. with another 500 MW under development"; "stacked revenue streams can deliver up to $80,000 per MW annually" (SPP). [file 10]

## 4. Cross-vendor observations

- **The flare-gas→AI pivot is industry-wide and now explicit.** Crusoe divested mining to NYDIG (Mar 2025) "to focus exclusively on AI infrastructure"; Giga rebranded to "modular AI data center developer" (GigaBase/GigaPod, Jan 2026 Giga Power Systems launch) while keeping mining containers and a Power-Markets mining blog alive; Upstream Data remains the only one of the three still purely mining/oilfield-focused (with the same stranded-gas pitch Crusoe abandoned).
- Both crusoe.ai and upstreamdata.com still publish their 2024-25 legal settlement ("crusoe-upstream-data-to-resolve-lawsuit" appears in both nav trees) — a signal of prior competitive overlap in DFM.
- Publishing cadence: Giga blog weekly (latest 10.8.2026); Crusoe newsroom is PR-driven (latest visible teasers Oct 2026); Upstream site is static marketing + docs portal (docs.upstreamdata.com).

## 5. Gaps / not captured (budget cap ~10 files)

- Crusoe /energy and /data-centers product pages (MW detail lives in newsroom items instead); Crusoe blog.
- Upstream: hash-hut, white-box, stealth-container pages; oil-and-gas-calculator (JS calculator); FAQ answers (JS-loaded).
- Giga: /giga-box-air & /giga-box-hydro spec pages (mining-container hardware detail), /blog/how-giga-power-systems-optimizes-breakeven (contains 50 MW worked example: "$68,000 per MW" payout vs "$30,000 to $40,000" legacy — from search snippet, needs capture to quote as captured fact).
