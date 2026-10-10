# Hashrate Heating Economics

> Sources: Hashrate Heatpunks Telegram group, 2024-08-02 → 2026-10-08
> Raw: [Hashrate Heatpunks Telegram signal digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

A miner turns essentially all of its electricity into heat, so it heats as well as a resistive heater and also earns some bitcoin. The Heatpunks summed it up as 'Heat IS the product. BTC is the prize' [#985 · 2024-09-04 · Jonathan Y]. Whether it *pays* depends on a few things: what fuel the miner replaces (resistive electric, propane and heating oil are the easy targets; cheap natural gas and heat pumps are hard to beat), the local electricity rate against current hashprice, how many hours a year the heat is actually used, and how much the hardware costs [#579 · 2024-08-10 · Tyler Stevens] [#3320 · 2025-01-12 · Cody Harris] [#9654 · 2026-03-13 · Cody Harris]. Payback reports for the right customer run from about 12 to 24 months. The members still disagree about efficiency, heat pumps, always-on versus intermittent operation, and whether a bought system ever 'mines its sats back'. This page gives the rules of thumb first, then the payback math, sizing, business models and tax, and ends with dated price and rate data points.

## Rules of thumb

- **A miner is a heater that also earns bitcoin.** For the same 1600w, case 1 is a heater that earns no BTC and case 2 is a miner that gives the same BTU's plus some BTC [#557 · 2024-08-10 · Dane O]. Newcomers are often surprised that it is 'essentially a 1:1 kw of electricity in to kw heat out' [#6938 · 2025-08-06 · Patrick Patel]. In the members' words, 'All miners are very close to 100%' efficient as heaters, minus fans and LEDs. The real losses are BTUs that escape through the case and piping before reaching the load [#6772 · 2025-07-10 · Travis Bitkle] [#6770 · 2025-07-09 · Travis Bitkle]. One hydro data point is '4kw in equals 3.41 BTU's per watt out' [#6769 · 2025-07-09 · Travis Bitkle].
- **Natural gas access is the biggest variable.** US natural gas heat costs about the equivalent of $.02-$.03 /kwhr from a BTU perspective, so propane and electric-resistance users are the 'no-brainer' targets [#579 · 2024-08-10 · Tyler Stevens]. Sales advice from an installer is not to try to convince people. Instead, target anyone heating with electricity or propane [#4581 · 2025-03-19 · Cade] [#4592 · 2025-03-19 · Cade].
- **Go where heat spend is already high.** A $100/yr heat bill gives you no case. A $100k/mo industrial heat bill does [#1168 · 2024-09-17 · Jonathan Y] [#1169 · 2024-09-17 · Jonathan Y] [#1170 · 2024-09-17 · Jonathan Y].
- **Utilization is everything.** Downtime hurts hashrate heating, so industrial and business clients that use heat all year are preferred. In Colorado the best residential targets are high-elevation homes without natural gas [#387 · 2024-08-04 · Tyler Stevens] [#137 · 2024-08-02 · Tyler Stevens]. Outside pool and water heating, most use cases lacked the utilization to justify the extra expense. Without that use, a miner is 'just really expensive resistive heating element' [#768 · 2024-08-23 · Harrison The Space].
- **Hot water is the most universal load.** Everyone has a water heater and uses it daily, in every climate and all year [#2978 · 2024-12-29 · Karl] [#3000 · 2024-12-29 · Dane O].
- **The easiest sale is a replacement that was going to happen anyway.** The best case is a customer who is about to spend '10 grand on a home furnace or boiler + install anyway' [#6658 · 2025-06-29 · Tyler Stevens]. In a new central heating system, the electrical, cabinet and hydronic costs would be paid anyway, so the only extra cost is the ASIC [#773 · 2024-08-23 · Cade]. A related pitch is to keep the system price close to the alternative heating source, which makes the customer profitable given their sunk energy costs [#6648 · 2025-06-28 · Dane O].
- **New miners usually don't pencil out for heating.** Older, cheap hardware usually wins, as the sections below show [#9654 · 2026-03-13 · Cody Harris] [#3542 · 2025-01-16 · Patrick Patel].
- **Think in hashprice.** Do trade calculations in terms of hashprice [#2811 · 2024-12-16 · Bob] [#2814 · 2024-12-16 · Bob]. Hashrate heating works while block reward is roughly equal to the cost of electricity [#278 · 2024-08-02 · Toine Heat Reuse].

## Comparing against other heat sources

### Fuel cost on a $/BTU basis

To compare fuels, convert any fuel or power cost into $/BTU or $/joule of heat and correct for appliance efficiency. Gas furnaces are in the 90% range, electric heat is 100%, and heat pumps are 200-400% [#5181 · 2025-03-30 · Tyler Stevens]. One home heat-pump water system was cited at 1kW electrical input for 4kW heat output [#5231 · 2025-03-31 · Dev 🇳🇿].

### Heat pumps and COP framing

- 'Heat pumps are electrically efficient. Hash Heat is financially efficient.' Hash heating uses more energy (a lower SCOP) but can cost less to operate, because mining revenue offsets the energy price [#3965 · 2025-02-12 · Cody Harris].
- Heat-pump COP depends on outdoor temperature. A COP of 4-5 is typically measured at 15C, when little heat is needed. COP drops into the 2-3 range at -5, and lower below that [#3968 · 2025-02-12 · Nicolas Drouin-Audet]. Climate matters: Wyoming runs aux backup constantly, Denmark almost never needs it, and heat pumps work poorly in dry, high-altitude climates far below freezing [#3988 · 2025-02-12 · Cody Harris] [#3993 · 2025-02-12 · Tyler Stevens].
- Effective COP of a miner (December 2025): at <10 cent power and a hashprice of 0.037 $/TH/s/day, an M64 has 'a COP of ~ 7.5' [#8276 · 2025-12-15 · Tyler Stevens] [#8275 · 2025-12-15 · Heatpunk Forum]. Members suggested several refinements. Plot heat-pump COP against outdoor temperature, compare tariffs against outdoor temperature, and count total cost of ownership, since heat pumps need maintenance [#8286 · 2025-12-16 · Alex HeatBit]. Altitude and temperature should also be added [#8301 · 2025-12-16 · Cade].
- People perceive the same system very differently depending on their rate. Below 10c/kWh the experience is 'I get paid to heat my home', while above 15c/kWh it is a heating bill about 20% lower. Hashrate heating should therefore win in the market pockets where the numbers line up [#8292 · 2025-12-16 · Jarno] [#8293 · 2025-12-16 · Jarno] [#8294 · 2025-12-16 · Tyler Stevens].
- A miner does two jobs, heat and network security, much as engine heat warms a car's cabin [#3984 · 2025-02-12 · Karl]. For someone whose capital is in bitcoin, the hashrate itself adds value beyond the COP math [#8280 · 2025-12-15 · Karl].

> **Status: Disputed** — heat pumps vs miners
> Bas (Mining Wholesale, EU) said that in the EU home mining for heat is 'really niche due to better alternatives'. In his view the capex of new-gen machines is too high, although older machines 'do have a chance', and he called the HS05 a questionable choice [#7971 · 2025-11-25 · Bas | Mining Wholesale 🇳🇱] [#7975 · 2025-11-25 · Bas | Mining Wholesale 🇳🇱]. Earlier, Denmark (electricity about 0,35/kwh in USD terms) was called very hard to make profitable even with heat reuse, and district heating is hard to beat for Danish city homes [#3976 · 2025-02-12 · Jake⚡️] [#3978 · 2025-02-12 · Nicolas Drouin-Audet] [#3997 · 2025-02-12 · Jake⚡️]. Cade's counterpoint is that heat pumps don't power snow melt or hot tubs and earn no revenue, while mining heat reuse is dependable and does earn [#7915 · 2025-11-24 · Cade] [#7916 · 2025-11-24 · Cade]. Best assessment (as of 2026-10): heat pumps win on energy where power is expensive and winters are mild. Miners win on cost where power is cheap, the climate is cold or dry and high, the load is luxury heat, or the hardware is old and cheap.

### Efficiency: does J/TH matter when replacing resistive heat?

> **Status: Disputed**
> View A: efficiency is pointless when replacing resistive heat. A resistive heater earns 0%, so any BTC is a gain [#534 · 2024-08-10 · Dane O] [#557 · 2024-08-10 · Dane O] [#573 · 2024-08-10 · Jonathan Y] [#986 · 2024-09-04 · Dane O]. View B: efficiency still matters for heating, because the goal is the best bang for the buck [#553 · 2024-08-10 · Toine Heat Reuse]. A related argument from the upgrade debate is that the efficiency premium isn't worth paying when you hash intermittently [#2073 · 2024-11-20 · Karl] [#2075 · 2024-11-20 · Cade]. Best assessment: J/TH barely affects heat output but sets how much BTC each kWh earns. For heat-led, intermittent use, cheap older machines usually give a better return on capital than efficient new ones.

### Is your electricity cost irrelevant?

> **Status: Disputed**
> If you already heat with electricity, the electricity cost is irrelevant because mining adds no extra consumption [#3522 · 2025-01-16 · Patrick Patel] [#3527 · 2025-01-16 · Alex HeatBit]. Heat-first mining makes electricity 'effectively' free, since the house must be heated anyway [#2063 · 2024-11-20 · Jonathan Y]. Brett Rowan's counter is that this isn't the common case, residential power is expensive so margins are thin, and miners are worse than resistive heat on maintenance today [#3521 · 2025-01-16 · Brett Rowan] [#3534 · 2025-01-16 · Brett Rowan] [#3546 · 2025-01-16 · Brett Rowan]. Best assessment: during heating hours the marginal cost of mining heat is zero for someone already on resistive heat. Any heat the miner makes beyond what is needed is plain mining at the residential rate.

### Measured useful-heat fraction

The 'close to 100%' rule needs one caveat. A peer-reviewed study of water heating with an S19 Pro Hydro found that only about ~90% of the electricity input became useful heat [#10339 · 2026-07-21 · Heatpunk Forum]. A separate research paper evaluated the cost efficiency of two systems in a Softwarm heating project [#9754 · 2026-03-27 · Heatpunk Forum].

## Break-even and payback math

### Break-even electricity rate

Elijah Sanders' method takes revenue per TH per day and the machine's efficiency. Using the example input $/th/d = $0.0557 (May 2025) [#6024 · 2025-05-17 · Elijah Sanders]:

1. $/th/d ÷ 24h → $ per TH-hour
2. ÷ J/TH → $/W/h
3. × 1000w (1kw) → the $/kWh break-even rate

A simple hashprice estimate is 450 (BTC mined per day) × BTC price ÷ network hashrate [#8791 · 2026-01-21 · Nick]. In January 2025, break-even on most X19 models was below .08c. At that rate you lose money on any heat you make but don't use, and insights.braiins.com is the reference [#3320 · 2025-01-12 · Cody Harris]. Karl counters that break-even math ignores the extra value of home-mined coins, which are KYC-free with a short history from the coinbase [#3327 · 2025-01-13 · Karl].

### Ways to frame payback

- **Heating seasons.** Count the heating seasons needed to pay off the system against a heater that doesn't mine. Cody's system should pay off in 'like 1.5 heating seasons', or about '.5 heating seasons' counting only the extra install cost over propane [#2808 · 2024-12-16 · Cody Harris].
- **Discounted bitcoin.** If the power bill is $400 and you mine $100 of bitcoin that month, you bought 'kyc free Bitcoin at a 25% discount' [#2810 · 2024-12-16 · Karl].
- **Total cost of ownership versus a heat pump.** Nicolas Drouin-Audet's customer calculator (February 2025) assumes power at 0,08$/kWh, a 5% annual Bitcoin gain and a 3% hashprice-index increase. On those inputs, cost of ownership falls below a heat pump after 15 months and full payback comes at 35 months, even though the capex is higher [#3969 · 2025-02-12 · Nicolas Drouin-Audet] [#3972 · 2025-02-12 · Nicolas Drouin-Audet]. The model assumes each 1% BTC price rise is matched by a 1% hashrate rise. The hashprice index is BTC price ÷ difficulty, so a 5% index gain means 5% more BTC for the same hashrate [#3975 · 2025-02-12 · Nicolas Drouin-Audet] [#3977 · 2025-02-12 · Nicolas Drouin-Audet].
- **The 'test drive'.** Let a prospect plug a heater in for a month so they see the electric cost next to the mined revenue [#538 · 2024-08-10 · Toine Heat Reuse].
- **Forecasting humility.** Price-growth guesses are always wrong, and 'the only thing that has been somewhat predictable is that Hashrate doubles every year' [#6042 · 2025-05-18 · Patrick Patel]. For that reason Tyler built a tool that maps a building's actual heat energy use onto historical daily hashprice and hashvalue to show what it would have earned, with no forward projection [#6426 · 2025-06-08 · Tyler Stevens] [#6431 · 2025-06-08 · Tyler Stevens].

### Reported ROI and payback (field claims)

| Claim | Context | Anchor |
|---|---|---|
| Pre-halving, many setups would ROI in 18 months | general, 2024 | [#278 · 2024-08-02 · Toine Heat Reuse] |
| About 12 months owner ROI | two industrial water-tank setups | [#3552 · 2025-01-16 · Cade] |
| About 18-24 month ROI; about 12 months with an older machine like a j Pro | Softwarm customers, June 2025 | [#6657 · 2025-06-29 · Cade] |
| 3+ year payback | new S21 miners, Jan 2025 | [#3322 · 2025-01-12 · Zackery Miller] |
| S19j Pro fastest ROI when heat cost is sunk | Jan 2025 | [#3323 · 2025-01-12 · Cade] |
| '50% cagr on invested capex per year' | claimed projection, not yet backed by data | [#3560 · 2025-01-16 · The schnauze] |
| Stacked about 0.1 BTC over two years | concrete-plant water tank plus office | [#6909 · 2025-08-01 · Cade] |
| Saved over 600$ in 6 months | basement dry cooler for jacuzzi and water heater | [#568 · 2024-08-10 · Dane O] |
| Hot water at 'half price' | Karl's canola-immersion water heater | [#8282 · 2025-12-15 · Karl] |
| Costs $28/month to run an M64 vs $300/month mined 'at today's hashprice' | Elijah, May 2025 (power rate not stated) | [#5975 · 2025-05-12 · Elijah Sanders] |
| Around $9500 annual power vs $11500 annual mining | non-profit pitch projection | [#6425 · 2025-06-08 · Code] |

> **Status: Disputed** — does a bought system ever pay back in sats?
> Karl says it is 'very hard to end up with more sats than you started' even with used gear. He values his heat at 'about 30 percent' and argues that a DIY, permaculture-style build is the way to end up with more bitcoin [#6651 · 2025-06-28 · Karl]. Cade reports 18-24 month ROI for customers, or about 12 months with an older machine [#6657 · 2025-06-29 · Cade]. Dane disagrees with 'never mine the sats back' and says it depends on the use case [#6655 · 2025-06-29 · Dane O]. Best assessment: payback holds when the heat displaces a costly fuel or a planned replacement and the hardware is cheap. It does not hold for pure-sats accounting on new gear.

### HODL vs sell backtests

- A backtest of an S9 at 60% power (8 TH) from 1/1/2017, heating 5 months a year, gives about $3700 if the sats were sold weekly, versus 75.8 M sats (~ $76,000) if held [#3880 · 2025-02-07 · Tyler Stevens].
- Tyler's Python scripts take mining power (TH/s) and a start date. They return either a fiat sum using each day's hashprice (selling to offset heat) or a satoshi sum using each day's hashvalue (HODL) [#3872 · 2025-02-05 · Tyler Stevens]. Historical data comes from `https://insights.braiins.com/api/v1.0/hashrate-value-history`. The `hashrate-stats` endpoint returns only the live reading [#3866 · 2025-02-05 · Dylan Seib] [#3863 · 2025-02-05 · Tyler Stevens].
- Live hashprice for feasibility models was being pulled manually from Luxor, and Cade noted an API is mentioned 'on the silver plan' [#2858 · 2024-12-20 · Tyler Stevens] [#2861 · 2024-12-20 · Cade]. Hashrateindex also has an ASIC price index API [#5402 · 2025-04-10 · Wilfred Allyn].

### Calculators

- **Exergy hashrate heating calculator.** The code is at github.com/exergyheat/webapp-calculators, with the equations documented at docs.exergyheat.com, and Canada support (CAD, fuel rates, heat map) was added in December 2025 [#8332 · 2025-12-19 · Tyler Stevens] [#8348 · 2025-12-20 · Tyler Stevens] [#8349 · 2025-12-20 · Tyler Stevens]. It is purely fiat-based at a moment in time and ignores bitcoin appreciation [#8336 · 2025-12-19 · Tyler Stevens]. Network inputs have three knobs: % fees of the block subsidy, total network hashrate and hashvalue [#8660 · 2026-01-13 · Tyler Stevens]. Reports can be printed to pdf for prospective clients [#8976 · 2026-01-30 · Heatpunk Forum].
- **Solar Monetization calculator** (calc.exergyheat.com). It estimates sats from an array or from excess solar exported to the grid. It assumes no battery and uses PVWatts kWh [#8511 · 2026-01-03 · Tyler Stevens] [#8520 · 2026-01-03 · Tyler Stevens]. Its utilization example is a 10 kw system with a 1 kw miner, which is 10% [#8524 · 2026-01-03 · Tyler Stevens].
- **Cody's Propane vs Bitcoin calculator**, for checking whether a machine pencils out against propane [#9654 · 2026-03-13 · Cody Harris] [#9683 · 2026-03-16 · Heatpunk Forum].
- **Ian's calculator** uses simple linear difficulty and price assumptions, compares three miners or infrastructure types, takes a configurable halving date, and outputs electrical and all-in cost per coin [#6053 · 2025-05-19 · Ian].

## Sizing for the coldest day

- **Size for the monthly average, then plan for the extremes.** Matching heat demand month by month gives the average target, but the existing furnace was sized for 'the coldest day'. Bob replaced a 120,000 BTU (35kW) furnace with 2 S19jPros that can overclock to 9kW. The house held 71-72 F all winter except for two sub-zero 24-hour periods, when he needed a gas fireplace [#427 · 2024-08-05 · Bob].
- **Don't oversize the mining.** A miner system designed for the coldest day spends a lot of money on mining power that won't get used. Add a cheap supplementary heater that doesn't mine for the one or two coldest days instead [#427 · 2024-08-05 · Bob]. Keep a backup heat source that doesn't need electricity for power outages [#2890 · 2024-12-23 · Karl] [#2893 · 2024-12-23 · Trevor Bello].
- **Other sizing inputs** are other heat sources in the building, intended mining uptime, and whether excess heat can be rejected outside [#428 · 2024-08-05 · Gerald Glickman].
- **Data points.**
  - 13kW for 3000sqft on a hydronic floor (a 1300Th customer), with 2 outdoor air coolers allowing 24/7 operation and summer pool heating, and the gas boiler kept as backup [#385 · 2024-08-04 · Nicolas Drouin-Audet] [#388 · 2024-08-04 · Nicolas Drouin-Audet].
  - A hydronic-floor replacement plan set the power limit around 2700 watts based on last year's coldest month and lets the firmware adjust down. That customer pays 14 cents and doesn't want summer mining [#380 · 2024-08-04 · Tyler Stevens].
  - A 3000 W electric water heater used 7 months a year for hydronic floor heat was replaced by one immersion miner [#135 · 2024-08-02 · Tyler Stevens] [#146 · 2024-08-02 · Tyler Stevens].
- **Don't sell a miner on 'more heat makes more bitcoin'.** Common misconceptions are that mining generates electricity, or that more heat makes the computer make more bitcoin [#6934 · 2025-08-06 · Cade]. Thermal modeling usually isn't needed, and plug-and-play with correct sizing is the key [#676 · 2024-08-19 · Tyler Stevens].

## Operating strategy and utilization

### Always-on vs intermittent

> **Status: Disputed**
> Cody Harris argues that intermittent heat reuse with new machines can't pay off capex except where energy is very cheap. He says dumping heat is only an option in 'ultra juicy .04c power' regions, and his own system dumps no heat [#4807 · 2025-03-23 · Cody Harris] [#4814 · 2025-03-23 · Cody Harris] [#3564 · 2025-01-16 · Cody Harris] [#3568 · 2025-01-16 · Cody Harris] [#3574 · 2025-01-16 · Cody Harris]. Cade runs all machines 24/7/365 and dumps unused heat. He says this is still profitable with S19 Pros, though some units were turned off or way down in summer to stay profitable [#4821 · 2025-03-23 · Cade] [#4822 · 2025-03-23 · Cade] [#3572 · 2025-01-16 · Cade] [#3573 · 2025-01-16 · Cade]. The schnauze prefers always-on with a built-in heat dump for best ROI [#4849 · 2025-03-24 · The schnauze]. Brett notes that heat dumping wastes heat and lowers system efficiency [#3550 · 2025-01-16 · Brett Rowan]. Best assessment: always-on with a dump pays where power is below break-even (a low power-cost context of '.058c' was cited [#4844 · 2025-03-23 · Dane O]). Elsewhere, run heat-led and intermittent on cheap hardware.

- **Mining user types (Cade):**
  1. Need heat but power is expensive relative to BTC, so they run on/off with demand (most of the USA).
  2. Luxury heat, such as hot tubs and snow melt.
  3. Straight mining 24/7 on cheap power.
  4. Ideologues.

  Air-cooled fits type 1. Immersion in a loop fits types 2 and 3 because it can run all the time [#3581 · 2025-01-16 · Cade] [#3582 · 2025-01-16 · Cade] [#3583 · 2025-01-16 · Cade]. Types 3 and 4 need a heat dump, types 1 and 2 need variable output management, and a user can become type 3 depending on hashprice [#5066 · 2025-03-28 · Cade] [#5067 · 2025-03-28 · Cade].
- **'Heat is the product. Overclocking is optimal.'** Two computers at 10kw make over 30k BTU/hr. Turn the S19j down to half power when the heat isn't needed seasonally or when it's unprofitable [#3773 · 2025-01-22 · Cade] [#3774 · 2025-01-22 · Cade]. Controls in development let users flip between 'Mining profitable' (max output) and 'Mining not profitable' (just heat) modes [#4837 · 2025-03-23 · Cade].
- **Summer profit mode.** A planned Home Assistant automation pulls real-time hashprice, takes your electric rate, TOU rates and solar, and runs the miner only when it is profitable. It is meant for summer, when you want profit rather than heat [#7450 · 2025-10-23 · Tyler Stevens]. Most Loki and home heater owners were 'letting them rip' through summer, mostly on solar [#6093 · 2025-05-23 · Karl].
- **Hardware vintage drives the priority.** Installs of older hardware put heat ahead of uptime. New efficient miners suit clients who want uptime, because they can ROI on residential rates [#852 · 2024-08-25 · Toine Heat Reuse] [#856 · 2024-08-26 · Dane O].

### Rates, time-of-use and thermal storage

- **Peak-rate scheduling.** Avoiding peak hours cut the effective cost from $0.14 CAD to 0.097 CAD per kWh while keeping about 80% uptime [#204 · 2024-08-02 · Toine Heat Reuse] [#205 · 2024-08-02 · Toine Heat Reuse].
- **Off-peak thermal storage.** One plan uses an insulated 500 gal tank charged only off-peak at $0.045/kWh, targeting 50,000 BTUs an hour for 7-8 hours to cover on-peak periods [#3648 · 2025-01-18 · Travis Bitkle] [#3650 · 2025-01-18 · Travis Bitkle] [#3655 · 2025-01-18 · Travis Bitkle]. Thick radiant floors can serve as thermal mass to use $.06 off-peak power [#3651 · 2025-01-18 · Cody Harris].
- **Cheapest-hours scheduling.** A biofuel plant needs heat only 16 of 24 hours, so it picks the 16 cheapest hours in the daily power market [#5168 · 2025-03-30 · csh2000].
- **Demand-based rates.** Power rates get much better above 100kw of demand, and a garage-scale immersion box makes sense at around 25j/th efficiency [#3096 · 2025-01-04 · Karl].
- **Solar.** Solar mining suits anywhere without 1-1 net metering, and miners can read a CT meter to soak up what would be exported [#3013 · 2024-12-31 · Dane O] [#3014 · 2024-12-31 · Dane O] [#8378 · 2025-12-22 · Dane O]. A business with natural gas heat and $0.20/kWh electricity basically needs solar, or a long wait for large price appreciation, before hashrate heating makes sense [#8533 · 2026-01-03 · Jon C] [#8540 · 2026-01-04 · Tyler Stevens].
- **Separate metering.** One home added a full second 200 amp panel. The ideal would be ASIC heating plus an EV on that panel at an alternate rate [#2541 · 2024-12-05 · Jonathan Y].

### Low power, duty cycling and standby cost

- **Low-wattage running is inefficient.** Under 1200w an S19 is 'not really worth it' [#1080 · 2024-09-07 · Toine Heat Reuse] [#1081 · 2024-09-07 · Zack Bomsta]. Duty-cycling at a higher, efficient wattage beats running at low wattage. For example, to meet 600W of demand, run at 1200W half the time if thermal mass allows cycles longer than 20 minutes [#1082 · 2024-09-07 · Zack Bomsta].
- **Standby isn't free.** Antminers draw 150w to 240w in standby, and Braiins sleep mode is about 200w [#742 · 2024-08-23 · Toine Heat Reuse] [#257 · 2024-08-02 · Toine Heat Reuse]. LuxOS curtailment was reported at only 25 watts, with only the control board left on [#741 · 2024-08-23 · Tyler Stevens]. See [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md).
- **Heating slowly may save energy.** Karl finds it more power-efficient to heat water slowly and to dry clothes with more airflow at a lower temperature. This is his observation, not a measurement [#3002 · 2024-12-29 · Karl].
- **Pool choice matters for on/off heaters.** A 2025 S9 experiment found 'The juice is not worth the squeeze from a utility bill perspective', with FPPS leading TIDES by ~3.3% [#7080 · 2025-08-14 · Heatpunk Forum]. See [Pool Choice for Heat Miners](../pools/pool-choice-for-heat-miners.md).

## Hardware choice and build costs

### Old vs new miners

- **Older machines usually win for heat.** S19s went from $4k up to $13k in an earlier cycle. Karl says the efficiency premium isn't worth it when hashing intermittently, and Cade says to use older machines if you can't mine continuously without needing the heat [#2060 · 2024-11-20 · Jonathan Y] [#2073 · 2024-11-20 · Karl] [#2075 · 2024-11-20 · Cade]. Cheap units that are unprofitable to run (sub 1k) can be used instead of new 5k miners [#3542 · 2025-01-16 · Patrick Patel]. Two S19K pros deliver more than one S21 for less capital and operating cost [#3958 · 2025-02-10 · Toine Heat Reuse].
- **The PSU holds much of the value.** On S19s the PSU is 'worth practically as much as the boards' [#2078 · 2024-11-20 · Karl].
- **Cheap last-gen silicon.** A mini3-style heater built on cheaper last-gen silicon might ROI faster [#4391 · 2025-03-04 · Cody Harris]. A miner-based space heater is a tough sell when baseboard heaters cost about 100 bucks [#3148 · 2025-01-07 · Trevor Bello].
- **Hardware lifetime.** A water heater lasts ~20 years and a hash board won't, so upgradability has to be designed in [#1028 · 2024-09-04 · Jonathan Y] [#1030 · 2024-09-04 · Jonathan Y]. Appliances can fund their own upgrades from earned sats. Karl's water heater paid for its upgraded heat exchanger and S19 KPro boards [#5162 · 2025-03-29 · Karl] [#6651 · 2025-06-28 · Karl].
- **Difficulty outlook (November 2024 debate).** Travis Bitkle expected difficulty to spike and cancel much of any price gain as old M30's and jPros come back online ('Could be up 50% in 6 months easy'). Karl thought new mines can't come online as fast as price rises [#2094 · 2024-11-21 · Travis Bitkle] [#2096 · 2024-11-21 · Travis Bitkle] [#2095 · 2024-11-21 · Karl].

### Build-cost examples

- **Central heat core for 4 ASICs (August 2024).** A central ASIC heat core plus hydronic system for 4 ASICs was costed at roughly Electrical: 1k, Cabinet frame out: 500, Hydronic system parts: 5k and Immersion equipment: 3k [#770 · 2024-08-23 · Cade].
- **Karl's DIY immersion water heater.** It cost 'less than $100 in parts' beyond the pumps, oil and miner [#2996 · 2024-12-29 · Karl]. Later he put the pumps and heat exchanger at $136, plus $60 of canola oil [#6651 · 2025-06-28 · Karl]. Dane estimated the same pumps and HX at about $200 retail [#6648 · 2025-06-28 · Dane O].
- **Ducted S19 (March 2025).** A used S19 95TH (3250W) bought for $300 USD was cleaned, shrouded and ducted into a furnace in about an hour. It runs at about 23 W/TH on LuxOS, and Toine says he is 'heating at a 90% discount' at his rate [#4671 · 2025-03-22 · Toine Heat Reuse]. Once the space warms and the miner downclocks, he estimates about $0.20 per day to heat the cabin [#4680 · 2025-03-22 · Toine Heat Reuse].
- **DIY portable 120V hydro miner.** About $350 for hydro block, pump, fittings and plate exchanger [#8260 · 2025-12-11 · Josh].

### Dated hardware price points

Prices are volatile and each is dated to its message.

| As of | Item | Price | Anchor |
|---|---|---|---|
| Aug 2024 | Fog Hashing immersion tank | $1000 | [#142 · 2024-08-02 · Tyler Stevens] |
| Aug 2024 | Two C1's, a dry cooler and 10gallons of Bitcool (old unused stock) | $400 | [#144 · 2024-08-02 · Cody Harris] |
| Aug 2024 | Used S19k pro | 900 (CAD) | [#840 · 2024-08-23 · Toine Heat Reuse] |
| Oct 2024 | Used S19k pro; S19j; S19 Pro | $400; around 400; 915$usd each | [#1278 · 2024-10-05 · Toine Heat Reuse] [#1281 · 2024-10-05 · Trevor Bello] [#1280 · 2024-10-05 · Nicolas Drouin-Audet] |
| Oct 2024 | New S19k pro 115T (7 months warranty) | 7,6$/Th, vs 9,6$/Th paid recently | [#1562 · 2024-10-15 · Nicolas Drouin-Audet] [#1567 · 2024-10-15 · Nicolas Drouin-Audet] |
| Oct 2024 | New S19k pro, Amazon business | $1400 cad | [#1614 · 2024-10-20 · Toine Heat Reuse] |
| Oct 2024 | S21 listings at $4/TH | most likely a scam | [#1629 · 2024-10-20 · Alex HeatBit] |
| Oct 2024 | ePIC UMC V5 control board | 150$ | [#1744 · 2024-10-28 · Trevor Bello] |
| Nov 2024 | Used S19 J Pro (104)TH, cleaned, 1yr warranty (Montreal) | $520 / unit; 4 units bought for $2000 | [#2146 · 2024-11-24 · Toine Heat Reuse] [#2188 · 2024-11-29 · Toine Heat Reuse] |
| Dec 2024 | 88-chip S19 for a water heater build | $275 | [#2982 · 2024-12-29 · Karl] |
| Dec 2024 | Hashrate House immersion system (tank, PDU, bphx, hoses, cooler) incl. shipping | $2700 total; tank $1700; cooler $1000; coolant $160 per 20L | [#3007 · 2024-12-30 · Dane O] [#2411 · 2024-12-02 · Dane O] |
| Jan 2025 | CADDY 2 immersion product | $8k to $25k for 320 to 800 TH/s | [#3067 · 2025-01-03 · Colin Sullivan] |
| Mar 2025 | Used S19 95TH (3250W), 60 day warranty | $300 USD | [#4671 · 2025-03-22 · Toine Heat Reuse] |
| Mar 2025 | HeatCore 5kW AIO hydro unit | 'like $6000' | [#4807 · 2025-03-23 · Cody Harris] |
| Mar 2025 | High-end hydro/immersion miner | '8k per miner' | [#4851 · 2025-03-24 · Dane O] |
| Apr 2025 | Whatsminer M64, next batch | 'around $14/T' | [#5271 · 2025-04-02 · Dev 🇳🇿] |
| Apr 2025 | Surplus APW12 PSUs, control boards, hashboards | ~50% off online prices | [#5522 · 2025-04-15 · Will Ramirez] [#5535 · 2025-04-15 · Will Ramirez] |
| May 2025 | Whatsminer M64 | around 2.5 k delivered (tariff-dependent) | [#6322 · 2025-05-31 · Pat Kelly \| Fog Hashing - Director of Sales, Global] |
| May 2025 | Boiler units at Bitcoin 2025 | one at $9,000; the Heat Core one $1500 with radiator | [#6316 · 2025-05-31 · Elijah Sanders] |
| Sep 2025 | Whatsminer M64 | $2700 delivered | [#7367 · 2025-09-21 · Elijah Sanders] |
| Nov 2025 | Whatsminer M64S 220T, 18j/th | $2680 + shipping from HK | [#7922 · 2025-11-24 · Elijah Sanders] |
| Mar 2026 | Whatsminer M74 275T, group buy (MOQ 50) | $14.5/T | [#9624 · 2026-03-12 · Travis Bitkle] [#9625 · 2026-03-12 · Travis Bitkle] |
| Mar 2026 | Whatsminer M74 275T, single phase (MOQ 50pcs) | USD10.7/T, then USD10.4/T | [#9648 · 2026-03-13 · Dev 🇳🇿] [#9682 · 2026-03-16 · Dev 🇳🇿] |
| Mar 2026 | Whatsminer M6DS++ / M7D / M7DS | $6.5/T / $8.7/T / $10/T | [#9623 · 2026-03-12 · Joe C] |
| Mar 2026 | Used S19 jPro (Denver area) | $15, 'a buy no matter what hashprice is' | [#9738 · 2026-03-26 · Travis Bitkle] [#9743 · 2026-03-26 · Travis Bitkle] |
| Mar 2026 | WhatsMiner M50S | cheap, 23-24 J/TH | [#9685 · 2026-03-16 · Dan Sokil] |

Earlier critiques of vendor pricing included charging over $1k for an S9 with a fiat heater bolted on [#548 · 2024-08-10 · Toine Heat Reuse]. Engineered immersion fluid barrels used to cost $8/Liter, while canola is $8/gal versus $20-25/gal for mineral oil [#8941 · 2026-01-29 · Elijah Sanders] [#9820 · 2026-04-08 · Karl]. Product details are in [Hashrate Heating Products and Installs](../industry/hashrate-heating-products-and-installs.md).

## Valuing heat reuse and business models

### Ways to value the heat

- **Heaters with mini lotto tickets.** The heat reward is constant while the sats are intermittent [#983 · 2024-09-04 · Tyler Stevens]. One rationale for solo-mining heaters is 'Im already paying for the heat', so pointing that hashrate at the global lottery makes sense [#7308 · 2025-09-08 · Trevor Bello].
- **Sellable products.** Mining to produce something you can sell beats mining for space heat alone [#1174 · 2024-09-17 · Karl]. The HS05 economics framing is that the electric cost goes up while the heating fuel cost goes down [#7098 · 2025-08-18 · Heatpunk Forum].
- **Space trade.** Miners need little floor area. Travis described it as '400 sq ft of space to heat like 10,000 sq ft' [#4433 · 2025-03-06 · Travis Bitkle] [#4434 · 2025-03-06 · Travis Bitkle].
- **Taxonomy.** Tyler separates 'Bitcoin Mining Heat Recapture', where mines sell their heat (MARA, Finland-style), from 'Electric Heating Bitcoin Recapture', which covers hashrate-powered appliances in homes and businesses [#5013 · 2025-03-28 · Tyler Stevens] [#5167 · 2025-03-30 · Tyler Stevens]. Others questioned the line, noting for example that Softwarm would count as recapture. A counter-argument is that the residential side will decentralize while mine-scale recapture centralizes [#5041 · 2025-03-28 · Cody Harris] [#5042 · 2025-03-28 · Patrick Patel] [#5047 · 2025-03-28 · Tyler Stevens].
- **Industrial plants are a hard sell.** Low-grade industrial heat (steam below 150C) is cheap and usually already goes to economizers, so niches without excess heat are better targets [#769 · 2024-08-23 · Harrison The Space]. Heat reuse is harder at mega-miner scale because sites are rural and nobody nearby wants the heat [#767 · 2024-08-23 · Tyler Stevens].

### Business models

- **Free lease plus revenue split.** One firm leases machines to customers for free and takes a split of the revenue, because 'even $1000 machine is expensive and a hard sell' [#3551 · 2025-01-16 · The schnauze].
- **Debt-financed industrial heat (Ecobit).** Ecobit debt-finances miners for warehouse heating. The client gets the heat and Ecobit gets the mined BTC minus the heating expense, which leaves a stock of fully depreciated hardware to sell. Power in Montreal is 6.8 cents / kWh (CAD), and the latest install was reportedly 50 S21s [#2194 · 2024-11-29 · Toine Heat Reuse] [#2195 · 2024-11-29 · Toine Heat Reuse] [#2198 · 2024-11-29 · Toine Heat Reuse].
- **Revenue share for pools.** One idea is a trailer-mounted C2 system for pool owners that splits heating costs 50/50 [#4602 · 2025-03-19 · Dev 🇳🇿].
- **Hosting rebate.** In this model the host keeps none of the hashrate but gets a '$50 monthly rebate' for buying the heater [#7238 · 2025-09-02 · Elijah Sanders].
- **Peer-to-peer hosting marketplace.** A proposed marketplace would connect miners who need no more heat with homes, businesses and nonprofits that do, like Uber or Airbnb 'but with your electricity' [#7240 · 2025-09-02 · Michael | Bitstorian].
- **Hot-water-tank leasing.** The case for it is a universal need plus an existing leasing ecosystem, with reliability and capex as the open problems [#4781 · 2025-03-23 · The schnauze] [#5175 · 2025-03-30 · The schnauze]. Critics say it 'breaks too much' (service load) and point out that many homes use gas or, in Asia, don't heat water [#4793 · 2025-03-23 · Karl] [#5176 · 2025-03-30 · Dev 🇳🇿].
- **Commercial sites.** These work well because of tax write-offs and the ability to run all the time. One produce-industry operator saw far more interest in heating warehouses than greenhouses [#3532 · 2025-01-16 · The schnauze] [#3580 · 2025-01-16 · The schnauze].
- **A weak alternative: flare gas.** A Michigan flare gas offer (June 2025) required S21 or better on a 50/50 split, with $0.00 electricity, a $2,000 Monthly maintenance fee, a $50,000 commitment fee and a 5-Year contract. The poster found it less compelling than heat reuse [#6474 · 2025-06-15 · Shawn Flowers].

### Adoption friction

- **Onboarding is the bottleneck.** Customer adoption is often held up by Bitcoin onboarding: explaining mining, setting up wallets, managing BTC and cashing out [#2507 · 2024-12-05 · The schnauze] [#2510 · 2024-12-05 · The schnauze].
- **Trust and trades.** Heating means survival in the north, so people trust established HVAC brands, and pool heating is a lower-risk entry point [#584 · 2024-08-10 · Bob]. Tradespeople also need education to service heaters [#594 · 2024-08-10 · Tyler Stevens].
- **Rural oil-heat homes are hard to convert.** Rural Ontario homes on dyed-diesel furnaces benefit most but resist the most [#582 · 2024-08-10 · Toine Heat Reuse].
- **Common pushback** in public comments is heat pumps, 'Bitcoin isnt real', profitability skepticism and GPUs [#7218 · 2025-08-28 · Cade].

## Tax, accounting and insurance

Nothing here is professional advice.

- **Bookkeeping.** Track the $ cost of electricity used each month and the $ value of sats when they hit the wallet [#4126 · 2025-02-19 · R D]. Income is the USD value of mined bitcoin at the time of mining plus any USD heat sales. Expenses include electricity and depreciated equipment, and profit is income minus expenses [#4127 · 2025-02-19 · Patrick Patel].
- **Depreciation.** Moving aging miners into heat recapture lets you write off depreciation and keep the BTC mined over the unit's life [#3328 · 2025-01-13 · The schnauze]. Even for LLCs, properly metered power is an expense, and '100% depreciation' helps miner investments [#7095 · 2025-08-17 · Heatpunk Forum]. Cade posted on tax advantages for sole proprietors [#6761 · 2025-07-08 · Heatpunk Forum]. In NZ, computers depreciate at 50% yearly [#4601 · 2025-03-19 · Dev 🇳🇿].
- **Banking and insurance.** A Canadian heat-reuse firm reported being debanked and refused insurance for being crypto-affiliated, even though business was booming [#3060 · 2025-01-03 · The schnauze]. Commercial clients 'pretty much all ask about insurability' because miners lack UL/CE certification [#7101 · 2025-08-18 · Tyler Stevens]. Code and listing workarounds are covered in [Hashrate Heating Products and Installs](../industry/hashrate-heating-products-and-installs.md).

## Market size (TAM) data points

These figures are as quoted in the chat, and several are unsourced.

- About 25% of global energy consumption goes to comfort heating (unsourced estimate) [#990 · 2024-09-04 · Tyler Stevens].
- Converting 1% of comfort heating to hashrate heat could push network hashrate past 2 ZH. A reviewer computed 1594EH/s added and questioned the 176TWh source, using a gut-check fleet average of ~30 J/TH [#1460 · 2024-10-10 · Tyler Stevens] [#1464 · 2024-10-10 · Nicolas Drouin-Audet] [#1466 · 2024-10-10 · Tyler Stevens].
- Converting all French households with electric heaters would match the then-current Bitcoin hashrate [#1468 · 2024-10-11 · Jim ⚡️].
- Residential electric space heating is about 600 TWh per year, roughly 3x all of bitcoin mining [#3537 · 2025-01-16 · Alex HeatBit].
- As of 2020 data, 25% of US houses are all-electric [#2469 · 2024-12-04 · Tyler Stevens].
- Monthly heating bills:
  - a 2,500 sq ft house in Montrose, CO spends $900/mo on electric baseboard heat [#2485 · 2024-12-05 · Zinjinlao]
  - homes about 45 min north of NYC pay $700/mo for heating oil with a forced-air furnace [#2967 · 2024-12-29 · Tyler Stevens] [#2971 · 2024-12-29 · Tyler Stevens]
  - a greenhouse at 10,000 ft in Idaho Springs, CO with no natural gas spends in excess of $5000/mo on propane [#785 · 2024-08-23 · Tyler Stevens]
  - Australian nursery and hydroponic greenhouse owners pay 'hundreds of thousands' for gas and LPG water heating [#7839 · 2025-11-22 · Cosmo]
- Most of the US Northeast lacks natural gas, heats with oil, and doesn't have cheap electricity. Massachusetts voted for a natural gas ban in all new construction [#2973 · 2024-12-29 · Nicolas Drouin-Audet] [#2974 · 2024-12-29 · Nicolas Drouin-Audet]. Heating-fuel maps may show only the primary heat source, and many oil systems are secondary to heat pumps [#2886 · 2024-12-23 · The schnauze].
- Good fits include places with cold nights or winters where homes lack central heat and run space heaters half the year [#6358 · 2025-06-02 · Michael | Bitstorian]. Spas are another, because they typically use a ceramic heating element rather than a heat pump or gas [#6007 · 2025-05-14 · Dev 🇳🇿] [#6008 · 2025-05-14 · Dev 🇳🇿].
- **Off-grid example (El Salvador, July 2026).** Electricity is 28c/kWh all-in and a rural grid connection is $2000/pole per 50m. The plan pairs 17kWp of solar and a 12kW inverter with a foghashing C2 running old miners during the solar day, targeting hospitality venues that use 5000W electric shower heads [#10345 · 2026-07-21 · Jake #️⃣ Hashpower Academy 🎓].

## Electricity rate data points (dated)

| As of | Location / context | Rate | Anchor |
|---|---|---|---|
| Aug 2024 | Cheese-plant micro-mine demand response (summer / winter) | $0.071 / $0.061 per kWh | [#84 · 2024-08-02 · Travis Bitkle] |
| Aug 2024 | Petrochemical boiler-water preheat (CAD) | 0,04$/kwh | [#764 · 2024-08-23 · Nicolas Drouin-Audet] |
| Aug 2024 | Home with natural gas: peak electric bill vs summer | $600/mo vs about $250 | [#581 · 2024-08-10 · Jonathan Y] |
| Sep 2024 | Idaho, most domestic and commercial; 3-phase | 5-6 cents; 4.2 | [#1196 · 2024-09-18 · Cade] |
| Nov 2024 | Montreal (CAD) | 6.8 cents / kWh | [#2198 · 2024-11-29 · Toine Heat Reuse] |
| Jan 2025 | Pennsylvania residential | 7.65 cents per kWh | [#3265 · 2025-01-12 · Zackery Miller] |
| Jan 2025 | Off-peak thermal-storage plan | $0.045/kWh | [#3648 · 2025-01-18 · Travis Bitkle] |
| Feb 2025 | Denmark (USD terms) | 0,35/kwh | [#3976 · 2025-02-12 · Jake⚡️] |
| Mar 2025 | New Zealand | $0.105 USD/kWh | [#4852 · 2025-03-24 · Dev 🇳🇿] |
| Jan 2026 | Business with gas heat | $0.20/kWh | [#8533 · 2026-01-03 · Jon C] |
| Jul 2026 | El Salvador, all-in | 28c/kWh | [#10345 · 2026-07-21 · Jake #️⃣ Hashpower Academy 🎓] |

## See Also

- [Open Mining Economics](open-mining-economics.md)
- [Pool Choice for Heat Miners](../pools/pool-choice-for-heat-miners.md)
- [Pool Payout Schemes](../pools/pool-payout-schemes.md)
- [Air-Cooled Hashrate Heating](../hardware/air-cooled-hashrate-heating.md)
- [Hydronic Heat Reuse](../hardware/hydronic-heat-reuse.md)
- [Immersion Heat Reuse](../hardware/immersion-heat-reuse.md)
- [Whatsminer M64 Hydro Heaters](../hardware/whatsminer-m64-hydro-heaters.md)
- [Heater Electrical and 120V Builds](../hardware/heater-electrical-and-120v-builds.md)
- [ASIC Thermals and Heat Reuse](../hardware/asic-thermals-and-heat-reuse.md)
- [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md)
- [Home Assistant Heater Control](../mining-software/home-assistant-heater-control.md)
- [Hashrate Heating Products and Installs](../industry/hashrate-heating-products-and-installs.md)
- [On-Demand Hashrate](../hashrate-market/on-demand-hashrate.md)
- [Heatpunks Community Timeline](../history/heatpunks-community-timeline.md)
