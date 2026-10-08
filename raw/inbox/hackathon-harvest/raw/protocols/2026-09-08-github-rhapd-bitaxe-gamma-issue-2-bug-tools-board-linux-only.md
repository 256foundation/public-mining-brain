# 256foundation/rhapd-bitaxe-gamma issue #2: bug: tools/board Linux-only port discovery

> Source: https://github.com/256foundation/rhapd-bitaxe-gamma/issues/2
> Collected: 2026-10-07
> Published: 2026-09-08

- Repository: 256foundation/rhapd-bitaxe-gamma
- Type: issue
- Number: 2
- State: open
- Author: cmckenney240
- Opened: 2026-09-08
- Closed: n/a
- Labels: none

## Description

## Issue Description

`tools/board` discovers serial ports by globbing Linux sysfs. On macOS the glob
matches nothing, so `find()` always returns `None` and both subcommands abort
with "no RHAP-D or ROM bootloader on USB" regardless of the board's actual
state. Because the `flash` recipe brackets espflash with those two calls,
`just flash` cannot complete on a macOS host.

`tools/board:61-72`:

```python
def ports():
    """Yield (device path, (vid, pid), interface number) for each CDC port."""
    for tty in sorted(glob.glob("/sys/class/tty/ttyACM*")):
        iface = os.path.realpath(tty + "/device")
        usb = os.path.dirname(iface)
```

`/sys` does not exist on macOS. CDC-ACM devices appear as `/dev/cu.usbmodem*`
and their USB metadata lives in the IOKit registry.

Everything else in the script is portable POSIX and works on macOS as-is: the
`termios` raw-mode setup in `open_raw()`, the SLIP framing, the ROM sync, and
the RTC watchdog register writes. Only `ports()` needs a platform branch.

## Expected Behavior

`tools/board bootloader` and `tools/board reset` locate the RHAP-D control port
(or a board already in the ROM bootloader) on macOS as they do on Linux, so
`just flash` performs the full button-free reflash cycle.

## Actual Behavior

Both subcommands exit with "no RHAP-D or ROM bootloader on USB" even with the
board enumerated and answering. 
## Reproduction Steps

1. On macOS, connect a Bitaxe Gamma running RHAP-D over USB.
2. Confirm the board is present and enumerated:
   ```
   $ ls /dev/cu.usbmodem*
   /dev/cu.usbmodem58e6c56bd3b41
   /dev/cu.usbmodem58e6c56bd3b43
   ```
3. Run `tools/board bootloader`.
4. Observe the abort described above; the same happens for `tools/board reset`.

## Suggested Fix

Add a `sys.platform == "darwin"` branch to `ports()`, parsing the IOKit registry
through `ioreg` and stdlib `plistlib`. This keeps the script's stated
"no dependency beyond the Python standard library" property. The Linux path is
untouched.

`mujina-miner/src/transport/usb/macos.rs`
does the same lookup natively, matching `IOSerialBSDClient` entries and walking
to the parent USB device with `kIORegistryIterateParents`, returning sorted
`/dev/cu.*` callout paths. The Python port mirrors that shape.

## Environment

- **Board:** Bitaxe Gamma 602 (BM1370), stock, no modifications
- **Firmware:** rhapd-bitaxe-gamma at `59e90f6` ("fix(control)!: unify response frame format")
- **Host:** macOS 26.6.2 (build 25G83), arm64 (Apple Silicon), Darwin 25.6.0
- **Python:** 3.14.5 (system `python3`)
- **Tools:** just 1.58.0, espup 0.17.1, cargo-espflash 4.4.0
- **Toolchain:** `rustc +esp` 1.97.0-nightly (1.97.0.0)
