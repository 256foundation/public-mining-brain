# bitaxeorg/ESP-Miner issue #658: extranonce2 length from pool is ignored

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/658
> Collected: 2026-10-07
> Published: 2025-01-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 658
- State: closed
- Author: JKK1
- Opened: 2025-01-16
- Closed: 2025-01-27
- Labels: bug

## Description

The miner submits shares of extranonce size of 4 bytes while the pool is requesting shares of a size smaller.
To reproduce connect to a pool with extranonce size 3 like powerpool.io

Likely a bug in the stratum request handling part of the code.


## Comments

### skot on 2025-01-16

looking at this quickly it seems we are correctly parsing the extranonce_2 length from the stratum response, so the issue is prolly in `construct_coinbase_tx()` https://github.com/skot/ESP-Miner/blob/a04c00ba070dbfc61682041d944a6fa19857a90c/components/stratum/mining.c#L15-L28

or

`extranonce_2_generate()` https://github.com/skot/ESP-Miner/blob/a04c00ba070dbfc61682041d944a6fa19857a90c/components/stratum/mining.c#L113-L124
