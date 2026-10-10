# 256foundation/asic-rs pull request #286: feat(temp): 4-field temperature model (per-board chip inlet/outlet + miner coolant inlet/outlet)

> Source: https://github.com/256foundation/asic-rs/pull/286
> Collected: 2026-10-07
> Published: 2026-06-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 286
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-19
- Closed: 2026-06-22
- Labels: none

## Description

Continues the discussion in #285 — the full 4-field temperature model we landed on.

**Per-board (`BoardData`)** — splits the single chip temperature into the two values the hardware actually reports:
- `inlet_chip_temperature` — coolest chip on the board
- `outlet_chip_temperature` — hottest chip on the board

**Miner-level (`MinerData`)** — the coolant loop, both ends:
- `fluid_temperature` — coolant inlet (already existed)
- `outlet_fluid_temperature` — coolant outlet (new)

This keeps the chip sensors and the coolant sensors as distinct, self-documenting fields rather than overloading one `chip_temperature`, and avoids the inlet=chip-vs-water ambiguity. VNish maps chip min/max → inlet/outlet chip and the two water sensors → fluid/outlet fluid; firmwares that don't report a value simply leave it `None`.

Verified live on an S19 Pro Hydro (VNish): under load the coolant inlet/outlet delta runs ~8–15 °C, and the per-board chip inlet/outlet spread widens with power — so the split carries real signal, not just cosmetics.

If you'd rather fold this into #285, happy to — just say the word and I'll close this in favour of that.
