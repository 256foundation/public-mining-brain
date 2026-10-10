# 256foundation/asic-rs pull request #328: fix(antminer): send `new_api` as a top-level flag rather than a `parameter`

> Source: https://github.com/256foundation/asic-rs/pull/328
> Collected: 2026-10-07
> Published: 2026-08-13

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 328
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-13
- Closed: 2026-08-19
- Labels: none

## Description

`send_rpc_command` wraps every parameter value in cgminer's `parameter`
argument. Bitmain's `new_api` is not a `parameter` — it is a top-level flag
alongside `command`. Nested, the firmware ignores it and answers with the
legacy payload.

Every `new_api` helper on this client is affected — `stats`, `summary`,
`pools`, `rate`, `warning` and `reload` all ask for the new API and silently
receive the old one. Nothing errors: the response is a well-formed
`STATUS: "S"` body, just the wrong shape, so a caller cannot tell.

## Evidence

Against an L9 and an L11 on `86.48-2.0.0`:

```
{"command":"stats","new_api":true}                -> STATS len 1, Msg "stats",         power/watt present
{"command":"stats","parameter":{"new_api":true}}  -> STATS len 2, Msg "CGMiner stats", no power field
```

The second response is byte-identical to sending `{"command":"stats"}` with no
parameter at all.

## The change

Object parameters merge at the top level; scalars keep the `parameter`
wrapper, preserving cgminer's own convention for commands like `switchpool`
that take a pool index. Every parameter currently passed within this backend
is a `new_api` object, so nothing relied on the old wrapping.

Request construction moves into `build_rpc_request` so the wire format is
unit-testable without a socket.

## Verification

- `cargo fmt --all -- --check` — clean
- `cargo clippy -p asic-rs-firmwares-antminer --all-targets` — clean
- `cargo test -p asic-rs-firmwares-antminer` — 20 passed (8 new, covering
  object merge, scalar wrapping, absent parameters, and `command` precedence
  over a conflicting key)
- `cargo test --workspace` — no failures

Checked against live hardware by temporarily sourcing `DataField::Wattage`
from `stats` + `new_api` (that wiring is *not* part of this PR). With the fix,
wattage resolves on hardware that reports it and stays absent elsewhere:

```
L11   3651 W      L9   3357 W
L11   3636 W      L9   3353 W
                  L9   3379 W
```

Models whose firmware exposes no power draw (T21, S21 Hydro, S21+ Hydro)
correctly report nothing rather than erroring, and older units that do not
honour `new_api` at all still receive the legacy payload exactly as before.

The two payloads share only `fan_num` and `rate_30m`, identical in both, so
merging them into one field carries no risk of silently clobbering a value.
