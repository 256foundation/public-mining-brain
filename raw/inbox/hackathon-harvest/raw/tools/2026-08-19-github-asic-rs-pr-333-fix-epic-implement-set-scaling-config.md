# 256foundation/asic-rs pull request #333: fix(epic): implement set_scaling_config instead of reporting false support

> Source: https://github.com/256foundation/asic-rs/pull/333
> Collected: 2026-10-07
> Published: 2026-08-19

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 333
- State: closed
- Author: cryptographicturk
- Opened: 2026-08-19
- Closed: 2026-08-20
- Labels: none

## Description

## What

`supports_scaling_config()` returns `true` for PowerPlay, but the backend only
ever implemented `parse_scaling_config` — so `set_scaling_config` fell through
to the trait default:

```rust
anyhow::bail!("Setting scaling config is not supported on this platform");
```

PowerPlay is the only backend in the repo whose flag says `true`, and no backend
anywhere implements the setter. A caller that correctly checks the capability
before writing still fails, and fails silently, because the Python binding maps
the error to `None`.

## The fix

Scaling *is* settable on PowerPlay — it just has no endpoint of its own.
`min_throttle` and `throttle_step` are written by the same
`perpetualtune/algo` call that sets the tuning target, which is why #330's live
test passes the current scaling config through `set_tuning_config`.

This is that observation in reverse: read the current tuning config, resend it
with the new scaling. Reading first is the necessary part — without it a
scaling-only write would clobber the tuning target.

```rust
async fn set_scaling_config(&self, config: ScalingConfig) -> anyhow::Result<bool> {
    let current = self.get_tuning_config().await?;
    self.set_tuning_config(current, Some(config)).await
}
```

## Verified

Against a PowerPlay-BMS v1.24.0 unit (Antminer S19j Pro, `BoardTune`, 70 TH/s
target):

```
before:   scaling step=5 min=10   tuning 70 TH/s BoardTune
set_scaling_config(step=7, min=15) -> True
          CHANGED within 5s -> step=7 min=15
          tuning target preserved: 70 TH/s BoardTune
restored: scaling step=5 min=10   tuning 70 TH/s BoardTune
```

The live test added here follows #330's convention and asserts the target
preservation, not just that the write returned `true` — a write that reports
success without changing anything is the failure mode I was chasing in #331.

`cargo clippy` clean; the crate's tests pass (9 passed, 4 ignored live tests).

## One deliberate omission

Asserting the tuning config is unchanged wants `PartialEq` on `TuningConfig`,
which does not exist today. Deriving it would pull `asic-rs-core` into an
epic-only change, so the test compares serialised JSON instead. Happy to add the
derive in a separate PR if you would rather have it.


## Comments

### b-rowan on 2026-08-19

> Asserting the tuning config is unchanged wants PartialEq on TuningConfig,
> which does not exist today. Deriving it would pull asic-rs-core into an
> epic-only change, so the test compares serialised JSON instead. Happy to add the
> derive in a separate PR if you would rather have it.

@cfilipescu thoughts?  Will leave this one up to you.
