# 256foundation/emberone-usbserial-fw pull request #20: fix(control)!: unify response frame format

> Source: https://github.com/256foundation/emberone-usbserial-fw/pull/20
> Collected: 2026-10-07
> Published: 2026-03-28

- Repository: 256foundation/emberone-usbserial-fw
- Type: pull request
- Number: 20
- State: open
- Author: rkuester
- Opened: 2026-03-28
- Closed: n/a
- Labels: none

## Description

Add an explicit status code byte to all responses and make the length field mean total packet length, matching commands.

1) There was no way to distinguish a success response from an error response on the wire. The error code occupied the same position as the first data byte.

2) The length field had different semantics depending on whether the response was success or error. Success used payload-only length while error used total packet length.

Both are resolved by giving every response a status code at byte 3: 0x00 for success, existing codes for errors.

Bumps firmware version to v5.1.0 so the host can distinguish protocol versions via bcdDevice.

BREAKING CHANGE: response format adds a status byte at offset 3
