# 256foundation/asic-rs issue #275: Braiins BMM100 shows with `"make": "Antminer"`

> Source: https://github.com/256foundation/asic-rs/issues/275
> Collected: 2026-10-07
> Published: 2026-06-16

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 275
- State: closed
- Author: plebhash
- Opened: 2026-06-16
- Closed: 2026-06-17
- Labels: none

## Description

as noted in https://github.com/stratum-mining/sv2-apps/pull/553#issuecomment-4723784505

```
"miner_telemetry": {
        "ip": "192.168.15.31",
        "make": "Antminer",
        "model": "BRAIINS MINI MINER BMM 100",
        "firmware_version": "2026-04-14-0-912d084c-26.04-plus",
        "reported_hashrate_hs": 1012813471661.3801,
        "power_consumption_w": 41.0,
        "efficiency_j_per_th": 40.48129408542047,
        "average_temperature_c": null,
        "uptime_secs": 944,
        "is_mining": true
      }
```

## Comments

### b-rowan on 2026-06-16

Same python script as with your other issue, can you try this?  This time trying to see what its picking up as a false positive to classify as AM make.

```python
import asyncio
import logging

from pyasic_rs import MinerFactory

logging.basicConfig(level=logging.DEBUG)

async def main():
    miner = await MinerFactory().get_miner("192.168.15.31")
    if miner is not None:
        print(await miner.get_data())

asyncio.run(main())
```

### b-rowan on 2026-06-17

I found the issue, it's a regression caused by introducing an unknown miner type.  Fix WIP.

### plebhash on 2026-06-17

sorry for the delay @b-rowan 

there you go:
```
python3 test.py
DEBUG:asyncio:Using selector: KqueueSelector
DEBUG:asic_rs.factory:get_miner; ip=192.168.15.31
DEBUG:asic_rs_core.util:send_rpc_command; ip=192.168.15.31 command="devdetails"
DEBUG:asic_rs_core.util:send_web_command; ip=192.168.15.31 command="/"
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:asic_rs_core.util:send_rpc_command; ip=192.168.15.31 command="version"
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:asic_rs_core.util:parse_rpc_result; response="{\"STATUS\":[{\"STATUS\":\"S\",\"When\":1781724257,\"Code\":22,\"Msg\":\"BOSer versions\",\"Description\":\"BOSer boser-openwrt 0.1.0-912d084c\"}],\"VERSION\":[{\"API\":\"3.7\",\"BOSer\":\"boser-openwrt 0.1.0-912d084c\"}],\"id\":1}"
DEBUG:asic_rs_core.util:send_graphql_command; ip=192.168.15.31 command="{ bosminer { info { modelName } } }"
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:asic_rs_core.util:send_graphql_command; ip=192.168.15.31 command="{ bos { info { version { full } } } }"
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:reqwest.connect:starting new connection 'Some("192.168.15.31")'
DEBUG:hyper_util.client.legacy.connect.http:connecting to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.connect.http:connected to 192.168.15.31:80
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:reuse idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:reuse idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:reuse idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:reuse idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:reuse idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:reuse idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:reuse idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:reuse idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:reuse idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:reuse idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
DEBUG:hyper_util.client.legacy.pool:pooling idle connection for ("http", 192.168.15.31)
MinerData(schema_version='0.6.0', timestamp=1781724258, ip='192.168.15.31', mac='88:A6:EF:D0:05:34', device_info=DeviceInfo(make='Antminer', model='BRAIINS MINI MINER BMM 100', hardware=MinerHardware(fans=None, boards=None), firmware='Braiins', algo=SHA256), serial_number='KSmwyPBVNHR0dp4G', hostname='miner-d00534', api_version='1.3.0', firmware_version='2026-04-14-0-912d084c-26.04-plus', control_board_version=MinerControlBoard(known=True, name='BraiinsCB'), expected_hashboards=None, hashboards=[], hashrate=HashRate(value=0.0, unit=TH/s, algo='SHA256'), expected_hashrate=HashRate(value=1.0, unit=TH/s, algo='SHA256'), expected_chips=None, total_chips=None, expected_fans=None, fans=[FanData(position=0, rpm=173.0)], psu_fans=[], average_temperature=None, fluid_temperature=None, wattage=2.0, tuning_target=None, scaled_tuning_target=None, efficiency=None, light_flashing=False, messages=[], uptime=113.0, is_mining=False, pools=[PoolGroupData(name='', quota=1, pools=[PoolData(position=0, url=stratum2+tcp://v2.stratum.braiins.com:3336, accepted_shares=0, rejected_shares=0, active=False, alive=True, user='plebhash'), PoolData(position=1, url=stratum2+tcp://75.119.150.111:3333, accepted_shares=0, rejected_shares=0, active=False, alive=True, user='plebhash.bmm100'), PoolData(position=2, url=stratum+tcp://192.168.15.56:34255, accepted_shares=0, rejected_shares=0, active=False, alive=False, user='bmm100'), PoolData(position=3, url=stratum2+tcp://75.119.150.111:3333, accepted_shares=0, rejected_shares=0, active=False, alive=True, user='sri/donate/50/xxx'), PoolData(position=4, url=stratum2+tcp://54.251.17.13:3333, accepted_shares=0, rejected_shares=0, active=False, alive=True, user='xxx'), PoolData(position=5, url=stratum2+tcp://192.168.15.56:34255, accepted_shares=0, rejected_shares=0, active=False, alive=True, user='bmm100'), PoolData(position=6, url=stratum2+tcp://stratum.braiins.com:3333, accepted_shares=0, rejected_shares=0, active=False, alive=True, user='plebhash.test'), PoolData(position=7, url=stratum2+tcp://192.168.15.52:34265, accepted_shares=0, rejected_shares=0, active=False, alive=True, user='solo_miner')])])
```
