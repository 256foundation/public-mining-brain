# 256foundation/emberone-usbserial-fw pull request #19: fix(usb): derive serial number from flash unique ID

> Source: https://github.com/256foundation/emberone-usbserial-fw/pull/19
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/emberone-usbserial-fw
- Type: pull request
- Number: 19
- State: closed
- Author: rkuester
- Opened: 2026-03-19
- Closed: 2026-03-19
- Labels: none

## Description

The JEDEC ID identifies the flash chip model, not individual chips, so all boards with the same flash part produced the same serial number. Use the per-chip unique ID (command 0x4B) instead.

## Comments

### rkuester on 2026-03-20

Thanks, @korbin. I appreciate all the reviews.
