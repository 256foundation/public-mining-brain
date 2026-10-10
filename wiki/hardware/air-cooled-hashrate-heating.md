# Air-Cooled Hashrate Heating

> Sources: Hashrate Heatpunks Telegram group, 2024-08-02 → 2026-10-08
> Raw: [Hashrate Heatpunks Telegram signal digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

Air-cooled hashrate heating is the cheapest entry point to heat reuse: take a stock air-cooled ASIC (usually a used S19-family Antminer or a Whatsminer), replace or supplement its screaming stock fans with a quieter inline duct fan and a shroud, and blow the exhaust into a room, a basement, or the return side of a forced-air HVAC system. Builders in the Hashrate Heatpunks group report that dumping exhaust into the HVAC return (or simply into the coldest part of the house, typically the basement) works well, with the furnace kept downstream as backup heat [#563 · 2024-08-10 · Toine Heat Reuse] [#564 · 2024-08-10 · Toine Heat Reuse] [#577 · 2024-08-10 · Jonathan Y]. Immersion was judged too expensive for a one- or two-ASIC residential system, so air-only is the preferred residential path for many [#554 · 2024-08-10 · Toine Heat Reuse]; air-cooled machines fit the need-heat, expensive-power, on/off-with-demand user type, while immersion in a loop suits always-on use [#3581 · 2025-01-16 · Cade] [#3582 · 2025-01-16 · Cade]. The hard parts are airflow (CFM vs static pressure), noise (especially PSU whine), and not overloading the house's existing blower or furnace safeties.

## Rules of thumb

- **A miner is a ~1:1 electric heater.** Essentially all input power becomes heat, minus fans and LEDs; real losses are BTUs leaking out through the case and duct before reaching the target space [#6772 · 2025-07-10 · Travis Bitkle] [#6770 · 2025-07-09 · Travis Bitkle] [#6938 · 2025-08-06 · Patrick Patel]. Hence the BTU-for-BTU framing: a 1600w resistive heater earns nothing, a miner at 1600w gives the same BTUs plus some BTC [#557 · 2024-08-10 · Dane O].

> **Status: Disputed**
> "All miners are very close to 100%" efficient as heaters [#6772 · 2025-07-10 · Travis Bitkle]. A peer-reviewed study of water heating with an S19 Pro Hydro found only about ~90% of input became useful heat [#10339 · 2026-07-21 · Heatpunk Forum]. Best assessment: both hold — conversion is effectively 100%, but delivery losses (case, ducts, piping) cut the useful fraction; long ducts are a measured example of this [#7344 · 2025-09-10 · Jarno].

- **Where to put the heat.** Heating the coldest part of the home performed almost as well as ducting into HVAC [#563 · 2024-08-10 · Toine Heat Reuse] [#564 · 2024-08-10 · Toine Heat Reuse]. Large (>5000 sqft) homes probably need HVAC integration; smaller homes may do fine dumping directly into a room [#575 · 2024-08-10 · Toine Heat Reuse].
- **Run the HVAC circulating fan 24/7** so warm basement air circulates through the whole house [#576 · 2024-08-10 · Toine Heat Reuse]. If the miners make enough heat for the whole home, turn off the furnace's heat mode and keep only recirculation on [#3935 · 2025-02-10 · Toine Heat Reuse]. Dumping into the return duct with the ventilation fan always on is "like turbo charging the miner" through extra cooling [#4717 · 2025-03-22 · Toine Heat Reuse].
- **Don't over-cool.** Each miner has a temp/efficiency sweet spot, so too cold is also bad [#4719 · 2025-03-22 · Karl]. One operator got 23w/Th at 55C chip temps on underclocked S19j Pros; pushing to 40C in winter showed diminishing returns below 50C [#154 · 2024-08-02 · Travis Bitkle] [#155 · 2024-08-02 · Travis Bitkle].
- **Keep the control simple.** The simplest scheme used: two modes only — low power in spring/fall, full power in winter — with the regular heat source covering peaks [#940 · 2024-09-04 · Jonathan Y]. A cheap wifi thermometer plus a smart switch driving a contactor (relays are not safe at this power) can schedule the miner and toggle it at preset temps [#203 · 2024-08-02 · Toine Heat Reuse] [#942 · 2024-09-04 · Toine Heat Reuse]. See [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md) and [Home Assistant Heater Control](../mining-software/home-assistant-heater-control.md).
- **Thermostat deadband.** Pause/resume the miner from the thermostat rather than scaling power, and widen the deadband (e.g. 69F/73F instead of 70F/72F) so it cycles less [#8077 · 2025-12-02 · Travis Bitkle] [#8079 · 2025-12-02 · Travis Bitkle].
- **Size for the month, not the worst day.** Match monthly heat demand and add a cheap non-mining supplementary heater for the coldest days rather than oversizing mining [#427 · 2024-08-05 · Bob]. Details in [Hashrate Heating Economics](../economics/hashrate-heating-economics.md).
- **Mind the circuit.** On 120v, about 1900W is usable on a 20 amp circuit and about 1400W on a 15 amp; if breakers trip, check wire size, replace worn breakers and remove other loads [#8064 · 2025-12-01 · Cade] [#8067 · 2025-12-01 · Mike Clear]. Full electrical guidance is in [Heater Electrical and 120V Builds](heater-electrical-and-120v-builds.md).

## Airflow: fans, CFM and static pressure

### Inline duct fans

- The community default is an 8-inch AC Infinity (ACI) inline fan with a Njord fan-control board; the Njord typically holds the fan between 300 and 700 cfm depending on chip temp [#560 · 2024-08-10 · Toine Heat Reuse] [#617 · 2024-08-10 · Toine Heat Reuse]. An 8-inch ACI fan at 70% still keeps an M30S+ cool [#731 · 2024-08-23 · Toine Heat Reuse].
- The ACI inline fan maxes out at 800cfm, but one heater typically runs at about half, varying with temperature [#3374 · 2025-01-14 · Toine Heat Reuse] [#3373 · 2025-01-14 · Toine Heat Reuse]. For comparison, two stock S19 fans together move about 370cfm [#3370 · 2025-01-14 · Dane O], and two Noctua fans in a Loki-style config moved 1300 CFM [#642 · 2024-08-11 · Mark | @satstackingpleb].
- Inline-fan setups draw "Lower by 50 to 100w than the same th output on stock fans" [#3382 · 2025-01-14 · Toine Heat Reuse].
- Cheap alternatives disappoint: one builder tried no fewer than 10 inline fans from Amazon — noisier and much less efficient than ACI, and the one decent option lacked a tach signal [#1581 · 2024-10-15 · Zack Bomsta].
- The Njord board requires a tach signal back from the fan, so it can't be fooled into running the miner when the fan isn't spinning [#1581 · 2024-10-15 · Zack Bomsta]. It also handles fan spoofing for S19 fan swaps in one board [#6441 · 2025-06-09 · Travis Bitkle]. Caveat: an S17 on a Njord took a long time to tune and cycled on and off for about two days before running steadily [#6979 · 2025-08-12 · Travis Bitkle].
- Gotcha: ACI fans powered from a miner PDU would not start at about 262v per leg with no load; once the miners were running, line voltage dropped to about 252v and the fans started [#3676 · 2025-01-20 · Travis Bitkle].

### Static pressure and the house blower

- Higher air speed means more static pressure, which mainly loads the fan; the static pressure from a fan or blower isn't seen as a risk to the chips [#3381 · 2025-01-14 · Patrick Patel]. One builder forced 585cfm through a Whatsminer without the blower stalling or vibrating — the fan curve matters more than the miner [#3371 · 2025-01-14 · Patrick Patel].
- Watch the house blower motor: like high MERV/FPR filters, a miner in the plenum adds static pressure that can burn out a blower motor early [#3385 · 2025-01-14 · Dane O]. Tube-fin heat exchangers installed in plenums have a maximum allowable cfm that must be balanced [#3376 · 2025-01-14 · Dane O].
- A single furnace blower eventually hits an aerodynamic limit pushing high volumes of air through Whatsminers, prompting interest in aftermarket hashboard heat exchangers [#7380 · 2025-10-03 · Patrick Patel].
- Static pressure builds up fast with miners, so airflow management is key in any ducted design [#3336 · 2025-01-13 · The schnauze].

## Shrouds, baffles, grills and fan swaps

- **Shrouds.** On S19 builds the shroud mounts on the 8 fan screw holes; removing the 4 outside screws pulls fan and shroud off in one shot [#5582 · 2025-04-16 · Toine Heat Reuse]. Not all shrouds help: 3D-printed S9 "muffler" shrouds from cults3d made the miner louder and added resistance, and the Crypto Cloaks single-to-6in shroud is sold as a product, not a file [#3025 · 2025-01-02 · Jason]. Yeggi searches many model sites at once, and Thingiverse also has S9 shrouds [#3030 · 2025-01-02 · Jonathan Y] [#3026 · 2025-01-02 · Dane O].
- **Grills.** Removing intake/exhaust grills reduces obstruction, fan work and noise; on S19 shroud builds the intake grill is needed to mount the shroud, and the exhaust grill can stay for finger safety [#5577 · 2025-04-16 · Dane O] [#5578 · 2025-04-16 · Toine Heat Reuse] [#5586 · 2025-04-17 · Patrick Patel]. On Whatsminers, remove the inlet/outlet frames [#5586 · 2025-04-17 · Patrick Patel].
- **Baffles.** Venturi-style air baffles on the StealthMiner design were "far exceeding" expectations [#1604 · 2024-10-16 · Ryan Ramminger] [#1606 · 2024-10-16 · Mark | @satstackingpleb]. With 3000 rpm Noctuas an S19 can run on 2 fans instead of 4 up to around where chips get voltage-starved, but air baffles are required [#5977 · 2025-05-12 · Josh]. The baffle kit still needs fitment work but works very well [#7203 · 2025-08-28 · Heatpunk Forum].
- **PSU fans.** An 8 inch ACI fan with a shroud adapter that covers PSU cooling lets you remove the PSU fans [#2013 · 2024-11-17 · Eric Blockhouse] [#2020 · 2024-11-17 · Mark | @satstackingpleb]; Nakamoto mining fan shrouds put an adapter over the PSU for the same reason [#8116 · 2025-12-02 · Trevor Bello]. Swapping PSU fans for Noctuas allows 1600w pull with no issues [#2021 · 2024-11-17 · Mark | @satstackingpleb]. The apw3++ PSU fan can reportedly be swapped with just an adapter, no spoofer (unconfirmed) [#2009 · 2024-11-17 · Trevor Bello] [#2015 · 2024-11-17 · Trevor Bello]. At about 1,300 watts (roughly a third of PSU rating), going from 3 PSU fans to one checks out [#8113 · 2025-12-02 · Travis Bitkle] [#8124 · 2025-12-03 · Karl].
- **Printing.** PCTG is recommended filament for ASIC parts — good temperature resistance and easy to print [#5769 · 2025-04-25 · Toine Heat Reuse] [#5774 · 2025-04-25 · PizzAndy].

### Open design files

- Antminer S19 CAD files: github.com/SatStackingPleb/Antminer-S19-CAD-Files [#4523 · 2025-03-14 · Mark | @satstackingpleb]
- S19 Air Baffle Kit: github.com/SatStackingPleb/S19-Air-Baffle-Kit; Slim19: github.com/SatStackingPleb/Slim19 [#4675 · 2025-03-22 · Mark | @satstackingpleb] [#4677 · 2025-03-22 · Mark | @satstackingpleb]
- 140mm APW12 fan adapter: github.com/jsorchik/apw12-140mm [#4524 · 2025-03-14 · Josh] [#4885 · 2025-03-26 · Josh]
- StealthMiner, Slim19/21 and baffle files are also posted on heatpunks.org [#7203 · 2025-08-28 · Heatpunk Forum]; StealthMiner add-ons in progress are a HEPA intake and 8 inch capture shrouds [#7361 · 2025-09-14 · Mark | @satstackingpleb]
- Single-board S19 case for the APW3 PSU on MakerWorld (makerworld.com/en/models/375862) [#1322 · 2024-10-08 · Jonathan Y]; 256heat.com sells 3D-printed heat-reuse components [#9479 · 2026-03-02 · Toine Heat Reuse]

## Noise and quiet mods

- Reported noise for heater setups ranged 40 - 60db [#572 · 2024-08-10 · Toine Heat Reuse]. Compact rigs trade dB against performance: the StealthMiner stays under 60dB while the Slim19 is "stupid quiet in the 40s" [#5600 · 2025-04-17 · Mark | @satstackingpleb]; anything in the 40s reads as background noise to one builder [#5601 · 2025-04-17 · Toine Heat Reuse].
- dB doesn't capture annoyance: the 40s are tolerable only if the PSU's high pitch is silenced too, and harmonics from many fans grate even at low dB [#5605 · 2025-04-17 · Cody Harris]. On a shrouded S19 the PSU fan is louder than the ACI fan until fan speed 4 [#5606 · 2025-04-17 · Toine Heat Reuse]. Small-diameter fans are annoying even at 45 dB because of pitch [#5589 · 2025-04-17 · Toine Heat Reuse].
- Canaan's Q heater marketing cites 45-65 db depending on power profile; 65 dB was judged too loud for home use [#5587 · 2025-04-17 · Toine Heat Reuse] [#5588 · 2025-04-17 · The schnauze]. An earlier Canaan heater listed at 45-64db drew the verdict that even 45 is too high [#4342 · 2025-02-28 · Cody Harris].
- Slowed-fan quiet mods are verified only up to 1100W; it is unclear whether a slowed fan can cool full wattage [#5613 · 2025-04-17 · Mark | @satstackingpleb]. Inline resistors on fans reduce noise [#8126 · 2025-12-03 · Karl].
- Insulated duct between the miner and the heated space helps reduce noise [#125 · 2024-08-02 · Travis Bitkle]. Custom radiators with ACI inline fans run "like 50 decibels" [#1704 · 2024-10-24 · Ryan Ramminger].
- Startup roar: fans run at 100% on boot because they're powered before the OS can send speed signals [#1683 · 2024-10-23 · Brett Rowan]. Workaround: set the inline fan manually (no Njord board) and run Braiins OS+ in "immersion mode", tuning to your highest tolerable cfm [#1686 · 2024-10-23 · Toine Heat Reuse] [#1687 · 2024-10-23 · Toine Heat Reuse].
- Furnace-style products sidestep the issue: a 4-Whatsminer electric furnace replacement uses a standard furnace-style blower so the noise is what people expect [#3150 · 2025-01-08 · Patrick Patel].

## Furnace and HVAC integration

### Ducting into the return

- One home filters the inlet and dumps miner exhaust straight into the furnace intake — it "Worked amazing all winter long" [#919 · 2024-09-03 · Jonathan Y]. Another cut up the furnace to send miner output into the return air (air-cooled, stock firmware) [#2609 · 2024-12-07 · Jonathan Y]. Others push old S9s against the air intakes [#2349 · 2024-12-02 · Jason].
- Product idea from the group: a furnace with a modular ASIC bay placed before the gas section so boards never see furnace heat [#589 · 2024-08-10 · Jonathan Y].
- Gotcha: a furnace's limit switch can shut the furnace down if intake air is too hot; duct miners in before the blower [#3896 · 2025-02-08 · Jason].
- Open concern: cutting a hole just before the furnace reduces the vacuum at every other return in the house, which could hurt circulation [#7878 · 2025-11-23 · Tyler Stevens].
- An electric damper that recirculates air based on temperature worked well [#3670 · 2025-01-20 · Toine Heat Reuse]. Pair a thermostat controller with a smart outlet so the fan doesn't run during curtailment or on-peak shutdowns [#3683 · 2025-01-20 · Travis Bitkle]. Tuya smart plugs handled S9s at 800w, but a couple burned out above 1000w [#3669 · 2025-01-20 · Dylan Seib].
- In extreme cold, start older Whatsminers first and blow their hot air to the cold side to warm the other machines before starting them [#3664 · 2025-01-20 · Travis Bitkle].

### Heat-pump aux and staged thermostats

- Heat-pump aux heat is usually a plain resistance coil in the plenum, triggered by a 24v signal, so a miner can stand in as an on-demand hashrate aux heater [#3986 · 2025-02-12 · Dane O]; on one system aux runs only when the set temp is 2° above actual or during defrost, so it cycles [#4025 · 2025-02-13 · Dane O]. Heat-pump backup resistive elements are already on a 240v circuit — a natural slot for a miner [#1065 · 2024-09-04 · Tyler Stevens] [#1066 · 2024-09-04 · R D].
- Hybrid setup at the Exergy office: a Canaan Avalon Q is connected wirelessly to Stage 1 of a Venstar T7900 thermostat via Home Assistant, while Stage 2 is hard-wired to the furnace [#8895 · 2026-01-27 · Heatpunk Forum].
- Whatsminer-based furnaces behave like resistive heaters (on or off); one builder sets low/normal/high mode at install and prefers more miners on low power to limit power cycles [#3167 · 2025-01-08 · Patrick Patel], and ships a side-mounted or remote thermostat [#5197 · 2025-03-31 · Patrick Patel] [#5198 · 2025-03-31 · Patrick Patel].

### Hybrid: liquid-cooled miner, air delivery

Hydro miners can also feed forced air via a water-to-air coil, which removes the noise problem. A Heat Core HS05 supplied "buddy" heat to a natural gas furnace: with only the furnace circulator fan running (no flame), airflow pulled 4000 Watts (normal mode M64) off the dry cooler without its fans turning on, making a silent furnace miner [#7875 · 2025-11-23 · Tyler Stevens] [#7876 · 2025-11-23 · Tyler Stevens] [#7877 · 2025-11-23 · Tyler Stevens]. Another M64 Hydro in an HS05 chassis works well with a water-to-air HX in the furnace plenum [#8458 · 2025-12-26 · Britton]; its design estimate was 1000cfm through the HX with 176F water and 60F inlet air giving outlet air around 128F [#7390 · 2025-10-06 · Britton]. Installer tip: put a large furnace filter in front of a basement dry cooler so dirt doesn't clog the HX — it also filters basement air [#7899 · 2025-11-23 · Dane O]. Wrapping PEX around ducts conducts poorly; put a water-to-air exchanger (even an old car heater core) inside the duct instead [#4997 · 2025-03-28 · Dylan Seib] [#5016 · 2025-03-28 · Jonathan Y]. See [Whatsminer M64 Hydro Heaters](whatsminer-m64-hydro-heaters.md) and [Hydronic Heat Reuse](hydronic-heat-reuse.md).

## Small spaces and single-board heaters

- To heat a tiny space where an S9 at 380W is too much, disable hashboards in Braiins OS — leave the disabled board in place for normal airflow, or disconnect it from the PSU [#5720 · 2025-04-23 · Jake⚡️] [#5726 · 2025-04-23 · ₿ Minion]. To drop a board, turn it off in firmware rather than pulling the 18 pin ribbon [#5846 · 2025-04-29 · Toine Heat Reuse].
- Single-board S19s on 120v (Loki board or APW12 resistor mod) are the community's standard room heater, and S19s have largely displaced S9s for this role [#2219 · 2024-11-29 · Jonathan Y] [#5930 · 2025-05-09 · Jason]. A single jpro board hashed at 25.5j on 110v with only 2 quiet fans (arctic p12 pro 3k rpm), measured at the wall; temps averaged 44c with 65c chip temp [#8886 · 2026-01-26 · Karl] [#8889 · 2026-01-26 · Karl].
- Altair BitChimney: a T21 board runs a steady 48th and heats a 625sqft room well [#8906 · 2026-01-28 · Joe C]; another unit with a used JPro board drew 1,220 at the wall at "33+ w/th" [#8913 · 2026-01-28 · Barnminer Barnmyna].
- HeatJack S19 Loki space heater build guide, written for an office using 900 - 1500W of heat a day [#8995 · 2026-02-02 · Heatpunk Forum]. Small-bedroom options suggested: Canaan Mini 3 or HeatBit Maxi [#7690 · 2025-11-14 · Heatpunk Forum]; a whole-home guide uses Avalon Mini 3s with zigbee sensors and a Home Assistant thermostat [#7210 · 2025-08-28 · Tyler Stevens].
- Builds, PSUs and breaker limits for these rigs live in [Heater Electrical and 120V Builds](heater-electrical-and-120v-builds.md).

## Indoor air quality (VOCs)

- A summit panel claimed hot air-cooled miners release chemicals into the air [#4193 · 2025-02-23 · Patrick Patel].
- Response: miners use standard electronics fabrication; expect some volatile off-gassing on first run like any PCB product, and a CE mark implies "materials of concern" compliance [#4203 · 2025-02-23 · Bob].
- Toine called the claim FUD: the S17 had an issue, but VOC testing on S19s came back good; a post-hashboard filter helps if you're concerned [#4207 · 2025-02-23 · Toine Heat Reuse] [#4209 · 2025-02-23 · Toine Heat Reuse].
- Higher chip temperatures may matter for emissions, assuming board materials don't change [#4201 · 2025-02-23 · R D]. A fresh-air intake near the miners can leave house air fresher in winter [#4199 · 2025-02-23 · Travis Bitkle]; StealthMiner's planned HEPA intake addresses dust [#7361 · 2025-09-14 · Mark | @satstackingpleb].
- For food drying with miner air, some worry about fumes from heated circuits reaching the food, and miner air doesn't get hot enough to dry meat safely [#8623 · 2026-01-08 · Elijah Sanders] [#8631 · 2026-01-11 · Karl].
- Assessment (as of 2026-10-09): no field measurements of harm were posted; the group consensus is that new-unit off-gassing is transient and filtering is the cautious mitigation.

## Safety

- A running miner fan badly cut someone who stuck a finger in it [#2039 · 2024-11-18 · Karl] — another reason to keep the exhaust grill [#5586 · 2025-04-17 · Patrick Patel].
- Losing fan power will "melt all the heat sinks off"; set dangerous temp to around 85°C and hot to 80°C [#6980 · 2025-08-12 · Travis Bitkle].
- Firmware sleep still draws power — Antminers pull 150w to 240w in standby and Braiins sleep is about 200w — so a switch or contactor is needed to truly cut power at the target temp [#742 · 2024-08-23 · Toine Heat Reuse] [#257 · 2024-08-02 · Toine Heat Reuse] [#255 · 2024-08-02 · Toine Heat Reuse].
- Internet outage gotcha: when the internet went out, miners stopped hashing and blew cold air, and the house got cold [#2897 · 2024-12-23 · Toine Heat Reuse]. Use a "limp mode" such as Braiins' drain:// backup pool [#7931 · 2025-11-24 · Heatpunk Forum]. Cutting ethernet instead of power to stop a heater is probably gentler, but fans keep running with no heat, which confuses households [#7856 · 2025-11-23 · Jarno] [#7857 · 2025-11-23 · Josh].

## Field data

| Setup | Result | Anchor |
|---|---|---|
| Three-floor home, 800sqft/floor, ASIC into HVAC | Furnace only fired under -5C | [#578 · 2024-08-10 · Toine Heat Reuse] |
| Two underclocked jPros blown into home HVAC | Two running at 1,600 watts | [#162 · 2024-08-02 · Travis Bitkle] [#174 · 2024-08-02 · Travis Bitkle] |
| Furnace replaced by 2 S19jPros (overclock to 9kW) | Held 71-72 F all winter except two sub-zero periods | [#427 · 2024-08-05 · Bob] |
| Commercial building, miners as only heat | -10F outside, 88F air into a 7,000 sq/ft building; shop 60F+ | [#4121 · 2025-02-18 · Travis Bitkle] |
| Commercial air build | Pumping 1,600 cfm into adjacent spaces | [#1987 · 2024-11-16 · Travis Bitkle] |
| Used S19 95TH (3250W), cleaned, shrouded, ducted into furnace in about an hour | About 23 W/TH on LuxOS; "heating at a 90% discount" | [#4671 · 2025-03-22 · Toine Heat Reuse] |
| Same, after the space warms and it downclocks | About $0.20 per day to heat the cabin | [#4680 · 2025-03-22 · Toine Heat Reuse] |
| 104 TH J Pro | Heating half a house at -1C outside | [#4769 · 2025-03-23 · Toine Heat Reuse] [#4770 · 2025-03-23 · Toine Heat Reuse] |
| 88 TH S19 on Vnish, basement heat | 66TH and 2100 watts | [#3325 · 2025-01-12 · Zackery Miller] |
| RV heated by two 120V S19s (88 chip, APW12, LuxOS) | About 27 J/Th; no propane yet in single-digit temps | [#8154 · 2025-12-05 · Heatpunk Forum] |
| Air-cooled Whatsminer as sauna pre-heater | Reached 30 C; a ton of heat lost in the long duct | [#7339 · 2025-09-10 · Jarno] [#7342 · 2025-09-10 · Jarno] [#7344 · 2025-09-10 · Jarno] |

Efficiency comparisons from the same thread: another builder's best was ~26j/th on single boards at about 700w [#4682 · 2025-03-22 · Karl]; Toine credited good ventilation and called the K Pro "the downclock champs" [#4691 · 2025-03-22 · Toine Heat Reuse] [#4694 · 2025-03-22 · Toine Heat Reuse]. Whatsminer M50S units were noted as cheap and more efficient than the S19jpro, especially at 2000W, at 23-24 J/TH [#9685 · 2026-03-16 · Dan Sokil]. On Braiins DPS, room temps going from 20 to 25 drove chip temps from 60 - 70 fairly reliably on S19K Pro, S19 XP and S21 [#243 · 2024-08-02 · Toine Heat Reuse].

### Commercial air-heat example: the cheese plant

A micro-mine in an old cheese plant used a temporary wall to form a chimney into the attic, insulated duct to duct socks, and tenant-side ACI fan controllers so tenants take as much heat as they want [#116 · 2024-08-02 · Travis Bitkle] [#119 · 2024-08-02 · Travis Bitkle] [#127 · 2024-08-02 · Travis Bitkle]. A 10-inch ACI fan at 1,400 cfm moves 120F air to the larger space, with 8-inch ACI fans for the smaller one and ~300K BTU's planned for the drafty building [#122 · 2024-08-02 · Travis Bitkle] [#123 · 2024-08-02 · Travis Bitkle] [#124 · 2024-08-02 · Travis Bitkle] [#125 · 2024-08-02 · Travis Bitkle]. Excess heat dumps through a fan at the chimney's ceiling penetration [#129 · 2024-08-02 · Travis Bitkle].

### Laundromat dryer assist

A laundromat project ducts basement miners up through the floor into 6” exhaust, with a damper sending air to electric Speed Queen dryers when in use or outside when not [#3260 · 2025-01-12 · Zackery Miller]. Dryer blowers are 4” rather than 6 or 8 [#3275 · 2025-01-12 · Zackery Miller]. A home trial found the gotchas: the dryer element doesn't run continuously, and the miner needs far more airflow than a dryer moves, so positive drum pressure pushed lint into the room [#3287 · 2025-01-12 · Karl]. Fixes suggested: size up the exhaust hose or replace the dryer elements with mining heat entirely [#3289 · 2025-01-12 · Patrick Patel]; drive the damper from a relay off the dryer's circuit or its switched 120V leg [#3277 · 2025-01-12 · R D] [#3288 · 2025-01-12 · Patrick Patel].

## Prices (dated)

- As of March 2025: used S19 95TH (3250W) units at $300 USD with a 60 day warranty [#4671 · 2025-03-22 · Toine Heat Reuse].
- As of March 2026: JPros called "the modern S9" and great for heatpunks, with a local listing at $15 judged a buy no matter what hashprice is (the message does not say whether that is per unit) [#9738 · 2026-03-26 · Travis Bitkle] [#9743 · 2026-03-26 · Travis Bitkle].
- Broader hardware pricing history is in [Hashrate Heating Economics](../economics/hashrate-heating-economics.md).

## See Also

- [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- [Heater Electrical and 120V Builds](heater-electrical-and-120v-builds.md)
- [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- [Whatsminer M64 Hydro Heaters](whatsminer-m64-hydro-heaters.md)
- [Immersion Heat Reuse](immersion-heat-reuse.md)
- [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md)
- [Home Assistant Heater Control](../mining-software/home-assistant-heater-control.md)
- [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)
- [Hashrate Heating Products and Installs](../industry/hashrate-heating-products-and-installs.md)
- [Community Workshop Wisdom](../getting-started/community-workshop-wisdom.md)
