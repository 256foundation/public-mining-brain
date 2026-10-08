# 256foundation/asic-rs pull request #334: fix(braiins): report why a power-target write was refused instead of returning false

> Source: https://github.com/256foundation/asic-rs/pull/334
> Collected: 2026-10-07
> Published: 2026-08-21

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 334
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-21
- Closed: 2026-08-21
- Labels: none

## Description

## What

`set_power_limit` ends in `.is_ok()` on all five Braiins backends, so a refused
write reaches the caller as `Ok(false)` — not `Err` — with the reason discarded.
The transport below it has already done the work: `send_command` returns
`BraiinsError::HttpError { status, body }` on the REST backends
(`v26_04/web.rs:65-70`), and the GraphQL client unwraps the `errors` array into a
message even when the HTTP status is 200 (`v21_09/graphql.rs:152-157`). All of it
is thrown away one frame up.

## Why it matters

BOS+ says plainly what is wrong. Against an idle `S19XP` on 26.07:

```
400  new power target '500' is out-of-range (min: Some(954), max: Some(6435))
400  new power target '20000' is out-of-range (min: Some(954), max: Some(6435))
400  new power target '0' is out-of-range (min: Some(954), max: Some(6435))
```

That is the same error family as the pool-write message #331 surfaced — `group
name '' length (0) is out-of-range (min: Some(1), max: None)` — and until now all
of it collapsed to `false`. A caller cannot tell "target outside the tuner
envelope" from "BOSminer is not running" from an expired token, and those are
three different actions for whoever is standing in front of the miner.

## Change

`.is_ok()` becomes `?`, then `Ok(true)`. Five call sites, nothing else. It is the
same edit #331 made to `set_pools_config` on these same two clients.

## On the three GraphQL backends

#331 deliberately left alone code it could not test, and I want to flag that I
have not held to that here. Every unit on my bench resolves to a REST backend
(26.08 and 26.07 to `v26_04`, 26.01 and 25.11 to `v25_07`), so `v21_09`,
`v25_03` and `v25_05` are untested by me. I included them because the edit is
mechanical and `send_graphql_command` already returns `Err` for both a failed
HTTP status and a populated `errors` array — `?` only propagates what it was
already building. If you would rather this stayed to the two backends I can
demonstrate, say so and I will drop the other three.

## Verified

- `cargo fmt --all --check` clean; `cargo check --workspace` and
  `cargo check --features python` clean; `cargo clippy --all-targets --workspace
  -- -D warnings` clean; the braiins crate's 8 tests pass. rustc 1.98.0.
- Live hardware: `Antminer S19 XP` on BOS+ 26.07, `v25_07` backend, idle, tuner
  configured at 3200 W within the envelope above. The three refusals quoted are
  the actual responses. `configuration/miner` read back `power_target 3200 W`
  unchanged after each one, so nothing was mutated to produce them.

## Not in this change

The value is cast with `limit.as_watts() as u64`, which saturates instead of
failing — a negative or non-finite target silently becomes `{"watt": 0}`. Worth
tightening, and the ePIC backend already has `to_non_negative_u32_target` doing
exactly that, but it is a separate concern and this fix downgrades it from silent
to visible: `0` now comes back as the third refusal above rather than vanishing.
Happy to follow up if you want the Braiins side validating before the cast.

The same `.is_ok()` is still in the braiins `restart`, `pause` and `resume`
paths. Same defect, left alone for the same reason #331 left its neighbours.
