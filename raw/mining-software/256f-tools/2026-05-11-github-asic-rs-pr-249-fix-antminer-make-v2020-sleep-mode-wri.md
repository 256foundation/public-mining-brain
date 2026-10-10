# 256foundation/asic-rs pull request #249: fix(antminer): make v2020 sleep mode writes effective

> Source: https://github.com/256foundation/asic-rs/pull/249
> Collected: 2026-10-07
> Published: 2026-05-11

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 249
- State: closed
- Author: DanNicolau
- Opened: 2026-05-11
- Closed: 2026-05-14
- Labels: none

## Description

## Root Cause

  On at least some older Bitmain stock firmware, `get_miner_conf.cgi` reports the mode using `bitmain-work-mode`, but
  writing that same key back to `set_miner_conf.cgi` does not actually change the miner mode.

  Observed on:

  - Antminer S19j Pro
  - `INFO.CompileTime`: `Mon Dec 26 17:10:01 CST 2022`
  - `system_filesystem_version`: `Mon Dec 26 17:10:01 CST 2022`

  For this firmware:

  - `{"bitmain-work-mode":1}` returns `M000 OK` but leaves the miner in normal mode
  - `{"miner-mode":1}` returns `M000 OK` and changes both `stats.miner-mode` and `get_miner_conf.bitmain-work-mode` to sleep
  - `set_miner_conf.cgi` can take around 21s to respond, so the existing 5s timeout can falsely report failure

  ## Changes

  - For `AntMinerV2020::pause()` and `resume()`, write `miner-mode` first when either `miner-mode` or `bitmain-work-mode` is
  present.
  - Re-read `get_miner_conf.cgi` after writes and only return success if the target mode is reflected.
  - Fall back to writing `bitmain-work-mode` if `miner-mode` does not apply.
  - Increase `set_miner_conf` timeout to at least 30s.

  ## Validation

Tested on 2022 dec 26 fw and 2025 oct 15 fw.

## Comments

### b-rowan on 2026-05-11

As mentioned in the issue, please split this out into 2 different types, 1 for `v2020`, replacing the old code entirely with the code for this older version that fixes the issue, without any extra handling for newer stuff, and `v202?`, a copy/paste of what was in v2020 prior to this PR, with the version selection and name being based on an approximate "earliest" version where this was fixed.  Exactly what version this was fixed in can be refined at a later date, but I would like to try to be within a ~6 month period to try to be optimal in most cases.

### DanNicolau on 2026-05-13

Yes, I think it is good to go.

### b-rowan on 2026-05-14

Supersedes: #251
