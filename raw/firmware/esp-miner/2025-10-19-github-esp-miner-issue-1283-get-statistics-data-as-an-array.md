# bitaxeorg/ESP-Miner issue #1283: Get statistics data as an array

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1283
> Collected: 2026-10-07
> Published: 2025-10-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1283
- State: closed
- Author: terratec
- Opened: 2025-10-19
- Closed: 2025-12-05
- Labels: cleanup

## Description

To further simplify and minimize the mutex locks, it's probably more efficient to just copy the whole array into a temporary copy within a single mutex lock, instead of a lock per entry.

Not sure what's easier, return the whole array as-is, with current start/end, or do 2 memcpys into a fit-to-size array.

_Originally posted by @mutatrum in https://github.com/bitaxeorg/ESP-Miner/pull/1246#discussion_r2441753169_
            

## Comments

### mutatrum on 2025-12-05

Closed by #1246
