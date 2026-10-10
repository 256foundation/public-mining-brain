# Hydronic Heat Reuse

> Sources: Hashrate Heatpunks Telegram group, 2024-08-02 → 2026-10-08
> Raw: [Hashrate Heatpunks Telegram signal digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

Hydronic heat reuse moves ASIC heat into water (or a water/glycol mix) and from there into the loads a building already has: boiler loops, radiant floors, radiators, domestic hot water (DHW), pools, hot tubs and snow-melt slabs. Heat comes off the chips in one of two ways. Hydro miners such as the Whatsminer M64, Antminer hydro units, or air-cooled S19s converted with Cryobyte or Zeus waterblocks have water running straight through their cold plates. Immersion tanks put the heat into oil, which then gives it up to water across a plate heat exchanger. Between 2024 and 2026 the Hashrate Heatpunks group settled on a few rules. Keep the miner on its own loop and isolate it from building water with a heat exchanger. Control the temperature by changing how much heat you pull from the loop, not how hard the miner runs. Size the exchangers and emitters for the small temperature differences miners produce. Treat water chemistry and dissimilar metals as a design input. Members still disagree on whether every system needs an outdoor heat dump. This article covers the water side. For immersion fluids and tanks see [Immersion Heat Reuse](immersion-heat-reuse.md), and for the M64-based boilers see [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md).

## Rules of thumb

- **A miner is essentially a 1:1 electric heater.** All miners are "very close to 100%" efficient as heaters, minus fans and LEDs. The real losses are BTUs that leak out through the case and piping before they reach the load [#6772 · 2025-07-10 · Travis Bitkle] [#6770 · 2025-07-09 · Travis Bitkle] [#6938 · 2025-08-06 · Patrick Patel]. One counterpoint: a peer-reviewed study of water heating with an S19 Pro Hydro found that only about ~90% of the electricity became useful heat [#10339 · 2026-07-21 · Heatpunk Forum].
- **Flow is your main tuning knob.** For a liquid-cooled miner the energy balance is m*cp*∆T_water = h*A*∆T_chip. At max wattage the chip temperature is fixed, so water flow is the only variable you can easily change [#685 · 2024-08-19 · Tyler Stevens]. The same balance holds for air and immersion, where it is easier to add heat-sink area than it is on a waterblock [#689 · 2024-08-19 · Tyler Stevens].
- **Vary the heat you extract, not the miner.** Cade's maxim is "Dont vary the computer for heat demand. Vary the way you pull the heat from the loop" [#3559 · 2025-01-16 · Cade] [#3563 · 2025-01-16 · Cade]. When the loop saturates, Braiins autotuning turns the miner down on its own because it can no longer dump heat [#3561 · 2025-01-16 · Cade] [#3567 · 2025-01-16 · Cade].
- **Isolate the miner loop.** Building heating water is "full of dirt", and heating pipes are not fully oxygen-proof. A heat exchanger between the miner loop and the building loop keeps both problems out of the miner. Running separate pumps on each side also lets you set the temperature each side reaches [#6842 · 2025-07-25 · Christian Naef] [#6845 · 2025-07-26 · Christian Naef]. Tyler Stevens describes the HX plus two pumps as "Two knobs to turn" [#6864 · 2025-07-29 · Tyler Stevens].
- **Low delta-T means big heat exchangers.** The closer the hot and cold sides get, the more heat-transfer area you need. A high miner outlet temperature still needs its return cooled, by a pool or a dry cooler, before it re-enters the miner [#669 · 2024-08-19 · Dane O]. Oversizing a liquid-to-liquid HX does not add much cost [#712 · 2024-08-21 · Harrison The Space]. Instead of adding a heat dump, you can enlarge the HX to narrow the delta-T [#5119 · 2025-03-29 · Cody Harris].
- **Size for the coldest days, but don't oversize the mining.** In one radiant-floor home at sustained -25, the floor delivery system was the limit, not the miners [#429 · 2024-08-05 · Cody Harris]. Lower fluid temperatures mean limited capacity through an existing emitter [#430 · 2024-08-05 · Bob].
- **Plan for hardware to be swapped.** A water heater lasts ~20 years and a hashboard won't, so hydronic loops should be modular and upgradable [#1028 · 2024-09-04 · Jonathan Y] [#1030 · 2024-09-04 · Jonathan Y].
- **Insulate everything.** PEX and pipe insulation are cheap, so the miner does not have to sit next to the load. Insulate the tubing, HX and reservoir, or the room gets the heat instead [#5118 · 2025-03-29 · Josh] [#4895 · 2025-03-27 · Josh]. Uninsulated PEX plus radiation from an M64 can overheat a basement; one proposed fix is insulating the joists to push the heat upstairs [#7603 · 2025-11-07 · Travis Bitkle] [#7604 · 2025-11-07 · Tyler Stevens].

> **Status: Disputed**
> Does every system need a heat dump? Cade says "every system ALWAYS needs a heat dump", for example a greenhouse roof exhaust fan. His systems run continuously, though some were turned off or way down in summer to stay profitable [#3565 · 2025-01-16 · Cade] [#3572 · 2025-01-16 · Cade] [#3573 · 2025-01-16 · Cade]. Cody Harris counters that dumping heat only works with "ultra juicy .04c power", and his own system dumps no heat [#3564 · 2025-01-16 · Cody Harris] [#3568 · 2025-01-16 · Cody Harris] [#3574 · 2025-01-16 · Cody Harris]. He later called a heat dump a "non starter" in most areas [#5119 · 2025-03-29 · Cody Harris]. Brett Rowan notes that dumping makes the system less efficient [#3550 · 2025-01-16 · Brett Rowan]. Dane O sees a dump as useful in some localities but wants it optional and bypassable [#6324 · 2025-05-31 · Dane O]. Best assessment: a dump earns its keep where power is cheap, or as a summer outlet for solar or for an always-on user, which Cade calls types 3 and 4 [#5066 · 2025-03-28 · Cade]. Heat-only intermittent installs can skip it if they modulate the miner instead.

## Loop topologies

### Boiler loop with plate HX and thermostatic dump

The most-cited pattern puts the miner, or an immersion tank, on a boiler loop with a brazed plate heat exchanger (BPHE). An outdoor dry cooler acts as the heat dump, and its fan runs on a thermostat that holds the fluid up to 57c. When the water needs heat, a recirculation pump pushes it through the HX [#3558 · 2025-01-16 · Cade]. On a Fog Hashing C1 the flow is Tank > plate HX > external dry cooler > Tank [#3743 · 2025-01-22 · Cade]. Cade picked the 57 (c) setpoint because it keeps machine efficiency and water temperature both acceptable [#3754 · 2025-01-22 · Cade]. In field data from 2 underclocked S19s, 54 inlet and 65 outlet gave maximum heat [#3752 · 2025-01-22 · Dane O].

### Primary/secondary loops (avoiding temperature shock)

Travis Bitkle's hydro-miner water heater hit two failure modes, documented in [#6408 · 2025-06-07 · Travis Bitkle] and [#6409 · 2025-06-07 · Travis Bitkle]:

1. When the aquastat opened the zone valves, a slug of 115F water dumped back into a miner holding 170F water and threw an error code.
2. The zone valves opened too slowly, so the pump briefly dead-headed. Flow stopped and chip temperatures rose, then 50F colder water rushed in and made the swing worse.

The fix was a primary/secondary loop [#6410 · 2025-06-07 · Travis Bitkle]. The water heater draws from the primary hot supply, and the aquastat triggers a relay for the secondary pump. The water-heater return dumps back into the hot line, so it mixes through the loop and the radiator with "No temp shock to the miner". With no call for heat, the primary loop pumps on past to a garage radiator. The miner now runs full time, and the water heater gets full-temperature water for the fastest recharge [#6412 · 2025-06-07 · Travis Bitkle]. He uses two pumps to keep DHW at 120°F rather than 170°F without an HX between zones [#6869 · 2025-07-29 · Travis Bitkle]. Hydro miners can also shut down when the inlet-to-outlet delta gets too large [#6740 · 2025-07-07 · Pat Kelly | Fog Hashing - Director of Sales, Global].

### Mixing and modulating

- Radiant floors need a mixing valve, because miner outlet heat is too hot for floor boards [#6866 · 2025-07-29 · Tyler Stevens].
- A mixing valve didn't behave as needed on a heat exchanger, so Dane O looked for a digitally controlled proportional valve (0-100%) that could target an outlet water temperature [#1062 · 2024-09-04 · Dane O] [#1068 · 2024-09-04 · Dane O].
- You can attach a dry cooler on the miner side and switch between loops with a valve [#6843 · 2025-07-25 · Christian Naef].
- For radiant zone control, Softwarm recommended Taco controllers, while Dylan Seib leans on Home Assistant [#6380 · 2025-06-04 · Heatpunk Forum].

### Cascades (hottest load first)

Jonathan Y proposed this order for an oil loop: Miner > Hot Water heater > Furnace > Fish Tank > Miner [#1007 · 2024-09-04 · Jonathan Y] [#1017 · 2024-09-04 · Jonathan Y]. Dane O countered that the water-to-air furnace exchanger belongs last, as the "final dry cooler", because air heating still works with only slightly warm fluid [#1011 · 2024-09-04 · Dane O]. By late 2025 Jonathan's plan had become Miner > House heater > Hot water heater > Fish tank > outdoor dry cooler > back to tank [#8451 · 2025-12-26 · Jonathan Y]. A Finnish plan sends a hydro miner's heat first to DHW, then a radiator loop, then the geothermal heat pump's intake liquid, with any excess going into the geothermal wells for silent rejection and possible seasonal storage [#6516 · 2025-06-23 · Jarno].

### Water-to-air (ducts and plenums)

Wrapping PEX around a duct won't conduct heat well. Put a water-to-air heat exchanger inside the duct instead; an old car heater core works [#4997 · 2025-03-28 · Dylan Seib] [#4998 · 2025-03-28 · PizzAndy] [#5007 · 2025-03-28 · Ian] [#5008 · 2025-03-28 · Travis Bitkle] [#5016 · 2025-03-28 · Jonathan Y]. One design estimate: forcing 1000cfm through a plenum HX with 176F water and 60F inlet air gives outlet air around 128F. The water then returns at 120F–130, which a sidearm HX could use to bring DHW to about 120 [#7390 · 2025-10-06 · Britton]. Field reports of M64 plenum installs are in [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md#field-installs).

## Domestic hot water

- **Why DHW.** Karl argues hot water is the best way to bring mining into anyone's home because everyone has it and uses it every day [#2978 · 2024-12-29 · Karl]. Dane O adds that it is needed year-round in any climate [#3000 · 2024-12-29 · Dane O]. The catch is that one M64 is a lot of power for a water heater alone and will cycle on and off heavily. It works better tied into forced air or a radiant slab as well [#8370 · 2025-12-22 · Dane O].
- **Retrofit, don't replace.** Instead of buying a new water heater, get a tank and build a recirculation loop [#6629 · 2025-06-27 · Karl]. Fitting compute directly inside a tank is too hard, so retrofits likely need a two-stage loop [#489 · 2024-08-08 · Harrison The Space]. In one working build, cold input enters at the top by the pressure relief valve, and recirculation leaves the bottom through a BPHX. Dane O advised adding a filter between the heater drain and the pump/HX [#3000 · 2024-12-29 · Dane O] [#3001 · 2024-12-29 · Karl].
- **Preheat tanks.** An old water-heater tank can serve as a "pre heat tank" at ~105F that feeds the regular water heater [#2980 · 2024-12-29 · Cody Harris]. R D's system pre-warms the boiler's tap water in winter [#2663 · 2024-12-09 · R D]. Cody Harris runs a miner two hours a day to preheat (~110F) 45gal of water that feeds an electric water heater [#4789 · 2025-03-23 · Cody Harris].
- **Hitting 140F is hard without extra cooling.** Josh's S19 jpro with Cryobyte waterblocks went from 110 to 130 easily, but above that the differential became too small and the boards overheated. A radiator or heat dump, or the miner's own fans, was needed to reach 140f in reasonable time [#5118 · 2025-03-29 · Josh]. Keeping fans to exhaust heat lets a water-heating miner keep running after the water reaches its target [#8259 · 2025-12-11 · Karl].
- **Travis's water heater.** He powers the miner off once return water reaches 120F, and tap water reached "like 136F" [#6074 · 2025-05-19 · Travis Bitkle]. On first fill the tank heated so fast that he judged a second zone radiator necessary [#6051 · 2025-05-18 · Travis Bitkle]. In low power mode the system settled at a 35°F ∆T [#6144 · 2025-05-25 · Travis Bitkle].
- **Scale and sediment.** Karl reports that miner-heated water doesn't build scale the way heating elements do, because it heats "slowly but continuously". For hard water, put a filter in the loop so the HX doesn't clog [#6643 · 2025-06-27 · Karl]. Drain the water heater at least once a year, because calcium and sediment ruin any heat-reuse integration [#1200 · 2024-09-18 · Dane O].
- **Glycol and drinking water.** Never use ethylene glycol (engine coolant) in a loop that exchanges heat with domestic water. An HX failure would put toxic chemicals in the drinking water. Use propylene glycol [#4863 · 2025-03-24 · Dane O].
- **Retrofit products** existed by 2026. Dane O's Aqueon adds a custom controller and 2 heat exchangers to an existing water heater, with DHW as primary and furnace, radiant floor or heat dump as secondary [#10283 · 2026-06-24 · Dane O]. Superheat built firmware that sets clock speed from water temperature for closed water-heater tanks [#8609 · 2026-01-08 · Tyler Stevens] [#8611 · 2026-01-08 · Andrew Geng]. See [Hashrate Heating Products and Installs](../industry/hashrate-heating-products-and-installs.md).

## Radiant floors, slabs and snow melt

- **Inlet temperatures.** Most radiant floor systems are rated for around a 50-60c inlet and a 40c-ish return, which suits immersion operating temperatures. Many can run lower, at about 95f inlets [#1432 · 2024-10-08 · Dane O]. An early field report saw ~112° oil at 70C chip temp yield about ~105° glycol inlet temp [#167 · 2024-08-02 · Cody Harris].
- **Emitter sizing is the bottleneck.** A system designed around an electric boiler on 1/2 pex at about 160f cannot heat the house with a 120 degree ASIC. The fix is to oversize the radiant floor, using 5/8 pex at close intervals for more BTU per square foot [#469 · 2024-08-08 · Cade] [#470 · 2024-08-08 · Cade] [#471 · 2024-08-08 · Cade]. For cold starts and extreme cold, one plan adds a boiler "turbo button" that lets the miners run hotter temporarily [#431 · 2024-08-05 · Cody Harris]. The nextgenboiler.com radiant design guide was shared as a sizing resource [#475 · 2024-08-08 · Nicolas Drouin-Audet].
- **Rejection capacity.** 500 feet of 1/2-inch and 1200 feet of 3/8-inch radiant tubing together reject more than 7kw [#4784 · 2025-03-23 · Cody Harris]. Thick radiant floors also work as thermal mass for $.06 off-peak power [#3651 · 2025-01-18 · Cody Harris].
- **Sizing data points.** 13kW heats 3000sqft of hydronic floor (a 1300Th customer), with 2 outdoor air-coolers allowing 24/7 operation, summer pool heating, and the gas boiler kept as backup [#385 · 2024-08-04 · Nicolas Drouin-Audet] [#388 · 2024-08-04 · Nicolas Drouin-Audet]. Another plan set a power limit around 2700 watts based on the previous year's coldest month [#380 · 2024-08-04 · Tyler Stevens]. In a larger install, 6x S21 heat a 6000sqft floor, a pool and a snow-melting slab [#476 · 2024-08-08 · Nicolas Drouin-Audet].
- **Install gotchas.** One customer did an install with 1-inch water-softener lines from Home Depot at -20 outside, and one apartment ran "like 85 degrees" [#4612 · 2025-03-19 · Cade] [#4613 · 2025-03-19 · Cade] [#4614 · 2025-03-19 · Cade]. WarmBoard over-slab panels work, but installers can easily nail through PEX that isn't set in concrete [#8361 · 2025-12-22 · Mike Clear]. Exergy's radiant install at The Space took longer than expected and ended up needing professional plumbers [#6973 · 2025-08-11 · Heatpunk Forum].
- **Snow melt and slabs.** Snow melt only needs the ground just above freezing, and one immersion-fed install runs in Juneau, Alaska [#1432 · 2024-10-08 · Dane O]. Snow-melt lines use antifreeze [#1449 · 2024-10-10 · Jonathan Y], and a hydronic loop under a sidewalk works as a summer heat dump [#1377 · 2024-10-08 · Mark | @satstackingpleb]. A hydro "Antminer S19 Pro+ 198th" heats a concrete slab outside the cheese mine and "does melt snow nicely" [#7017 · 2025-08-12 · Travis Bitkle] [#7021 · 2025-08-12 · Travis Bitkle]. A planned immersion-fed slab is approx 8-10 inches thick, with PEX near the top to heat, insulation board in the middle, and PEX below to cool the fluid further. The glycol loop replaces the dry cooler, and in summer the box switches to an inground pool [#7349 · 2025-09-11 · Brian EcobitQC] [#7355 · 2025-09-11 · Brian EcobitQC]. State regulations cover snow melt but not concrete slabs used as heat exchangers for liquid-cooled servers [#5567 · 2025-04-16 · Travis Bitkle].

## Pools, spas and hot tubs

- **Material choice.** Salt pools need titanium heat exchangers for longevity. Plain chlorinated pools can get away with 316SS [#7578 · 2025-11-07 · Dane O]. No cupro plate-frame HX was found for salt water [#782 · 2024-08-23 · Nicolas Drouin-Audet], but cupronickel works well for salt-water immersion applications. Ti was noted as not great at heat transfer [#4640 · 2025-03-20 · Dane O]. Dane O also went looking for a fully stainless BPHX in the US as a Ti alternative for domestic water [#5814 · 2025-04-25 · Dane O].
- **Oversize about 2x.** HX ratings assume a 140f+ delta between the heating medium and the pool, while immersion gives at best a 50-60f delta. Roughly double whatever you calculate [#7582 · 2025-11-07 · Dane O]. A 600k BTU titanium shell-and-tube unit was pricey, but doubling it to 1.2MM BTUs would have added only another 25% [#714 · 2024-08-21 · Gerald Glickman].
- **Placement.** Install the HX downstream of the pool filter and plumb it so you can backwash through it. Backwashing once a year is good practice [#7610 · 2025-11-08 · Nicolas Drouin-Audet] [#7611 · 2025-11-08 · Nicolas Drouin-Audet].
- **A working pool-heater plate-frame build** used a 3/4” inlet on the oil side and 1” on the water side, with ~70lpm water flow and 45lpm oil flow [#789 · 2024-08-23 · Nicolas Drouin-Audet]. It ran 30 plates for 2 miners, and the concern with fewer plates is pressure loss rather than cooling [#790 · 2024-08-23 · Nicolas Drouin-Audet] [#800 · 2024-08-23 · Nicolas Drouin-Audet]. Its connections are 1-1/2” to match pool equipment, with a reducer at the exchanger [#798 · 2024-08-23 · Nicolas Drouin-Audet].
- **Hot tubs are natural sinks.** At 104 (F), the upper comfort limit, a hot tub matches the 40c inlet most immersion systems want [#3586 · 2025-01-16 · Dane O]. Spas also usually heat with ceramic elements rather than heat pumps or gas, which makes them easy to beat [#6007 · 2025-05-14 · Dev 🇳🇿] [#6008 · 2025-05-14 · Dev 🇳🇿]. One hashrate-heated cedar tub runs at "103 f. 200 TH" [#9260 · 2026-02-21 · Tyler Stevens]. Watch chlorine with cedar; copper-ionization sanitation paired with custom cupronickel HXs cuts chemical demand [#9262 · 2026-02-21 · Gerald Glickman] [#9263 · 2026-02-21 · Dane O].

> **Status: Disputed**
> Plate vs shell-and-tube for pools. Nicolas Drouin-Audet says plate HX are "Much more efficient volume wise", while shell-and-tube needs to be much bigger for the same surface [#7613 · 2025-11-08 · Nicolas Drouin-Audet]. Ian says shell-and-tube is better for particulate-laden water like pools [#7639 · 2025-11-10 · Ian], and Dev notes it has long been used for pools and spas [#7636 · 2025-11-09 · Dev 🇳🇿]. Nicolas himself prefers shell-and-tube for scaling resistance and robustness, but uses plate-frame units in all his systems because of size, adding backwash capability plus a cheap extra strainer [#7650 · 2025-11-13 · Nicolas Drouin-Audet]. Best assessment as of 2026-10-09: use a plate unit where space is tight, protected by a strainer and backwash plumbing, and shell-and-tube where water quality or robustness dominates.

## Heat exchangers: sizing and sourcing

- **Calculator.** SWEP SSP is a free BPHE calculator. The downloadable version supports custom fluids, multi-calculations, pressure drops and plate dimensional data [#695 · 2024-08-19 · Bob] [#696 · 2024-08-19 · Bob] [#702 · 2024-08-19 · Bob]. An SSP run for a single M64, with margin (75C instead of 80C), gave around 1/2 gal/min at around 71C [#692 · 2024-08-19 · Bob].
- **Long-life builds.** A custom nickel-brazed 316 SS plate HX was built for an M64 integration so it lasts as long as a boiler or water heater [#8383 · 2025-12-22 · Dane O].
- **Budget builds.** Vevor heat exchangers cost about $40, versus about $200 for an Amazon equivalent [#8222 · 2025-12-09 · Elijah Sanders] [#8223 · 2025-12-09 · Travis Bitkle]. Karl upgraded his water heater to a bigger, cheaper, lower-quality HX to speed up heat recovery [#4406 · 2025-03-04 · Karl].
- **Tank-in-tank.** In a double-wall tank, the whole outside of the inner tank sits in a boiler water jacket; one such product has a built-in aquastat at 200° boiler temp [#5747 · 2025-04-24 · Travis Bitkle] [#5758 · 2025-04-24 · Dane O].
- **Aquariums.** Aluminum in tank water built up deposits, so the choices are stainless or titanium HXs [#8395 · 2025-12-22 · Jonathan Y] [#8397 · 2025-12-22 · Jonathan Y] [#8405 · 2025-12-22 · Jonathan Y]. Aluminum inside an aquarium corroded seriously [#4638 · 2025-03-20 · Jonathan Y].

## Dry coolers, radiators and heat dumps

- **EC fan curve.** One dry cooler's EC fan measured 25% speed 30dba @20w, 50% 40dba @50w, 75% 54dba @155w and 100% 60dba @343w. A vastly oversized dry cooler rarely runs above 50% [#644 · 2024-08-11 · Dane O]. If you're not doing the math, oversize it; non-EC or non-industrial fans bring diminishing returns [#7966 · 2025-11-25 · Dane O].
- **Fan staging.** On at 30 and off at 50c gives 20 steps (5% increases). On at 45 and off at 50 gives 5 steps (20% increases) [#3748 · 2025-01-22 · Dane O].
- **Off-the-shelf units.** Stock dry coolers "don't work very well" for immersion because they are built for 200-300l/min flows [#5538 · 2025-04-15 · Dane O].
- **Radiators.** Builder prices as of April 2025: a ~$600 radiator rated 6 KW, or 12 KW units made from ASIC fans for about $500 [#5501 · 2025-04-14 · Elijah Sanders]. A DCX 15kw radiator was rejected because its copper coils pose a galvanic risk with aluminum waterblocks. Searching for "oil radiator" turns up units that are generally aluminium fin [#5505 · 2025-04-14 · Ian] [#5509 · 2025-04-14 · Ian] [#5516 · 2025-04-14 · Dev 🇳🇿]. A car radiator also works as a dry cooler, ideally with a cheap HX in between [#7954 · 2025-11-25 · Elijah Sanders] [#7957 · 2025-11-25 · Elijah Sanders].
- **Filtering the intake.** Put a large furnace filter in front of an indoor dry cooler so basement dirt doesn't clog the HX [#7899 · 2025-11-23 · Dane O].
- **Other places for surplus BTUs** once the water heater is hot: an outdoor drycooler, a ductwork coil in winter, a $60 above-ground pool, or a free jacuzzi [#5819 · 2025-04-25 · Travis Bitkle] [#5821 · 2025-04-25 · Dane O] [#5822 · 2025-04-25 · Dane O] [#5823 · 2025-04-25 · Dane O]. A laundromat's hot water would need a hydronic system with a 24kw heat dump [#3620 · 2025-01-16 · Cade].

## Water chemistry, glycol and corrosion

- **Galvanic corrosion.** Dissimilar metals in electrical contact in a conductive fluid corrode. Inhibited glycol is less conductive, and plastic tubing segments act as dielectric breaks [#4854 · 2025-03-24 · Travis Bitkle]. Mixed aluminum and copper loops raise electrolysis concerns, and one builder isolated them with tubing [#4796 · 2025-03-23 · Cody Harris] [#4797 · 2025-03-23 · Travis Bitkle].
- **Aluminum fails first.** M64 cooling plates are aluminum, so in a mixed-metal loop they "would be the first to go", risking pinhole leaks onto hashboards [#6856 · 2025-07-29 · Dane O] [#9231 · 2026-02-20 · Tyler Stevens].
- **Fill water.** Travis filled his loop with remineralized RO water, which "basically dissolved the copper pipe" and pumped "liquid copper" through his M64 for the first couple of days [#6876 · 2025-07-29 · Travis Bitkle]. He flushed and refilled with filtered softened water plus a little chemical treatment, and did not think the miner was permanently damaged [#6880 · 2025-07-29 · Travis Bitkle] [#6887 · 2025-07-29 · Travis Bitkle] [#6901 · 2025-07-30 · Travis Bitkle].
- **Glycol mix and inhibitor.** One Heat Core system was commissioned on ~35% propylene glycol plus demineralized water [#9089 · 2026-02-11 · Heatpunk Forum]. To add inhibitor: stop the miner, bleed down the pressure, pour in a few ounces, recharge to the starting cold pressure, run the pumps to clear air, then power on [#9243 · 2026-02-20 · Travis Bitkle]. Model-specific details are in [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md#plumbing-fittings-and-coolant).
- **Glycol reuse.** The reused glycol in one loop was aluminum-safe, mixed with distilled water, and never touched domestic water [#4864 · 2025-03-24 · Travis Bitkle].
- **Too-cold starts.** A hydro miner that had 3C water circulating through it for a day refused to start because it was too cold [#4862 · 2025-03-24 · Travis Bitkle].

## Pumps, strainers, air and failsafes

- **Pump ladder.** Home builds can climb from a single-speed circulator, to multi-speed manual, to home-sized ECM pumps that vary speed on a temperature input, and finally to industrial pumps [#713 · 2024-08-21 · Bob].
- **Strainers.** Use a "y strainer" and match its micron rating to your BPHE's specs [#6649 · 2025-06-28 · Dane O].
- **Air.** In a sealed double loop, an inverted T at the high spot let the loop "burp like you would a radiator" [#7282 · 2025-09-06 · Barc].
- **Pump continuity after outages.** At remote sites, put a 240v UPS on the tank pump only, not the miners, so the loop recovers from a power outage without a site visit [#3751 · 2025-01-22 · Cade]. An integrated PDU lets the pump, network switch and miners all come back on their own [#3756 · 2025-01-22 · Dane O].
- **Interlocks.** Cody Harris asked for a contactor that kills miner power if the pump stops [#5353 · 2025-04-07 · Cody Harris] [#5355 · 2025-04-07 · Cody Harris]. Web-controlled PDUs with individually switched outlets can switch a dry cooler, valves or pump from a temperature signal [#8321 · 2025-12-17 · Dane O].
- **Sensor placement.** Unexplained temperature spikes while a pump was off were traced to convective thermosiphon "bleed over" through the BPHX. Move the sensors further down the line and add probes on the oil side [#4556 · 2025-03-18 · Dev 🇳🇿] [#4562 · 2025-03-18 · Dane O] [#4565 · 2025-03-18 · Dev 🇳🇿].
- **Hoses and fittings.** FH hoses are not cheap, and FH BSP flat-face + gasket fittings are uncommon in some markets. Nylon fittings are fine for experiments but not for customer installs [#4615 · 2025-03-19 · Dev 🇳🇿] [#4649 · 2025-03-20 · Dev 🇳🇿].

## Waterblock miners: Cryobyte, Zeus kits and converted S19s

- **Direct-to-chip.** CryoByte Labs offers direct-to-chip cold plates for single-phase miners; its founder concluded direct-to-chip was the most cost-effective way to capture heat [#1590 · 2024-10-16 · Ryan Ramminger]. One hybrid product puts liquid on the chip faces and fans on the back of the hashboards [#1430 · 2024-10-08 · Tyler Stevens]. A direct-to-chip demo used two 360mm aluminum radiators with six stock Antminer fans [#1703 · 2024-10-24 · Ryan Ramminger].
- **Josh's Cryobyte water heater.** An S19 jpro with Cryobyte blocks fits in a much smaller space than an immersion tank, at the cost of more upfront work installing the blocks [#4891 · 2025-03-27 · Josh] [#4894 · 2025-03-27 · Josh] [#4899 · 2025-03-27 · Josh]. Here is how it runs:
  - LuxOS ATM holds 62c and scales down as the water gets hotter. The tank pump turns on when the water heater falls below 60c [#4912 · 2025-03-27 · Josh] [#4913 · 2025-03-27 · Josh].
  - With the tank at 130 (54c), the miner held 62c underclocked to 400mhz/2000w. Without radiator fans it reached 140, then overheated and shut itself off [#5120 · 2025-03-29 · Josh] [#5127 · 2025-03-29 · Josh].
  - Household hot water alone does not justify the full 3kw, so the unit could become a "central heat mine" feeding HVAC, a pool and so on [#5118 · 2025-03-29 · Josh].
- **Block costs.** Elijah Sanders paid $50 per waterblock making his own; the cheapest set seen elsewhere was about $107 [#5490 · 2025-04-14 · Elijah Sanders] [#5491 · 2025-04-14 · Dev 🇳🇿]. A DIY portable 120V hydro miner cost about $350 for the block, pump, fittings and plate exchanger. The block came from Zeus Mining because Cryobyte blocks seemed unavailable by December 2025 [#8260 · 2025-12-11 · Josh]. On a 120v circuit, a hydro build covering 500w to 1600w gives a lot of useful range [#5791 · 2025-04-25 · Mark | @satstackingpleb] [#5793 · 2025-04-25 · Toine Heat Reuse].
- **Fitment.** S19 JPro+ boards have soldered-on heatsinks, so off-the-shelf Cryobyte kits won't fit without rework [#7508 · 2025-11-01 · Travis Bitkle]. First-series S19k Pro boards also have soldered single heatsinks, while later series use plate heatsinks with paste. Soldered sinks can be removed with chip-rework hot air [#7513 · 2025-11-01 · Gianluca L] [#7514 · 2025-11-01 · Gianluca L]. Retrofit kits are model-specific because board size, ASIC count and position, and case dimensions all differ [#7519 · 2025-11-01 · Gianluca L]. On an Ember One, soldermask is "not a reliable insulator", so watch for metal tabs touching the PCB [#7631 · 2025-11-08 · Skot Bitaxe].
- **Converted S19s vs factory Bitmain hydro (October 2026).** Benji's S19 hydro conversions on Zeus Mining kits run at ~80°C chip temp with no restarts and a flow temperature around 52°C [#10610 · 2026-10-05 · Benji]. In his experience the original Bitmain hydro miners aren't well suited to this kind of setup ("temperatures rise very quickly"), while the modified S19s run at 80–81°C chips with a 50°C heating flow [#10615 · 2026-10-06 · Benji].
- **Outlet temperatures by maker.**
  - Whatsminer M64: 80 C / 176 F outlet [#662 · 2024-08-19 · Tyler Stevens]
  - Bitdeer SealMiner (claimed): 70C out and 60C in [#4662 · 2025-03-20 · Dev 🇳🇿]
  - Canaan hydro: 87C outlet, with chips around 98C [#10614 · 2026-10-06 · Aadhi M]
- **Power.** Antminer hydros want three-phase power; see [Heater Electrical and 120V Builds](heater-electrical-and-120v-builds.md).

## Control for hydronic loads

- **Lower the "hot" limits on fixed heat sinks.** When the miner feeds a water loop, drop the hot temp from 80°C to near your run point, for example hot 72°C and danger 78°C, and use DPS to manage power [#5159 · 2025-03-29 · Travis Bitkle].
- **DPS against the slab.** Travis's slab-heating hydro Antminer uses Braiins DPS to scale power up and down with how much heat the slab can take. Setting the hot temp lower and the target higher keeps the operating range tight [#6665 · 2025-06-30 · Travis Bitkle], and he calls it "set it and forget it" [#7013 · 2025-08-12 · Travis Bitkle].
- **Slow restarts hurt.** When a miner scales on boiler fluid temperature, a long firmware restart lets the fluid cool further and triggers a deeper, unneeded scaling event [#2383 · 2024-12-02 · Cody Harris].
- **Fast ATM timing.** LuxOS ATM with timing set to 1 minute adjusts quickly and overclocks as cold water enters during long showers [#5118 · 2025-03-29 · Josh].
- **Simple alternatives.** Braiins DPS plus a bang-bang 220V timer switch can replace Home Assistant for a water heater [#4911 · 2025-03-27 · Cody Harris]. Pair it with [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md) and [Home Assistant Heater Control](../mining-software/home-assistant-heater-control.md).

## Thermal storage and buffer tanks

- **Batch loads need buffers.** Batch processes such as microbreweries need buffer tanks, because a few thousand watts running continuously would outstrip distribution [#768 · 2024-08-23 · Harrison The Space].
- **Off-peak charging.** One plan uses an insulated 500 gal tank charged only off-peak at $0.045/kWh, targeting 50,000 BTUs an hour for 7-8 hours to cover the on-peak window [#3648 · 2025-01-18 · Travis Bitkle] [#3650 · 2025-01-18 · Travis Bitkle] [#3655 · 2025-01-18 · Travis Bitkle].
- **Big tanks.** Two S19j pro at 3.2kw each heated a 3000 gallon tank to 115F in about 1.5 days for a concrete batch plant [#3594 · 2025-01-16 · Cade] [#3598 · 2025-01-16 · Cade]. An instant gas heater on the output can top off for hotter water [#3597 · 2025-01-16 · Cade]. Two industrial water-tank setups were reported very reliable, with owner ROI of about 12 months [#3552 · 2025-01-16 · Cade].
- **Two-coil buffer.** Benji's next step is a 600 L buffer with the lower coil on the miner glycol loop, the upper coil on the heating water, and a target flow temp of 55–60°C [#10610 · 2026-10-05 · Benji].
- **Alpine chalet.** A chalet above 1,700 meters in Switzerland is heated entirely by an RY3T system with no issues at –20 °C. Its controller labels the tap water tank (WW), the radiator buffer tank (Puffer), the RY3T delivery temperature (WEZ) and the mixed radiator temperature (HK1) [#8752 · 2026-01-20 · Christian Naef] [#8762 · 2026-01-20 · Christian Naef].

## Field data and installs (chronological)

- 2024-08: A shop's radiant floor, hot water and jacuzzi were heated with two underclocked S19s (a hashratehouse.com product) [#441 · 2024-08-06 · Dane O]. A client with a basement dry cooler feeding a jacuzzi and water heater saved over 600$ in 6 months [#568 · 2024-08-10 · Dane O].
- 2024-08: A central ASIC heat core plus hydronic system for 4 ASICs was costed at Electrical 1k, Cabinet frame out 500, Hydronic system parts 5k and Immersion equipment 3k [#770 · 2024-08-23 · Cade]. In new construction, everything but the ASIC would be paid anyway [#773 · 2024-08-23 · Cade].
- 2025-01: "Newer S21s heat better it seems" [#3597 · 2025-01-16 · Cade]. A hot-water-heater oil tank held water between 150 and 127 (F) depending on use [#3833 · 2025-02-01 · Karl].
- 2025-06: Exergy and The Space received an RY3T Mini and a Heat Core HS05, both M64-based, for a radiant-floor demo [#6446 · 2025-06-10 · Heatpunk Forum]. See [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md).
- 2025-11: A C2 immersion install with two S19 Pro 110T heats an aircraft hangar, with a brazed plate HX feeding a big wash-water tank [#7977 · 2025-11-25 · Cade] [#7979 · 2025-11-25 · Cade].
- 2026-10: Benji's converted S19 hydro build in Austria [#10610 · 2026-10-05 · Benji].

## Contradictions & Open Questions

- Whether every install needs a heat dump (see the Disputed block above).
- Plate vs shell-and-tube for pool water (see the Disputed block above).
- Whether one loop of mixed metals (copper, cast iron, brass, stainless) with an aluminum-plate M64 and no HX survives long term. Travis is running it as a live test [#6862 · 2025-07-29 · Travis Bitkle].
- Whether two coils in one buffer tank, one for the miner glycol and one for heating water, perform well. The question was open as of 2026-10-05 [#10610 · 2026-10-05 · Benji].

## See Also

- Same topic: [Whatsminer M64-Family Hydro Heaters](whatsminer-m64-hydro-heaters.md)
- Same topic: [Immersion Heat Reuse](immersion-heat-reuse.md)
- Same topic: [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md)
- Same topic: [Heater Electrical and 120V Builds](heater-electrical-and-120v-builds.md)
- Same topic: [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- Same topic: [Ember One (BZM2)](ember-one-bzm2.md)
- Firmware: [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md)
- Software: [Home Assistant Heater Control](../mining-software/home-assistant-heater-control.md)
- Economics: [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)
- Industry: [Hashrate Heating Products and Installs](../industry/hashrate-heating-products-and-installs.md)
- Industry: [Repair, Supply and Vendors](../industry/repair-supply-and-vendors.md)
- History: [Heatpunks Community Timeline](../history/heatpunks-community-timeline.md)
