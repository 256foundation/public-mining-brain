# Bitcoin Mining Heat Reuse — ch. 2: Hashrate Heating Across Different Scales (extract)

> Source: https://braiins.com/books/bitcoin-mining-heat-reuse?lang=en (Braiins Publishing, free distribution; authored by Tyler Stevens; foreword by Paul Jin Li)
> Collected: 2026-10-11
> Published: 2025
> Registry ID: braiins-books
> Posture: extract (key information with chapter attribution; full text at source)
> Note: text extracted via pdftotext from the author's final per-chapter production PDFs; the typeset font's space glyph extracts as "!" and is normalized to spaces in quotes; typography otherwise verbatim.

## Key points (ch. 2)

- Origin story: "Bitcoin heat reuse originated as small-scale systems in homes and small businesses. These early prototypes and proof-of-concepts were largely the work of bitcoin plebs and hobbyists" — later, "some large-scale mining sites began to sell or repurpose their excess heat in district applications." (p. 26)
- The untapped middle: "There is a substantial untapped middle ground for heat reuse between small-scale home setups and large-scale operations." (p. 26)
- "The incentive to reduce utility costs is the largest driver for hashrate heating implementation." (p. 26)
- District heating defined (footnote): "a centralized system where heat is generated at a plant and distributed via insulated pipes to multiple buildings or facilities for space and water heating." (p. 26)
- Tier 1 — Residential & Small Business: "Mining Scale: Roughly 100 W - 100 kW"; "Typically Home and Small Business Zone & Water Heating"; considerations include consumer energy prices, "Complexity of integration (install difficulty)", "Dependence on heating demand (intermittent usage)", "Limited maintenance, technician, and tradesmen understanding". (p. 27)
- Tier 1 verdict: "It's still financially feasible for some, but is a more unique market." (p. 27)
- Tier 2 — Industrial, Manufacturing & Commercial: "Mining Scale: Roughly 100 kW - 10 MW"; includes "large warehouses, apartment buildings, office spaces, and manufacturing plants, as well as industrial operations that require low-grade (warm, not hot) heat for production." (p. 28)
- Tier 2 advantages: "More favorable commercial energy prices", "Higher potential for constant heat demand (more usage = faster payback)", "Financing, access to capital, and tax write-offs or subsidies", on-site technicians. (p. 28)
- Tier 2 verdict: "It's the most well-rounded candidate for hashrate heating." (p. 29)
- Tier 3 — Mega Miners & Power Generation: "Mining Scale: Roughly 10 MW+"; "profitable (for now) without needing to repurpose their exhaust heat thanks to cheap energy access"; "Thermodynamic cycles that turn excess heat back into electricity have yet to be showcased for mega-miners" (Rankine/Brayton cycles footnote). (pp. 29–30)
- Tier 3 potential: "with well-balanced energy prices and revenue from heating, the overall cost of mining can be significantly reduced, potentially resulting in net negative operational costs." (p. 29)
- Tier 3 future-proofing: "As block subsidies decrease, heat monetization becomes more attractive and possibly even necessary for these large-scale businesses to survive into the future." (p. 29)
- Energy pricing across tiers: residential consumers face "higher utility rates with limited negotiating power"; industrial operations get "scale-based pricing", "Power Purchase Agreements (PPAs)", or "near-production-cost energy by operating close to energy sources or off-grid." (p. 31)
- Integration ladder: at smallest scale "localized zone heating... simple to implement plug-and-play solutions, requiring no integration"; replacing central heat "requires more substantial modifications... upgrades to electrical systems... along with adjustments to HVAC ducting or hydronic plumbing." (pp. 31–32)
- Integration reality check: "bitcoin miners are industrial-grade electronics. They are not yet designed to perfectly integrate with off-the-shelf heating infrastructure found at your local hardware store." — "there is limited contractor experience." (p. 32)
- In integrated systems: "the bitcoin miners act as the heating core in the system that converts electricity into warmth. But to replicate the performance of a furnace or water heater, the miner must be paired with other hardware to ensure the heat is effectively captured and distributed." (p. 32)
- Capital reality: "Bitcoin miners are expensive devices – especially when compared to boilers and furnaces used most commonly for heating." — but "Unlike traditional heaters such as boilers and furnaces, however, these ones pay you back over time." (p. 34)
- Tax/subsidy levers: businesses "write off expenses from their taxable income"; "Many grants and subsidies also exist in the name of emissions reduction and electric heating." (pp. 34–35)
- Revenue-asset ratio (KPI): "The heat delivery and control infrastructure does not pay you – only the bitcoin miners. Optimizing this ratio results in a faster return on investment." — formula as served: "RatioRev Gen Assets = CostMiners / CostInfrastructure" (p. 35)
- Ratio by tier: "typically higher for large mega-mining operations. Then comes industrial operations... Typically, home and small business hashrate heating systems have the worst ratio." (pp. 35–36)
- "The bigger and closer to the money printer you are, the better you have it." (p. 36)
- Duty cycle definition: "the percentage of time that the system is actively operating to provide heat, relative to the total time period being considered, or the fraction of power a miner runs at compared to its maximum output capacity." Worked example: 15 min/hour = 25% time-based; "1250 watts" average vs "5000 watts" max = 25% power-based. Formulas as served: "Duty CycleTime= TimeON / TimeTOTAL", "Duty CyclePower = PowerMiner / PowerMiner Max". (p. 36)
- Duty cycle by tier: residential depends on climate; industrial "Food plants, distilleries, green houses, and countless other businesses require heat year-round"; mega-mines "operate with almost full uptime. Their duty cycle is near 100%." (p. 37)
- Tier conclusion: "Hashrate heating systems that run more often will pay themselves off faster than systems that run intermittently. Given this fact and the benefits of their scale, industrial and manufacturing operations are the best suited for hashrate heating." (p. 37)
- Section flow: TIER 1: RESIDENTIAL & SMALL BUSINESSES → TIER 2: INDUSTRIAL, MANUFACTURING & COMMERCIAL BUSINESSES → TIER 3: MEGA MINERS & POWER GENERATION → COMPARING TIERS (Energy Pricing / Levels of Integration and Infrastructure / Economics and Financing / Uptime and Duty Cycle) → ONE FILTER FITS ALL? (pp. 26–37)
