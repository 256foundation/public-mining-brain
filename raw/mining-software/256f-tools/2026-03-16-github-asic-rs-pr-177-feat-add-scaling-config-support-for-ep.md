# 256foundation/asic-rs pull request #177: feat: add scaling config support for epic backend

> Source: https://github.com/256foundation/asic-rs/pull/177
> Collected: 2026-10-07
> Published: 2026-03-16

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 177
- State: closed
- Author: cfilipescu
- Opened: 2026-03-16
- Closed: 2026-03-16
- Labels: none

## Description

## Summary
- add `ScalingConfig` support in core, including optional `algorithm` metadata for firmware-specific requirements
- extend `Miner` trait bounds to include `SupportsScalingConfig`, and add default `supports_scaling_config = false` impls across non-ePIC backends
- implement ePIC scaling config parsing from `/summary` `PerpetualTune.Algorithm` and expose it through the live test path
