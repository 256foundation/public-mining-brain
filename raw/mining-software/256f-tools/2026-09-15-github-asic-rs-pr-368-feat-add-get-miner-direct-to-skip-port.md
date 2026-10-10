# 256foundation/asic-rs pull request #368: Feat: add get_miner_direct to skip port pre-check

> Source: https://github.com/256foundation/asic-rs/pull/368
> Collected: 2026-10-07
> Published: 2026-09-15

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 368
- State: closed
- Author: nkatha23
- Opened: 2026-09-15
- Closed: 2026-09-15
- Labels: none

## Description

`MinerFactory::get_miner(ip)` runs a TCP port pre-check against ports 80, 4028, 4029, and 8889 before attempting firmware identification. This is the right default for bulk scanning, but the wrong behaviour when the caller already holds a live connection to the miner, imo. 

In pool software, miners dial the pool over Stratum. The pool has a live session and knows theminer's IP, but management ports are often firewalled for inbound probes. `get_miner` returns `Ok(None)`,  indistinguishable from the miner being
offline.

This PR Adds `MinerFactory::get_miner_direct(ip)`: same panic-catch and identification timeout as `get_miner`, but calls `get_miner_inner`directly without the port pre-check.

PS: `send_rpc_command` hardcodes port 4028, which causes port collisionsbetween parallel tests. Worked around with a static mutex for now.Making ports configurable per-factory can be worked on separately as a follow-up.
