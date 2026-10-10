# bitaxeorg/ESP-Miner issue #1571: v2.13.0 regression – non-BTC pools: Decode Coinbase disabled but banner remains and pool stats stay frozen (after reboot)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1571
> Collected: 2026-10-07
> Published: 2026-02-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1571
- State: open
- Author: 0xdeadbeefnetwork
- Opened: 2026-02-21
- Closed: n/a
- Labels: none

## Description

On ESP-Miner v2.13.0 only, when mining a non-Bitcoin stratum pool, disabling Decode Coinbase does not remove the coinbase warning banner.
At the same time, the pool/status panel statistics (for example Share %) remain stuck (e.g. Share: 0%) even though the logs clearly show accepted shares.

I disabled Decode Coinbase and rebooted the miner. The problem still occurs after reboot.

Mining itself is working correctly. This appears to be a UI / frontend or stats update regression in v2.13.0.

This issue does not occur on v2.12.2.

To Reproduce

Open the Bitaxe web UI.

Configure a non-Bitcoin stratum pool.

Start mining and confirm activity in the logs.

Go to Settings.

Uncheck Decode Coinbase.

Reboot the miner.

Return to the main / status page.

Observed (v2.13.0 only)

The coinbase warning banner is still shown.

Pool panel shows Share: 0% and does not update.

Expected behavior

When Decode Coinbase is unchecked, the coinbase warning banner should not be shown.

Pool and share statistics should update normally for non-Bitcoin pools when shares are accepted.


Additional context

Logs show valid work and accepted shares, for example:

asic_result ... diff 11659.9 of 4096
stratum_api: tx: {"method":"mining.submit", ...}
stratum_api: rx: {"error":null,"result":true}
stratum_task: message result accepted

Despite this, the main/status page continues to show Share: 0% and the coinbase warning banner.

This looks like a frontend or stats update regression in v2.13.0 that still depends on BTC / coinbase-decode related fields when mining non-Bitcoin pools, even after disabling Decode Coinbase and rebooting.

## Comments

### LsLoki on 2026-02-21

As per #1570 (closed) unchecking Decode Coinbase Tx does remove the coinbase warning banner, at least for some of us? Might it be worth you reinstalling your updates to be sure you have a clean install? 


### 0xdeadbeefnetwork on 2026-02-21

> As per [#1570](https://github.com/bitaxeorg/ESP-Miner/issues/1570) (closed) unchecking Decode Coinbase Tx does remove the coinbase warning banner, at least for some of us? Might it be worth you reinstalling your updates to be sure you have a clean install?

I've done so. No dice. Almost seems like an NVS issue. running this twice and rebooting twice fixes it, but no dice via the webUI. `curl -X PATCH http://[BITAXE-IP]/api/system -H "Content-Type: application/json" -d "{\"stratumDecodeCoinbase\": false}"` I am investigating this issue myself and so far coming up with no ideas. Also as a note, once running the curl command, trying to re-enble decode coinbase from webUI does not bring back the banner after reboot either.

### 0xdeadbeefnetwork on 2026-02-21

### What works
curl -X PATCH http://<device-ip>/api/system \
  -H "Content-Type: application/json" \
  -d '{"stratumDecodeCoinbase": 0}'

After reboot, the setting sticks and the warning banner is gone.

### What doesn't work
Unchecking "Decode Coinbase" in the web UI pool settings and saving.
After reboot, the setting reverts to enabled and the warning banner returns.

### Attempted fixes (none resolved the web UI issue)

1. **Angular sends boolean `false`, firmware expects number `0`**
   - p-checkbox with [binary]="true" produces JS boolean true/false
   - JSON.stringify sends `"stratumDecodeCoinbase": false`
   - curl sends `"stratumDecodeCoinbase": 0`
   - Firmware's cJSON accepts both (cJSON_IsBool and cJSON_IsNumber),
     so this shouldn't matter — but we patched it anyway:
     ```typescript
     // pool.component.ts - convert booleans to numbers before PATCH
     for (const key of Object.keys(form)) {
       if (typeof form[key] === 'boolean') {
         form[key] = form[key] ? 1 : 0;
       }
     }
     ```
   - Result: no change

2. **NVS async race condition**
   - PATCH handler returned HTTP 200 before NVS queue finished writing to flash
   - Added nvs_config_sync() to wait for queue to drain before responding
   - Result: curl became more reliable, web UI still broken

3. **check_settings_and_update() is all-or-nothing**
   - If ANY field in the PATCH payload fails validation, NOTHING is saved
   - The pool form sends ~15 fields at once
   - A single bad field silently kills the entire save
   - HTTP 400 is returned but the error may not be obvious in the UI
   - Status: not yet confirmed as root cause

4. **Browser caching stale assets**
   - Web server sets Cache-Control: max-age=2592000 (30 days)
   - Ctrl+Shift+R hard refresh attempted
   - Result: no change

### Still need to verify
- Browser DevTools Network tab: what payload does the web UI actually send?
- Is the PATCH response 200 or 400?
- Which specific field (if any) is failing validation and killing the save

### Files modified
- main/nvs_config.c (added nvs_config_sync)
- main/nvs_config.h (nvs_config_sync declaration)
- main/http_server/http_server.c (call nvs_config_sync, debug logging)
- main/http_server/axe-os/src/app/components/pool/pool.component.ts (bool→number)
- main/http_server/axe-os/src/app/components/home/home.component.ts (banner logic)

### mutatrum on 2026-02-22

Did you do a hard refresh of the dashbord?

### 0xdeadbeefnetwork on 2026-02-22

> Did you do a hard refresh of the dashbord?

control+shift+r? yes.

### ffisk on 2026-02-26

Hi, ditto on your issues plus

odd spacing on certain text fields, look at the worker description and block header sections (see image)

<img width="953" height="293" alt="Image" src="https://github.com/user-attachments/assets/1ddf795c-bea5-4f9e-8cda-7bb3dfec9d07" />

Ended up rollback to v2.12.2 to continue mining on my gammas.

### ryzhenkovmarat-max on 2026-03-10

подскажите как откатится до предыдущей версии дело в том после обновы не подключается к пулу

### ffisk on 2026-03-10

Just go to https://bitaxeorg.github.io/bitaxe-web-flasher - you may need to figure out which windows com port yours is, but then the selection for firmware version and you should be good to go...gl

<img width="550" height="412" alt="Image" src="https://github.com/user-attachments/assets/c474930a-cec7-4b1b-b26d-bde7eb596555" />
