# Hydro Three Phase > Single Phase Conversion?

> Source: https://forum.heatpunks.org/t/hydro-three-phase-single-phase-conversion/205
> Collected: 2026-10-10
> Published: 2025-10-11
> Registry ID: heatpunks-forum

BitcoinHeatEric | 2025-10-11 03:33:52 UTC | #1

Wondering if anyone is working on or knows of any three phase to single phase conversion work being done for the modern hydro systems that come with the modern efficiencies…

I’d like to do more ASIC to water installs for residential and eventually strata building hydronic, pool and spa heating and it seems like the obvious choice for efficiency and clean infrastructure is the hydro equipment.

Residential customers are not generally blessed with 3ph, so what are we doing about it heatpunks?

-------------------------

tylerkstevens | 2025-10-15 13:33:01 UTC | #2

This is a good question. I’ve also wondered if anyone has tried this, or if any Electricians care to comment.

I hate that we are limited to the M64 from MicroBT here in North America. Since it’s the only single phase power hydro miner.

-------------------------

Rowdy | 2025-11-03 23:01:21 UTC | #3

You can build or buy a rotary phase converter. There is also digital phase converters. Phase Technologies makes good equipment. I would contact them to see what fits your needs.

-------------------------

BitHeat | 2025-11-06 18:43:01 UTC | #4

Some VFDs(variable frequency drive) support phase conversion, will have to oversize it by a good amount especially for continous use. I haven’t done this myself but I know it is possible.

-------------------------

Typirtz | 2025-11-09 03:18:09 UTC | #5

I bought a small Chinese transformer that converts to 380 volts, which is usually the min input voltage but I was scared to even try running it.  If anyone wants it for testing purposes get ahold of me and I would sell it at a discount.

-------------------------

thak777 | 2025-12-03 14:07:50 UTC | #6

I’ve never seen a Bitmain hydro unit and I’m certainly not an electrical engineer, but I would imagine that the individual hashboards don’t require 3-phase.

Unless one board is A-B, one is B-C, and one is A-C (all hot-hot, which doesn’t make sense to me)…wouldn’t that mean that each board is actually hot-neutral on the individual A/B/C phases? and if so, couldn’t you “convert” the miner into 3 individual miners like the Loki-style singleboard setups?

you’d need to get 2 extra control boards–so you have one for each hashboard–but combined with custom firmware and some oldschool 120V PSUs…maybe?
