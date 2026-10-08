# bitaxeorg/ESP-Miner issue #193: Nicehash sends separate mining.set_extranonce messages sometimes... maybe handle them?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/193
> Collected: 2026-10-07
> Published: 2024-05-31

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 193
- State: closed
- Author: skot
- Opened: 2024-05-31
- Closed: 2025-06-26
- Labels: enhancement

## Description

I haven't seen this before on any other pool. Maybe we should consider handling this unsolicited extranonce change?

```
I (9556) stratum_task: Get IP for URL: sha256asicboost.auto.nicehash.com
I (9586) stratum_task: Connecting to: stratum+tcp://sha256asicboost.auto.nicehash.com:9200 (130.211.20.161)
I (9586) stratum_task: Socket created, connecting to 130.211.20.161:9200
I (9586) ASIC_task: ASIC Ready!
I (9596) main_task: Returned from app_main()
I (9606) stratum_api: tx: {"id": 1, "method": "mining.subscribe", "params": ["bitaxe/BM1368"]}
I (9606) stratum_api: tx: {"id": 2, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (9626) stratum_api: tx: {"id": 3, "method": "mining.suggest_difficulty", "params": [1000]}
I (9636) stratum_api: tx: {"id": 4, "method": "mining.authorize", "params": ["<redacted>", "x"]}
I (9696) stratum_task: rx: {"id":1,"error":null,"result":[[["mining.set_difficulty","02187bbb75009a23a3"],["mining.notify","02187bbb75009a23a3"]],"02187bbb75009a23a3",3]}
I (9706) stratum_api: extranonce_str: 02187bbb75009a23a3
I (9706) stratum_api: extranonce_2_len: 3
I (9726) stratum_task: rx: {"id":4,"result":true,"error":null}
I (9726) stratum_task: setup message accepted
I (9726) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[262144.0]}
I (9736) stratum_task: Set stratum difficulty: 262144
I (9746) stratum_task: rx: {"id":null,"method":"mining.set_version_mask","params":["1fffe000"]}
I (9756) stratum_task: Set version mask: 1fffe000

...

I (82806) stratum_task: rx: {"id":null,"method":"mining.set_extranonce","params":["3263b370affeb0d550",3]}
I (82806) stratum_api: unhandled method in stratum message: {"id":null,"method":"mining.set_extranonce","params":["3263b370affeb0d550",3]}
I (82816) stratum_task: Set version mask: 1fffe000
I (82826) stratum_task: rx: {"id":null,"method":"mining.set_difficulty","params":[262144.0]}
```

## Comments

### seangrant82 on 2024-06-11

does this prevent hashing on nicehash? I haven't been able to get it to work

### skot on 2024-06-11

It seemed like it was working for me.. esp-miner was definitely submitting shares. 

### seangrant82 on 2024-06-12

it works on bitaxe but not nerdaxe. will have to submit issue there:


₿ (21067) STRATUM: Socket connection closed
₿ (21067) stratum_task: Failed to receive JSON-RPC line, reconnecting...
₿ (26077) stratum_task: Shutting down socket and restarting...
₿ (26077) stratum_task: Socket created, connecting to 130.211.20.161:9200
₿ (26107) stratum_api: tx: {"id": 9, "method": "mining.subscribe", "params": ["NerdAxe/BM1366"]}
₿ (26217) stratum_api: Received result {"id":9,"error":null,"result":[[["mining.set_difficulty","1111f6c5ce2b7dcdfb"],["mining.notify","1111f6c5ce2b7dcdfb"]],"1111f6c5ce2b7dcdfb",3]}
₿ (26227) stratum_api: tx: {"id": 10, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
₿ (32317) stratum_api: Received result {"id":0,"method":"client.reconnect","params":[]}
₿ (32317) stratum_api: tx: {"id": 11, "method": "mining.suggest_difficulty", "params": [1000]}
₿ (32337) stratum_api: tx: {"id": 12, "method": "mining.authorize", "params": ["wallet.nerdaxe", "fake_password"]}
₿ (32347) STRATUM: Socket connection closed
₿ (32347) stratum_task: Failed to receive JSON-RPC line, reconnecting...

### seangrant82 on 2024-06-12

Doesn't seem to accept shares though 
<img width="407" alt="image" src="https://github.com/skot/ESP-Miner/assets/11846453/b3793244-9244-4458-bfbe-672d362d5277">


### mutatrum on 2025-06-23

WTF?
```
I (14087) stratum_task: Opening connection to pool: sha256asicboost.auto.nicehash.com:9200
I (14087) stratum_task: Starting heartbeat thread for primary pool: sha256asicboost.auto.nicehash.com:9200
I (14114) stratum_task: Connecting to: stratum+tcp://sha256asicboost.auto.nicehash.com:9200 (130.211.20.161)
I (14427) stratum_task: Socket created, connecting to 130.211.20.161:9200
I (14440) stratum_task: Resetting stratum uid
I (14441) stratum_task: Clean Jobs: clearing queue
I (14441) stratum_api: tx: {"id": 1, "method": "mining.configure", "params": [["version-rolling"], {"version-rolling.mask": "ffffffff"}]}
I (14454) stratum_api: tx: {"id": 2, "method": "mining.subscribe", "params": ["bitaxe/BM1368/v2.9.0b3-dirty"]}
I (14465) stratum_api: tx: {"id": 3, "method": "mining.authorize", "params": ["bc1q######################################.bitaxe-supra", "x"]}
I (14634) stratum_task: rx: {"id":1,"error":null,"result":{"version-rolling":true,"version-rolling.mask":"1fffe000"}}
I (14635) stratum_api: Set version mask: 1fffe000
I (14640) stratum_task: Set version mask: 1fffe000
I (14647) stratum_task: rx: {"id":2,"error":null,"result":[[["mining.set_difficulty","7800000f3e6411b09a"],["mining.notify","7800000f3e6411b09a"]],"7800000f3e6411b09a",3]}
I (14662) stratum_api: extranonce_str: 7800000f3e6411b09a
I (14667) stratum_api: extranonce_2_len: 3
I (14673) stratum_task: rx: {"id":3,"result":true,"error":null}
I (14679) stratum_task: setup message accepted
I (14684) stratum_api: tx: {"id": 4, "method": "mining.suggest_difficulty", "params": [1000]}
I (14694) stratum_api: tx: {"id": 5, "method": "mining.extranonce.subscribe", "params": []}
I (14886) stratum_task: rx: {"id":5,"result":true,"error":null}
I (14886) stratum_task: message result accepted
I (37727) stratum_task: rx: {"id":3,"result":false,"error":[0,"Missing KYC/KYB",null]}
E (37728) stratum_task: setup message rejected: Missing KYC/KYB
I (37732) stratum_api: Error: recv (errno 128: Socket is not connected)
E (37739) stratum_task: Failed to receive JSON-RPC line, reconnecting...
E (37746) stratum_task: Shutting down socket and restarting...
```

![Image](https://github.com/user-attachments/assets/59258b96-0bfd-4439-b457-172bfd4789df)

https://www.nicehash.com/support/general-help/kyc/kyc-tiers
