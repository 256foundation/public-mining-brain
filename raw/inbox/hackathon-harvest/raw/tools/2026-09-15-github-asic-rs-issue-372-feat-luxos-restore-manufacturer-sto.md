# 256foundation/asic-rs issue #372: feat(luxos): restore manufacturer stock OS

> Source: https://github.com/256foundation/asic-rs/issues/372
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 372
- State: closed
- Author: cfilipescu
- Opened: 2026-09-15
- Closed: 2026-09-16
- Labels: enhancement

## Description

## Goal

Implement LuxOS stock-OS restoration through its authenticated TCP RPC API.

## Scope

- Add the LuxOS RPC wrapper for `uninstallluxos`.
- Reuse the existing session authentication and send the session ID in `parameter`.
- Implement `RestoreStockOs` for `LuxMinerV1`.
- Map an accepted RPC response to the shared restore result.
- Do not route this operation through `factory_reset()`.

## Acceptance criteria

- The request uses TCP port 4028 with `command: uninstallluxos`.
- The command is privileged and includes a valid session ID.
- RPC rejection is returned as an error.
- `supports_restore_stock_os()` is true for LuxOS.
- Tests use mocked protocol responses and never contact real hardware.

## Dependencies

Blocked by #371.
