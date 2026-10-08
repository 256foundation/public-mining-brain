# 256foundation/asic-rs issue #371: feat(core): separate stock OS restore from factory reset

> Source: https://github.com/256foundation/asic-rs/issues/371
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 371
- State: closed
- Author: cfilipescu
- Opened: 2026-09-15
- Closed: 2026-09-15
- Labels: enhancement

## Description

## Goal

Introduce a dedicated API for uninstalling third-party firmware and restoring the manufacturer stock OS. This operation must remain semantically separate from `factory_reset()`, which only restores default miner settings and does not change the installed OS.

## Scope

- Add a `RestoreStockOs` trait with `restore_stock_os()` and `supports_restore_stock_os()`.
- Add a result model that makes request acceptance explicit and can carry an optional reboot delay.
- Add the trait to the object-safe `Miner` composition and blanket bounds.
- Add unsupported implementations for every existing backend so the workspace continues to compile.
- Clarify the `FactoryReset` documentation as settings-only behavior.
- Do not add vendor endpoint calls in this issue.

## Semantics

- `factory_reset()` restores default/stock settings while retaining the current OS.
- `restore_stock_os()` removes the aftermarket OS and initiates restoration of the manufacturer OS.
- A successful result means the restore request was accepted or started; it does not mean the device has completed rebooting.

## Acceptance criteria

- The new API is callable through `dyn Miner`.
- Existing factory reset behavior is unchanged.
- Unsupported backends report `supports_restore_stock_os() == false`.
- The workspace compiles and existing tests continue to pass.

## Dependencies

None.

Blocks #372, #373, #374, #375, #376, and #377.

## Implementation

Tracked by #378.
