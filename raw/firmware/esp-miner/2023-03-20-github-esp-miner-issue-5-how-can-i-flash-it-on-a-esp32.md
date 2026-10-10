# bitaxeorg/ESP-Miner issue #5: How can I flash it on a esp32

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/5
> Collected: 2026-10-07
> Published: 2023-03-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 5
- State: closed
- Author: a-1500
- Opened: 2023-03-20
- Closed: 2023-05-25
- Labels: none

## Description

How can I flash it on a esp32, I have no idea how, please explain 

## Comments

### skot on 2023-03-20

The ESP32-S3 on the bitaxe is [flashed just like any other ESP32](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/get-started/index.html) kit or dev board out there. 

Just be aware you'll need to use a [ESP-Prog](https://espressif-docs.readthedocs-hosted.com/projects/espressif-esp-iot-solution/en/latest/hw-reference/ESP-Prog_guide.html) and a [Tag Connect cable](https://www.tag-connect.com/product/tc2030-idc-nl), as there is no USB port on the bitaxe.

### a-1500 on 2023-03-20

I meant how can I flash the esp-miner

### skot on 2023-03-20

Sorry, I'm not sure what you are asking.

### a-1500 on 2023-03-20

> Sorry, I'm not sure what you are asking.

Can I flash the firmware ESP-miner on the esp32 on the bimax bord to be able to mine

### skot on 2023-03-20

This firmware needs _alot_ more work before it will mine. You can see the latest if you checkout the `i2c_test` branch.

### a-1500 on 2023-03-20

> This firmware needs _alot_ more work before it will mine. You can see the latest if you checkout the `i2c_test` branch.

Ok, and I'm very excited for the firmware to be completed
