# 256foundation/asic-rs issue #376: feat(bindings): expose stock OS restoration across Python, FFI, and Go

> Source: https://github.com/256foundation/asic-rs/issues/376
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 376
- State: closed
- Author: cfilipescu
- Opened: 2026-09-15
- Closed: 2026-09-17
- Labels: enhancement

## Description

## Goal

Expose the stock-OS restoration capability and operation consistently across every supported language without changing factory-reset semantics.

## Scope

- Python: add `supports_restore_stock_os` and async `restore_stock_os()`.
- FFI/C: add the capability-map field, exported function, header declaration, and result conversion.
- Go: add the support field, result type, and client method.
- Export the shared result model where each binding requires it.
- Update API documentation so factory reset is explicitly settings-only and stock-OS restoration is a separate operation.

## Acceptance criteria

- Public names consistently use `restore_stock_os`.
- Factory reset APIs remain backward-compatible and settings-only.
- The support map distinguishes `factory_reset` from `restore_stock_os`.
- Binding builds and existing compatibility checks pass.

## Dependencies

Blocked by #371.

Integration should land after #372, #373, #374, and #375 so each supported backend can be exercised through the bindings.
