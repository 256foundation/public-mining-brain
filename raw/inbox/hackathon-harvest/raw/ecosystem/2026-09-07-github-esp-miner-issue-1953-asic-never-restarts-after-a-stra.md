# bitaxeorg/ESP-Miner issue #1953: ASIC never restarts after a stratum outage; miner spins on "ASIC not initialized" then panics

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1953
> Collected: 2026-10-07
> Published: 2026-09-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1953
- State: open
- Author: SerpentXSF
- Opened: 2026-09-07
- Closed: n/a
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
If the pool becomes unreachable long enough to exhaust the stratum retry budget, power_management stops mining and powers the ASIC down — and it is never brought back, even after the pool returns and stratum reconnects successfully. The miner then logs ASIC not initialized, skipping job send every ~500 ms indefinitely, and eventually panics and reboots.

At that point the miner is otherwise perfectly healthy: WiFi is up, the pool is reachable, stratum is connected and receiving work. Only the ASIC is off, because nothing turns it back on. So a transient pool or network blip costs the entire uptime rather than just the outage window.

In my run the ASIC went down at t=100 s and never returned: 902 ASIC not initialized messages over 452 seconds, with no Mining started, no asic_initialize, and no re-detection attempt anywhere in the log, before the panic at t≈553 s.

I first hit this in the field, where two miners panicked 3 seconds apart during a single WiFi access-point outage.

**To Reproduce**
Take 10 minutes, no special hardware.

Steps to reproduce the behavior:
1. Set the miner's primary and fallback pool to a blackhole address, so connections time out rather than being refused — I used 192.0.2.1:3333 (RFC 5737 TEST-NET-1).
2. Restart the miner so the pool config takes effect.
3. Wait for the retry budget to exhaust. The log shows Transport unable to connect ... Attempt: 2, 3 → Max V1 retry attempts reached (3), notifying coordinator → Protocol failure reported (state=1, failures=1/2) → power_management: Stopping mining, and the ASIC ramps down to vcore: Set ASIC voltage = 0.000V.
4. Note that this state is stable — mine sat here 6 minutes with no problem. Retry exhaustion on its own is not enough to trigger the bug.
5. Set the pool back to a working address. Do not restart — this is what exercises the live reconnect path.
6. Stratum reconnects (TLS disabled, Using TCP transport), but the ASIC is never re-initialized. The miner logs ASIC not initialized, skipping job send every ~500 ms.
7. After ~7.5 minutes in that state it panics and reboots. esp_reset_reason() reports "Software reset due to exception/panic".

**Expected behavior**
When the pool becomes reachable again, the miner should re-initialize the ASIC and resume mining. Failing that, it should at least not sit in an unrecoverable loop until it panics — a stratum outage should be survivable without losing the device's uptime.

**Screenshots & Photos**
Not applicable — the evidence is in the logs. Relevant excerpt from the reproduction, at the moment the pool came back:

```
W (547036) create_jobs_task: ASIC not initialized, skipping job send
W (547538) create_jobs_task: ASIC not initialized, skipping job send
I (547548) stratum_api: TLS disabled, Using TCP transport      <- pool is back, stratum reconnects
W (548041) create_jobs_task: ASIC not initialized, skipping job send   <- ASIC still down
W (548544) create_jobs_task: ASIC not initialized, skipping job send
   ... continues ~900 times ...
--- SYSTEM RESTART ---
```

The original field occurrence, same shape, triggered by WiFi loss rather than a blackholed pool:

```
E transport_base: tcp_read error, errno=Software caused connection abort
E stratum_v1_task: Failed to receive JSON-RPC line, reconnecting...
I stratum_v1_task: WiFi disconnected, attempting to reconnect...
W wifi: Haven't to connect to a suitable AP now!
E esp-tls: [sock=43] select() timeout
E stratum_v1_task: Transport unable to connect to <pool>:3333 (errno -1). Attempt: 2
E stratum_v1_task: Transport unable to connect to <pool>:3333 (errno -1). Attempt: 3
W stratum_v1_task: Max V1 retry attempts reached (3), notifying coordinator
W protocol_coordinator: Protocol failure reported (state=1, failures=1/2)
I power_management: Stopping mining
   ASIC ramped 156 MHz -> 50 MHz, then  vcore: Set ASIC voltage = 0.000V
I power_management: Mining stopped
W create_jobs_task: ASIC not initialized, skipping job send   (repeating)
--- SYSTEM RESTART ---
```

**Hardware (please complete the following information):**
- Bitaxe HW version: Gamma, board version 601 (BM1370). Reproduced on two units.
- Bitaxe HW vendor: Solo Satoshi
- ESP-Miner FW version: based on 2.14.2 (see note below)
- Hash Frequency: 525 MHz (second unit 555 MHz)
- Voltage: 1140 mV (second unit 1170 mV)
- Pool URL, Port, User: local ckpool (FutureBit Apollo) on the LAN, port 3333, plain TCP, no TLS. Worker is a bech32 payout address — redacted.

**Additional context**
Firmware disclosure: I run a dual-pool fork of 2.14.2. Every code path and log string above is unmodified upstream — stratum_v1_task.c, protocol_coordinator.c, power_management_task.c and create_jobs_task.c match current upstream head. My changes are elsewhere (a second pool task, UI). Flagging it for completeness rather than because I think it is implicated; a confirmation on stock firmware would be welcome and should be quick given the reproduction steps.

What I have not established: I have not root-caused the panic itself and I am not proposing a patch. What is solid is the precondition — after Stopping mining, nothing re-initializes the ASIC when the pool returns, and the device spins in create_jobs_task until it dies. Whether the panic is a watchdog on that spin, heap exhaustion from the log flood, or something else, I cannot tell from the RAM log alone: the panic handler writes to UART, which the ring buffer does not capture. A serial console attached during step 6 would settle it.

Ruled out: not the pool (reachable throughout, other miners kept submitting); not signal strength (RSSI −30 to −67 dBm); not thermal (45–66 °C against a ~70 °C cap, no thermal events logged); not power (RESET_BROWNOUT appears in zero captures); not retry exhaustion alone (stable for 6 minutes).

Logs: I have full pre-crash captures (~530 KB each) from the reproduction and from two field occurrences, and can attach or trim them to whatever window is useful.


## Comments

### mutatrum on 2026-09-08

The pool connection code has been changed massively in #1897, can you retry with that PR?

### dlepaux on 2026-09-11

Same failure on a Naja Duo (board 1201, 2× BM1373) running `v2.14.0-48-gc4796e2a`, so before #1897. Both pool slots point at one solo pool (ckpool on our own node), which went away for about four minutes during planned maintenance. From our Prometheus scrape of `/api/system/info` (UTC, 2026-09-11):

- 13:45:15 `isUsingFallbackStratum` = 1
- 13:46:15 hashrate 0
- 13:46:45 power 0 W (ASIC powered down)
- 13:47:11 pool back and serving work
- 13:47:29 the board reboots; `resetReason` afterwards is `Software reset due to exception/panic`

Power stayed at 0 W after the pool came back, until the panic. Two earlier outages the same day had the same shape (a reboot 25–70 s into the pause), but their reset reason was overwritten before we could read it.

We haven't tried #1897 yet: v2.15.2rc0 is the only release with BM1373 support, and it predates the merge. We'll retest on the first release that carries #1897 and report back here.


### mutatrum on 2026-09-12

Current master has both bm1373 support and 1897, you can test with that.
