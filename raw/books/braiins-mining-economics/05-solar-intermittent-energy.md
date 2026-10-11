# Bitcoin Mining Economics — ch. 70–98: Solar & Intermittent Energy Economics (2 chapters, extract)

> Source: https://braiins.com/books/bitcoin-mining-economics (PDF: https://cdn.prod.website-files.com/5e5fcd39a7ed2643c8f70a6a/64bf960e8f1e7d89f67dbdb3_Mining%20eco_PDF%20sazba.pdf) (Braiins Publishing, free PDF)
> Collected: 2026-10-10
> Published: 2023
> Registry ID: braiins-books
> Posture: extract (key information with chapter attribution; full text at source PDF)

## Key points (ch. 68–69 — Energy Sources Deep Dive, section intro)

- Miners "want power that is in surplus supply relative to demand, as this will always be the cheapest power" — "excess solar on a sunny day, excess wind on a windy day, excess hydro during the wet season, stranded gas that's uneconomic to take to market, or even excess grid power during times of low demand"; when demand is high, "bitcoin miners will reduce consumption or turn off completely, as the power is worth more to somebody else than it is to the miner." (p. 68)
- Demand-response speed: similar industrial consumers "typically require many minutes, if not hours, to fully ramp up or down their consumption, while bitcoin miners can do this in a matter of seconds." (pp. 68–69)

## Key points (ch. 70–88 — Economics of Bitcoin Mining with Solar Energy)

- Waste-gas scale (US EIA): "the amount of natural gas being flared and vented in the US is around 1.48 billion cubic feet per day (Bcf/d), equivalent to about 1.52 trillion BTUs/day... could be used to generate roughly 162 TWh/year of electricity" — vs "the entire Bitcoin network, which consumes an estimated 116 TWh per year" (Cambridge CBECI, May 29, 2021). (pp. 72–73)
- Methane potency: "estimated by the Environmental Protection Agency to be 25 times worse for the environment than CO2 over a 100-year time span and 80 times worse over a 25-year time span." (pp. 72–73)
- LCOE definition (verbatim, from the BCEI whitepaper discussion): "Levelized Cost of Energy (LCOE): the total lifetime cost of building and operating a power generation asset divided by the total amount of energy it produces." (p. 73)
- Solar economics input: the Bitcoin Clean Energy Initiative (Square + ARK Invest, April 2021 whitepaper) solar LCOE range averaged to "$0.035/kWh" for the mining analysis. (pp. 73–74)
- Solar model constraint: "the miners run entirely on solar power, not using grid power during unproductive solar hours"; grid-first logic — "the sun's energy will not be used to mine bitcoin unless the demand from the grid is first met." (pp. 74–75)
- Uptime reality: from ARK's open-source model, average deployed hashrate "1.923 EH/s" vs "5.449 EH/s" maximum = "35% uptime for the deployed ASICs... mines for about 8 hours per day on average"; typical load-balancing miners "will have 80%+ uptime". (pp. 75–76)
- Difficulty history: "Since 2017, network difficulty... increased from 317 billion to 25 trillion, equaling a 164% annual increase over the past 56 months"; analysis conservatively used "100%" annual difficulty increment with "$40,000 per BTC" price and "$30,000 for monthly OpEx... for all the costs involved in staffing a 170 MW facility". (p. 77)
- Baseline result: "nearly $100 million in negative cumulative cash flow by Month 34, when mining becomes unprofitable on a marginal basis (assuming hardware fully depreciates in 48 months)". (p. 78)
- Bull case (+70%/yr price): "mining remains profitable... for the entire 48-month period... the initial CapEx investment is actually paid off near the end of the 3rd year of operations." (p. 79)
- HODL effect: with "a HODL Ratio of 50%, the CapEx break-even point is shortened to less than 2 years, and the final cash flow of the operation... reaches nearly $600 million." (p. 80)
- BTC-denominated verdict: "a total of 4,641 bitcoins are mined" over 4 years, but "at $40,000 per BTC, the $247,680,000 could be used to purchase 6192 bitcoins with no OpEx... the miners never break even on the CapEx in BTC terms"; BTC-denominated cash flow ends "nearly negative 4,000 BTC". (pp. 80–81)
- Free-power test: "even with free electricity, the operation never breaks even on the initial fiat CapEx investment unless BTC price goes up substantially." (p. 82)
- Full-uptime comparison (same CapEx, $0.05/kWh, 5.45 EH/s / 178 MW): "the operation breaks even during Year 2 and remains profitable for about 2.5 years... final cash flow of $205 million—not bad for a $247 million initial investment." (pp. 83–84)
- Best case (70%/yr price + 50% HODL): "USD CapEx break-even occurs in just 9 months, and the final cash flow of the project exceeds $1.7 billion. The total BTC mined over 4 years is close to 13,000, more than double the amount that could have been bought with the initial CapEx investment amount." (p. 84)
- Uptime rule (verbatim): "Mining farms with 90%+ uptime are likely to break even within the first 2 years of operations with electricity prices at the high end of the spectrum, while extremely cheap electricity prices are not enough to make most operations viable with less than 60% uptime." (p. 86)
- Hardware note: model ASIC mix averaged "32.6 J/TH" ("most similar to an Antminer S19 or Whatsminer M30S+"); at June 2021 market prices of "$80-100/TH", hardware CapEx would be "$400MM-$550MM, as opposed to $248MM (the figure used)". (p. 88)
- Cheap-hardware aside: "purchasing 50,000 Antminer S9s around the halving in May 2020 when they were selling for $20-$40 each" as a lower-CapEx strategy. (p. 86)

## Key points (ch. 89–98 — Optimizations for Bitcoin Mining with Intermittent Energy Sources)

- Efficiency history: "The first ASIC—the Avalon1 released by Canaan in 2013—had a hashrate of 60 GH/s and a consumption of 595 W. In today's efficiency terms, that's just under 10,000 J/TH"; "the release of the Antminer S9 in 2016 took us below 100 J/TH"; "The best ASICs of 2021 hash at around 30 J/TH and are only ~10-20 J/TH more efficient than their mid-gen predecessors." (p. 90)
- ERCOT demand response: Texas miners "acting as Controllable Load Resources in the ERCOT (Electric Reliability Council of Texas) system... agree to consume less power when there is high demand from the grid, and in exchange they pay much lower prices (e.g. 1-3 ¢/kWh) for their electricity the rest of the time." (p. 89)
- Difficulty treadmill: "the bitcoin network difficulty has been steadily climbing to the tune of ~8% monthly increases during the modern ASIC era"; with an ASIC cost of 0.2 BTC, the 100%-uptime unit "exceeds the cost of the ASIC (in BTC terms) during Month 12", the 70%-uptime unit never does. (p. 91)
- Supplemental power math (S19j Pro, 8h free solar + 16h grid at 8 ¢/kWh, BTC $30k, difficulty ~50T): "$2.61 (⅓ * $7.84) of profit each day during the 8 hours with free electricity, and $1.30 (⅔ * $1.93) of profit the other 16 hours, for a total of $3.90... you increase your daily profit by nearly 50% by running the miners on the more expensive electricity rather than just shutting them off for those 16 hours." (p. 93)
- Firmware upside: with Braiins OS+ "boosts profitability from $7.84 to $8.23 per 24 hours after factoring in the 2.5% firmware devfee"; in the high-efficiency profile (2200 W) the S19j Pro produces "approximately 88 TH/s at 25 J/TH for a profit of $2.25 per 24 hours of operation with $0.08/kWh electricity"; daily total "$4.24 per day—a 12% profitability increase compared to stock firmware and a 62% profitability increase compared to stock firmware without a secondary energy source, not to mention an extra 800 satoshis mined per machine each day." (pp. 94–95)
- Rate structure: bills often have "a base charge and a demand charge based on your peak power consumption in a short time interval for the entire month or billing period" — lower per-miner consumption lowers the demand charge and the effective $/kWh. (p. 96)
- Thermal cycling: ASIC chips operate "at quite high temperatures during mining (optimally 70-85oC or 158-185oF)"; "The process of heating up and cooling down the material is called thermal cycling, and it can result in an accelerated degradation of the silicon chip's quality. There is no public data (yet) to help quantify the effect." (p. 97)
- Heat–efficiency research: "research by Braiins published in 2022 demonstrated that, when all other factors (voltages and frequencies) are equal, hardware efficiency for the Antminer S19 generation significantly decreases at higher temperatures" (constant 13.5V; 450/550/650 MHz compared). (pp. 97–98)
