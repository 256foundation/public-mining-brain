# bitaxeorg/ESP-Miner issue #382: request: script to automate building recovery images for all hardware

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/382
> Collected: 2026-10-07
> Published: 2024-10-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 382
- State: open
- Author: skot
- Opened: 2024-10-07
- Closed: n/a
- Labels: enhancement, help wanted

## Description

The only difference in the recovery images for different hardware versions is some of the values in the config.cvs for the NVS. It would be slick to somehow automate the building of the recovery images for all known hardware versions.

This would probably making a JSON file that has the NVS parameters for all known hardware.

reminder: a recovery image is the same as a factory image, except for the `self_test` parameter is 0
