# bitaxeorg/ESP-Miner issue #762: Build inside container breaks because npm is missing

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/762
> Collected: 2026-10-07
> Published: 2025-03-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 762
- State: closed
- Author: mapio
- Opened: 2025-03-11
- Closed: 2025-03-28
- Labels: none

## Description

If using the container with Visual Studio Code the build breaks (while attempting to create the axe-os web application) due to the lack of nodejs/npm in `espressif/idf:v5.4`.
