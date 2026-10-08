# bitaxeorg/ESP-Miner issue #2019: BM1370 (Gamma 601): v2.15.2+ leaves 1–2 hash domains at 0 GH/s on every boot; v2.15.1 is fine

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/2019
> Collected: 2026-10-07
> Published: 2026-10-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 2019
- State: open
- Author: EichelJoe
- Opened: 2026-10-07
- Closed: n/a
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
After updating a Gamma 601 from v2.14.1 to v2.15.3, the miner hashes at about half of `expectedHashrate`. `hashrateMonitor` shows two of the four BM1370 hash domains at 0 GH/s. Which domains are silent changes between boots. The pool-side hashrate confirms the loss, so it is not only a reporting issue. `errorPercentage` stays at about 2–3 % because silent domains produce no error hashes (same observation as #2004).

A soft restart and a full power cycle (unplugged for several minutes) did not help. Flashing v2.15.1 to the other OTA slot fixed the extra silent domains with no other change. At stock frequency, all four domains are live and the hashrate matches `expectedHashrate`.

v2.15.2 changed the BM1370 init sequence in `components/asic/bm1370.c` (commit 3a09ea00, #1916). Diff v2.15.1 → v2.15.2:

- Core Register Control `0x3C` ClockDelayCtrl: `80 00 80 0C` → `80 00 80 10` (`BM1370_CLOCK_DELAY_CTRL_VALUE`), both broadcast and per-chip
- new broadcast write to `0x14`: `00 00 00 FF`
- Analog Mux Control `0x54` = `00 00 00 03` broadcast (previously commented out)
- new PLL3 `0x68` write: `5A A5 5A A5`
- `asic_init_core_register_delay()` added between writes

I have not bisected which of these causes it. The ClockDelayCtrl change is my first suspect.

**Measurements** (same unit, same PSU and pool; domains in GH/s, read about 2 min after boot unless noted)

```
FW       Freq / Vcore       Boot                        domains (GH/s)        hashRate / expected (GH/s)
-------  -----------------  --------------------------  --------------------  --------------------------
v2.15.3  690 MHz / 1150 mV  soft reset                  [408, 369, 0, 0]      ~710 / 1408 (pool: 590–655)
v2.15.3  690 MHz / 1150 mV  power-on, uptime 3 h        [0, 354, 0, 301]      ~700 / 1408 (pool: 645–750)
v2.15.3  690 MHz / 1150 mV  power-on                    [0, 331, 0, 361]      ~690 / 1408
v2.15.1  690 MHz / 1150 mV  after OTA                   [322, 378, 0, 367]    ~1010–1050 / 1408
v2.15.1  690 MHz / 1150 mV  soft restart                [288, 346, 0, 354]    ~1040 / 1408
v2.15.1  525 MHz / 1150 mV  soft restart                [253, 279, 253, 210]  ~1000–1080 / 1071
v2.15.1  525 MHz / 1150 mV  after 6 h 19 min            [294, 251, 292, 281]  1073 (1 h avg) / 1071, 691 shares, 0 rejected
v2.15.1  600 MHz / 1150 mV  soft restart, after 10 min  [337, 316, 271, 335]  1221 (10 min avg) / 1224, 0 rejected
```

On v2.15.1, domain 2 also drops out at 690 MHz. That looks like a separate overclock limit of this chip. On v2.15.3, other domains also fall silent at the same settings, and the set changes from boot to boot.

On v2.15.3 the serial log showed a normal init. `Chip 0 detected`, TPS546 OK (VIN 5.0 V, Vout 1.144 V), frequency ramp to 690 MHz OK, `ASIC initialized successfully with 1 chip(s) (cold boot mode)`, shares accepted. There were no warnings or errors. The domains simply never report hashes.

**To Reproduce**
1. Gamma 601 running fine on v2.14.1 / v2.15.1.
2. OTA update to v2.15.3 (also expected on v2.15.2, not tested separately).
3. Check `GET /api/system/info` → `hashrateMonitor.asics[0].domains`: one or more domains stay at 0, and `hashRate` is far below `expectedHashrate`.
4. OTA v2.15.1 (same settings) → domains come back.

**Expected behavior**
All four hash domains hash after init, as on v2.15.1. If a domain stays silent, the firmware should at least detect it (see #2004 / #2006).

**Screenshots & Photos**
n/a (API and serial log captures above)

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601 (BM1370, 1 chip)
 - Bitaxe HW vendor: bought second-hand (original vendor unknown)
 - ESP-Miner FW version: v2.15.3 (affected), v2.15.1 (OK)
 - Hash Frequency: 690 MHz (also tested 525 / 600 MHz on v2.15.1)
 - Voltage: 1150 mV (actual 1144 mV)
 - Pool URL, Port, User: public-pool.io:21496 (SV1)

**Additional context**
- Input 5.0–5.09 V, ASIC 46–57 °C, VR 60–91 °C, no overheat_mode, no throttling.
- Related: #2004 (single BM1370 domain stuck at 0 until restart). This report differs in two ways: a restart or power cycle does not fix it, and it goes away when downgrading to v2.15.1.
