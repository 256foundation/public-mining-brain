# bitaxeorg/ESP-Miner issue #1451: Mixing the primary and fallback pools

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1451
> Collected: 2026-10-07
> Published: 2025-12-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1451
- State: closed
- Author: Painerman
- Opened: 2025-12-13
- Closed: 2025-12-17
- Labels: none

## Description

I set the fallback pool as the primary pool, then I go to the logs and see that the primary wallet is sent to the pool at the beginning, and the fallback wallet is sent to the completed tasks.

ESP-Miner LV07

₿ (24940) power_management: PID startup ramp phase: 3/17 (Total cycle: 6), current D: 17.0
₿ (24949) power_management: Temp: 54.6 °C, SetPoint: 58.0 °C, Output: 65.0% (P:15.0 I:0.2 D_val:17.0 D_start_val:20.0)
₿ (25506) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1366/v2.12.0-1.12.2"]}
₿ (25508) stratum_api: tx: {"id": 2, "method": "mining.authorize", "params": ["**_PRIMARY_WALLET_**", "d=4096"]}
₿ (25762) bm1366: Job ID: 50, Asic nr: 0, Core: 39/7, Ver: 040FE000
₿ (25763) asic_result: ID: 0000286f, ASIC nr: 0, ver: 040FE002 Nonce 37E2024E diff 330.9 of 4096.
₿ (28844) stratum_api: rx: {"jsonrpc":"2.0","method":"mining.notify","params":["00002871","ec83c5fa659abf1a4e8a22f067581246ae283583484ba7f10000000d00000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff24026f0707062f503253482f04d8a92d6900","0a4d696e696e67636f7265000000000100e40b54020000001976a914941d5be0d6c17f19819ab1c47255b92f64e94b4188ac00000000",[],"00000002","1925c492","692da9d8",false],"id":null}
₿ (32290) stratum_api: tx: {"id": 8, "method": "mining.submit", "params": ["**_FALLBACK_WALLET_**", "00002870", "02000000", "692da9ce", "ff7d015b", "0891e000"]}

## Comments

### mutatrum on 2025-12-15

Please share which firmware version you're running. As for the first issue, if the fallback pool is being used, there is also a connection made to the primary pool to see if it comes back online. But not sure if that's the case here.

As for the other issues, can you give a bit more information? And it would make sense to make separate issues, as otherwise it gets complicated with several problems listed on a single ticket.

### Painerman on 2025-12-15

The software version, as indicated in the logs ( esp-miner-factory-lv07A-v2.12.0-1.12.2.bin ). I assumed that the ability to manually select a pool is needed precisely to make the backup pool the primary one. In that case, there's no need to ping the primary pool. It would be nice to be able to add more pools and then select the one that's needed at the moment. 

### mutatrum on 2025-12-15

This is not our software, so we can't help here. You have to open an issue with the manufacturer.

### Painerman on 2025-12-15

As far as I understand, this software was derived from yours by adding compatibility with other similar devices, but the bugs were originally yours, so I was advised to contact you directly. Those who work on expanding compatibility won't fix every new version you publish with the same errors!

### Painerman on 2025-12-15

MrBonkerz wrote: Please raise this in the main bitaxeorg repo—the fix there will be synced to my fork.

### mutatrum on 2025-12-15

Ok, reopened it for now. It's a bit tricky as we don't know which things have changed in that firmware, so there's a risk of us trying to find bugs that aren't ours and we can't keep tabs on all the custom firmware out there. Hence the hesitation.

Back to the issue at hand: if I understand correctly, when selecting the secondary pool with the dropdown on the dashboard, it still pings the primary pool? You are correct that it shouldn't ping primary, only until secondary is unavailable and it switches over.

There are plans to add more pools, but that needs more groundwork before that can be added, so that'll take a while.

### Painerman on 2025-12-15

As far as I understand the logs, authorization occurs on the main wallet, and in the task results (TX) the fallout wallet is sent.

### Painerman on 2025-12-15

Here's what I think is a good interface for adding pools (screenshot):

![Image](https://github.com/user-attachments/assets/b51e422d-951a-4c9c-b11d-4ee2c3a47b41)

One caveat: there's no option to select one of the existing pools as the primary one; I have to copy and paste manually or I put an incorrect symbol in front of an unnecessary pool and wallet to cause an error and the system to start trying to connect to the next one.. To be on the safe side, I also do it the old-fashioned way on LV07 – manually.
