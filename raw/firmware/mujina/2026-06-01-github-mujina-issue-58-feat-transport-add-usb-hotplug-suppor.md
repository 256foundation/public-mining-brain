# 256foundation/mujina issue #58: feat(transport): add USB hotplug support on Windows

> Source: https://github.com/256foundation/mujina/issues/58
> Collected: 2026-10-07
> Published: 2026-06-01

- Repository: 256foundation/mujina
- Type: issue
- Number: 58
- State: open
- Author: rkuester
- Opened: 2026-06-01
- Closed: n/a
- Labels: contributor-friendly

## Description

Mujina detects USB hashboards being plugged and unplugged at runtime on Linux and macOS, but not yet on Windows. This would be a great self-contained first contribution for someone who wants to dig into the USB transport layer, ideally with a Windows machine and a board to test against.

Device enumeration and hotplug events already come from `nusb`, which is cross-platform, so the missing piece is the platform-specific step of mapping a discovered USB device to its serial port(s). See `mujina-miner/src/transport/usb.rs`, which selects a per-platform module (`linux.rs`, `macos.rs`) for `device_path` and `get_serial_ports` and falls back to a stub on everything else. Windows currently lands on that stub. The task is to add a `windows.rs` implementing those two functions (enumerating COM ports for a given USB device, likely via SetupAPI/WMI) and wire it up alongside the existing `#[cfg(target_os = ...)]` arms. The macOS implementation is the closest analog to follow, including its retry to handle the device appearing before its serial node does.
