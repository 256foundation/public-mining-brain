# bitaxeorg/ESP-Miner issue #1820: ASIC results duplicated ~200x each (~11ms apart);

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1820
> Collected: 2026-10-07
> Published: 2026-07-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1820
- State: open
- Author: mtmorandba-code
- Opened: 2026-07-19
- Closed: n/a
- Labels: none

## Description

## Summary

On my Bitaxe Gamma 601, nearly every `asic_result` is re-reported **~195–207 times** at ~11ms intervals (a ~2.3s burst per unique result), across two firmware versions and three frequency/voltage profiles. Accompanying this: periodic `Checksum failed on response` and `Preamble mismatch` errors whose raw bytes contain **repeated byte fragments within a single response**, suggesting a serial-integrity issue on the ESP32↔BM1370 link. On pools with low share difficulty, the duplicates reach `mining.submit` and produce mass `Duplicate` rejects.

## Hardware / environment

- **Device:** Bitaxe Gamma, board version 601, BM1370 (purchased at BTC Prague, June 2026)
- **Firmware:** reproduced identically on **v2.4.0** and **v2.14.1** (OTA-updated; System page confirms both FW and AxeOS at v2.14.1; ESP-IDF v5.5.3)
- **Pool:** DATUM Gateway v0.4.x on LAN (OCEAN), pool min diff 131072; also reproduced against solo.ckpool.org (fallback)
- **PSU:** ABT ABT060050H, 5.0V / 6.0A / 30W (certified, barrel connector) — ample headroom for ~22W peak
- **WiFi RSSI:** −35 dBm (excellent)

## Symptom 1 — duplicate ASIC results (~200x per unique result)

Example (v2.14.1, 490 MHz / 1.05 V):

```
I (34337020) asic_result: ID: 6a5aa37d8ac05703, ASIC nr: 0, Core: 79/11, ver: 20016000 Nonce 4810D39E diff 310.4 of 131072.
I (34337023) asic_result: ID: 6a5aa37d8ac05703, ASIC nr: 0, Core: 79/11, ver: 20016000 Nonce 4810D39E diff 310.4 of 131072.
I (34337034) asic_result: ID: 6a5aa37d8ac05703, ASIC nr: 0, Core: 79/11, ver: 20016000 Nonce 4810D39E diff 310.4 of 131072.
I (34337046) asic_result: ID: 6a5aa37d8ac05703, ASIC nr: 0, Core: 79/11, ver: 20016000 Nonce 4810D39E diff 310.4 of 131072.
... (continues ~197 times total, ~11ms apart)
```

Quantified across captured logs (each ~8–16 min):

| Log window | Firmware | Freq/Volt | asic_result lines | Unique results | Typical repeat count |
|---|---|---|---|---|---|
| A | v2.4.0 | 400 MHz / 1.00 V | ~3,480 | ~304 | ~197x |
| B | v2.14.1 | 525 MHz / 1.15 V | ~3,168 | ~292 | ~197x |
| C | v2.14.1 | 400 MHz / 1.00 V | ~3,006 | ~318 | ~197x |
| D | v2.14.1 | 490 MHz / 1.05 V | ~3,441 | ~453 | ~197x |

The repeat count is strikingly uniform (~195–207) regardless of settings, and each burst lasts ~2.3s — it looks deterministic (result buffer re-read until overwritten?) rather than random noise.

## Symptom 2 — duplicates reach mining.submit on low-diff pools

At pool difficulty 131072 (DATUM/OCEAN), sub-target duplicates are discarded locally and only occasionally duplicate an actual share: DATUM client stats showed e.g. **40 accepted / 302 rejected** and **47 accepted / 70 rejected** (rejects in exact multiples of 131072 — i.e., duplicate submissions of valid shares). When the device failed over to solo.ckpool (low vardiff), each valid share was followed by **~200 identical submits**, each rejected `Duplicate` — effectively spamming the pool.

## Symptom 3 — serial checksum/preamble errors with stuttered bytes

Roughly 8–11 per 10-minute window, all settings:

```
E (34186656) common: Checksum failed on response
I (34186662) common: aa 55 90 09 55 90 09 7b 93 02 fe
```

Note the repeated fragment `55 90 09` **within one response** — byte-level stutter on the wire.

```
E (34268550) common: Preamble mismatch: got 0x559f, expected 0xaa55
E (34506204) common: Preamble mismatch: got 0xaa8f, expected 0xaa55
```

## Symptom 4 — power-correlated I2C failures (possibly related)

- At **525 MHz / 1.15 V**: repeated `i2c_bitaxe: FATAL: [EMC2101] (0x4c) failed all 3 retries`, `EMC2101: Failed to read fan speed LSB: ESP_ERR_TIMEOUT`
- At **490 MHz / 1.05 V**: intermittent `TPS546: Could not read VIN` + `i2c_bitaxe: FATAL`
- At **400 MHz / 1.00 V**: no I2C errors observed

The UART duplication/checksum issue however is **identical at all three profiles**, so it does not appear power-marginal in the same way.

## Side effects observed

- Dashboard hashrate wildly inflated shortly after boot (e.g., **298 TH/s** displayed, 21% "error" rate) — consistent with duplicated results being counted
- Log spam makes real events hard to see
- Duplicate-submit behaviour risks pool-side throttling/bans on low-diff pools

## Ruled out

- Firmware version (identical on v2.4.0 and v2.14.1, OTA)
- Frequency/voltage (400/1.00, 490/1.05, 525/1.15 — duplication unchanged)
- Cold power cycles (full unplug) — no change
- Settings reset (post-OTA defaults) — no change
- PSU rating (certified 5V/6A/30W unit; connector seated; no brownouts/restarts)
- WiFi (−35 dBm; issue is on the ASIC serial side, pre-network)

## Questions

1. Is this a known errata for early Gamma 601 boards / BM1370 serial comms?
2. Is the uniform ~197x / ~2.3s repeat consistent with the result FIFO being re-read until the next result overwrites it (missing read-acknowledge)?
3. Should duplicate nonces be filtered before `mining.submit` as a mitigation, to protect pools from duplicate spam when share diff is low?

Full log captures (8 windows across all the above configurations) available on request — happy to run any diagnostics or test builds.

## Comments

### mtmorandba-code on 2026-07-20

Firmware: reproduced identically on v2.4.0, v2.14.1, and v2.14.2 (including the #1797 use-after-free race fix); AxeOS matching; ESP-IDF v5.5.3

### WantClue on 2026-07-20

1. Known errata? Partly. The BM1370 duplicate-nonce tendency is known and already worked around (the HCN margin above). But the stuttered bytes — aa 55 90 09 55 90 09 7b 93 02 fe with 55 90 09 repeated inside one 11-byte frame, plus the Preamble mismatch: got 0x559f/0xaa8f — are UART signal-integrity artifacts, not something the protocol produces. Combined with the power-correlated I²C failures (Symptom 4) on the same board, this points at a hardware issue on this specific unit/batch (BTC Prague 601), not a firmware defect. The firmware handles these correctly: CRC fails → SERIAL_clear_buffer() → frame dropped.

2. Is ~197×/2.3s "FIFO re-read until overwritten"? Not as stated — the firmware never re-reads (see above). The mechanism is the ASIC re-emitting the same latched (nonce, version) repeatedly: ~11 ms is the chip's internal re-report cadence, and the burst ends when the next job overwrites the search state. The uniform count reflects job_interval / 11 ms. Note the BM1370 job interval is default_asic_timeout = 500 (device_config.h:95), so a ~2.3 s burst also suggests jobs aren't refreshing as fast as expected on that setup — worth checking DATUM's job cadence. Either way: the re-emission is the chip's, the firmware just faithfully forwards each one.

3. Filter duplicates before mining.submit? Yes — this is the right mitigation and it's cheap. It won't fix the underlying marginal-hardware re-transmission, but it will (a) stop pool spam / duplicate-reject bans on low-diff pools, (b) fix the inflated dashboard hashrate (298 TH/s — duplicates are being counted in SYSTEM_notify_found_nonce / scoreboard), and (c) massively cut log spam. It's a safe guard: a real second discovery of the identical (job_id, nonce, rolled_version) is astronomically unlikely, so dropping exact repeats loses no legitimate shares.

### mtmorandba-code on 2026-07-21

Thanks — I can now add measured data from both sides, and one finding that complicates the re-emission-until-new-job explanation. Note I'm now on **v2.14.2** (flashed yesterday), so everything below is current firmware.

**The pathology persists unchanged on v2.14.2.** Fresh 6-minute capture: 18 duplicate bursts, typical burst = 196 repeats of the same (nonce, version) over ~2.31 s at ~11.8 ms cadence (a few at 205–206 repeats / ~2.43 s; two cut short at 121 and 99). Same ~197 / ~2.3 s I originally reported — so not a legacy-firmware artifact.

**Gateway-side job cadence measured:** 167 stratum job updates over 2 hours, median interval 40.92 s (min 40.85, mean 42.89, max 81.99 — one skipped beat). Miner-side `New Work Dequeued` timestamps confirm the same ~41 s spacing. So stratum work refreshes every ~41 s, not every ~2.3 s.

**Bursts do not terminate on new stratum work.** Clearest example from the capture: burst starts t=102356369, `mining.notify` arrives mid-burst at 102357611, `create_jobs_task: New Work Dequeued` at 102358124, and the burst continues to 102359233 — ~1.1 s past the dequeue. So "burst ends when the next job overwrites the search state" doesn't hold for stratum-driven jobs, and at ~41 s cadence they'd predict ~3,700-repeat bursts anyway, not ~196.

**What does terminate bursts: a corrupted frame.** 11 of 18 bursts end with a `Checksum failed on response` or `Preamble mismatch` exactly one re-emission slot (~12 ms) after the last good duplicate — and *every* checksum failure in the capture sits at a burst boundary, none elsewhere. Examples: burst ends 102342312 → checksum fail 102342324; 102359233 → 102359244; 102368954 → 102368966; 102480239 → 102480251. So the corrupt frames aren't random noise — they're systematically coincident with burst termination. My working guess: something (an internal job send to the ASIC?) happens every ~2.3 s, ends the re-emission, and collides with the chip mid-frame, mangling the final response. If that's right, the ~2.3 s effective interval vs `default_asic_timeout = 500` (device_config.h:95) is the discrepancy to explain — is there a path on v2.14.x where the ASIC job dispatch runs at ~2.3 s instead of ~500 ms, or is the burst cap intrinsic to the chip (~200 repeats)?

**Pool impact is conditional, not constant.** In this capture every burst nonce was below the 131072 vardiff (best 17.7k), so these duplicates never reached the pool — they're CPU/log/accounting spam. Duplicate *submits* only occur when a latched result happens to clear pool difficulty, which matches the intermittent duplicate-rejects I see.

**Hardware symptoms persist post-flash**, consistent with your marginal-unit read: 3× `EMC2101 (0x4c) failed all 3 retries` I²C errors in the same 6 minutes, plus stutter-pattern frames (`aa 55 8d 1a 2e 9b 89 aa 55 8d 1a`).

On the submit-side duplicate filter — is that something you'd take as a PR / plan to merge? Beyond stopping the conditional pool spam, it should also fix the inflated dashboard hashrate if duplicates are being counted in the scoreboard. Happy to test a build against this unit; it reproduces the pathology reliably on current firmware (~3 bursts/minute).


### mutatrum on 2026-07-22

Can you also test with current master?

It sounds like a hardware issue, to be honest. Did you build it yourself or purchased it from a manufacturer? If bought, can you also contact the seller?

### mtmorandba-code on 2026-07-23

Will do — I'll build current master and re-run the same capture (bursts are frequent enough that a few minutes of logs gives a clean sample). One check first: this board runs Axeos — is flashing stock master over it via OTA safe/reversible on this hardware, or should I test via a serial flash instead?

Purchased assembled — it's a board 601 unit from Bitronics booth @BTC Prague this year. I'll maybe contact them about the hardware symptoms (the power-correlated EMC2101 I²C failures and the UART stutter frames being the strongest indicators). If any other 601 owners are watching this issue, it'd be useful to know whether your units show the same `Checksum failed` / `Preamble mismatch` pattern at burst boundaries.

For completeness: the unit is mining and being credited normally at the pool on v2.14.2 (payouts confirmed post-flash), so this is an efficiency/correctness issue rather than a bricked-or-broken one — the duplicates cost chip time and pollute accounting rather than stopping work.

One thing I'd still flag as firmware-relevant regardless of the hardware outcome: the checksum failures land *exactly* at duplicate-burst boundaries (11 of 18 in my capture, one re-emission slot after the last good frame, none elsewhere). Random signal-integrity noise wouldn't be that correlated with burst termination — whatever ends the burst every ~2.3 s seems to be involved in corrupting the final frame. If you can point me at what runs on that cadence in the ASIC task path, I can instrument around it when I test master.

### mutatrum on 2026-07-23

I've never seen it on my 601. Do you have a different PSU to verify if that's not causing power ripples or something like that? What does the voltage say on the dashboard?

And yes, master is like any other version, you can just re-flash a release version after that.

### mtmorandba-code on 2026-07-23

I will sample the voltage rail every second for 10 minutes and see how much it wanders. As I am using claude to help with troubleshooting and trying different options. Power supply was one of our 1st checks. 

### mtmorandba-code on 2026-07-23

Dashboard voltage looks rock solid: I sampled /api/system/info at 1 Hz for 10 minutes — 600 samples, input rail mean 5327 mV, total spread 16 mV (essentially one ADC step: 90% of samples read exactly 5328 mV), core voltage 1052–1054 mV, current 11.2–11.4 A with normal load variation. No sags or dropouts. That rules out slow supply issues, though I appreciate a 1 Hz poll can't see switching ripple — I don't have a spare 5 V supply to swap-test with at the moment, so I can't fully exonerate the PSU; if I add another unit later I'll use its PSU as the cross-check.

One data point that bears on the ripple theory either way: the duplicates are strictly localized. Across both v2.14.2 and master captures, all 37 bursts originate from cores 66–79 — one domain of four — with the other three domains clean, and the per-domain hashrate telemetry shows the same single domain misbehaving ([225, 257, 269775, 287] on master; that same domain read 0 with an errorCount overflow on v2.14.2). Supply ripple reaches the whole chip, so a defect this surgical seems more consistent with a marginal domain on the die — though ripple aggravating an already-borderline domain is plausible too. Interested whether your 601's domains array shows anything unusual.

Good to know re-flashing back to a release is straightforward — I'll return to v2.14.2 (or the next release) once testing wraps up.

### adammwest on 2026-07-23

for me there are 2 interesting behaviours here
> `aa 55 8d 1a 2e 9b 89 aa 55 8d 1a` 

partially related https://github.com/bitaxeorg/ESP-Miner/issues/24 https://github.com/bitaxeorg/ESP-Miner/pull/851
these partial frame writes are really rare
makes me think of HW problem

> 2.3s burst per unique result

the asic timeout value has not been changed in a very long time for the gamma it is 500ms, there is no path 
that get a different number, the alternate path is 500, so the asic is doing very strange things 
makes me think of a HW problem

Really the only thing you can do is change the fan speed and core voltage, maybe there is a special combination of frequency temperature and core voltage. 
Are you in a hot location?


> Is this a known errata for early Gamma 601 boards / BM1370 serial comms?

No 

> Is the uniform ~197x / ~2.3s repeat consistent with the result FIFO being re-read until the next result overwrites it (missing read-acknowledge)?

No its more like version increment has not been broadcast to some/all cores of the chip so the nonce range is repeated for the same header, hence getting the same solution for a core/s.

> Should duplicate nonces be filtered before mining.submit as a mitigation, to protect pools from duplicate spam when share diff is low?

The `drop the result if exactly the same` result seems to be a good idea. for uniqueness you need (job_id,extranonce2,rolled_version,nonce) 

21% error rate is high I only had 1 chip like that out of 32, most of mine (28/32) are <2% error
so most likely you have a bad ASIC
I second mutatrum's  `can you also contact the seller?`

### mtmorandba-code on 2026-07-24

Thanks — your version-broadcast mechanism fits my data well, and I've now tested the voltage suggestion. A few results, plus one correction to my earlier post.

**Version analysis supports intermittent broadcast failure.** All 37 bursts across my v2.14.2 and master captures carry exactly one (nonce, version) pair — perfect repeats, consistent with the affected cores re-searching the same header. But the *same* cores show *different* version values from burst to burst (e.g. core 70 appears in four bursts with four different versions). So the version isn't permanently stuck on that domain — it updates between bursts. This looks like an intermittent broadcast failure: some version/job updates don't take on cores 66–79, the core re-finds the same solution for ~2.3 s, then a later update lands and normal operation resumes. If the internal job cadence is 500 ms, a ~2.3 s burst suggests roughly every 4th–5th broadcast gets through to that domain.

**Temperature context:** yes, hot-ish — ~30 °C ambient (heatwave), fan pinned at 100%, chip holding ~59–60 °C / VR 61–64 °C at my usual 490 MHz / 1060 mV.

**Core voltage test: the pathology is operating-point sensitive.** 14 minutes at 1150 mV (1142 actual), same 490 MHz:

- Bursts *fragmented*: at 1060 mV the distribution is bimodal (results appear once or ~196×); at 1150 mV I got 51 bursts spanning 6–197 repeats, most under 100, only two full-length — consistent with broadcasts landing sooner on the deaf domain.
- Duplicate volume roughly halved (~156/min from cores 66–79 vs ~378/min at 1060 mV), while legitimate unique results held steady (~49/min vs ~40/min).
- UART corruption nearly vanished: 1 checksum/preamble error in 14 min vs 9 in 8.2 min at baseline (~15× reduction). The per-domain telemetry inflation dropped from ~286 TH to ~3.6 TH on the bad domain.

Confound to note: the voltage bump also raised chip temp from ~60 °C to ~71 °C (power 17→21 W), so strictly this shows operating-point sensitivity, not voltage alone — though if the domain were heat-aggravated it should have gotten *worse* hotter, and it got better, which leans voltage margin. I plan to run 400 MHz / 1150 mV (high margin, low heat) to separate the two; if bursts stay suppressed cool, voltage margin is the variable — and that's probably my keeper tune for this unit.

**Correction to my earlier post:** master does *not* appear to filter duplicate submits. My "5 accepted / 0 rejected in 1 h" was luck (no burst cleared the 131072 vardiff in that window). After ~10 h on master the counters read 59 accepted / 682 rejected, all "duplicate" (~68/h). So the submit-side dedup on (job_id, extranonce2, rolled_version, nonce) remains a worthwhile mitigation as proposed.

Minor note: one `Software reset due to exception/panic` on master (fb55a4f) in ~24 h of running — mentioning in case panics on this build are of interest; I have not seen a second one yet.

Seller has been contacted (Bitronics) with the domain-localization evidence — thanks both for the steer. Happy to keep testing on this unit in the meantime; it's a reliable reproducer.


### mutatrum on 2026-07-24

Can you connect it to serial over usb, and see if you can capture the crash exception?

### mtmorandba-code on 2026-07-31

Connected over serial as suggested — but there's no crash exception to
capture, because the ESP32 never crashes.

What's actually happening is a core voltage regulator overcurrent
shutdown. The ESP32 stays up throughout: WiFi holds, the web UI
responds, and it keeps pulling jobs from DATUM indefinitely. The ASIC
rail is simply dead.

    E (25206) TPS546: Status: 0x4850
    E (25206) TPS546: The voltage regulator is turned off
    E (25206) TPS546: An output overcurrent fault has occurred

STATUS_WORD 0x4850 = IOUT/POUT fault (bit 14), POWER_GOOD# deasserted
(bit 11), unit OFF (bit 6), IOUT_OC (bit 4).

Reproducible across three boots with different trigger methods:

| Trigger          | asic_result lines | Trip at   |
|------------------|-------------------|-----------|
| unknown          | 2                 | 25206 ms  |
| software restart | 2                 | 26603 ms  |
| cold power cycle | 4                 | 25521 ms  |

Same status word every time. The chip initialises cleanly, hashes for
~20 seconds, emits a handful of results, then the rail trips and never
comes back. Reported cores differ each run, so it isn't one core
misbehaving on submission.

Config from boot: 490 MHz, vcore 1060 mV, IOUT_OC_FAULT_LIMIT 30.00 A,
IOUT_OC_FAULT_RESPONSE 0xc0 (shutdown and latch off). Expected draw at
this operating point is roughly 11-13 A, so it's tripping at ~2.5x
normal.

Post-fault telemetry via /api/system/info:

    coreVoltageActual: 21     (commanded 1060)
    current:           -225.8 mA
    power:             4.995 W   (ESP32 + fan only)
    temp:              21.6 C    (ambient - chip dissipating nothing)
    hashRate:          0

Hardware: Bitaxe Gamma, 1x BM1370, board version 601, firmware fb55a4f.

I take this as the power-side view of the same defect behind the
cores 66-79 duplicate nonce bursts in #1820, rather than a separate
issue. Happy to be told otherwise.

One note for anyone attempting this: the ROM bootloader banner and
rst: code aren't capturable over the native USB CDC port, since the
device de-enumerates on reset and re-enumeration takes ~6 seconds.
A physical UART header would be needed. In this case it turned out
not to matter.
