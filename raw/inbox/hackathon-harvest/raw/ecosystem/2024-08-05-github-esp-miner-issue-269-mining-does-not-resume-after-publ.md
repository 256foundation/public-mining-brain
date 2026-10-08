# bitaxeorg/ESP-Miner issue #269: mining does not resume after public-pool outage

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/269
> Collected: 2026-10-07
> Published: 2024-08-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 269
- State: closed
- Author: skot
- Opened: 2024-08-05
- Closed: 2024-12-27
- Labels: none

## Description

after public-pool went down for the fiber upgrade, none of my devices reconnected without a manual reset

## Comments

### skot on 2024-08-05

this was a sneaky outage.. it seemed like public-pool.io was still up, so maybe the socket didn't close, but no new work was being sent?

People reported their hashrate slowly dropping to zero and then never recovering.

### skot on 2024-08-06

I think the feature here would be to detect if no new `mining.notify` stratum messages have arrived within a certain timeout period.

### WantClue on 2024-08-14

An esp restart with a certain timer or an rst to the asic could solve this. 

### WantClue on 2024-12-27

fixed with the fallback implementation
