# 256foundation/asic-rs issue #377: test: validate stock OS restoration capability and request contracts

> Source: https://github.com/256foundation/asic-rs/issues/377
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 377
- State: closed
- Author: cfilipescu
- Opened: 2026-09-15
- Closed: 2026-09-18
- Labels: documentation, enhancement

## Description

## Goal

Complete cross-backend validation for stock-OS restoration while guaranteeing that tests never trigger a real uninstall.

## Scope

- Add or consolidate mocked contract coverage for LuxOS, VNish, Braiins, and ePIC.
- Verify unsupported backends remain false.
- Verify factory reset remains independent and settings-only.
- Verify successful restore results mean accepted/started rather than completed.
- Regenerate and verify the supported-devices matrix and public API documentation.
- Run formatting, Clippy, unit tests, Python tests, FFI checks, and Go tests relevant to the complete feature.

## Acceptance criteria

- Every destructive request is tested only against mocks or fixtures.
- Version- and platform-specific capability behavior is covered.
- Generated documentation exposes separate Factory Reset Settings and Restore Stock OS capabilities.
- The complete workspace and binding validation passes.

## Dependencies

Blocked by #371, #372, #373, #374, #375, and #376.
