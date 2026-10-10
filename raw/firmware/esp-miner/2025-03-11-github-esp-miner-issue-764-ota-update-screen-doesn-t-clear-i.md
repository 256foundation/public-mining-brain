# bitaxeorg/ESP-Miner issue #764: OTA update screen doesn't clear if an error occurs

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/764
> Collected: 2026-10-07
> Published: 2025-03-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 764
- State: open
- Author: 0xf0xx0
- Opened: 2025-03-11
- Closed: n/a
- Labels: enhancement, good first issue

## Description

**Describe the bug**
If an error occurs when sending a firmware file over the air, the screen will get stuck on the error screen and require a reset to clear, even though the chip is still hashing.

**To Reproduce**
Steps to reproduce the behavior:
1. Get a firmware file
2. Send a malformed OTA update request (notice the lack of POST): `curl --data "@esp-miner.bin" http://bitaxe/api/system/OTA`
3. Screen is stuck on
```
Firmware update
esp-miner.bin
Write Error
```

**Expected behavior**
I expected the boot button to clear the error screen.

**Hardware (please complete the following information):**
 - Bitaxe HW version: gamma (gekkoscience mod)
 - Bitaxe HW vendor: gekkoscience
 - ESP-Miner FW version: master 36272f63
 - Hash Frequency: irrelevant
 - Voltage: irrelevant
 - Pool URL, Port, User: irrelevant

**Additional information**
while the reproduction steps involve sending a malformed request, the same issue happens if the connection drops out mid-transfer.

## Comments

### mutatrum on 2025-03-12

It seems there are several issues:

1. It should probably stop hashing while performing the firmware update;
2. If there are non-fatal errors, e.g. before anything is written to the partition, those should be clearable by the user;
3. Handle cases when something actually breaks while updating.

Your case is the 2nd I guess, pressing the boot button is a nice way of clearing these errors.

### TowyTowy on 2026-07-08

Hi @mutatrum — I'd like to take this, scoped to your case #2 (the reporter's actual bug). The OTA/WWW handlers in `http_server.c` leave `is_firmware_update = true` on every error return, so `screen.c` keeps forcing `SCR_FIRMWARE` even though `esp_ota_abort` already rolled back and the chip never stopped hashing. Plan: mark those non-fatal errors with a separate flag and clear it from the boot-button handler (`screen_button_press`) — press to dismiss, exactly as you described. No auto-timeout, and nothing in the AxeOS Angular UI. I'll leave "stop hashing during a good update" as a separate follow-up so this stays small and reviewable.

I've got a Bitaxe Gamma to test on: I can repro the stuck screen with the curl from the issue and with a mid-transfer drop, confirm the boot button clears it while hashrate never dips, and check a real OTA still reboots cleanly. I'll put before/after photos of the screen in the PR.

### mutatrum on 2026-07-09

Take note of #1763 , that will change things quite a bit. Not sure how this case is handled there, or if others points are still open on the error handeling.

### TowyTowy on 2026-07-09

Thanks — yes, case 2 exactly. I've got the fix built (separate error flag set on the non-fatal OTA/WWW error paths, boot button clears it in screen_button_press, no auto-timeout, no AxeOS changes) and I'm testing it on a Gamma today. I've read through #1763 — it reworks POST_OTA_update in http_server.c so there'd be an overlap; I've kept my diff small (a helper + flag sets on the error returns) so it rebases easily whichever lands first, and happy to rework mine on top of #1763 if that's the preferred order.
