# 256foundation/asic-rs pull request #14: feature: add serialization for `MinerData`

> Source: https://github.com/256foundation/asic-rs/pull/14
> Collected: 2026-10-07
> Published: 2025-07-29

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 14
- State: closed
- Author: b-rowan
- Opened: 2025-07-29
- Closed: 2025-07-29
- Labels: none

## Description

Now serializing `MinerData` results in this JSON output - 
```JSON
{
   "schema_version":"0.1.0",
   "timestamp":1753763352,
   "ip":"192.168.86.21",
   "mac":"F0:F5:BD:4A:AA:1C",
   "device_info":{
      "make":"BitAxe",
      "model":{
         "Bitaxe":"Supra"
      },
      "hardware":{
         "chips":1,
         "fans":1,
         "boards":1
      },
      "firmware":"Stock",
      "algo":"SHA256"
   },
   "serial_number":null,
   "hostname":"bitaxe",
   "api_version":null,
   "firmware_version":"v2.4.5-3-gb5d1e36-dirty",
   "control_board_version":"401",
   "expected_hashboards":1,
   "hashboards":[
      {
         "position":0,
         "hashrate":{
            "value":574.3460573484966,
            "unit":"GigaHash",
            "algo":"SHA256"
         },
         "expected_hashrate":{
            "value":0.0,
            "unit":"GigaHash",
            "algo":"SHA256"
         },
         "board_temperature":0.0,
         "intake_temperature":0.0,
         "outlet_temperature":0.0,
         "expected_chips":1,
         "working_chips":1,
         "serial_number":null,
         "chips":[
            {
               "position":0,
               "hashrate":{
                  "value":574.3460573484966,
                  "unit":"GigaHash",
                  "algo":"SHA256"
               },
               "temperature":60.0,
               "voltage":4.94375,
               "frequency":490.0,
               "tuned":true,
               "working":true
            }
         ],
         "voltage":4.94375,
         "frequency":490.0,
         "tuned":true,
         "active":true
      }
   ],
   "hashrate":{
      "value":574.3460573484966,
      "unit":"GigaHash",
      "algo":"SHA256"
   },
   "expected_chips":1,
   "total_chips":1,
   "expected_fans":1,
   "fans":[
      {
         "position":0,
         "rpm":6560.999999999999
      }
   ],
   "psu_fans":[
      
   ],
   "average_temperature":60.0,
   "wattage":14.0,
   "efficiency":24.375548192376993,
   "light_flashing":null,
   "messages":[
      
   ],
   "uptime":{
      "secs":1244,
      "nanos":0
   },
   "is_mining":true,
   "pools":[
      {
         "position":0,
         "url":{
            "scheme":"StratumV1",
            "host":"stratum.mypool",
            "port":3333,
            "pubkey":null
         },
         "accepted_shares":138,
         "rejected_shares":0,
         "active":true,
         "alive":null,
         "user":"b-rowan.bitaxe"
      },
      {
         "position":1,
         "url":{
            "scheme":"StratumV1",
            "host":"stratum.mypool",
            "port":3333,
            "pubkey":null
         },
         "accepted_shares":138,
         "rejected_shares":0,
         "active":false,
         "alive":null,
         "user":"b-rowan.bitaxe"
      }
   ]
}
 ```


## Comments

### b-rowan on 2025-07-29

Only thing I don't like here - 
```json
      "model":{
         "Bitaxe":"Supra"
      },
```
Makes it very inconsistent to parse (this could turn into `"WhatsMiner": "M30S++VG30"` for example)
