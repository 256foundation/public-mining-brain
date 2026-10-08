# bitaxeorg/ESP-Miner issue #775: Handle share count and share reject reasons from secondary pool

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/775
> Collected: 2026-10-07
> Published: 2025-03-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 775
- State: closed
- Author: mutatrum
- Opened: 2025-03-17
- Closed: 2025-06-27
- Labels: question

## Description

Currently, when the machine fails over to the secondary pool, the share count and share reject reasons continues counting:

Primary pool is ckpool, secondary pool is public-pool, and the lower two share reject reasons are coming from the secondary pool:

![Image](https://github.com/user-attachments/assets/ce30dfed-7cae-4054-bcbe-87e05cecd611)

I'm not sure how to handle this though. My first thought is to split the share count and reject reasons between primary and secondary pool, but this might be confusing when it switches over. Another option is to just reset everything when it connects to a pool either primary or secondary, but that would means the statistics are for the pool uptime, not the miner uptime, don't really like that.

(Also: it should have been sorted by count descending.)

## Comments

### WantClue on 2025-06-27

fixed by #847
