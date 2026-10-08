# bitaxeorg/ESP-Miner issue #194: Display hashrate updates too slowly on high diff pools

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/194
> Collected: 2026-10-07
> Published: 2024-06-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 194
- State: closed
- Author: skot
- Opened: 2024-06-01
- Closed: 2024-06-03
- Labels: bug

## Description

Now that we have a fix for #190 and we are always using the pool diff, it seems like the display updates way too slow on higher min diff pools.

It prolly makes sense to calculate the hashrate on every chip share, not just pool shares. This will still need some smoothing.

## Comments

### skot on 2024-06-03

this fix is in 4bda726
