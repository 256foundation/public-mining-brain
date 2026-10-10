# bitaxeorg/ESP-Miner issue #1579: Fix Self Test after #1559

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1579
> Collected: 2026-10-07
> Published: 2026-02-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1579
- State: closed
- Author: benjamin-wilson
- Opened: 2026-02-25
- Closed: 2026-02-26
- Labels: bug, critical

## Description

This PR changed the hashrate calculation function parameter from using ms to us without updating all calling methods.  

Caused by #1559 


## Comments

### benjamin-wilson on 2026-02-25

After this is fixed this should probably be hotfix released. 

### WantClue on 2026-02-25

ACK

### mutatrum on 2026-02-26

Pushed a fix for review. To prevent this, we might need to use unit-specific types, something like this:
```
typedef int64_t time_us_t;
typedef int64_t time_ms_t;
typedef int64_t time_sec_t;
```
Not sure if that'll work, but worth a look at.
