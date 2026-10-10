# 256foundation/mujina pull request #107: feat(bitaxe): support the RHAP-D firmware

> Source: https://github.com/256foundation/mujina/pull/107
> Collected: 2026-10-07
> Published: 2026-08-30

- Repository: 256foundation/mujina
- Type: pull request
- Number: 107
- State: closed
- Author: rkuester
- Opened: 2026-08-30
- Closed: 2026-08-30
- Labels: none

## Description

Match Bitaxe Gamma boards running [RHAP-D](https://github.com/256foundation/rhapd-bitaxe-gamma), the successor to [bitaxe-raw](https://github.com/bitaxeorg/bitaxe-raw), alongside boards still running bitaxe-raw. RHAP-D enumerates as 1209:6102, the pid.codes allocation to the Bitaxe project, with product string "Bitaxe Gamma RHAP-D", and answers with the v1 response frame the EmberOne firmware also uses, so a second descriptor selects the format by product string. bitaxe-raw boards match as before and keep the v0 frame. Verified on a Bitaxe Gamma running each firmware.
