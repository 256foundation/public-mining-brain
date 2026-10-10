# 256foundation/asic-rs issue #392: Expose hashboard enable/disable controls through the Miner API

> Source: https://github.com/256foundation/asic-rs/issues/392
> Collected: 2026-10-07
> Published: 2026-09-24

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 392
- State: closed
- Author: cfilipescu
- Opened: 2026-09-24
- Closed: 2026-09-24
- Labels: none

## Description

## Problem

The `Miner` API exposes hashboard data, but it does not provide a high-level operation to enable or disable individual hashboards. Applications that need this must call firmware-specific APIs directly.

For example, an application using EPic/UMC OS currently has to read capabilities and summary data, determine which supported boards are disabled, then call the firmware's `boardenable` endpoint. That logic cannot be reused for miners running firmware with a different control API.

## Request

Please consider adding a capability-checked hashboard enable/disable API to `asic-rs`, implemented by firmware backends where supported. Callers should be able to check whether a backend supports the operation and set the enabled state for selected board indices. A helper for enabling all supported disabled boards could then be built on top of that API.

The API should report unsupported firmware or boards clearly and preserve firmware-specific validation of available board indices.

## Use case

Fleet management tools need to re-enable hashboards that an operator has disabled or that firmware has disabled after a fault, without embedding one firmware's HTTP API in the application.
