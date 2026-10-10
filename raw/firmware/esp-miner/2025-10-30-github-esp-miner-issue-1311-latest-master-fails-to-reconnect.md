# bitaxeorg/ESP-Miner issue #1311: latest master fails to reconnect or switch if pool goes down

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1311
> Collected: 2026-10-07
> Published: 2025-10-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1311
- State: closed
- Author: 0xf0xx0
- Opened: 2025-10-30
- Closed: 2025-11-01
- Labels: none

## Description

**Describe the bug**
If the pool goes down while mining, latest master will fail to reconnect or switch to the fallback pool.

**To Reproduce**
Steps to reproduce the behavior:
1. Mine to a local pool
2. Shut down the pool
3. Restart it
4. Watch the axe never rejoin (and see its logs)

**Additional context**
Offending commit is 3bf3eed/#1292


## Comments

### duckaxe on 2025-10-30

Duplicate of https://github.com/bitaxeorg/ESP-Miner/issues/1248 ?

### 0xf0xx0 on 2025-10-30

i dont think so, 1248 is for switching at boot 🤔 

### 0xf0xx0 on 2025-11-01

forgot to mark closed by #1312
