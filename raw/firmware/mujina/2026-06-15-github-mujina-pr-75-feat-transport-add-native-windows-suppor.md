# 256foundation/mujina pull request #75: feat(transport): add native Windows support

> Source: https://github.com/256foundation/mujina/pull/75
> Collected: 2026-10-07
> Published: 2026-06-15

- Repository: 256foundation/mujina
- Type: pull request
- Number: 75
- State: closed
- Author: aadhi1014
- Opened: 2026-06-15
- Closed: 2026-08-08
- Labels: none

## Description

## Summary

- **Windows USB discovery**: polls COM ports every 2s via `tokio_serial::available_ports()`, groups by VID:PID:serial, emits the same `UsbDeviceConnected`/`UsbDeviceDisconnected` events as the Linux udev path
- **Windows serial I/O**: `serial_windows.rs` wraps `tokio-serial` with async read/write, runtime baud rate changes, split reader/writer/control handles — identical API surface to the Unix implementation
- **Signal handling**: replaces `SIGINT`/`SIGTERM` with `tokio::signal::ctrl_c()` on Windows
- **Board matching**: switched from manufacturer/product string matching to VID:PID (`c0de:cafe`) — Windows reports "Microsoft" as manufacturer for CDC ACM devices instead of "OSMU"/"Bitaxe"
- **Async init**: `BitaxeBoard::new()` is now `async` to avoid "runtime within runtime" panics when opening the data port on Windows
- **Docs**: `WINDOWS.md` covers setup, architecture, troubleshooting, and known limitations

## Platform notes

Tested on Windows 11 with a BitAxe Gamma running bitaxe-raw firmware. No WSL2 or Docker required — runs as a native `.exe`.

Detection latency is ~2s on Windows (polling) vs near-instant on Linux (udev netlink). This is acceptable for mining use.

## Test plan

- [ ] Build on Windows: `cargo build --release`
- [ ] Plug in a BitAxe Gamma (bitaxe-raw firmware, VID:PID `c0de:cafe`) and confirm it appears in logs within 2s
- [ ] Unplug and confirm disconnect event is logged
- [ ] Confirm Linux build is unaffected (`cargo build` on Linux)
- [ ] Confirm `cargo check --target x86_64-unknown-linux-gnu` passes from Windows (cross-check)

## Files changed

| File | Change |
|------|--------|
| `transport/usb/windows.rs` | NEW — COM port polling discovery |
| `transport/serial_windows.rs` | NEW — async serial I/O via tokio-serial |
| `transport/mod.rs` | conditional compilation for Windows serial |
| `transport/usb.rs` | Clone impl, Windows platform wiring |
| `daemon.rs` | Windows Ctrl+C signal handling |
| `board/bitaxe.rs` | VID:PID matching, async new(), fan diagnostics |
| `WINDOWS.md` | setup and architecture docs |

🤖 Generated with [Claude Code](https://claude.com/claude-code)

## Comments

### rkuester on 2026-06-15

This is a great start, @aadhi1014. Thank you!
