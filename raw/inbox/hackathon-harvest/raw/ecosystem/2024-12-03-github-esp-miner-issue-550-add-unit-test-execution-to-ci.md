# bitaxeorg/ESP-Miner issue #550: Add unit test execution to CI

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/550
> Collected: 2026-10-07
> Published: 2024-12-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 550
- State: closed
- Author: tdb3
- Opened: 2024-12-03
- Closed: 2026-05-29
- Labels: none

## Description

Could be beneficial to add unit tests to CI, to prevent regressions from going unnoticed.

Wish list item for now.

There are probably a few ways to do this (e.g. abstracting hardware with mocks, having a self-hosted runner with physical esp32 devices attached, etc.).

https://docs.espressif.com/projects/esp-idf/en/v5.3.1/esp32/api-guides/unit-tests.html

## Comments

### eandersson on 2024-12-03

You can run tests using QEMU, there is even a Github Action that handles it for you, but it isn't maintained and only supports ESP-IDF 4.x.

It might be this one.
https://github.com/Batov/esp32_qemu_unity_test_action

### eandersson on 2024-12-06

Spent some time trying to get it to work, but kept running into crashes.
https://github.com/eandersson/ESP-Miner/actions/runs/12205882369/job/34057802320#step:6:55

### eandersson on 2025-01-07

I figured out the crash. QEMU does not support hardware accelerated SHA (CONFIG_MBEDTLS_HARDWARE_SHA) so that feature needs to be disabled, but that leads issues as the software implementation is slightly different.
https://github.com/eandersson/ESP-Miner/commit/43b5b4bb7eb163dbe8ef62bfd7e04d21a2b1f993#diff-382cd75d2d2b14dad2fd5104843e642afda81185c5c88a5870b64a5e7a6ffe91R22

https://github.com/skot/ESP-Miner/pull/627

### tdb3 on 2025-01-08

Nice. Since no test is perfect, I think it seems reasonable to have layers of testing, each with their own advantages and limitations (and we clearly state those limitations). For example, the QEMU based CI for unit test execution might have to run mostly the same (but not identical) software, but still enables finding some types of bugs.

I also don't think it would be too crazy to use real ESP32s dev boards (maybe a separate CI/test). They are cheap enough, and could enable testing code that we might not be able to test well with QEMU. It has a tiny bit of a Rube Goldberg machine vibe, but would be just one layer of testing.

### WantClue on 2026-05-29

QEMU and frontend CI tests are in current master. Thanks
