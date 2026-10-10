# 256foundation/asic-rs pull request #325: fix(antminer): read power draw from the `new_api` stats payload

> Source: https://github.com/256foundation/asic-rs/pull/325
> Collected: 2026-10-07
> Published: 2026-08-12

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 325
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-12
- Closed: 2026-08-19
- Labels: none

## Description

> **Depends on #328.** That PR fixes the RPC transport so `new_api` actually
> reaches the miner. Until it merges, its commit appears here too; afterwards
> this PR is the single `mod.rs` change. Reworked from the web endpoint to RPC
> per review.

`wattage` is always `None` on newer stock firmware. `DataField::Wattage` is
sourced from the legacy RPC `stats` payload, which carries no power reading on
these generations.

## Where the reading lives

The `new_api` variant of `stats` reports it. That is a different payload to the
legacy one — its `STATS` array holds a single element, so the value sits at
`/STATS/0` rather than the `/STATS/1` the legacy source uses:

```
{"command":"stats"}                  -> STATS len 2, Msg "CGMiner stats", no power
{"command":"stats","new_api":true}   -> STATS len 1, Msg "stats",         power/watt present
```

## The change

- Adds `stats` + `new_api` as a second source for `DataField::Wattage`, read at
  `/STATS/0`.
- Accepts the `watt` key alongside the existing `power` / `Power` /
  `chain_power`. The spelling varies by model on identical firmware: the L9
  reports `power`, the L11 `watt`.

The legacy location is kept and tried first, so firmware that does report power
there is unaffected. Applied to both `v2020` and `v2023_07`.

## Measured

Against live hardware, all previously `None`:

```
L11   3651 W        L9   3357 W
L11   3636 W        L9   3353 W
                    L9   3379 W
```

An idle unit reports its true low draw rather than falling back to absent, so a
genuine zero stays distinguishable from a missing reading.

No regressions in the groups that cannot benefit: T21, S21 Hydro and S21+ Hydro
expose no power draw on any transport and continue to report nothing, and older
units that do not honour `new_api` still receive the legacy payload exactly as
before.

The two payloads share only `fan_num` and `rate_30m`, identical in both, so
merging them into one field cannot silently clobber a value.

## Verification

- `cargo fmt --all -- --check` — clean
- `cargo clippy -p asic-rs-firmwares-antminer --all-targets` — clean
- `cargo test -p asic-rs-firmwares-antminer` — 20 passed
- `cargo test --workspace` — no failures
- Live check against multiple L9 and L11 units


## Comments

### cryptographicturk on 2026-08-14

I updated it after submitting another PR to fix an underlying issue that prevented this solution from working.
