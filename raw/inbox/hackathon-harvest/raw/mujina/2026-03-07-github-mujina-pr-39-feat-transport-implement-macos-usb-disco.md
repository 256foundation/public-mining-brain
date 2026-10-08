# 256foundation/mujina pull request #39: feat(transport): implement macOS USB discovery using IOKit

> Source: https://github.com/256foundation/mujina/pull/39
> Collected: 2026-10-07
> Published: 2026-03-07

- Repository: 256foundation/mujina
- Type: pull request
- Number: 39
- State: closed
- Author: skot
- Opened: 2026-03-07
- Closed: 2026-03-31
- Labels: none

## Description

## Summary
- add macOS USB discovery using IOKit
- support device enumeration and hotplug notifications
- map USB devices to /dev/cu.* serial ports by location ID
- document macOS support in the README

## Validation
- cargo test --no-run


## Comments

### skot on 2026-03-07

tested with a bitaxe-raw bitaxeGamma from MacOS and seems to be working.

### majoal0 on 2026-03-09

Tested on macOS with a BitAxe Gamma 602 connected via USB-C. The device was detected correctly and communication through Mujina worked as expected.

### rkuester on 2026-03-12

I assume you needed `cargo test --no-run` because `cargo test` hung. That's the bug tracked in #46. It should be fixed now by 9ea2497. Please try running `cargo test` again and let me know if it works for you on macOS.

### Nickamoto on 2026-03-17

Tested on: Mac mini (Apple M-series, macOS 26.2) with a Bitaxe Gamma (BM1370, AxeOS v2.13.0) connected via USB.

Build: Clean. No new errors or warnings introduced by this PR.

Hardware verification: The Bitaxe enumerates in IORegistry under IOUSBHostDevice (VID 0x303A / Espressif) with an associated IOSerialBSDClient at /dev/cu.usbmodem*. This is exactly the class and serial port path the PR targets.

Issues found:
1.  Race condition in monitor_blocking — enumerate_devices() is called before IOServiceAddMatchingNotification is registered. A device plugged in during that window will be missed. The standard IOKit pattern avoids this: register the notification first, then drain the returned iterator — the drain step already yields existing devices. The separate enumerate_devices() call is both redundant and racy.
 
2.  kIOMasterPortDefault is deprecated since macOS 12 — kIOMainPortDefault is the current replacement. Functionally equivalent (both are 0), but worth updating to avoid future warnings.
 
3.  Stale module doc in usb.rs — Line 10 still reads "macOS: Stub implementation (IOKit support planned for future)". Should be updated to reflect that macOS is now fully supported.
 
4.  _master_port field in MacOsIoKitDiscovery - Stores kIOMasterPortDefault (the constant 0) but is never used. The field could be removed entirely.

After flashing bitaxe-raw (esp-hal-update branch) onto the Bitaxe, re-ran the same discovery tests. The firmware presents a different USB descriptor than AxeOS:
    • bitaxe-raw: VID=c0de PID=cafe, product="Bitaxe", manufacturer="OSMU"
   • AxeOS: VID=303a PID=1001, product="USB JTAG/serial debug unit", manufacturer="Espressif"
  Both are correctly enumerated by MacOsIoKitDiscovery. Under bitaxe-raw, two serial ports are exposed and both are correctly resolved by find_serial_ports_for_device:
    • /dev/cu.usbmodem9e79bedc1 — control serial (I2C, GPIO, ADC)
   • /dev/cu.usbmodem9e79bedc3 — data serial (ASIC UART passthrough)

### rkuester on 2026-03-31

Merged this feature to main with a slightly different approach in d174cde. I've tested this with Bitaxe 601 connected to an M3 Mac running macOS 26.3 via the hub on a Studio Display. Other test reports are welcome, thanks!
