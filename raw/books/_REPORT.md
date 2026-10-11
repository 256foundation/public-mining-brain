# raw/books/ — Braiins Books extraction report

> Task: capture-loop A5 · book rule = extract posture (Tyler, 2026-10-10)
> Registry ID: braiins-books
> Collected: 2026-10-10
> Ownership: this directory (`raw/books/`) only.

## Sources

| Book | Landing page | Free PDF | Words (pdftotext) | Published |
|---|---|---|---|---|
| Braiins Insights: Bitcoin Mining Handbook | https://braiins.com/books/bitcoin-mining-handbook | https://cdn.prod.website-files.com/5e5fcd39a7ed2643c8f70a6a/63ebadbe407c5bc4621f0d2a_Handbook%20I_web%20verze_3.pdf | 21,959 (/tmp/bmh.txt) | 2022 (ISBN 978-80-907975-9-8, © 2022 Braiins) |
| Braiins Insights: Bitcoin Mining Economics | https://braiins.com/books/bitcoin-mining-economics | https://cdn.prod.website-files.com/5e5fcd39a7ed2643c8f70a6a/64bf960e8f1e7d89f67dbdb3_Mining%20eco_PDF%20sazba.pdf | 33,804 (/tmp/bme.txt) | **2023** (ISBN 978-80-908709-7-0, © 2023 Braiins; foreword signed June 15, 2023). NOTE: task brief said 2024; the artifact self-identifies as 2023 everywhere, so extract headers carry 2023. Adjust registry row if the site lists 2024. |

## Extracted — Bitcoin Mining Handbook (8 files, `braiins-mining-handbook/`)

| File | Chapter (book page) |
|---|---|
| 01-how-bitcoin-mining-works.md | Bitcoin Mining is NOT Solving Complex Math Problems (p. 12) |
| 02-merits-of-proof-of-work.md | On the Merits of Proof of Work (p. 18) |
| 03-nodes-vs-miners.md | Bitcoin Nodes vs. Miners: Demystified (p. 25) |
| 04-cost-to-51-percent-attack.md | How Much Would it Cost to 51% Attack Bitcoin? (p. 32) |
| 05-autotuning-vs-overclocking.md | Autotuning vs. Overclocking for Bitcoin Miners (SHA-256 ASICs) (p. 42) |
| 06-mining-pools-shares-luck.md | Bitcoin Mining Pools: Luck, Shares, and Estimated Hashrate Explained (p. 47) |
| 07-stratum-v2.md | Hashrate Robbery: Stratum V2 Fixes This (and More) (p. 56) + Bitcoin's Decentralization with Stratum V2 (p. 63) — merged, same theme |
| 08-mining-profitability-calculation.md | How to Calculate Bitcoin Mining Profitability (p. 75) |

Skipped (Handbook):
- Foreword (Marty Bent), Preface — front matter.
- Mining business section intro (p. 70) — 1-page framing.
- Bitcoin Mining Profiles: The Investor, The Entrepreneur, and The Prospector (p. 71) — persona essay, low technical grounding.
- Green Innovation in Bitcoin Mining: Recycling ASIC Heat (p. 84) — heat-reuse case studies (MintGreen, Genesis greenhouses, GreenMine, Sato, SPA-256); marketing-adjacent project showcase. One citable stat lost to the skip: energy is "79% of operational expenses on average" for miners (p. 85).
- Economics of Immersion Cooling for Bitcoin Miners (p. 91) — **superseded**: the print edition truncates the analysis ("find it on the Braiins blog"); the full version is in the Economics book and was extracted there.
- Mining memes (p. 98) — memes section.

## Extracted — Bitcoin Mining Economics (7 files, `braiins-mining-economics/`)

| File | Chapter (book page) |
|---|---|
| 01-hashvalue-hashprice-rigprice.md | Hashvalue, Hashprice, and Rigprice (p. 14) |
| 02-rigprice-cost-to-mine-1-btc.md | Rigprice and Marginal vs. Total Cost to Mine 1 Bitcoin (p. 23) |
| 03-debt-capital-markets.md | The History of Debt in Bitcoin Mining: Part 1 (p. 32) + Part 2 (p. 46) — merged, one financing theme |
| 04-when-miners-sell-btc.md | Understanding When and Why Bitcoin Miners Sell Their BTC (p. 62) |
| 05-solar-intermittent-energy.md | Energy Sources Deep Dive intro (p. 68) + Economics of Bitcoin Mining with Solar Energy (p. 70) + Optimizations for Bitcoin Mining with Intermittent Energy Sources (p. 89) — merged: LCOE + demand response |
| 06-stranded-flared-gas-mining.md | From Flare to Fortune: Mining Bitcoin Off-Grid with Stranded Gas (p. 99) |
| 07-immersion-hydro-cooling.md | Economics of Immersion Cooling for Bitcoin Miners (p. 110) + The Emergence of Hydro (Water) Cooling (p. 132) — merged, liquid cooling |
| 07-transaction-fee-luck.md | Transaction Fees and Halving Cycles (p. 135) + Transaction Fee "Luck" for Bitcoin Miners (p. 137) — merged (numbering note: two files share the 07 prefix; both extract from pp. 110–146 range) |

NOTE: prefix collision — `07-immersion-hydro-cooling.md` and `07-transaction-fee-luck.md` both carry "07". Registry row should treat them as files 07 and 08 respectively (or rename the latter to 08).

Skipped (Economics): Acknowledgements, Foreword (Jason Les), Preface; Fundamentals section intro (p. 13, folded into ch. 14 extract context); Hashrate and Humor: Mining For Memes (p. 147); Closing Thoughts (p. 157); "More from Braiins Insights" back matter (pp. 159–160).

## Method / invariant notes

- Full plain-text reads of both pdftotext extractions; page numbers cited are the book's printed pages (stable across print/PDF).
- Extract posture: key claims only, with the book's exact literals (numbers, units, quotes) preserved for future wiki citation. No full-text dumps; source PDFs are freely distributed by Braiins.
- Where two chapters form one theme they were merged into one file with both chapter attributions inside (Stratum V2; Debt Parts 1+2; Solar + Optimizations; Immersion + Hydro; Fees + Fee luck).
- Figures are time-stamped to the book's writing (e.g. "150 EH/s network hashrate" = Jan 2021 Handbook; ">300 EH/s" = Feb 2023 Economics); wiki articles must carry that vintage context when citing.
