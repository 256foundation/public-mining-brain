# Immersion Fluids

> Sources: *Bitcoin Mining Heat Reuse* (Stevens, 2025) ch. 5–6 (immersion mechanics, thermal battery, fluid limits); Constellation Heating products page (Liquid21); 256F Telegram (fluid-practice remarks)
> Raw: [book ch. 6 extract](../../raw/books/braiins-heat-reuse/06-picking-hardware.md); [book ch. 5 extract](../../raw/books/braiins-heat-reuse/05-managing-and-controlling-heat.md); [Constellation products](../../raw/industry/constellation-heating/2026-10-11-constellation-products.md); [256F Telegram digest](../../raw/history/2026-10-08-256f-telegram-signal.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

## Why dielectric oil

The book's immersion mechanics (ch. 6): "a non-conductive, dielectric oil is used. This oil doesn't conduct electricity, so it won't short-circuit the device" — "You can take an air-cooled ASIC miner, remove its fans (since pumps now move the oil instead of fans moving air), and submerge it in the tank"; "cool immersion oil is pumped in from the bottom and flows up through the miner's heat sinks, absorbing heat via convection." (p. 97)

## What the oil buys you

- Dust/debris insulation + thermal mass: "Immersion cooling submerges miners in dielectric oil, insulating hardware from dust and debris while leveraging the oil's high specific heat capacity and thermal mass to absorb and store heat. This helps stabilize temperatures, reducing wear and extending hardware lifespan." (pp. 114–115)
- Thermal-battery operation: "The immersion tank acts as a thermal battery, storing heat energy due to the high thermal mass of the liquid... When the oil cools down sufficiently, the miners turn on to warm it back up; if the oil overheats, they switch off." — Cody Harris's design, in-print (pp. 90–91); the same pattern grounds [Immersion Heat Reuse](immersion-heat-reuse.md).
- Full capture: "immersion-cooling captures all heat from ASIC chips, power supplies, and control boards, making it ideal for applications where every watt of heat is valuable." (p. 115)

## The engineering costs (ch. 6 is blunt about these)

- Pumping: "Oil's high viscosity (thickness) makes it less efficient for pumping and transferring heat over long distances compared to water." (p. 115)
- Hardware wear: "immersion systems are notorious for eroding thermal paste between ASIC chips and heat sinks." (p. 115) — plan re-pasting as scheduled maintenance.
- Hydronic incompatibility: "most hydronic hardware - like pumps, valves, manifolds, and expansion tanks - is incompatible with dielectric oil." (p. 115) — this is the root of the dual-loop isolation rule in [Hydronic Heat Reuse](hydronic-heat-reuse.md).

## Named fluids in the ecosystem

- **Liquid21** (Constellation Heating) — shipped fluid for their pool boilers: "Titanium heat exchanger, Liquid21 fluid included" (products page, 2026-10-11). Titanium-exchanger pairing implies fluid chemistry chosen for compatibility; no public datasheet captured.
- **Hydro-side coolant**: water blocks run purified water "sometimes mixed with antifreeze coolant like ethylene glycol to prevent freezing" (pp. 98–99) — that is the hydro class, not immersion; see [Hydronic Heat Reuse](hydronic-heat-reuse.md).

## Community risk culture

The group's running joke is also its maintenance brief: "I think "dielectric fluid poisoning" is biggest risk my man. Looks delicious!" [#1501 · 2025-01-24 · Gerald Glickman] — behind the joke: oil in the wrong loop (or on the wrong floor) is the standing immersion hazard; isolation and containment carry the safety load.

## No vendor endorsements

No fluid vendor passes the notability bar as of 2026-10-11 beyond Constellation's own platform fluid — hobbyist mineral-oil practice predates the group but carries no dated anchor here. Sizing and control physics live in [ASIC Thermals & Heat Reuse](asic-thermals-and-heat-reuse.md).

## See Also

- [Immersion Heat Reuse](immersion-heat-reuse.md)
- [Hashrate Heater Comparison](hashrate-heater-comparison.md)
- [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- [Hashrate Heating & Mining Infrastructure Companies](../industry/hashrate-heating-companies.md)
