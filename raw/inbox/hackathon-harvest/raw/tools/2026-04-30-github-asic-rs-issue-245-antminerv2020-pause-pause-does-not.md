# 256foundation/asic-rs issue #245: AntMinerV2020 Pause::pause does not support older stock set_miner_conf.cgi payload shape

> Source: https://github.com/256foundation/asic-rs/issues/245
> Collected: 2026-10-07
> Published: 2026-04-30

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 245
- State: closed
- Author: DanNicolau
- Opened: 2026-04-30
- Closed: 2026-05-14
- Labels: none

## Description

## Summary

  `AntMinerV2020::pause()` currently sends a partial JSON payload to `/cgi-bin/set_miner_conf.cgi`, but at least some older
  Bitmain stock firmware versions require the browser/UI-style full config payload with `Content-Type: text/
  plain;charset=UTF-8`.

  As a result, `pause()` returns `false` or times out, and the miner does not enter sleep mode.

  ## Current behavior

  For stock Antminer firmware, `Pause::pause()` reads `/cgi-bin/get_miner_conf.cgi`, then sends one of these partial JSON
  payloads:

  ```json
  {"miner-mode":"1"}
```
  or:
```json
  {"bitmain-work-mode":"1"}
```
  via AntMinerWebAPI::set_miner_conf.

  On the affected firmware, this does not change the mode. get_miner_conf.cgi continues to report:
```json
  "bitmain-work-mode": "0"
```
  ## Affected device / firmware

  Observed on:

  Antminer S19j Pro
  Linux 4.9.113 #1 SMP PREEMPT Mon Dec 26 17:29:52 CST 2022
  system_filesystem_version: Mon Dec 26 17:10:01 CST 2022
  firmware_type: Release

  ## Browser behavior that works

  The stock web UI sends a full config payload to the same endpoint:

  POST /cgi-bin/set_miner_conf.cgi
  Content-Type: text/plain;charset=UTF-8
  X-Requested-With: XMLHttpRequest
  Accept: application/json, text/javascript, */*; q=0.01

  Example body:
```json
  {
    "bitmain-fan-ctrl": false,
    "bitmain-fan-pwm": "100",
    "miner-mode": 1,
    "freq-level": "100",
    "pools": [
      {
        "url": "stratum+tcp://example:3334",
        "user": "user1",
        "pass": ""
      },
      {
        "url": "stratum+tcp://example:3334",
        "user": "user2",
        "pass": ""
      },
      {
        "url": "stratum+tcp://example:443",
        "user": "user3",
        "pass": ""
      }
    ]
  }
```
  Notable differences from the current asic-rs request:

  - Content-Type is text/plain;charset=UTF-8, not application/json
  - the body is the full miner config, not only the mode key
  - the UI uses miner-mode: 1 as a number
  - the UI includes existing pool/fan/frequency fields

  ## Expected behavior

  AntMinerV2020::pause() should support this older stock UI payload shape, or fall back to it when the partial JSON update
  does not apply.

  A possible approach:

  1. Read get_miner_conf.cgi
  2. Try the current partial JSON behavior
  3. Re-read config and verify sleep mode
  4. If unchanged, send a full UI-style config payload using text/plain;charset=UTF-8
  5. Confirm either miner-mode == 1 or bitmain-work-mode == 1

  ## Why this matters

  Consumers of Pause::pause() expect a successful result to mean the miner is actually entering sleep mode. On this
  firmware, the current call can fail or time out without changing the miner state, preventing safe workflows that need
  mining stopped before installation or maintenance.

## Comments

### DanNicolau on 2026-04-30

Let me know if this is in scope for asic-rs. I realize there may be some complications around sending the full payload because there are other fields which really should be orthogonal to miner-mode, so I'd understand if this won't be supported, but I think it should be addressed at least.

### b-rowan on 2026-04-30

Makes sense.  As always, the goal is the best miner support possible, so I think the fix for this is to try to figure out the newest firmware where this isn't an issue, then create a versioned struct for that, making these changes on the current v2020 version.

@DanNicolau could you test a few things?  

- Can you try sending the work mode value and an integer instead with the small payload, to see if that improves it?
- Can you see if you can find the version where this stops being an issue and starts working properly?
- If possible, could you try on some other bitmain S miner types with firmware versions similar to this to see if the functionality is the same, and do the same thing with testing the latest version for those where this stops happening?

I want to answer a few questions here, namely:
- Is it just needing an int?
- What firmware should we switch this functionality at?
- Is it miner specific which version it changes on?

### DanNicolau on 2026-04-30

Sure I'll get some more details in the next few days. I'm not sure if I have a lot of versions similar, but I'll look around. Also, in my exploration of stock firmware I've learned that the changes bitmain makes are not necessarily chronological between versions; i.e. an S19kpro version released in October 2025 may contain changes that are not in an S21 pro from January 2026 for instance. I think for most or all of the asic-rs features this can be ignored, but it may come up in the future.

### DanNicolau on 2026-04-30

After some further testing the S19jpro firmware that I'm testing on (even if a good request is made) still doesn't actually go to sleep until a reboot occurs. I'll check to see if other stock firmware versions have a working sleep mode without reboot, and if the current api is compatible with them. This change may not even be necessary if it's just for this version and the api is broken.

### DanNicolau on 2026-05-11

  Tested again on the affected device:

  - Model: Antminer S19j Pro
  - `INFO.CompileTime`: `Mon Dec 26 17:10:01 CST 2022`
  - `system_filesystem_version`: `Mon Dec 26 17:10:01 CST 2022`
  - Config endpoint reports `bitmain-work-mode`
  - Runtime stats endpoint reports `miner-mode`

  Findings:

  - Small JSON payload `{"bitmain-work-mode":1}` returns `{"stats":"success","code":"M000","msg":"OK!"}` but does **not**
  change the mode. `get_miner_conf.cgi` still reports `"bitmain-work-mode":"0"` and `stats.cgi` still reports `"miner-
  mode":0`.
  - Small JSON payload `{"miner-mode":1}` returns the same success response and **does** change the mode. Afterward,
  `get_miner_conf.cgi` reports `"bitmain-work-mode":"1"` and `stats.cgi` reports `"miner-mode":1`.
  - So for this firmware, the issue is not just string vs integer. The read key is `bitmain-work-mode`, but the effective
  write key is `miner-mode`.
  - `set_miner_conf.cgi` responses take about 21 seconds on this firmware, so a 5s timeout can falsely report failure even
  when the request eventually applies.
  - Even after the mode is set to sleep, hashrate did not drop within 60s. A reboot was still required before the install
  flow could safely continue, matching my earlier observation.

  Local fix tested successfully:

  - For `AntMinerV2020`, try writing `miner-mode` first when either `miner-mode` or `bitmain-work-mode` is present.
  - Re-read `get_miner_conf.cgi` and only return success if either mode field reflects the target mode.
  - Fall back to writing `bitmain-work-mode` if `miner-mode` does not apply.
  - Increase `set_miner_conf` timeout to at least 30s.

  With that local change, the install flow got past sleep mode, detected that hashrate stayed active, rebooted the miner,
  reconnected, and completed the install successfully.

--

I'll get a PR in with these changes soon so we can discuss if this is the right direction.

### b-rowan on 2026-05-11

Main concern is if that will work on newer versions of stock FW, my guess is that this will end up having to be broken into versions based on when this issue stops happening.  Something like `v2020` -> updated implementation as with this issue, `v202x` -> old version from v2020 that doesnt have this issue.

### DanNicolau on 2026-05-11

I will check a few versions soon to see how this strategy interacts with new versions, thanks

### b-rowan on 2026-05-14

Fixed in #249
