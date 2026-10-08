# 256foundation/mujina issue #110: build(deps): require cargo 1.100 and drop the nightly cooldown workaround

> Source: https://github.com/256foundation/mujina/issues/110
> Collected: 2026-10-07
> Published: 2026-09-04

- Repository: 256foundation/mujina
- Type: issue
- Number: 110
- State: open
- Author: rkuester
- Opened: 2026-09-04
- Closed: n/a
- Labels: none

## Description

Cargo 1.100 will stabilize `min-publish-age`, which #109 enables on cargo nightly via the `[unstable]` table in `.cargo/config.toml`. Once 1.100 is released:

- Drop the `[unstable]` table from `.cargo/config.toml`.
- Drop the `+nightly` from the `deps` recipes in the justfile.
- Require 1.100 through `rust-toolchain.toml` rather than `rust-version`, so Debian packaging keeps building with its own toolchain.
- Move the CI image in `build.Containerfile` to the 1.100 tag.

Until then, a plain `cargo add` or `cargo update` using cargo stable, instead of the just recipes in the `deps` group, ignores the cooldown. `just check-dep-cooldown` and the "Check dep cooldown" CI job catch the young version afterwards, but nothing stops it from entering `Cargo.lock` in the first place.


## Comments

### j-kon on 2026-09-05

Thanks for opening this. I’ve been following the dependency cooldown work from #104 and #109, so I’d be interested in helping with this once Cargo 1.100 is released and min-publish-age is stable.

The scope looks clear to me: remove the unstable config, drop +nightly from the dependency recipes, add the rust-toolchain.toml requirement, and update the CI image.

I’ll keep an eye on the Cargo 1.100 release and would be happy to pick this up when it becomes actionable.
