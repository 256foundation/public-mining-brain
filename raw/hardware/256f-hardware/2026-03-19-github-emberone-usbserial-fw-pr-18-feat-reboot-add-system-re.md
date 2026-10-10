# 256foundation/emberone-usbserial-fw pull request #18: feat(reboot): add system reboot commands

> Source: https://github.com/256foundation/emberone-usbserial-fw/pull/18
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/emberone-usbserial-fw
- Type: pull request
- Number: 18
- State: open
- Author: rkuester
- Opened: 2026-03-19
- Closed: n/a
- Labels: none

## Description

Add a System command page with reboot and reboot-to-bootloader commands. Both require a magic payload to guard against accidental triggering from line noise or framing desync. Neither sends a response; the host detects success by observing USB re-enumeration or a UF2 device appearing.

Reboot uses the cortex-m system reset. Reboot to bootloader calls the RP2040 ROM function that is the programmatic equivalent of holding the BOOTSEL button during reset.

## Comments

### rkuester on 2026-03-28

Waiting for #20. Merging one at a time.
