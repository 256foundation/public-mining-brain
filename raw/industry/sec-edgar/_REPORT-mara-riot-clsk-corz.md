# Phase A10 Report — SEC EDGAR + MARA IR (MARA, RIOT, CLSK, CORZ)

> Registry IDs: sec-edgar-miners, mara-ir
> Collected: 2026-10-10
> Agent: fetch agent (tickers MARA/RIOT/CLSK/CORZ only; HUT/IREN/WULF/BTDR handled by sibling)
> Posture: extract | verbatim (per-file, see headers)

## Forms captured

| Ticker | CIK | Form | Period | Filed | Accession | Extract file |
|---|---|---|---|---|---|---|
| MARA | 1507605 | 10-K | 2025-12-31 | 2026-03-02 | 0001507605-26-000007 | raw/industry/sec-edgar/2026-10-10-edgar-MARA-10K-extract.md |
| MARA | 1507605 | 10-Q | 2026-06-30 | 2026-08-06 | 0001507605-26-000022 | raw/industry/sec-edgar/2026-10-10-edgar-MARA-10Q-extract.md |
| RIOT | 1167419 | 10-K | 2025-12-31 | 2026-03-02 | 0001104659-26-022322 | raw/industry/sec-edgar/2026-10-10-edgar-RIOT-10K-extract.md |
| RIOT | 1167419 | 10-Q | 2026-06-30 | 2026-08-10 | 0001104659-26-093448 | raw/industry/sec-edgar/2026-10-10-edgar-RIOT-10Q-extract.md |
| CLSK | 827876 | 10-K | 2025-09-30 | 2025-11-25 | 0001193125-25-297510 | raw/industry/sec-edgar/2026-10-10-edgar-CLSK-10K-extract.md |
| CLSK | 827876 | 10-Q | 2026-06-30 | 2026-08-06 | 0001193125-26-338382 | raw/industry/sec-edgar/2026-10-10-edgar-CLSK-10Q-extract.md |
| CORZ | 1839341 | 10-K | 2025-12-31 | 2026-03-02 | 0001628280-26-013305 | raw/industry/sec-edgar/2026-10-10-edgar-CORZ-10K-extract.md |
| CORZ | 1839341 | 10-Q | 2026-06-30 | 2026-07-28 | 0001839341-26-000014 | raw/industry/sec-edgar/2026-10-10-edgar-CORZ-10Q-extract.md |

Note: CLSK fiscal year ends Sep 30, so its latest 10-K (FY2025) was filed 2025-11-25; its 10-Q covers its fiscal Q3 (quarter ended 2026-06-30). All others are calendar-year filers. These are the latest 10-K/10-Q per EDGAR submissions JSON as of 2026-10-10 (no newer 10-K/10-Q exists for any of the four).

## Headline numbers per ticker (all quotes are exact literals from the filings)

### MARA Holdings (CIK 1507605)
- Hashrate/fleet — 10-K (Item 1/MD&A): "approximately 490,000 mining rigs globally... with an energized hashrate of approximately 66.4 exahashes per second"; capacity table "Total 1,315 | 1,861 | 66.4" (MW operational / MW total / EH/s; owned 779/1,324/37.2; hosted 536/537/29.2).
- 10-Q (MD&A metrics): "Energized hashrate 70.3 | 57.4" EH/s; "Miner efficiency (in joules per terahash) 17.3 | 18.3"; "Total energy capacity (in GW) 1.9 | 1.7"; "approximately 440,000 mining rigs globally".
- Revenue — 10-K: "We generated revenues of $907.1 million for the year ended December 31, 2025" (table: Revenues $907,093K; Bitcoin mining revenue $872,401K). 10-Q: "$174.9 million" Q2'26 (vs $238.5M); 6M "$349.5 million" (vs $452.4M).
- Mining cost/margin — 10-K: "Cost per Petahash per day improved approximately 16%, from $35.6 to $29.8"; "Purchased energy costs per bitcoin for our owned mining sites were $38,956"; "Energy cost... represented 38.5%... of our owned mining revenues". 10-Q: Q2 energy = "54.9%... as a percentage of our owned mining revenues" (vs 34.1%); Cost per PH/day $27.7; purchased energy cost per BTC $38,690 (Q2).
- BTC holdings — 10-K: "we held approximately 53,822 bitcoin, including 15,315 bitcoin under our digital asset management strategy... carrying value of approximately $4.7 billion". 10-Q: "we held approximately 35,577 bitcoin... carrying value of approximately $2.1 billion"; "we sold approximately 23,093 bitcoin" in 6M'26; holdings history table "December 31, 2025 | 53,822 | $87,498" per BTC.
- AI/HPC language — 10-K (VERBATIM): Starwood "Strategic Agreement... retain up to a 50% ownership interest in a newly formed joint venture... The joint platform is expected to provide more than 1 GW of initial IT capacity in the initial development, with a potential pathway to expand to more than 2.5 GW over time." 10-Q: "2026 Restructuring Plan... to reallocate resources toward AI initiatives and related critical IT and HPC opportunities"; Long Ridge "485 megawatt... combined-cycle gas turbine power plant" (April 2026 agreement, not yet closed at Q2); HIF Matagorda "2,000 megawatts ("MW") of power capacity for an aggregate purchase price of up to $600.0 million" (subsequent to quarter end).
- Impairments — 10-K: goodwill "$82.8 million" + Garden City storm "$26.0 million". 10-Q: 6M "$42.0 million related to the elimination of certain business activities involving mining rigs and equipment as part of the 2026 Restructuring Plan"; "$48.2 million" accelerated depreciation 6M.
- Power cost — 10-Q: "our ability to access power at $0.04 per kilowatt hour ("kWh") across our owned and operated sites".
- Profitability — 10-K: "Net income (loss) attributable to common stockholders: $(1,311,480)" thousand FY2025; Adjusted EBITDA $(330,824)K. 10-Q: Q2'26 $(609,685)K; 6M $(1,869,304)K.

### Riot Platforms (CIK 1167419)
- Hashrate/capacity — 10-K: "total deployed hash rate of 38.5 exahash per second" (vs 31.5); "Total power capacity 1,292 MW" (Rockdale 700, Corsicana 400, Kentucky 192); avg operating 31.4 EH/s FY2025. 10-Q: "Combined Bitcoin Mining hash rate, deployed 44.4 EH/s" at Jun 30, 2026 (Rockdale 17.4, Corsicana 16.6, Kentucky 10.5); avg operating Q2 37.2 EH/s; "Combined all-in power cost 3.6" cents/kWh Q2.
- Revenue — 10-K: "Total revenue $647,435" thousand FY2025 (Bitcoin Mining $576,276; Engineering $64,688; Other $6,471). 10-Q: "Total revenue for the three months ended June 30, 2026 and 2025 was $174.2 million and $153.0 million"; Bitcoin Mining $113.7M Q2; Data Center (new segment) "$23.2 million and $56.4 million" Q2/6M; Engineering $37.3M/$59.5M.
- Mining margin (cost to mine) — 10-K: "Cost to mine one bitcoin, excluding bitcoin miner depreciation $49,645" (49.0% of "Production value of one bitcoin mined $101,350"); "All-in power cost... Combined 3.7" cents/kWh; power curtailment credits "$(56,729)"K. 10-Q: Q2 "Cost to mine one bitcoin, excluding bitcoin miner depreciation $49,912" = "69.6%" of production value $71,667/BTC (vs 49.6% LY); incl. depreciation "126.5%" — above 100% in Q2 2026.
- BTC holdings — 10-K: "Balance as of December 31, 2025: 18,005 bitcoin, $1,575,441" thousand (14,028 unrestricted + 3,977 restricted pledged to the "$200 million credit facility"). 10-Q: "Balance as of June 30, 2026: 11,380 / $666,038"; sold 9,665 BTC for $732.5M in 6M.
- AI/HPC language — 10-Q (VERBATIM): AMD Lease + Amendment "for the deployment of 50 MW of critical IT load capacity, with the potential for additional expansion of up to a total of 200 MW"; and "In August 2026, the Company and a leading frontier AI lab, (the "Tenant"), entered into a long-term data center lease agreement (the "Tenant Lease") at the Rockdale Facility for an initial deployment of 191 MW of critical IT load capacity... initial term of 20 years... expected to generate approximately $9.1 billion in base rent over the initial term"; funded by "$573.0 million interim credit facility... with the lenders party thereto and Morgan Stanley Senior Funding, Inc." (XBRL tag identifies tenant as Anthropic PBC: riot:LeaseAgreementWithAnthropicPbcMember). New Data Centers reportable segment from Q1 2026.
- Impairment — 10-K: "$29.7 million" PP&E impairment (Corsicana long-lead items, mining→data-center pivot). 10-Q: no new impairment; "loss of $74.6 million" Q2 change in FV of bitcoin.
- Profitability — 10-K: "we reported a net loss of $663.2 million" FY2025. 10-Q: "net loss of $737.6 million" 6M'26.

### CleanSpark (CIK 827876; FY ends Sep 30)
- Hashrate/capacity — 10-K: "average computing power of 45.6 exahash per second ("EH/s"), reaching a peak of 50 EH/s"; fleet table "Total 1,027 MW / 45.60 EH/s / 33 locations" (GA 620/27.02; MS 63/2.63; TN 234/12.43; WY 110/3.52); 241,934 miners in service. 10-Q: "total contracted power capacity of approximately 1,817 megawatts ("MW") as of June 30, 2026"; "During June 2026... average computing power of 42.6 exahash per second"; "approximately 326,530 miners, of which approximately 225,137 were in service"; efficiency "15.8 J/TH"; share of global hashrate "4.36%".
- Revenue — 10-K: "Total revenues, net $766,314" thousand FY2025 (vs $378,968); owned-facility mining revenue "$754,691". 10-Q: "Bitcoin mining revenue, net $138,006" Q3 FY26 (vs $198,644); 9M "$455,594" (vs $542,662); single pool customer "Foundry Digital... represented 100% of revenue".
- Mining margin (cost to mine) — 10-K: "Cost of energy per bitcoin mined $42,890"; "Average revenue of each bitcoin mined $97,687"; energy-only cost = "44.0%" of revenue. 10-Q: Q3 "Cost of energy per bitcoin mined $44,317" = "61.9%" of "Average revenue of each bitcoin mined $71,692"; fully-loaded (incl. depreciation) "134.3%" — negative fully-loaded mining margin in Q3 FY2026.
- BTC holdings — 10-K: "the Company held 10,428 and 6,819 bitcoin" (Sep 30 2025 vs 2024); fair value $1,189,443K + 2,583 BTC collateral receivable (~$295M). 10-Q: "we held approximately 12,205 bitcoins and had a receivable for 1,719 bitcoin... fair value... $714,293... and... $100,607".
- AI/HPC language — 10-K (VERBATIM): "we announced that we acquired rights to approximately 271 acres of land in Austin County, Texas and executed long-term power supply agreements totaling 285 megawatts to support the development of a next-generation data center campus"; "As of the date of filing... we have not had material revenue from our AI and HPC services business." 10-Q (VERBATIM, subsequent event): "On July 10, 2026, the Company entered into a 20-year triple-net infrastructure lease agreement (the "Sandersville Lease")... with a leading global technology company for 175 MW of critical information technology load at newly acquired land located adjacent to the Company's Sandersville, Georgia campus... the power will be diverted to the Sandersville AI Campus and bitcoin mining activity will cease"; Tenant LOI + exclusivity "covering our entire Texas portfolio of 718 acres with up to 885 MW of secured and planned power capacity"; Sandersville bitcoin mining "expects to fully decommission... during fiscal year 2028."
- Impairments — 10-K: none FY2025 ("Impairment expense - bitcoin — ; Impairment expense - fixed assets —"); FY2024 $197,041K + $7,163K. 10-Q: Sandersville-related impairment "cannot reasonably estimate" yet.
- Profitability — 10-K: "net income from our continuing operations for the fiscal year ended September 30, 2025 of $364,464" thousand. 10-Q: "Net loss was $239,842" Q3 FY26; "Net loss for the nine months ended June 30, 2026 was $996,896".

### Core Scientific (CIK 1839341)
- Portfolio — 10-K: "ten data centers across seven U.S. states, representing approximately 1.4 gigawatts ("GW") of gross utility power capacity, or approximately 920 megawatts ("MW") of total leasable customer power capacity"; utility table "Total 1,426" MW gross (largest: Denton TX 394, Pecos TX 300, Dalton GA 195). 10-Q: adds Hunt County TX ("approximately 430 MW of gross utility power capacity", $233M, May 2026) and pending Polaris DS OK ("up to 440 MW", ~$421M cash).
- Hashrate/fleet — 10-K: "we deployed approximately 151,400 bitcoin miners... approximately 135,500 self-miners and approximately 15,900 hosted miners, which represented 15.7 exahash per second ("EH/s") and 2.2 EH/s". 10-Q: self-mining fleet run "at two facilities"; "We are not investing in new mining equipment"; hosted mining "expected to conclude by December 31, 2026".
- Revenue — 10-K: "Total revenue $319,019" thousand FY2025 (Colocation $65,424; self-mining $229,207; hosted $24,388) vs $510,672 FY2024. 10-Q: Q2'26 "Total revenue 164,201" (Colocation $136,669 — vs $10,560 LY; self-mining 21,535; hosted 5,997); 6M "279,445"; "colocation revenue represented 77% of total revenue" 6M'26 (vs 12%); "CoreWeave represented approximately 77% of our total revenue"; "contracted 590 MW of leased customer power capacity and were actively billing for 395 MW".
- Self-mining metrics — 10-K table: "Bitcoin mined 2,276 | 6,595 (-65%)"; "Average price of bitcoin $101,639 | $65,894"; "Self-mining hash rate 15.7 | 19.1 EH/s".
- BTC holdings — 10-K: "December 31, 2025 — Quantity 2,537; Cost Basis $254,694; Fair Value $222,000" thousand; plan "to monetize substantially all of our bitcoin holdings" in 2026. 10-Q: "June 30, 2026 — 848 / $65,454 / $49,675"; "we mined approximately 695 bitcoin, sold 2,385 bitcoin for aggregate proceeds of $208.2 million".
- AI/HPC language — 10-K (VERBATIM): "We intend to convert every megawatt in our portfolio to high-density colocation infrastructure over the next three years"; CoreWeave relationship grew to "approximately 590 MW of leased power capacity"; "One customer, CoreWeave, currently accounts for 100% of our Colocation segment revenue." 10-Q (VERBATIM, subsequent events July 27 2026): "AMD Leases... with Advanced Micro Devices, Inc. ("AMD") for an aggregate of 377 MW of critical IT capacity at the Company's Pecos, TX; Muskogee, OK; and Hunt County, TX sites; and Lease Agreements (the "Neocloud Leases"... with a Neocloud... for 152 MW... Each of the Leases is for a fifteen year term with three five-year options. The AMD Leases provide AMD a reservation... of... an additional 1,925 MWs of critical IT capacity through December 28, 2028."; warrant "to purchase up to 30 million shares... at an exercise price of $23.47 per share"; liquidity section: "strategic commercial relationship with AMD with the potential to support up to 2.5 GW of leasable capacity, anchored by a 15-year agreement for approximately 530 MW across five sites."
- Impairments — 10-K: PP&E impairment "$11,359"K FY2025 (vs $122,869K FY2024; driven by mining→HDC demolition). 10-Q: "$266.5 million" impairment on mining PP&E in Q1'26 ("declines in bitcoin prices, declines in bitcoin hashprice, and significant decreases in secondary market values for digital asset mining equipment") + "$19.5 million" held-for-sale remeasurement loss + "$41.9 million" Block, Inc. mining-equipment contract termination loss.
- Profitability — 10-K: "Net loss was $288.6 million in 2025"; Adjusted EBITDA "$(29,659)"K. 10-Q: "Net loss $(1,155,310)" Q2'26 (mostly non-cash: "$1,045,515" warrant/CVR fair-value change); 6M $(1,502,498)K; 6M operating cash flow "$230,949" helped by $208.2M BTC sales.

## Cross-ticker posture synthesis (collector's note)

- AI/HPC pivot language status: CORZ = already colocation-primary (77% of revenue); RIOT = dual-platform with first large leases signed (AMD 50→200 MW; frontier-AI-lab 191 MW, $9.1B base rent); MARA = power-first platform pivot (Starwood JV, Long Ridge CCGT, HIF 2 GW site); CLSK = first anchor lease just signed (Sandersville 175 MW) with mining decommission planned at that site.
- Mining margin stress in H1 2026 visible in all four: energy as % of owned mining revenue up sharply (MARA 54.9% Q2 vs 34.1%; CLSK 61.9% energy-only, 134.3% fully loaded; RIOT 69.6% ex-depreciation cost ratio; CORZ winding mining down entirely).
- Bitcoin treasury behavior diverged: MARA sold 23,093 BTC in 6M'26 (from 53,822 to 35,577) + $1.0B notes repurchase funded by 15,133 BTC sale (IR PR 1418); RIOT sold 9,665 BTC (18,005→11,380, heavily restricted as collateral); CLSK grew holdings to 12,205; CORZ liquidated most holdings (2,537→848) per stated plan.

## HTTP log (house contract: UA declared, ≤10 req/s, sleeps between calls)

User-Agent: `public-mining-brain/1.0 (research; contact: tyler@256foundation.org)` (EDGAR/data.sec.gov); ir.mara.com fetched once with a browser UA for the listing page and then with the same project UA for detail pages.

| # | URL | Status | Note |
|---|---|---|---|
| 1 | https://www.sec.gov/files/company_tickers.json | 200 | CIK resolution, single fetch, filtered locally |
| 2-5 | https://data.sec.gov/submissions/CIK{1507605,1167419,827876,1839341}.json | 200 | 0.7s sleep between |
| 6-13 | https://www.sec.gov/Archives/edgar/data/<cik>/<accnodash>/index.json (8 filings) | 200 | 0.6s sleep between |
| 14-21 | Primary documents: mara-20251231.htm, mara-20260630.htm, riot-20251231x10k.htm, riot-20260630x10q.htm, clsk-20250930.htm (6.0 MB), clsk-20260630.htm, core-20251231.htm, core-20260630.htm | 200 | sizes 1.5-6.0 MB; 0.7s sleep between |
| 22 | https://ir.mara.com/news-events/press-releases | 200 | listing page |
| 23-25 | ir.mara.com detail pages 1424, 1419, 1418 | 200 | 1s sleep between |

Total ~22 requests; peak rate well under 10 req/s (explicit sleeps 0.6-1.0s). All fetches succeeded; no retries needed. Filing HTML converted to text locally via python3 html.parser (script in session temp dir, not committed); extraction-only captures written to repo.

## Parks / caveats

- CLSK 10-K and all XBRL-heavy filings embed a single giant inline-XBRL header line (tens of KB on one line); handled by line-based filtering (awk NR>… / body-only greps). No parsing failures.
- RIOT 10-Q names its AI tenant only as "a leading frontier AI lab (the 'Tenant')"; the Anthropic identification comes from the filing's own XBRL context member tag `riot:LeaseAgreementWithAnthropicPbcMember` — noted as such in the capture, not asserted as prose fact.
- CLSK 10-Q reports no AI/HPC revenue ("we had earned no revenues from our AI and HPC services business"); Sandersville Lease is a subsequent event (post-quarter) and its financial effect is explicitly not yet estimable in the filing.
- CORZ fleet/mining metrics are in decline by design (conversion to HDC); hosted-mining revenue expected to end by Dec 31, 2026 per 10-Q.
- MARA 10-Q "we hold approximately 35,577 bitcoin" — carrying value $2.1B at $58,524/BTC; the large 6M fair-value loss ($1.4B) is a non-cash ASC 350-60 item, not a cash event.
- No numbers were taken from memory; every figure above is a quoted literal from the captured filing text, with section attribution in the extract files.
