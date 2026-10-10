# bitaxeorg/ESP-Miner issue #1786: SV2 connects unauthenticated by default, and the cert validity window is parsed but never enforced

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1786
> Collected: 2026-10-07
> Published: 2026-06-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1786
- State: closed
- Author: cbyam
- Opened: 2026-06-23
- Closed: 2026-09-14
- Labels: bug, good first issue, accepted

## Description

**Describe the bug**

SV2 server authentication is implemented but neither enforced nor complete. The Noise_NX handshake does a real Schnorr/BIP-340 check of the pool's certificate against `stratumV2AuthorityPubkey` and fails closed on a bad signature (#1553), but two gaps leave that protection unused in practice. Both are in `components/stratum_v2/sv2_noise.c`:

1. Validity window parsed but never enforced. Step 14 decodes and logs `valid_from` / `not_valid_after` but never compares them to the current time, so an expired or replayed cert passes as long as the signature verifies. Root cause: the firmware has no clock, the lone `esp_sntp.h` include (in `stratum_v1_task.c`) is unused and nothing reads wall-clock time. Not SV2-specific either: without a time source SV1 TLS almost certainly skips cert dates too. Only the signature/chain half of cert validation works today; the expiry half is skipped everywhere.

2. No way to require authentication. With no authority key set (the default), the handshake takes the "Skipping certificate verification (no authority pubkey)" branch and connects anyway, so SV2 is encrypted-but-unauthenticated out of the box. The Authority Pubkey tooltip already warns that without the key "a man-in-the-middle attack could redirect your hashrate," but nothing lets the user act on it.

**To Reproduce**

Unauthenticated by default:
1. Pool Settings > Advanced Options > Stratum Protocol = SV2.
2. Leave SV2 Authority Pubkey blank, save, restart.
3. Connect to any SV2 pool; serial log shows "Skipping certificate verification (no authority pubkey)" and it mines, with no way to refuse.

Validity not enforced:
1. Set SV2 with a valid Authority Pubkey against a pool whose cert `not_valid_after` is in the past (or replay an old, still-validly-signed cert).
2. Connect; log shows "Server certificate verified OK" and mining proceeds.
3. Expected the expired/stale cert to be rejected.

**Expected behavior**

- A "require authentication" option that refuses to connect when no key is set or verification can't complete, instead of silently connecting unauthenticated.
- The signed validity window enforced (`valid_from <= now <= not_valid_after`) once a clock exists.

**Additional context**

Fixes, in priority order:

- Enforcement toggle (small): per-pool "require authentication" NVS bool + a checkbox in the existing SV2 options block, next to the Authority Pubkey field. Verify path unchanged; it just refuses to fall through when verification can't happen. Lets the user act on the MITM warning the UI already shows.

- Validity check + time source: add a coarse SNTP sync at boot (network's already up, ESP-IDF's `esp_netif_sntp` is a few lines), then enforce the window. The accuracy bar is low, cert windows are wide, so one boot-time fetch is plenty, no RTC needed, with a "skip if time unknown" path for the pre-sync window. Honest limit: NTP is unauthenticated, so an on-path attacker who spoofs time can defeat expiry anyway, this is defense-in-depth (honest expiry, misconfig, passive replay), not airtight against a determined MITM. Bonus: the same clock lets SV1 TLS enforce cert dates too.

- TOFU pinning (optional): for pools without a published key, pin the server static key on first connect and warn if it changes. Lower priority.

Happy to PR the enforcement toggle. I run NerdQAxe++ against my own SV2 pool, so I can test the server side (valid/expired/wrong-key/no-key certs), but would want a maintainer with a Bitaxe to confirm the on-device flash.

## Comments

### 0xf0xx0 on 2026-06-25

for 1, the bitaxe has no concept of the current time and we'd rather not call out to a timeserver for privacy reasons (see https://github.com/bitaxeorg/ESP-Miner/issues/601#issuecomment-2577644156). 2 should be fixed imo, a pr would be welcome :3 

### 0xf0xx0 on 2026-08-11

eventually we need to tackle the cert validation

### 0xf0xx0 on 2026-09-14

resolved in #1897
