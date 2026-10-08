# bitaxeorg/ESP-Miner issue #1808: Fix inverted environment.mock checks in SystemApiService.updateSystem

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1808
> Collected: 2026-10-07
> Published: 2026-07-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1808
- State: closed
- Author: skot
- Opened: 2026-07-10
- Closed: 2026-07-10
- Labels: none

## Description

## Description

`SystemApiService.updateSystem()` checks `environment.mock` before invoking the generated API client or making an HTTP PATCH request:

```ts
if (environment.mock && this.api && !uri) {
  return from(this.api.invoke(functions.updateSystemSettings, { body: update as Settings }));
}

if (environment.mock && uri) {
  return this.httpClient.patch(`${uri}/api/system`, update);
}
```

This is inverted relative to the other methods in `system.service.ts`, which use real API transports only when `environment.mock` is false.

## Impact

In a non-mock build, `updateSystem()` skips both real API paths and falls through to the mock response. As a result, system-setting updates may appear to succeed without being sent to the device. In mock mode, it may unexpectedly attempt a real API request.

## Proposed fix

Negate both checks:

```ts
if (!environment.mock && this.api && !uri) {
  return from(this.api.invoke(functions.updateSystemSettings, { body: update as Settings }));
}

if (!environment.mock && uri) {
  return this.httpClient.patch(`${uri}/api/system`, update);
}
```

This makes `updateSystem()` consistent with `getInfo()`, `restart()`, and the other service methods.
