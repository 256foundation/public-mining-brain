# Open Mining Economics

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md)
> Updated: 2026-10-08
> As-Of: 2026-10-08
> Status: Draft

## Overview

What open-source mining actually costs, why it can't win on $/TH alone, and where its real economic cases are: alternative form factors, heat reuse, and independence from Bitmain's supply chain. The honest baseline from the community's own manufacturing math: even with free ASICs, small-scale open hardware lands at $8-$12/TH against Bitmain's $.50-$1.50/TH — roughly an order of magnitude — so the mission is 'building something Bitmain doesn't control', not price parity [#2183 · 2025-05-16 · Mike Hamilton] [#2180 · 2025-05-16 · econoalchemist].

## The $/TH debate (May 2025)

- Small-scale manufacturing math (Mike Hamilton): even with free BZM2 ASICs, building 3 hashboards + control board + PSU + Fans + Shell at 3,000-10,000 machine scale costs $8-$12/TH (appx 400 GH/s per chip); Bitmain's economies of scale put them around $.50-$1.50/TH (not including asics) [#2183 · 2025-05-16 · Mike Hamilton]
- Bitmain's market position: 'They have captured over 80% of the market with this BS. Open source mining is currently a worse value. If we do this right it won't be like that forever.' [#2195 · 2025-05-17 · Skot Bitaxe]
- econoalchemist settled the mission question: 'The 256 Foundation is a nonprofit; this isn't about how big the market is, this is about building something Bitmain doesn't control' [#2180 · 2025-05-16 · econoalchemist]
- The foundation's real value is alternative form factors (home water heater, pool heater, brewing boiler); adit 'should be the focus of another dev' [#2188 · 2025-05-16 · Mike Hamilton]
- Elijah Sanders on Bitmain's incentives: 'Nothing bitmain does is to accommodate the customers. The entire design is to support as much Chinese industry as possible. From the shipping packaging to the components packaging' — not profit-maximizing for anyone but Bitmain 'selling shovels' [#2196 · 2025-05-17 · Elijah Sanders] [#2197 · 2025-05-17 · Elijah Sanders]

> **Status: Disputed** — aditBoard vs emberOne priority (May 2025)
> Bas | Mining Wholesale: aditBoard should be the priority — 'Ember great and all, but economically it does not make a lot of sense'; let MicroBT/Bitmain/Canaan/BitDeer race on cheap hashboards and plebs run them on FOSS Libre Boards via Adit; sees big heat-reuse/curtailment potential [#2168 · 2025-05-15 · Bas | Mining Wholesale 🇳🇱] [#2169 · 2025-05-15 · Bas | Mining Wholesale 🇳🇱] [#2170 · 2025-05-15 · Bas | Mining Wholesale 🇳🇱] [#2171 · 2025-05-15 · Bas | Mining Wholesale 🇳🇱] [#2175 · 2025-05-15 · Bas | Mining Wholesale 🇳🇱]. Mike Hamilton: adit 'should not be the focus of the foundation' [#2188 · 2025-05-16 · Mike Hamilton]. Reckless Apotheosis: kickstart the ecosystem around BZM2s to prove demand for 'ASICs on reels'; 'Bitmain really must die' [#2184 · 2025-05-16 · Reckless Apotheosis] [#2185 · 2025-05-16 · Reckless Apotheosis] [#2187 · 2025-05-16 · Reckless Apotheosis]. Skot: many mining use cases don't fit 1000W Antminer boards, hence the 100W emberOne; 'Of course it's hard to beat the $/W of a old S19j Pro hashboard, so for those we have the aditBoard project' [#2172 · 2025-05-15 · Skot Bitaxe]. Ryan: emberOne isn't meant to compete on price — it's an open reference for form factors distinct from Antminer boards [#2177 · 2025-05-16 · Ryan]. Bas's closing synthesis: Libre+Adit on native boards is the migration path ('from native shitmain stuff to hybrids to fully open source') and an indirect donation channel, but firmware for every 'shitmain' board variant is a time-consuming tradeoff against ember work [#2199 · 2025-05-17 · Bas | Mining Wholesale 🇳🇱] [#2201 · 2025-05-17 · Bas | Mining Wholesale 🇳🇱]. Best assessment: both tracks proceed; the mission (not $/TH) decides.

## Heat-as-service economics

- Heat-reuse-as-a-service could become a vertical inside HVAC: installers maintain miners under service contracts, plus education partnerships with home builders; adoption happens only when customers demand it, and CAPEX must be sold as household opex reduction [#604 · 2024-03-25 · Alex Brammer] [#606 · 2024-03-25 · Alex Brammer] [#607 · 2024-03-25 · Alex Brammer]
- The structural problem: miners obsolesce and the Bitcoin subsidy declines over time, unlike a 15-year water heater [#608 · 2024-03-25 · Alex Brammer]
- Scale reference: DR Horton built 89,000 homes in the prior year — the kind of builder home-mining advocates wanted to reach [#610 · 2024-03-25 · Alex Brammer]
- Company-owns-the-miner lease model keeps homeowner CAPEX at zero but concentrates rewards with the operator — 'a distributed mega miner', weaker for decentralization [#615 · 2024-03-25 · Tyler Stevens]
- Heat-arbitrage datapoint: Dylan Seib's hashprice+solar-aware controller means he is effectively paid +$0.13/kWh to heat his home with mining; the system downshifts when solar drops or the furnace wins [#3130 · 2025-10-15 · Dylan Seib]

## Sell vs hodl for heat miners

- Scripts over historical weekly hashprice/hashvalue data; example — S9 running at 60% power (8 TH) starting 1/1/2017, heat-only 5 months out of the year: ~$3700 if selling sats weekly vs 75.8 M sats (~$76,000) if HODLing [#1613 · 2025-02-07 · Tyler Stevens] [#1614 · 2025-02-07 · Tyler Stevens] [#1629 · 2025-02-07 · context]

## Site & energy deals

- 3MW of built-out grid power in brand-new construction including land listed at $1M without ASICs at 4¢/kWh (March 2025) [#1719 · 2025-03-17 · Elijah Sanders]
- Tariff timing: 67% US tariffs starting May 2025 front-loaded M64S purchase decisions [#1775 · 2025-04-05 · Elijah Sanders] [#1783 · 2025-04-05 · Elijah Sanders]
- Old-ASIC hold-out economics: a Whatsminer M31S+ — '82 trilly' — still running at '29j' because the owner hates to turn it off (April 2024) [#802 · 2024-04-11 · Barnminer Barnmyna]
- Hash the Torch pitch math: Altair Urlacher conversion + used S19-class unit + pool with 1k-sat Lightning payouts (Lincoin) is what makes 120 V meetup mining viable [#1043 · 2024-06-08 · Barnminer Barnmyna]

## Foundation funding economics

- 256F grants are funded as full-time salaries at market rate for the respective skill sets — across 4 projects 'it adds up'; budgets being updated, transparency report coming Fall 2026 showing how money flows [#5084 · 2026-07-22 · Tyler Stevens]
- Scott Offord working on a $1.5M grant application for GeoHashing (December 2025) [#3763 · 2025-12-01 · Scott Offord]
- Hardware projects need final validation + polish and the foundation is explicitly 'funding constrained right now' (July 2026) [#5079 · 2026-07-22 · Tyler Stevens]

## Used-equipment price points (2026)

- Used/rumored PSU pricing: APW12 units at $20 each (satstackingpleb), rumors of official Bitmain-branded new APW7 for $20; with the 120V unlock 'the APW12 is a champ' [#5122 · 2026-07-22 · Skot Bitaxe] [#5125 · 2026-07-22 · Skot Bitaxe] [#5126 · 2026-07-22 · Skot Bitaxe]
- Cheap 1200W APW3/7 PSUs change small-rack economics: support the molex connectors directly, two fit side-by-side in a 2U [#5093 · 2026-07-22 · Skot Bitaxe] [#5094 · 2026-07-22 · Skot Bitaxe]

## See Also

- [ASIC Thermals and Heat Reuse](../hardware/asic-thermals-and-heat-reuse.md)
- [Ember One & the BZM2 Hardware Stack](../hardware/ember-one-bzm2.md)
- [On-Demand Hashrate](../hashrate-market/on-demand-hashrate.md)
- [Repair, Supply & Vendors](../industry/repair-supply-and-vendors.md)
