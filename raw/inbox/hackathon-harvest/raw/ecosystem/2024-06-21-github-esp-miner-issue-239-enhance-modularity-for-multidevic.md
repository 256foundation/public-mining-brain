# bitaxeorg/ESP-Miner issue #239: Enhance Modularity for Multidevice Support

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/239
> Collected: 2026-10-07
> Published: 2024-06-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 239
- State: closed
- Author: tdb3
- Opened: 2024-06-21
- Closed: 2026-05-29
- Labels: enhancement, help wanted

## Description

Currently, ESP-Miner is very focused on Bitaxe hardware.  It would be great to implement a set of refactors to ease the integration of other hardware (e.g. non-Bitaxe, Bitaxe-custom hardware, etc.).  This could also have the added benefit of scoping functionality in a way that bugs for one type of board are less likely to impact other types (i.e. more scalable support).

These comments are from an OSMU Discord user:
```
Since clearly the direction this is heading is "centralized" bitaxe-ONLY multi-board support, how does custom boards gets included in the firmware?
Do we need to put up our ADC and other gizmos' libraries and contribute conditional code to the master branch?
```

**Wanted to open this as an Issue first to garner discussion before submitting PRs on this.**  I'm thinking something along the lines of:
 - Implement hardware abstraction through well-defined interfaces (e.g. C++ style classes that provide interface methods to purposefully abstract hardware specifics)
 - Enable developers of other hardware to implement these interfaces for the specific hardware they would like supported
 - Restructure directories to facilitate the integration of other hardware devices while minimizing the changing of existing/adjacent files



Here's a simple example discussing displays:
Currently, the i2c SSD1306 OLED display is supported, and calls in system.c use it.
https://github.com/skot/ESP-Miner/blob/08b7ad54092c59ba17b88ed4d64a4eac363ebe36/main/system.c#L129-L140
This could be abstracted out to support other displays in general, providing a few simplified well-defined interface methods.  For example:

![image](https://github.com/skot/ESP-Miner/assets/106488469/0223808d-7013-4f6e-9e11-71265e70c5fa)

This is just a straightforward application of object-oriented approaches (e.g. inheritance/polymorphism).

system.c could be made agnostic of specific display type (i.e. just call the interface methods on a Display* that is pointing to an SSD1306Display object, which is required to implement or inherit Display's interface).  Someone comes along and decides to implement support for a cool eInk display.  No problem, create a new child class eInkABC123Display.

More complicated examples would include things like:
 - An abstraction for NVS
 - A "Board" or "Miner" base class and child classes that initialize and manage specifics of the board/hardware being used, rather than have switch statements on board type throughout the code.
 - Factory pattern implementation for instantiating the appropriate "Board" (e.g. from NVS data on startup)

We could roll this out gradually in pieces over multiple PRs.

Some areas of interest:
- [ ] display interface: In work
- [ ] non-volatile storage interface
- [ ] hash device interface (i.e. ASIC, to make it easier to support different ASIC chips and maybe one day Block's new ASIC)
- [ ] user input interface
- [ ] network interface (for WiFi at first, but lay groundwork for potentially other network types, e.g. Ethernet, LoRa, etc.)

## Comments

### tdb3 on 2024-06-21

We could modularize everything, but we should figure out where to draw the line based on what's reasonable.  The repo is named "ESP-Miner".  I'm going to assume that for now we want to have the base assumption that we're supporting the ESP32 family of microcontrollers (although currently we're just S3?).

Longer term (over years and beyond), it would be cool to have open source mining software runnable on a plethora of devices.  Do this right and we can be the "Linux" of open source mining devices.  Base software that enables a diverse world of open source mining devices, and enables products to come to market faster/easier/cheaper (distributing/decentralizing hashrate).  One day my heated blanket will keep me warm while mining sats (kidding about this part).

### skot on 2024-06-22

I am 100% into this. We are getting outside the "let's just see if this will work" stage and rapidly approaching an unmanageable number of variants, on the Bitaxe alone.

Supporting other Bitcoin mining projects is how we win.

### tdb3 on 2024-06-30

Working a draft PR for a display interface as time permits. It would be a good well contained first step.

Afterward, a board class, or similar, can use an instantiated Display. Different boards can use different Displays by instantiating the appropriate object.

### 3x3y3z3t on 2024-06-30

> More complicated examples would include things like:
> 
> * An abstraction for NVS
> * A "Board" or "Miner" base class and child classes that initialize and manage specifics of the board/hardware being used, rather than have switch statements on board type throughout the code.
> * Factory pattern implementation for instantiating the appropriate "Board" (e.g. from NVS data on startup)

I am in the process of making a C++ port for the firmware (it's more like a rewritten than a port), and is designing it to support these abstraction.

### My design is:
- A `Bitaxe` base (abstract) class. It holds reference to these objects:
  - `PowerManager`: (abstract) class that manage board power, chip power.
  - `ThermalManager`: (abstract) class that manage board temp, chip temp and fan control.
  - `ASICChain`: (abstract) class that manage the ASICs chain's job

These base classes deal with all the low level stuff.

Developer will create derive classes from these base classes for each version of the Bitaxe. For example, `Bitaxe_Ultra : public Bitaxe`, `ASICChain_BM1366 : public ASICChain`. They shouldn't care about hardware programming, just call the base class's method.

### Things I have implemented (and working) so far:
- NVS abstraction with handle auto-cleanup.
- `NVSConfig` object that holds all config so we don't have to read from NVS every 2 seconds.
- I2C abstraction.
- `I2CDevice` base class and derive classes for any component that use the I2C interface (e.g `OLED : public I2CDevice`, `INA260 : public I2CDevice`).

I want to make a PR and ask for review, but they are written in C++ so will not build (for now). Other than the C++ thingy they are completely compatible with the current code base.

### tdb3 on 2024-06-30

> I am in the process of making a C++ port for the firmware (it's more like a rewritten than a port), and is designing it to support these abstraction.
> 
>...
> 
> I want to make a PR and ask for review, but they are written in C++ so will not build (for now). Other than the C++ thingy they are completely compatible with the current code base.

That all sounds excellent!
Do you have a fork/branch available? If not, either of us could create one and maybe we can team up? I would like to avoid duplicating effort, and it sounds like we're thinking on the same page in terms of design.
So far I have a work-in-progress BaseDisplay class that defines an interface for a display, and an SSD1306Display child class that implements the interface to handle the internals of commanding the OLED display. I haven't finished tidying up and porting all the command communication yet, but some parts are in place.

Also happy to jump on a design call in Discord. Whatever makes the most sense.

### 3x3y3z3t on 2024-07-01

I have just pushed the branch to my fork, you can get it here: https://github.com/3x3y3z3t/ESP-Miner/tree/cpp-support
(I have been working locally so the branch didn't get pushed earlier).

I have collected the known working parts, which are:
- `system/nvs.h` `system/nvs.cpp`: interface to access NVS, this class deal with esp32 stuff.
- `system/i2c.h` `system/i2c.cpp`: interface to access I2C, this class deal with esp32 stuff.
- `system/i2c_device.h`: base class for a component that use I2C (I call it an "I2C Device").
- `nvs_config_cpp.h` `nvs_config_cpp.cpp`: an object to hold all config stored in NVS. Bitaxe application will read from and write to this object instead of from/to NVS.
- `components/oled.h` `components/oled.cpp`: SSD1306 oled display implementation which derives from `I2CDevice`. Currently it works with 128x32 and 128x64 variant.

You can pull out those parts and strap to a blank esp-idf project to confirm.

If you prefer I think we can open a thread on #firmware on Discord to discuss more about this, I would also like to team up. My username is `Arime-chan` (or `3x3y3z3t`)


### tdb3 on 2024-11-16

Jotted down some initial thoughts on a refactor.  Nothing formal so far, just thinking out loud. Needs to be refined, but it can at least start conversation.  The interfaces need further refinement. I have a local branch where I've implemented some conceptual classes (e.g. `NVStorage/ESP32NVStorage`, `Miner/BitaxeSupraMiner`) and implemented proof-of-concept for the compile-time device selection and unit test approaches.

https://github.com/tdb3/notes/blob/main/esp_miner/esp-miner_refactor_thoughts.md

### adammwest on 2025-02-08

I believe https://github.com/shufps/ESP-Miner-NerdQAxePlus/tree/develop/main a version of esp exists with c++ already maybe some parts can be utilized 

### WantClue on 2026-05-29

I think we have achieved a higher modularity over time now and esp-miner can be easily adapted to different hardwares already. If this still needs more ping again so we open this issue again for discussion
