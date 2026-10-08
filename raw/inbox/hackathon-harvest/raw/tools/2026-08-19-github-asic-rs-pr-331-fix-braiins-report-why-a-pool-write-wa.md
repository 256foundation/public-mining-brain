# 256foundation/asic-rs pull request #331: fix(braiins): report why a pool write was refused instead of returning false

> Source: https://github.com/256foundation/asic-rs/pull/331
> Collected: 2026-10-07
> Published: 2026-08-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 331
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-19
- Closed: 2026-08-19
- Labels: none

## Description

## What

`set_pools_config` on the two Braiins REST backends ended in `.is_ok()`, so every
failure of `PUT /api/v1/pools/batch` reached the caller as `Ok(false)`.
`BraiinsError::HttpError` compounded it by carrying only the status code, so even
a propagated error could say no more than `HTTP error: 400`.

## Why it matters

Testing pool writes across a 24-miner bench turned up three distinct failures.
Each needs different action from the operator. All three arrived as `false`:

```
400  group name '' length (0) is out-of-range (min: Some(1), max: None)
412  BOSminer is not running
500  BOSminer API connection error: Connection refused (os error 111)
```

The first one is what sent me looking. Writing a `PoolGroupConfig` with an empty
name is rejected outright by BOS+, while UMC OS and AntMiner Stock accept a blank
name without comment — so pool writes appeared to succeed and silently did
nothing on Braiins alone. Finding that took a packet capture against live
hardware; the miner had been saying so plainly the whole time.

## Change

`HttpError` carries the response body alongside the status, and both REST
backends propagate with `?` rather than collapsing to a boolean. A caller that
gets `Ok(true)` now knows the miner accepted the write; one that gets an error is
told which of the three happened.

## On changing the enum

I did look for a narrower change that left `HttpError(u16)` alone, but
`send_command` consumes the response before it returns, so the body is gone by
the time a caller sees the error. The alternatives were duplicating the HTTP
client at the call site, or adding a second near-identical variant. If you would
rather not change the existing variant, say so and I will go the additive route.

`Display` keeps the old output when the body is empty, so nothing that only had a
status code reads any worse than before.

## Verified

- `cargo check` (also with `--features python`), `clippy` clean, the crate's 8
  tests pass
- Live hardware: BOS+ 26.01 (`v25_07` backend) and 26.08 (`v26_04`), both on
  `Antminer S19j Pro` / `S19XP`. With a named group the write returns 201 and the
  miners come back mining on the new pool; with a blank name the 400 above is now
  surfaced instead of swallowed.

## Not in this change

The same `.is_ok()` appears in the antminer, whatsminer and vnish backends, and
in the bosminer restart the three GraphQL braiins backends issue after a
successful mutation. Same defect, but I only have hardware to reproduce this
path, so I have left them alone rather than change code I cannot test. Happy to
follow up if you want them moved together.

There is a companion change to the Python binding — it ends in `.ok()` too, so
this fix alone turns a refused write from `False` into `None` for Python callers
rather than raising. I will open it separately once this lands, since it is an
API decision rather than a bug fix.
