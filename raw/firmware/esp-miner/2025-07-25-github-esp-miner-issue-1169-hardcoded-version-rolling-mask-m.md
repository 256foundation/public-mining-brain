# bitaxeorg/ESP-Miner issue #1169: hardcoded version-rolling.mask might exceed what ASIC can roll

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1169
> Collected: 2026-10-07
> Published: 2025-07-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1169
- State: open
- Author: skot
- Opened: 2025-07-25
- Closed: n/a
- Labels: bug, help wanted

## Description

hardcoded version-rolling.mask -> 0xFFFFFFFF in https://github.com/bitaxeorg/ESP-Miner/blob/0958185217f324c8fe786cd6ef05f22e117f616d/components/stratum/stratum_api.c#L424-L434

This might not agree with what the ASIC can actually roll. This parameter should be pulled from an ASIC-specific function in components/asic/ so we don't suggest to the pool something the hardware can't do.

## Comments

### mutatrum on 2025-07-30

How do we know what rolling mask the ASIC can do?

### adammwest on 2025-08-18

for bitmain chips so far we know they do
Max Roll = 65536/midstates
Max Space covered 65536

Versionmask= 65536<<13

proportional to nonce % and time %

This applies for 
Bm13
98/62/66/68/70 

Unsure about the new 1340 and other chips
I think this can be defined


### skot on 2025-08-18

I suppose for completeness we should add max ASIC version rolling to individual chip constants. We just have never needed this due to relatively low hashrate chains.

### vortexopenclaw on 2026-06-01

I dug into this as an issue-first explanation.

The hardcoded `ffffffff` mask does appear to over-advertise version rolling capability for BM1366/BM1368/BM1370. Their version-mask setters shift the mask right by 13 before writing the roll register, so only bits that survive into that register are actually usable. Advertising all 32 bits can therefore tell the pool the firmware can roll bits that the ASIC path will not apply.

The safer direction I tested was:

- add an ASIC-level helper for the supported version-rolling mask
- advertise the supported mask in `mining.configure` instead of hardcoding `ffffffff`
- clamp pool-provided masks from `mining.configure` and `mining.set_version_mask` before storing/applying them
- keep BM1397 behavior unchanged, since its setter is currently a placeholder and changing that path would broaden the scope

For BM1366/BM1368/BM1370, the supported mask used by the test branch was `1fffe000`.

Validation I ran on the proposed approach:

- `git diff --check`
- `GITHUB_ACTIONS=true idf.py -C test-ci build`
- firmware `idf.py build`
- test coverage for configure JSON and mask clamping, including `ffffffff -> 1fffe000`, low unsupported bits clamping to `00000000`, and BM1397 compatibility coverage
- hardware smoke on Bitaxe Gamma and a BM1368-based Bitaxe: both booted, API/UI stayed reachable, mining resumed, and both were rolled back healthy

Reference implementation from the closed PR, if useful for discussion: #1740
