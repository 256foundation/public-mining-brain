# bitaxeorg/ESP-Miner issue #517: FEAT: Implemented stratum client.reconnect

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/517
> Collected: 2026-10-07
> Published: 2024-11-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 517
- State: closed
- Author: benjamin-wilson
- Opened: 2024-11-26
- Closed: 2024-11-26
- Labels: none

## Description

CK's switch to new hardware made it apparent we do not implemented the stratum client.reconnect functionality. 

## Comments

### skot on 2024-11-26

`client.reconnect("hostname", port, waittime)`

I always thought that was a pretty sketchy command for an unencrypted conection..

### benjamin-wilson on 2024-11-26

Fair enough,
