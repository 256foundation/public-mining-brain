# 256foundation/asic-rs pull request #308: fix: epic volcminer control board parsing

> Source: https://github.com/256foundation/asic-rs/pull/308
> Collected: 2026-10-07
> Published: 2026-07-01

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 308
- State: closed
- Author: cfilipescu
- Opened: 2026-07-01
- Closed: 2026-07-01
- Labels: none

## Description

## Summary
- parse EPic PowerPlay `platform: TVXilinx` as VolcMiner `TVXilinx`
- keep generic AntMiner `Xilinx` platform parsing unchanged for AntMiner models
- handle generic Xilinx fallback as VolcMiner only when the detected make is VolcMiner
- add regression coverage for the ambiguous Xilinx cases

## Tests
- cargo test -p asic-rs-firmwares-epic
- cargo test -p asic-rs-makes-volcminer
- MINER_IP=10.208.0.242 cargo test parse_data_live_test -p asic-rs-firmwares-volcminer -- --ignored --nocapture
- MINER_IP=192.168.13.235 cargo test parse_data_live_test_auto_detect -p asic-rs-firmwares-epic -- --ignored --nocapture

## Comments

### cfilipescu on 2026-07-01

Updated the make checks to compare against `VolcMinerMake::default().to_string()` instead of the raw `"VolcMiner"` string.

I kept the explicit `platform == "TVXilinx"` guard because the live PowerPlay response that exposed this had `make=Unknown model=Unknown: undefined` with `platform: "TVXilinx"` and `cpu: "Xilinx Zynq Platform"`. If we only key off make there, that device falls through to the generic AntMiner Xilinx fallback again.
