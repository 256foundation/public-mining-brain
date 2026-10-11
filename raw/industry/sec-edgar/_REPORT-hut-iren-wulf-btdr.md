# A10 SEC EDGAR capture — HUT / IREN / WULF / BTDR

> Registry ID: sec-edgar-miners
> Collected: 2026-10-10
> Posture: extract (targeted windows, not full filings)
> Agent: hut-iren-wulf-btdr subagent
> Files: 8 extracts (this dir) + this report

## 0. Files written

| File | Form | Period | Filed | Accession |
|---|---|---|---|---|
| 2026-10-10-edgar-HUT-10K-extract.md | 10-K | 2025-12-31 | 2026-02-25 | 0001104659-26-019392 |
| 2026-10-10-edgar-HUT-10Q-extract.md | 10-Q | 2026-06-30 | 2026-08-04 | 0001104659-26-090025 |
| 2026-10-10-edgar-IREN-10K-extract.md | 10-K | 2026-06-30 | 2026-08-27 | 0001878848-26-000052 |
| 2026-10-10-edgar-IREN-10Q-extract.md | 10-Q | 2026-03-31 | 2026-05-08 | 0001878848-26-000026 |
| 2026-10-10-edgar-WULF-10K-extract.md | 10-K | 2025-12-31 | 2026-02-27 | 0001083301-26-000031 |
| 2026-10-10-edgar-WULF-10Q-extract.md | 10-Q | 2026-06-30 | 2026-08-05 | 0001083301-26-000166 |
| 2026-10-10-edgar-BTDR-20F-extract.md | 20-F | 2025-12-31 | 2026-04-30 | 0001213900-26-049770 |
| 2026-10-10-edgar-BTDR-6K-extract.md | 6-K (interim FS, ex-99.1) | 2026-06-30 | 2026-09-29 | 0001213900-26-104638 |

CIKs (from company_tickers.json): HUT = 1964789 "Hut 8 Corp."; IREN = 1878848 "IREN Ltd"; WULF = 1083301 "TeraWulf Inc."; BTDR = 1899123 "Bitdeer Technologies Group".

## 1. HUT — Hut 8 Corp. (Nasdaq: HUT)

Forms: 10-K FY2025 (2025-12-31, filed 2026-02-25, acc 0001104659-26-019392); 10-Q Q2 2026 (2026-06-30, filed 2026-08-04, acc 0001104659-26-090025). Note: Hut 8 Corp. is the post-merger entity (legacy Hut 8 Mining Corp + US Bitcoin Corp "Business Combination"); reporting segments were renamed — "Our previous reporting segments were Digital Asset Mining, Managed Services, High Performance Computing – Colocation and Cloud, and Other" → now Power, Digital Infrastructure, Compute, Other (10-K).

Headline numbers (literal quotes):
- Energy capacity: "As of December 31, 2025, our platform spanned 1,020 megawatts of energy capacity under management across 15 sites in the United States and Canada … 330 megawatts of energy under construction at one site in Louisiana; 1,230 megawatts of energy capacity under development across three sites in Texas and Illinois; 1,755 megawatts of energy capacity under exclusivity; and 5,185 megawatts of energy capacity under diligence." (10-K). 10-Q KPI table: "Energy Capacity Under Development 550 MW … Energy Capacity Under Construction 830 MW … Energy Capacity Under Management 710 MW … Total Energy Capacity Pipeline 9,370 MW" (vs 1,020 MW managed / 8,560 MW pipeline at 12/31/25; decline reflects Q1 2026 divestiture of four Ontario gas plants, Far North JV, ~310 MW).
- Development pipeline: "our development pipeline comprised approximately 8,500 MW of capacity" (10-K, 12/31/25).
- Revenue: "Total revenue was $235.1 million and $162.4 million for the twelve months ended December 31, 2025, and 2024 respectively" (10-K MD&A). 10-Q consolidated: Q2 2026 "Total revenue 74,932" vs "41,299" ($K; six months 145,949 vs 63,114) — Compute segment $72,471K of it.
- Hashrate: "increase in deployed hashrate from approximately 5.6EH/s to 9.3EH/s and an improvement in average fleet efficiency from approximately 31.7 J/TH to 20 J/TH. These miners were contributed to American Bitcoin" (10-K). American Bitcoin separately bought "16,299 of the Bitmain Miners, representing a total of approximately 14.02 EH/s, for a total purchase price of approximately $314.0 million, paid through the pledge of 2,234 Bitcoin" (10-Q).
- BTC held: "Number of Bitcoin held as of December 31, 2025 15,679 / pledged to Bitmain 3,744 / cost basis $1,057,990" ($K, 10-K); "Number of Bitcoin held as of June 30, 2026 17,316 / pledged 3,090 / cost basis $1,141,496" ($K, 10-Q).
- AI/HPC pivot (verbatim): "In December 2025, we announced a strategic partnership with Anthropic, PBC ('Anthropic') and Fluidstack Ltd. ('Fluidstack') to develop AI data center infrastructure. As part of the partnership, we entered into a 15-year, triple-net lease with Fluidstack for 245 MW of AI data center IT capacity at our River Bend campus ('River Bend') in Louisiana. The agreement grants Fluidstack a Right of First Offer for up to an additional 1,000 MW of IT capacity at future expansion phases" (10-K); River Bend "will commercialize 330 MW of utility capacity and is targeted for initial delivery and commissioning in Q2 2027" (10-K). Q2 2026: "Beacon Point Phase 2 comprises 352 MW of additional critical IT capacity (approximately 500 MW utility capacity) … estimated base contract value of approximately $9.8 billion over its 15-year initial term … bringing Beacon Point's total contracted critical IT capacity to 704 MW (approximately 1 GW utility capacity). Together, the two leases represent approximately $19.6 billion of aggregate base [contract value]" with "the same high-investment-grade technology company that is the tenant for Beacon Point Phase 1" (10-Q).
- Margin: no "mining margin" metric; Compute cost of revenue "$78.4 million and $45.0 million for the twelve months ended December 31, 2025 and 2024" (10-K); Q2 2026 total cost of revenue "$26.9 million and $21.8 million" (10-Q); avg revenue per BTC mined fell "from approximately $98,320 to approximately $71,905" (10-Q).
- Impairments: risk-factor language on American Bitcoin equity ("may decline significantly, which could result in impairment charges"); no large FY2025 impairment charge surfaced in extract windows.
- Parks/sites: Salt Creek + Medicine Hat (Alberta), Vega (TX), Drumheller (AB, "reenergized" March 2026 for ~11,298 ABTC miners ≈ 3.05 EH/s), River Bend (St. Francisville, LA), Beacon Point (Nueces County, TX), 5 cloud/colocation data centers in BC & Ontario (TeraGo, 200+ customers), 4 Ontario gas plants via Far North JV (divested Feb 2026), King Mountain JV (TX).

## 2. IREN — IREN Limited (Nasdaq: IREN; EDGAR name "IREN Ltd")

Forms: 10-K FY2026 (period 2026-06-30, filed 2026-08-27, acc 0001878848-26-000052); 10-Q Q3 FY2026 (period 2026-03-31, filed 2026-05-08, acc 0001878848-26-000026). Fiscal-year quirk: FYE = June 30, so the latest annual is FY2026 (not FY2025 — that 10-K, period 2025-06-30, was filed 2025-08-28 and is superseded); the June quarter is covered by the 10-K, so the latest 10-Q is the March quarter (Q3 FY2026).

Headline numbers (literal quotes):
- Revenue: "Our total revenue was $707.0 million for the year ended June 30, 2026, compared to total revenue of $501.0 million for the year ended June 30, 2025." (10-K)
- Profitability: "We generated net income (loss) of $(702.6) million for the year ended June 30, 2026 compared to net income (loss) of $86.9 million for the year ended June 30, 2025. We generated Adjusted EBITDA of $245.7 million and $269.7 [million]" (10-K). Loss driven by AI buildout (depreciation, GPU purchases) per MD&A.
- Hashrate: "As of June 30, 2026, our installed Bitcoin mining capacity was approximately 23.2 EH/s, representing approximately 380MW of data center capacity." (10-K); "Our average operating hashrate increased to 36.5 EH/s for the year ended June 30, 2026 as compared to 25.7 EH/s for the year ended June 30, 2025." (10-K); "As of March 31, 2026, we had installed hashrate capacity of approximately 38 EH/s." (10-Q).
- BTC held: "We typically liquidate all the Bitcoin we mine daily and therefore did not have any Bitcoin held on our balance sheet as of June 30, 2026." (10-K; identical policy stated as of 3/31/26 in 10-Q).
- AI/HPC pivot (verbatim): "We aim to substantially complete this transition [of data center capacity toward AI Cloud Services] by December 31, 2026." (10-K); "we announced a five-year agreement with Microsoft in November 2025, which includes GPU acquisitions and the development of the 'Horizon 1,' 'Horizon 2,' 'Horizon 3' and 'Horizon 4' data center facilities representing approximately $9.7 [billion]" (10-K); "Horizon 1 was delivered to, and accepted by, Microsoft in August 2026, Horizon 2-4 is targeted for delivery in phases in calendar Q4 2026" (10-K); "As of June 30, 2026, our operating AI Cloud Services capacity represented approximately 40MW." (10-K); 10-Q defines the pivot: "operate and expand our high-performance computing ('HPC') business (including our AI Cloud Services business and, potentially, colocation services such as powered shell, build-to-suit and turnkey data centers ('Colocation Services') (collectively 'HPC and AI services'))".
- Q3 FY2026 P&L (10-Q, $K): "Bitcoin mining revenue $111,160 … AI Cloud Services revenue 33,635 … Total revenue 144,795" (vs 141,242 / 3,581 / 144,823 prior year); nine months FY26: 511,502 / 58,280 / 569,782. Electricity cost (Bitcoin mining) nine months: "$165,390" (10-Q).
- Childress transition: "the development of 150MW of additional direct-to-chip liquid cooling data centers at the Childress campus (Horizons 5 and 6). As part of the transition, the Group expects all Bitcoin mining operations at Childress to cease over time" (10-Q).
- Impairment: risk language — "re-purposing data centers historically used for Bitcoin mining, along with the related impairment charges we may incur upon retirement of existing Bitcoin mining hardware, which could be material" (10-K).
- Parks: "seven data center sites … representing 4,510MW of total power capacity: … Childress (750MW), Sweetwater 1 (1,400MW) and Sweetwater 2 (600MW), one in Oklahoma (1,600MW) … and three in British Columbia … Canal Flats (30MW), Mackenzie (80MW) and Prince George (50MW)" (10-Q); 10-K pipeline adds Kiowa OK 1,600MW, Bundey (South Australia) 800MW, Badajoz (Spain) 300MW. Balance sheet 3/31/26: cash $2,213.3M; convertible notes payable $3,687.8M; nine-month financing inflow $3,968.8M (10-Q).

## 3. WULF — TeraWulf Inc. (Nasdaq: WULF)

Forms: 10-K FY2025 (2025-12-31, filed 2026-02-27, acc 0001083301-26-000031); 10-Q Q2 2026 (2026-06-30, filed 2026-08-05, acc 0001083301-26-000166). (FY2024 10-K/A and Q1-2025 10-Q/A exist; originals for FY2025/Q2-2026 captured.)

Headline numbers (literal quotes):
- AI/HPC pivot (verbatim): "TeraWulf has undergone a deliberate strategic transition toward HPC hosting as its primary business. While the Company operates legacy bitcoin mining facilities and leverages this flexible compute load to support early HPC infrastructure development, going forward capital allocation [prioritizes HPC]" and "While the Company currently derives the majority of its revenue from bitcoin mining, HPC hosting is now the Company's primary growth driver and operating focus." (10-K). Identity: "We are a vertically integrated owner, developer, and operator of large-scale digital infrastructure in the United States, purpose-built to support high-performance computing ('HPC') workloads, including artificial intelligence ('AI'), machine learning, and advanced cloud applications." (10-K).
- Revenue: FY2025 "Digital asset revenue $151,556 … HPC lease revenue 16,899 … Total revenue $168,455" vs FY2024 $140,051 ($K; 10-K). Q2 2026: "Digital asset revenue $12,835 [$47,636] … HPC lease revenue 31,932 [—] … Total revenue 44,767" — six months $78,779 ($K; 10-Q). Mining revenue collapsed y/y as capacity converts to HPC leasing.
- Hashrate: "approximately 49,400 bitcoin miners operational at the Lake Mariner Data Campus, representing approximately 9.3 EH/s of self-mining capacity" and "nameplate at the LMD Bitcoin Mining Facilities was 10.9 EH/s and 9.7 EH/s as of December 31, 2025 and 2024" (10-K); "10.6 EH/s and 12.8 EH/s as of June 30, 2026 and 2025" (10-Q); "we owned approximately 53,700 miners, with approximately 28,300 oper[ational]" (10-Q, 6/30/26).
- MW / HPC commitments: "energized 145 MW of capacity across three buildings" (mining, Lake Mariner); "energized 81 critical IT MW of HPC leasing capacity at the Lake Mariner Data Campus. As of the date these … statements were issued, TeraWulf had energized 102 MW of critical IT HPC capacity" (10-Q). Contracted platform: "522 MW of critical IT load" incl. 50.1% share of Abernathy; "18 critical IT MW of HPC capacity" energized at 12/31/25 (10-K). Akela: "three data center lease agreements … with Fluidstack USA I Inc. … we will provide 378 MW of critical IT load at the Lake Mariner Data Campus", which "benefit from substantial credit support provided by Google" (10-K); Core42: "committed to deliver 60 MW of critical IT load … initial ten-year term with two five-year renewal options" (10-K); Abernathy JV: "168 MW critical IT load datacenter campus in Abernathy, Texas … In July 2026, the Company entered into a definitive agreement to sell its entire 50.1% equity interest in the Abernathy Joint Venture" to the Fluidstack side (10-Q); Cayuga (Lansing, NY): "potential to support up to 400 MW of gross capacity, representing approximately 320 MW of contractual critical IT load" (10-K). Google Backstop warrants fair-value swing of "$971,992"K recognized in Q2 2026 P&L (10-Q).
- BTC held: "Number of bitcoin held 2 [6/30/26] / 3 [12/31/25]; Carrying basis $135 / $269; Fair value $133 / $270" ($K; 10-Q) — TeraWulf holds essentially no BTC treasury.
- Impairment: "Impairment of property, plant, and equipment … 25,697" ($K, six months FY2026; 10-Q).
- Energy/PPA: HPC lease "Cost of revenue (exclusive of depreciation) represents power costs which are passed through to the customer without markup" (10-K & 10-Q).
- Parks: Lake Mariner (Barker, NY — mining + WULF Compute HPC), Abernathy (TX, JV w/ Fluidstack, being sold), Cayuga (Lansing, NY ground lease).

## 4. BTDR — Bitdeer Technologies Group (Nasdaq: BTDR; foreign private issuer)

Forms: 20-F FY2025 (2025-12-31, filed 2026-04-30, acc 0001213900-26-049770) — latest annual, as expected for an FPI; no 10-Q exists. Quarterly equivalent captured instead: 6-K filed 2026-09-29 (period 2026-06-30, acc 0001213900-26-104638) containing unaudited interim consolidated financial statements for the six months ended June 30, 2026 (ex-99.1). Later 6-Ks (Oct 2/8, 2026) exist but are announcements, not quarterly financials.

Headline numbers (literal quotes):
- Revenue/profit: "We recorded total revenue of US$368.6 million, US$349.8 million and US$620.3 million for the years ended December 31, 2023, 2024 and 2025, respectively" and "net profit of US$65.6 million for the year ended December 31, 2025" (20-F). "Cost of revenue increased by 97.4% from US$283.4 million … to US$559.3 million for the year ended December 31, 2025, primarily driven by higher electricity costs associated with the expanded self-mining fleet, increased depreciation expenses from newly deployed SEALMINER mining rigs" (20-F).
- Hashrate: "As of March 31, 2026, our proprietary hash rate was 70.9 EH/s. Together with the 7.2 EH/s hosting hash rate generated from mining rigs hosted in our mining datacenters, we possessed a total of 78.1 EH/s of hash rate under management as of March 31, 2026." (20-F)
- Capacity: "increase our total capacity to approximately 3,003.5 MW, including 1,259.5 MW power supply in the pipeline, as of March 31, 2026" (20-F); datacenter table shows "Total electrical capacity 1,744" MW online plus pipeline: Massillon OH 74/26 MW (Q2/Q3 2026), Clarington OH 570 MW, Niles OH 300 MW (Q4 2028, colocation/AI cloud), Rockdale TX 179 MW, Alberta 101 MW (Q2 2027). Fire rebuild: "Approximately 26 MW in two fire-damaged buildings is expected to be rebuilt and energized by the end of the third quarter of 2026 … total reconstruction cost will be substantially recovered through insurance coverage." (20-F)
- AI/HPC pivot (verbatim): "We are building out our AI infrastructure and AI cloud bu[siness]" with "Our AI infrastructure and AI cloud business, generating revenue of US$6.8 million for the year ended December 31, 2025, remains at an early stage" (20-F); "We have initiated the conversion of several of our existing mining datacenter sites, including facilities in Tydal, Norway, Knoxville, Tennessee and Wenatchee, Washington, into AI datacenters." (20-F); colocation negotiations "for our datacenters in Tydal, Norway" (20-F).
- SEALMINER: "We began generating revenue from our sale of SEALMINER mining rigs and accessories in 2025 … This business became our second largest revenue source for the year ended December 31, 2025, representing approximately 17.5% [of total revenue]" (20-F).
- H1 2026 (6-K, $K): "Total net revenues 417,714 [H1-26] / 225,710 [H1-25] … Gross (loss) profit (47,567) / 8,011 … Loss from operations (208,293) / (93,827)"; segment split H1-26: "Self-mining 315,226 | Co-mining 34,002 | AI Cloud 17,689 | General hosting 8,226 | Membership hosting 26,529 | Cloud hash rate 7,425 | Sale of rigs 4,087 | Total 413,184"; "Electricity cost in operating mining rigs (180,191)" plus "Depreciation expense (185,431)". Balance sheet: "Cash and cash equivalents 456,838 / 149,352; Digital assets 34,762 / 85,488; Digital assets receivables from a related party 162,171 / 135,558" ($K); "Impairment charges — [H1-26] / 778 [H1-25]".
- BTC/crypto held: no BTC-treasury count in extract windows; "Substantially all of our cryptocurrencies were held in custody by BIT Group, a related party" (20-F); self-mining output is "strategically manage[d] … based on prevailing market conditions" (20-F).
- Parks: Gedu (Bhutan) 100 MW operational since Q3 2023; Jigmeling (Bhutan) 500 MW phased from April 2025; Massillon (OH) 121 MW online; Tydal-1 50 MW / Tydal-2 175 MW (Norway, crypto→colocation Q4 2026); Knoxville (TN) 37+49 MW; Wenatchee (WA) 13 MW; Molde (Norway) 84 MW; Oromia (Ethiopia) 50 MW; Cyberjaya (Malaysia) 2 MW AI cloud; pipeline Clarington 570 MW / Niles 300 MW / Rockdale 179 MW / Alberta 101 MW (20-F).

## 5. Cross-ticker pivot framing (for the brain)

- HUT: power-first platform, fully pivoted to AI data-center development economics (Anthropic/Fluidstack River Bend 245 MW IT; Beacon Point 704 MW IT, ~$19.6B contracted); mining now housed in consolidated American Bitcoin (ABTC) with its own BTC reserve (HUT consolidated BTC 17,316 at 6/30/26).
- IREN: most aggressive conversion — Bitcoin mining fleet (23.2 EH/s installed, 380 MW) being repurposed to AI Cloud/Horizon liquid-cooled campuses; Microsoft 5-yr GPU deal (~$9.7B); no BTC held (daily liquidation).
- WULF: "deliberate strategic transition toward HPC hosting as its primary business"; 522 MW contracted critical IT (Fluidstack/Google-backed Akela 378 MW, Core42 60 MW, Abernathy 168 MW); mining shrunk to ~28,300 operational miners / 10.6 EH/s nameplate.
- BTDR: diversified four-way (self-mining 315M H1-26 + rig sales + hosting/cloud hash + AI cloud 17.7M H1-26); 78.1 EH/s under management; converting legacy sites (Tydal, Knoxville, Wenatchee) to AI datacenters; ~3.0 GW total capacity incl. 1.26 GW pipeline.

## 6. HTTP log (UA: public-mining-brain/1.0 (research; contact: tyler@256foundation.org); ~0.4 s spacing, ≤10 req/s honored)

```
200  https://www.sec.gov/files/company_tickers.json                    799,583 B  (fetched twice: initial + re-run after logging bug)
200  https://data.sec.gov/submissions/CIK0001964789.json                42,279 B
200  https://data.sec.gov/submissions/CIK0001878848.json                53,561 B
200  https://data.sec.gov/submissions/CIK0001083301.json               165,092 B
200  https://data.sec.gov/submissions/CIK0001899123.json                47,641 B  (fetched twice: listing + 20-F/6-K drill-down)
200  https://www.sec.gov/Archives/edgar/data/1899123/000121390026104638/index.json   12,766 B
200  https://www.sec.gov/Archives/edgar/data/1899123/000121390026093742/index.json      789 B
200  https://www.sec.gov/Archives/edgar/data/1899123/000121390026087067/index.json      787 B
200  https://www.sec.gov/Archives/edgar/data/1899123/000121390026086938/index.json      679 B
200  https://www.sec.gov/Archives/edgar/data/1964789/000110465926019392/hut-20251231x10k.htm   5,347,664 B  (fetched twice)
200  https://www.sec.gov/Archives/edgar/data/1964789/000110465926090025/hut-20260630x10q.htm   3,719,420 B  (fetched twice)
200  https://www.sec.gov/Archives/edgar/data/1878848/000187884826000052/iren-20260630.htm      3,199,003 B  (fetched twice)
200  https://www.sec.gov/Archives/edgar/data/1878848/000187884826000026/iren-20260331.htm      1,959,900 B  (fetched twice)
200  https://www.sec.gov/Archives/edgar/data/1083301/000108330126000031/wulf-20251231.htm      2,252,446 B  (fetched twice)
200  https://www.sec.gov/Archives/edgar/data/1083301/000108330126000166/wulf-20260630.htm      1,819,379 B  (fetched twice)
200  https://www.sec.gov/Archives/edgar/data/1899123/000121390026049770/ea0282628-20f_bitdeer.htm  5,213,498 B  (fetched twice)
200  https://www.sec.gov/Archives/edgar/data/1899123/000121390026104638/ea0306473-6k_bitdeer.htm     361,957 B
200  https://www.sec.gov/Archives/edgar/data/1899123/000121390026104638/ea030647301ex99-1.htm      1,526,626 B  (fetched twice)
```
Notes: one early run aborted due to an internal logging-format bug (%d on a string header) — the underlying requests all returned 200; rerun clean. Documents were fetched in pass 1 and re-fetched once in pass 2 (stripped text then cached locally); no 403/429s.

## 7. Failures / caveats

- No failures. One supplemental regex missed on first try (IREN FY2026 revenue sentence) — fixed manually and appended.
- BTDR files no 10-Q (FPI); 6-K interim FS used as the quarterly capture (file named -6K-). Later 6-Ks (2026-10-02, 2026-10-08) are non-financial announcements and were not captured.
- "Mining margin" as a labeled metric does not appear in any of the four filers' extracts; margin evidence is via gross profit / cost-of-revenue lines quoted above.
- Sibling-agent files (MARA, CLSK, CORZ, RIOT) present in the same directory were not touched.
