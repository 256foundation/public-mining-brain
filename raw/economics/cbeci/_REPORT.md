# Phase A8 economics fetch report — CBECI + Cambridge Digital Mining Industry Report

> Collected: 2026-10-10
> Scope: registry IDs `cbeci`, `cbeci-methodology`, `cambridge-report`
> Agent: fetch-only subagent (phase A8, economics)

## Files captured

| File | Registry | Posture | Source |
|---|---|---|---|
| `raw/economics/cbeci/cbeci-landing.md` | cbeci | extract | https://ccaf.io/cbnsi/cbeci |
| `raw/economics/cbeci/cbeci-methodology.md` | cbeci-methodology | verbatim | https://ccaf.io/cbnsi/cbeci/methodology |
| `raw/economics/cbeci/cbeci-data-access.md` | cbeci | extract (pointers) | ccaf.io SSR/JS + endpoint probes |
| `raw/economics/cambridge-report/dmir-2025-extract.md` | cambridge-report | verbatim→extract | jbs.cam.ac.uk 2025 PDF (150 pp.) |

## Key numbers & facts (with exact literals + file locations)

### CBECI — current estimate (as rendered 2026-10-10; in `cbeci-landing.md`)

- "Bitcoin network power demand" boxes, 2026-10-10 render:
  - "Theoretical lower bound **9.48 GW / 83.08 TWh**"
  - "Estimated **18.48 GW / 162.04 TWh**"
  - "Theoretical upper bound **35.56 GW / 311.70 TWh**"
- Hardware efficiency boxes: "Theoretical lower bound **9.50 J/TH** · Estimated **17.01 J/TH** · Theoretical upper bound **30.00 J/TH**"
- Presentation: GW figure "Updated every 24 hours"; annualised TWh uses "a seven-day moving average"; model "begins on July 18th 2010"; electricity-cost slider default = 5¢/kWh (documented default 0.05 USD/kWh).
- Important presentation change: live/raw data now behind "Live estimates — Available on request — Request access" gates on the landing page.
- License: "Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License". Footer: "Cambridge Centre for Alternative Finance © 2026".

### CBECI — methodology version & key assumptions (in `cbeci-methodology.md`, verbatim)

- Latest documented model update: **v1.4.0** ("The latest update (v1.4.0) marks a significant change in how we compute our best-guess estimate").
- Best-guess mechanics: release-date weighting "ranging from 1 to 0, decreasing in five steps of 0.2", five-year economic lifetime (from listed miners' depreciation schedules), plus "a delay of two months from the hardware's release date to when it is considered in our model".
- Assumptions: electricity cost "USD 0.05 per kilowatt-hour"; PUE lower-bound 1.01, upper-bound 1.20, best-guess 1.10; 14-day moving average on profitability threshold; hardware basket = Bitmain/MicroBT/Canaan ("estimated combined market share of at least 85%"); 100+ ASIC list "available at http://sha256.cbeci.org".
- Table 2 comparison anchor: "Digiconomist — Live estimate — Bitcoin Energy Consumption Index — **204.44** (TWh)".

### CBECI — dataset/API pointers (in `cbeci-data-access.md`)

- CSV dataset endpoint (linked on methodology page): `https://demo.cbeci.org/api/v1.0.5/download/data` → 302 → `https://demo.ccaf.io/cbeci/api/v1.0.5/download/data` (HTTP 200; CSV; first line verbatim: `Average electricity cost assumption: 0.05 USD/kWh,,,,`; columns `Timestamp,Date and Time,MAX,MIN,GUESS`). **Full CSV NOT downloaded/committed** (no-massive-data rule).
- Live stats JSON: `https://ccaf.io/cbeci/api/data/stats/live` → HTTP 200 `{"digiconomist":"204.44"}`.
- Headline-number API: `https://ccaf.io/cbeci/api/data/live` → HTTP 400 "Invalid recaptcha response" for bare curl (invisible reCAPTCHA, site key 6LcxxtUpAAAAAGGCa99eoB7bpeI2fKdHyg-1NZQ_). Numbers therefore captured from the rendered page, not the raw API.
- Frontend API base (from /cbnsi/_nuxt JS): `"https://ccaf.io/cbeci/api"`; calls `/data/<price>`, `/data/stats/<price>`, `/charts/mining_map_countries`; separate CBNSI projects API `https://api.ccaf.io/v1/projects`.
- Hardware list: `http://sha256.cbeci.org` → HTTP 200, "Mining equipment list - Google Sheets".
- Change log: methodology links `https://ccaf.io/cbnsi/change_log` → **HTTP 404** on 2026-10-10 (and `…/cbeci/change_log` soft-404s with SPA "404 Page Not Found"). Parked.

### Cambridge Digital Mining Industry Report — headline stats (in `dmir-2025-extract.md`, page-cited)

- Identity: title page p.1 — "Cambridge Digital Mining Industry Report — Global Operations, Sentiment, and Energy Use — FIRST EDITION — April 2025". 150 pages. Principal researcher Alexander Neumueller (p.5); team Gina Pieters, Kamiar Mohaddes, Valentin Rousseau, Bryan Zhang. Survey June–Sept 2024.
- Coverage: "268 EH/s, equivalent to 48% of the implied Bitcoin network' hashrate (as of 30 June 2024)"; "7.3 GW" capacity; 49 firms; HQs in 16 countries; operations in 23 (p.46).
- Consumption: "estimated at 138.2 TWh as of 30 June 2024… a 17% YoY increase… approximately 0.54% of the world's total annual electricity consumption"; CBECI model "137.4 TWh"; end-2024 "183 TWh", hashrate "558.7 EH/s (30 June 2024) to 795.7 EH/s (31 December 2024)" (p.63). Divergence 2021–24: hashrate "+455%" vs consumption "+111%" (p.62).
- Efficiency: weighted "28.2 J/TH" (June 2024, −24% YoY); non-weighted median 29.5, mean 30.6, range 18.0–71.4 J/TH (p.59); CBECI-model 25.3 J/TH; end-2024 23.7 J/TH (p.61/63); next-gen expected "12.0 / 11.5 / 5.5 J/TH" (p.52).
- Geography (p.46–47): US 75.4%, Canada 7.1%, Kazakhstan 3.4%, Paraguay 2.8%, Norway 2.6% (+ 18 more countries listed, Russia 2.26%, UAE 2.17%, Bhutan 1.35%…).
- Electricity mix (p.67): "52.4% sustainable" (hydro 23.4%, wind 15.4%, solar 3.2%, other 0.5%, nuclear 9.8%) vs "47.6% fossil" (gas 38.2%, coal 8.9%, oil 0.5%); method spread: CBECI 37.6% sustainable, SBLB 47.9% (p.68); intensity 288.2 (Survey) vs 338.9 (SBLB) vs 506.7 (CBECI) gCO2e/kWh; GHG 39.8 vs 46.8 vs 69.6 MtCO2e (p.68); "0.08% of global annual GHG emissions" (p.69).
- Off-grid: "26%" of firms, "8.1%, or 1.23 GW" of consumption (p.65); curtailment "888 GWh" in 2023 (p.9).
- Hardware market: Bitmain 82.0% / MicroBT 15.0% / Canaan 2.1% (p.53); firmware stock 44.4% / Vnish 26.4% / custom 17.6% / Braiins OS 5.6% / LuxOS 3.3% / ePIC 2.7% (p.53); retirement "11.1% of the current hashrate (61.8 EH/s)" phased out end-2024, "86.9%" repurposed/recycled, e-waste "about 2.3 kilotonnes" (p.9, p.56).
- Cost curve (p.86–87): direct cost/BTC "$17,417 to $56,606, with a median of $39,189" (CBECI cross-check "$39,009"); all-in "$21,771 to $60,960, with a median of $48,333"; electricity rates median direct "$45/MWh", all-in "$55.5/MWh", gap "$10.5/MWh" other expenses, split "81.1% / 18.9%" electricity vs other (COGS+SG&A).
- Profitability (p.88–93): 2020–24 BTC price "+1209%" vs difficulty "+734%" vs hashprice "−60%"; hashcost "$128 → $16 (−87.5%)" across epochs (p.104); hash-margin matrix incl. break-even: "$80/MWh: 25 J/TH slightly above break-even… 30 J/TH already… a loss"; "$40/MWh: 45 J/TH still remain profitable" (p.92); 30 J/TH margin "peak of 91%… below 10%… rebounding to 35% by the end of 2024" (p.92–93); revenue/kWh "30 J/TH… about $0.08/kWh, whereas newer models… $0.11 – $0.15/kWh" (p.90).
- AI/HPC: revenue "$1,600 to $4,000 per MWh (CaaS)" vs "$120 to $400 (IaaS)" vs "$80 to $151" BTC mining; CAPEX "$9 to $40 million per MW" vs "$1.2 million per MW"; data-centre demand "+116% from 2024 to 2030" (p.112); Core Scientific/CoreWeave "~500 MW" (p.113).
- Sentiment: energy price 57% / gov action 47% / BTC price 40% concerns; diversification 64% / power hedging 60% / geo diversification 55%; barriers deployment 46.8% (p.98), logistics 45%, debt 40%, equity 36%.

## HTTP status log

| URL | Status | Note |
|---|---|---|
| https://ccaf.io/cbnsi/cbeci | 200 | SSR HTML 149,837 B |
| https://ccaf.io/cbnsi/cbeci/methodology | 200 | SSR HTML 300,931 B |
| https://ccaf.io/cbeci/api/data/stats/live | 200 | {"digiconomist":"204.44"} |
| https://ccaf.io/cbeci/api/data/live | 400 | "Invalid recaptcha response" (needs JS/reCAPTCHA) |
| https://ccaf.io/cbeci/api/data/stats/total (and variants) | 500 | wrong/unknown arg |
| https://ccaf.io/cbeci/api/charts/total_electricity_consumption/daily | 404 | path not found |
| https://demo.cbeci.org/api/v1.0.5/download/data | 302 | → demo.ccaf.io mirror |
| https://demo.ccaf.io/cbeci/api/v1.0.5/download/data | 200 | CSV; only 1,200-byte range fetched (no mass data) |
| https://demo.ccaf.io/cbeci/api/data/stats/live | 200 | same payload as prod |
| http://sha256.cbeci.org | 200 | Google Sheets "Mining equipment list" |
| https://ccaf.io/cbnsi/change_log | 404 | SPA 404 page |
| https://ccaf.io/cbnsi/cbeci/change_log | 200 (soft-404) | renders "404 Page Not Found" |
| https://www.jbs.cam.ac.uk/wp-content/uploads/2025/04/2025-04-cambridge-digital-mining-industry-report.pdf | 200 | 19,988,568 B application/pdf |
| https://www.jbs.cam.ac.uk/faculty-research/centres/alternative-finance/publications/cambridge-digital-mining-industry-report/ | 200 | landing; links the same PDF |
| https://ccaf.io/cbnsi/reports | 404 | probed for report listing; not needed |

## Failures / parks

- PARK (data): CBECI full CSV/time-series not downloaded by design (no-massive-data rule); pointer + CSV schema captured in `cbeci-data-access.md`. Note the methodology-page endpoint is the v1.0.5-era dataset; the current v1.4.0 series is exposed via the reCAPTCHA-gated `/data/live` API and "Request access" flow.
- PARK (change log): `https://ccaf.io/cbnsi/change_log` → 404 (2026-10-10); methodology still links it. Model version history currently unverifiable online; "v1.4.0" is the latest version named in the verbatim methodology text.
- NOTE (rendering): CBECI headline numbers are client-side rendered behind invisible reCAPTCHA; values in `cbeci-landing.md` were observed in a rendered browser (OpenChamber panel) after consent + reCAPTCHA round-trip, initial render showed "LOADING" with blank boxes. SSR HTML contains no estimate values.
- NOTE (PDF text layer): Kazakhstan/Paraguay labels on DMIR p.46 have doubled digits ("33..44%%", "22..88%%"); normalised to 3.4% / 2.8% (descending Top-5 order confirms) and flagged in the extract.

## Self-check

- All written files are under `raw/economics/cbeci/` and `raw/economics/cambridge-report/` only. ✔
- Every capture file carries the provenance header (Registry ID / Source / Collected / Published / Posture / As-Of). ✔
- No files under wiki/, scripts/, sources/, .agent/ touched; no git commands run. ✔
- Full CBECI dataset and full DMIR text/PDF intentionally kept out of the repo (temp only). ✔
