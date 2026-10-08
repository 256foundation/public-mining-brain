# bitaxeorg/ESP-Miner issue #1921: Restart button on settings page form is never active in version 2.15.0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1921
> Collected: 2026-10-07
> Published: 2026-08-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1921
- State: closed
- Author: trprice
- Opened: 2026-08-29
- Closed: 2026-08-29
- Labels: none

## Description

The settings page has a restart button between the Save button and the "Disable Overclock Mode" button. After updating settings and clicking save the restart button can't be clicked to restart the device. The new restart icon at the top of the page works to restart the device.

If the disabling of this button is intentional to force use of the restart icon the button should likely be removed altogether because it just causes confusion.

<img width="3816" height="1896" alt="Image" src="https://github.com/user-attachments/assets/781105c2-7354-4b98-8322-d8b32c58147a" />

## Comments

### WantClue on 2026-08-29

You don't need to restart you device if you change the frequency or voltage. As well as the Statistics, these changes happen immediately on save. This is not an issue

### trprice on 2026-08-29

Oof, I didn't notice that as a change. Thanks
