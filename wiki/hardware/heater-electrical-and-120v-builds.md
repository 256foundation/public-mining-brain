# Heater Electrical & 120V Builds

> Sources: Hashrate Heatpunks Telegram group, 2024-08-02 → 2026-10-08
> Raw: [Hashrate Heatpunks Telegram signal digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

A hashrate heater is an electric resistance heater that happens to compute, so the electrical side decides what is safe and what is possible. The Heatpunks group's working rules: give each miner a dedicated 240V circuit sized with the 80% continuous-load margin; size contactors with a 20% buffer; switch big loads with contactors, not cheap relays or smart plugs; terminate wires with proper crimps or ferrules at the correct torque; and fuse anything you build [#203 · 2024-08-02 · Toine Heat Reuse] [#1700 · 2024-10-24 · Dane O] [#1525 · 2024-10-12 · Toine Heat Reuse] [#3914 · 2025-02-09 · R D]. For homes without spare 240V, the community worked out how to run one or two S19 hashboards from an ordinary 120V outlet, using either a Loki board or an APW12 PSU with a resistor mod that stops brown-out protection from tripping [#2219 · 2024-11-29 · Jonathan Y] [#2332 · 2024-12-01 · Dev 🇳🇿] [#2767 · 2024-12-15 · Karl]. Larger sites hit a different problem. Many US commercial buildings have 208V three-phase service, while hydro ASICs expect 220-277V per leg, so transformers are part of the plan [#4430 · 2025-03-06 · Travis Bitkle] [#8159 · 2025-12-05 · Travis Bitkle]. Builders also tied miners directly to solar.

## Rules of thumb

### Circuits and the 80% rule

- **Size for continuous load at 80% of the breaker rating.** Worked example for two 3200w miners: 3200w x2 = 6400w; 6400w / 240v = 26.6A; a 40A breaker gives 9600w, and x.8 = 7680w continuous, so the pair fits [#3914 · 2025-02-09 · R D]. When R D was going through failed contactor coils, others told him to check the amp rating against the load and the 80% load factor [#2153 · 2024-11-24 · Dane O] [#2162 · 2024-11-25 · R D].
- **Target per-miner draw:** about 24A max per miner, which is 24Ax240v = 5.7kw or 24Ax208v = 5kw. A 30a PDU feeding 2 miners limits each one to about 2.8kw. On a 50A outlet, about 20A per machine is usually where it lands [#3776 · 2025-01-22 · Cade] [#3777 · 2025-01-22 · Cade] [#3778 · 2025-01-22 · Cade].
- **Common circuit patterns:** 1-2 miners per PDU on a dedicated 30 or 40 amp 240 V breaker [#3299 · 2025-01-12 · Zackery Miller]. Two miners on one PDU with 10awg L6-30 wiring works well if you don't overclock [#3957 · 2025-02-10 · Toine Heat Reuse].
- **Overclocking headroom:** overclocking commonly pushes 3200w to like 4000w, and the next bottleneck is usually the 20amp c19 cables [#3915 · 2025-02-09 · R D]. For overclocking, use 50A for 2 miners and 60A for 3 [#3916 · 2025-02-09 · Nicolas Drouin-Audet]. Sharing one circuit limits headroom. One builder ran two 30 amp circuits instead, because 60 amp wire is stiff and hard to work with [#3914 · 2025-02-09 · R D].
- **Fewer, bigger runs are usually cheaper.** One larger wire, breaker and outlet usually costs less than two smaller wires, two breakers and two outlets [#3936 · 2025-02-10 · Dane O]. A suggested layout is one dedicated 40 amp circuit for the miner plugs plus one 10amp circuit with a junction box for peripherals such as the switch, sensors, pumps, controllers and dry cooler [#3938 · 2025-02-10 · Dane O] [#3928 · 2025-02-10 · Dane O].
- **Existing 240V heating circuits are natural slots.** Baseboard heaters are usually 220 on a 20a breaker, which is enough for one miner [#724 · 2024-08-23 · Toine Heat Reuse] [#729 · 2024-08-23 · Toine Heat Reuse]. The backup resistive elements on a heat pump are already on a 240v circuit, which makes a miner a natural backup heat source [#1065 · 2024-09-04 · Tyler Stevens] [#1066 · 2024-09-04 · R D].

### Receptacles, cords and splitters

- Each miner needs at least its own dedicated L6-20R (20A circuit), with no splitter. Note that 6-20R and L6-20R are different receptacles [#3925 · 2025-02-09 · Patrick Patel]. To save on PDUs, wire each breaker to an L6-20 plug [#3310 · 2025-01-12 · Patrick Patel].
- Cade's standard is at least 10ga wire to an L6-30 and a PDU with a surge protector and switch. For two miners he runs 6/3 wire to a 50A outlet and an RV splitter to 2 L6-30 pigtails, which supports 4 s19j pros downclocked or two overclocked [#3948 · 2025-02-10 · Cade]. A 50A RV outlet to a dual L6-30 splitter runs 2 PDUs for 2 S19j with 8kw power supplies or overclocked S21s [#3765 · 2025-01-22 · Cade].
- He uses a 14-50 50A splitter. The neutral isn't really used, but 6-50 splitters are harder to source and the 4-prong setup is stronger [#3768 · 2025-01-22 · Cade].
- Big two-miner boxes outgrow residential plugs. Two Auradine miners in one box exceed 14kw (a 63amp constant load), and no residential plug handles over a 45amp constant load at the 80% margin, so split or external PDUs make sense [#3775 · 2025-01-22 · Dane O].
- A proposed PDU plugs into an existing Nema 14-50 outlet (dryer, range, ev charger) and passes the appliance back through, so no new wiring is needed [#5348 · 2025-04-07 · Dane O] [#5352 · 2025-04-07 · Dane O].

> **Status: Disputed** (20A 240V circuits)
> Patrick Patel treats a dedicated L6-20R (20A circuit) per miner as the minimum [#3925 · 2025-02-09 · Patrick Patel], and baseboard-heater 20a circuits are cited as enough for one miner [#724 · 2024-08-23 · Toine Heat Reuse]. Cade refuses 20A 240v circuits: "I don't f around with 20A 240v circuits" [#3949 · 2025-02-10 · Cade]. Current best assessment: a 20A circuit can carry one stock-clocked miner within the 80% margin, but it leaves no overclock headroom, and the 20amp c19 cables become the bottleneck [#3915 · 2025-02-09 · R D]. If you are pulling new wire, 30A (10ga, L6-30) or larger is the safer default.

### PDU vs PSU, phases and per-leg voltage

- A PDU distributes power to multiple devices. A PSU converts input AC (220V-277V generally) to 12V DC for the control board and hashboards [#1573 · 2024-10-15 · Brett Rowan].
- Miner PDUs take three phase, but the individual PSUs take 200-250v single phase. In the example PDU, L1 feeds the first 8 C19 plugs, L2 the next 8 and L3 the remaining 8 [#449 · 2024-08-06 · Travis Bitkle] [#451 · 2024-08-06 · Travis Bitkle]. The T21 PSU is reportedly a true 3 phase PSU [#453 · 2024-08-06 · Travis Bitkle].
- With 415Y240 power, L-L is 415 and L-N is 240, and load must be balanced across the phases [#456 · 2024-08-06 · Brett Rowan] [#190 · 2024-08-02 · Travis Bitkle].
- A miner fed 120v on one leg and nothing on the other did not start, and it was not damaged [#1519 · 2024-10-12 · R D].
- Gotcha: AC Infinity fans powered from a miner PDU would not start at about 262v per leg with no load. Once the miners were running, line voltage dropped to about 252v and the fans started [#3676 · 2025-01-20 · Travis Bitkle].
- External vs in-tank PDU: Cade prefers an external PDU because passing power through an immersion tank makes UL ratings and power-cord compatibility harder. Network switches can sit outside too [#3759 · 2025-01-22 · Cade] [#3760 · 2025-01-22 · Cade]. Three-phase or single-phase 125A 6-plug PDUs are hard-wired with fine-strand stage lighting cable from a junction box or switch [#3765 · 2025-01-22 · Cade].
- An integrated PDU lets the pump, network switch and miners come back on their own after a power outage [#3756 · 2025-01-22 · Dane O]. At remote sites, put a 240v UPS on the tank pump only, not on the miners, so the loop recovers without a site visit [#3751 · 2025-01-22 · Cade]. PDUs with individually controlled outlets and locking plugs can switch a dry cooler, valves or a pump from a temperature signal and can be controlled over the web [#8321 · 2025-12-17 · Dane O].

## Switching: contactors, relays and smart plugs

- **Use a contactor for on/off control of a miner.** A smart switch drives the contactor coil. Relays are not safe at this power [#203 · 2024-08-02 · Toine Heat Reuse].
- **Size contactors with a 20% buffer.** A 30 amp load * 1.2 = 36 amp, so use a 40 amp contactor. Equivalently, 40amp * .8 = 32amp max load [#1700 · 2024-10-24 · Dane O].
- **Terminations cause most burn damage.** In one contactor failure, the damage likely came from the wire-to-contactor interface, where some strands carried more current and acted as a slow-burn fuse. The fix is high-current crimps (yellow crimps for 10 gauge) or ferrules [#1520 · 2024-10-12 · Bob] [#1521 · 2024-10-12 · R D]. Terminals have torque specs, and both over-torqued and under-torqued connections cause poor contact and heat [#1700 · 2024-10-24 · Dane O].
- **Fuse the contactor box.** A fuse or breaker in the box is a requirement for UL/CSA approval [#1525 · 2024-10-12 · Toine Heat Reuse]. DIN rail breakers are sourced from McMaster-Carr and Digikey [#1531 · 2024-10-12 · Bob] [#1532 · 2024-10-12 · Bob].
- **Field notes on hardware.** DIN-rail-mounted 32A contactors have run in heaters with no issues other than oil ingress, and oil wicking along wires into contactors is a recurring problem in immersion builds [#1514 · 2024-10-12 · Nicolas Drouin-Audet] [#1499 · 2024-10-12 · Nicolas Drouin-Audet]. The 30amp version of one AC-style contactor is very noisy [#1498 · 2024-10-12 · Toine Heat Reuse]. R D's contactor coils run on 24vac with about 17ish amps through one miner, and he went through many failed activating coils in one season [#2154 · 2024-11-24 · R D] [#2157 · 2024-11-24 · R D].
- **Smart plugs: only at S9 scale.** Tuya smart plugs handle S9s at 800w without issue, but a couple burned out above 1000w [#3669 · 2025-01-20 · Dylan Seib]. One suggested smart device was "only good up to 25amps" [#2374 · 2024-12-02 · Dane O]. Sonoff S31 smart plugs measure power and can be flashed with Tasmota to run fully local [#7487 · 2025-10-29 · Heatpunk Forum].
- **Wi-Fi PDU switch.** It sits between the mainline breaker and the PDU and switches the system on or off from temperature sensors, other triggers, or manually from anywhere [#1273 · 2024-10-05 · Trevor Bello]. Firmware sleep still draws power, so a switch like this is still needed to fully cut power at the target temperature [#255 · 2024-08-02 · Toine Heat Reuse] [#257 · 2024-08-02 · Toine Heat Reuse]. A 240V wifi relay switch paired in Home Assistant with a Venstar T7900 local-API thermostat runs one furnace-integrated miner [#7877 · 2025-11-23 · Tyler Stevens].
- **Pump failsafe.** One builder asked for a contactor that kills power to the miners if the pump stops [#5353 · 2025-04-07 · Cody Harris] [#5355 · 2025-04-07 · Cody Harris].
- **Power cut vs network cut.** Cutting ethernet instead of power is probably gentler on the hardware, but fans keep running with no heat, which confuses non-technical households. Josh prefers smart plugs so the household has a manual button [#7856 · 2025-11-23 · Jarno] [#7857 · 2025-11-23 · Josh].
- **DIN-mount controller option.** The LILYGO T-Connect Pro combines an Ethernet touchscreen, a 10amp relay and an esp32 for $70 [#4412 · 2025-03-06 · Dane O].

## Service capacity and curtailing around big appliances

- Panel capacity is often the real limit. One home added a full second 200 amp panel, ideally with ASIC heating and an EV on that panel at an alternate rate [#2541 · 2024-12-05 · Jonathan Y]. A commercial building with 800 amp service is "very rare" [#1890 · 2024-11-06 · Travis Bitkle].
- Curtail miners while a central furnace or AC compressor runs, then resume [#2351 · 2024-12-02 · Cade] [#2353 · 2024-12-02 · Cade]. Options include current sensors on big appliances that signal Home Assistant to turn off the wifi relays [#2386 · 2024-12-02 · Dev 🇳🇿], Toine's Wi-Fi PDU Switch curtailing from sensors [#2377 · 2024-12-02 · Toine Heat Reuse], or transfer switches (50-63-100amp etc.) so the heater runs only when an appliance like the dryer is off, which avoids an extra wire run through the house [#2375 · 2024-12-02 · Dane O].
- Controls in development can auto-adjust to a service limit, for example 160A on a 200A service [#4837 · 2025-03-23 · Cade] [#4842 · 2025-03-23 · Cade]. Home Assistant can also alert at a demand threshold such as a 10kw demand limit [#5209 · 2025-03-31 · Karl] [#5217 · 2025-03-31 · Dylan Seib].
- Laundromat example: power a 120V damper from the switched 120V leg of the dryer's 240V element circuit and stay under the 80% circuit threshold [#3288 · 2025-01-12 · Patrick Patel].

## Measuring power

- Measure draw with a clamp meter at the breaker or a permanently installed CT, ideally wired into Home Assistant. One builder made a DIY meter with C13/14 and C19/20 inputs for plugs that aren't NEMA 5-15 [#4573 · 2025-03-19 · Travis Bitkle] [#4574 · 2025-03-19 · Dev 🇳🇿] [#4566 · 2025-03-18 · Dane O].
- Iotawatt Wi-Fi ESP32 devices with current-transformer ports monitor whole panels [#9002 · 2026-02-02 · Barnminer Barnmyna].
- Firmware power estimates can be off. In one single-board build, "the firmware overshoots by about 100w" compared with the wall reading [#8889 · 2026-01-26 · Karl]. A BitChimney drew 1,220 at the wall, a bit over the firmware estimate [#8913 · 2026-01-28 · Barnminer Barnmyna].

## Safety and code

- Ground continuity: a builder felt tingling when touching the PSU of a canola immersion unit in a plastic box. Possible causes were isolation from ground and static from pumping oil, which was a big issue on early immersion systems with ungrounded PVC pipes. Make sure the PSU ground has continuity to ground and check panel bonding [#5852 · 2025-04-29 · Karl] [#5867 · 2025-04-29 · Dane O].
- Lightning: one M64 was likely lost to a lightning strike [#10383 · 2026-07-28 · Travis Bitkle].
- Code: building code requires forced-air heaters to be listed, and inspectors invoke UL for them. Cade's workaround is immersion miners with an external PDU, and he reports passing inspections that way. A listed PDU is the main issue [#5566 · 2025-04-16 · Cade] [#7258 · 2025-09-03 · Cade] [#7259 · 2025-09-03 · Cade]. In Minnesota, a pool heater install needs both a mechanical license and an electrical license [#7236 · 2025-09-02 · Elijah Sanders]. See [Hashrate Heating Products & Installs](../industry/hashrate-heating-products-and-installs.md) for certification and insurance.

## 120V builds: single-board S19 heaters

### Why 120V

Most US rooms only have 120V outlets. Running one or two S19 hashboards at reduced power lets builders heat with an ordinary outlet anywhere in the house [#2219 · 2024-11-29 · Jonathan Y]. A full miner can also run on 120V if it is underclocked [#1566 · 2024-10-15 · Mark | @satstackingpleb]. Splitting an S19 into 3 miners needs a control board, power supply, enclosure and cooling for each hashboard, and it spreads the hashpower across house circuits [#4327 · 2025-02-27 · Josh]. With Loki boards, S19s became the common space heater and S9s were left looking for new uses. One builder called S19-era machines "the next S9's. Durable as hell. Reliable" [#5930 · 2025-05-09 · Jason] [#2216 · 2024-11-29 · Jonathan Y] [#2334 · 2024-12-01 · Karl].

### 120V circuit limits

- About 1900W is usable on a 20 amp circuit and about 1400W on a 15 amp circuit. If breakers trip, verify the wire size, replace old breakers (they wear out and trip early), and make sure no other loads are on the circuit [#8064 · 2025-12-01 · Cade] [#8067 · 2025-12-01 · Mike Clear].
- Field case: Trevor's 3-board attempt tripped the breaker after about 10 minutes. On an all-new 15 amp circuit, 2 boards ran fine at 1400w, but 3 boards went to 15-1600 and tripped [#8045 · 2025-12-01 · Trevor Bello] [#8066 · 2025-12-01 · Trevor Bello]. A 3-board S19 jPro on the APW12 120v mod shows a minimum of 944 watts in BraiinsOS [#8044 · 2025-12-01 · Travis Bitkle]. Running all 3 boards on a jpro at 110v would require going below 350mhz, and 2 boards probably give better efficiency [#8059 · 2025-12-01 · Karl] [#8046 · 2025-12-01 · Karl].
- A 120V hydro build had a usable range "from 500w to 1600w", which was described as a ton of useful range [#5791 · 2025-04-25 · Mark | @satstackingpleb] [#5793 · 2025-04-25 · Toine Heat Reuse].

### Path A: Loki board

- Background: S19 hashboards need I2C comms from the PSU. The Loki board fakes that input, so an APW3++ or another PSU that doesn't provide it can be used [#2332 · 2024-12-01 · Dev 🇳🇿] [#2333 · 2024-12-01 · Jonathan Y].
- An APW3 paired with a single S19 hashboard needs a Loki board, otherwise the control board will not start the hashboard [#1342 · 2024-10-08 · Zack Bomsta] [#1345 · 2024-10-08 · Jim ⚡️]. "Loki board is the way to go" for running an S19 at 120v [#1353 · 2024-10-08 · Trevor Bello].
- Working example: the "S9" PSU with a single S19 card and an S19 control board. For 12-14V operation, "all you need is the Loki chip" [#2338 · 2024-12-01 · Jonathan Y] [#2340 · 2024-12-01 · Karl].
- First-rig advice (BB control board + LuxOS + Loki kit): set up the control board before connecting hashboards, and confirm the UI works with the OS [#5545 · 2025-04-16 · Toine Heat Reuse] [#5548 · 2025-04-16 · Karl] [#5551 · 2025-04-16 · Nick]. The pivotalpleb.com file repo documents the configuration each firmware needs for Loki builds [#5554 · 2025-04-16 · Travis Bitkle]. Pivotal Pleb sells a Loki kit, and mine4heat sells enclosures [#4327 · 2025-02-27 · Josh].
- Control boards: the ePIC UMC V5 is compatible with the Loki Kit and was quoted at 150$ (October 2024) [#1721 · 2024-10-28 · Trevor Bello] [#1744 · 2024-10-28 · Trevor Bello]. One builder made a module that connects an S19x control board to an s9 power supply so the control board can modulate output voltage [#4488 · 2025-03-13 · Jim ⚡️].
- Single-board Braiins gotcha: Braiins power targets assume 3 hashboards, so "if you set it at 3kw then disable two HB it will run at 1kw. If you set it at 1kw, that board will run at 333w" [#2242 · 2024-11-29 · Cade]. This explains a single 120v card that was meant to be at full power around 1010watts but showed only 13-14th/s [#2223 · 2024-11-29 · Jonathan Y] [#2240 · 2024-11-29 · Jonathan Y].

### Path B: APW12 brown-out resistor mod (no Loki)

- How it works: resistors make the brown-out sensors think 240v is still coming in when the PSU only gets 120v [#2767 · 2024-12-15 · Karl] [#2771 · 2024-12-15 · Karl]. The mod is credited to Zack Bomsta [#6095 · 2025-05-23 · Travis Bitkle]. A Loki board is not needed when running the stock (modded) PSU [#5644 · 2025-04-21 · Toine Heat Reuse] [#5656 · 2025-04-21 · Travis].
- Why choose it: "no Loki necessary so it's technically a cheaper 120v mod. The resistors are almost free." On solar hashers it also replaces two apw3s with one PSU [#2776 · 2024-12-15 · Karl] [#2775 · 2024-12-15 · Karl].
- Cabling: the power cable cost about $14 (December 2024). If you bridge the two inputs on the apw12, you can use the same power cable as an apw3 [#2777 · 2024-12-15 · Karl].
- Going back to 240V: a modded APW12 can be plugged back into 220V without problems if the "1M ohm resistors" from the mod guide were used, and that value was chosen for this reason [#6099 · 2025-05-23 · Zack Bomsta]. This was corroborated in practice [#6097 · 2025-05-23 · Josh].
- Troubleshooting when hashboards fail at 120V but work at 240v: spinning PSU fans prove nothing. Check both the power and command wires to the control board, measure voltage on the hashboard bus at boot, suspect soldering that doesn't properly bypass the brown-out sensors, and verify resistor values and placement. Resetting tuning profiles and rebooting was also suggested [#5648 · 2025-04-21 · Toine Heat Reuse] [#5663 · 2025-04-21 · Travis] [#5670 · 2025-04-21 · Toine Heat Reuse] [#5676 · 2025-04-22 · Mark | @satstackingpleb] [#5679 · 2025-04-22 · Mark | @satstackingpleb] [#5700 · 2025-04-22 · Travis].
- Other single-board PSU options floated: an APW12 with the resistor mod, or a Mean Well LRS-600-12 [#8748 · 2026-01-20 · Travis Bitkle] [#8751 · 2026-01-20 · Cody Harris]. On 14v with a modified apw7, an 88-chip S19 board reached 27.5j [#8852 · 2026-01-23 · Karl].

### PSU fans at reduced load

- At about 1,300 watts (roughly 1/3 of the PSU rating), going from 3 PSU fans to one "checks out" [#8113 · 2025-12-02 · Travis Bitkle] [#8124 · 2025-12-03 · Karl].
- An 8 inch AC Infinity fan with a shroud adapter over the PSU lets you remove the PSU fans entirely [#2013 · 2024-11-17 · Eric Blockhouse] [#2020 · 2024-11-17 · Mark | @satstackingpleb] [#8116 · 2025-12-02 · Trevor Bello]. Swapping PSU fans for Noctuas allowed "1600w pull with no issues" [#2021 · 2024-11-17 · Mark | @satstackingpleb]. The apw3++ PSU fan can reportedly be swapped with just an adapter and no spoofer, because the control board isn't connected to the PSU fans (unconfirmed) [#2009 · 2024-11-17 · Trevor Bello] [#2015 · 2024-11-17 · Trevor Bello]. A 140mm APW12 fan adapter design is shared at github.com/jsorchik/apw12-140mm [#4885 · 2025-03-26 · Josh].

### Control boards: Mara

> **Status: Disputed** (Mara control board for Loki-style builds)
> Trevor's Mara board in a modified Loki rig left the boards unable to hash after two weeks ("Dont use it") [#7866 · 2025-11-23 · Karl] [#7867 · 2025-11-23 · Trevor Bello]. Karl later ran an 88-chip S19 board and a JPro board successfully on a Mara control board [#8825 · 2026-01-22 · Karl] [#8886 · 2026-01-26 · Karl]. Current best assessment: it works for some board types. The base S19 / S19 Pro is incompatible with the Mara control board [#8853 · 2026-01-23 · David Campos], and results with an apw7 are untested [#8859 · 2026-01-23 · David Campos].

MaraFW auto fan control works with only 2 fans [#8851 · 2026-01-23 · Karl]. The firmware throttles or shuts off before boards reach a dangerous temperature [#8884 · 2026-01-26 · Karl].

### 120V field data (dated)

| Build | Result | Anchor |
|---|---|---|
| Compact 3D-printed Loki rig, Noctua fans | 650-850w of heat, tuned for efficiency | [#514 · 2024-08-09 · Mark \| @satstackingpleb] |
| Single S19j board on 120v, underclocked | around 23j/t | [#603 · 2024-08-10 · Jonathan Y] [#620 · 2024-08-10 · Jonathan Y] |
| 88-chip S19 board, Mara control board, 110v | 28j | [#8825 · 2026-01-22 · Karl] |
| Single jpro board, 110v, 2 arctic p12 pro 3k rpm fans | 25.5j at the wall; temps averaged 44c, chip temp 65c | [#8886 · 2026-01-26 · Karl] [#8888 · 2026-01-26 · Karl] [#8889 · 2026-01-26 · Karl] |
| RV heated by two S19s (one single-board, one double-board) on 120V APW12s, LuxOS | about 27 J/Th; no propane needed yet in single-digit temps | [#8154 · 2025-12-05 · Heatpunk Forum] |
| Altair BitChimney with a used JPro 104T board | 1,220 at the wall, "33+ w/th" | [#8905 · 2026-01-28 · Barnminer Barnmyna] [#8913 · 2026-01-28 · Barnminer Barnmyna] |
| BitChimney with a T21 board | steady 48th, heats a 625sqft room | [#8906 · 2026-01-28 · Joe C] |

Other designs and guides: a single-board S19 case for the APW3 PSU on MakerWorld (makerworld.com/en/models/375862) [#1322 · 2024-10-08 · Jonathan Y]; Attakaï's single S19 board with an S9 power supply and 8 fans on LuxorOS [#1312 · 2024-10-08 · Jim ⚡️]; the HeatJack S19 Loki space heater build guide, written for an office using 900 - 1500W of heat a day [#8995 · 2026-02-02 · Heatpunk Forum]; and a DIY portable 120V hydro miner built for about $350 in hydro block, pump, fittings and plate exchanger (December 2025) [#8260 · 2025-12-11 · Josh]. Canaan's 120v home miner was seen as following the 120v heat-miner builds the community was already doing [#5763 · 2025-04-24 · Travis Bitkle].

## Three-phase, 208V and transformers

- **Know your service.** A "208V three phase" building service is typically 120v per leg (hot to neutral), with legs 120 degrees apart and 208v line to line [#8159 · 2025-12-05 · Travis Bitkle]. The cheese-plant site had 208Y120 three phase, but 415Y240 was needed, and its first hash came online on 120v [#190 · 2024-08-02 · Travis Bitkle] [#1535 · 2024-10-12 · Travis Bitkle].
- **What the machines want.** Bitmain hydro specs call for 380V-415v 3 PH (220v-240v per leg). The power cord has four wires (three hot legs plus ground), so delta may work, but verify the voltage per leg. One operator runs about 250v per leg [#4430 · 2025-03-06 · Travis Bitkle] [#4431 · 2025-03-06 · Travis Bitkle]. The expected standard is between 240v and 277v per leg. Single-phase machines can run on 277 but are technically not rated above 250v [#8163 · 2025-12-05 · Travis Bitkle]. Some PSUs accept up to 277v, and a 3-phase 208v site can tap higher to get close to 220v [#410 · 2024-08-04 · Colin Sullivan] [#412 · 2024-08-04 · Colin Sullivan].
- **Step-up transformers.** Travis's conclusion: "if you want to power Antminer hydros, you'll need a step up transformer so far as I can tell" [#8161 · 2025-12-05 · Travis Bitkle]. In March 2025, one 120v-per-leg site installed a step-up 208 delta to 440Y260 transformer [#4440 · 2025-03-07 · Travis Bitkle]. By December 2025, Travis was using a 208 Delta to 480Y277 step-up transformer tapped down to about 250v per leg to feed the PDUs and the hydro machine. He sees about 260v per leg at no load and 245v-250v under full load [#8159 · 2025-12-05 · Travis Bitkle] [#8163 · 2025-12-05 · Travis Bitkle].
- **Taps, refurbs and chaining.** Most transformers have multiple taps to fine-tune voltage by +/-15%, and refurbished units were found for about 40% less than new [#4445 · 2025-03-07 · Travis Bitkle] [#4447 · 2025-03-07 · Travis Bitkle]. Avoid chaining step-down and step-up transformers, because each transformation loses efficiency to impedance losses [#4453 · 2025-03-07 · Travis Bitkle]. A Canadian site with 600/347 input considered taps or a step-down to 440 [#4444 · 2025-03-07 · The schnauze] [#4446 · 2025-03-07 · The schnauze].
- **Single-phase availability.** Out-of-box single-phase 220 immersion miners were believed to be only the Canaan 1466 and Auradine models, and an S21 immersion unit is three phase, "bunk for residential" [#2100 · 2024-11-21 · Dane O]. No single-phase Antminer hydros exist for the US market [#7002 · 2025-08-12 · Tyler Stevens]. As far as anyone knew, only single-phase M64s exist [#6748 · 2025-07-07 · Dev 🇳🇿]. The Heat Core HS05 and RY3T Mini are "30 Amp, 220 V" and were wired with a standard L6-30 receptacle [#6970 · 2025-08-11 · Heatpunk Forum].
- **Untested workaround.** One idea for running an Antminer hydro on single phase is to power it with two APW9s, which produce voltages similar to the hydro 3-phase PSUs, possibly on 120v if underclocked and maybe with a Loki kit [#8469 · 2025-12-29 · Travis Bitkle] [#8473 · 2025-12-29 · Karl].

## Solar-direct and DC hashing

- Karl's approach is to let the PSU regulate voltage and tie into the "grid" to cover clouds. His own setup is a 24v battery bank and inverter [#2322 · 2024-12-01 · Karl]. Wiring the charge controller directly to the PSU lets the grid bridge cloud gaps without batteries or capacitors. He believes it would work with a Loki rig but hadn't tried it on anything valuable [#2795 · 2024-12-16 · Karl] [#2797 · 2024-12-16 · Karl]. He thinks the charge voltage must be set higher than the PSU's output so they match, and he had not tried it with an apw12 [#2801 · 2024-12-16 · Karl].
- One solar-powered heater fed the battery 12A and sent the rest to the miner, averaging 17TH while charging [#1330 · 2024-10-08 · Mark | @satstackingpleb] [#1334 · 2024-10-08 · Mark | @satstackingpleb].
- Solar mining suits anywhere without 1-1 net metering. Miners reading a CT meter can match the output being exported to the grid [#3013 · 2024-12-31 · Dane O] [#3014 · 2024-12-31 · Dane O]. CT clamps on the back feed can tune miners to absorb surplus [#8378 · 2025-12-22 · Dane O], and in Mossel Bay, miners running hass-miner through Home Assistant respond to inverter battery charge levels [#8556 · 2026-01-06 · Jason].
- S9 and L3 machines "still have room to shine this cycle" when supplemented with solar [#2332 · 2024-12-01 · Dev 🇳🇿]. Most Loki and home-heater owners were "letting them rip" through summer, mostly on solar [#6093 · 2025-05-23 · Karl].
- Off-grid example (July 2026): an El Salvador plan with 17kWp of solar and a 12kW inverter running old miners during the solar day, aimed at replacing 5000W electric shower-head heaters in hospitality venues [#10345 · 2026-07-21 · Jake #️⃣ Hashpower Academy 🎓].

## See Also

- [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md)
- [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- [Whatsminer M64 Hydro Heaters](whatsminer-m64-hydro-heaters.md)
- [Immersion Heat Reuse](immersion-heat-reuse.md)
- [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- [Heater Firmware & Power Control](../firmware/heater-firmware-and-power-control.md)
- [Home Assistant Heater Control](../mining-software/home-assistant-heater-control.md)
- [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)
- [Hashrate Heating Products & Installs](../industry/hashrate-heating-products-and-installs.md)
- [Repair, Supply & Vendors](../industry/repair-supply-and-vendors.md)
- [Community Workshop Wisdom](../getting-started/community-workshop-wisdom.md)
