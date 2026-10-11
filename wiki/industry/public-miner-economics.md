# Public Miner Economics

> Sources: SEC EDGAR latest annual + quarterly filings for eight listed miners (MARA RIOT CLSK CORZ HUT IREN WULF BTDR; BTDR files 20-F/6-K as a foreign private issuer), captured 2026-10-10 via data.sec.gov submissions JSON with the house User-Agent and ≤10 req/s; MARA investor-relations press releases; Crusoe, Upstream Data, Giga Energy vendor sites
> Raw: [MARA 10-K FY2025](../../raw/industry/sec-edgar/2026-10-10-edgar-MARA-10K-extract.md); [MARA 10-Q Q2'26](../../raw/industry/sec-edgar/2026-10-10-edgar-MARA-10Q-extract.md); [RIOT 10-K FY2025](../../raw/industry/sec-edgar/2026-10-10-edgar-RIOT-10K-extract.md); [RIOT 10-Q Q2'26](../../raw/industry/sec-edgar/2026-10-10-edgar-RIOT-10Q-extract.md); [CLSK 10-K FY2025](../../raw/industry/sec-edgar/2026-10-10-edgar-CLSK-10K-extract.md); [CLSK 10-Q FQ3'26](../../raw/industry/sec-edgar/2026-10-10-edgar-CLSK-10Q-extract.md); [CORZ 10-K FY2025](../../raw/industry/sec-edgar/2026-10-10-edgar-CORZ-10K-extract.md); [CORZ 10-Q Q2'26](../../raw/industry/sec-edgar/2026-10-10-edgar-CORZ-10Q-extract.md); [HUT 10-K FY2025](../../raw/industry/sec-edgar/2026-10-10-edgar-HUT-10K-extract.md); [HUT 10-Q Q2'26](../../raw/industry/sec-edgar/2026-10-10-edgar-HUT-10Q-extract.md); [IREN 10-K FY2026](../../raw/industry/sec-edgar/2026-10-10-edgar-IREN-10K-extract.md); [IREN 10-Q Q3 FY26](../../raw/industry/sec-edgar/2026-10-10-edgar-IREN-10Q-extract.md); [WULF 10-K FY2025](../../raw/industry/sec-edgar/2026-10-10-edgar-WULF-10K-extract.md); [WULF 10-Q Q2'26](../../raw/industry/sec-edgar/2026-10-10-edgar-WULF-10Q-extract.md); [BTDR 20-F FY2025](../../raw/industry/sec-edgar/2026-10-10-edgar-BTDR-20F-extract.md); [BTDR 6-K H1'26](../../raw/industry/sec-edgar/2026-10-10-edgar-BTDR-6K-extract.md); [EDGAR report MARA/RIOT/CLSK/CORZ](../../raw/industry/sec-edgar/_REPORT-mara-riot-clsk-corz.md); [EDGAR report HUT/IREN/WULF/BTDR](../../raw/industry/sec-edgar/_REPORT-hut-iren-wulf-btdr.md); [MARA IR: Long Ridge](../../raw/industry/mara-ir/2026-10-10-mara-ir-pr-long-ridge-acquisition-verbatim.md); [MARA IR: HIF Texas 2GW](../../raw/industry/mara-ir/2026-10-10-mara-ir-pr-hif-texas-2gw-verbatim.md); [Crusoe about/timeline](../../raw/industry/crusoe/2026-10-10-crusoe-about-company.md); [Crusoe home](../../raw/industry/crusoe/2026-10-10-crusoe-home.md); [Crusoe NYDIG exit PR](../../raw/industry/crusoe/2026-10-10-crusoe-newsroom-nydig-bitcoin-exit.md); [Upstream BlackBox](../../raw/industry/upstream-data/2026-10-10-upstream-black-box.md); [Upstream Hash Generator](../../raw/industry/upstream-data/2026-10-10-upstream-hash-generator.md); [Giga demand-charge economics](../../raw/industry/giga-energy/2026-10-10-giga-cost-of-mining-a-bitcoin.md); [Giga home](../../raw/industry/giga-energy/2026-10-10-giga-home.md); [Giga demand response](../../raw/industry/giga-energy/2026-10-10-giga-bitcoin-mining-demand-response.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10 — filings snapshot; latest 10-K/10-Q (or 20-F/6-K) per ticker at capture
> Status: Draft

## Overview

The eight miners Tyler tracks (MARA RIOT CLSK CORZ HUT IREN WULF BTDR) filed a synchronized story in 2026: **mining margins went negative on a fully-loaded basis for several of them, bitcoin treasuries diverged into sellers and accumulators, and every one of the eight now describes its growth as AI/HPC infrastructure** — with contract values ($9.1B, $9.7B, $19.6B) that dwarf mining revenue. This page is the filings-level view; the market-side context (hashprice "$39.44 / PH/DAY" As-Of Oct 2026 — [homepage snapshot](../../raw/economics/hashrate-index/2026-10-10-homepage-snapshot.md); forward curve) is in [Hashprice and Difficulty](../economics/hashprice-and-difficulty.md), and the dated event ledger is in [Network State 2022–2026](network-state-2022-2026.md).

## The cohort (latest filings, As-Of 2026-10-10)

| Ticker | Latest forms (period) | Hashrate | Power | Revenue signal | BTC held | Pivot stage |
|---|---|---|---|---|---|---|
| MARA | 10-K FY25 (filed 3/2/26); 10-Q Q2'26 | "Energized hashrate 70.3" EH/s (from 66.4) | "Total energy capacity (in GW) 1.9" | Q2'26 rev "$174.9 million" | 35,577 (sold "approximately 23,093" in 6M) | JV + gas-plant M&A |
| RIOT | 10-K FY25; 10-Q Q2'26 | "44.4 EH/s" deployed (6/30/26) | "Total power capacity 1,292 MW" | Q2 mining rev $113.7M | 11,380 (sold 9,665 for $732.5M) | 200 MW AMD + 191 MW AI-lab lease |
| CLSK | 10-K FY25 (Sep FYE); 10-Q FQ3'26 | "42.6 exahash per second" (Jun 2026) | "1,817 megawatts" contracted | Q3 mining rev "$138,006"K | 12,205 + 1,719 receivable (grew) | First anchor lease signed |
| CORZ | 10-K FY25; 10-Q Q2'26 | self-mining "at two facilities"; hosted "expected to conclude by December 31, 2026" | "920 MW of total leasable customer power capacity, or 1.4 GW on a gross utility power capacity basis" (10-K) + Hunt 430 MW | colocation = "77% of total revenue" | 848 (monetizing) | Colocation-primary |
| HUT | 10-K FY25; 10-Q Q2'26 | 5.6→"9.3EH/s" (contributed to American Bitcoin) | "1,020 megawatts of energy capacity under management"; "9,370 MW" pipeline | FY25 rev $235.1M | 17,316 (grew) | AI leases signed, big |
| IREN | 10-K FY26 (Jun FYE); 10-Q Q3 FY26 | "23.2 EH/s" installed (Jun 30) | 4,510 MW portfolio | FY26 rev $707.0M | 0 ("liquidate all the Bitcoin we mine daily") | AI Cloud primary growth |
| WULF | 10-K FY25; 10-Q Q2'26 | "10.6 EH/s" (Jun 30, 2026) | 522 MW critical IT contracted | Q2'26: HPC lease revenue "31,932" $K > digital asset revenue "12,835" $K | 2 (essentially none) | "HPC hosting as its primary business" |
| BTDR | 20-F FY25; 6-K H1'26 | "78.1 EH/s under management" | "~3,003.5 MW" incl. pipeline | FY25 rev $620.3M, net profit $65.6M | (custody, related party) | Rigs + AI conversion both |

## Mining-margin stress (H1–Q3 2026, per filings)

- **Riot**: Q2'26 "Cost to mine one bitcoin, excluding bitcoin miner depreciation $49,912" = "69.6%" of production value ($71,667/BTC); including depreciation "126.5%" — "above 100% in Q2 2026". FY25 baseline was 49.0% excluding depreciation.
- **CleanSpark**: FQ3'26 "Cost of energy per bitcoin mined $44,317" = "61.9%" of average revenue "$71,692"; fully-loaded "134.3%" — negative fully-loaded mining margin. Its only pool customer is "Foundry Digital... represented 100% of revenue".
- **MARA**: Q2'26 energy costs = "54.9%... as a percentage of our owned mining revenues" (vs 34.1% a year earlier); even the FY25 10-K showed "Cost per Petahash per day improved approximately 16%, from $35.6 to $29.8" while revenue per PH fell faster.
- **Core Scientific** already exited the comparison: "We are not investing in new mining equipment"; self-mining shrank to two facilities.
- Context: the energy-tier margin ladder (Luxor, Sep 2026) shows industrial break-even at "~$51/MWh for 25–38 J/TH" against a "$48/MWh" average power cost ([Lookback Sep 2026](../../raw/economics/hashrate-index/2026-10-10-lookback-september-2026.md)) — the filings' cost ratios are that ladder showing up in audited numbers. See [Hashprice and Difficulty](../economics/hashprice-and-difficulty.md).

## BTC treasury divergence (12/31/25 → 6/30/26)

| Ticker | Held start | Held end | Behavior |
|---|---|---|---|
| MARA | 53,822 | 35,577 | "we sold approximately 23,093 bitcoin" — funding the pivot |
| RIOT | 18,005 | 11,380 | sold 9,665 for $732.5M; 3,977 were restricted (pledged) |
| CLSK | 10,428 (+2,583 collateral recv.) | 12,205 + 1,719 recv. | kept HODLing |
| CORZ | 2,537 | 848 | "to monetize substantially all of our bitcoin holdings" |
| HUT | 15,679 | 17,316 | still accumulating; 3,090 pledged |
| IREN | 0 | 0 | "liquidate all the Bitcoin we mine daily" |
| WULF | 3 | 2 | essentially no treasury |
| BTDR | n/d (custody at BIT Group) | 34,762 $K digital assets (6/30/26) | "strategically manage[d]" |

Read: the "HODL-or-die" era is over for half the cohort — the 2026 cycle funds AI capex partly from treasury sales.

## The AI/HPC pivot, in the filers' own words (verbatim)

- **CORZ** (furthest along): "We intend to convert every megawatt in our portfolio to high-density colocation infrastructure over the next three years"; "One customer, CoreWeave, currently accounts for 100% of our Colocation segment revenue."; July 2026 AMD Leases "for an aggregate of 377 MW" + Neocloud 152 MW, 15-year terms, with an AMD reservation of "an additional 1,925 MWs" — "the potential to support up to 2.5 GW of leasable capacity".
- **WULF**: "TeraWulf has undergone a deliberate strategic transition toward HPC hosting as its primary business."; Fluidstack 378 MW at Lake Mariner "benefit from substantial credit support provided by Google" (Google Backstop warrants fair-value swing "$971,992"K in Q2'26 P&L).
- **IREN**: five-year Microsoft agreement "representing approximately $9.7" billion (Horizon 1–4 GPU data centers, signed with Microsoft in November 2025 per the 10-K); "We aim to substantially complete this transition by December 31, 2026." — all Childress mining capacity converts to AI cloud.
- **HUT**: Anthropic + Fluidstack partnership, 15-year triple-net "245 MW of AI data center IT capacity at our River Bend campus"; Beacon Point: "total contracted critical IT capacity to 704 MW", "approximately $19.6 billion" of aggregate base contract value.
- **RIOT**: AMD lease ("50 MW of reserved capacity" now; "increase to 200 MW" if both expansion options are exercised); and (Aug 2026) "a leading frontier AI lab" — "191 MW of critical IT load capacity", "initial term of 20 years", "approximately $9.1 billion in base rent" (the XBRL tag names the tenant: `riot:LeaseAgreementWithAnthropicPbcMember`); funded by a "$573.0 million interim credit facility" (Morgan Stanley Senior Funding, Inc.).
- **CLSK**: "20-year triple-net infrastructure lease agreement" (the Sandersville Lease) "for 175 MW of critical information technology load" where "bitcoin mining activity will cease" (subsequent event; Sandersville mining "expects to fully decommission... during fiscal year 2028"); Texas LOI "up to 885 MW".
- **MARA**: Starwood JV "more than 1 GW of initial IT capacity" in initial development, pathway to expand to more than 2.5 GW over time (10-K); "2026 Restructuring Plan... to reallocate resources toward AI initiatives"; Long Ridge "485 megawatt... combined-cycle gas turbine power plant" (IR PR verbatim) and HIF Matagorda "2,000 megawatts ("MW") of power capacity for an aggregate purchase price of up to $600.0 million".
- **BTDR**: converting Tydal (Norway), Knoxville (TN), Wenatchee (WA) "into AI datacenters"; AI cloud "remains at an early stage" ($6.8M FY25); SEALMINER rig sales are "our second largest revenue source" for FY25, "representing approximately 17.5%" of revenue.

## The cost side: demand charges (Giga Energy)

The filings show energy as 54.9–77% of mining revenue at industrial scale; Giga Energy's January 2026 post is the cleanest public walkthrough of why billed $/kWh understates the true number:

- Demand charges of "$10–$20/kW" on a 5 MW peak = "$50K–$100K/mo"; demand is "30-50%" of the bill, adding "$0.02–$0.04/kWh".
- Worked example: "$0.05/kWh. Your demand charges, when spread across total consumption, add another $0.025/kWh. Capacity and transmission fees add $0.015/kWh. Added together, your all-in cost is $0.09/kWh; an 80% increase over the rate you probably used to model profitability".
- Grid participation cuts all-in to "$0.06-$0.09/kWh" — "an additional $20,000 to $80,000 per MW per year, depending on your region and market structure"; Giga runs "175+ MW" of flex load (500 MW under development) and in SPP markets "stacked revenue streams can deliver up to $80,000 per MW annually".
- Home-miner relevance: residential bills hide demand-charge mechanics behind tiered rates — the industrial cost ladder these filings show is why home heat-first economics diverge (see [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)).

## The wasted-energy vendor base, post-pivot

- **Crusoe** — the bellwether exit. Timeline: 2018 "pioneering technology to convert wasted natural gas into energy" → 2025 "Divest our bitcoin mining business to NYDIG to focus exclusively on AI infrastructure" (about-page timeline, verbatim). The exit PR (3/25/2025) tallies the mining era: Crusoe "deployed more than 425 modular data centers (250+ MWs) in the field" across seven states and two countries, with the operation and teams moving to NYDIG. Homepage now: "The AI factory company" ($3.9B Series F).
- **Upstream Data** — still mining-first (domain moved .ca → **upstreamdata.com**): BlackBox™ container line, three models in a "(kW)" column reading 8 / 20 / 40 (2/6/12 miner slots), chips "45 kW Max power" and "30 dB Sound reduction"; Hash Generator™ gas gensets "50–325 kW" from "10-100 mcf/d" wells with LoadSync™ control. The off-grid/field-gas niche the public miners left behind.
- **Giga Energy** — "modular AI data center developer" positioning with Giga Box Air/Hydro mining containers and an active bitcoin blog (posts through Oct 2026); the demand-charge and demand-response posts above are the working economics library.

## Disputed / caveats

> **Status: Disputed** — RIOT's "$9.1B" tenant
> The 10-Q prose says "a leading frontier AI lab, (the "Tenant")"; the XBRL member tag identifies the tenant as Anthropic PBC (`riot:LeaseAgreementWithAnthropicPbcMember`). HUT's 10-K names Anthropic for its own Fluidstack deal in prose. Recorded both ways; use the XBRL identification with that caveat.

- CLSK's 10-K covers Oct 2024–Sep 2025 (Sep FYE) — its "FY2025" is a year offset vs the calendar filers.
- IREN's June FYE means its latest annual (FY2026, filed 2026-08-27) is newer than everyone else's; its latest 10-Q is the March quarter (no June-quarter 10-Q exists — the 10-K covers it).
- BTDR files 20-F/6-K (FPI): the quarterly equivalent is a 6-K with interim FS filed 2026-09-29, named `-6K-` in captures.
- RIOT's "Data Center" and CORZ's colocation revenue make cross-ticker "revenue" non-comparable; segment splits are in each extract.

## See Also

- [Hashprice and Difficulty](../economics/hashprice-and-difficulty.md) — the market variable all of this responds to
- [Network State 2022–2026](network-state-2022-2026.md) — dated corporate-event ledger (this phase extends the 2026 rows)
- [On-Demand Hashrate](../hashrate-market/on-demand-hashrate.md) — the rental market converting miners into hosts
- [Hashrate Heating Economics](../economics/hashrate-heating-economics.md) — the home-scale version of the same cost math
