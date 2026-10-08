# bitaxeorg/ESP-Miner issue #1382: v2.11: Invalid VCORE config in NVS causes SYSTEM_init_peripherals failure and effectively soft-bricks device

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1382
> Collected: 2026-10-07
> Published: 2025-11-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1382
- State: closed
- Author: dario-spagnolo
- Opened: 2025-11-24
- Closed: 2025-11-29
- Labels: none

## Description

After upgrading a Bitaxe Gamma 601 from **v2.10.x** to **v2.11.0**, an existing config with **VCORE = 0.900 V** causes the miner to fail during peripheral init and never reach a usable state (no UI, no hashing). The same hardware and config works on **v2.10.x**.

This looks like an unintended side effect of the new behavior in v2.11 where `SYSTEM_init_peripherals()` failure is treated as fatal in `app_main()`.

### Environment

* **Board:** Bitaxe Gamma 601
* **Firmware:**

  * Previously OK on 2.10.x
  * Problem appears after upgrade to 2.11.0
* **Config:** ASIC VCORE set to **0.900 V** (saved in NVS from earlier firmware)

---

### Symptoms

On v2.11.0, the serial log shows:

```text
I (...) vcore: Set ASIC voltage = 0.900V
E (...) TPS546: Voltage requested (0.900000 V) is out of range
E (...) vcore: VCORE_set_voltage(...): TPS546 set voltage failed!
E (...) system: SYSTEM_init_peripherals(...): VCORE set voltage failed!
E (...) bitaxe: Failed to init peripherals
```

After this:

* The device does **not** bring up AxeOS (no screen UI / web UI).
* It appears “dead” or stuck, and there is no way to correct the bad VCORE via the normal interface.

Downgrading to **2.10.x** on the same hardware with the same stored config **does** boot to a usable state again.

---

### Likely cause in 2.11

In 2.11, two changes seem relevant:

1. Extended TPS546 detection / startup failure handling.
2. `app_main()` now explicitly checks the return value of `SYSTEM_init_peripherals()` and logs `"Failed to init peripherals"` then returns if it is not `ESP_OK`.

This means a previously “just bad but survivable” VCORE config (e.g. 0.900 V) now causes the whole app to abort at startup, leaving the user with no way to fix the config without low-level intervention.

---

### Expected vs actual

**Expected:**

* If VCORE in NVS is out of range for the board:

  * Either clamp it to a safe default and continue, or
  * Boot in a “safe mode” where hashing is disabled but the UI/API is available so the user can correct settings.

**Actual in 2.11.0:**

* Out-of-range VCORE causes `VCORE_set_voltage` → `SYSTEM_init_peripherals` to fail.
* `app_main()` treats this as fatal and exits early.
* Device never reaches a usable UI/API state; from a user’s perspective it looks soft-bricked after the upgrade.

---

### Suggestions

A few possible mitigations:

1. **Clamp VCORE on load:**
   When reading VCORE from NVS, clamp values outside the board’s allowed range to `[MIN, MAX]` and log a warning instead of failing init.

2. **Safe-mode fallback on init failure:**
   If `SYSTEM_init_peripherals()` fails due to VCORE/TPS546 issues, reset VCORE to a default and retry once, or boot a minimal mode with ASIC disabled but UI/API available.

3. **Validate VCORE on write:**
   Reject out-of-range VCORE values in the UI/API/config writer instead of allowing them to be stored and only failing at next boot.

---

* Is this fatal-on-`SYSTEM_init_peripherals` behavior in 2.11 intended even for purely config-driven issues like invalid VCORE?
* Would it be acceptable to provide a safe-mode path so that an out-of-range user setting cannot render the device effectively unusable after an upgrade?

## Comments

### AJ406ecom on 2025-11-24

face it .. v2.11 screwed us all 

### mutatrum on 2025-11-24

> face it .. v2.11 screwed us all

Yeah, some people indeed have some annoying issues with v2.11. This happens, we only have limited testing capability and with so many different manufacturers, models, power bricks, fans, etc., it's impossible to catch everything. We can always use more testers, occasionally picking up a test release or having a go at current development version would be very welcome! You're also very welcome on the Discord if you're not already there, if you want to be closer in the development loop. There should be a link somewhere on the front page or the wiki.

### mutatrum on 2025-11-24

Change was #1320. I'm trying to think what the rationale was on this change, but I struggle to remember. I think it was deemed a code quality improvement, but didn't consider the case where it fails to startup. 

If I now look at the code of `SYSTEM_init_peripherals`, it exits on every error, so depending on what goes wrong, only a part of the peripherals are initialized, hence the idea that it's a fatal error. So if the VCORE value is invalid, the temp sensor, display and buttons are not initialised, but it will continue to boot.

Ideally, it should try to at least initialism all peripherals, and if that works, set the VCORE (and maybe other configurations). Secondary, if VCORE (and maybe other NVS configuration values) are out of spec, they should be clamped to valid values.

### mutatrum on 2025-11-24

What I don't understand is how you can end up with 0.9V as VCORE, as `TPS546_set_vout` hasn't changed AFAIK, or at least not recently (~8 months).

There might be a side-issue, where the NVS config for VCORE should only be saved if it has been successfully set by the TPS546.

### dario-spagnolo on 2025-11-25

Thank you for taking the time to look into this.

VCORE at 0.9V was set via the API (/patch endpoint if I remember correctly). It was accepted by the Bitaxe and it was hashing fine for a few hours before I did the firmware upgrade.
