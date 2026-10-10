# bitaxeorg/ESP-Miner issue #41: stratum method client.reconnect not supported

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/41
> Collected: 2026-10-07
> Published: 2023-10-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 41
- State: closed
- Author: PSLLSP
- Opened: 2023-10-08
- Closed: 2024-12-01
- Labels: enhancement, help wanted, good first issue

## Description

I assume that `BitAxe` miner doesn't support stratum method [**client.reconnect**](https://en.bitcoin.it/wiki/Stratum_mining_protocol#client.reconnect). It is used in pool [MiningRigRentals](https://www.miningrigrentals.com/), to redirect miner from default TCP port (like 3333) to dynamically allocated TCP port. Most well known miners supports this method, for example `cgminer`, `bfgminer`, `gminer` and many others...

Demo configuration, for test. [`cpuminer`](https://github.com/pooler/cpuminer) tested at Linux PC:
```bash
$ cat mrr-test-sha256d-1.sh
#!/bin/sh

POOL="stratum+tcp://eu-01.miningrigrentals.com:3311"
USER="droidMiner.296231"
PASS="BITAXE"

./minerd -a "sha256d" -o "$POOL" -u "$USER" -p "$PASS" $@
```
Show miner version:
```
$ ./minerd -V
cpuminer 2.5.1
 built on Oct  5 2023
 features: x86_64 PHE SSE2 AVX AVX2 XOP
libcurl/7.81.0 OpenSSL/3.0.2 zlib/1.2.11 brotli/1.0.9 zstd/1.4.8 libidn2/2.3.2 libpsl/0.21.0 (+libidn2/2.3.2) libssh/0.9.6/openssl/zlib nghttp2/1.43.0 librtmp/2.3 OpenLDAP/2.5.16
```
Start miner:
```
$ sh mrr-test-sha256d-1.sh

[2023-10-05 22:45:53] Starting Stratum on stratum+tcp://eu-01.miningrigrentals.com:3311
[2023-10-05 22:45:53] 1 miner threads started, using 'sha256d' algorithm.
[2023-10-05 22:45:53] Server requested reconnection to stratum+tcp://eu-01.miningrigrentals.com:52211
[2023-10-05 22:45:54] Stratum requested work restart
[2023-10-05 22:45:55] thread 0: 2097152 hashes, 8222 khash/s
...
```

Notice that miner was redirected from TCP port 3311 to port 52211; this port was allocated dynamically and will change in the future...
Details about protocol are visible when script is started with `-P` parameter:
```
$ sh mrr-test-sha256d-1.sh -P

[2023-10-05 22:57:51] 1 miner threads started, using 'sha256d' algorithm.
[2023-10-05 22:57:51] Starting Stratum on stratum+tcp://eu-01.miningrigrentals.com:3311
*   Trying 188.166.37.58:3311...
* Connected to eu-01.miningrigrentals.com (188.166.37.58) port 3311 (#0)
* Connection #0 to host eu-01.miningrigrentals.com left intact
[2023-10-05 22:57:51] > {"id": 1, "method": "mining.subscribe", "params": ["cpuminer/2.5.1"]}
[2023-10-05 22:57:51] < {"error": null, "id": 1, "result": [["mining.notify", "ae6812eb4cd7735a302a8a9dd95cf71f"], "f800002e", 4]}
[2023-10-05 22:57:51] > {"id": 2, "method": "mining.authorize", "params": ["droidMiner.296231", "BITAXE"]}
[2023-10-05 22:57:51] < {"error": null, "id": 2, "result": true}
[2023-10-05 22:57:51] < {"method": "client.reconnect", "id": 0, "error": null, "params": ["eu-01.miningrigrentals.com","52211"]}
[2023-10-05 22:57:51] Server requested reconnection to stratum+tcp://eu-01.miningrigrentals.com:52211
*   Trying 188.166.37.58:52211...
* Connected to eu-01.miningrigrentals.com (188.166.37.58) port 52211 (#0)
* Connection #0 to host eu-01.miningrigrentals.com left intact
[2023-10-05 22:57:51] > {"id": 1, "method": "mining.subscribe", "params": ["cpuminer/2.5.1"]}
[2023-10-05 22:57:52] < {"id":1,"result":[[["mining.set_difficulty","65536.000"],["mining.notify","730f2d39331a0fef6024fbde40a6e46d"]],"68993b7c",4],"error":null}
[2023-10-05 22:57:52] > {"id": 2, "method": "mining.authorize", "params": ["droidMiner.296231", "BITAXE"]}
[2023-10-05 22:57:52] < {"id":2,"result":true,"error":null}
[2023-10-05 22:57:52] < {"id":null,"method":"mining.set_difficulty","params":[65536]}
...
```

Notice request `{"method": "client.reconnect", "id": 0, "error": null, "params": ["eu-01.miningrigrentals.com","52211"]}` sent to the miner...

I reviewed code for BitAxe miner and I assume that **client.reconnect** support is missing...

When miner doesn't support (or ignore) redirection request, it is disconnected from MRR, this can be demonstrated with cpuminer:
```
$ sh mrr-test-sha256d-1.sh --no-redirect -P
[2023-10-07 17:59:56] 1 miner threads started, using 'sha256d' algorithm.
[2023-10-07 17:59:56] Starting Stratum on stratum+tcp://eu-01.miningrigrentals.com:3311
*   Trying 188.166.37.58:3311...
* Connected to eu-01.miningrigrentals.com (188.166.37.58) port 3311 (#0)
* Connection #0 to host eu-01.miningrigrentals.com left intact
[2023-10-07 17:59:56] > {"id": 1, "method": "mining.subscribe", "params": ["cpuminer/2.5.1"]}
[2023-10-07 17:59:56] < {"error": null, "id": 1, "result": [["mining.notify", "ae6812eb4cd7735a302a8a9dd95cf71f"], "f800002e", 4]}
[2023-10-07 17:59:56] > {"id": 2, "method": "mining.authorize", "params": ["droidMiner.296231", "BITAXE"]}
[2023-10-07 17:59:56] < {"error": null, "id": 2, "result": true}
[2023-10-07 17:59:56] < {"method": "client.reconnect", "id": 0, "error": null, "params": ["eu-01.miningrigrentals.com","52211"]}
[2023-10-07 17:59:56] Ignoring request to reconnect to stratum+tcp://eu-01.miningrigrentals.com:52211
[2023-10-07 17:59:56] stratum_recv_line failed
[2023-10-07 17:59:56] Stratum connection interrupted
*   Trying 188.166.37.58:3311...
* Connected to eu-01.miningrigrentals.com (188.166.37.58) port 3311 (#0)
* Connection #0 to host eu-01.miningrigrentals.com left intact
[2023-10-07 17:59:57] > {"id": 1, "method": "mining.subscribe", "params": ["cpuminer/2.5.1"]}
[2023-10-07 17:59:57] < {"error": null, "id": 1, "result": [["mining.notify", "ae6812eb4cd7735a302a8a9dd95cf71f"], "f800002e", 4]}
[2023-10-07 17:59:57] > {"id": 2, "method": "mining.authorize", "params": ["droidMiner.296231", "BITAXE"]}
[2023-10-07 17:59:57] < {"error": null, "id": 2, "result": true}
[2023-10-07 17:59:57] < {"method": "client.reconnect", "id": 0, "error": null, "params": ["eu-01.miningrigrentals.com","52211"]}
[2023-10-07 17:59:57] Ignoring request to reconnect to stratum+tcp://eu-01.miningrigrentals.com:52211
[2023-10-07 17:59:57] stratum_recv_line failed
[2023-10-07 17:59:57] Stratum connection interrupted
*   Trying 188.166.37.58:3311...
...
```

Example of miner that added missing support for **client.reconnect** is [`gminer`](https://github.com/develsoftware/GMinerRelease/issues/556) 

---

Maybe you wonder why support for **client.reconnect** should be added. Well, MRR allows easy reconfiguration of connected  miners and it allows failover pools. Create account at MRR, flash BitAxe with configuration to connect to MRR and you can use MRR pool to change mining pool without reflashing firmware in BitAxe. Alternatively, you can run local stratum proxy, like [ckpool](https://bitbucket.org/ckolivas/ckpool/src/master/), in that case you do not need MRR...

## Comments

### skot on 2024-02-16

This seems reasonable. Thank for the very detailed feature request.

It seems like a quick and dirty way to do this would be just reset the ESP32 whenever we get `client.reconnect`. Of course, doing it right would be nice too.

### WantClue on 2024-12-01

implemented in #253
