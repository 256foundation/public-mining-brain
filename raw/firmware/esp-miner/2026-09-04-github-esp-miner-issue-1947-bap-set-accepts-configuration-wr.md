# bitaxeorg/ESP-Miner issue #1947: BAP `SET` accepts configuration writes and restarts from any UART peer with no gate

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1947
> Collected: 2026-10-07
> Published: 2026-09-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1947
- State: closed
- Author: cbyam
- Opened: 2026-09-04
- Closed: 2026-09-08
- Labels: none

## Description

The BAP accessory UART's `SET` command has no authentication and no mode gate. Anything wired to the accessory header can issue it. From `main/bap/bap_handlers.c`, `SET` currently:

- `ssid` and `password`: write NVS, then call `esp_restart()`.
- `frequency`: applies live (`ASIC_set_frequency`, `ASIC_set_nonce_space`) and writes NVS.
- `asic_voltage`: writes NVS.
- `fan_speed` / `auto_fan_speed`: write NVS.

So a peer on the header can repoint the device at a different Wi-Fi network, change its clock and core voltage, and reboot it, with no confirmation from the owner.

Worth noting the code already has a mode concept: `SUB` and `REQ` are refused with `ap_mode_no_subscriptions` / "Request not allowed in AP mode" when the device is in setup-AP mode. `SET` is the one command with no check at all, so it's inconsistent with its siblings as well as ungated.

The threat here is physical or accessory-side, not remote, so this isn't urgent in the way the pool-side parsing bugs were. But BAP is intended for third-party accessories, and a compromised or malicious accessory shouldn't be able to reconfigure the miner silently.

A few options, roughly in increasing weight, for whoever owns BAP to pick from:

1. **Confirm on the device.** Require a physical button press (or a short on-screen confirmation window) before a `SET` that writes NVS or restarts is applied. Live-only tuning like `frequency` could stay immediate.
2. **Gate by mode.** Only accept `SET` for network credentials while the device is in setup-AP mode, matching how the existing AP-mode checks already partition behavior. Tuning parameters could stay allowed while mining.
3. **Pair the accessory.** A one-time pairing token stored in NVS that `SET` must present. Heavier, but it's the only option that actually authenticates the peer rather than just adding friction.

This is a UX decision, so it's the maintainers' call. That said, option 1 looks like the best fit: it's the smallest real gate, it needs no protocol change on the accessory side, and it reuses hardware the device already has. It would also close the "silent reconfigure" case without breaking the normal accessory flow, since an owner pressing a button once to accept a new Wi-Fi network is not a burden. Options 2 and 3 are worth it only if the button turns out to be unavailable on some boards or if third-party accessories need to reconfigure unattended.

Related: #1948 removes the Wi-Fi password from `SUB`, redacts credentials from the duplicate-path log, fixes a CR LF double-parse that ran `SET` twice, and makes the checksum uniform. That PR deliberately leaves `SET` alone because it's a UX decision, not a bug fix.


## Comments

### WantClue on 2026-09-08

This is on purpose as you need physical access and the GT Touch Display is the current only accessory that uses these
