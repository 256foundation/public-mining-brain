# 256foundation/asic-rs issue #326: Inconsistent MinerData fields when scanning Antminer T21 with different firmware (VNish vs Stock)

> Source: https://github.com/256foundation/asic-rs/issues/326
> Collected: 2026-10-07
> Published: 2026-08-13

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 326
- State: closed
- Author: Kraitcer
- Opened: 2026-08-13
- Closed: 2026-08-13
- Labels: none

## Description

Hi. I ran a test and scanned the device using a simple program in Rust, and this is what I got. The device with stock firmware, unlike the device with the VNish firmware, did not return the following fields:
inlet_chip_temperature

outlet_chip_temperature

voltage (board voltage)

tuned

expected_hashrate (per‑board)

serial_number (board serial)

chips – the full per‑chip array (always empty in Stock)

All other board‑level fields (board_temperature, frequency, active, working_chips, expected_chips) are present in both.
