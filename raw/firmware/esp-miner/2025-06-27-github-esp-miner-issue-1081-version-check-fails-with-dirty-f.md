# bitaxeorg/ESP-Miner issue #1081: Version check fails with dirty flag mismatch

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1081
> Collected: 2026-10-07
> Published: 2025-06-27

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1081
- State: closed
- Author: mutatrum
- Opened: 2025-06-27
- Closed: 2025-06-27
- Labels: none

## Description

#1006 
```
E (2097) http_server: Firmware (v2.9.0b5-2-gc501769) and AxeOS (v2.9.0b5-2-gc501769-dirty) versions do not match. Please make sure to update both www.bin and esp-miner.bin.
```

![Image](https://github.com/user-attachments/assets/e878376e-4404-4efd-bab1-0c61864331d3)

## Comments

### mutatrum on 2025-06-27

I tried removing the `--dirty` flag from `generate-version.js`, but that's not the solution.

The firmware can have the dirty flag:

![Image](https://github.com/user-attachments/assets/edae9e7d-6237-45e1-b287-d0b22d3565c1)

Not sure how the first one happened now. 😕 

### mutatrum on 2025-06-27

Note to self: don't save files during a build.
