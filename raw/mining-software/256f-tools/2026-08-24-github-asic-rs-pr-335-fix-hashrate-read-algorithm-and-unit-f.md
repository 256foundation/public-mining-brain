# 256foundation/asic-rs pull request #335: fix(hashrate): read algorithm and unit from the miner instead of assuming SHA-256

> Source: https://github.com/256foundation/asic-rs/pull/335
> Collected: 2026-10-07
> Published: 2026-08-24

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 335
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-24
- Closed: 2026-08-24
- Labels: none

## Description

## Problem

Scrypt Antminers (L3+/L7/L9/L11) come back as **SHA-256 miners** under both VNish and stock firmware, and every hashrate is read on the assumption that it is in GH/s.

None of this depended on what the miner replied — the values were compile-time literals, so no device response could change the outcome.

## Three causes

**1. `AntMinerModel` never overrode `MinerModel::hash_algorithm()`**, so it inherited the trait's SHA-256 default. Only VolcMiner and Elphapex override it, and both return `Scrypt` unconditionally because every model in those makes is Scrypt. AntMiner is the one genuinely mixed-algorithm make in the repo — SHA-256, Scrypt, X11, Kadena, Equihash, Ethash, Handshake — and the one that never used the hook.

**2. Both firmwares hardcoded the algorithm** — `HashAlgorithm::SHA256` into `DeviceInfo::new`, `algo: "SHA256"` into every `HashRate`. Five sites per VNish backend, three per stock backend.

**3. Both hardcoded the unit, although both firmwares report it.** VNish publishes `hr_measure` (`GH/s` / `MH/s` / `N/A`) on `/info` — the same response already parsed for the model — documented in the 1.2.x and 1.3.x API specs under `meta/`. Stock cgminer publishes `rate_unit` in STATS; it is sitting next to `total_rateideal` in the repo's own S21 fixture (`rate_unit: "GH"`).

## Approach

The algorithm now comes from the model; the unit comes from the miner.

For VNish, `hr_measure` is carried alongside each hashrate figure using the collector's existing `tag` mechanism (the same pattern whatsminer/proto/luxminer already use), so **no core API change** was needed.

For stock, the two sources are deliberately kept separate: cgminer's SUMMARY key names its own unit (`GHS 5s` vs `MHS 5s`), so that key is trusted for the value it labels, while `rate_unit` is used only for the STATS figures — `total_rateideal`, `chain_rate*` — whose names say nothing about their scale. Crossing the two would let an inconsistent `rate_unit` corrupt a value read from a correctly-named key.

## Non-regression

Everything falls back to GH/s when the unit is absent or unusable (`"N/A"`), and `GHS 5s` is tried first, so SHA-256 models take exactly the path they did before. The pre-existing `test_antminer` fixture tests still pass unchanged, which is the signal that matters.

## Scope left out

Models whose algorithm `HashAlgorithm` cannot yet name — KS3/KS5 (kHeavyHash), K7 (Eaglesong), E9 Pro (Ethash), Z15 (Equihash), HS3 (Handshake), DR5 (Blake256R14) — still report SHA-256. Unchanged from today, and documented in a comment rather than left silent. Naming them means adding public enum variants that flow into the Python and TypeScript bindings, which seemed like a separate call — happy to fold it in if you would prefer.

Also left out, as neither is this bug: VNish control-board parsing (the firmware sends short codes `aml|bb|cv|stm|xil`, and `AntMinerControlBoard::parse` only knows `AML`/`BB`, so `cv`/`xil`/`stm` yield no control board), and the VNish `set_power_limit` assumption that autotune presets are named by wattage.

## Not verified against hardware

That a Scrypt stock Antminer names its SUMMARY key `MHS 5s`. I could not confirm it, so it is only consulted as a fallback after `GHS 5s` misses — a wrong guess yields today's behaviour rather than something worse. If anyone has an L7/L9 on stock firmware, a `summary` + `stats` dump would settle it.

## Verification

Run on Rust 1.98.0 stable (`--workspace` needs Python dev headers for `asic-rs-pydantic` to link, so the three changed crates were targeted):

- `cargo test` — 33 passed, 0 failed
- `cargo clippy --all-targets` — clean, with `warnings = "deny"`
- `cargo fmt --all -- --check` — clean

Seven new tests: `l_series_is_scrypt`, `d_series_is_x11`, `sha256_models_are_unchanged`, `unknown_model_defaults_to_sha256`, plus fixture-driven `scrypt_model_is_read_in_the_unit_it_reports` for stock v2020 and both VNish backends, and `sha256_model_is_unchanged` / `unusable_unit_falls_back_to_gigahash` guarding the fallback.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ErTo1a4BgYptp5tC8r1oHR

## Comments

### cryptographicturk on 2026-08-24

All five nits addressed — replies inline. But your "double check the Antminer model stuff" instinct was right, and it turned up something the whole test suite was missing.

## The fix was not reaching real miners at all

I got access to live L9 and L11 hardware on stock firmware. Both still reported `"algo": "SHA256"` after my changes, while all 33 unit tests passed.

Model detection returns an `AntMinerCompatibleModel`, never a bare `AntMinerModel`, and that wrapper forwards `make_name` and `is_known` but not `hash_algorithm` — so every miner fell straight through to the trait's SHA-256 default. My tests constructed backends with `AntMinerModel` directly and never touched the wrapper.

`BraiinsCompatibleModel` wraps `AntMinerModel` too and has the identical gap — latent today since Braiins targets SHA-256 machines, but the same defect. `EPicCompatibleModel` already forwarded correctly, so there was a working reference in-tree the whole time. Both now forward, with a test that asserts it directly rather than only through the make.

After the fix, all three machines report `Scrypt`, with per-board values matching `chain_rate*` exactly.

## Two corrections to the original PR description

**Stock cgminer does not universally emit STATS' `rate_unit`.** It is in the S21 fixture, which is where I got it, but it is *absent* on both the L9 and L11. So the GH/s fallback is the live path for these models, not a rarely-hit safety net.

**Scrypt Antminers on stock report GH/s, not MH/s.** `GHS 5s = 19.21` on the L11, `11.48` on the L9, and `total_rateideal` / `chain_rate*` are GH as well. So on stock there was never a 1000x error for these models — the numbers were already right and only the algorithm label was wrong. That risk is real on VNish, where the field is unit-neutral; on stock the self-describing key name protected it. I stated that too broadly the first time.

## New fixtures

Added L9 and L11 payloads captured from the live machines, under `v2023_07` — which is the backend they actually use, since their `CompileTime` dates resolve past 2023.7. The L9 fixture has one board degraded to 25 of 110 chips, so it exercises partial-failure parsing. The captured commands carry telemetry only: no pool, worker, network or serial identifiers.

Also worth noting the fixtures confirm the hardware definitions already in the repo: `miner_count: 3` with `chain_acn` of 110 for the L9 and 88 for the L11, matching `hardware.rs` exactly.

## On the algorithm enum

Your point about defining the algorithm types more strictly — `HashRate.algo` is a `String` today while `HashAlgorithm` is already a proper enum with `EnumString`, so making the field the enum looks like a contained change. Happy to fold it into this PR if you would prefer, or leave it as the separate issue you suggested. Say which and I will do it.

Verification: `cargo test` 43 passed / 0 failed across the antminer, braiins, vnish and makes crates, `cargo clippy --all-targets` clean under `warnings = "deny"`, `cargo fmt --check` clean, plus the live run against three machines.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ErTo1a4BgYptp5tC8r1oHR

### b-rowan on 2026-08-24

> Your point about defining the algorithm types more strictly — `HashRate.algo` is a `String` today while `HashAlgorithm` is already a proper enum with `EnumString`, so making the field the enum looks like a contained change. Happy to fold it into this PR if you would prefer, or leave it as the separate issue you suggested. Say which and I will do it.

With the new enum property attached to the model types, this might get more difficult.  For now I think this is fine as-is, we can always make changes to this later if needed, but algo's may need to support strings anyway as a generic fallback, in case someone wanted to extend the library externally.

### cryptographicturk on 2026-08-24

Following up on your enum question — I audited every model in every make to see what the algorithm type would actually need, and split the result into three PRs so each is a small review:

- **#337** — the six algorithms missing across the supported models (kHeavyHash, Eaglesong, EtHash, Equihash, Handshake, Blake256R14), plus `Unknown`. Also worth knowing: `X11`, `Blake2S256` and `Kadena` exist today but are **never constructed anywhere** — only `SHA256` and `Scrypt` are ever produced.
- **#338** — `__eq__`/`__hash__` on `HashAlgorithm` and `HashRateUnit`, so they compare against their own names. This is what makes the next one non-breaking.
- **#339** — `HashRate.algo` becomes the enum, which is your original suggestion.

They merge in that order. This PR should land **after** #337, at which point I will expand it to cover the nine AntMiner models whose algorithms were previously unnameable (KS3/KS5/KS5 Pro, K7, E9 Pro, Z15/Z15 Pro, HS3, DR5) and drop the "left to a follow-up" caveat from the model doc comment entirely.

Also opened **#336** — unrelated to any of this, but `.gitignore` has no rule for anything the Python side generates, and `maturin develop` writes a ~390 MB extension module into `python/pyasic_rs/`. I managed to commit one and had the push rejected at GitHub's file size limit.

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ErTo1a4BgYptp5tC8r1oHR

### cryptographicturk on 2026-08-24

Correction to my previous comment: it said this PR "should land after #337" and that I would expand it. It had already merged by the time I posted — I was working from a stale view. The expansion is #340 instead.

#340 closes the gap this PR documented and deferred: the nine models that reported SHA-256 only because `HashAlgorithm` had no variant for what they mine (HS3, DR5, KS3/KS5/KS5 Pro, K7, E9 Pro, Z15/Z15 Pro). It depends on #337 for those variants.

Merge order for the whole set:

    #336  (independent, .gitignore)
    #337  ->  #340   (algorithm variants, then the models that need them)
          ->  #338  ->  #339   (equality semantics, then HashRate.algo as the enum)

🤖 Generated with [Claude Code](https://claude.com/claude-code)

https://claude.ai/code/session_01ErTo1a4BgYptp5tC8r1oHR
