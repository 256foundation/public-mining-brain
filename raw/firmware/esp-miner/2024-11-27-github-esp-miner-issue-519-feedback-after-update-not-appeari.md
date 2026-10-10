# bitaxeorg/ESP-Miner issue #519: Feedback after update not appearing

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/519
> Collected: 2026-10-07
> Published: 2024-11-27

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 519
- State: closed
- Author: tdb3
- Opened: 2024-11-27
- Closed: 2024-12-01
- Labels: none

## Description

Settings Page, Update Firmware and Update Website forms.

When uploading a new firmware file (e.g. ), the page shows a `Working...` overlay, then appears to show no feedback of the completion status of the update (i.e. success or failure). This was tested using Firefox and Chrome.

Looks like there is code for this, but the Toasts weren't observed. https://github.com/skot/ESP-Miner/blob/29a543da76ba5fd19e07f43da87214613d67455a/main/http_server/axe-os/src/app/components/settings/settings.component.ts#L186-L200

Running developer tools showed:
![image](https://github.com/user-attachments/assets/6bc56bca-0658-4bdc-8a1a-d39d7b2434f6)


**To Reproduce**
Steps to reproduce the behavior:
1. Go to the `Settings` page
2. Click `Browse` in the `Update Website` form
3. Select `www.bin`

**Expected behavior**
Feedback is provided to the user.

**Hardware:**
 - Bitaxe HW version: Supra 401
 - ESP-Miner FW version: master (29a543da76ba5fd19e07f43da87214613d67455a)
 - Hash Frequency: N/A for issue
 - Voltage: N/A for issue
 - Pool URL, Port, User: N/A for issue



## Comments

### tdb3 on 2024-11-27

Looks like the intent of the existing code is to reload the page after `www.bin` update, which would be prudent (to force the user to use the new web UI rather than the client-side code remnant of the UI pre-update). Doesn't appear that this reload is occurring.

### skot on 2024-11-30

If we don't have to restart the ESP32 to reload the page, that works too!

### tdb3 on 2024-12-01

#521 fixes the issue (and provides a nice percentage status while waiting!)
