# bitaxeorg/ESP-Miner issue #826: Make firmware releases for other PSRAM variants

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/826
> Collected: 2026-10-07
> Published: 2025-04-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 826
- State: open
- Author: mutatrum
- Opened: 2025-04-06
- Closed: n/a
- Labels: none

## Description

Unfortunately, the ESP32-S3 cannot auto-detect if the PSRAM on board is Quad or Octal. There have been 3 instances of people installing ESP's with different PSRAM settings on board, and they end up with a boot loop. They all succeeded in creating their own firmware, but it might be a small effort to have two subfolders in the build directory where images for these variants can be prepared. It would only have to be Quad and maybe for models without PSRAM. 

AFAIK there are no other ESP types that causes boot issues. There are also models with smaller flash size, but AFAIK these only trigger a warning in the logs, they don't cause a boot loop.

## Comments

### mutatrum on 2025-09-15

Tracking issue in ESP-IDF: https://github.com/espressif/esp-idf/issues/13343

### skot on 2025-09-15

Is this going to solve the issue? I'm not so sure, considering most people don't know they have a different ESP32S3 until they flash an update and it puts their bitaxe into a boot loop with the screen off. They prolly won't even know what the problem is at that point either, because they bought from a shady seller that didn't mentioned they subbed out parts.

It might be more beneficial for DIY builders to mention this in the docs, and provide instructions for a custom esp-miner build?

### mutatrum on 2025-09-15

AFAIK the cases we know of there was no support from the manufacturer. And it's easy to imagine people blaming the project if it's not working.

So, 4 options, in ascending order of pretty:

1. Do nothing;
2. Hope ESP fixes it on their end;
3. Placeholder PR (#1234) to trigger occasional builds;
4. Add it to the release pipeline as separate artefact (this original issue).

It should be added to the documentation in the first 3 cases.

### mutatrum on 2025-09-15

5. Make the firmware run without psram, as currently it continues booting if the wrong type is selected. With a few components disabled (bap and statistics) it's running without PSRAM. If memory is low, show a banner on the dashboard, hinting at this issue.

### sil-ver24 on 2026-09-17

I would like to add a real-world data point that may be relevant to this issue.

I have several early Bitaxe Gamma 601 units fitted with an ESP32-S3-WROOM-1 M0N16 module (16 MB flash, no PSRAM).

These units work correctly with ESP-Miner v2.9.0, but newer firmware versions can fail to boot. 
The serial log showed: Failed to init external RAM

This led us to verify that the ESP32 module installed on the board is an M0N16, therefore it has no PSRAM.

An interesting detail is that v2.9.0 is able to continue booting on these boards despite the absence of PSRAM, while newer firmware versions I tested do not appear to tolerate this hardware configuration.

During troubleshooting of one affected Gamma 601, I performed a complete flash erase and then flashed v2.9.0. After the erase, the board entered the factory self-test and stopped at the PSRAM test.

I was able to recover the board by copying the NVS partition from another known-good, otherwise identical Gamma 601 with an M0N16 module running v2.9.0.

The partition copied was:
NVS offset: 0x9000
Length: 0x6000

After restoring that NVS image, the board correctly identified itself as:
Gamma 601
BM1370
and the OLED, Wi-Fi and mining functionality all returned to normal.

So, based on what I observed, some early Gamma 601 boards appear to have been manufactured with ESP32-S3-WROOM-1 M0N16 modules without PSRAM, and v2.9.0 can still operate on them, whereas newer firmware can boot-loop during PSRAM initialization.

I hope this information may be useful for identifying early Gamma 601 hardware using no-PSRAM ESP32 modules, or for considering a firmware build/profile that can still support them.

For transparency: the troubleshooting was performed by me with technical assistance from ChatGPT  and this GitHub comment was drafted with AI assistance based on the troubleshooting results and logs I collected.

### mutatrum on 2026-09-17

That's more related to #1239. We're past the point that we can run ESP-Miner on just the internal ram of the ESP32S3. There have indeed been a few boards mistakenly produced with a no-PSRAM version of the ESP32S3 module, but unfortunately we cannot support these any longer, the firmware just needs more memory. It's cheap and reasonably doable to replace the module with a supported module.

This PR is specifically for supporting Quad PSRAM modules, but that's blocked by upstream support by Espressif.

### cezane822 on 2026-10-05

@sil-ver24 I had the same issue on my 601 ([https://github.com/bitaxeorg/legitlist/issues/58](https://github.com/bitaxeorg/legitlist/issues/58)). For what is worth.
