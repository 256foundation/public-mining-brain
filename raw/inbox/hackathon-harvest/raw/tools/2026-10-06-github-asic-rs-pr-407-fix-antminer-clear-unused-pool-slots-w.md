# 256foundation/asic-rs pull request #407: fix(antminer): clear unused pool slots when fewer pools are pushed

> Source: https://github.com/256foundation/asic-rs/pull/407
> Collected: 2026-10-07
> Published: 2026-10-06

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 407
- State: closed
- Author: cryptographicturk
- Opened: 2026-10-06
- Closed: 2026-10-06
- Labels: none

## Description

`set_pools_config` posts only the pools it is given. Stock firmware's
`set_miner_conf.cgi` overwrites just the slots it receives, so pushing two
pools to a miner holding three leaves the old third pool in place. Other
backends remove it.

## Evidence

Against an S19j Pro (firmware `Mon Dec 26 17:19:30 CST 2022`, `v2020` backend)
holding three pools, pushing two:

```
master       -> slots 1-2 rewritten, slot 3 keeps its old pool; get_pools_config returns 3
this branch  -> slot 3 is {"url":"","user":"","pass":""};      get_pools_config returns 2
```

On master the write clearly lands — slots 1 and 2 pick up the `stratum+tcp://`
prefix — while slot 3 keeps its original un-prefixed URL.

## The change

The pool list is always sent as three entries, with unused slots blanked.
`parse_pools_config` already skips empty-URL entries, so a cleared slot does
not read back as a pool.

Payload construction moves into a small `pools_payload` helper in each backend
so the wire format is unit-testable without a miner.

One behaviour change to be aware of: pushing an empty pool list now blanks all
three slots, where before it left the miner's pools as they were.

## Verification

- `cargo fmt --all -- --check` — clean
- `cargo test -p asic-rs-firmwares-antminer` — 37 passed, 3 ignored (1 new test per backend)
- CI on the fork (Run Tests, Cargo Assist) — passing
- Live, on the S19j Pro above with this commit: 3 → 2 → 1 → 3 pools, each read
  back correctly through `get_pools_config` and in the raw `get_miner_conf`
  output. Fan, frequency, voltage and work-mode settings were unchanged by
  every write.

Not covered: the `v2023_07` backend gets the same payload change but was not
exercised on hardware, so I am not claiming this addresses the pool part of
#310.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
