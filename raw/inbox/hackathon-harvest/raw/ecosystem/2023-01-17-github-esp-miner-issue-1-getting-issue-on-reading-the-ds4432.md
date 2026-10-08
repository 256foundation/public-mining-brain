# bitaxeorg/ESP-Miner issue #1: getting issue on reading the DS4432U

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1
> Collected: 2026-10-07
> Published: 2023-01-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1
- State: closed
- Author: developeralgo8888
- Opened: 2023-01-17
- Closed: 2023-01-18
- Labels: none

## Description

```
I (1947) wifi station: connected to ap SSID:ABHomie
I (1957) i2c-test: Init LEDs!
I (1957) i2c-test: I2C initialized successfully
ESP_ERROR_CHECK failed: esp_err_t 0x107 (ESP_ERR_TIMEOUT) at 0x42008e62
0x42008e62: DS4432U_read at /developer/Downloads/ESP-Miner-i2c_test/build/../main/DS4432U.c:75 (discriminator 1)

file: "../main/DS4432U.c" line 75
func: DS4432U_read
expression: register_read(DS4432U_SENSOR_ADDR, DS4432U_OUT1_REG, data, 1)

abort() was called at PC 0x4037de33 on core 0
0x4037de33: _esp_error_check_failed at /developer/.espressif/esp-idf-ae062fbba3ded0aa/v5.0/components/esp_system/esp_err.c:47
```

## Comments

### skot on 2023-01-17

I think that is ESP-IDF's lovely way of saying no response from the I2C address `DS4432U_SENSOR_ADDR`.

What do you have `DS4432U_SENSOR_ADDR` set to? Is it `0x48` ?
Can you confirm the DS4432U+ has power and your I2C lines SDA and SCL are connected properly? You should get a 0x00 response.

### developeralgo8888 on 2023-01-17

I think my DS4432U_SENSOR_ADDR is set to 0x48 but let me confirm . It's 0x48 on the DS4432U.c file  but the Datasheet says that the slave (hex  7-bit addressing) address is  90h = 0x90 , Memory F8h = 0xF8 and  F9h = 0xF9. I have tried both 0x90 and 0x48 for the slave address and do not seem to get a response, Checked the power and connection and i am getting 3.3V into the DS4432U , SDA & SCL are connected fine no shorts

### developeralgo8888 on 2023-01-18

issue solved
