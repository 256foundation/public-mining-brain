# bitaxeorg/ESP-Miner issue #518: Browsing for update file disallowed after unsuccessful initial attempt

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/518
> Collected: 2026-10-07
> Published: 2024-11-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 518
- State: closed
- Author: tdb3
- Opened: 2024-11-26
- Closed: 2024-11-30
- Labels: none

## Description

Settings page, `Update Firmware` and `Update Website` areas.

If the user mistakenly loads an incorrectly named update file (e.g. `dummy.bin` instead of `www.bin` or `esp-miner.bin`), the user receives an error toast (e.g. `Incorrect file, looking for www.bin`). Afterward, clicking the `Browse` button repeats the same error. The user is not permitted to browse for a new file (to remedy the mistake). This was observed on both Firefox and Chrome.

The current workaround is to refresh the `Settings` page, but the desired behavior would be permitting the user to browse for a new file without having to refresh the page.

![image](https://github.com/user-attachments/assets/22a8e906-849c-4baf-a0b5-443d3dc1fc82)


## Comments

### tdb3 on 2024-11-30

#521 fixed this issue nicely
