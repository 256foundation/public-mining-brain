# AxeOS API

> Sources: Open Source Miners United (osmu.wiki, Bitaxe API Endpoints), collected 2026-10-07; bitaxeorg (ESP-Miner README), collected 2026-10-07
> Raw: [Bitaxe API Endpoints](../../raw/ecosystem/osmu-wiki-bitaxe-api.md); [ESP-Miner README](../../raw/ecosystem/github-bitaxeorg-esp-miner.md)
> Updated: 2026-10-07

## Overview

AxeOS, the web interface of the ESP-Miner firmware, exposes an HTTP API on the Bitaxe itself. It reports system and ASIC information, serves logged statistics, restarts and updates the device, and changes settings. Two sources describe it: the OSMU wiki and the ESP-Miner README. The README lists more endpoints than the wiki. Both point to an `openapi.yaml` file in the ESP-Miner repository as the complete specification. For the firmware itself see [AxeOS / ESP-Miner Firmware](axeos-esp-miner-firmware.md).

## Endpoints

Listed by both sources:

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/system/info` | System information |
| GET | `/api/system/asic` | ASIC settings information |
| GET | `/api/system/statistics` | System statistics; data logging must be on |
| GET | `/api/system/statistics/dashboard` | Statistics for the dashboard |
| GET | `/api/system/wifi/scan` | Scan for Wi-Fi networks |
| POST | `/api/system/restart` | Restart the system |
| POST | `/api/system/identify` | Identify the device |
| POST | `/api/system/OTA` | Update system firmware |
| POST | `/api/system/OTAWWW` | Update AxeOS |
| PATCH | `/api/system` | Update system settings |

Listed only in the README:

| Method | Path | Purpose |
|--------|------|---------|
| GET | `/api/system/scoreboard` | Top 20 highest difficulty shares |
| GET | `/api/system/logs` | Download system logs |
| WebSocket | `/api/ws` | Text stream log |
| WebSocket | `/api/ws/live` | Stream of partial system info updates |

The README's examples also call `/api/system/pause` and `/api/system/resume` to pause and resume mining, and send PUT requests to `/api/system/pools/0` and `/api/system/pools/1` to configure pool slots. One example sets a Stratum V1 pool and the other a Stratum V2 pool. The README says the API works with IP addresses or `.local` hostnames.

## Settings you can change

The wiki lists the settings that a PATCH to `/api/system` accepts. Several can go in one request. Some need a restart, but many apply on the fly.

- **Pool.** Primary and fallback stratum URL, port, user and password, and a flag to force the fallback pool. Ports range 1-65535.
- **Wi-Fi.** `ssid`, `wifiPass` and `hostname`.
- **ASIC.** `coreVoltage` in millivolts and `frequency` in MHz. Both need `overclockEnabled` set to 1.
- **Fan.** `autofanspeed` for automatic control, `fanspeed` as a manual percentage, and `temptarget` as the target temperature for automatic control.
- **Display.** `rotation`, `invertscreen` and `displayTimeout`.
- **Advanced.** `overheat_mode` and `statsFrequency`, the logging interval in seconds, where 0 disables logging.

The README adds `useCustomWWW`, which switches a custom web interface on or off.

## Responses

- All endpoints return JSON except the OTA update endpoints.
- `/api/system/asic` reports the ASIC model. The wiki maps models to boards: BM1366 for the Bitaxe Ultra, BM1368 for the Supra, BM1370 for the Gamma and BM1397 for the original Bitaxe.
- `/api/system/wifi/scan` returns networks with an authentication mode number and signal strength. The wiki rates -30 dBm as excellent and -90 dBm as unusable.
- `/api/system/statistics` only works when `statsFrequency` is above 0. A `columns` query parameter filters the output. Columns cover hashrate over several windows, temperatures, voltages, power and current, fan speed, Wi-Fi signal, free memory and pool response time.
- Wi-Fi and stratum passwords are write-only and never returned.
- Units: temperature in Celsius, power in watts, hashrate in GH/s, and ASIC voltage settings typically in millivolts.

## Status codes

| Code | Meaning |
|------|---------|
| `200 OK` | Request successful |
| `400 Bad Request` | Invalid request parameters or settings |
| `401 Unauthorized` | Client not in allowed network range |
| `500 Internal Server Error` | Server error occurred |

## See Also

- [AxeOS / ESP-Miner Firmware](axeos-esp-miner-firmware.md)
- [Bitaxe Model Lineup](bitaxe-models.md)
