# bitaxeorg/ESP-Miner issue #1758: Sv2: No SubmitSharesExtended frames sent — handshake + OpenChannel succeed, then silence (v2.14.0)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1758
> Collected: 2026-10-07
> Published: 2026-06-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1758
- State: closed
- Author: dvb-projekt
- Opened: 2026-06-07
- Closed: 2026-06-08
- Labels: none

## Description

## Symptom

ESP-Miner (`v2.14.0`, BM1370) connects to a Stratum V2 pool, completes
the NOISE handshake, opens an extended mining channel, receives the
initial `NewExtendedMiningJob` + `SetNewPrevHash` — and then mines
silently without ever sending a `SubmitSharesExtended` (0x1b) frame.

The miner web UI shows steady hashrate (1.4 TH/s on my Bitaxe) and
`bestSessionDiff` climbing as expected, but the pool sees zero submit
frames over any duration. Switching the same hardware to V1 makes
shares flow instantly.

## Affected firmwares

- `bitaxeorg/ESP-Miner v2.14.0` — Bitaxe 1.4 TH/s, this issue
- `shufps/ESP-Miner-NerdQAxePlus v1.0.37.1` — NerdQAxe++ 6.5 TH/s,
  same behaviour ([NerdQAxe issue #625](https://github.com/shufps/ESP-Miner-NerdQAxePlus/issues/625))
- `shufps/ESP-Miner-NerdQAxePlus v1.1.0-alpha1` — Alpha firmware,
  same behaviour

Two independent ESP-Miner forks on different ASIC counts (one
BM1370 vs four BM1370) show the identical frame pattern. The Sv2-task
code path that handles share submission lives in
`main/tasks/stratum_v2_task.c` / `components/stratum_v2/sv2_protocol.c`
on both sides.

## Reproduction

1. Pool: any spec-conformant Sv2 pool. I tested against
   [dvb-WarpPool](https://github.com/dvb-projekt/dvb-WarpPool), which
   has independently been verified byte-identical against a
   spec-conformant miner's header reconstruction
   ([PR #33](https://github.com/dvb-projekt/dvb-WarpPool/pull/33)
   for `SetNewPrevHash.prev_hash` encoding,
   [PR #34](https://github.com/dvb-projekt/dvb-WarpPool/pull/34)
   for initial channel target from `nominal_hash_rate`).
2. Bitaxe / NerdQaxe pool settings: URL `<pool>`, Port `34254`,
   Stratum Protocol `V2`, Authority Pubkey configured.
3. Reboot, wait ~3 min, observe the pool log.

## Pool-side frame log (Bitaxe v2.14.0, peer `192.168.178.42:50224`)

```
DEBUG sv2 connection opened
DEBUG sv2 noise handshake complete
DEBUG sv2 frame in   ext=0     msg_type=0x00 (SetupConnection)              payload_len=42
DEBUG sv2 frame out  ext=0     msg_type=0x01 (SetupConnectionSuccess)       payload_len=6
DEBUG sv2 frame in   ext=0     msg_type=0x13 (OpenExtendedMiningChannel)    payload_len=95
DEBUG sv2 frame out  ext=0     msg_type=0x14 (OpenExtendedMiningChannelSuccess) payload_len=51
DEBUG sv2 frame out  ext=32768 msg_type=0x1f (NewExtendedMiningJob)         payload_len=591
DEBUG sv2 frame out  ext=32768 msg_type=0x20 (SetNewPrevHash)               payload_len=48
INFO  sv2 job broadcast fan-out job_id=2 channels=1 frames_out=2
INFO  sv2 job broadcast fan-out job_id=3 channels=1 frames_out=2
...
```

Frame counts after ~3 minutes:

| msg_type | direction | count |
|---|---|---|
| 0x00 SetupConnection | in | 1 |
| 0x01 SetupConnectionSuccess | out | 1 |
| 0x13 OpenExtendedMiningChannel | in | 1 |
| 0x14 OpenExtendedMiningChannelSuccess | out | 1 |
| 0x1f NewExtendedMiningJob | out | 1 + N broadcast |
| 0x20 SetNewPrevHash | out | 1 + N broadcast |
| **0x1b SubmitSharesExtended** | **in** | **0** |
| 0x1c SubmitSharesSuccess | out | 0 |
| 0x1d SubmitSharesError | out | 0 |

TCP stays `ESTABLISHED`. NOISE-NX completes cleanly. The miner never
reconnects (we'd see another handshake).

## Miner-side state at the same moment

`GET /api/system/info` on Bitaxe v2.14.0:

```json
{
  "version": "v2.14.0",
  "ASICModel": "BM1370",
  "stratumURL": "192.168.178.10",
  "stratumPort": 34254,
  "stratumProtocol": "SV2",
  "uptimeSeconds": 153,
  "hashRate_1m": 1440,
  "bestSessionDiff": 50774,
  "sharesAccepted": 0,
  "sharesRejected": 0
}
```

`bestSessionDiff=50774` and `hashRate_1m=1440 GH/s` confirm the chip
is hashing and finding work that should be submittable.
`sharesAccepted=0`, `sharesRejected=0` means it never tries.

## Switching to V1 on the same hardware: works instantly

| State | bitaxe v2.14.0 | NerdQAxe v1.0.37.1 |
|---|---|---|
| V1, 0s | 0 | 0 |
| V1, 60s | several accepted | several accepted |
| V1, 4 min | 50+ accepted, ~3 TH/s | 70+ accepted, ~6.5 TH/s |
| **SV2, 3 min** | **0 accepted, 0× 0x1b frame** | **0 accepted, 0× 0x1b frame** |

## Suspected location

`main/tasks/stratum_v2_task.c` and / or
`components/stratum_v2/sv2_protocol.c`. Setup / OpenChannel /
job-reception clearly works — the channel state advances and the
NOISE encryption pipeline carries frames in both directions. But the
mining loop seems to either (a) not call into the share-submit code
on a found share, (b) build the SubmitSharesExtended payload and drop
it before the NOISE codec, or (c) gate the send behind a condition
that's never satisfied (e.g. waiting for an initial `SetTarget`
that's not actually required by the spec — section 5.3.5 of the
[Sv2 Mining Protocol spec](https://github.com/stratum-mining/sv2-spec/blob/main/05-Mining-Protocol.md)
puts the initial target inside `OpenExtendedMiningChannel.Success`,
so a separate `SetTarget` is optional).

It might be the same code path that
[#1720](https://github.com/bitaxeorg/ESP-Miner/issues/1720) touched
for per-submit response timing — that change measured timings against
the submit but doesn't tell us whether the submit byte stream
actually leaves the device. A simple `ESP_LOGI("sv2", "sending submit
seq=%u len=%u", ...)` directly above the NOISE-encrypt + socket-send
call in the submit path would make this trivially diagnosable.

I'm happy to instrument the firmware build and capture a serial-
console trace if that would help, and to re-verify against my pool
the moment a fix is in. Pool-side is fully spec-conformant; if any
other Sv2 client connects successfully, that's a useful cross-check.

## Cross-reference

- NerdQAxePlus fork tracking the same behaviour:
  https://github.com/shufps/ESP-Miner-NerdQAxePlus/issues/625

## Comments

### dvb-projekt on 2026-06-07

Additional data point: the bug is **not** specific to Extended Channels.

I just switched the same Bitaxe v2.14.0 hardware to **"Standard Channels"** in the SV2 Channel Type setting, kept everything else (URL/port/authority pubkey) the same, and rebooted. The pool now sees the standard-channel handshake instead — but still zero submit frames:

```
DEBUG sv2 connection opened          peer=192.168.178.42:61853
DEBUG sv2 noise handshake complete   peer=192.168.178.42:61853
DEBUG sv2 frame in   ext=0     msg_type=0x00 (SetupConnection)            payload_len=42
DEBUG sv2 frame out  ext=0     msg_type=0x01 (SetupConnectionSuccess)     payload_len=6
DEBUG sv2 frame in   ext=0     msg_type=0x10 (OpenStandardMiningChannel)  payload_len=93
DEBUG sv2 frame out  ext=0     msg_type=0x11 (OpenStandardMiningChannelSuccess) payload_len=49
DEBUG sv2 frame out  ext=32768 msg_type=0x15 (NewMiningJob)               payload_len=49
DEBUG sv2 frame out  ext=32768 msg_type=0x20 (SetNewPrevHash)             payload_len=48
INFO  sv2 job broadcast fan-out job_id=9 channels=1 frames_out=2
... (additional job broadcasts, no submit frames)
```

After 171 s of mining the miner's web UI shows:

```
uptime=171s
bestSessionDiff=962874
hashRate_1m=1422 GH/s
sharesAccepted=0
sharesRejected=0
```

A diff-962874 share at `stratumDifficulty=1000` would normally trigger hundreds of submissions over the same window. Nothing hits the wire.

So the bug is in the shared "found-share → emit-frame" path, not in the Extended-channel-specific coinbase reconstruction. That narrows it: both `SubmitSharesStandard` (0x18) and `SubmitSharesExtended` (0x1b) are silent, which suggests the gating / never-called code is one level above the message type — somewhere between the chip-found-share notification and the SV2-task's submit-message builder.

Symptom summary, two channel types ✕ two firmware forks:

| Firmware | Channel | Open OK | Initial job OK | Submit frames |
|---|---|---|---|---|
| bitaxeorg ESP-Miner v2.14.0 | Extended | ✅ | ✅ | **0** |
| bitaxeorg ESP-Miner v2.14.0 | Standard | ✅ | ✅ | **0** |
| shufps NerdQAxePlus v1.0.37.1 | Extended | ✅ | ✅ | **0** |
| shufps NerdQAxePlus v1.1.0-alpha1 | Extended | ✅ | ✅ | **0** |


### warioishere on 2026-06-07

I wrote the SV2 implementation for both Bitaxe and NerdQAxe (they share the same code path, so it's the same client logic being tested in both cases). It runs fine against my own SV2 pool (Blitzpool, a TypeScript implementation written by the spec), against the SRI reference pool, and against Public Pool. It's used in production by miners every day on those.
  
A spec-conformant client working against three independent SV2 pools - one of which is the canonical reference - and failing only against yours, is a fairly strong signal that the issue is on the pool side.

My prime suspect is the target in OpenExtendedMiningChannelSuccess (and SetTarget if you send one). Per spec, target is a U256 little-endian "maximum target a share fulfilling this job can have". The client converts it to a pdiff and only submits nonces with nonce_diff >= pool_diff. If the target you serialize is too tight, or is in the wrong byte order, or in difficulty space instead of target space, you get exactly your symptom: channel opens, the miner hashes, bestSessionDiff climbs, and zero SubmitSharesExtended ever leave the wire.

bestSessionDiff = 1,096,416 in your log means the highest difficulty the miner found was ~1.1M. If your effective target maps to a pdiff above that, nothing qualifies for submission. For a starting handshake, SV2 pools typically send an initial target around pdiff a few thousand to bootstrap vardiff.

Worth comparing your OpenExtendedMiningChannelSuccess payload byte-by-byte against the SRI reference pool's output and re-reading section 5.x of the SV2 spec on target encoding.



### dvb-projekt on 2026-06-08

**Update — your diagnosis was spot-on, fixed pool-side.** Massive thank you, @warioishere.

You called it exactly: it was the `target` field in `OpenExtendedMiningChannelSuccess` (and the other five U256 wire sites). Our pool was sending the internal big-endian bytes raw — your client correctly read them as little-endian per Sv2 spec §5.3.1, computed an astronomically high pdiff, and silently filtered every share before submission. The "bestSessionDiff = 1,096,416 with zero submits" symptom was precisely the trap you described.

For diff = 1, the canonical pool target maps to `0x00000000_FFFF0000_00000000_..._00000000`. Pre-fix wire form (raw BE bytes) had the two `0xff` bytes at offsets 4–5 from the start. A spec-conformant LE reader recovers roughly `2^48`, computes `pdiff ≈ 2^176`, and rejects everything. After the fix the same bytes land at offsets 26–27 from the start (i.e. the same numeric value, written LE). Identical math, just the correct byte order on the wire.

Fix: dvb-projekt/dvb-WarpPool#37 — single `target_be_le_flip` helper in `pow.rs`, applied at all six U256 wire sites in `messages.rs`:

- `OpenStandardMiningChannel.max_target` (C→S)
- `OpenStandardMiningChannelSuccess.target` (S→C) ★
- `OpenExtendedMiningChannel.max_target` (C→S)
- `OpenExtendedMiningChannelSuccess.target` (S→C) ★
- `SetTarget.maximum_target` (S→C) ★
- `SetNewPrevHashTdp.target` (TDP)

Internal pipeline keeps the BE convention so the `pow_check_extended` path and `hash_meets_target` need no changes. The encoder and decoder both flip → roundtrip-identity holds, all existing tests still pass, and 5 new regression tests cover byte-order on the wire.

Live-verified end-to-end against three independent ESP-Miner family builds:

| Device | Firmware | Submit frames pre-fix | Submit frames post-fix |
|---|---|---|---|
| NerdOctaxe | shufps fork v1.0.37+ | 0 | many, ~88% accepted |
| Bitaxe-602-Gamma | bitaxeorg v2.14.0 mainline | 0 | many, ~35% accepted |
| NerdAxeGamma | gamma build | 0 | many, ~16% accepted |

The lower accept-rate on the small devices is not the firmware — it's a separate pool-side gap (we don't send `SetTarget`-based vardiff updates on Sv2 channels yet, so the initial target stays for the channel lifetime). Tracking as our own follow-up.

I want to be honest about the lesson here: until your comment we had filed this as a firmware-side bug ([details](https://github.com/shufps/ESP-Miner-NerdQAxePlus/issues/625)) — that was wrong, and the data point that should have killed that hypothesis (your client working against Blitzpool, the SRI reference pool, and Public Pool in production) was right there. We shipped exactly the same "spec says LE, we sent BE" mistake on `prev_hash` in v1.0.7 a week earlier and didn't connect the dots. That's on us.

Thank you for taking the time to actually read our logs and walk through the byte layout instead of just dismissing the report. Closing this from our side; happy to keep it open if you'd rather wait for an upstream sanity check.

— maintainer, dvb-projekt/dvb-WarpPool

### mutatrum on 2026-06-08

Awesome finding, and good analysis on both sides.
