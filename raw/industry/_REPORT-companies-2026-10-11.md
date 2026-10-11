# A15 Company-Tracker Vetting Report — heat-reuse & mining-infrastructure companies

> Registry IDs: foghashing, heatbit, mintgreen, heatcore, ry3t, hestia, constellation-heating, pivotal-pleb-tech, hashrate-house, hotmine, superheat, d-central, cryptocloaks, altair-tech, gridless, 256heat, nakamoto-mining, griid, exergy-docs, exergy-calculators, exergy-forum
> Collected: 2026-10-11
> Method: all fetches same day (curl, browser UA); CleanSpark PR via reader fetch — direct curl 403
> Posture: extract (assessment memo; raw extracts in sibling files)
> As-Of: 2026-10-11

Mandate (Tyler, 2026-10-11): deep-dive hashrate-heating companies and notable mining-infrastructure companies; only ingest companies that are obviously legit with industry impact — any hesitation → leave out. The output is the bot-facing company tracker: registry rows (what the loop re-checks) + `wiki/industry/hashrate-heating-companies.md`.

## 1. Files captured (21 extracts + this report)

**Heat-reuse appliance & system vendors**
1. `raw/industry/foghashing/2026-10-11-foghashing-home.md` — https://foghashing.io — HTTP 200, 154,811 B
2. `raw/industry/heatbit/2026-10-11-heatbit-home.md` — https://heatbit.com — HTTP 200, 184,543 B
3. `raw/industry/mintgreen/2026-10-11-mintgreen-home.md` — https://mintgreen.co — HTTP 200, 118,631 B
4. `raw/industry/heatcore/2026-10-11-heatcore-home.md` — https://heatcore.tech — HTTP 200, 151,091 B
5. `raw/industry/ry3t/2026-10-11-ry3t-home.md` — https://ry3t.com/en/ — HTTP 200, 139,899 B
6. `raw/industry/hestia/2026-10-11-hestia-home.md` — https://hestiaheat.ca — HTTP 200, 73,610 B
7. `raw/industry/constellation-heating/2026-10-11-constellation-home.md` — https://constellationheating.com — HTTP 200, 14,873 B
8. `raw/industry/superheat/2026-10-11-superheat-home.md` — https://www.superheat.xyz — HTTP 200, 183,811 B
9. `raw/industry/hotmine/2026-10-11-hotmine-home.md` — https://hotmine.io — HTTP 200, 35,703 B
10. `raw/industry/hashrate-house/2026-10-11-hashrate-house-home.md` — https://www.hashratehouse.com — HTTP 200, 76,568 B

**DIY/enthusiast hardware & vendors**
11. `raw/industry/pivotal-pleb-tech/2026-10-11-pivotal-home.md` — https://pivotalpleb.com — HTTP 200, 109,435 B
12. `raw/industry/256heat/2026-10-11-256heat-home.md` — https://256heat.com — HTTP 200, 245,328 B
13. `raw/industry/d-central/2026-10-11-dcentral-home.md` — https://d-central.tech — HTTP 200, 269,322 B
14. `raw/industry/cryptocloaks/2026-10-11-cryptocloaks-home.md` — https://www.cryptocloaks.com — HTTP 200, 512,997 B
15. `raw/industry/altair-tech/2026-10-11-altair-home.md` — https://altairtech.io — HTTP 200, 706,922 B
16. `raw/industry/nakamoto-mining/2026-10-11-nakamoto-home.md` — https://nakamotomining.com — HTTP 200, 654,062 B

**Infrastructure**
17. `raw/industry/gridless/2026-10-11-gridless-home.md` — https://gridlesscompute.com — HTTP 200, 94,264 B
18. `raw/industry/griid/2026-10-11-cleanspark-griid-acquisition.md` — investors.cleanspark.com PR (reader fetch; curl 403) — full text captured

**Exergy verification (flips proposed → active)**
19. `raw/industry/exergy/2026-10-11-exergy-docs-intro.md` — https://docs.exergyheat.com — HTTP 200, 25,576 B
20. `raw/industry/exergy/2026-10-11-exergy-support-forum.md` — https://support.exergyheat.com — HTTP 200, 185,021 B (public Discourse confirmed)
21. `raw/industry/exergy/2026-10-11-exergy-calculators-github.md` — https://github.com/exergyheat/webapp-calculators — HTTP 200, 364,931 B

## 2. Vetting decisions — INGESTED (18 registry rows)

All pass the bar: live official site + third-party corroboration (press, patents, funding, or sustained community adoption) + current activity.

| Company | Why obvious |
|---|---|
| Fog Hashing → Fog Computing | Paul Jin Li's company (book foreword); C-series home immersion ubiquitous in community; CES 2024; 4 MW Australia solar site; expanding into AI DC + transformers/switchboards; site banner "Fog Hashing is now Fog Computing" |
| Heatbit | UL-certified heaters shipping since 2021; Trio/Maxi line; new Bitair product shipping ("October batch"); Trustpilot 4.5/350+ reviews; book profile |
| MintGreen | Digital Boilers, Lonsdale Energy district-heat contract (North Vancouver), 96%-recovery figure repeated in District Energy press; active projects list |
| HeatCore | MicroBT WhatsMiner authorized hydro partner + repair; H/M/N/X/E rack lines; first US hydro heat-recovery pilot 2022; active X output Sep 2026 |
| RY3T | Swiss RY3T ONE in existing home water systems; S-GE trade-press item on first single-family home; book profile |
| Hestia | 4 US patents, ETL/Intertek listed, 25+ furnaces deployed Labrador/Quebec since 2019, trademarked, podcast + book coverage |
| Constellation Heating | Star Heater pool boiler (600 TH); founder Nicolas Drouin (@BTC_Grid); Daniel Batten coverage; live products page |
| Superheat | CES 2026 award winner; H1C computational water heater; Founding Batch preorders open; already cited in wiki hydronics article from community msgs #8609/#8611 |
| Hotmine | Ukrainian heater-miner pioneer (own blog: developers since 2013); active Woo store; CES 2026 water-heater floor coverage |
| Hashrate House | Live systems vendor (HashTub immersion, Aqueon, Hydro lines); "Heat Punk Innovation Award" badge; Snorkel partnership; summit presence |
| Pivotal Pleb Tech | Loki Kit 120V ecosystem standard; Njord Cloudline board; resold via Altair/D-Central; cryptonews Urlacher coverage; book ch. 3 |
| 256 \| HEAT (Toine) | Live accessory shop (Wi-Fi PDU, shrouds, consulting); PDU is the community-standard accessory in 256F field reports; two podcast features |
| D-Central | Established Quebec vendor: Bitaxe/open-source units, 11 SKU space-heater category, quiet modded Antminers, repair; "zero orders dropped" status page |
| CryptoCloaks | Community-standard S9 heater STLs + testing-data page; Colorado shop; May 2026 heater guide |
| Altair Technology | Active reseller with Loki Rigs category, home-miner lines, live network widget; consulting/show presence |
| Nakamoto Mining LTD. | Schnitzel's live Shopify store (120V Home Mining, FILE DEPOT); community-anchored HashTub builder |
| Gridless | Block/Stillmark $2M seed; multi-country hydro/solar/geothermal sites; CNBC/BBC; the reference case for mining-as-energy-infra |
| GRIID Infrastructure | NASDAQ GRDI miner; acquired by CleanSpark 2024-10-30 (0.06959 CLSK/share, 400 MW Tennessee TVA buildout) — row kept dormant for history |

## 3. Vetting decisions — NOT ingested (hesitation → skip)

| Candidate | Decision | Reason |
|---|---|---|
| Unbound Networks | skip | Web search returned only unrelated hits; could not verify current company status/site. Book mention exists but no verified live footprint |
| Hashlabs Mining (Jaran Mellerud) | tracker mention only, no registry row | Legit consultancy (Mining Pod, Energy-to-Compute, Africa coverage) but no verifiable official site found (hashlabsmining.com and hashlabs.fi DNS-fail); track via podcasts/LinkedIn, not a row |
| Bitcoin Bloem | skip | Tulip-farm heat reuse is real (book ch. 4) but no 2026 activity verified; already covered via book extract in products article |
| Sato Technologies | skip | Did not complete verification this pass; TSXV-listed but heat-reuse line unconfirmed — revisit only with direct evidence |
| Heata (UK) | skip | Server-heat water heating, general compute not bitcoin — out of scope |
| Soluna / Bitmine Immersion / BitFury-Allied | skip | Surfaces in results but no heat-reuse-for-homes angle or verification done; public-miner economics already covered by `public-miner-economics` + `sec-edgar-miners` |
| Assorted startup "slop" | skip | Bar: only companies with verifiable site + independent corroboration; everything unverified stayed out |

## 4. SSR vs JS-shell assessment

- All 20 direct fetches SSR (Shopify, WooCommerce, WordPress, HubSpot, Webflow, mdBook, Discourse, GitHub) — key marketing copy present in raw HTML.
- Exceptions: gridlesscompute.com field-feed counters are JS (render as "0" in HTML; copy intact); 256heat.com page `<title>` empty in HTML (Shopify template; body copy intact); constellationheating.com is a small (14,873 B) one-pager — all copy present.
- exergy.me is behind Cloudflare Access (sign-in wall) — public docs/support/GitHub captured instead.
- investors.cleanspark.com 403s curl; captured via reader fetch with full PR text.

## 5. Registry outcomes

- 17 new `active` site rows (monthly cadence): foghashing, heatbit, mintgreen, heatcore, ry3t, hestia, constellation-heating, superheat, hotmine, hashrate-house, pivotal-pleb-tech, 256heat, d-central, cryptocloaks, altair-tech, nakamoto-mining, gridless
- 1 new `dormant` row: griid (absorbed by CleanSpark 2024-10-31; static cadence, PR captured)
- 3 flips `proposed` → `active`: exergy-docs, exergy-calculators, exergy-forum (all verified live; forum public Discourse confirmed)
- Tracker mention (no row): Hashlabs Mining
