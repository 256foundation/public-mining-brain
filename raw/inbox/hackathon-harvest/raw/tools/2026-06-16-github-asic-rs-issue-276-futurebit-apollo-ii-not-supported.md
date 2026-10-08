# 256foundation/asic-rs issue #276: FutureBit Apollo II not supported

> Source: https://github.com/256foundation/asic-rs/issues/276
> Collected: 2026-10-07
> Published: 2026-06-16

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 276
- State: closed
- Author: plebhash
- Opened: 2026-06-16
- Closed: 2026-06-18
- Labels: none

## Description

as noted in https://github.com/stratum-mining/sv2-apps/pull/553#issuecomment-4723784505

## Comments

### b-rowan on 2026-06-16

Could you run this python script (can provide the same script in rust if you prefer, it's basically just a tracing subscriber on debug) and provide the result?  Need to see if there is anything I can use to discover this miner on the http endpoint or via 4028 api.

```python
import asyncio
import logging

from pyasic_rs import MinerFactory

logging.basicConfig(level=logging.DEBUG)

async def main():
    miner = await MinerFactory().get_miner("192.168.15.7")
    if miner is not None:
        print(await miner.get_data())

asyncio.run(main())
```

### plebhash on 2026-06-17

```
$ cat test.py
import asyncio
import logging

from pyasic_rs import MinerFactory

logging.basicConfig(level=logging.DEBUG)

async def main():
    miner = await MinerFactory().get_miner("192.168.15.7")
    if miner is not None:
        print(await miner.get_data())

asyncio.run(main())
$
$
$ ping 192.168.15.7
PING 192.168.15.7 (192.168.15.7): 56 data bytes
64 bytes from 192.168.15.7: icmp_seq=0 ttl=64 time=1.305 ms
64 bytes from 192.168.15.7: icmp_seq=1 ttl=64 time=1.098 ms
^C
--- 192.168.15.7 ping statistics ---
2 packets transmitted, 2 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 1.098/1.202/1.305/0.103 ms
$
$
$ python3 test.py
DEBUG:asyncio:Using selector: KqueueSelector
DEBUG:asic_rs.factory:get_miner; ip=192.168.15.7
DEBUG:asic_rs_core.util:send_rpc_command; ip=192.168.15.7 command="version"
DEBUG:asic_rs_core.util:send_rpc_command; ip=192.168.15.7 command="devdetails"
DEBUG:asic_rs_core.util:send_web_command; ip=192.168.15.7 command="/"
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.7")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.7:80
DEBUG:asic_rs_core.util:failed to connect to 192.168.15.7 rpc
DEBUG:asic_rs_core.util:failed to connect to 192.168.15.7 rpc
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.7:80
DEBUG:asic_rs.factory:failed to identify 192.168.15.7
```

### b-rowan on 2026-06-17

Ok, its not logging any result from the http endpoint.  Can you run curl against it?

`curl http://192.168.15.7/`

### plebhash on 2026-06-17

```
curl http://192.168.15.7/
/overview%
```

let's proceed with the VPN approach as discussed on Discord
