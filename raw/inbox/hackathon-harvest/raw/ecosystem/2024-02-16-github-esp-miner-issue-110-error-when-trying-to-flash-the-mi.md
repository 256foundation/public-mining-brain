# bitaxeorg/ESP-Miner issue #110: Error when trying to flash the miner

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/110
> Collected: 2026-10-07
> Published: 2024-02-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 110
- State: closed
- Author: pinokio240
- Opened: 2024-02-16
- Closed: 2024-02-16
- Labels: none

## Description

Error when trying to flash the miner
![error](https://github.com/skot/ESP-Miner/assets/37944152/042880d8-77a4-41ac-b927-53ff13dd7797)
![ver_win](https://github.com/skot/ESP-Miner/assets/37944152/29bcbc9f-33f7-4836-bdd5-376b1d1e621f)
If you flash the file esp-miner-factory-v2.0.4.bin without config.cvs using Espressif. The miner starts but cannot be configured. How to flash NVS partition using Espressif? 
Should I remove 3.12?
Miner: JDHX bit lottery bm1397 v.3.8   z
P.S.
Figured it out:
1) Removed Python 3.12
2) Cleaned the registry
3) Installed Python 3.4
4) Installed esptool using the commands pip install esptool and pip install esptool --upgrade
For firmware I used ESP-prog

## Comments

### skot on 2024-02-16

you can flash just the config.cvs using bitaxetool. `bitaxetool --config ./config.cvs`

glad you got it figured out!

### johnny9 on 2024-02-17

I removed distutils from bitaxetool. bitaxetool version 0.6 should work with 3.12 on Windows now.

### pinokio240 on 2024-02-17

Now the problem is like in https://github.com/skot/ESP-Miner/issues/100. Doesn't measure power correctly and restarts. I tried different firmwares - it didn’t help. 
In older versions, there is either an error in the calculation or the same problem with the power supply; if you measure it with a tester, the power supply is normal

### pinokio240 on 2024-02-17

> you can flash just the config.cvs using bitaxetool. `bitaxetool --config ./config.cvs`
> 
> glad you got it figured out!

OK
