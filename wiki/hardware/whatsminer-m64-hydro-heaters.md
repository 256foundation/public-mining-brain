# Whatsminer M64-Family Hydro Heaters

> Sources: Hashrate Heatpunks Telegram group, 2024-08-02 → 2026-10-08
> Raw: [Hashrate Heatpunks Telegram signal digest](../../raw/economics/2026-10-09-heatpunks-telegram-signal.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

The MicroBT Whatsminer M64 Hydro became the default heating core for Hashrate Heatpunks builders who wanted water-cooled hashrate on residential power. As far as the group knows it is single-phase only, and its rated water outlet temperature is high enough to drive hydronic loads directly [#662 · 2024-08-19 · Tyler Stevens] [#6748 · 2025-07-07 · Dev 🇳🇿]. Several products are built around it:

- the Heat Core HS05 "hydro rack"
- the RY3T Mini boiler
- Hashrate House's hydro system and Dane O's later Aqueon water-heater retrofit
- DIY loops such as Travis Bitkle's water heater and Britton's furnace-plenum install

The later M64S and M74 keep the same form factor with newer chips. Three caveats run through every build:

- **Control.** Stock firmware offers coarse power modes and slow re-tuning, so dynamic power control is still a struggle.
- **Corrosion.** The water blocks are aluminum, so loop chemistry and galvanic isolation matter.
- **Supply.** Supply depends on MicroBT and Heat Core, with minimum order quantities, and there is worry that single-phase hydro could be discontinued.

General hydronic design (loops, heat exchangers, dry coolers, chemistry) is in [Hydronic Heat Reuse](hydronic-heat-reuse.md).

## Builder rules of thumb

- **Isolate the M64 with a heat exchanger.** Building heating water carries dirt and oxygen [#6842 · 2025-07-25 · Christian Naef] [#6845 · 2025-07-26 · Christian Naef]. Because the M64's cooling plates are aluminum, they "would be the first to go" in a mixed-metal loop, risking pinhole leaks [#6856 · 2025-07-29 · Dane O]. An HX plus two pumps also gives you "Two knobs to turn" for temperature control [#6864 · 2025-07-29 · Tyler Stevens].
- **Don't feed it to a water heater alone.** One M64 is a lot of power for just a hot water heater and will cycle on and off heavily. Tie it into forced air or a radiant slab as well [#8370 · 2025-12-22 · Dane O].
- **Plan for heat leaking into the room.** Radiation from PEX and the M64 itself overheated one basement [#7603 · 2025-11-07 · Travis Bitkle].
- **Budget for control work.** Even with the API, every power-limit change triggers a re-tune that takes minutes (see [Power control, firmware and API](#power-control-firmware-and-api)).
- **Ramp rate beats tuning quality for heating.** The goal is to match miner wattage to heating demand. Reaching the power target faster than the miner can tune for optimal hashrate is acceptable [#6999 · 2025-08-12 · Tyler Stevens].

## Specifications (as reported)

| Item | Value | Anchor |
|---|---|---|
| PSU | Single phase | [#662 · 2024-08-19 · Tyler Stevens] [#6748 · 2025-07-07 · Dev 🇳🇿] |
| Rated water outlet | 80 C / 176 F | [#662 · 2024-08-19 · Tyler Stevens] |
| Flow requirement | 3.5l/min | [#681 · 2024-08-19 · Dane O] |
| Power | "around a 4kw machine" (19.9j x 200Th, about 4kw not 5) | [#9656 · 2026-03-13 · Travis Bitkle] |
| Normal-mode heat | 4000 Watts (normal mode M64) | [#7876 · 2025-11-23 · Tyler Stevens] |
| Water blocks | Aluminum; hashboards never touch the water | [#9231 · 2026-02-20 · Tyler Stevens] [#9300 · 2026-02-22 · Travis Bitkle] |
| Port threads | 1/4-inch BSPP on the miner itself | [#9316 · 2026-02-23 · Travis Bitkle] |
| Electrical (in HS05 / RY3T Mini) | 30 Amp, 220 V, wired to a standard L6-30 receptacle | [#6970 · 2025-08-11 · Heatpunk Forum] |
| Power modes | Commonly described as High, Med, Low | [#5358 · 2025-04-08 · Tyler Stevens] [#6983 · 2025-08-12 · Heatpunk Forum] |

- **Flow sizing.** Bob ran SWEP SSP for a single M64 with margin, using 75C instead of 80C. It gave around 1/2 gal/min at around 71C. That is low, and he would not go lower on flow. The high outlet temperature "really expands the design space" [#692 · 2024-08-19 · Bob].
- **Overclock claims (unverified).** The Winchain contact showed a Russian crew getting 97c outlet temps on an M64 clocked to 6000w on the stock PSU [#6324 · 2025-05-31 · Dane O]. A later source claimed up to 6000w with custom firmware and the right wiring, at temps almost at 100c; Dane had not tested it [#9660 · 2026-03-13 · Dane O].
- **Newer chips run hotter.** Water output from new Whatsminer chips "can reach 70C aparently" [#4802 · 2025-03-23 · Dev 🇳🇿]. Whatsminer junction temperatures run somewhat higher than other ASICs but stay within a PCB-compatible range [#9583 · 2026-03-10 · Aadhi M].

> **Status: Disputed**
> Rated power. Some spec summaries treat the M64 as a ~5 kW unit; HeatCore units were called "5kw HeatCore Units" [#4807 · 2025-03-23 · Cody Harris]. Travis Bitkle corrected a spec post: "19.9j x 200Th is about 4kw not 5" [#9656 · 2026-03-13 · Travis Bitkle]. Field data at normal mode was 4000 Watts [#7876 · 2025-11-23 · Tyler Stevens]. Best assessment as of 2026-10-09: plan around ~4 kW in normal mode, with headroom that some claim reaches 6000w on modified firmware.

## Plumbing, fittings and coolant

- **Missing connectors.** One M64 arrived without its stock connectors. The working substitute was a Festo 9396 AD-G1/4-1/4 npt I adapter, McMaster-Carr part number 1527N22 [#5958 · 2025-05-10 · Dane O] [#5961 · 2025-05-10 · Elijah Sanders].
- **Coolant.** The first Heat Core NS200 system with a WhatsMiner M65S was commissioned on ~35% propylene glycol + demineralized water. Whatsminer's documentation calls for a composite corrosion inhibitor from Peric, dosed in wt%, but gives no clear product name or EU source [#9089 · 2026-02-11 · Heatpunk Forum]. A heating distributor said some boiler makers require such additives to keep the heat exchanger under warranty. He did not recognize the HeatCore brand [#9133 · 2026-02-12 · Deleted Account] [#9134 · 2026-02-12 · Deleted Account].
- **Adding inhibitor** [#9243 · 2026-02-20 · Travis Bitkle]:
  1. Stop the miner and bleed down the system pressure.
  2. Pour in a few ounces of inhibitor.
  3. Recharge to the starting cold pressure.
  4. Run the pumps to clear air.
  5. Power the miner back on.
- **Mixed-metal test.** Travis runs his M64 in a loop with copper, cast iron, brass and stainless and no HX isolation, as a deliberate long-term test [#6862 · 2025-07-29 · Travis Bitkle]. Filling it with remineralized RO water dissolved copper into the loop for the first couple of days. A flush and refill with filtered softened water plus some treatment fixed it, with no damage he could see [#6876 · 2025-07-29 · Travis Bitkle] [#6880 · 2025-07-29 · Travis Bitkle] [#6901 · 2025-07-30 · Travis Bitkle].
- **Long-life HX.** Hashrate House built a custom nickel-brazed 316 SS plate heat exchanger for its M64 integration, aiming for boiler-like lifetime [#8383 · 2025-12-22 · Dane O].
- **Temperature limits.** Hydro miners can shut down when the inlet-to-outlet delta gets too large [#6740 · 2025-07-07 · Pat Kelly | Fog Hashing - Director of Sales, Global]. A slug of 115F water hitting a miner holding 170F water threw an error code, which is why Travis moved to a primary/secondary loop [#6408 · 2025-06-07 · Travis Bitkle] [#6410 · 2025-06-07 · Travis Bitkle].

## Power control, firmware and API

**What the stock firmware offers.**

- **Modes.** Elijah Sanders used the easy low power mode and knew of a high power mode [#5367 · 2025-04-08 · Elijah Sanders]. The M64 is widely believed to offer only "[High, Med, Low]". But the API has a variable for a custom power limit, and the Heat Core team said dynamic power adjustment is possible [#6983 · 2025-08-12 · Heatpunk Forum].
- **API power set.** Earlier, Sam found that MBT API v3.0.0 has a power-set function that adjusts dynamically. That is useful for tracking PV production without rebooting [#5257 · 2025-04-02 · Sam] [#5288 · 2025-04-03 · Sam].
- **Re-tune cost.** A Whatsminer power limit can be set externally, for example with Foreman, but the miner always re-tunes after a change [#6989 · 2025-08-12 · Jarno]. "Adjust Upfreq Speed" makes tuning faster but still takes minutes, and the reached power fluctuates a bit [#6997 · 2025-08-12 · Jarno]. "Power Fast Boot" ramps faster and is aimed at curtailment for bigger players [#7000 · 2025-08-12 · Jarno]. Tyler said WM tuning time "seems to kill the point" of the feature heaters need [#6993 · 2025-08-12 · Tyler Stevens].
- **API access.** Full API access requires dealing with the Whatsminer password setting [#6995 · 2025-08-12 · Jarno]. pyasic's btminer RPC code was pointed to as the command reference [#6996 · 2025-08-12 · Brett Rowan].

**How integration evolved.**

- **August 2025.** The M64 did not react to hass-miner mode-change commands (low, normal, high) [#7006 · 2025-08-12 · Dylan Seib].
- **November 2025.** The M64 initially didn't work with PyASIC [#7668 · 2025-11-13 · Tyler Stevens]. Through hass-miner it then "mostly works": all sensors populated except one board, but commands still failed, and generating the API key was the blocker [#7780 · 2025-11-16 · Dylan Seib]. Travis got a Whatsminer working in Home Assistant by talking to the miner API directly, with a schedule [#7845 · 2025-11-22 · Travis Bitkle] [#7880 · 2025-11-23 · Travis Bitkle]. The heatpunks forum keeps a Whatsminer API documentation thread [#7885 · 2025-11-23 · Tyler Stevens].
- **December 2025.** Travis's intuition is that air-cooled Whatsminers dislike power scaling the way Antminers on Braiins DPS tolerate it. The M64's upfreq time is shorter than on his air-cooled units [#8076 · 2025-12-02 · Travis Bitkle] [#8080 · 2025-12-02 · Travis Bitkle].
- **Simplest working control (late 2025).** Exergy's furnace-buddy HS05 uses a 240V wifi relay switch for on/off, paired in Home Assistant with a Venstar T7900 local-API thermostat [#7877 · 2025-11-23 · Tyler Stevens].

**Aftermarket firmware.** Dane O called control "a major hurdle" unless an "unlocked firmware" for Whatsminer becomes available [#6324 · 2025-05-31 · Dane O]. Whatsminer is significantly harder than Antminer to reverse engineer [#5622 · 2025-04-18 · Skot Bitaxe]. Porting open firmware such as Mujina is "Much harder on any miner that doesn’t already have aftermarket firmware" [#10230 · 2026-06-10 · Tyler Stevens] [#10234 · 2026-06-10 · Brett Rowan].

**The missing combination.** As of August 2025, no single package offered "Single phase, high water temp, BraiinsOS DPS all together" [#7013 · 2025-08-12 · Travis Bitkle]. No single-phase Antminer hydros exist for the US market. Auradine seems to have power ramping solved but has no 220 V hydros either [#7002 · 2025-08-12 · Tyler Stevens] [#7003 · 2025-08-12 · Tyler Stevens].

## Products built on the M64

### Heat Core HS05 (and NS200 / HS20)

- **What it is.** The HS05 is a single-miner "hydro rack" for liquid heating, with a heat exchanger at the rear for hydronic loads such as radiant floor, pool or hot tub [#7896 · 2025-11-23 · Heatpunk Forum]. Spec: Manufacturer Heat Core, Model HS05, Miner Compatibility M64, Power "Single Phase. 30A, 220V" [#6974 · 2025-08-11 · Heatpunk Forum].
- **Dry cooler.** Its dry cooler is plumbed in series, which makes a convenient summer and solar heat dump. It shipped with 50ft extension tubes and wiring, so no customization was needed [#7165 · 2025-08-23 · Tyler Stevens]. The cooler turns on at a temperature threshold set on the HS05's controller [#8460 · 2025-12-26 · Britton].
- **Related units.** Heat Core also makes the NS200, the first of which was commissioned with an M65S [#9089 · 2026-02-11 · Heatpunk Forum], and an HS20 that was on one Finnish shortlist [#6516 · 2025-06-23 · Jarno].
- **Dry cooler requirement (unconfirmed).** In March 2025 Tyler understood, from a call he flagged as uncertain because of a language barrier, that HeatCore products require a dry cooler to bleed heat outside. He argued that residential marketing would be misleading if so [#5052 · 2025-03-28 · Tyler Stevens] [#5057 · 2025-03-28 · Tyler Stevens].

> **Status: Disputed**
> Is the HS05 a heating product? Elijah Sanders criticized its "giant unnecessary extra power source" and an attached radiator that forces the machine outside [#6318 · 2025-05-31 · Elijah Sanders]. Christian Naef (RY3T) said a near-identical unit his team tested is "a mining unit, not a heating product", with pipes too small and the heat exchanger "far too small" [#6334 · 2025-06-01 · Christian Naef]. Dane O called the built-in dump useful for a few localities but wants it optional [#6324 · 2025-05-31 · Dane O]. A European wholesaler later called the HS05 "a questionable choice" against heat pumps [#7971 · 2025-11-25 · Bas | Mining Wholesale 🇳🇱]. On the other side, Exergy and Britton both report it working well in forced-air installs (see [Field installs](#field-installs)). Best assessment as of 2026-10-09: it works as a plug-and-play heat source when paired with a building-side exchanger, and the integrated dry cooler is a feature only where heat dumping makes sense.

### RY3T Mini

- **Earlier RY3T systems.** RY3T (Switzerland) began with immersion boilers holding 1 to 2 Whatsminers of the M56 to M66 series [#1242 · 2024-10-01 · Christian Naef], or one to two M56-series miners at 7-14kw [#2467 · 2024-12-04 · Christian Naef].
- **The Mini.** The Mini is M64-based and was built in partnership with Winchain: RY3T brings the heating expertise, Winchain the mining-infrastructure engineering [#6336 · 2025-06-01 · Christian Naef].
- **Positioning.** It works out of the box, carries a warranty, is installed by professional plumbers, and lets the owner choose their own pool [#6334 · 2025-06-01 · Christian Naef].
- **First US unit.** The first US RY3T Mini was driven from Las Vegas to Denver to heat The Space [#6294 · 2025-05-31 · Christian Naef]. Like the HS05 it is 30 Amp, 220 V [#6970 · 2025-08-11 · Heatpunk Forum].

### Hashrate House hydro system and Aqueon

- **Hydro system (June 2025).** Hashrate House finished R&D on its first hydro system: an M64 heating domestic hot water plus another loop, plug-and-play [#6621 · 2025-06-27 · Dane O].
- **Aqueon (June 2026).** The Aqueon is a DHW water-heater retrofit for m54-64-74 series miners. It has a custom controller with a locally hosted web interface and 2 heat exchangers, with DHW as primary and furnace, radiant floor or heat dump as secondary [#10283 · 2026-06-24 · Dane O].
- **Aqueon plumbing.**
  - 3/4-inch push-connect fittings on both loops [#10286 · 2026-06-24 · Dane O].
  - It answers a standard 24vac thermostat call once the water heater is satisfied [#10286 · 2026-06-24 · Dane O].
  - It circulates through an existing DHW recirculation system or a short stainless or brass pump loop [#10291 · 2026-06-25 · Dane O].
- **Monitoring.** A later controller update added heating and profit tabs and a "heat capture efficiency" metric to flag HX fouling or a failing pump [#10313 · 2026-07-09 · Dane O].

## Supply, prices and MOQ (dated)

All prices are as quoted in the chat on the anchor date. They are volatile and exclude local tariffs unless stated.

| Date | Model | Quote | Anchor |
|---|---|---|---|
| Apr 2025 | M64 | Sold out; next batch in June might be around $14/T | [#5271 · 2025-04-02 · Dev 🇳🇿] |
| Sep 2025 | M64 | $2700 delivered | [#7367 · 2025-09-21 · Elijah Sanders] |
| Nov 2025 | M64S | 220T, 18j/th, $2680 + shipping from HK | [#7922 · 2025-11-24 · Elijah Sanders] |
| Mar 2026 | M74 (per Heat Core) | ~240 TH at 3500 Watts; ~325 TH at 5000 Watts; MOQ 60, no spec sheet | [#9527 · 2026-03-05 · Tyler Stevens] [#9528 · 2026-03-05 · Tyler Stevens] |
| Mar 2026 | M74 | 14.5j/TH (MicroBT contacts) | [#9536 · 2026-03-06 · Colin Sullivan] |
| Mar 2026 | M74 275T | $14.5/T, split of an MOQ 50, 2 month lead time, 50% down on 5+ units | [#9624 · 2026-03-12 · Travis Bitkle] [#9625 · 2026-03-12 · Travis Bitkle] |
| Mar 2026 | M74 275T (single phase) | USD10.7/T, MOQ 50pcs, 2.5-3 month future batch | [#9648 · 2026-03-13 · Dev 🇳🇿] |
| Mar 2026 | M74 275T | USD10.4/T | [#9682 · 2026-03-16 · Dev 🇳🇿] |

- **May 2025 M64 quote.** Around 2.5 k delivered, depending on tariffs [#6322 · 2025-05-31 · Pat Kelly | Fog Hashing - Director of Sales, Global].
- **Heater unit prices.** In March 2025 the 5 kW HeatCore units were said to be "like $6000" [#4807 · 2025-03-23 · Cody Harris]. At Bitcoin 2025 (May) the Heat Core unit was quoted at $1500 with a radiator attached, while another boiler unit reportedly retailed for $9,000 [#6316 · 2025-05-31 · Elijah Sanders]. These may be different products or configurations. Treat both as anecdotal.
- **M74 form factor.** Per Heat Core, the M74 keeps the same form factor and firmware as the M64 with "No new features" [#9527 · 2026-03-05 · Tyler Stevens]. Others describe it the same way: M64 shape, different chips, 3 months delivery after the order is confirmed [#9640 · 2026-03-12 · Dan Sokil] [#9641 · 2026-03-12 · Dan Sokil]. Exergy was told the M74 fits the HS05 but treats that as unconfirmed ("we have been told a lot of things") [#9627 · 2026-03-12 · Mike Clear] [#9632 · 2026-03-12 · Travis Bitkle].
- **No-MOQ seller.** Billion Bison was reported to have no MOQ, a 30% deposit and a 45-60 day lead time [#9628 · 2026-03-12 · Joe C].
- **Discontinuation risk.** In December 2025 Tyler worried that the only single-phase hydro miner might be discontinued. Dev reported that Dr Yang would make one if asked, while someone else said the maker isn't confident it can produce a stable single-phase product in this form [#8190 · 2025-12-08 · Tyler Stevens] [#8201 · 2025-12-08 · Dev 🇳🇿]. Tyler's preference order for commercial work is Auradine AH3880s, then M63, then M64 single phase as the worst case, and he wants hydro and U form-factor standards [#8162 · 2025-12-05 · Tyler Stevens].
- **Parts.** After a likely lightning loss of an M64, Zeusbtc's Whatsminer parts page was recommended as a reliable PSU and parts source even though "Site looks sketchy" [#10383 · 2026-07-28 · Travis Bitkle] [#10385 · 2026-07-28 · Brett Rowan].
- **Certification.** Elijah Sanders set out to get the M64 a US safety certification [#7236 · 2025-09-02 · Elijah Sanders]. He later held off on a UL rating for the M64S: a decline would leave no path to improve it and would put the M64 "on the radar" [#9178 · 2026-02-15 · Elijah Sanders] [#9181 · 2026-02-15 · Elijah Sanders].
- **Fog Hashing.** Fog Hashing had no current priority on small (5-50 kW) units to compete with Heat Core's [#6721 · 2025-07-05 · Tyler Stevens] [#6722 · 2025-07-05 · Pat Kelly | Fog Hashing - Director of Sales, Global].

## Economics snapshots (dated)

- **May 2025.** "$28/month to run an M64" versus "$300/month at today's hashprice", from one member's example [#5975 · 2025-05-12 · Elijah Sanders].
- **December 2025.** At <10 cent power and a hashprice of 0.037 $/TH/s/day, an M64 has a COP of ~ 7.5 [#8276 · 2025-12-15 · Tyler Stevens].

Full models are in [Hashrate Heating Economics](../economics/hashrate-heating-economics.md).

## Field installs

- **The Space radiant floor (2025).** Exergy and The Space received an RY3T Mini and a Heat Core HS05 to test in a radiant floor system [#6446 · 2025-06-10 · Heatpunk Forum]. The install was finished with hired professional plumbers after taking longer than expected [#6973 · 2025-08-11 · Heatpunk Forum].
- **Exergy "furnace buddy" (November 2025).** An HS05 supplies "buddy" heat to a natural gas furnace [#7875 · 2025-11-23 · Tyler Stevens]. With only the furnace circulator fan running (no flame), the airflow pulled 4000 Watts of heat off the dry cooler, and the cooler's own fans never had to turn on [#7876 · 2025-11-23 · Tyler Stevens]. The open question is whether cutting into the return just before the furnace starves the other returns in the house [#7878 · 2025-11-23 · Tyler Stevens].
- **Britton's plenum build (October to December 2025).** In October Britton estimated that 1000cfm through a plenum HX with 176F water and 60F inlet air gives about 128F outlet air, with the 120F–130 return available to a sidearm DHW exchanger [#7390 · 2025-10-06 · Britton]. By December his M64 Hydro in an HS05 chassis was working well with a water-to-air HX in the furnace plenum [#8458 · 2025-12-26 · Britton]. The circulator is on a smart plug so he can stop flow, and the dry cooler then kicks in at the HS05 threshold [#8460 · 2025-12-26 · Britton]. In winter the house absorbs everything. His spring plan is to move the dry cooler to the garage and add a valve plus a sidearm HX on the DHW heater [#8461 · 2025-12-26 · Britton].
- **Travis's water heater and garage loop (2025).** He uses primary/secondary pumping so DHW stays at 120°F rather than 170°F, with no HX [#6869 · 2025-07-29 · Travis Bitkle]. Design details are in [Hydronic Heat Reuse](hydronic-heat-reuse.md#primarysecondary-loops-avoiding-temperature-shock).
- **Finnish geothermal plan (June 2025).** The plan is a hydro miner (HS20 or HS05 shortlisted) feeding DHW, then radiators, then the heat pump's intake, with excess heat going into the geothermal wells [#6516 · 2025-06-23 · Jarno].

## Contradictions & Open Questions

- Whether the M74 drops into an HS05 unchanged. Exergy says it was told yes but has not confirmed [#9627 · 2026-03-12 · Mike Clear].
- Whether the stock firmware's API power limit can track heating demand fast enough. The re-tune is measured in minutes [#6997 · 2025-08-12 · Jarno].
- Whether single-phase hydro Whatsminers will keep being produced [#8190 · 2025-12-08 · Tyler Stevens] [#8201 · 2025-12-08 · Dev 🇳🇿].
- Which corrosion inhibitor product meets the Whatsminer documentation outside China [#9089 · 2026-02-11 · Heatpunk Forum].

## See Also

- Same topic: [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- Same topic: [Immersion Heat Reuse](immersion-heat-reuse.md)
- Same topic: [Heater Electrical and 120V Builds](heater-electrical-and-120v-builds.md)
- Same topic: [ASIC Thermals and Heat Reuse](asic-thermals-and-heat-reuse.md)
- Firmware: [Heater Firmware and Power Control](../firmware/heater-firmware-and-power-control.md)
- Firmware: [Mujina](../firmware/mujina.md)
- Software: [Home Assistant Heater Control](../mining-software/home-assistant-heater-control.md)
- Software: [asic-rs](../mining-software/asic-rs.md)
- Economics: [Hashrate Heating Economics](../economics/hashrate-heating-economics.md)
- Industry: [Hashrate Heating Products and Installs](../industry/hashrate-heating-products-and-installs.md)
- Industry: [Repair, Supply and Vendors](../industry/repair-supply-and-vendors.md)
- History: [Heatpunks Community Timeline](../history/heatpunks-community-timeline.md)
