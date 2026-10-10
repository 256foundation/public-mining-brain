# 256foundation/asic-rs issue #375: feat(epic): restore stock OS on supported UMC OS builds

> Source: https://github.com/256foundation/asic-rs/issues/375
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 375
- State: closed
- Author: cfilipescu
- Opened: 2026-09-15
- Closed: 2026-09-16
- Labels: enhancement

## Description

## Goal

Implement the authenticated UMC OS uninstall endpoint without advertising it on PowerPlay builds that do not expose the route.

## Scope

- Add `POST :4028/uninstall` with `{"param": null, "password": "..."}`.
- Parse the legacy `{"result": bool, "error": ...}` response and surface failures.
- Detect support non-destructively from `GET :4028/openapi.json` by checking for `paths./uninstall.post`.
- Store the detected capability on `PowerPlayV1`.
- Report support only for stock-controller UMC OS builds; PowerPlay/ePIC-controller builds remain unsupported.
- Document that success means the uninstall script was queued, not completed.

## Acceptance criteria

- Amlogic, BeagleBoard, and Xilinx UMC OS builds with the route report support.
- OpenAPI documents without `/uninstall` report unsupported.
- Authentication and `param: null` match the server contract.
- Missing-script and execution errors returned by the API are surfaced.
- Tests use mocked HTTP responses only.

## Dependencies

Blocked by #371.
