# bitaxeorg/ESP-Miner issue #916: Incompatibility With Miningcore Based Pools

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/916
> Collected: 2026-10-07
> Published: 2025-05-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 916
- State: closed
- Author: The1Anubis
- Opened: 2025-05-12
- Closed: 2025-05-16
- Labels: none

## Description

The miner will not connect to pools that are Miningcore based. Have 4 of these and all are the same result. Using one for a test subject to modify firmware, but no luck.

Thank you.

**To Reproduce**

**Expected behavior**
Should connect and accept jobs.
 
**Screenshots & Photos**
```
₿ (14130) bm1370Module: Setting Frequency to 525.00MHz (525.00)
₿ (14230) bm1370Module: Setting max baud of 1000000
₿ (14230) serial: Changing UART baud to 1000000
₿ (14230) stratum_task: Starting heartbeat thread for primary endpoint: www.sporadicprecision.com
₿ (14230) ASIC_task: ASIC Job Interval: 500.00 ms
₿ (14250) ASIC_task: ASIC Ready!
₿ (14230) stratum_task: Trying to get IP for URL: www.sporadicprecision.com
₿ (14230) main_task: Returned from app_main()
₿ (14290) stratum_task: Connecting to: stratum+tcp://www.sporadicprecision.com:4920 (76.204.61.25)
₿ (14290) stratum_task: Socket created, connecting to 76.204.61.25:4920
₿ (14380) stratum_api: Resetting stratum uid
₿ (14380) stratum_task: Clean Jobs: clearing queue
₿ (14380) stratum_api: tx: {"id": 1, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
₿ (14390) stratum_api: tx: {"id": 2, "method": "mining.subscribe", "params": ["bitaxe/BM1370/v2.5.1"]}
₿ (14400) stratum_api: tx: {"id": 3, "method": "mining.authorize", "params": ["16obFFgEfMuLboyqb32sqFfwGKdKjuGHoM", "x"]}
₿ (14410) stratum_api: tx: {"id": 4, "method": "mining.suggest_difficulty", "params": [1000]}
₿ (14450) stratum_task: rx: {"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":1}
₿ (14450) stratum_task: setup message rejected: unknown
₿ (14490) stratum_task: rx: {"result":[[["mining.set_difficulty","0HNCHKAL0L2SS"],["mining.notify","0HNCHKAL0L2SS"]],"10000002",4],"id":2}
₿ (14490) stratum_task: setup message rejected: unknown
₿ (14500) stratum_task: rx: {"jsonrpc":"2.0","method":"mining.set_difficulty","params":[1024.0],"id":null}
₿ (14510) stratum_task: Set stratum difficulty: 1024.
```

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: ACMiner
 - ESP-Miner FW version: 2.51,,2.61,,2.7.1
 - Hash Frequency: NA
 - Voltage: ~120
 - Pool URL, Port, User: Multiple Pools

**Additional context**
Modified code to force work to be accepted but could never get the work to be processed by the miner.


## Comments

### mutatrum on 2025-05-13

I fixed a stratum parsing bug. Can you test with this firmware?

https://github.com/bitaxeorg/ESP-Miner/actions/runs/14992859434

You only need `www.bin` and `esp-miner.bin`.

### The1Anubis on 2025-05-13

It is working perfectly now. Thank you!
What did you find if I may ask?

### mutatrum on 2025-05-13

Thanks for the feedback! This pool returns
```
{"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":1}
```
where ckpool and public-pool return
```
{"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"},"id":1,"error":null}
```
The error field missing threw off the parser, as it only checked for the `error` field being null, not the absence of the `error field.

### pool2win on 2025-08-12

This was the mistake I was making on hydra/p2pool. I now send result/error as null instead of skipping them. Turns out that is actually a json 1.0 thing :) Ref: https://www.jsonrpc.org/specification_v1#a1.2Response

So @WantClue you were right in expecting error: null to be there in the older versions.
