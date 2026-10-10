# 256foundation/asic-rs issue #278: Interest in optional per-miner Cargo features (faster builds)?

> Source: https://github.com/256foundation/asic-rs/issues/278
> Collected: 2026-10-07
> Published: 2026-06-17

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 278
- State: closed
- Author: pos-ei-don
- Opened: 2026-06-17
- Closed: 2026-06-17
- Labels: none

## Description

Following on from #277 — while building the workspace I noticed the root crate (and the Python `pyasic_rs` package) compiles every `asic-rs-makes/*` and `asic-rs-firmwares/*` crate unconditionally, since they're hard dependencies and the factory registers every make.

For deployments that only target a couple of miner families, gating each make/firmware behind a Cargo feature — with `default` enabling all of them, so nothing changes out of the box — would let `--no-default-features --features antminer,vnish,braiins` build only what's needed. That noticeably cuts compile/CI time, with no behavior change for anyone on defaults.

Would a PR along those lines fit the project's direction? I'm happy to implement it, just wanted to check for interest before doing the work. Thanks!


## Comments

### b-rowan on 2026-06-17

Yep, this was actually the intention, but I very well could have something set up wrong...

Here's where the feature flags are declared, not sure if this is correct, but feel free to open a PR if anything needs to change here - 

https://github.com/256foundation/asic-rs/blob/43d706ef31aa154f8bea0bd7ef8e81caa9cbe491/Cargo.toml#L138-L169

The only thing that we do right now that might be an issue is we do compile the makes for every build, but that is because I would rather not explicitly define which firmwares support which makes, but possibly something that could change.

### pos-ei-don on 2026-06-17

Dug into this on a real wheel build. The feature flags themselves are wired up correctly (the `lib.rs` re-exports and `default_firmware_registry()` are all `#[cfg(feature)]`-gated), but two things stop gating from actually pruning the build:

1. **The `python` feature re-enabled every firmware.** It listed `asic-rs-firmwares-X/python` without the `?` prefix, which implicitly enables the optional dep — so any Python wheel pulled in all firmware crates regardless of `--features`. Fixed in #281 (weak `?` form). Verified on the cp314 musllinux wheel: `--features python,core,proto,antminer,vnish,braiins` went from **621 → 601 compile requests (210 → 190 Rust units)**, i.e. 20 firmware crates no longer compiled. No change on default features.

2. **The makes are non-optional**, so they compile on every build (your point exactly). I probed making one optional (`asic-rs-makes-auradine`, optional + weak python): it builds fine — the root crate doesn't reference makes directly — and drops exactly **1** unit. Every unused make is ~1 unit (they all depend only on shared crates: core/serde/strum/serde_json/pyo3), so gating all of them saves only ~8 units on top of the firmware fix.

So honestly the makes aren't worth much, and gating them needs an explicit firmware→make mapping — which is the bit you said you'd rather not hardcode. That's your design call; I left it out of #281 so that PR stays minimal and uncontroversial. Happy to follow up with a makes PR if you decide the ~8 crates are worth the mapping.

### b-rowan on 2026-06-17

> 1. **The `python` feature re-enabled every firmware.** It listed `asic-rs-firmwares-X/python` without the `?` prefix, which implicitly enables the optional dep — so any Python wheel pulled in all firmware crates regardless of `--features`. Fixed in [fix(features): weak `?` python features so firmwares actually gate (#278) #281](https://github.com/256foundation/asic-rs/pull/281) (weak `?` form).

Cool, I didn't know this was possible.  Not something we will likely ever use, since published builds have all features, maybe there is a future where we could feature gate on the python side too, but for someone building from source it's a nice speed up.

> Happy to follow up with a makes PR if you decide the ~8 crates are worth the mapping.

I don't think it will end up being worth it, those crates are mostly static type information and very little actual code, so it's pretty likely they end up not being a huge performance issue anyway.  It prevents some maintenance headaches if something ever gets missed, so its a pretty small tradeoff IMO.
