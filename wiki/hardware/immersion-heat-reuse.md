# Immersion Heat Reuse

> Sources: Hashrate Heatpunks Telegram group, 2024-08-02 → 2026-10-08
> Raw: [Hashrate Heatpunks Telegram signal digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

Immersion cooling submerges ASIC hashboards in a dielectric liquid (engineered fluids such as Bitcool or DCX, mineral oil, or even canola oil) and moves the heat out of the tank through a plate heat exchanger into water, glycol or air. For heat reuse it has three attractions the Hashrate Heatpunks group keeps returning to: the oil bath is a large thermal buffer (Karl: a much larger battery than water cooling) [#2321 · 2024-12-01 · Karl], it is silent once the fans are removed or slowed in oil [#2669 · 2024-12-09 · Michael Schmid @Schnitzel], and it decouples the heat source from the miner model, so one tank can host several hardware generations [#8207 · 2025-12-08 · Cade] [#8388 · 2025-12-22 · Dane O]. The price is plumbing, fluid chemistry and a set of failure modes air cooling doesn't have: oil wicking up cables, plastic and seal compatibility, static, and fluid degradation. Builds range from canola oil in a trash can heating 40 gallons of domestic hot water to commercial Fog Hashing tanks heating a hangar.

## Rules of thumb

- **Don't immerse miners in the water you want to heat.** Immersing miners in hot water isn't good for them; the working pattern is an immersion-cooled miner on a boiler loop with a brazed plate heat exchanger (BPHX) [#3540 · 2025-01-16 · Brett Rowan] [#3543 · 2025-01-16 · Cade].
- **Every system needs a heat dump.** Cade's pattern: a dry cooler outside on thermostatic fan control holds the oil at up to 57c, and a recirculation pump pulls fluid through the HX only when the water needs heat [#3558 · 2025-01-16 · Cade] [#3565 · 2025-01-16 · Cade]. 57 (c) keeps machine efficiency and water temperature acceptable [#3754 · 2025-01-22 · Cade]. Corollary: vary the way you pull heat from the loop, not the computer [#3559 · 2025-01-16 · Cade] [#3563 · 2025-01-16 · Cade]. Whether dumping heat is affordable is disputed; see [Contradictions](#contradictions--open-questions).
- **Match the sink to immersion temperatures.** Most radiant floors want around a 50-60c inlet and a 40c ish return, which suits immersion operating temps [#1432 · 2024-10-08 · Dane O]; a hot tub at 104 (F) matches the 40c inlet most immersion systems want [#3586 · 2025-01-16 · Dane O].
- **Oversize heat exchangers.** Pool HX ratings assume a 140f+ delta between heating medium and pool, while immersion gives at best a 50-60f delta, so roughly double whatever you calculate [#7582 · 2025-11-07 · Dane O]. Oversizing liquid-to-liquid HXs doesn't increase cost by much [#712 · 2024-08-21 · Harrison The Space]. Immersion oil won't warp plate HX plates [#7648 · 2025-11-12 · Dev 🇳🇿] [#7650 · 2025-11-13 · Nicolas Drouin-Audet].
- **Move water, not oil.** For a water loop through an oil tank it is cheaper to move a high volume of water through a coil in the oil than to pump lots of oil around a big loop; the main risk is water leaking into the oil [#8396 · 2025-12-22 · Karl] [#8406 · 2025-12-22 · Karl].
- **Keep the PSU and control board out of the oil when you can.** In Karl's water-heater build neither the PSU nor the control board is in the oil, and he uses bus bars instead of cables [#2772 · 2024-12-15 · Karl] [#2989 · 2024-12-29 · Karl]. S19 PSUs reportedly don't like the heat, so air-cooling the PSU while liquid-cooling the boards is suggested for very hot fluid [#2987 · 2024-12-29 · Cody Harris]. Prefer an external PDU: passing power through the tank complicates UL ratings and cord compatibility [#3759 · 2025-01-22 · Cade] [#3760 · 2025-01-22 · Cade].
- **Fail safe on the pump.** A contactor that kills miner power if the pump stops was requested as a failsafe [#5353 · 2025-04-07 · Cody Harris] [#5355 · 2025-04-07 · Cody Harris]; at remote sites put a 240v UPS on the tank pump only, and an integrated PDU lets pump, switch and miners come back by themselves after an outage [#3751 · 2025-01-22 · Cade] [#3756 · 2025-01-22 · Dane O].

## Fluids

### Engineered dielectrics, mineral oil and canola

| Fluid | Field notes |
|---|---|
| Engineered (Bitcool, DCX) | Purpose-built for ASICs. DCX engineered fluid barrels used to cost $8/Liter [#8941 · 2026-01-29 · Elijah Sanders] [#8946 · 2026-01-29 · Elijah Sanders]; Hashrate House sold coolant at $160 per 20L in December 2024 [#3007 · 2024-12-30 · Dane O]. A Bitcool vs DCX freezing test was run, with no result posted [#7161 · 2025-08-21 · Elijah Sanders]. |
| Mineral oil | Farm-store mineral oil (sold as a bovine digestive aid) worked for S9 testing [#1183 · 2024-09-17 · Jonathan Y] [#2421 · 2024-12-02 · Jonathan Y]. Typically needs Nylon-covered wires and Viton seals to avoid damage in the medium term (months) [#8937 · 2026-01-29 · Gianluca L]. Cost cited as $20-25/gal (April 2026) [#9820 · 2026-04-08 · Karl]. |
| Canola / vegetable oil | Cheap and available; Karl's long-running choice. $8/gal (April 2026) [#9820 · 2026-04-08 · Karl]. Degrades and must be replaced or reconditioned (see below). |
| Transformer oil | **Don't use it.** High sulfur content and dissolves silicone-based components such as capacitor seals; buy legitimate dielectric oil for ASICs [#7965 · 2025-11-25 · Dane O]. |

Regular immersion fluid and pumps "isn't really made for these temps" when pushed for water heating [#2665 · 2024-12-09 · Michael Schmid @Schnitzel].

### Canola oil: lifetime and maintenance

The evolution of Karl's canola experience, from first trial to more than a year of service:

- **Sep 2024:** canola immersion in use for maple syrup production; seen as fine short-term given cost and availability, and an oil-soaked board was cleaned and returned to air cooling. Jonathan Y reported canola had mixed reports [#1178 · 2024-09-17 · Karl] [#1184 · 2024-09-17 · Karl] [#1185 · 2024-09-17 · Karl] [#1183 · 2024-09-17 · Jonathan Y].
- **Dec 2024:** vitamin e oil added to keep it stable; open questions were how long canola lasts and whether its failure could cause an arc and fire [#2988 · 2024-12-29 · Karl] [#2998 · 2024-12-29 · Karl].
- **Mar–Apr 2025:** year-old canola still working as dielectric in the maple sap heater; oil reused from the previous season, still going strong [#4435 · 2025-03-06 · Karl] [#5481 · 2025-04-14 · Karl] [#5482 · 2025-04-14 · Karl]. If canola goes rancid, a cheap oil change is the remedy [#5893 · 2025-05-03 · Josh].
- **Nov 2025:** cheaper than most options even if replaced or reconditioned every 8-12 months, but Karl's oil degraded faster than expected from too much oxygen and too much heat [#7968 · 2025-11-25 · Karl].
- **Apr 2026:** with vitamin e the oil lasts about 8 months; a test without it lasted 6 months. Less oxygen exposure or aeration and a lower max temperature should extend life [#9808 · 2026-04-08 · Karl] [#9817 · 2026-04-08 · Karl]. After a year and a few months with a couple of oil changes, no board degradation, and boards can be cleaned and run on air again [#9810 · 2026-04-08 · Karl] [#9817 · 2026-04-08 · Karl].

**How you know it's spent:** the system overheats faster and faster as the oil thickens and flow drops, until it can't dump heat [#9821 · 2026-04-08 · Karl]. Karl is experimenting with cutting thickened canola with mineral oil to lower viscosity (6:1 canola : mineral oil) [#9808 · 2026-04-08 · Karl] [#9818 · 2026-04-08 · Karl]. Spent oil can become chainsaw bar oil or fatwood-soaking oil for kindling no thicker than one inch [#9811 · 2026-04-08 · Mike Clear] [#9812 · 2026-04-08 · Karl].

> **Status: Disputed**
> Is mineral oil safe for hashboards? Jonathan Y used farm-store mineral oil successfully [#1183 · 2024-09-17 · Jonathan Y]. Karl has heard mineral oil is bad for hashboards [#9818 · 2026-04-08 · Karl], and Gianluca L says mineral oil usually needs Nylon-covered wires and Viton seals to avoid damage over months [#8937 · 2026-01-29 · Gianluca L]. Current best assessment: mineral oil works short-term; plan cable insulation and seal materials for it, or use an engineered fluid for long-lived installs.

## Tanks, containers and plumbing

- **DIY containers.** Karl has run immersion in plastic storage totes, smaller trash cans and water coolers, while flagging static-electricity concerns with plastic [#5891 · 2025-05-03 · Karl]. Josh considered a polypropylene trash can sized for an S19 and later ran a "2-board s19 with 120v mod in an ikea trash can immersion tank" [#5889 · 2025-05-03 · Josh] [#5892 · 2025-05-03 · Josh] [#6014 · 2025-05-16 · Josh]. Karl's maple sap heater is an S19 board and modified apw12 submerged in canola in a paper shredder waste bin, with wood blocks and ceramic weights as ballast [#4435 · 2025-03-06 · Karl].
- **Pipe material.** Use CPVC rather than PVC: PVC "will weaken overtime with the Dielectric fluid and crack" and doesn't handle heat well [#5985 · 2025-05-12 · Dane O]; CPVC has more fittings, but its fail temperature is the main concern [#5992 · 2025-05-13 · Gerald Glickman].
- **Commissioning a new loop.** Don't get it wet: wipe down and/or blow compressed air to clear debris [#5979 · 2025-05-12 · Gerald Glickman] [#5980 · 2025-05-12 · Nicolas Drouin-Audet] [#5981 · 2025-05-12 · Josh]. An experienced builder has never used isopropyl to prep systems, only to clean miners leaving immersion [#5983 · 2025-05-12 · Nicolas Drouin-Audet]; isopropyl is super flammable, so nothing energized and never pump it through the system [#5986 · 2025-05-12 · Dane O].
- **Water-heater plumbing.** Karl's input goes into the top at the pressure relief valve with recirculation out the bottom through a BPHX; a filter between heater drain and pump/HX is recommended [#3000 · 2024-12-29 · Dane O] [#3001 · 2024-12-29 · Karl].
- **Dry coolers.** Off-the-shelf drycoolers "don't work very well" for immersion because they are built for much higher flow rates (200-300l/min) [#5538 · 2025-04-15 · Dane O]. If you aren't doing the math, oversize the dry cooler; non-EC or non-industrial fans give diminishing returns [#7966 · 2025-11-25 · Dane O]. A car radiator can work, ideally behind a cheap (~$50) HX so dielectric fluid doesn't run through it, though pumping oil straight through also works [#7954 · 2025-11-25 · Elijah Sanders] [#7957 · 2025-11-25 · Elijah Sanders] [#7960 · 2025-11-25 · Elijah Sanders]. Dry-cooler fan staging: on at 30 and off at 50c gives 20 steps (5% increases), on at 45 and off at 50 gives 5 (20% increases) [#3748 · 2025-01-22 · Dane O]. A large furnace filter in front of an indoor dry cooler keeps basement dirt off the HX [#7899 · 2025-11-23 · Dane O].
- **Plate HX details.** A pool-heater plate-frame HX: 3/4” inlet on the oil side, 1” on the water side, ~70lpm water and 45lpm oil flow; plate count can be adjusted to miner count, with pressure loss the concern when reducing plates [#789 · 2024-08-23 · Nicolas Drouin-Audet] [#790 · 2024-08-23 · Nicolas Drouin-Audet] [#800 · 2024-08-23 · Nicolas Drouin-Audet].
- **Corrosive water.** Salt water needs titanium or cupronickel; aluminium in an aquarium corroded seriously [#782 · 2024-08-23 · Nicolas Drouin-Audet] [#4638 · 2025-03-20 · Jonathan Y] [#4640 · 2025-03-20 · Dane O].

## Cable wicking and sealing

Oil climbs power cords and sensor cables by capillary action — reported on DIY tanks and on the Fog C2 [#1775 · 2024-10-30 · R D] [#3746 · 2025-01-22 · R D].

- Sealing the plug-to-cord-jacket junction mitigates it [#1777 · 2024-10-30 · Gerald Glickman].
- Oil creeps inside cable insulation even through cable glands; refineries epoxy-seal cables, and the permanent fix is a sealed connection [#1794 · 2024-10-30 · Nicolas Drouin-Audet].
- Cables over 1m stiffen about a foot out of the fluid; on smooth tank walls fluid climbs about an inch [#1798 · 2024-10-31 · Bob].
- Oil reaching contactors along the wires is a recurring problem in immersion heaters; DIN-rail 32A contactors ran without other issues [#1499 · 2024-10-12 · Nicolas Drouin-Audet] [#1514 · 2024-10-12 · Nicolas Drouin-Audet].
- Bus bars instead of cables (Karl) sidestep part of the problem [#2772 · 2024-12-15 · Karl].

## Converting air-cooled miners: fans and fan simulators

- To convert an air-cooled miner such as the Avalon A15 Pro, remove the fans and add fan simulators [#8008 · 2025-11-28 · Aadhi M]. Whatsminer offers a free "Air to Liquid" firmware for aftermarket fans or immersion [#1646 · 2024-10-21 · Toine Heat Reuse].
- Alternatively keep the fans: Schmid mounts the miner fans at the bottom (case inlet) to push oil through the miner. Without them the oil is already at 90F mid-miner and the upper chips don't cool; "With the fans it works muuuch better", and the flow is far more than a basic external-pump setup [#2665 · 2024-12-09 · Michael Schmid @Schnitzel] [#2672 · 2024-12-09 · Jonathan Y].
- Fans in oil: power them with 12V directly and drop the RPM wire; they run much slower and silent — Karl guesses oil limits them to like 200rpm [#2669 · 2024-12-09 · Michael Schmid @Schnitzel] [#2670 · 2024-12-09 · Karl]. Set fans to 100% in firmware and ignore RPM [#2674 · 2024-12-09 · Jonathan Y].
- Thermal paste: S17 and S19 are fine in immersion; S21s are mixed — fine in a properly designed tank, but too high a flow blows the paste off [#7939 · 2025-11-24 · Dane O].

## Firmware and temperature limits

Hotter chips mean hotter water, and builders have pushed firmware limits well above air-cooled norms:

- Vnish's default critical chip temp is 90c. Karl raised his limit from 81 to 90 for longer runtime between draws, settling on critical 90, target 80, hot 85 [#2657 · 2024-12-09 · Karl] [#2666 · 2024-12-09 · Karl] [#2676 · 2024-12-09 · Karl]. Before raising limits he reached 130f water [#2660 · 2024-12-09 · Karl].
- Michael Schmid runs "90 target, 95 hot, 100 critical" and gets water easily to 140-145F [#2659 · 2024-12-09 · Michael Schmid @Schnitzel] [#2662 · 2024-12-09 · Michael Schmid @Schnitzel].
- **The limiting part isn't the ASIC.** The i2c communication chips glitch at high temps, breaking hashboard-to-control-board communication; the control board treats one glitch as failure and doesn't recover until mining is fully restarted [#2668 · 2024-12-09 · Michael Schmid @Schnitzel]. Similarly, S9 chips could run above 100C but other hashboard components limited the device to 80C [#3212 · 2025-01-08 · Tyler Stevens].
- Control boards in immersion: two Braiins BCB100s ran in S19JPROs in immersion for about 4 months without problems [#4285 · 2025-02-26 · Cody Harris] [#4290 · 2025-02-26 · Cody Harris]; ePIC boards reported working great in immersion with good response and tuning [#6670 · 2025-06-30 · Dane O]. Braiins fan management complaints are irrelevant when immersed [#4916 · 2025-03-28 · Mark | @satstackingpleb]. Braiins OS+ also has an "immersion mode" setting [#1686 · 2024-10-23 · Toine Heat Reuse].
- Whatsminer immersion firmwares Rosseau (defunct) and BixBit underwhelmed; BixBit cuts startup from ~90seconds to about 10 seconds but carries a 2% dev fee [#4491 · 2025-03-13 · Cody Harris].

> **Status: Disputed**
> How hot should immersed chips run? R D's hottest observed chip temp is 77-78° and he thinks 80 is probably safe but "way less efficient J/Th"; Cody Harris stresses about 70C [#2658 · 2024-12-09 · R D] [#2680 · 2024-12-09 · Cody Harris]. Schmid and Karl run 80-90c+ for water heating [#2659 · 2024-12-09 · Michael Schmid @Schnitzel] [#2986 · 2024-12-29 · Karl]. Current best assessment: 80-90c works for months in DIY water heaters at an efficiency cost; the i2c glitch failure mode, not the hashing chip, is the practical ceiling.

## Build: Karl's canola-oil immersion water heater

The group's most documented DIY immersion build is Karl's domestic hot water heater.

- **Setup (Dec 2024):** a 40gal tank and an 88 chip S19 bought for $275, usually on one board; oil tank recirculates through a BPHX; neither PSU nor control board in the oil; an apw12 modified for 120v because the 240v plug was needed for house heating [#2982 · 2024-12-29 · Karl] [#2985 · 2024-12-29 · Karl] [#2989 · 2024-12-29 · Karl] [#2422 · 2024-12-02 · Karl].
- **Cost:** "less than $100 in parts" beyond the pumps, oil and miner (Dec 2024) [#2996 · 2024-12-29 · Karl]; later itemized as $136 for pumps and heat exchanger plus $60 of canola oil (June 2025), though Dane O estimated the same parts at about $200 alone in retail [#6651 · 2025-06-28 · Karl] [#6648 · 2025-06-28 · Dane O].
- **Power and temperatures:** he expected around 1800w continuously but most of the time needs only about 700w; one board at 700w keeps the water above 120 if usage isn't all at once [#3002 · 2024-12-29 · Karl] [#3005 · 2024-12-30 · Karl]. With 1500w he gets all the hot water he needs; chips sit in the 80c range and hit 90c before the miner reaches critical temp and shuts off mid-night, with water at 150 at the farthest tap [#2982 · 2024-12-29 · Karl] [#2986 · 2024-12-29 · Karl] [#3005 · 2024-12-30 · Karl]. Feb 2025: water ranged from 150 down to 127 (F) depending on use [#3833 · 2025-02-01 · Karl]. Mar 2025: 800w keeps the tank very hot but the miner still overheats around 4am [#4905 · 2025-03-27 · Karl].
- **Recovery:** after two showers, dishwasher and laundry it takes several hours to get back to 150; a 1500w recharge rate is probably too slow for 5 showers in a row [#3005 · 2024-12-30 · Karl] [#2983 · 2024-12-29 · Karl]. He upgraded to a bigger HX to speed recovery [#4406 · 2025-03-04 · Karl].
- **Late 2025 numbers:** 22-24j/th, max about 1200w, hot water close to 150f; about 1.5kw covers his water heater, so 2 boards should cover most demand, and a bigger tank solves simultaneous draws [#8281 · 2025-12-15 · Karl] [#7968 · 2025-11-25 · Karl] [#8386 · 2025-12-22 · Karl]. He upgraded the hashboards to S19 KPro, paid for with the system's own mined bitcoin [#6651 · 2025-06-28 · Karl].
- **Reliability:** ran continuously for over a month with no issues by Dec 2024 and was still running since November in April 2025 [#3001 · 2024-12-29 · Karl] [#5482 · 2025-04-14 · Karl].
- **Thesis:** hot water is the best way to integrate mining into any home because everyone uses it daily, year-round in any climate [#2978 · 2024-12-29 · Karl] [#3000 · 2024-12-29 · Dane O].

A gentler variant is a "pre heat tank" (~105F) feeding the regular water heater [#2980 · 2024-12-29 · Cody Harris]; Cody Harris runs a miner two hours a day to preheat 45gal of water to ~110F [#4789 · 2025-03-23 · Cody Harris]. The same canola unit, moved to a cold frame, ran stable at 600w heating soil to 75f via a pex loop in moist sand [#4664 · 2025-03-21 · Karl] [#5852 · 2025-04-29 · Karl].

## Commercial immersion products

- **Fog Hashing** (a Whatsminer partner): tank priced at $1000 in August 2024, carried in the US by BitMars [#142 · 2024-08-02 · Tyler Stevens] [#147 · 2024-08-02 · Cody Harris] [#691 · 2024-08-19 · Cade]. The C1 kit suits water heat because it has an external heat dump (Tank>plate HX>external dry cooler>Tank) [#3743 · 2025-01-22 · Cade]; another user runs the same setup and thinks it could be popular "if Fog fixes a few minor problems" [#3745 · 2025-01-22 · Cody Harris]. The C6 has a pump and a dry-cooler outlet with everything else external [#3761 · 2025-01-22 · Cade]; the M1 fits two M33s [#3875 · 2025-02-07 · Trevor Bello]. Used-market data point: two C1's, a dry cooler and 10gallons of Bitcool for $400 [#144 · 2024-08-02 · Cody Harris].
- **CADDY 2:** $8k to $25k for 320 to 800 TH/s (January 2025); about 140cm by 200 in size, with a 14kw figure at 320 discussed; the maker modifies off-the-shelf product and wants its own boards but can't easily get cores [#3067 · 2025-01-03 · Colin Sullivan] [#3072 · 2025-01-03 · Dane O] [#3078 · 2025-01-03 · Dane O] [#3095 · 2025-01-04 · Colin Sullivan].
- **Hashrate House** (Dane O), December 2024 pricing including shipping: total system $2700 (tank, PDU, bphx, hoses and cooler); tank only $1700; cooler only $1000 [#3007 · 2024-12-30 · Dane O]. Its coolers are redesigned with custom internals and an EC fan with built-in temperature controller [#5536 · 2025-04-15 · Dane O] [#5538 · 2025-04-15 · Dane O].
- **RY3T** (Christian Naef, Switzerland): water-based immersion heating for boilers, floor heating, radiators, tap water and pools; holds one to two M56-series miners (7-14kw) with electronics inside the case but outside the tank, and a regulatory kill switch [#423 · 2024-08-05 · Christian Naef] [#2467 · 2024-12-04 · Christian Naef] [#1242 · 2024-10-01 · Christian Naef].
- **Purpose-built immersion miners:** for 220 single phase, believed to be only the Canaan 1466 and Auradine models; an S21 immersion unit is three phase, "bunk for residential" [#2100 · 2024-11-21 · Dane O].
- **Open source:** github.com/NicoHeatingBTC/home-bitcoin-immersion-mining-system [#1032 · 2024-09-04 · R D].

## Field installs

- 3000 gallon tank heated to 115F by two S19j pro at 3.2kw each in about 1.5 days for a concrete batch plant; add an instant gas heater on the output for hotter water [#3594 · 2025-01-16 · Cade] [#3598 · 2025-01-16 · Cade] [#3597 · 2025-01-16 · Cade]. Two industrial water-tank setups reported an owner ROI of about 12 months [#3552 · 2025-01-16 · Cade].
- Fog C1 water heat: 54 inlet and 65 outlet on 2 underclocked s19's [#3752 · 2025-01-22 · Dane O].
- C2 with 2 S19 Pro 110T heats a hangar of about 2400 ft^2 with a 20' ceiling, plus a BPHX heating aircraft wash water [#7977 · 2025-11-25 · Cade] [#7978 · 2025-11-25 · Cade] [#7979 · 2025-11-25 · Cade].
- Comparison point: an immersion setup gave ~120F water with 74C chip temp [#5121 · 2025-03-29 · Cody Harris]; radiant floor: ~112° oil at 70C chip temp gave ~105° glycol inlet [#167 · 2024-08-02 · Cody Harris].
- Immersed K Pros pegged at 150th [#3474 · 2025-01-15 · R D].
- Immersion-fed snow melt running in Juneau, Alaska [#1432 · 2024-10-08 · Dane O]; a planned immersion-fed concrete slab uses glycol loops instead of a dry cooler and switches to pool heating in summer [#7349 · 2025-09-11 · Brian EcobitQC].
- Building code: Cade's crews pass inspection using immersion miners plus an external PDU, since inspectors require forced-air heaters to be UL listed but immersion moves heat by fluid and keeps equipment outside [#7258 · 2025-09-03 · Cade] [#5566 · 2025-04-16 · Cade].

## Failure modes and safety

- **Static and grounding.** Tingling from touching the PSU of a canola unit in a plastic box: possibly isolation from ground plus static from pumping oil, a big issue on early immersion systems with ungrounded PVC. Verify PSU ground continuity and panel bonding [#5852 · 2025-04-29 · Karl] [#5867 · 2025-04-29 · Dane O].
- **Hose failure.** A tubing failure sprayed warm oil from the pump into a builder's face and eye (no harm done) [#2421 · 2024-12-02 · Jonathan Y].
- **Sensor misreads.** Temperature spikes on a Fog C2 with the water pump off were attributed to thermosiphon bleed-over through the BPHX; move sensors further down the line and add oil temp probes [#4556 · 2025-03-18 · Dev 🇳🇿] [#4562 · 2025-03-18 · Dane O] [#4565 · 2025-03-18 · Dev 🇳🇿].
- **Water ingress** into the oil is the main risk of a water coil in the tank [#8406 · 2025-12-22 · Karl].
- **Oil degradation** (canola): thickening, falling flow, faster overheating [#9821 · 2026-04-08 · Karl].
- **Board survival.** Schmid has "never killed a board in immersion", versus at least 5 on air [#2671 · 2024-12-09 · Michael Schmid @Schnitzel].

## Contradictions & Open Questions

> **Status: Disputed**
> S21s in immersion: Cade reports about 18 s21 in immersion with no issues [#3604 · 2025-01-16 · Cade]; Dane O relays reports of "loads of problems" in an immersion channel [#3605 · 2025-01-16 · Dane O]. Later nuance: S21 thermal paste holds in a properly designed tank but too high a flow blows it off [#7939 · 2025-11-24 · Dane O]. Best assessment: S21 immersion works with controlled flow; older S17/S19 are the safer bet.

> **Status: Disputed**
> Aquariums as tanks: Gerald Glickman says aquarium seals are generally incompatible with Bitcool or legitimate immersion oils, so a leak is a matter of time [#8934 · 2026-01-29 · Gerald Glickman]. Elijah Sanders says a regular aquarium works fine for a full-size ASIC [#8942 · 2026-01-29 · Elijah Sanders], and Jonathan Y's 40 gallon breeders and 125G tanks still hold their seals [#8977 · 2026-01-30 · Jonathan Y]. Best assessment: works in practice for some, but seal chemistry varies by tank — inspect and plan for leaks.

> **Status: Disputed**
> Is immersion worth it at home? Toine considered immersion too expensive for a solo or twin ASIC residential system and preferred air [#554 · 2024-08-10 · Toine Heat Reuse]; Karl argues it is probably the way to go for home use because of the oil buffer [#2321 · 2024-12-01 · Karl], and his canola build shows a low-cost path. Dumping excess heat is itself contested: Cody Harris says it only pays in cheap-power regions and his system dumps none, while Cade says it depends on location [#3564 · 2025-01-16 · Cody Harris] [#3568 · 2025-01-16 · Cody Harris] [#3572 · 2025-01-16 · Cade].

Open questions: whether canola failure can cause arcing [#2998 · 2024-12-29 · Karl]; control-board extension or mount options to keep boards dry [#2765 · 2024-12-15 · Dev 🇳🇿] [#2766 · 2024-12-15 · Dev 🇳🇿]; the unposted Bitcool vs DCX freezing result [#7161 · 2025-08-21 · Elijah Sanders].

## See Also

- [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md)
- [Heater Electrical and 120V Builds](heater-electrical-and-120v-builds.md)
- [Whatsminer M64 Hydro Heaters](whatsminer-m64-hydro-heaters.md)
- [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md)
- [Home Assistant Heater Control](../mining-software/home-assistant-heater-control.md)
- [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)
- [Hashrate Heating Products and Installs](../industry/hashrate-heating-products-and-installs.md)
- [Repair, Supply and Vendors](../industry/repair-supply-and-vendors.md)
- [Heatpunks Community Timeline](../history/heatpunks-community-timeline.md)
