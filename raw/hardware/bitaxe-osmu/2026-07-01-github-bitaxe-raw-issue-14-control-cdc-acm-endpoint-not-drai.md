# bitaxeorg/bitaxe-raw issue #14: Control CDC ACM endpoint not drained on Bitaxe Gamma over USB-IP (works fine for ASIC UART)

> Source: https://github.com/bitaxeorg/bitaxe-raw/issues/14
> Collected: 2026-10-07
> Published: 2026-07-01

- Repository: bitaxeorg/bitaxe-raw
- Type: issue
- Number: 14
- State: open
- Author: IxTechCrypto
- Opened: 2026-07-01
- Closed: n/a
- Labels: none

## Description

## Summary

Writes to the control CDC ACM interface hang indefinitely on my Bitaxe Gamma running current bitaxe-raw main. Writes to the ASIC UART CDC ACM on the same device work correctly. The two USB endpoints behave completely differently despite identical task structure in the firmware.

## Environment

- Bitaxe Gamma (BM1370), serial `4c792b82`
- bitaxe-raw at commit `109916f` (PR #8 esp-hal-update, HEAD of main)
- Flashed with `cargo espflash flash --release --chip esp32s3`
- Host: Windows 11 → WSL2 Ubuntu → usbipd-win 5.3.0 forwarding the Bitaxe into WSL

Note: I have not yet tested against a native Linux host without usbipd, so it's possible this is a usbipd-side interaction rather than a bitaxe-raw bug. Flagging that up front.

## What works

- USB enumeration: `lsusb -v -d c0de:cafe` shows manufacturer `OSMU`, product `Bitaxe`, both CDC ACM interfaces (`1-1:1.0` at ttyACM0 for control class, `1-1:1.2` at ttyACM1 for ASIC UART class, verified via `/sys/class/tty/`)
- Data port drains fine: writing 4096 bytes to `/dev/ttyACM1` completes in ~340 ms

## What doesn't work

- Writing any bytes to `/dev/ttyACM0` (the control interface) hangs. 4096-byte write returns `Write timeout` after 2 s. 6-byte GPIO frame also hangs.
- Behavior is identical whether:
  - Using Mujina (Rust, tokio-serial)
  - Using pyserial with `dtr=True, rts=True` explicitly set
  - Using raw `echo -en '\x06\x00\x00\x00\x06\x00' > /dev/ttyACM0` from bash

Response direction was never tested because the write never completes.

## Reproducer

```python
import serial, time
s = serial.Serial("/dev/ttyACM0", 115200, timeout=0.5, write_timeout=2.0)
s.dtr = True; s.rts = True
try:
    s.write(bytes([0x55] * 4096))
    s.flush()
    print("drained")
except serial.SerialTimeoutException:
    print("hang — control endpoint not being read by firmware")

## Comments

### rkuester on 2026-07-02

Tested your reproducer on a Bitaxe Gamma plugged directly into Linux (no usbipd). The control interface drained fine, and it responded afterward: a `GetAsicResetn` returned the expected reply.

### IxTechCrypto on 2026-07-03

So: Bitaxe + Mujina on Windows is a no-go at the moment. Native Linux only until either bitaxe-raw ships Microsoft OS Descriptors or Windows' usbser.sys learns to enable both endpoints of this composite. Not asking you to do either — just closing out the diagnosis on my end. I'll move on to other things. Thanks for taking a look

### rkuester on 2026-07-03

For what it's worth, the story may be complicated. As much as I'd love to blame Windows, it might still be Mujina and or bitaxe-raw's issue. The stack from kernel up through serial library may behave a bit differently on Windows, and exposing a bug.

I've seem some issues, even on Linux, where a failure of Mujina to read from one (or either?) of these serial channels causes the write direction to wedge itself. I could imagine the stacks on Windows and Linux handling reading and buffering differently in a way that affects what bitaxe-raw is seeing. Sending 4K of data may cause bitaxe-raw to respond with an error the test isn't reading. I haven't looked closer to see if that's an inherent limitation, a bitaxe-raw bug, or something that bitaxe-raw should handle differently (e.g., dropping data rather than blocking).

I'm curious to hear more if anyone chases this further.
