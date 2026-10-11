# Hashprice and Difficulty

> Sources: Luxor Hashprice Index methodology (docs.luxor.tech, captured via llms-full.txt after Cloudflare 403 on the direct route); Hashrate Index homepage SSR + September 2026 Lookback + Q4 2026 Global Hashrate Heatmap; WhatToMine BTC/SHA-256 + /asics SSR snapshots; Cambridge CBECI landing page (rendered) + methodology (verbatim) + data-access notes; Cambridge Digital Mining Industry Report, First Edition April 2025 (150 pp. PDF extract); Galaxy Research breakeven-hashprice (2022-02-11) + Bitcoin Miners Powering the AI Revolution (2024-12-18); CoinShares Bitcoin 13F Q2 2026 + Equities Week 41; Braiins blog (dashboard is a JS shell); TheMinerMag → TheEnergyMag migration + mining index
> Raw: [Hashprice methodology (verbatim)](../../raw/economics/hashprice-docs/2026-10-10-hashprice-methodology.md); [Hashrate Index homepage snapshot](../../raw/economics/hashrate-index/2026-10-10-homepage-snapshot.md); [Lookback Sep 2026](../../raw/economics/hashrate-index/2026-10-10-lookback-september-2026.md); [Heatmap Q4 2026](../../raw/economics/hashrate-index/2026-10-10-heatmap-q4-2026.md); [WhatToMine BTC snapshot](../../raw/economics/whattomine/2026-10-10_whattomine-btc-sha256-ssr-extract.md); [WhatToMine /asics ranking](../../raw/economics/whattomine/2026-10-10_whattomine-asic-ranking-ssr-extract.md); [CBECI landing](../../raw/economics/cbeci/cbeci-landing.md); [CBECI methodology](../../raw/economics/cbeci/cbeci-methodology.md); [CBECI data-access pointers](../../raw/economics/cbeci/cbeci-data-access.md); [DMIR 2025 extract](../../raw/economics/cambridge-report/dmir-2025-extract.md); [Galaxy breakeven hashprice](../../raw/economics/galaxy-research/2022-02-11_galaxy-breakeven-hashprice-extract.md); [Galaxy miners-AI](../../raw/economics/galaxy-research/2024-12-18_galaxy-bitcoin-miners-ai-revolution-extract.md); [CoinShares research index](../../raw/economics/coinshares-research/2026-10-10_coinshares-research-index-mining-listing.md); [CoinShares 13F + Week 41](../../raw/economics/coinshares-research/2026-10-10_coinshares-mining-relevant-extracts-13f-week41.md); [Braiins shell note + blog index](../../raw/economics/braiins-insights/2026-10-10_braiins-insights-shell-note-and-ssr-blog-index.md); [Braiins GDA 40MW case study](../../raw/economics/braiins-insights/2026-03-03_braiins-gda-40mw-firmware-case-study-extract.md); [Braiins TÜV SÜD testing](../../raw/economics/braiins-insights/2025-04-01_braiins-tuv-sud-efficiency-extract.md); [TheEnergyMag migration + MARA](../../raw/economics/minermag/2026-10-10_theenergymag-migration-mining-index-mara.md); [TheEnergyMag great-unplug extract](../../raw/economics/minermag/2026-10-01_theenergymag-bitcoin-great-unplug-extract.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10 — every market number on this page is a dated snapshot, not a constant
> Status: Draft

## Overview

The two variables every mining decision hangs on: **hashprice** (revenue per unit of hashrate) and **difficulty** (the work the network demands for it). Hashprice is "a term coined by Luxor in 2019", defined as quantifying "how much a bitcoin miner can expect to earn from a specific quantity of hashrate"; the industry's canonical index is denominated per petahash-day, while Galaxy's working definition is "the market value of one unit of hashpower measured in dollars per terahash" — same quantity, three orders of magnitude apart in units. This page pins the definitions, the construction of the indexes, the October 2026 market snapshot, the difficulty/fee mechanics behind them, and the cost curve that decides who survives a down-market. Heat-first corollaries (heaters run when hashprice doesn't cover power) live in [Hashrate Heating Economics](hashrate-heating-economics.md) and [Open Mining Economics](open-mining-economics.md).

## Hashprice: two denominations, three-to-four inputs

- BTC hashprice: "a function of three inputs: block subsidy, transaction fees, and network difficulty."
- USD hashprice adds the fourth: "USD hashprice is a function of four inputs: block subsidy, transaction fees, network difficulty, and bitcoin price."
- Construction (verbatim, methodology): "Luxor's Bitcoin Hashprice Index uses a 144-block lagging simple moving average to account for transaction fees, and a simple average of the spot price for bitcoin on three US-based cryptocurrency exchanges to account for USD conversion."
- Unit (verbatim): "Luxor's Bitcoin Hashprice Index quantifies the expected value of 1 PetaHash per second (PH/s) of hashrate per day on the Bitcoin Network." Live tracking: data.hashrateindex.com; API `GET /hashprice/current`.
- Cadence: "Bitcoin's hashprice changes with every new block added to the blockchain (i.e., block height)." Difficulty, by contrast, moves on the retarget: "Network difficulty is adjusted every 2,016 blocks (approximately every two weeks) to a level that targets an average block time of ten minutes."
- Correlation rule (verbatim): "USD-denominated hashprice is positively correlated with changes to Bitcoin's spot price, block subsidy and transaction fees and negatively correlated with changes to Bitcoin's network difficulty."
- Galaxy's 2022 framing and the name analogy: "You can think of hashprice as being analogous to the value of WTI crude oil for the oil and gas industry." Galaxy separates revenue (hashprice) from survival: "breakeven hashprice, which measures the threshold below which miners begin operating unprofitably. This figure factors in operational costs like power and hosting costs, payroll (excluding any employee stock-based compensation), and selling, general and administrative (SG&A) expenses, as well as interest expense as a non-operating expense." (Galaxy open-sourced the spreadsheet calculator.)
- The Braiins *Bitcoin Mining Economics* (2023) book baseline — hashvalue/hashprice/rigprice definitions and the cost-to-mine framework — is in [Open Mining Economics](open-mining-economics.md); Luxor's index is the live-market realization of the same construct.
- Payer status: "The BTC hashprice formula is used by a majority of mining pools to pay miners for their hashrate" — i.e. FPPS/PPLNS payouts are hashprice derivatives (see [Pool Payout Schemes](../pools/pool-payout-schemes.md)).

## Market snapshot (As-Of 2026-10-10, three independent SSR sources)

| Metric | Hashrate Index homepage | WhatToMine | Notes |
|---|---|---|---|
| Hashprice | "$39.44 / PH/DAY" | — | the $/PH figure ÷ 1000 |
| BTC price | "$82,982" | "Ex. rate: $82,977.33 (WhiteBIT)" | single-venue (WTM: WhiteBIT) vs 3-exchange SMA |
| Difficulty | "Projected Difficulty 132.72 T" | "Difficulty: 132,716,002M" | current epoch 132.76T per Lookback |
| Network hashrate | "1002.42 EH/s" | "1,003,540.30 Ph/s" | same value, different smoothing |
| Block time | "9m 38s" | "9m 28s" | different windows |
| Block reward | — | "Bl. reward: 3.17" (incl. fees) | subsidy 3.125 + ~0.02–0.04 fees |
| Daily emission | — | "Daily emission: 477.809 BTC" | ≈ 144 × 3.125 + fees |

- The three sources agree within snapshot-timing variance; no dispute. WTM's multi-coin `/coins` table is JS-only (gap noted in capture); its BTC coin page and `/asics` ranking are SSR.
- Best-machine margin check from the WTM `/asics` SSR rows (at "$0.19/kWh"): "Bitmain Antminer U3S23H | Jan 2026 | 1.16 Ph/s @ 11020W | SHA-256 | $0.19/kWh | 9.50 W/Th | $49.03 | $22.58" (24h revenue/profit) — ~46% margin for the best air hardware; implied SHA-256 revenue ≈ $0.042/TH/day. Compare Luxor's energy tiers below.

## Difficulty and the 2026 network state

- September 2026 (Lookback, published 2026-10-09): "Difficulty averaged 129.24T (+2.0%), and finished the month at 132.76T. Two adjustments occurred and both were upward: +1.31% on September 5 and +4.16% on September 19, the largest single retarget since June 27."
- Hashrate trend: "the 7-day network hashrate average rose from 926 to 975 EH/s across the month"; "the 7-day hashrate average currently stands at 999 EH/s" (2026-10-08) — the 1 ZH/s threshold is live.
- Peak context (Heatmap Q4 2026, published 5 Oct 2026): "Network hashrate held at ~941 EH/s, +0.1% QoQ after -6.3% and -5.8% in the prior two quarters. It remains -8.7% year-over-year and ~15% below the ~1,110 EH/s peak set in November 2025." (Note: Heatmap counts ~941 EH/s while homepage shows 1002.42 — different metrics: country-attributed vs total.)
- Geography: "United States — 35.6% (~335 EH/s)", "Russia — 18.1% (~170 EH/s)", "China — 11.7% (~110 EH/s)" — "the top three countries commanding roughly two-thirds of global hashrate" ("65.4%, down from 66.2%").
- Fees: "Average fee collection fell 10.1% to 0.0199 BTC per block, the lowest since May. Fees were 0.63% of total block rewards, a fifteenth consecutive month below 1%." Fee revenue is noise for planning; the 144-block SMA in the index exists precisely to smooth it.
- Subsidy (methodology as written): "The block subsidy is currently 3.125 BTC" and "the next "halving" is projected for April 2028" — the docs' own double-quoted term.
- Forward curve: "Luxor's Hashrate Forward Market is pricing an average hashprice of $36.65 or 0.00044 BTC per PH/s/day over the October 2026 – March 2027 window"; September sellers locked "$30.10 and $34.72 per PH/s/day against a $39.33 spot settlement"; implied network hashrate "crosses 1 ZH/s in January 2027 at 1,029 EH".

> **Status: Disputed** — US hashrate share, two methodologies
> Cambridge DMIR 2025 survey (49 firms, 268 EH/s = "48% of the implied Bitcoin network' hashrate (as of 30 June 2024)"): "US 75.4%" of surveyed capacity (p.46–47). Luxor Heatmap (network-wide attribution, ~941 EH/s, Oct 2026): "United States — 35.6% (~335 EH/s)". Not a measurement error — firm-HQ/fleet survey coverage vs country-level hashrate attribution differ, and the dates are 15 months apart; both verbatim. Use DMIR for corporate concentration, Luxor for physical geography.

## Energy price tiers — the margin ladder (September 2026)

Luxor's Lookback publishes the electricity price each efficiency class can sustain at prevailing hashprice: "~$137/MWh for under 14 J/TH", "~$99/MWh for 14–19 J/TH", "~$74/MWh for 19–25 J/TH", "~$51/MWh for 25–38 J/TH" — against an "average industrial bitcoin mining power cost of $48/MWh".

- Read: at $39/PH/day, only machines ≤ ~25 J/TH on sub-$50/MWh power clear industrial margins — the bar home heaters beat by monetizing heat on top.
- Historical decay (DMIR, survey data): hashcost fell "$128 → $16 (−87.5%)" across epochs; BTC price "+1209%" (2020–24) against difficulty "+734%" and hashprice "−60%".
- DMIR cost curve (June 2024 survey): direct cost to mint "1 BTC" "$17,417 to $56,606, with a median of $39,189"; all-in "median of $48,333"; electricity rates median "$45/MWh" direct / "$55.5/MWh" all-in — "81.1% / 18.9%" of cash opex is electricity vs everything else.
- Hash-margin break-even matrix (DMIR p.92): "at an electricity rate of $80/MWh, miners with an efficiency of 25 J/TH are slightly above break-even, while those with 30 J/TH are already experiencing a loss"; conversely "at a lower electricity cost of $40/MWh, miners with an efficiency as low as 45 J/TH still remain profitable".

## Consumption and efficiency context (CBECI + DMIR)

- CBECI (rendered 2026-10-10): best-guess boxes 18.48 (GW) / "162.04" (TWh annualised), bounds 9.48–35.56 (GW) and 83.08–311.70 (TWh); hardware efficiency estimate "17.01 J/TH" (bounds 9.50–30.00). Model v1.4.0: release-date weighting "ranging from 1 to 0, decreasing in five steps of 0.2", five-year economic lifetime, "a delay of two months from the hardware's release date to when it is considered in our model"; 0.05 USD/kWh default; PUE 1.01/1.10/1.20; hardware basket = Bitmain/MicroBT/Canaan ("estimated combined market share of at least 85%"). Live numbers are reCAPTCHA-gated client-side; dataset pointers in the capture (full CSV not committed — no-massive-data rule).

> **Status: Disputed** — annualized consumption, CBECI vs Digiconomist (both live, Oct 2026)
> CBECI best-guess "162.04 TWh" vs Digiconomist "204.44" TWh (CBECI's own live-stats endpoint returns `{"digiconomist":"204.44"}` and methodology Table 2 carries the same anchor). The spread is methodological: CBECI models a profitability-weighted hardware fleet with PUE bounds; Digiconomist runs a continuous extrapolation. Treat 160–205 TWh as the live-methods band, not a fact discrepancy to resolve.

- DMIR 2025 (First Edition, April 2025; survey June–Sept 2024; 150 pp.): consumption "estimated at 138.2 TWh as of 30 June 2024" — "approximately 0.54% of the world's total annual electricity consumption" — with survey/CBECI cross-check "137.4 TWh"; weighted efficiency "28.2 J/TH" (−24% YoY); US 75.4% of survey hashrate (see Disputed above); energy mix "52.4% sustainable" (gas 38.2% single largest source); Bitmain 82.0% / MicroBT 15.0% / Canaan 2.1% hardware share; firmware mix: stock 44.4% / Vnish 26.4% / custom 17.6% / Braiins OS 5.6% / LuxOS 3.3% (feeds [Mining Firmware Security](../industry/mining-firmware-security.md)); 2024 divergence: hashrate "+455%" vs consumption "+111%" (2021–24).
- AI/HPC pivot (DMIR p.112–113): mining revenue "$80 to $151" per MWh vs CaaS "$1,600 to $4,000 per MWh"; CAPEX "$9 to $40 million per MW" (data center) vs "$1.2 million per MW" (mining). This is the economics driving the public-miner pivot below.

## Public miners: the 2026 repricing (TheEnergyMag, ex-TheMinerMag)

- Rebrand: theminermag.com now 301/redirects to **theenergymag.com** (same BlocksBridge/Wolfie Zhao team; "Digital Mining" section live with SSR) — the A8 "parked: JS shell" candidate cleared itself.
- Hashrate shed: "public miners lost 75 EH/s of realized hashrate while their directly reported HPC and AI revenue rose 52% quarter over quarter." At the $20/TH acquisition anchor that is "roughly $1.5 billion in equivalent hardware investment".
- Impairments: "approximately $1.1 billion in asset impairments and held-for-sale markdowns during the first half of 2026. IREN and Core Scientific (NASDAQ: CORZ) accounted for almost 89% of the total."
- Capex cycle: "Public miners and AI infrastructure peers recorded $30.7 billion of 2026 net capital spending, already 43% above their full-year 2025 total."
- Ownership datapoint (CoinShares 13F Q2 2026): "13F filers reported 264k BTC equivalent at the end of June, up from 261k in Q1 (+1.3%)"; hedge funds −22% QoQ; 13F share of US ETF AUM "rose from 20.8% to 22.4%".
- Financing pressure (CoinShares Week 41, 2026-10-09): "miners pursuing capital-intensive AI expansion remained more exposed to financing pressures and changing expectations for infrastructure returns" — with the 10Y UST "briefly reached approximately 5.36%, a 24-year high".
- Operational anchor (TheEnergyMag mining index): Bitdeer "produced 1,310 Bitcoins during the month, supported by a self-mining hash rate of 79.9 EH/s and a co-mining hash rate of 21.6 EH/s" (Aug 2026); MARA "Pledges 18,750 BTC for $600 Million New Bitcoin-Backed Loans".
- Public-miner filings economics (10-K/10-Q extract posture) is the A10 phase; this section is the press-level view.

## Firmware-as-margin (vendor-claimed)

- Braiins/GDA 40 MW case study (2026-03-03): "achieving up to 40% higher hashrate on identical hardware"; measured "the hashrate delta remained approximately 32%"; "The efficiency delta was approximately 1 J/TH". Marketing claim ("up to 40%") vs measured delta (~32%) — both verbatim, the gap is the claim's shape.
- Braiins/TÜV SÜD (2025-04-01): "greater efficiency performance in all four tests" (per-test figures context-truncated in SSR — captured as-is).
- Dashboard note: insights.braiins.com is a 1,613-byte React shell (build 8da3b47fd6f46d10, 2026-06-01); the SSR blog lives at braiins.com/blog. Hashprice widget renders label `USD/TH/Day` + "+1.53%" but the value is JS-populated — no number captured, none invented.

## Heat-reuse relevance

- The energy-tier ladder is the correct frame for heat-first deployments: home-run hardware in the "19–25 J/TH" class breaks even near "~$74/MWh" — far above the industrial "$48/MWh" average — so on residential power mining alone loses; heat monetization is the arbitrage (see [Hashrate Heating Economics](hashrate-heating-economics.md)).
- Hashprice downside is bounded work for small heaters: at "0.00048965 BTC per PH/s/day" (September's BTC-denominated average), a Bitaxe-class single-TH unit earns on the order of tens of sats per day before power — the pool-threshold math in [Pool Choice for Heat Miners](../pools/pool-choice-for-heat-miners.md) applies directly.
- Difficulty planning baseline for heater uptime (50%/yr difficulty growth assumption, sats-payback caveats) is maintained in [Hashrate Heating Economics](hashrate-heating-economics.md); this page holds the live-market side.

## See Also

- [Open Mining Economics](open-mining-economics.md) — book baselines (hashvalue/hashprice/rigprice), used-equipment price points, POD256 field data
- [Hashrate Heating Economics](hashrate-heating-economics.md) — the heat-first corollary of everything above
- [Pool Payout Schemes](../pools/pool-payout-schemes.md) — how pools actually pay the hashprice formula
- [Network State 2022–2026](../industry/network-state-2022-2026.md) — dated hashrate/difficulty/price snapshots (A10 extends)
- [Public Miner Economics](../industry/public-miner-economics.md) — filings-level view (A10)
- [Data Resources](../meta/data-resources.md) — the live-endpoint layer (hashrate index, CBECI) vs the frozen captures cited here
