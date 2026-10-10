# 256foundation/mujina pull request #112: docs: point Bitaxe users at rhapd-bitaxe-gamma

> Source: https://github.com/256foundation/mujina/pull/112
> Collected: 2026-10-07
> Published: 2026-09-26

- Repository: 256foundation/mujina
- Type: pull request
- Number: 112
- State: closed
- Author: rkuester
- Opened: 2026-09-26
- Closed: 2026-10-05
- Labels: none

## Description

Point the README, the Bitaxe Gamma board guide, and the issue triage template at [rhapd-bitaxe-gamma](https://github.com/256foundation/rhapd-bitaxe-gamma) in place of the deprecated [bitaxe-raw](https://github.com/bitaxeorg/bitaxe-raw), and call the management channel RHAP in the architecture examples. People still build bitaxe-raw because nothing in the docs points them away from it (for example, [bitaxe-raw#17](https://github.com/bitaxeorg/bitaxe-raw/pull/17#issuecomment-5703306796)). Mujina still drives boards running bitaxe-raw, and the board guide says so.

The RHAP naming came up on the [20260831 dev call](https://github.com/256foundation/mujina/discussions/108). The bitaxe-raw protocol document and modules keep their names until the RHAP spec is published.
