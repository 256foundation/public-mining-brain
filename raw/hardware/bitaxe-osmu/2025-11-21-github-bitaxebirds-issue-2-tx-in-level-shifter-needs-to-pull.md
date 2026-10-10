# bitaxeorg/bitaxeBIRDS issue #2: TX_IN level shifter needs to pull low, not high

> Source: https://github.com/bitaxeorg/bitaxeBIRDS/issues/2
> Collected: 2026-10-07
> Published: 2025-11-21

- Repository: bitaxeorg/bitaxeBIRDS
- Type: issue
- Number: 2
- State: closed
- Author: skot
- Opened: 2025-11-21
- Closed: 2026-02-10
- Labels: bug

## Description

the ASIC `TX_IN` signal level shifter is incorrectly pulling high, when it should pull low.

R36, R42, and R48 need to pull down to GND_L

## Comments

### skot on 2025-11-22

<img width="1130" height="981" alt="Image" src="https://github.com/user-attachments/assets/ed2a3188-05d5-4aea-aa15-9f65400e5515" />
