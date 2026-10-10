# 256foundation/asic-rs pull request #182: feat: add firmware upgrade for antminer stock

> Source: https://github.com/256foundation/asic-rs/pull/182
> Collected: 2026-10-07
> Published: 2026-03-17

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 182
- State: closed
- Author: glitchpixelz
- Opened: 2026-03-17
- Closed: 2026-03-18
- Labels: none

## Description

Antminer stock firmware upgrades now support both merged BMU bundles and raw single-image .bmu files. For merged bundles, the backend reads miner_type.cgi, matches the correct internal image to the miner’s model/control-board subtype, and uploads only that selected payload. For raw images, it skips filename heuristics and uploads directly, relying on upgrade.cgi to accept or reject the firmware.

The upload path now also validates the Antminer response more strictly: success requires both HTTP success and the expected JSON payload (code = U000, stats = success), while malformed or rejected responses return explicit errors.

## Comments

### b-rowan on 2026-03-17

Concept ACK, but I think it might make sense to change the implementation a bit to make `FirmwareImage` generic with Ext traits.  Helps break things apart a bit, since the `mod.rs` files are starting to get pretty big.

### glitchpixelz on 2026-03-17

[Antminer T21 Firmware Testing Results.md](https://github.com/user-attachments/files/26070006/Antminer.T21.Firmware.Testing.Results.md)
5:30PM 3/17/2026

### b-rowan on 2026-03-18

Starting to get very close now, just a couple smaller style/nit things.

### glitchpixelz on 2026-03-18

[Antminer_Firmware_Upgrade_Tests_2026-03-18.md](https://github.com/user-attachments/files/26100738/Antminer_Firmware_Upgrade_Tests_2026-03-18.md)
4:55PM 3/18/2026
