# bitaxeorg/ESP-Miner issue #1002: Unified firmware update

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1002
> Collected: 2026-10-07
> Published: 2025-06-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1002
- State: closed
- Author: mutatrum
- Opened: 2025-06-04
- Closed: 2025-11-29
- Labels: duplicate

## Description

Currently having a 2-stage firmware update is error prone and confusing. Secondary goal is to step away from the strict filenames. There are a few options to do this:

1. Merge `esp-miner.bin` and `www.bin` into a single binary file. This is a custom format, and needs some sort of simple header + size. One thing we could add into this header is a device marker, so we can do a validity check on that instead of the filename to prevent people of flashing the wrong firmware;

2. Have a zip file with both files. Same idea here, and it's trivial to add simple manifest file for device validity check;

3. Get rid of `www.bin` and have the AxeOS files embedded into `esp-miner.bin`. I haven't looked at this in detail, but it's worth exploring this as well, as this makes the upgrade path way simpler. We can just forget about the spiffs partition when this is loaded onto the device. Somehow all the files need to be embedded into `esp-miner.bin`, and I'm not sure it that'll fit.

The first two need a clear upgrade/downgrade path, and we need to supply both variants for a while, possibly adding to the confusion.

## Comments

### skot on 2025-06-04

Having a unified firmware update image would be so helpful. I suspect a lot of update errors/confusion are caused by having to update two separate images.

My Search skills are failing me right now, But I know others have looked into this previously, like @tdb3 and @benjamin-wilson. IIRC the main issue is that a combined image is too big to fit into the Factory App partition (and corresponding OTA partition).

We should be able to change the default partition size though. Can we make it big enough for a combined image?

### ghost on 2025-06-04

#910 should cover it for now with ref to people not updating with both files that was included in v2.8.0.

### mutatrum on 2025-06-11

Previous issue with similar ideas and some technical exploration: #308 

### sz4bi on 2025-06-27

I vote for Option 2, it is the easiest to implement and require no modifications in the system.

### duckaxe on 2025-08-08

Related https://github.com/bitaxeorg/ESP-Miner/discussions/1179

### WantClue on 2025-11-29

Community agreement atm is to keep it in for potential alternative WebUI like AxeWellUi
