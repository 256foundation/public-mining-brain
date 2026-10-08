# bitaxeorg/ESP-Miner issue #1328: Reset error register after frequency change

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1328
> Collected: 2026-10-07
> Published: 2025-11-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1328
- State: open
- Author: mutatrum
- Opened: 2025-11-05
- Closed: n/a
- Labels: enhancement

## Description

On some ASICs, the error register increases quite a bit whenever the frequency changes, including the initial frequency ramp-up at boot, sometimes in resulting in an error counter above 1000 immediately. Resetting the error counter after a frequency change will reduce user confusion.
