# bitaxeorg/ESP-Miner issue #43: Not Mining

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/43
> Collected: 2026-10-07
> Published: 2023-10-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 43
- State: closed
- Author: laststrawman
- Opened: 2023-10-16
- Closed: 2023-10-19
- Labels: none

## Description

I am connected to my WiFi but I don't seem to be mining. How do I debug? I am using a Bitaxe board purchased from D-Central. I am trying to connect to public-pool.io 
Also, my led displays ASIC model invalid so I am wondering if there is something wrong with my build config.

## Comments

### laststrawman on 2023-10-17

Ok ... update. I flashed the BM1397 following this link: https://github.com/skot/ESP-Miner/releases/tag/v2.0.0
I now can see it talking to public-pool.io but I am still not mining. I definitely have the BM1397 2.2 chip so I set the config.cvs to those settings. 

### geg780 on 2023-10-17

Do you have a proper power supply? At least 4a are needed.

### laststrawman on 2023-10-17

![image](https://github.com/skot/ESP-Miner/assets/29166705/cb99da19-58d1-4616-9d84-8b7fa703308a)


### laststrawman on 2023-10-17

I have seen my miner on public-pool.io
![image](https://github.com/skot/ESP-Miner/assets/29166705/60cff2bd-0600-4e7e-9433-e6335b4299ac)


### laststrawman on 2023-10-17

I think you are right ... I looked at my power supply and it has an output of 5v = 1A

### geg780 on 2023-10-17

Yeah thats the issue

### laststrawman on 2023-10-19

I am fixed ... it was the power supply.
