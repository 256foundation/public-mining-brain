# bitaxeorg/ESP-Miner issue #1551: Store total uptime and total hashes

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1551
> Collected: 2026-10-07
> Published: 2026-02-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1551
- State: closed
- Author: mutatrum
- Opened: 2026-02-13
- Closed: 2026-08-12
- Labels: none

## Description

Updating a counter every second will wear the NVS out. However, assuming a 24kb NVS partition:

<img width="350" alt="Image" src="https://github.com/user-attachments/assets/ba4e18df-0f10-466f-a0a5-397697a6bcba" />

once a minute should be doable actually.

As for the total work, we could use `log2_work`:

> It is the 2-logarithm of the expected number of block header hash attempts were necessary the build the chain up to that point.
