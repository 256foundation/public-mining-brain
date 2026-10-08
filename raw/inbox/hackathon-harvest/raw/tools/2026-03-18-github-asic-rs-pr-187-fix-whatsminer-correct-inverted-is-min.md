# 256foundation/asic-rs pull request #187: fix(whatsminer): correct inverted is_mining logic across all backends

> Source: https://github.com/256foundation/asic-rs/pull/187
> Collected: 2026-10-07
> Published: 2026-03-18

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 187
- State: closed
- Author: ankitgoswami
- Opened: 2026-03-18
- Closed: 2026-03-19
- Labels: none

## Description

## Summary

- **V1/V2**: `parse_is_mining` was inverted — the `btmineroff`/`mineroff` field means "miner is off", so `"true"` means mining is OFF, but the old code returned `true` (mining active). Added fallback extraction at `/Msg/mineroff` for newer firmware responding to the legacy API.
- **V3**: Had no implementation (trait default always returned `true`). Now extracts the `working` field from `get.device.info` at `/msg/miner/working`.
- Named intermediate variables (`miner_off`, `working`) to match the actual API field names so the inversion logic is self-documenting.

## Test plan

- [x] Unit tests for `parse_is_mining` covering `mineroff="true"`, `mineroff="false"`, and missing field
- [x] Verified against M60SVK40 (V3 backend): `pause()` → `is_mining=false`, `resume()` → `is_mining=true`
- [x] Verified against M50SVH50 (V2 backend, fw 20240624): `pause()` → `is_mining=false`, `resume()` → `is_mining=true`
- [ ] Verify against a V1-era WhatsMiner

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### b-rowan on 2026-03-18

```
{
  "STATUS": "S",
  "When": 1773871985,
  "Code": 131,
  "Msg": {
    "mineroff": "false",
    "mineroff_reason": "",
    "mineroff_time": "",
    "FirmwareVersion": "20230803.11.REL",
    "power_mode": "",
    "hash_percent": ""
  },
  "Description": ""
}
```

From V2 miner.  V1 should be the same.

### b-rowan on 2026-03-18

```
{
  "STATUS": "S",
  "When": 1773872028,
  "Code": 131,
  "Msg": {
    "mineroff": "false",
    "mineroff_reason": "",
    "mineroff_time": "",
    "FirmwareVersion": "20240924.14.Rel",
    "power_mode": "normal",
    "power_limit_set": "3300",
    "hash_percent": "0"
  },
  "Description": ""
}
```

Another firmware version.

### b-rowan on 2026-03-18

```
{
  "STATUS": "S",
  "When": 1773872068,
  "Code": 131,
  "Msg": {
    "mineroff": "false",
    "FirmwareVersion": "20230208.18.Rel",
    "power_mode": "normal",
    "hash_percent": "0"
  },
  "Description": ""
}
```

Older still.  This might be closer to the V1 API.

### b-rowan on 2026-03-18

```
{
  "STATUS": "S",
  "When": 1773872125,
  "Code": 131,
  "Msg": {
    "mineroff": "false",
    "mineroff_reason": "",
    "mineroff_time": "",
    "FirmwareVersion": "20250214.16.1",
    "power_mode": "",
    "power_limit_set": "2147483647",
    "hash_percent": ""
  },
  "Description": ""
}
```

Here's the result from a V3 device.

### b-rowan on 2026-03-18

I'll see if I can confirm V1 results tomorrow, we have some M20s laying around that use 1.4.0

### ankitgoswami on 2026-03-18

I left the /SUMMARY/0/btmineroff extraction path in assuming it was for V1

### b-rowan on 2026-03-18

> I left the /SUMMARY/0/btmineroff extraction path in assuming it was for V1

That's my guess too, but it might be one or the other for V1/V2, I'll know more tomorrow.

### b-rowan on 2026-03-19

```
{
  "STATUS": "S",
  "When": 1773930539,
  "Code": 131,
  "Msg": {
    "btmineroff": "true",
    "Firmware Version": "'20220919.15.REL'"
  },
  "Description": "whatsminer v1.4.0"
}
```

V1 is in fact the one with `btmineroff`.
