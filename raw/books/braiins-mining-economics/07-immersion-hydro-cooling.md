# Bitcoin Mining Economics — ch. 110–134: Immersion & Hydro Cooling Economics (2 chapters, extract)

> Source: https://braiins.com/books/bitcoin-mining-economics (PDF: https://cdn.prod.website-files.com/5e5fcd39a7ed2643c8f70a6a/64bf960e8f1e7d89f67dbdb3_Mining%20eco_PDF%20sazba.pdf) (Braiins Publishing, free PDF)
> Collected: 2026-10-10
> Published: 2023
> Registry ID: braiins-books
> Posture: extract (key information with chapter attribution; full text at source PDF)

## Key points (ch. 110–131 — Economics of Immersion Cooling for Bitcoin Miners)

- Post-China-ban context: summer 2021 miners saw revenue "temporarily double in bitcoin terms, from under 500 satoshis/TH/day to nearly 1000 sats/TH/day"; by late May 2022 the 30-day moving average hashrate sat "above 200 EH/s" with "North America [picking] up China's slack", Texas "the clear global frontrunner in terms of hashrate/m2". (pp. 110–111)
- China hashrate share (mid-2022): manufacturer employees suggested "as much as 30-40% of network hashrate remained in China", the author "believes it's more likely below 20%". (p. 111)
- Heat sensitivity: "the power consumption of Antminer S19 models can increase by 40%+ with higher temperatures even as frequencies are constant (and thus hashrate is constant as well), meaning that the J/TH efficiency of the machines suffers significantly." (p. 112)
- Fan overhead: "on a new-generation miner like an Antminer S19, the 4 fans consume roughly 35 W each, accounting for ~5% of the machine's total electricity consumption in air. Removing them... means that the 5% energy savings can go towards more hashing, improving the J/TH by roughly that amount." (p. 114)
- Air-cooled infrastructure: "$150-400k/MW"; cooling components (wet curtains, intake/exhaust fans, hot/cold aisle insulation) "will rarely account for more than 10% of total infrastructure CapEx, while the more common case is probably at or below 5%". (p. 115)
- Immersion adds: "Dry coolers / cooling towers; Tanks and frames; Pumps and pipes; Heat exchangers; Dielectric coolant; Sensors and monitoring / control systems." (p. 115)
- Immersion CapEx premium: extra CapEx "almost identical to the original air cooling CapEx range, $150k-350k per MW"; total "somewhere in the wide range of $280k-730k/MW... More realistically... somewhere in the $280-600k range." (p. 116)
- Scenario inputs: "$40,000/BTC and 29794407589312 difficulty (as of early May 2022)"; "10 MW of available power capacity for 4 years"; 5% safety margin leaving "9.5 MW for mining"; "104 TH/s Antminer S19j Pro's with a total machine cost of $8500/unit (rig price $81.7/TH) and stock power consumption per unit of 3068 W". (pp. 116–117)
- Infrastructure assumptions: "Air cooled = $250k/MW, or $2.5MM total for 10 MW; Immersion = $450k/MW (air cooling + $200k/MW), or $4.5MM total for 10 MW"; hardware depreciation "20%/ year for both"; "All-in electricity rates will be a fixed $0.05/ kWh with 24/7 uptime"; "HODL Ratio will be 100% of profits in all cases". (p. 117)
- Scenario endpoints: moderately bullish May 2026 "$400k/BTC and 182.3T difficulty" (difficulty +70%/year, price +80%/year, "20% halving difficulty drop"); moderately bearish May 2026 "$95k/BTC and 98.7T difficulty" (difficulty +50%/year, price +25%/year, "0.1 BTC transaction fees per block", "30% halving difficulty drop"). (pp. 117–118)
- CapEx proportions: "325 S19j Pro's per MW. At a unit cost of $8500, the hardware CapEx is $2.76MM/ MW— approximately 10x the air cooling infra cost and 5.5x the immersion cooling infra cost." (p. 118)
- Case 1 (air, stock firmware): "3,096 S19j Pro's for a total hardware CapEx of $26.32MM... total CapEx for the 10 MW air-cooled operation to $28.82MM (720.5 BTC). Our total hashrate is 322 PH/s and our pool fee is 1%." (p. 119)
- Case performance (bear: BTC mined / final holdings / cumulative profit / USD breakeven / avg cost per BTC, p. 125): Air stock ₿910.4 / ₿399.6 / $12.6mm / 43 mo / $20,038; Air BOS+ ₿962.7 / ₿437.4 / $13.9mm / 41 / $19,240; Immersion stock ₿955.9 / ₿445.2 / $14.2mm / 42 / $19,083; Immersion BOS+ @3086W ₿1,002.3 / ₿491.5 / $15.8mm / 40 / $18,201; @4000W ₿906.0 / ₿395.0 / $12.5mm / 39 / $20,143; @5500W ₿769.3 / ₿258.6 / $7.9mm / 45 / $23,711.
- Case performance (bull, p. 126): Air stock ₿839.5 / ₿442.4 / $24.0mm / 27 mo / $21,728; Air BOS+ ₿887.7 / ₿490.7 / $26.4mm / 26 / $20,548; Immersion stock ₿881.5 / ₿484.4 / $26.1mm / 27 / $20,694; Immersion BOS+ @3086W ₿924.2 / ₿527.2 / $28.2mm / 26 / $19,736; @4000W ₿857.3 / ₿460.0 / $26.9mm / 25 / $21,287; @5500W ₿713.1 / ₿316.0 / $17.6mm / 27 / $25,581.
- Head-to-head verdict (verbatim): "immersion performs better—more BTC mined in total, more BTC in holdings after paying for OpEx, and higher cumulative profit." (p. 126)
- Overclocked immersion: "a typical S19j Pro in immersion can hash at around 136 TH/s with a power consumption target of 4000 W... we've seen some hashing above 140 TH/s in ideal conditions"; only 2,375 machines needed, hardware CapEx $20.19MM, total $24.69MM (617.25 BTC), 323 PH/s. (p. 123)
- Extreme overclock: custom 6 kW PSUs "about $500/each" bring machine cost to $9000; at "5500 W each, we need 1727 S19j Pro's"; "a hashrate of 160 TH/s at 5500 W (34.4 J/TH)" for 276.3 PH/s total; total CapEx $20.04MM (501 BTC). (p. 124)
- BTC-denominated reality: bear-case final holdings "just under 400 BTC... 320 BTC short of our original CapEx spend"; bullish case "440 BTC, but still well below CapEx breakeven in BTC terms" — the two best BTC-denominated scenarios are the autotuned/overclocked ones, which "essentially produce a discount on the rigprice ($/TH) of your hardware." (pp. 121–122, 127)
- Immersion resale caveat: "the thermal paste used in hardware, including Antminer S19s, will dissolve in most dielectric coolants" — immersed machines "probably shouldn't ever be run in air", segregating the secondary market. (p. 129)
- Infrastructure longevity: "immersion systems can be used for multiple generations of hardware across 10+ years"; heat capture means "they are effectively dropping their electricity price by making the electricity count twice". (pp. 129–130)
- Last word: "the winning strategy... is using immersion cooling infrastructure and running it around stock power consumption or stock efficiency levels (i.e. moderate overclocking) with autotuning firmware like Braiins OS+." (p. 130)

## Key points (ch. 132–134 — The Emergence of Hydro (Water) Cooling)

- Adoption gap: "well over 1 GW of immersion cooling infrastructure has been built out by bitcoin miners in the last several years, hydro (i.e. water) cooling has been much slower to catch on. Bitmain released an 18 TH/s Antminer S9 Hydro in 2018 with minimal success." (p. 132)
- Mechanism: "water (potentially mixed with glycol) circulates through small tubes inside the hardware to cooling plates that are fixed to the hashboards. This is also called direct-to-chip or direct-to-plate cooling" — chips never touch fluid, so "it's possible to avoid using a costly dielectric coolant". (p. 132)
- Flagship spec: "the Whatsminer M53S Hydro from MicroBT, a 260 TH/s machine that consumes 6760 W at stock settings for an efficiency of 26 J/TH"; it uses "a standard 2U size" in server racks, where "1U = 1.75inches (4.45cm) tall x 19in (48.26cm) wide" — a move toward data-center standardization away from the "shoebox" form factor. (p. 133)
