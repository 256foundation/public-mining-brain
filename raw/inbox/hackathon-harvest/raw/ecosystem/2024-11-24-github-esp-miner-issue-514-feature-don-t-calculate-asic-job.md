# bitaxeorg/ESP-Miner issue #514: Feature: don't calculate asic_job_frequency but measure it.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/514
> Collected: 2026-10-07
> Published: 2024-11-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 514
- State: open
- Author: mutatrum
- Opened: 2024-11-24
- Closed: n/a
- Labels: help wanted

## Description

Taken from Slack: 
---
As a test, I extended the job_frequency to 5000ms, which is too long, and I see this:

```
I (18251) ASIC_task: Send next job: 20000000 Nonce 00000000 0000000000000000 diff 10000
I (18241) stratum_task: setup message accepted
I (19341) bm1368Module: Job ID: 18, Core: 45/1, Ver: 12AE2000
I (19341) asic_result: Ver: 32AE2000 Nonce DE4C035A diff 417.7 of 10000.
I (19651) bm1368Module: Job ID: 18, Core: 52/13, Ver: 1807A000
I (19651) asic_result: Ver: 3807A000 Nonce BC080368 diff 288.5 of 10000.
I (21201) bm1368Module: Job ID: 18, Core: 45/1, Ver: 12AE2000
I (21201) asic_result: Ver: 32AE2000 Nonce DE4C035A diff 417.7 of 10000.
I (21511) bm1368Module: Job ID: 18, Core: 52/13, Ver: 1807A000
I (21511) asic_result: Ver: 3807A000 Nonce BC080368 diff 288.5 of 10000.
I (23061) bm1368Module: Job ID: 18, Core: 45/1, Ver: 12AE2000
I (23061) asic_result: Ver: 32AE2000 Nonce DE4C035A diff 417.7 of 10000.
```
It starts looping, it returns the same 2 nonces of that range, every 1860ms.

This gives me an idea, instead of trying to calculate exactly what this period needs to be, we can just feed it a job for a few seconds, and time how long it took the chip to loop around. No need for difficult calculations, works on all chips and all nonce range masks and such.

---

The 1860ms is awfully close to the 1812ms from #420  Is the measurement wrong, or is there some time measurement overhead? It seems - in this small sample - to be consistent.

## Comments

### mutatrum on 2024-12-17

Suprising measurement is that the time for a wrap-around is still 1860ms when the Supra is running at 600Mhz. Above was default at 525Mhz.

### adammwest on 2025-01-14

> Suprising measurement is that the time for a wrap-around is still 1860ms when the Supra is running at 600Mhz. Above was default at 525Mhz.
yes it is surprising good find!

I have verified this at 490 and 420 mhz with the same value 1.86
All things equal this means
time = space/frequency 
nonce_space ∝frequency
setting the frequency at least in some cases changes the nonce range.

### benjamin-wilson on 2025-06-02

Nack
