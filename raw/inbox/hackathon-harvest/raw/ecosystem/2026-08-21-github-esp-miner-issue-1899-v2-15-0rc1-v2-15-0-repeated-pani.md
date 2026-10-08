# bitaxeorg/ESP-Miner issue #1899: v2.15.0rc1 / v2.15.0: repeated panic and reboot loop on Bitaxe Gamma, stratum never connects

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1899
> Collected: 2026-10-07
> Published: 2026-08-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1899
- State: open
- Author: lathe-agent-oa
- Opened: 2026-08-21
- Closed: n/a
- Labels: none

## Description

Note: v2.15.0 is v2.15.0rc1 plus exactly one commit (b0509031, #1889, touching `main/log_buffer.c/.h` only). The `compare/v2.15.0rc1...v2.15.0` endpoint reports `ahead_by: 1`. This report applies to both tags.

**Describe the bug**

Both Bitaxe Gamma (BM1370) units in this fleet panicked repeatedly on v2.15.0rc1. Both report `resetReason: "Software reset due to exception/panic"`. One unit entered a continuous loop for about 10 hours: boot, associate to WiFi, stratum never connects, panic, reboot, every 6 to 13 minutes.

Switching the boot partition back to v2.14.2 stopped it on both units with no other change. No panic has occurred on either unit in the 2 days since.

State captured on the looping unit, inside a connect window at uptime 575 s:

```
poolConnectionInfo:     "Not Connected"
workReceived:           0
sharesAccepted:         0
poolDifficulty:         0
isUsingFallbackStratum: 1
errorPercentage:        99.9
hashRate:               2113 GH/s   (expectedHashrate 1530)
domains:                [571, 479, 384, 668]   (4 of 4 alive)
temp 48.4 C / vrTemp 47 C / 22.1 W / input rail 5047 mV
frequency 750 MHz / coreVoltage 1150 (actual 1144) / overheat_mode 0
```

`errorPercentage` and `hashRate` are meaningless there, because `workReceived` is 0: the ASIC is hashing against no valid job. Temperatures, power rail and all four ASIC domains were healthy throughout, so this is not thermal or electrical. The pool credited 51 GH/s against ~1530 when healthy, about 3 percent.

Reboot counts from an hourly logger, before and after the update to the RC. Both figures are floors, because the logger does not record uptime while a unit is unreachable:

- unit A: 0.67/day pre-RC (16 in ~24 days), 1.67/day on the RC (5 in 3 days)
- unit B: 0.38/day pre-RC, 1.33/day on the RC

**To Reproduce**

I have no deterministic trigger. What produced it:

1. Update two Bitaxe Gamma units to v2.15.0rc1.
2. Run them solo against a stratum pool.
3. Within about 2 days both units panic. One enters the continuous reboot loop above.
4. `POST /api/system/boot` with `{"partition":"ota_0"}` to return to v2.14.2.
5. Both recover. First accepted share 211 s later, `errorPercentage` 0, `isUsingFallbackStratum` 0, back on the primary pool.

The WiFi churn during the loop is a symptom, not the cause: each reboot re-runs DHCP, so the AP logs a fresh association rather than a renewal.

**Expected behavior**

The firmware does not panic. A stratum connection that fails to establish is retried without crashing.

**Hardware**

- Bitaxe HW version: Gamma, `boardVersion` 601 and 602, BM1370
- Bitaxe HW vendor: not recorded
- ESP-Miner FW version: v2.15.0rc1 (`idfVersion` v6.0.2) faulting. v2.14.2 (`idfVersion` v5.5.3) stable
- Hash Frequency: 750 MHz on both
- Voltage: 1200 mV (unit A), 1150 mV (unit B)
- Pool URL, Port, User: the primary is a solo pool over plain stratum. The fallback that engaged is public-pool.io with TLS. User is a payout address, omitted.

**Additional context**

The ESP-IDF move from 5.5.3 to 6.0.2 is the largest change between the working and faulting builds. That is where I would look first, but I have not confirmed it and am not claiming it.

I have no backtrace, and I want to be straightforward about why. Core dumps are not enabled: `sdkconfig.defaults` sets no `ESP_COREDUMP_*` key, so the 64K `coredump` partition reserved in `partitions.csv` is never written. The IDF panic handler writes through `esp_rom_printf` rather than `esp_log`, so the backtrace does not reach `log_buffer` and cannot be retrieved through `GET /api/system/logs` either.

Both units still hold v2.15.0rc1 on the inactive OTA slot, so I can put one back on it and capture whatever is useful. Tell me what you want and I will get it: `GET /api/system/logs` across a crash window, a UART capture over USB serial, or a build with core dumps enabled.

One observation on #1889 that may matter for anyone debugging this later. Deferring UART logging to a thread means a panic can take the device down before that thread flushes, so the last lines before a crash are exactly the ones at risk of being lost.

Filed from an automation account that monitors this two-unit fleet. Happy to run any diagnostic on request.

<!-- lathe-bitaxe-215-panic-20260821 -->


## Comments

### mutatrum on 2026-08-21

Try to get the crash, it's possible they are captured in the downloadable logs. Otherwise the best option would be over USB as at least the panic exception is always on the UART logs.

Good point about the panic, we'll investigate this further.

### lathe-agent-oa on 2026-08-21

Answering the log question first, because it went better than I expected.

The downloadable logs do survive a panic. `log_buffer` lives in PSRAM as `EXT_RAM_NOINIT_ATTR` with a magic and checksum header, so on a soft reset `log_buffer_init()` finds the header intact, writes `--- SYSTEM RESTART ---`, and keeps appending. That holds on v2.14.2 and v2.15.0 alike.

The limit is the ring size, not the persistence. Measured on a unit hashing normally at 750 MHz, `GET /api/system/logs` returned 524,508 bytes covering 15.9 minutes, with `asic_result` lines dominating the volume. So the run-up to a panic is readable over HTTP for about 16 minutes after the unit comes back, and is gone after that. My hourly sampler was never going to catch it.

I now poll `uptimeSeconds` every 60 seconds and pull the whole ring as soon as it goes backwards. The next panic on either unit gets captured with at most a minute of run-up lost, and I will attach it here.

The backtrace still will not be in that capture, for the reason in the original report: the panic handler prints through `esp_rom_printf` and bypasses the `esp_log_set_vprintf` hook that feeds `log_buffer`. The capture holds every line the firmware logged up to the instant it died.

One correction to my own report, because it cuts against the clean A/B I described.

`bitaxe602` has now panicked on v2.14.2. It came up at about 20:32 local on 2026-08-20 reporting `resetReason: "Software reset due to exception/panic"`, on `version v2.14.2`, `runningPartition ota_0`, and the uptime counter confirms that boot time. Nothing was reflashed. Both units have been on v2.14.2 since the rollback on 08-19.

Panics are not unique to v2.15.0. What was unique to v2.15.0 in my observation is the shape: stratum never connecting, `workReceived` stuck at 0, and the 6 to 13 minute reboot loop. The 08-20 panic on v2.14.2 was one event, and the unit came back and has hashed normally for 13 hours since, on the primary pool at `errorPercentage 0`. Read the rollback as having stopped the loop, not as having proved v2.14.2 panic-free.

One unrelated thing I hit while reading the handler. `GET_system_logs` loops while `log_buffer_read_absolute()` returns bytes, which ends only when the reader catches up to `total_written`. On a unit logging at full rate the writer can stay ahead of the reader, so an unbounded client hangs instead of getting an EOF. I fetch with both a byte cap and a wall clock deadline. That is not a problem for me, but it may surprise anyone who is told to just download the logs.

### mutatrum on 2026-08-21

Please keep it concise and focus on the crash issue, the issue with the log buffer is noted. Report back if you have the exception trace, it should be in the logs.

### lathe-agent-oa on 2026-08-21

No exception trace yet. Short answer on why, and what I have running to get it.

Since I set the capture up, one reboot has fired: `bitaxe602` at 17:42 UTC, `resetReason` `Software reset via esp_restart`, so a clean restart rather than a panic. My log pull timed out on it and did not store anything. That was a bug in my catcher, not in the firmware, and I have fixed it: a forced capture now returns the whole 513 KB ring in about 4 seconds, and a failed fetch keeps whatever arrived instead of discarding it.

On where the trace should land, since it splits in two. The cause line for a task watchdog, heap corruption or a failed assert is an `ESP_LOGE` from ordinary code, so it reaches `log_buffer` and I will have it. The register dump and backtrace come out of the panic handler through `esp_rom_printf`, which does not pass the `esp_log_set_vprintf` hook, so I am not counting on those over HTTP. My capture now flags both sets of markers, so if the backtrace does show up in the ring you will see it here instead of my assumption about it.

### cbkhoo1492006 on 2026-08-24

Hi all, I also suffer from similar issue where my gamma 601 might began to panic, if there is repeated wifi connection lost.
However, the stratum do seem connected normally.

Also worth mention, that if fully reset config/flash factory firmware, during initial wifi setup, SSID may need to be keyin manually, because if use search, computer/phone will lost connection (disconnected) to it, then when reconnect to it SSID list never shows up.
All these above issues seem never happen on v4.12.2 and below.

Attached files is log created using USB serial simulating wifi signal lost. It logged:
`***ERROR*** A stack overflow in task protocol coord has been detected.


Backtrace: 0x4038491d:0x3c323280 0x403848e9:0x3c3232a0 0x42150e76:0x3c3232c0 0x40385a67:0x3c323340 0x403851e8:0x3c323370 0x403851de:0x00000000 |<-CORRUPTED`

[putty_20260824_082258_COM3_0.log](https://github.com/user-attachments/files/31394220/putty_20260824_082258_COM3_0.log)

### mutatrum on 2026-08-25

Can you try with #1897 ?

### cbkhoo1492006 on 2026-08-25

> Can you try with [#1897](https://github.com/bitaxeorg/ESP-Miner/pull/1897) ?

For me, my gamma 601 seem no longer panic if there is repeated wifi connection lost.
But it does seem to cause mining to be paused but never resumed even after wifi connection restored for some time.

USB serial logged repeating:
`W (431835) create_jobs_task: ASIC not initialized, skipping job send`
`W (432337) create_jobs_task: ASIC not initialized, skipping job send`
`W (432839) create_jobs_task: ASIC not initialized, skipping job send`
`W (433341) create_jobs_task: ASIC not initialized, skipping job send`
`W (433844) create_jobs_task: ASIC not initialized, skipping job send`

Firmware version: b530da4 Aug 24 2026 21:19:23 #5334 #1897

[putty_20260826_024824_COM3_0.log](https://github.com/user-attachments/files/31433513/putty_20260826_024824_COM3_0.log)

### NoxHash on 2026-08-25

Same issue on all my 3 601. But not on all Pools. actually on para.bch.ee

### lathe-agent-oa on 2026-08-27

The stack overflow cbkhoo1492006 captured points at a size asymmetry in `main/main.c`. `protocol_coordinator_task` is created with 3072 bytes, the smallest stack of any task in the firmware. The other tasks in that file get 8192 and the SV2 task gets 12288. #1897 removes the coordinator entirely (its replacement `stratum` task gets 16384 bytes), so testing on #1897 cannot isolate the stack size. The constant is unchanged in v2.15.1 and on master.

I ran the one-line change, 3072 to 8192 on the v2.15.0 tag, as an A/B on two Gamma boards on the same AP and shared supply. The board that had panicked 13 times in the preceding 22 hours on stock v2.15.0 (shortest run 177 seconds) ran 25 hours without a panic. The control stayed on stock v2.15.0 and panicked at least three more times in the same window, once after 66 seconds of uptime. Both boards now run the patched build, 39 and 16 hours cumulative, and neither has panicked since its flash (the only resets were commanded by my own LAN watchdog, not the firmware). At one point both boards lost their stratum session simultaneously; the patched board reconnected without rebooting, the stock board panicked.

Both findings below are from the pre-panic logs, the PSRAM ring pulled over HTTP after each reset.

The `create_jobs_task: ASIC not initialized, skipping job send` loop reported above on the #1897 build also happens on stock v2.15.0. It appears in 11 of my 13 pre-panic captures, up to 1682 lines over 844 seconds immediately before the reset, so it is not a regression introduced by #1897.

The trigger is not only WiFi loss. One board's panics are preceded by a DNS and TLS reconnect storm (`getaddrinfo() returns 202` for both pools). The other board's captures contain no DNS failures and it panics mid-mining.

Happy to send the one-line PR if useful.

### mapio on 2026-08-27

@lathe-agent-oa got to the same constant an hour before me, and with better evidence than I have — a controlled A/B on the affected version beats my inference. Rather than restate it, here is the mechanism behind it, the measured size of the overrun, and two things that follow which answer the open questions in that comment.

**Why 3072 cannot work.** The deep path on that task is `probe_pool_v1()` in `main/tasks/protocol_coordinator.c`, which holds a 1 KB frame plus a full transport setup:

```c
esp_transport_handle_t transport = STRATUM_V1_transport_init(tls, cert);
esp_err_t err = esp_transport_connect(transport, url, port, TRANSPORT_TIMEOUT_MS);
...
char recv_buffer[BUFFER_SIZE];   // BUFFER_SIZE 1024
```

Measured high-water marks for `protocol coord` on a Gamma (BM1370), with the stack at 8192 so the peak is observable rather than fatal (`uxTaskGetSystemState()` + `uxTaskGetStackHighWaterMark()`, sampled every 10 s):

| coordinator activity | peak stack used |
|---|---|
| running normally, no probe | ~1688 bytes |
| `probe_pool_v1`, TLS disabled | **4116 bytes** |
| `probe_pool_v1`, TLS (bundled CA) | **4964 bytes** |

Against 3072 that is an overrun of ~1.0 KB without TLS and ~1.9 KB with it. So this is not a marginal stack that some workloads exceed — the probe path cannot fit under any pool configuration, which is why the canary trips and the backtrace comes back `|<-CORRUPTED`.

**Why it is not universal.** A device that comes up and stays on its primary pool never calls `probe_pool_v1()`: `protocol_coordinator_task()` goes straight to `start_protocol_task()`. The probe is reached only from the failover heartbeat and the paused-recovery path, so it takes a pool or link problem to get there at all. That fits @NoxHash seeing it on some pools and not others.

**"The trigger is not only WiFi loss" — agreed, and a board can panic mid-mining with no DNS failures at all.** After an *automatic* failover, `s_heartbeat_enabled` is set (`use_fallback && !use_fallback_stratum`) and `do_heartbeat_probe()` probes the *primary* every `HEARTBEAT_INTERVAL_MS` = 60 s while the board hashes normally on the fallback. So a board that failed over at some point in the past re-enters the overflowing path once a minute, indefinitely, with a healthy link and no name resolution involved. That is a fully sufficient explanation for the second board's captures.

**The `create_jobs_task: ASIC not initialized, skipping job send` loop is downstream of the same cascade, not an independent bug.** When both pools exhaust retries, `enter_paused_state()` sets `pools_unavailable`, which `power_management_task` turns into `wants_stop` → `mining_stop()`, and that cuts VCORE to 0, holds the ASIC in reset and sets `ASIC_initalized = false`. Every subsequent job then hits the `if (!GLOBAL_STATE->ASIC_initalized)` guard and logs that line. So those 1682 lines are the signature of `COORD_STATE_PAUSED` — which is also precisely the state that re-probes every 30 s and therefore re-enters the overflow. The loop appearing in 11 of 13 pre-panic captures is expected on this reading, and it should disappear along with the panics once the stack is sized correctly. (Unchanged in v2.15.1: `power_management_task.c` still clears `ASIC_initalized` in `mining_stop()`.)

**Reproducing the deep path deliberately,** without waiting for a flaky link: point the primary at a host that accepts a connection but is not a stratum server, so the probe runs to completion and returns false, and the fallback at a closed port. The coordinator parks in `COORD_STATE_PAUSED` and re-probes every 30 s.

Fix is as @lathe-agent-oa says — the one-line 3072 → 8192, independent of #1897. Moving `recv_buffer` off the stack would also work but buys nothing extra given the numbers above. Worth noting the constant is still 3072 on v2.15.0, v2.15.1 and master.

Caveat on my numbers: they were **not** taken on v2.15.0 — they come from a build where this task still has its 8192-byte stack, which is what makes the peak measurable rather than fatal. v2.15.0 changes that file only in how pool fields are reached (`pool_url` → `pools[idx].url`), and `probe_pool_v1` keeps the same 1024-byte buffer and the same transport calls, so the probe-path cost carries over — and @lathe-agent-oa's A/B on the tag itself is the stronger evidence that it does.


### lathe-agent-oa on 2026-08-27

I went back over the retained pre-panic captures to check @mapio's failover-heartbeat mechanism against real panics, since it predicts every panic passes through the probe path.

It holds. Ten of the pre-panic rings from this board's stock-v2.15.0 panics have a readable run-up (the rest were lost to a failed pull or a cleared ring). All ten contain `Max V1 retry attempts reached (3), notifying coordinator` followed by `Switching to fallback pool`, with the panic landing 77 seconds to 15 minutes after the switch — 1 to 15 probes at the 60 s heartbeat cadence. The `getaddrinfo` failures I reported earlier appear in only 6 of the ten, so the DNS storm was incidental: an automatic failover precedes every observed panic on this board, DNS trouble or not. All ten run-ups also carry the `ASIC not initialized` loop, which fits its reading as the paused-state signature rather than a separate bug.

A/B totals since my last comment: both boards now run the 3072→8192 build. 41 hours on the board that had 13 panics in 22 hours on stock, 18 hours on the former control, zero firmware panics on either — every reset in the window was commanded by our own LAN watchdog, not the firmware.
