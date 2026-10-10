# bitaxeorg/ESP-Miner issue #1554: Alive gone crazy

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1554
> Collected: 2026-10-07
> Published: 2026-02-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1554
- State: closed
- Author: WantClue
- Opened: 2026-02-15
- Closed: 2026-05-28
- Labels: bug

## Description

When manually switching to using fallback the primary pool is still polled. Should not meh

## Comments

### Painerman on 2026-02-17

I already wrote about this on December 13, 2025. WantClue says it has **no plans** to fix the errors and is closing the requests: 

I set the fallback pool as the primary pool, then I go to the logs and see that the primary wallet is sent to the pool at the beginning, and the fallback wallet is sent to the completed tasks.

₿ (24940) power_management: PID startup ramp phase: 3/17 (Total cycle: 6), current D: 17.0
₿ (24949) power_management: Temp: 54.6 °C, SetPoint: 58.0 °C, Output: 65.0% (P:15.0 I:0.2 D_val:17.0 D_start_val:20.0)
₿ (25506) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1366/v2.12.0-1.12.2"]}
₿ (25508) stratum_api: tx: {"id": 2, "method": "mining.authorize", "params": ["PRIMARY_WALLET", "d=4096"]}
₿ (25762) bm1366: Job ID: 50, Asic nr: 0, Core: 39/7, Ver: 040FE000
₿ (25763) asic_result: ID: 0000286f, ASIC nr: 0, ver: 040FE002 Nonce 37E2024E diff 330.9 of 4096.
₿ (28844) stratum_api: rx: {"jsonrpc":"2.0","method":"mining.notify","params":["00002871","ec83c5fa659abf1a4e8a22f067581246ae283583484ba7f10000000d00000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff24026f0707062f503253482f04d8a92d6900","0a4d696e696e67636f7265000000000100e40b54020000001976a914941d5be0d6c17f19819ab1c47255b92f64e94b4188ac00000000",[],"00000002","1925c492","692da9d8",false],"id":null}
₿ (32290) stratum_api: tx: {"id": 8, "method": "mining.submit", "params": ["FALLBACK_WALLET", "00002870", "02000000", "692da9ce", "ff7d015b", "0891e000"]}
