# bitaxeorg/ESP-Miner issue #84: Stratum messages out of order for some pools

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/84
> Collected: 2026-10-07
> Published: 2024-01-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 84
- State: closed
- Author: skot
- Opened: 2024-01-10
- Closed: 2024-10-10
- Labels: bug

## Description

This is a follow on to #80 and #50

It seems that some pools, like Braiins do not like having `mining.subscribe` come before `mining.configure`. They send `"error":[21,"ConfigurationOutOfOrder"`

```
I (2391) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe BM1366"]}
I (2451) stratum_api: Received result {"id":1,"result":[[["mining.set_difficulty","1"],["mining.notify","1"]],"00",6],"error":null}
I (2451) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (2511) stratum_api: Received result {"id":2,"result":null,"error":[21,"ConfigurationOutOfOrder",null]}
I (2521) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}
```

This _should_ be a simple fix by just reordering STRATUM_V1_subscribe() and STRATUM_V1_configure_version_rolling() in main/tasks/stratum_task.c

The problem is when we do that, Braiins sends a result `{"id":null,"method":"mining.set_version_mask","params":["1fffe000"]}` which causes STRATUM_V1_parse() in components/stratum/stratum_api.c to crash.

So, the TODO here is;
- reorder STRATUM_V1_subscribe() and STRATUM_V1_configure_version_rolling() in main/tasks/stratum_task.c so that STRATUM_V1_configure_version_rolling() comes first
- figure out how to parse and handle the version mask in STRATUM_V1_parse() in components/stratum/stratum_api.c
