# bitaxeorg/ESP-Miner issue #1776: array sizing for

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1776
> Collected: 2026-10-07
> Published: 2026-06-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1776
- State: closed
- Author: WantClue
- Opened: 2026-06-19
- Closed: 2026-09-09
- Labels: enhancement

## Description

https://github.com/bitaxeorg/ESP-Miner/pull/1754#issuecomment-4667245517

## Comments

### realPJL on 2026-07-26

> There is an `ARRAY_SIZE` macro in use, but it's now defined in two separate places (`display.c` and `device_config.c`). Maybe extract that to a general place (maybe `utils.h`?) so it can also be used here.

Just so you don't have to open #1754 all the time

Is this still available?

### WantClue on 2026-08-06

yes this is still available and should be handled in a seperate PR if you want to do that would be appreciated if you already opened a PR please link the PR 

> > There is an `ARRAY_SIZE` macro in use, but it's now defined in two separate places (`display.c` and `device_config.c`). Maybe extract that to a general place (maybe `utils.h`?) so it can also be used here.
> 
> Just so you don't have to open [#1754](https://github.com/bitaxeorg/ESP-Miner/pull/1754) all the time
> 
> Is this still available?



### realPJL on 2026-08-14

Just created the PR #1879
