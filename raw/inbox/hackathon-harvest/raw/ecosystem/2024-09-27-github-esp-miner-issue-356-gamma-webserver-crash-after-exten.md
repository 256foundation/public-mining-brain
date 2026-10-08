# bitaxeorg/ESP-Miner issue #356: Gamma: Webserver crash after extensive API calls

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/356
> Collected: 2026-10-07
> Published: 2024-09-27

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 356
- State: closed
- Author: jrkalf
- Opened: 2024-09-27
- Closed: 2024-10-07
- Labels: none

## Description

I use home assistant with a restful sensor to query the api/system/info to obtain statistics. After doing several requests, I’ve not measured the exact number, the webservice becomes unavailable. The unit does remain online and mining (according to the pool stats), but the webservice and api are unreachable.

**To Reproduce**
Steps to reproduce the behavior:
1. start machine as usual
2. Do extensive API polling on api/system/info
3. Experience webservice to be unresponsibe
4. See error

**Hardware (please complete the following information):**
 - **Bitaxe HW version:** Gamma 601
 - **Bitaxe HW vendor:** TinyChipHub
 - **ESP-Miner FW version:** 2.2.2
 - **Hash Frequency:** 596
 - **Voltage:** 1150
 - **Pool URL, Port, User:** pool.satoshiradio.nl

**Additional context**
HomeAssistant polling method:
```
- platform: rest
    unit_of_measurement: Gh/s
    resource: !secret bitaxe_ip
    method: GET
    value_template: '{{ value_json.hashRate }}'
    name: Bitaxe hashrate
    scan_interval: 15
    
  - platform: rest
    unit_of_measurement: °C
    resource: !secret bitaxe_ip
    method: GET
    name: Bitaxe temp
    value_template: '{{ value_json.temp }}'
    scan_interval: 60
    
  - platform: rest
    unit_of_measurement: sec
    resource: !secret bitaxe_ip
    method: GET
    name: Bitaxe up-time
    value_template: '{{ value_json.uptimeSeconds }}'
    scan_interval: 60
```

and `bitaxe_ip` in the secrets.yaml points to `http://ip-address/api/system/info`

## Comments

### skot on 2024-09-27

Can you monitor the free heap memory on the Bitaxe while you do this? It's available in the Overview section on the AxeOS Logs tab.

I'm curious if we're leaking memory somewhere.

### jrkalf on 2024-10-01

@skot I've not been able to reproduce since I've replaced the stock cooling brick and fan with alternatives that make the BitAxe run a lot cooler. Perhaps my experience relates to #369 that the whole device is less stable when running hot?

### jrkalf on 2024-10-07

Closing this one as not-reproduceable.
