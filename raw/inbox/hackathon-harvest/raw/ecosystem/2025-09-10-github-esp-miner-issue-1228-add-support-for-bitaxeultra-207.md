# bitaxeorg/ESP-Miner issue #1228: Add support for bitaxeUltra 207 external temp diode

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1228
> Collected: 2026-10-07
> Published: 2025-09-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1228
- State: closed
- Author: skot
- Opened: 2025-09-10
- Closed: 2025-11-29
- Labels: enhancement

## Description

All of the BM1366-based bitaxeUltra are setup to use the EMC2101 internal temperature sensor because the BM1366 doesn't have a die temp diode. 

In 207 I added a external diode Q1 - MMBT3904 connected to the EMC2101 placed near the ASIC. 

<img width="684" height="225" alt="Image" src="https://github.com/user-attachments/assets/7fd31c44-870b-4133-ace5-480951d695aa" />

To support this in esp-miner we need a 207-conditional part of the EMC2101 code to switch back to external temp diode (like is done for Max, Supra and Gamma). 

This will also need some temp calibrating (ideality and/or beta compensation). As-is it will still work just fine, but it will be using the EMC2101 internal temp sensor, which probably isn't as close to the ASIC as it was for previous bitaxeUltras

## Comments

### ghost on 2025-09-11

Doing some tests here for this.

** **

<img width="1223" height="779" alt="Image" src="https://github.com/user-attachments/assets/1a11a9f1-795d-49be-b795-73c04943979c" />

** **

<img width="774" height="657" alt="Image" src="https://github.com/user-attachments/assets/fd101e0d-287e-408f-ab8b-8966c58e219a" />

### skot on 2025-09-11

the EMC2101 has been moved farther away from the ASIC in 207, so using the EMC2101-internal temp sensor will probably read a little cooler. 

<img width="706" height="657" alt="Image" src="https://github.com/user-attachments/assets/feac6a96-d79b-4e59-8460-d2c8f8dfe85b" />
