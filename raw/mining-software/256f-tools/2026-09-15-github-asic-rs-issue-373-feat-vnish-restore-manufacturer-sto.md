# 256foundation/asic-rs issue #373: feat(vnish): restore manufacturer stock OS

> Source: https://github.com/256foundation/asic-rs/issues/373
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 373
- State: closed
- Author: cfilipescu
- Opened: 2026-09-15
- Closed: 2026-09-16
- Labels: enhancement

## Description

## Goal

Implement VNish firmware removal and return to the manufacturer stock OS.

## Scope

- Implement `POST /api/v1/firmware/remove` in both VNish backend generations.
- VNish 1.2.x sends no request body.
- VNish 1.3.x sends `{"remove_stock_logs": false}`.
- Parse the `after` response field into the shared reboot-delay result.
- Keep this operation separate from `POST /settings/factory-reset`, which restores settings only.

## Acceptance criteria

- `VnishV120` and `VnishV130` report stock-OS restoration support.
- Authentication uses the existing bearer/API-key flow.
- HTTP 400 model incompatibility is surfaced as an error.
- Tests cover both version-specific request formats and reboot-delay parsing.
- No test contacts real hardware.

## Dependencies

Blocked by #371.
