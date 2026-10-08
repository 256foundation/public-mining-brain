# bitaxeorg/ESP-Miner issue #621: bug: API formatting inconsistency

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/621
> Collected: 2026-10-07
> Published: 2025-01-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 621
- State: closed
- Author: b-rowan
- Opened: 2025-01-06
- Closed: 2026-10-02
- Labels: bug, enhancement, help wanted, good first issue, accepted

## Description

In `http_server.c`, there is one key being added to the API JSON which does not match the others.  `overheat_mode` should be changed to `overheatMode` to match the format of other parts of the API.

https://github.com/skot/ESP-Miner/blob/39a4c4164ae2f5474d1a891ec02d4cfa0251903c/main/http_server/http_server.c#L430

Is there a procedure for deprecating this from the API, in case someone is using it, so that it can be changed?

## Comments

### vortexopenclaw on 2026-06-01

I took a closer look at this as an issue-first writeup.

The compatibility concern in the original issue looks valid: changing `overheat_mode` directly to `overheatMode` would break any existing clients already reading the current API field. A safer path is to expose both fields for now:

- keep `overheat_mode` in `/api/system/info` for backward compatibility
- add `overheatMode` as the camelCase alias for generated/new clients
- update OpenAPI and AxeOS mock data so both fields are represented
- switch AxeOS display reads that do not need legacy compatibility over to `overheatMode`

That keeps the current API stable while giving the camelCase API a migration path.

Validation I ran on the proposed approach:

- AxeOS `npm run test:ci`: 33 tests passed
- `git diff --check`
- firmware `idf.py build`
- OTA smoke on Bitaxe Gamma: API/UI recovered after update, then the device was rolled back healthy

Reference implementation from the closed PR, if useful for discussion: #1739


### gregweir on 2026-07-24

Happy to pick this up. PR #1739 proposed adding `overheatMode` as a camelCase alias while keeping `overheat_mode` for backward compatibility (C emission, OpenAPI, and the AxeOS reads all preferring `overheatMode ?? overheat_mode`) — that seems like the right migration.

One open question: should `overheatMode` go in the OpenAPI `required` list (as #1739 did), or stay optional? I'm inclined to keep it `required` since firmware always emits it, but I'll follow your preference.

I'll open a fresh PR mirroring that approach unless you'd like it handled differently.

### 0xf0xx0 on 2026-07-25

@gregweir see #945 for discussion

### gregweir on 2026-07-25

Thanks — makes sense that this lives in the v2 work now (#945). Happy to help on the `/status` slice if useful; otherwise I'll leave it to you.
