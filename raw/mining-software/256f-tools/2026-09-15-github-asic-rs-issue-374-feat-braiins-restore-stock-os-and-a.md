# 256foundation/asic-rs issue #374: feat(braiins): restore stock OS and accept empty success responses

> Source: https://github.com/256foundation/asic-rs/issues/374
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 374
- State: closed
- Author: cfilipescu
- Opened: 2026-09-15
- Closed: 2026-09-16
- Labels: bug, enhancement

## Description

## Goal

Implement the Braiins OS restore-stock endpoint and correct successful empty-body handling in the REST client.

## Scope

- Treat successful 204 or otherwise empty HTTP responses as success instead of forcing JSON decoding.
- Preserve JSON decoding for non-empty successful responses.
- Add `POST /api/v1/upgrade/restore-stock` to the v26.04 backend.
- Implement `RestoreStockOs` for v26.04 only; keep older backends unsupported.
- Preserve HTTP status and response body for 409 task conflicts and 501 unsupported platforms.
- Keep `factory_reset()` settings-only.

## Acceptance criteria

- Restore-stock accepts HTTP 204 as a started operation.
- Existing v26.04 factory reset also succeeds on HTTP 204.
- BMM and SD-card 501 responses remain actionable errors.
- Tests cover 204, 409, and 501 without contacting hardware.

## Dependencies

Blocked by #371.
