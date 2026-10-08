# bitaxeorg/ESP-Miner issue #2004: BM1370 hash domain stuck at 0 GH/s until restart

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/2004
> Collected: 2026-10-07
> Published: 2026-09-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 2004
- State: open
- Author: adamdecaf
- Opened: 2026-09-28
- Closed: n/a
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
One of four BM1370 hash domains stayed at 0 GH/s for a 5-day uptime. The device kept mining at ~75% of `expectedHashrate`. `errorPercentage` stayed 0. `POST /api/system/restart` recovered all four domains.

**To Reproduce**
No deterministic trigger. Observed on a Gamma 601, v2.15.1, after a boot with `resetReason: Software reset due to exception/panic`.

`GET /api/system/info` before restart:

- `expectedHashrate` 1224
- `hashRate_1h` ~917
- `hashrateMonitor.asics[0].domains` `[288, 0, 313, 289]`
- `errorPercentage` 0
- `sharesAccepted` 95475, `sharesRejected` 0
- `overheat_mode` 0, `miningPaused` false
- frequency 600 MHz, `coreVoltage` 1140 (`coreVoltageActual` 1134)

After `POST /api/system/restart` (ASIC cold-boot init, chip 0 detected, frequency ramp 50→600 MHz), within ~20 s:

- `hashRate_1m` ~1211
- all four domains ~270–320 GH/s
- 0 rejected shares

Four other Gamma units on the same LAN and firmware at 600 MHz were at 1164–1223 GH/s with all domains live.

**Expected behavior**
A silent domain is a fault. `self_test.c` already fails a domain below ~1/3 of expected. `power_management` already has `mining_stop` / `mining_start` (`ASIC_INIT_RECOVERY`) for pause and overheat. Runtime should use that path when a domain stays at ~0, or when `hashRate_1h` stays well below `expectedHashrate`.

**Screenshots & Photos**
n/a (API capture)

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: self-operated
 - ESP-Miner FW version: v2.15.1
 - Hash Frequency: 600 MHz
 - Voltage: 1140 mV
 - Pool URL, Port, User: pool.256foundation.org:3333, HardestBlocks-dot-org.bitaxe_69F9

**Additional context**
`errorPercentage` is `error_hashrate / current_hashrate`, so a silent domain does not raise it.


## Comments

### adamdecaf on 2026-09-28

Starlink was down around then (replaced the dish cable, restarted it a couple of times). Local WiFi stayed up. All five Gammas on the LAN hit the same panic (`Software reset due to exception/panic`, ~5.18 d uptime).

On v2.15.1 both pools dying does this:

1. `pools_unavailable` — https://github.com/bitaxeorg/ESP-Miner/blob/v2.15.1/main/tasks/protocol_coordinator.c#L359-L367
2. `mining_stop()` (vcore 0) — https://github.com/bitaxeorg/ESP-Miner/blob/v2.15.1/main/tasks/power_management_task.c#L144-L149
3. `probe_pool_v1()` on `protocol coord` (3072 B stack) — https://github.com/bitaxeorg/ESP-Miner/blob/v2.15.1/main/main.c#L236

That's #1899. #1897 removed the coordinator.

This board came back mining with domain 1 at 0 until a software restart — not #1953. Self-test already fails that; runtime does not: https://github.com/bitaxeorg/ESP-Miner/blob/v2.15.1/main/self_test/self_test.c#L675-L678
