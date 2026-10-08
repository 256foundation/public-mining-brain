# bitaxeorg/ESP-Miner issue #1950: feature: replace test mode with bitaxe-raw compatible mode

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1950
> Collected: 2026-10-07
> Published: 2026-09-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1950
- State: open
- Author: skot
- Opened: 2026-09-04
- Closed: n/a
- Labels: enhancement

## Description

Instead of having test mode run the tests directly from the ESP32, I think it would be more helpful/versatile to have test mode be a [bitaxe-raw](https://github.com/bitaxeorg/bitaxe-raw) compatible interface. Then what ever tests developers/manufacturers/troubleshooters would like to run, could be run from a USB connected PC. Tests could prolly even be run from a web browser. 

256F has been making some progress to standardize this protocol as [RAHP-D](https://github.com/256foundation/rhapd-bitaxe-gamma) although in this particular case it make sense to implement in C.

## Comments

### skot on 2026-09-04

factories already have to plug in via USB to flash the firmware, so it would be pretty easy to run a test suite on the new bitaxe right after flashing.

### skot on 2026-09-04

for situations like the TPS546 init where you want to test with what esp-miner is going to run, raw-mode could have commands to run those functions from esp-miner
