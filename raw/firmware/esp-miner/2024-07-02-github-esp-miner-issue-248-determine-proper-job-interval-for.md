# bitaxeorg/ESP-Miner issue #248: Determine proper job interval for version rolling ASICs

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/248
> Collected: 2026-10-07
> Published: 2024-07-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 248
- State: closed
- Author: skot
- Opened: 2024-07-02
- Closed: 2026-05-09
- Labels: bug, enhancement

## Description

Version rolling ASICs such as the BM1366 and BM1368 _should_ be able to have much longer job intervals, on the order of 10s of seconds.

We know that the interval for a S19XP with 110 chips in the chain is 2.14s

## Comments

### skot on 2024-07-02

The current formula, 
`GLOBAL_STATE.asic_job_frequency_ms = (NONCE_SPACE / (double) (GLOBAL_STATE.POWER_MANAGEMENT_MODULE.frequency_value * BM1366_SMALL_CORE_COUNT * 1000)) / (double) GLOBAL_STATE.asic_count;` 

results in `ASIC_task: ASIC Job Interval: 9.91 ms` which is way too short.

### skot on 2024-07-06

- Bitaxe 204, BM1366, 485MHz, 2s job interval, Reg10; `00  15 1C`
-> Braiins reported 1hr average hashrate; 433 GH/s

- Bitaxe 401, BM1368, 490MHz, 0.5s job interval, Reg10; `00 15 A4`
-> Braiins reported 1hr average hashrate; 638 GH/s

### skot on 2024-07-06

We think the expected hashrate should be:
Cores * Small Cores * Hash Freq

- BM1366; 112 * 8 * 485,000,000 = 434.5 GH/s
- BM1368; 90 * 16 * 490,000,000 = 705.6 GH/s

### Georges760 on 2024-07-07

Little correction : BM1368 has 80 cores not 90.

And instead of using the cores*small cores value, we should use the total small cores counts of 894 for BM1366 and 1276 for BM1368. It is a small difference but I believe these numbers exist just for this reason.

### skot on 2024-07-07

Ah, very good. so it should be;
- BM1366; 894 * 485,000,000 = 433.6 GH/s
- BM1368; 1276 * 490,000,000 = 625.2 GH/s

### skot on 2024-07-07

I'm getting _pretty_ close to these on my test 204 and 401 miners with the latest in PR https://github.com/skot/ESP-Miner/pull/249 

This uses hardcoded job interval numbers based on the job intervals measured on the S19XP and the S21

the problem is this will probably not work for overclocking.

### mutatrum on 2026-05-09

Fixed by #420
