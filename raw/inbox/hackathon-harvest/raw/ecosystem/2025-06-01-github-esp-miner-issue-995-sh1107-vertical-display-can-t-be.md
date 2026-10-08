# bitaxeorg/ESP-Miner issue #995: SH1107 vertical display can't be rotated

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/995
> Collected: 2026-10-07
> Published: 2025-06-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 995
- State: closed
- Author: mutatrum
- Opened: 2025-06-01
- Closed: 2025-06-22
- Labels: none

## Description

The pin-compatible vertical oriented SH1107 display (see #572) can't currently be configured to rotate. This is pending https://github.com/lvgl/lvgl/issues/7797 which will come with LVGL 9.3.

When this is fixed, the `flipscreen` flag should be changed into a rotation flag, which can be directly used with `lv_display_set_rotation`:

https://github.com/bitaxeorg/ESP-Miner/blob/f6c9276162ba52b8dcd26ced0c40e33195dda49e/main/display.c#L181

## Comments

### mutatrum on 2025-06-10

Fixed by #1022 

![Image](https://github.com/user-attachments/assets/34206e96-a08d-4a06-904c-dfd68e14d6f2)
