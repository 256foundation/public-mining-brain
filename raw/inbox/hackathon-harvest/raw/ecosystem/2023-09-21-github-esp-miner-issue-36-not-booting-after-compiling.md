# bitaxeorg/ESP-Miner issue #36: Not booting after compiling

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/36
> Collected: 2026-10-07
> Published: 2023-09-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 36
- State: closed
- Author: ed0nkey
- Opened: 2023-09-21
- Closed: 2023-09-24
- Labels: none

## Description

I've did everything that the guide said and even tried via vscode too, but after flashing using the latest project files it fails to boot. I don't have the slightest idea how this work but using the 1.0 release it boots fine.
![Code_7gGqBrOjvj](https://github.com/skot/ESP-Miner/assets/79872165/f9013501-2381-4ca8-9ffb-c247ddba5057)


## Comments

### johnny9 on 2023-09-21

It looks like it didn't flash the image correctly. Just the bootloader and partition table is there.

### ed0nkey on 2023-09-22

It is very strange because I saw everything being flashed correctly after compiling and I really don't know what could be causing this issue. Other branches like i2c_test flashes and boot just fine.

### ed0nkey on 2023-09-22

I've now tried the code from [this commit](https://github.com/skot/ESP-Miner/tree/66c4b2bb5736b32254846bbba4f32632de7a4ea8) and I get a different result but still it still doesn't want to boot. If it is useful info, I'm using the esp32-s3-wroom-1 and the esp-prog.

[crash.txt](https://github.com/skot/ESP-Miner/files/12699767/crash.txt)


### ed0nkey on 2023-09-22

I may have gotten the 4MB flash esp32 instead of a larger one, is that the issue right? :^)
If so which size should I get?

### johnny9 on 2023-09-24

The Bitaxe requires the 16N8R (16MB of flash 8MB of PSRAM) version of the wroom. Check the BOM on the Bitaxe repo for the exact one on DigiKey.

### johnny9 on 2023-09-24

Yes, the error in your logfile indicates you have too small of flash to use the normal Bitaxe firmware. You may, however, modify the configuration of the project to not use the ota paritions and instead just have factory and spiffs data. Refer to https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-guides/partition-tables.html for how to modify the parition table and use menuconfig to set the flash down to 4MB.

If you would like to discus further, I'd be happy to answer questions in our discord (https://discord.com/invite/pF9smpe3yE)
