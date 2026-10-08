# 256foundation/asic-rs issue #347: Expose a non-mutating firmware preflight and resolution API

> Source: https://github.com/256foundation/asic-rs/issues/347
> Collected: 2026-10-07
> Published: 2026-08-28

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 347
- State: closed
- Author: cfilipescu
- Opened: 2026-08-28
- Closed: 2026-09-10
- Labels: enhancement

## Description

## Problem

Library consumers need to validate firmware inputs without uploading them or duplicating backend-specific parsers.

Today, `UpgradeFirmware::upgrade_firmware` is the only public path that performs backend-specific preparation. For stock Antminers, BMU parsing, CRC validation, nested-bundle handling, and model/subtype payload resolution live privately inside the Antminer backend. A consumer can read a BMU to catch file I/O errors, but cannot validate its structure or confirm that it contains a compatible payload without starting the real upgrade.

## Proposed direction

Expose a non-mutating backend API for firmware preflight or preparation, for example a trait method conceptually similar to:

```rust
async fn prepare_firmware(
    &self,
    image: FirmwareImage,
) -> anyhow::Result<PreparedFirmware>;
```

The exact API is open for design, but it should:

- Read and validate backend-specific container structure and integrity.
- Use live miner metadata where required to resolve the compatible payload.
- Return useful selected-payload metadata or a prepared image without uploading it.
- Be reused by `upgrade_firmware` so preflight and real-upgrade validation cannot diverge.
- Perform no mutating request to the miner.

## Acceptance criteria

- Antminer BMU preflight reports malformed headers, truncation, CRC failures, excessive nesting, and no compatible model/subtype entry.
- Consumers do not need to copy private BMU parsing or selection rules.
- Actual firmware upgrades use the same preparation and validation implementation.
- The API is general enough for other backends and firmware containers.

## Comments

### b-rowan on 2026-08-31

Concept ACK.  I assume you want to implement with the self-assignment?
