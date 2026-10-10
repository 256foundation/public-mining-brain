# 256foundation/mujina pull request #91: build: harden the dependency supply chain

> Source: https://github.com/256foundation/mujina/pull/91
> Collected: 2026-10-07
> Published: 2026-08-10

- Repository: 256foundation/mujina
- Type: pull request
- Number: 91
- State: closed
- Author: rkuester
- Opened: 2026-08-10
- Closed: 2026-08-10
- Labels: none

## Description

Defend the build against supply-chain attacks. After this series, every input to a build names exact content: crate versions in a committed `Cargo.lock`, cargo tools at versions specified in the justfile, GitHub Actions by commit hash, and container base images by digest. They are changed by the normal reviewable and traceable commit process.

Notes for review:

- `just setup-tools` installs cargo-cooldown and cargo-deny at exact versions when they are missing, and leaves an installed copy alone. The build container runs the same recipe, so one version source covers CI and dev machines.
- The first scheduled audit run is expected to fail: four known advisories are deliberately left in the lock (ruint, anyhow, paste, time). A real failure exercises the issue reporting; the fixes follow as ordinary updates.
- CONTRIBUTING.md gains a tool-setup step and an Updating Dependencies section.
