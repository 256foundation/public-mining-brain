# bitaxeorg/ESP-Miner issue #50: Stratum V1 mining.configure sent out of order

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/50
> Collected: 2026-10-07
> Published: 2023-10-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 50
- State: closed
- Author: checksum0
- Opened: 2023-10-22
- Closed: 2023-10-22
- Labels: none

## Description

Per BIP0310, mining.configure SHOULD be the first message sent to the pool after the connection.

While it should not cause too many problem, it might cause pool to ignore the mining.configure message, creating issue with ASICBoosted shares being submitted.

## Comments

### checksum0 on 2023-10-22

PR #51 fixes this.

### checksum0 on 2023-10-22

I remarked also that the method only send the mining.configure message and discard the pool reply. Assuming all pools will support 1fffe000 rolling mask forever is a dangerous assumption, not all pool currently support that mask to begin with.
