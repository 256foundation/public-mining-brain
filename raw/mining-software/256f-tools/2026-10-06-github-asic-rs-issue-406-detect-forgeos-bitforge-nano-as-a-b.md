# 256foundation/asic-rs issue #406: Detect ForgeOS (BitForge Nano) as a Bitaxe-family miner

> Source: https://github.com/256foundation/asic-rs/issues/406
> Collected: 2026-10-07
> Published: 2026-10-06

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 406
- State: open
- Author: DarrelXero
- Opened: 2026-10-06
- Closed: n/a
- Labels: none

## Description

BitForge Nano miners run [ForgeOS](https://github.com/WantClue/forge-os), a GPL fork of ESP-Miner/AxeOS for the BM1370. asic-rs doesn't detect them, because Bitaxe detection looks for "AxeOS" (or "Nerd") on the web root, and ForgeOS serves `<title>ForgeOS</title>`.

The ForgeOS `/api/system/info` endpoint has the same fields asic-rs already reads for Bitaxe: `ASICModel` BM1370, `boardVersion` 800, power, temp, `hashRate`, `uptimeSeconds`, `stratumUser` and `stratumPort`.

Impact: in sv2-apps and sv2-ui, Nanos connected through the Translator show up as `unmatched` with `management_ip: null`, even when `stratumUser` and port match exactly.

Suggested fix: also match "ForgeOS" in the Bitaxe firmware check (`asic-rs-firmwares/bitaxe/src/firmware.rs`, around L64-66), or add a BitForge entry that reuses the Bitaxe API parsing.

Tested on two BitForge Nanos running ForgeOS v1.7, with sv2-ui on Umbrel and the Translator on port 34255.

## Comments

### DarrelXero on 2026-10-06

Related: WantClue/forge-os#44
