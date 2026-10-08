# bitaxeorg/ESP-Miner issue #16: Configs not written to NVS during compilation using ESP-IDF 5.1

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/16
> Collected: 2026-10-07
> Published: 2023-08-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 16
- State: closed
- Author: developeralgo8888
- Opened: 2023-08-20
- Closed: 2023-09-10
- Labels: none

## Description

Note about esp-miner master repo with ESP-IDF Version 5.1:

Run the following on a fresh bitaxe v2.2 to test esp-miner Repo V5.1 

```
(1)  idf.py set-target esp32s3
(2)  idf.py menuconfig  and also 
(3)  updated the config.cvs with same configs as menuconfig (except for Freq & Vcore)
(3)  idf.py -p PORT erase-flash
(4)  idf.py -p PORT flash monitor
```


Noticed that: Stratum configurations are not written to NVS . i did have to run the bitaxetool to write stratum config to NVS

Without running bitaxetool to write the configs to NVS the miner does not seem to connect imeediately or sometimes not at all. 


`(5)  bitaxetool --port PORT --firmware esp-miner.bin --config config.cvs`


[message.txt](https://github.com/skot/ESP-Miner/files/12387968/message.txt)


## Comments

### johnny9 on 2023-08-24

No configs are written to the NVS unless you use the bitaxetool. If you are compiling it yourself, you use menuconfig to configure the compiletime definitions that will be used to connect to your stratum server.
