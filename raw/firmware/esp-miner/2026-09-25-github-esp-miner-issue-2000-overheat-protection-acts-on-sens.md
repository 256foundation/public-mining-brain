# bitaxeorg/ESP-Miner issue #2000: Overheat protection acts on sensor fault codes / corrupt I2C reads and persists the downgrade to NVS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/2000
> Collected: 2026-10-07
> Published: 2026-09-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 2000
- State: open
- Author: awi81
- Opened: 2026-09-25
- Closed: n/a
- Labels: none

## Description

**Describe the bug**

The overheat protection in `power_management_task.c` acts on temperature values that are sensor fault codes or corrupted I2C words, not real temperatures. When it trips it writes manual fan 100 %, `overheat_mode` and a reduced frequency/voltage to NVS. All of that survives reboots, so every spurious trip lowers the miner's settings for good. We hit both cases below on a Gamma 601 with a failing I2C bus (a dead display module on the bus). The code paths are unchanged in current `master`.

**Case 1: EMC2101 diode fault read as 127 °C**
With an open-circuit external diode, the EMC2101 returns its fault code `0x3F8`, which `/ 8.0` turns into exactly 127.0 °C. `EMC2101_get_external_temp()` detects it (`EMC2101_TEMP_FAULT_OPEN_CIRCUIT`), logs it, and then converts it and returns it anyway. The overheat trip took the miner from 575 MHz / 1150 mV to 475 / 1050 while the chip was really at ~48 °C, and left the fan in manual mode.

**Case 2: TPS546 garbage word latched as the "last good" value**
```
OVERHEAT! VR: 16384.000000C ASIC: 64.250000C
```
This came seconds after `I2C bus is still busy but software timeout detected`. 16384 is 2^14, a garbage PMBus word that `slinear11_2_int()` decoded as a temperature. `smb_read_word()` returned `ESP_OK`, so `TPS546_get_temperature()` stored it in `last_temp` (TPS546.c ~866–872), and every later failed read returned 16384 again. Result:
- Repeated trips, each persisting a lower operating point: 625 → 500 → 400 MHz.
- The cooling loop (`while (… || vr_temp > TPS546_THROTTLE_TEMP - 10)`) re-reads that cached 16384 as long as the bus keeps failing, so it never exits. The miner sat there not mining with the fan at 100 % and needed a power cycle, twice.

The same bus produced other impossible values as well: power −6723579 W, and a VR temperature of −2228224 °C (raw `0x7fbc`, a formally valid SLINEAR11 decode).

**Suggested fixes (fork implementation available)**
- **TPS546 getters:** check the decoded value against a physically possible range before caching it, and treat an out-of-range value like an I2C error. The range must come from the board config, e.g. Vout from `tps546_config` rather than a fixed 0–3 V, which would reject real Hex readings.
- **EMC2101/EMC2103:** don't return a diode fault code as a temperature. Returning -1, as the I2C error paths already do, stops the false trip, but a *permanent* diode fault then leaves the ASIC-temperature trip blind: the VR temperature and the TPS546's own hardware OT still protect. It may be better to treat a persistent diode fault as a hardware fault (stop mining with a message) than as 127 °C. That's a maintainer call.
- **Overheat trigger / cooling loop:** only act on plausible values. Possibly require two consecutive readings before persisting anything to NVS.

We've run the first two on four Gamma 601s since August. Afterwards the plausibility filter caught 13 corrupt readings in one night on the affected board and zero on the three healthy ones. I can open PRs for whichever parts you want.
