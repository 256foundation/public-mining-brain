# 256foundation/mujina pull request #79: feat(tracing): add MUJINA_LOG filter variable

> Source: https://github.com/256foundation/mujina/pull/79
> Collected: 2026-10-07
> Published: 2026-07-15

- Repository: 256foundation/mujina
- Type: pull request
- Number: 79
- State: closed
- Author: rkuester
- Opened: 2026-07-15
- Closed: 2026-07-15
- Labels: none

## Description

Add MUJINA_LOG, a log filter for Mujina's own output. Interpret its directives relative to Mujina's crate, overriding RUST_LOG and the built-in defaults. Give RUST_LOG its standard Rust meaning: a directive that names a crate adds to the built-in defaults, and a bare level takes full control of the filter.

    MUJINA_LOG=trace               trace Mujina, nothing more
    MUJINA_LOG=asic::bm13xx=trace  module names as the log shows them
    RUST_LOG=nusb=trace            trace a dependency, defaults kept
    RUST_LOG=trace                 trace everything, as stock Rust

Previously the filter appended a bare RUST_LOG level after the defaults, where the per-crate default outranked it by specificity: RUST_LOG=trace promoted third-party crates to trace but left Mujina capped at info, exactly backwards from what a user asking for a trace log wants.

Update the startup hint, environment help, and docs to recommend MUJINA_LOG.


## Comments

### winterrdog on 2026-07-16

yeah, confirmed this makes investigating logs much easier.

i was using it while chasing down an issue around the power controller on a bitaxe gamma 602, and having targeted Mujina traces (_for my case_) without turning the rest of the world into `trace` made the debugging experience smoother
