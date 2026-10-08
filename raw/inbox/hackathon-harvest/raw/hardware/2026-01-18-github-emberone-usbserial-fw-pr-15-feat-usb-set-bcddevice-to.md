# 256foundation/emberone-usbserial-fw pull request #15: feat(usb): set bcdDevice to v5.0.0 for hardware revision 5

> Source: https://github.com/256foundation/emberone-usbserial-fw/pull/15
> Collected: 2026-10-07
> Published: 2026-01-18

- Repository: 256foundation/emberone-usbserial-fw
- Type: pull request
- Number: 15
- State: closed
- Author: rkuester
- Opened: 2026-01-18
- Closed: 2026-03-20
- Labels: none

## Description

Use BCD version format where major indicates hardware revision and
minor.patch indicates firmware version. Firmware versioning restarts
with each hardware revision.

This allows Mujina to distinguish v4, v5, and future hardware revisions.

## Comments

### rkuester on 2026-02-06

@skot Would you please review and merge this? Also, perhaps we merge/rebase the `v5_support` branch into `main`, and remove `v5_support`.

### rkuester on 2026-03-19

> @skot Would you please review and merge this? Also, perhaps we merge/rebase the `v5_support` branch into `main`, and remove `v5_support`.

Submitted #17 for this purpose.

### rkuester on 2026-03-20

@skot Any objections to this one? I'd like to make another change that depends on this being merged.

### skot on 2026-03-20

LGTM. merged
