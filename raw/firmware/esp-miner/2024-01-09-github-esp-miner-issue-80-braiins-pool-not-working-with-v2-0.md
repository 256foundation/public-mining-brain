# bitaxeorg/ESP-Miner issue #80: Braiins pool not working with v2.0.5

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/80
> Collected: 2026-10-07
> Published: 2024-01-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 80
- State: closed
- Author: skot
- Opened: 2024-01-09
- Closed: 2024-06-05
- Labels: bug

## Description

from twitter; https://x.com/der_hodler/status/1744807662947045797?s=20

> i found a small bug in new firmware. you can no longer mine on [http://eu.stratum.braiins.com](https://t.co/ywH3f2P20t). As soon as I enter another pool address like public pool it works. but brains no more. Worked before the update. Have tested it. i have 2 bitaxe. one public pool, one braiins.

<img width="597" alt="image" src="https://github.com/skot/ESP-Miner/assets/140785/93f40a9c-17da-4a68-851f-42607adaa7a2">


## Comments

### skot on 2024-01-09

I tried this myself and it also crashes. relevant log;

```
I (2401) stratum_task: Connecting to: stratum+tcp://stratum.braiins.com:3333 (159.223.239.132)

I (2411) stratum_task: Socket created, connecting to 159.223.239.132:3333
I (2421) main_task: Returned from app_main()
I (2571) stratum_api: tx: {"id": 1, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (2791) stratum_api: Received result {"id":null,"method":"mining.set_version_mask","params":["1fffe000"]}
E (2801) stratum_api: Unable to parse subscribe result {"id":null,"method":"mining.set_version_mask","params":["1fffe000"]}
I (2821) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}

I (2831) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1qqkredrrxc0pqjpcyp8ku3ry46e40tp40zrf0k0.bitaxe", "x"]}

Guru Meditation Error: Core  1 panic'ed (LoadProhibited). Exception was unhandled.

Core  1 register dump:
PC      : 0x400556d5  PS      : 0x00060530  A0      : 0x82095aae  A1      : 0x3fcc37a0  
0x400556d5: strlen in ROM

A2      : 0x00000000  A3      : 0xfffffffc  A4      : 0x000000ff  A5      : 0x0000ff00  
A6      : 0x00ff0000  A7      : 0xff000000  A8      : 0x00000000  A9      : 0x00000000  
A10     : 0x00000000  A11     : 0x0000000c  A12     : 0x3fcc39e4  A13     : 0x00000000  
A14     : 0x3fcc39b4  A15     : 0x00000001  SAR     : 0x00000004  EXCCAUSE: 0x0000001c  
EXCVADDR: 0x00000000  LBEG    : 0x400556d5  LEND    : 0x400556e5  LCOUNT  : 0xffffffff  
0x400556d5: strlen in ROM

0x400556e5: strlen in ROM



Backtrace: 0x400556d2:0x3fcc37a0 |<-CORRUPTED
0x400556d2: strlen in ROM





ELF file SHA256: c9338a7ebfe5b9b3
```

### skot on 2024-01-09

this is how it looks with public-pool

```
I (2151) stratum_task: Connecting to: stratum+tcp://public-pool.io:21496 (68.235.52.36)

I (2151) stratum_task: Socket created, connecting to 68.235.52.36:21496
I (2431) stratum_api: tx: {"id": 1, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (2531) stratum_api: Received result {"id":1,"error":null,"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"}}
I (2541) stratum_api: Set version mask: 1fffe000
I (2541) stratum_api: tx: {"id": 2, "method": "mining.subscribe", "params": ["bitaxe BM1366"]}

I (2841) stratum_api: Received result {"id":2,"error":null,"result":[[["mining.notify","8f02e4c8"]],"8f02e4c8",4]}
I (2841) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}

I (2851) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["bc1qqkredrrxc0pqjpcyp8ku3ry46e40tp40zrf0k0.skot", "x"]}

I (2871) stratum_task: Extranonce: 8f02e4c8
I (2871) stratum_task: Extranonce 2 length: 4
```


### skot on 2024-01-09

here is Braiins pool with v2.0.4
```
I (2353) stratum_task: Connecting to: stratum+tcp://stratum.braiins.com:3333 (159.223.18.138)

I (2353) stratum_task: Socket created, connecting to 159.223.18.138:3333
I (2543) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe BM1366"]}

I (2793) stratum_api: Received result {"id":1,"result":[[["mining.set_difficulty","1"],["mining.notify","1"]],"00",6],"error":null}
I (2793) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}

I (2803) stratum_api: tx: {"id": 3, "method": "mining.authorize", "params": ["skot9000", "x"]}

I (2813) stratum_task: Extranonce: 00
I (2813) stratum_task: Extranonce 2 length: 6
I (2823) stratum_api: tx: {"id": 4, "method": "mining.suggest_difficulty", "params": [512]}
```

### skot on 2024-01-10

it seems that the issue is sending `mining.configure` before `mining.subscribe`

### benjamin-wilson on 2024-01-10

```
I (2468) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (2528) stratum_api: Received result {"id":2,"result":null,"error":[21,"ConfigurationOutOfOrder",null]}

```
So the STRATUM_V1_configure_version_rolling function doesn't work (the parsing isn't correct) but if the order is reversed this function is skipped

### skot on 2024-01-10

this seems related to #50 

### skot on 2024-01-10

> ```
> I (2468) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
> I (2528) stratum_api: Received result {"id":2,"result":null,"error":[21,"ConfigurationOutOfOrder",null]}
> ```
> 
> 
>      
>   
> 
> So the STRATUM_V1_configure_version_rolling function doesn't work (the parsing isn't correct) but if the order is reversed this function is skipped

oh, I see what you mean.. Braiins is even complaining about it here; ConfigurationOutOfOrder

```
I (2391) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe BM1366"]}
I (2451) stratum_api: Received result {"id":1,"result":[[["mining.set_difficulty","1"],["mining.notify","1"]],"00",6],"error":null}
I (2451) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (2511) stratum_api: Received result {"id":2,"result":null,"error":[21,"ConfigurationOutOfOrder",null]}
I (2521) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}
I (2531) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["skot9000", "x"]}
I (2531) stratum_task: Extranonce: 00
I (2541) stratum_task: Extranonce 2 length: 6
I (2571) stratum_task: rx: {"id":3,"result":true,"error":null}
```

### benjamin-wilson on 2024-01-13

Did some more work on this,

When the order is correct mining.subscribe does not immediately receive the correct response. 

**Example response:**
` {“result”:[[[“mining.set_difficulty”,“731ec5e0649606ff”],[“mining.notify”,“731ec5e0649606ff”]],“e9695791”,4],“id”:1,“error”:null}`

**Actual response:**
```
 I (3828) stratum_api: tx: {"id": 2, "method": "mining.subscribe", "params": ["bitaxe/BM1366"]}
I (3838) stratum_api: STRATUM_V1_subscribe Received result {"id":null,"method":"mining.set_version_mask","params":["1fffe000"]}

```

So instead of a response we're getting a `mining.set_version_mask` which was already done in the configure. At this point it seems to be an issue with braiins


### benjamin-wilson on 2024-01-13

Stratum reference: https://reference.cash/mining/stratum-protocol

### CoanLuciano on 2024-06-05

I am using braiins with 2.1.7 and it's working.
I already have received some sats from 1 week of mining through lightning...
