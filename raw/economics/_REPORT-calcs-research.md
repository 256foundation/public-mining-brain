# A8 Economics Fetch Report — calcs & research sources

> Collected: 2026-10-10
> Posture: extract (all sources)
> Scope: whattomine · galaxy-research · coinshares-research · braiins-insights · minermag
> All volatile numbers As-Of 2026-10-10. Exact literal quotes preserved from SSR HTML.

---

## Files written (12 captures + this report)

| # | File | Source |
|---|------|--------|
| 1 | `raw/economics/whattomine/2026-10-10_whattomine-btc-sha256-ssr-extract.md` | whattomine.com (+ /coins/1-btc-sha-256) |
| 2 | `raw/economics/whattomine/2026-10-10_whattomine-asic-ranking-ssr-extract.md` | whattomine.com/asics |
| 3 | `raw/economics/galaxy-research/2026-10-10_galaxy-research-index-mining-listing.md` | galaxy.com/research → /insights/research + /insights/topics/mining/ |
| 4 | `raw/economics/galaxy-research/2022-02-11_galaxy-breakeven-hashprice-extract.md` | galaxy.com/insights/research/analyzing-public-miners-breakeven-hashprice/ |
| 5 | `raw/economics/galaxy-research/2024-12-18_galaxy-bitcoin-miners-ai-revolution-extract.md` | galaxy.com/insights/research/bitcoin-mining-ai-revolution/ |
| 6 | `raw/economics/coinshares-research/2026-10-10_coinshares-research-index-mining-listing.md` | coinshares.com/research → /insights/research-data/ |
| 7 | `raw/economics/coinshares-research/2026-10-10_coinshares-mining-relevant-extracts-13f-week41.md` | coinshares.com/insights/research-data/{bitcoin-13f-q2-2026-report, equities-update-09-10-2026}/ |
| 8 | `raw/economics/braiins-insights/2026-10-10_braiins-insights-shell-note-and-ssr-blog-index.md` | insights.braiins.com / learn.braiins.com + braiins.com/blog |
| 9 | `raw/economics/braiins-insights/2026-03-03_braiins-gda-40mw-firmware-case-study-extract.md` | braiins.com/blog/firmware-optimization-gda-40mw-case-study |
| 10 | `raw/economics/braiins-insights/2025-04-01_braiins-tuv-sud-efficiency-extract.md` | braiins.com/blog/tuv-sud-testing-how-braiins-os-delivers-more-efficient-bitcoin-mining |
| 11 | `raw/economics/minermag/2026-10-10_theenergymag-migration-mining-index-mara.md` | theminermag.com → theenergymag.com (+ /news/mining, /company/MARA) |
| 12 | `raw/economics/minermag/2026-10-01_theenergymag-bitcoin-great-unplug-extract.md` | theenergymag.com/news/2026-10-01/bitcoin-great-unplug-hardware-leave-behind-ai |

---

## Key numbers & facts (with exact quotes and file locations)

### Network / profitability snapshot (As-Of 2026-10-10) — files #1, #2

- BTC price (WTM SSR, WhiteBIT single venue): **"Ex. rate: $82,977.33 (WhiteBIT)"**; 24h $82,933.58; 3d $82,580.86; 7d $84,039.83. Ticker strip: "BTC $82,977 (+0.1%)".
- Difficulty: **"Difficulty: 132,716,002M"** (24h/3d/7d identical — flat window). Nethash: **"1,003,540.30 Ph/s"** (~1.004 ZH/s).
- Block: **"Last block: 970,868"**, "Block time: 9m 28s", "Bl. reward: 3.17" (24h: 3.14) — WTM reports reward incl. fees.
- Emission/supply: "Daily emission: 477.809 BTC", "Market cap: $1,667,546,859,271", "Create 1 BTC in: 3,659.19 Days".
- Best SHA-256 ASIC economics (WTM /asics, row-level $0.16–0.19/kWh): "Bitmain Antminer U3S23H | Jan 2026 | 1.16 Ph/s @ 11020W | SHA-256 | $0.19/kWh | 9.50 W/Th | $49.03 | $22.58" (rev/profit 24h); "Bitmain Antminer S23 Hyd … 580.00 Th/s @ 5510W … $24.59 | $11.36"; "Bitdeer Sealminer A4 Ultra Hydro … 886.00 Th/s @ 8373W … 9.45 W/Th … $37.50 | $17.40". Best-in-class efficiency 9.45–9.50 W/Th. Top SHA-256 coins by revenue: **QUAI, FB, XEC** (merged-mining lift).
- Implied SHA-256 revenue ≈ **$0.042/TH/day** (S23 Hyd $24.59/day ÷ 580 TH); margin at $0.19/kWh ≈ 46%.
- Gap note: WTM `/coins` multi-coin table is JS-only; header ticker + coin detail + /asics table are SSR (captured).

### Hashprice / margin methodology — file #4

- Definition: **"hashprice is the market value of one unit of hashpower measured in dollars per terahash"**; "You can think of hashprice as being analogous to the value of WTI crude oil for the oil and gas industry." (Galaxy, 2022-02-11)
- Breakeven method: "breakeven hashprice, which measures the threshold below which miners begin operating unprofitably. This figure factors in operational costs like power and hosting costs, payroll … and SG&A expenses, as well as interest expense as a non-operating expense." Galaxy open-sourced the spreadsheet calculator.

### Public-miner AI-pivot economics (2026 realized numbers) — file #12

- **"roughly $1.5 billion in equivalent hardware investment, even at an assumed acquisition price of just $20 per terahash"** for hashrate shed in H1 2026.
- **"public miners lost 75 EH/s of realized hashrate while their directly reported HPC and AI revenue rose 52% quarter over quarter."**
- **"approximately $1.1 billion in asset impairments and held-for-sale markdowns during the first half of 2026. IREN and Core Scientific (NASDAQ: CORZ) accounted for almost 89% of the total."**
- IREN: "roughly $695 million in impairments and held-for-sale markdowns during January–June 2026"; Cipher: "$96.1 million markdown specifically on Black Pearl's mining machines" vs "generated $57.9 million in revenue during 2025".
- Capex: **"Public miners and AI infrastructure peers recorded $30.7 billion of 2026 net capital spending, already 43% above their full-year 2025 total."** (file #11, Aug 20 2026 item)
- Hardware price anchor: **$20/TH/s** acquisition cost assumption (file #12).

### Public-miner operational data points — file #11

- Bitdeer Aug 2026: "produced 1,310 Bitcoins during the month, supported by a self-mining hash rate of 79.9 EH/s and a co-mining hash rate of 21.6 EH/s" (+249% YoY); July: "mined 1,190 bitcoin … share of network rewards reached 8.712%".
- MARA (SSR company page): price $9.65 (+4.08%), "Market Capitalization | $3.73B", "Pledges 18,750 BTC for $600 Million New Bitcoin-Backed Loans" (Aug 7), 2 GW Texas project conditional ERCOT study status (Sep 15).
- Other: CleanSpark ends monthly mining updates (1d ago); Foundry CEO Colyer steps down "as the Bitcoin pool's block share retreats" (3d ago); Simple Mining buys 8 MW Iowa mine for $1.5M.

### Research-report headline stats — files #5, #7

- Galaxy (2024-12-18): "Goldman Sachs Research forecasts U.S. data center demand to reach 45 GW by 2030 … 15% CAGR from 2023-2030"; "By 2038, JP Morgan projects hyperscaler AI capex will reach $370bn"; racks "now need to support over 132 kW per rack … GB200 NVL72"; miners "arbitraging their 6-12x EV/EBITDA valuation with current 20-25x multiples".
- CoinShares 13F Q2 2026: **"13F filers reported 264k BTC equivalent at the end of June, up from 261k in Q1 (+1.3%)"**; "dollar value of filer holdings fell 13% to $15.5B, driven by a 14% drop in bitcoin's price"; "13F share of total US bitcoin ETF AUM rose from 20.8% to 22.4%, the first increase since Q2 2025"; hedge funds −22% QoQ to 37.8k BTC; advisors 145.7k BTC (~55%).
- CoinShares Week 41 (2026-10-09): "miners pursuing capital-intensive AI expansion remained more exposed to financing pressures and changing expectations for infrastructure returns"; blockchain equity index −4.2% vs BTC −2.1% on the week; 10Y UST "briefly reached approximately 5.36%, a 24-year high".

### Efficiency claims (vendor-published) — files #9, #10

- Braiins/GDA 40 MW (2026-03-03): "achieving up to 40% higher hashrate on identical hardware"; "the hashrate delta remained approximately 32%"; "The efficiency delta was approximately 1 J/TH".
- Braiins/TÜV SÜD (2025-04-01): "greater efficiency performance in all four tests"; fragments "62% efficiency boost" / "89% efficiency boost" (per-test values, context truncated in SSR); hashprice framing: "When hashprice falls, that doesn't mean miners have to take the hit."

---

## Failures, parks, and gaps (with exact status)

| Item | Status | Detail |
|------|--------|--------|
| Braiins dashboard (insights.braiins.com) | **JS shell — not rendered (per instructions)** | insights.braiins.com → learn.braiins.com; HTTP 200, **1,613 B**, `<div id="app"></div>`, build 8da3b47fd6f46d10 (2026-06-01). Sitemap also shell. Recorded in file #8. |
| Braiins SSR hashprice widget | **Partial — value JS-populated** | Static HTML shows label `USD/TH/Day` + change "1.53%" only; numeric $/TH/day not in SSR. Noted file #8. |
| WhatToMine `/coins` comparison table | **JS-only gap** | SSR present elsewhere (ticker, coin detail, /asics). Noted files #1–#2. |
| CoinShares 13F publish date | n/d | No machine-readable date in SSR; index position implies ~2026-10-08/09. Noted file #7. |
| Galaxy mining research cadence | Observation, not failure | Most recent dedicated mining piece surfaced = 2024-12-18; topic page lists nothing newer. Files #3–#5. |
| CoinShares standalone miner-economics report | **Not surfaced on current index front page** | grep hashrate/hashprice in SSR HTML = 0 hits; mining economics carried by weekly Equities updates + 13F. Deeper pagination (?page=2+) not crawled. File #6. |
| MinerMag | **PARK CLEARED — not a shell** | theminermag.com HTTP 200, 22,890 B SSR → rebranded theenergymag.com; full SSR + /news/mining + /company pages. No `_SHELL-NOTE.md` needed; migration recorded in file #11. |
| Braiins blog date formats | Resolved | "3.3.2026"→2026-03-03, "1.4.2025"→2025-04-01 confirmed via page metadata ("Mar 03", "Apr 01"). |

## HTTP status summary (all via curl, Chrome UA, --compressed)

- whattomine.com, /coins, /coins/1-btc-sha-256, /asics: **200** (25–85 KB each)
- galaxy.com/research/ → /insights/research: **200** (79,956 B); topic /insights/topics/mining/: **200** (13,906 B); 2 article pages: **200**
- coinshares.com/research → /insights/research-data/: **200** (233,727 B); ?tags=mining: **200**; /insights/tags/mining: **404**; 13F + equities pages: **200**
- insights.braiins.com/blog → learn.braiins.com/blog: **200** (1,613 B shell); braiins.com/blog: **200** (39,472 B); 2 posts: **200**
- theminermag.com → theenergymag.com: **200** (22,890 B); /news/mining: **200** (265,629 B); /company/MARA: **200** (22,045 B); article: **200** (29,531 B)

Self-check: writes confined to `raw/economics/{whattomine,galaxy-research,coinshares-research,braiins-insights,minermag}/` + this report; no git commands; wiki/, scripts/, sources/, .agent/ untouched.
