# bitaxeorg/bitaxe-raw issue #11: Error Failed to format as esp-idf binary

> Source: https://github.com/bitaxeorg/bitaxe-raw/issues/11
> Collected: 2026-10-07
> Published: 2026-04-02

- Repository: bitaxeorg/bitaxe-raw
- Type: issue
- Number: 11
- State: closed
- Author: dhmyess
- Opened: 2026-04-02
- Closed: 2026-08-24
- Labels: none

## Description


I have followed the instructions but when I flash it an error appears

cargo flash --release --chip esp32s3
    Finished `release` profile [optimized + debuginfo] target(s) in 0.15s
    Flashing /home/dharma/miner/bitaxe/bitaxe-raw/target/xtensa-esp32s3-none-elf/release/bitaxe-raw
       Error Failed to format as esp-idf binary
            
            Caused by:
                ESP-IDF App Descriptor (https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/system/app_image_format.html#application-description) missing in your`esp-idf` application.

I don't know what to do next to resolve this error.
