# 256foundation/asic-rs issue #155: EPic miner dropped from scan when /capabilities returns Model: "undefined" (should fallback instead of returning None)

> Source: https://github.com/256foundation/asic-rs/issues/155
> Collected: 2026-10-07
> Published: 2026-03-02

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 155
- State: closed
- Author: DanNicolau
- Opened: 2026-03-02
- Closed: 2026-03-04
- Labels: none

## Description

When scanning an EPic/umcOS rig, asic-rs identifies the host as reachable and EPic-like, but if /capabilities returns "Model": "undefined", model parsing fails and the miner is dropped from results (None). This makes valid rigs invisible to callers. This is particularly an issue preventing rigs with 3 problematic hashboards (i.e. none alive) from being detected.

Environment
- asic-rs: 0.2.1 (also reproduced on 0.1.6 and 0.1.5)
- Caller path: MinerFactory::scan_stream_with_ip()
Observed behavior
- Scan returns no miner for host.
- Host is reachable and serving EPic endpoints:
  - GET http://<ip>:4028/summary -> 200, includes Software: "PowerPlay-BMS v1.14.0" and OS Type: "umcOS"
  - GET http://<ip>:4028/capabilities -> 200, includes Control Board Version.cpuHardware: "Amlogic" but Model is "undefined"

Expected behavior
- Miner should still be surfaced (with unknown model) rather than dropped.
- Scan should be resilient to missing/placeholder model metadata.

Root cause (code)
- get_model_epic parses capabilities["Model"] and requires known EPicModel variants.
- EPicModel enum is strict (BM520i, S19JProDual).
- On parse failure, factory path ends up as None and scan stream swallows error via .await.ok().flatten().

Suggested fix
- Add fallback handling for EPic unknown model values:
  1. Accept unknown model strings in EPic model parsing (e.g. Unknown(String) or generic EPic model), or
  2. If firmware identification succeeds but model parse fails, still return a generic miner/device object, or
  3. At minimum, propagate a typed error to caller instead of silently converting to None.
- Optional: treat "undefined", empty string, and null as explicit unknown-model cases.

## Comments

### DanNicolau on 2026-03-02

I'll probably put in a PR tomorrow for this.

### b-rowan on 2026-03-02

> I'll probably put in a PR tomorrow for this.

Sounds good.  I'm not really sure yet how we want to handle unknown models, mostly because it causes issues with chip counts and other static data, but I guess having a "catch-all" unknown model which maps to `DeviceInfo {None, None, None}` is probably fine...
