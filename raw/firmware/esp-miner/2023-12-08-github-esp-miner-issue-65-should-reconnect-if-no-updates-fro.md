# bitaxeorg/ESP-Miner issue #65: Should reconnect if no updates from stratum after a certain amount of time

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/65
> Collected: 2026-10-07
> Published: 2023-12-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 65
- State: closed
- Author: johnny9
- Opened: 2023-12-08
- Closed: 2024-12-01
- Labels: none

## Description

If the pool has dropped the miner's subscription but the tcp connection is still active the Bitaxe can get stuck mining for nothing. We need to have a sanity timer to restart the connection/subscription so it doesn't get stuck.

## Comments

### benjamin-wilson on 2023-12-08

ACK Yes, needed badly 

### skot on 2024-10-10

This is the goal of #272 

### WantClue on 2024-12-01

Has been fixed with #363
