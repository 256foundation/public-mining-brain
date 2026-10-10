# bitaxeorg/ESP-Miner issue #1383: Filter out `Method not found` on failed setup messages as rejected share reasons

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1383
> Collected: 2026-10-07
> Published: 2025-11-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1383
- State: open
- Author: mutatrum
- Opened: 2025-11-24
- Closed: n/a
- Labels: none

## Description

Some pools (f.e. Ocean) don't accept `mining.suggest_difficulty` and `mining.extranonce.subscribe`:
```
₿ (25228) system: Syncing clock
₿ (25231) create_jobs_task: New Work Dequeued 692374e64ec09303
₿ (25231) stratum_task: Block height 924898
₿ (25237) create_jobs_task: New pool difficulty 131072
₿ (25242) stratum_task: Scriptsig: .< OCEAN.XYZ >.Sinnx3 Mining.....@..V..A
₿ (25248) create_jobs_task: Set chip version rolls 65535
₿ (25256) stratum_api: rx: {"error":null,"id":3,"result":true}
₿ (25268) stratum_task: setup message accepted
₿ (25273) stratum_api: tx: {"id": 4, "method": "mining.suggest_difficulty", "params": [4657]}
₿ (25283) stratum_api: tx: {"id": 5, "method": "mining.extranonce.subscribe", "params": []}
₿ (25360) stratum_task: Stratum response time: 77.17 ms
₿ (25362) stratum_api: rx: {"error":[-3,"Method not found",null],"id":4,"result":null}
₿ (25365) stratum_task: setup message rejected: Method not found
₿ (25439) stratum_api: rx: {"error":[-3,"Method not found",null],"id":5,"result":null}
₿ (25440) stratum_task: message result rejected: Method not found
```

However, these are registered as failed shares with `Method not found` as reject reason, which is incorrect. These can be safely ignored.
