# bitaxeorg/ESP-Miner issue #1157: Swarm - Best Diff. sorting incorrect

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1157
> Collected: 2026-10-07
> Published: 2025-07-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1157
- State: closed
- Author: Travetown
- Opened: 2025-07-22
- Closed: 2025-10-21
- Labels: none

## Description

In the swarm overview, the “Best Diff.” column is sorted incorrectly under certain circumstances. 
In my case, the Bitaxe with 1.01 G is rated as the smallest in descending order. There is no conversion to a common base when sorting.

<img width="294" height="196" alt="Image" src="https://github.com/user-attachments/assets/526fd6b3-679a-4d02-9b30-a00d1b105ebc" />

## Comments

### duckaxe on 2025-07-23

For devs: I would prefer that ESP return a number instead of a pre-formatted string. Formatting should happen in AxeOS. This will also work with sorting.
