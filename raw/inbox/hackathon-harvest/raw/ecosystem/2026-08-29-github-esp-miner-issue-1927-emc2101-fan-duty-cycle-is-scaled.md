# bitaxeorg/ESP-Miner issue #1927: EMC2101 fan duty cycle is scaled against 63 but the register maximum is 2*PWM_F (46)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1927
> Collected: 2026-10-07
> Published: 2026-08-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1927
- State: open
- Author: Raoulito
- Opened: 2026-08-29
- Closed: n/a
- Labels: bug

## Description

## Summary

`EMC2101_set_fan_speed()` scales the requested percentage against `63`, but the maximum meaningful value of the Fan Setting register is `2 * PWM_F` = **46** with the driver's effective configuration. Every fan request is therefore ~1.37x too high, and everything at or above 73% saturates at 100% duty.

I have a working fix, but **correcting this in isolation caused a thermal shutdown on real hardware**, so I'm opening an issue rather than a PR — the naive fix breaks existing installations and the migration needs a maintainer decision.

## The defect

```c
speed = (uint8_t) (63.0 * percent);
i2c_bitaxe_register_write_byte(emc2101_dev_handle, EMC2101_REG_FAN_SETTING, speed);
```

Per the datasheet, duty cycle in Direct Setting mode is

```
duty_cycle = FAN_SETTING / (2 * PWM_F)
```

`PWM_F` (register `0x4D`) resets to `0x17` (23) and `EMC2101_init()` never writes it, so the ceiling is 46.

| requested | writes | actual duty |
|---|---|---|
| 25% | 15 | 33% |
| 50% | 31 | 67% |
| 63% | 39 | 85% |
| 73% | 45 | 98% |
| 74%+ | 46 | 100% |

Two consequences: fans run faster than commanded across the whole range, and the top quarter of the control range does nothing. `FAN_CONTROLLER_task` drives this from a PID with `outMax = 100`, so roughly a quarter of the controller's output span has no authority.

Corroboration for the reset value and the formula:

- [Adafruit_CircuitPython_EMC2101 #19](https://github.com/adafruit/Adafruit_CircuitPython_EMC2101/issues/19) — "PWM_F defaults to 0x17 after reset, not the maximum and recommended 0x1f... DUTY_CYCLE = FAN_SETTING / (PWM_F * 2) * 100%"
- [ESPHome EMC2101 docs](https://esphome.io/components/emc2101/) — "with the default values the PWM signal will have a frequency of 7.83KHz and a resolution of 2.17%", i.e. `360kHz / (2*23)` and `1/46`

## Why a naive fix is dangerous

Tested on a Bitaxe Supra, board 401, BM1368 at 500 MHz / 1166 mV, fan in **manual** mode at 53%.

That board had been stable for days at 68 °C. 53% commanded was producing 72% actual duty. After correcting the scaling, 53% commanded produced 52% duty — a 27% airflow reduction, with no feedback loop to compensate because the fan was in manual mode. The board climbed from 68 °C to the 75 °C `THROTTLE_TEMP` and `POWER_MANAGEMENT_task` entered safe mode, which also rewrote NVS to `autofanspeed = false`, `manualFanSpeed = 100`, and dropped voltage and frequency by 100 each.

The point generalises: **every existing installation's fan configuration — manual value, `minFanSpeed`, `temptarget` — has been calibrated against the 1.37x over-drive.** Correcting the scaling silently removes 27% of airflow from all of them at once. Users in manual mode get no compensation at all. Users on the PID get compensation limited by `Ki`, which resolves to 0.01 per 100 ms sample, i.e. ~0.1% of fan output per second per degree of error.

## Supporting measurements

Same board, 500 MHz / 1166 mV, upstream scaling, manual fan, 10 minutes settling per point. `power` is total input measured by the onboard INA260, so it includes fan draw:

| fan cmd | actual duty | rpm | temp | power | J/TH |
|---|---|---|---|---|---|
| 53% | 72% | 5137 | 68 °C | 13.93 W | 21.83 |
| 56% | 76% | 5320 | 65 °C | 13.45 W | 21.08 |
| 63% | 85% | 6033 | 62 °C | 13.47 W | 21.11 |

Two things worth noting for anyone working on fan control here:

**Leakage is measurable and significant.** At a fixed operating point, power tracked temperature at ~0.16 W/°C (0.57 W over 4 °C, then 0.48 W over 3 °C — two independent measurements). Running 6 °C cooler was worth ~1 W on a 14 W board, about 3% efficiency.

**There is a real optimum.** Fan power grows roughly with the cube of RPM while temperature gains shrink, so total system power has a minimum. On this board it was flat between 76% and 85% duty and would rise beyond. A controller that simply chases `temptarget` will overshoot that optimum.

## Suggested approach

Correcting the scaling alone is not enough. Landing this safely probably needs, in one change:

1. Correct the duty mapping, and write `PWM_F` explicitly rather than relying on the reset value.
2. Fix the PID startup handover (filed separately) so the fan doesn't drop to `minFanSpeed` when the ASIC reaches full power.
3. Revisit `Ki`, so the integrator can traverse the control range in seconds rather than minutes.
4. Decide on migration for existing configs. Scaling stored `manualFanSpeed` and `minFanSpeed` by 63/46 on upgrade would preserve current airflow; otherwise this needs to be a loud release note.

I'm happy to prepare that as a PR if there's agreement on the approach, particularly on migration — but I only have one board variant (EMC2101 with `emc_internal_temp`), so I can't validate the external-diode path or the EMC2103/EMC2302 boards.

The same `2 * PWM_F` question likely applies to `EMC2103_set_fan_speed()` and `EMC2302_set_fan_speed()`, which scale against 255 and would need checking against their own datasheets.
