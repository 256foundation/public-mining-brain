# bitaxeorg/ESP-Miner issue #564: Overheat Mode Extra Safeguard to Prevent Hardware Damage

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/564
> Collected: 2026-10-07
> Published: 2024-12-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 564
- State: closed
- Author: ACSBEN
- Opened: 2024-12-07
- Closed: 2026-06-02
- Labels: enhancement, good first issue

## Description

**Describe the bug**
Overheat mode will still allow up to 10 watts of power, and allow the asic and stratum tasks to initialize. In the case of a full fan failure, this is enough to cause a Hardware degradation if left unsupervised for long enough.

**To Reproduce**
1. Enter Overheat Mode in your method of choice
2. In the ESP log, the Stratum activity and Asic Serial Activity still remiains
3. Testing the "RST" Test Point with a multimeter will show RST is still outputting 1.2v (1.8v on older models)

**Expected behavior**
A cleaner overheat mode would eliminate these functions, and Pull down RST to 0v, this causes the Asic to consume the least amount of power possible with VDD still active. (We don't have hardware Mosfets to completely Isolate VDD from the Asic)

**Screenshots & Photos**
![PXL_20241207_191330492~2](https://github.com/user-attachments/assets/e2e2310d-a2b9-4ed8-b6d7-c5bdd3245bc9)
⬆️ This photo is the power draw with the current Overheat Mode implementation

![PXL_20241207_191954642~2](https://github.com/user-attachments/assets/7d8e4ad0-e184-4c8a-ad62-89caef984256)
⬆️ This photo is with a tweaked version that pulls RST down correctly.

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601 (affects all Bitaxe Models)
 - Bitaxe HW vendor: Self-Built
 - ESP-Miner FW version: Custom FW based on 2.4.0

**Additional context**
For my testing, I added the following lines:

https://github.com/skot/ESP-Miner/blob/636480552373a2f86c2a68ad3c098b6eb1ecac16/main/main.c#L121
⬆️ This was changed to 
`if (GLOBAL_STATE.ASIC_functions.init_fn != NULL && !GLOBAL_STATE.SYSTEM_MODULE.overheat_mode)`
This locks out the Asic Init and Stratum Init Functions if overheat mode is active. 

Currently, the GPIO_NUM_1 (RST Pin) is tied to the Asic Initialization process, meaning that before this is call, it is always high. We probably don't want that, even if overheat mode is not active, as it causes the asic to consume twice as much power while we are initializing the rest of the system. 

To get around this, we need to initialize the GPIO Pin early in app_Main, as the asic initialization process already has a built in function to pull this back high when timing is correct.
```
gpio_set_direction(GPIO_NUM_1, GPIO_MODE_OUTPUT);
gpio_set_level(GPIO_NUM_1, 0);
```


## Comments

### benjsc on 2025-11-21

Looks like this has been implemented in https://github.com/bitaxeorg/ESP-Miner/pull/1304
Which was released in [v2.11.0](https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.11.0)
