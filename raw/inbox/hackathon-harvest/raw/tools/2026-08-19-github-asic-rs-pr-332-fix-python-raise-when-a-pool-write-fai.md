# 256foundation/asic-rs pull request #332: fix(python): raise when a pool write fails instead of returning None

> Source: https://github.com/256foundation/asic-rs/pull/332
> Collected: 2026-10-07
> Published: 2026-08-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 332
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-19
- Closed: 2026-08-20
- Labels: none

## Description

## What

`Miner.set_pools_config` in the Python binding ends in `.ok()`, which turns any
error into `None`. #331 made the braiins backend report *why* a pool write was
refused; this lets a Python caller actually see it.

Without this, #331 alone changes a refused write from `False` to `None` for
every Python consumer — still silent, just a different flavour of silent.

## Before and after

Same two miners, same calls. Before, both returned a bare `False`:

```
RuntimeError: HTTP error: 412: {"message":"BOSminer is not running"}
RuntimeError: HTTP error: 400: {"message":"group name '' length (0) is
             out-of-range (min: Some(1), max: None)"}
```

A write that lands still returns `True`. Verified against BOS+ 26.01 and 26.08
on live hardware.

## Why raise here rather than return `Option`

`upgrade_firmware` already returns `PyResult<bool>` and raises through
`PyRuntimeError`, and the type stub already declares it `Awaitable[bool]` while
the `.ok()` setters are `Awaitable[bool | None]`. The distinction exists in the
API today — this moves one more consequential mutation onto the right side of
it. `upgrade_firmware` can leave a machine unbootable; `set_pools_config`
silently redirects hashrate to the wrong pool. Neither has a sensible `None`.

The getters keep returning `Option`, where an absent reading is a real answer.

## Worth noting beyond the pool case

While testing tuning calls on the same fleet I hit `set_tuning_config`
returning `None` on ePIC PowerPlay and spent a while on it before reading the
Rust, where the cause is stated plainly:

```rust
let Some(scaling) = scaling_config else {
    anyhow::bail!("ScalingConfig is required for ePIC PowerPlay")
};
```

The library knew exactly what was wrong, said so, and `.ok()` discarded it —
the same failure mode as the pool bug, in a completely different backend. Three
independent instances in one week is what convinced me this is worth changing
rather than working around.

## Scope

This leaves `set_pools_config` differing from `set_power_limit`,
`set_tuning_percent`, `set_scaling_config` and `set_fan_config`, which still
swallow. I would rather move those in a separate change than fold an API-wide
sweep into a bugfix — but if you would prefer they move together, say so and I
will do them all here.

The `.pyi` stub is updated to match. If it is generated rather than
hand-maintained, tell me the command and I will regenerate instead.


## Comments

### b-rowan on 2026-08-19

> but if you would prefer they move together, say so and I
> will do them all here.
> 
> 

Might as well do them all here, this change makes sense so best to keep the API consistent.


> The .pyi stub is updated to match. If it is generated rather than
> hand-maintained, tell me the command and I will regenerate instead.

This should get regenerated automatically by the pre-commit hooks.  Can't remember if it also gets fixed in CI here, but just run the pre-commit and should be good.


### cryptographicturk on 2026-08-20

Both done, thanks.

**All mutations now raise.** `set_fault_light`, `restart`, `pause`, `resume`, `factory_reset`, `change_password`, `set_power_limit`, `set_tuning_percent`, `set_scaling_config`, `set_tuning_config` and `set_fan_config` join `set_pools_config` and `upgrade_firmware`. Twelve in total.

I left `Option` on the seven reads — the five `get_*_config`, plus `read_logs` and `revalidate`. The first six are straightforward; `revalidate` is the judgement call, since its `False` already means something specific ("offline, or no longer valid for this backend") and it does not change miner state. Happy to move either of the last two if you would rather the line sat elsewhere.

I also dropped the note on `set_pools_config` explaining why it raised — with the whole surface behaving this way, it was describing the rule rather than an exception.

**Stubs regenerated** with `uvx maturin generate-stubs` via the hook rather than hand-edited. The generated file splits along the same line, which is a decent check that the rule is applied consistently: `Awaitable[bool]` for the twelve mutations, `Awaitable[... | None]` for the seven reads.

`cargo fmt --check`, `clippy --all-targets --all-features --workspace`, and `cargo test --all --locked` are clean.

One behaviour worth flagging, verified on live hardware. `set_power_limit` returns `True` where it lands. On a BOS+ unit whose BOSminer is stopped it returns `False` — not a raise — because that backend still ends in `.is_ok()` and collapses its own error to `Ok(false)`. That is the layering working as intended: the binding no longer hides an error, and does not manufacture one either. Those backend-level `.is_ok()` calls (antminer, whatsminer, vnish, and the braiins GraphQL restart) are still the follow-up I mentioned in #331.
