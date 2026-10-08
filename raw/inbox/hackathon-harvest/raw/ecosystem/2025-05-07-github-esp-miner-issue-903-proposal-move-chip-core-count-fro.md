# bitaxeorg/ESP-Miner issue #903: proposal: move chip core count from /api/system/info to /api/system/asic (and remove more hw-specific code from axeos)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/903
> Collected: 2026-10-07
> Published: 2025-05-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 903
- State: closed
- Author: 0xf0xx0
- Opened: 2025-05-07
- Closed: 2025-05-28
- Labels: none

## Description

since /api/system/asic is for chip info, it seems right to move the core count and small core count there. adding the default frequency and voltage would also allow for removing this hw-specific code https://github.com/bitaxeorg/ESP-Miner/blob/7be12ea14dcc52dfef07bdcadf50615f45ef1003/main/http_server/axe-os/src/app/components/edit/edit.component.ts#L37-L49  
and adding an (optional?) color field would let us remove this bit.
https://github.com/bitaxeorg/ESP-Miner/blob/7be12ea14dcc52dfef07bdcadf50615f45ef1003/main/http_server/axe-os/src/app/components/swarm/swarm.component.html#L88-L93

## Comments

### mutatrum on 2025-05-08

Take a look at #857. Ideally the whole device config structure should be in `/api/system/asic`. The color field is also added in that branch, but not used in the frontend yet.

### mutatrum on 2025-05-28

Closed by #857, and more context in #945.
