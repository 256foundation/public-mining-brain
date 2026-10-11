# Heat Core HS05 Furnace Buddy System (M64)

> Source: https://forum.heatpunks.org/t/heat-core-hs05-furnace-buddy-system-m64/222
> Collected: 2026-10-10
> Published: 2025-11-23
> Registry ID: heatpunks-forum

tylerkstevens | 2025-11-23 23:46:08 UTC | #1

Howdy,

Wanted to showcase what we’ve done for our first HVAC hashrate heating system that uses a hydro-cooled bitcoin miner (Whatsminer M64).

The HS05 single miner “hydro rack” is intended for liquid heating (water cooling of the miner). It has a heat exchanger at the rear where you can hookup to various hydronic applications (radiant floor, pool, hot tub, etc…).

However, instead of controlling the miner power up and down to prevent overheating if the liquid loop doesn’t take the heat, it has an integrated “dry cooler”, aka radiator to bleed off any excess heat that the liquid loop does not take.

We took advantage of this to do HVAC heating with a water cooled miner.

[![IMG_3105](https://forum.heatpunks.org/uploads/default/optimized/1X/c663bec1af4038b8bf083667f4238aef5df23253_2_666x500.jpeg)IMG_31051600×1200 204 KB](https://forum.heatpunks.org/uploads/default/original/1X/c663bec1af4038b8bf083667f4238aef5df23253.jpeg)

Simply don’t connect anything to the heat exchanger, and all the heat must be dumped out of the radiator.

We took advantage of this by connecting the radiator (it can separate from the miner rack “boiler” with up to 50 feet of extra tubing) directly to the HVAC duct, right before the furnace.

In this way, we are “leaking” heat from the miner into the HVAC duct right before the furnace. Turning on the furnace circulator fan (not flame for heating mode), pulls air through the miner dry cooler and pushes the heated air around the house.

We haven’t had the dry cooler fans even kick on once yet (will dynamically power up and down fan speed to ensure the 5kW of heat is bled from the liquid loop so miner doesn’t cook).

Our control solution involves a Wi-Fi relay for the 220 V HS05 rack, and a smart thermostat, both connected to Home Assistant. More logic details to come.

[![IMG_3107](https://forum.heatpunks.org/uploads/default/optimized/1X/24a75016a2402bc31a302bd3d6e3071f042abada_2_375x500.jpeg)IMG_31071200×1600 213 KB](https://forum.heatpunks.org/uploads/default/original/1X/24a75016a2402bc31a302bd3d6e3071f042abada.jpeg)
[![IMG_1684](https://forum.heatpunks.org/uploads/default/optimized/1X/0cb7a620f94454b045a1d8d341bfc26160d848ca_2_375x500.jpeg)IMG_16841920×2560 345 KB](https://forum.heatpunks.org/uploads/default/original/1X/0cb7a620f94454b045a1d8d341bfc26160d848ca.jpeg)

Let us know if you have any questions!

-------------------------

Cody | 2025-11-24 02:46:16 UTC | #2

Looks good!

So is this being run with a “Bang Bang” type control approach?  Like your Wi-Fi relay just applies and cuts power(220v) via Home Assistant signals?

-------------------------

tylerkstevens | 2025-11-24 16:08:48 UTC | #3

Correct. For now until we test and validate API control.

-------------------------

tylerkstevens | 2025-11-24 16:11:09 UTC | #4

We think we’re getting way more air changes per hour (ACH) in the basement - thanks to a 20x20" new return hole cut into the side of the furnace. Going to work on some plenum designs with a damper to dial this in.
