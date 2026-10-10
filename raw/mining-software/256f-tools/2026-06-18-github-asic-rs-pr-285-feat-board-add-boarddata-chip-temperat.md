# 256foundation/asic-rs pull request #285: feat(board): add BoardData.chip_temperature (populate for VNish)

> Source: https://github.com/256foundation/asic-rs/pull/285
> Collected: 2026-10-07
> Published: 2026-06-18

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 285
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-18
- Closed: 2026-06-22
- Labels: none

## Description

`BoardData` exposes `board_temperature` / `intake_temperature` / `outlet_temperature`, but no chip temperature — even where the firmware reports one. The VNish backend already reads `/chip_temp/max` per chain (it's used as the air-cooled intake fallback), but the value is otherwise discarded, so consumers lose the chip temperature.

This adds `BoardData.chip_temperature: Option<Temperature>` (defaults `None`, so backends that don't report it are unaffected) and populates it in the VNish backend from the already-parsed `chip_temp/max`.

### Tested
Live on an Antminer S19 Pro Hydro (VNish 1.3.3): all 4 boards report `chip_temperature` (~50 °C). Other backends unaffected (field stays `None`).

Context: we lost per-board chip temps migrating a Home Assistant integration from pyasic to asic-rs and needed them back (a >70 °C safety alarm depends on them). Happy to adjust — e.g. populate it for other firmwares that expose a chip temp too.

## Comments

### b-rowan on 2026-06-18

This seems to be an issue with documentation clarity.

Intake/inlet temperature is supposed to be either the temperature of the first chip on the chain, OR the lowest chip level temperature reported.  These are the same thing nearly all the time.

Outlet temperature is the same idea, either the last chip on the chain, OR the highest chip temp if not reported, again likely the same thing.

I would prefer to put the chip temperatures into those fields instead, I don't know how many different readings VNish provides,  it if they only provide 1 you can put it into both.

### pos-ei-don on 2026-06-18

There's a wrinkle worth deciding before I change this. On a **hydro** miner, #277 already maps `intake_temperature`/`outlet_temperature` to the **water** inlet/outlet temps (your own guidance there: "environment temperature = the incoming medium"). So on hydro, intake/outlet are the coolant temps, and the per-board **chip** temperature is a genuinely separate reading — folding it into intake/outlet would overwrite the water temps.

Two clean ways forward: **(a)** keep a dedicated `chip_temperature` field (this PR) — cleanest, since intake/outlet now mean coolant/environment; or **(b)** define precedence: hydro → water in intake/outlet, air-cooled → chip temps in intake/outlet (no new field). It's your data model — which do you prefer? I lean (a) for consistency across cooling types, but happy to do (b).


### b-rowan on 2026-06-18

I think (b) makes the most sense, keeping in mind that the thermal capacity of water in a hydro setup is much higher than that of air, its likely the chips are very close to the temperature of the water, and I think the question is "how do the hydro miners measure that incoming and exhaust temperature?".  I believe they are measuring them from the chips based on the index in the chain, so I think (b) actually keeps things consistent.

### pos-ei-don on 2026-06-18

Good distinction — and it's really a hardware point rather than a VNish one: the sensors live on the Antminer, the firmware (VNish or stock) just surfaces them. On the S19 Pro Hydro the hashboards report per-chip temperatures, the board has its PCB sensor, and the hydro cooling loop has **dedicated water inlet/outlet sensors** — physically separate from the chip sensors (the silicon sits above the coolant temp).

Your chip-index model fits **air** Antminers well: there's no dedicated intake/outlet sensor there, so first/last (or lowest/highest) chip is the sensible approximation. But on **hydro** there are real coolant sensors, so intake/outlet = water (what #277 maps), and the chip temperature is a genuinely separate reading — not derivable from the water. And the gap between the two isn't small or constant: it widens with load — at higher power the silicon runs well above the coolant, so the water temp would under-report the actual chip temperature exactly when the over-temp headroom matters most.

Also, `BoardData` already carries `board_temperature` (the PCB sensor) as its own field alongside intake/outlet, so multiple distinct per-board temperatures are already the model; a dedicated `chip_temperature` fits that pattern.

Proposal — purely additive, leaving your air-cooled model intact: keep `chip_temperature` as a dedicated field, populated where the hardware reports it (None otherwise). Air-cooled backends still derive intake/outlet from chip index exactly as you described; hydro keeps the real water temps in intake/outlet and exposes the chip temp separately.


### b-rowan on 2026-06-18

This starts to get even more confusing since we technically also surface chip temperatures inside the hashboard data's chips struct, but only some device types support that.  My biggest concern here is backwards compatibility with what is already here, but I think I would suggest a move in the opposite direction.

I would like to make `inlet` and `outlet` temperature the first and last chip temperatures, since that is how it has been implemented in the past, but for hydro I think we could add `outlet_fluid_temperature`, such that the model is now:

`inlet_temperature`: coolest/first chip
`outlet_temperature`: hottest/last chip
`fluid_temperature`: fluid temperature at the intake, including passive air
`outlet_fluid_temperature`: exhaust temperature for the fluid, likely only for water cooled miners with dedicated sensors.

I think this preserves existing functionality best while still ensuring that we have correct data for hydro units, but this does require a change to the recent vnish hydro changes.

Let me know your thoughts here, but I think this is a better path forward than creating a new field which requires all existing miners to port to it by instead adding a new field that only applies to very specific miners and can be added easily as needed.

The data gathering for the outlet fluid temp would just get appended to the existing `GetFluidTemperature` trait implementation, possibly as a new set of functions.

### pos-ei-don on 2026-06-18

Works for me — it's lossless (chip min/max in `inlet`/`outlet`, coolant in `fluid_temperature` + the new `outlet_fluid_temperature`), so I'm happy with that direction.

Two things to pin down:

**1. Who implements it?** It changes the recent VNish hydro work (#277 currently maps `intake`/`outlet` to the water sensors — those move to `fluid_temperature`/`outlet_fluid_temperature`, and `inlet`/`outlet` become coolest/hottest chip). Happy to do the VNish side myself, or leave it to you — just say which.

**2. Keeping it mappable.** With this model the field names invert relative to what the miners' own UIs show — both VNish and BraiinsOS label the coolant "inlet/outlet water", but in asic-rs `inlet_temperature`/`outlet_temperature` would be the chips, and the water lives under `fluid_temperature`/`outlet_fluid_temperature`. So to map a miner's UI to asic-rs you have to flip it: the UI's "chip temp" is `outlet_temperature`, the UI's "inlet water" is `fluid_temperature`, etc. Since this cuts across both firmwares, could we make that mapping explicit in the field docstrings so it's unambiguous which reading is which? That's the one thing I'd want documented.

On backwards-compat / "avoid making everyone port": I'd weight that lightly — your model itself adds a field and changes the hydro mapping, and the rewrite already reworked the entity/ID model, so consumers are porting regardless. So I don't think avoiding a new field needs to drive it; the model stands on its own merits.


### b-rowan on 2026-06-18

Would it make sense to go to
`inlet_chip_temperature`
`outlet_chip_temperature`
`fluid_temperature`
`outlet_fluid_temperature`

instead?

### pos-ei-don on 2026-06-18

Yes — that's much clearer. `inlet_chip_temperature` / `outlet_chip_temperature` say exactly what they are (no more "is inlet the chip or the water?"), and `fluid_temperature` / `outlet_fluid_temperature` are unambiguous for the coolant. Nothing's lost and the names are self-documenting across air and hydro — I'm happy with that as the model.

I'll take the VNish side and build it now: rename the per-board chip temps to `inlet_chip_temperature` / `outlet_chip_temperature`, move the water sensors to `fluid_temperature` / `outlet_fluid_temperature` (adjusting the recent #277 mapping), and wire `outlet_fluid_temperature` into the fluid-temperature trait. Do you want me to repurpose this PR (#285) to the 4-field model, or open a fresh one and close this?


### b-rowan on 2026-06-18

Might as well just build it out here, as a continuation of our discussion.

### pos-ei-don on 2026-06-19

Perfect timing — I've actually already built the full 4-field version out on my side: per-board `inlet_chip_temperature`/`outlet_chip_temperature` plus miner-level `fluid_temperature`/`outlet_fluid_temperature`, exactly as we discussed. It's CI-green on my fork and running live on my S19 Pro Hydro (the inlet/outlet coolant delta shows ~8-15 °C under load, so the split is clearly worth it).

I'll get it up as a PR **today** — so no need for you to spend time building it. Happy to open it fresh against `master` and reference #285, or fold it into this one, whichever you prefer. Just say the word.


### b-rowan on 2026-06-22

Superseded by #286
