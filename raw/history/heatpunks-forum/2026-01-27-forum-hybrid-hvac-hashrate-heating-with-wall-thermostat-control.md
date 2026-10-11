# Hybrid HVAC Hashrate Heating with Wall Thermostat Control

> Source: https://forum.heatpunks.org/t/hybrid-hvac-hashrate-heating-with-wall-thermostat-control/243
> Collected: 2026-10-10
> Published: 2026-01-27
> Registry ID: heatpunks-forum

tylerkstevens | 2026-01-27 14:25:38 UTC | #1

All,

Sharing how @tronsington and I have solved hybrid HVAC hashrate heating at the @Exergy office, with working connections to the default wall thermostats.

[![Screenshot 2026-01-27 at 07.02.45](https://forum.heatpunks.org/uploads/default/optimized/1X/b7844940aaf15383ef63e29627719d7c019c34ea_2_690x488.jpeg)Screenshot 2026-01-27 at 07.02.452140×1516 221 KB](https://forum.heatpunks.org/uploads/default/original/1X/b7844940aaf15383ef63e29627719d7c019c34ea.jpeg)

# What we Did:

Wirelessly connected our Canaan Avalon Q to “Stage 1” of our Venstar T7900 wall thermostat via Home Assistant (via @Exergy integration). Thermostat “Stage 2” has physical wire to furnace.

[![IMG_1964.HEIC](https://forum.heatpunks.org/uploads/default/optimized/1X/e7ae6f46d6ca440f5690cb4d2728153e87bce7b7_2_666x500.jpeg)IMG_1964.HEIC4032×3024 2.11 MB](https://forum.heatpunks.org/uploads/default/original/1X/e7ae6f46d6ca440f5690cb4d2728153e87bce7b7.jpeg)

# Logic:

When heat is called, turn on miner + circulation fan. If can’t hit desired room temp in 15 min → turn on gas flame for help.

Might tweak these parameters for performance sake.

# Result:

Our upstairs HVAC system has earned > $300 of BTC, and kept our space warm with 99% of heating time from the miner. Only 1% of the time has the gas kicked on to help.

# Takeaway:

- Cheaper Heat (solar + cheap power + btc rev)

- Less Emissions (gas rarely runs)

- Seamless integration (control off wall thermostat)

# Cost:

- $1900 Bitcoin Miner

- $200 Home Assistant raspberry pi setup

- $200 Thermostat with local API endpoints

- $50 of HVAC and mounting materials

[![IMG_1401](https://forum.heatpunks.org/uploads/default/optimized/1X/91ce76093e4244af5115729d91d665fcf73dd78c_2_666x500.jpeg)IMG_14011920×1440 323 KB](https://forum.heatpunks.org/uploads/default/original/1X/91ce76093e4244af5115729d91d665fcf73dd78c.jpeg)

# Documentation

All of the hardware and software required to do this is documented.

[Exergy Documentation](https://docs.exergyheat.com)

### [Introduction - Exergy Docs - Exergy Documentation](https://docs.exergyheat.com)

Documentation for Exergy heating system upgrades and bitcoin mining powered smart home solutions.

# Calculators to Estimate Savings

If you’re curious if this makes sense for you, check out our calculators.

[calc.exergyheat.com](https://calc.exergyheat.com)

### [Hashrate Heat Calculator - Home Heating with Bitcoin Miners](https://calc.exergyheat.com)

Calculate various economic metrics to evaluate if bitcoin mining powered heat can subsidize your heating bills.

# Support from Exergy on our Home Assistant Software

If you want to tackle this yourself and need some help with our software and automation logic, reach out to us on our support forum.

[Exergy Support](https://support.exergyheat.com)

### [Exergy Support](https://support.exergyheat.com)

Support for Exergy Systems and Services
