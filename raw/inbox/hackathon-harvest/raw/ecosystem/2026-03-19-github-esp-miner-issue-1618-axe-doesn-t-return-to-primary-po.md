# bitaxeorg/ESP-Miner issue #1618: Axe doesn't return to primary pool from fallback

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1618
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1618
- State: closed
- Author: 0xf0xx0
- Opened: 2026-03-19
- Closed: 2026-05-28
- Labels: none

## Description

**Describe the bug**
If the primary pool goes down, the axe won't switch back when it comes back up.

**To Reproduce**
Steps to reproduce the behavior:
1. Set up a local pool as your primary
2. take it down
3. let the axe fallback
4. bring the primary back up
5. watch the axe do the init sequence and nothing else

**Expected behavior**
The axe should return to the primary pool.

**Logs**
```
₿ (21389955) stratum_task: Resolved 10.42.0.1:5661 → 10.42.0.1
₿ (21389956) stratum_api: TLS disabled, Using TCP transport
₿ (21389971) stratum_api: tx: {"id":1,"method":"mining.subscribe","params":["bitaxe/BM1370/v2.13.2-116-g705b6c8a2-dirty"]}
₿ (21389976) stratum_api: tx: {"id":2,"method":"mining.authorize","params":["yipaxe","x"]}
# conn closed, submission to fallback pool still
₿ (21397929) stratum_api: tx: {"id":3015,"method":"mining.submit","params":["bc1qfakeaddr","6961cf8f00032a16","0000000000000000","69bc66d3","48eafb19","0d880000"]}
```

**Hardware (please complete the following information):**
 - ESP-Miner FW version: commit 51566625
 - Pool: atlaspool.io


## Comments

### mutatrum on 2026-03-21

This might be some socket timeout thing that was affected by #1413.

### WantClue on 2026-05-28

has been fixed in #1689
