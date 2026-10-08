# 256foundation/asic-rs issue #317: AntMiner Z15 & Z15Pro

> Source: https://github.com/256foundation/asic-rs/issues/317
> Collected: 2026-10-07
> Published: 2026-07-28

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 317
- State: closed
- Author: Kraitcer
- Opened: 2026-07-28
- Closed: 2026-08-10
- Labels: none

## Description

We are using asic-rs to scan our mining network. We have encountered two issues:

Z15 (non‑Pro) devices are not discovered at all – the scanner returns no entry for these miners, while a previous Python‑based library (e.g., pyasic) correctly detects them on the same network.

Z15Pro devices are discovered, but two metrics are always None:

inlet_chip_temperature

outlet_chip_temperature

For the sake of objectivity, I set up a minimal Rust project with a fresh dependency on asic-rs and ran the simple scan command exactly as described in the documentation – the problems persist.
Here is an example of the raw data I receive for Z5 Pro devices: 
MinerData(schema_version='0.7.2', timestamp=1785221660, ip='172.18.216.21', mac='EC:84:39:BF:69:2D', device_info=DeviceInfo(make='Antminer', model='Z15Pro', hardware=MinerHardware(fans=2, boards=[6, 6, 6]), firmware='AntMiner Stock', algo=SHA256), serial_number='THQGEVUBFJCAD0020', hostname='Antminer', api_version='3.1', firmware_version='Wed Dec 13 11:33:17 CST 2023', control_board_version=MinerControlBoard(known=True, name='Xilinx'), expected_hashboards=3, hashboards=[BoardData(position=0, hashrate=None, expected_hashrate=None, board_temperature=None, inlet_chip_temperature=None, outlet_chip_temperature=None, expected_chips=6, working_chips=None, serial_number=None, chips=[], voltage=None, frequency=None, tuned=None, active=False), BoardData(position=1, hashrate=None, expected_hashrate=None, board_temperature=None, inlet_chip_temperature=None, outlet_chip_temperature=None, expected_chips=6, working_chips=6, serial_number=None, chips=[], voltage=None, frequency=800.0, tuned=None, active=True), BoardData(position=2, hashrate=None, expected_hashrate=None, board_temperature=None, inlet_chip_temperature=None, outlet_chip_temperature=None, expected_chips=6, working_chips=6, serial_number=None, chips=[], voltage=None, frequency=800.0, tuned=None, active=True)], hashrate=HashRate(value=0.62914, unit=TH/s, algo='SHA256'), expected_hashrate=HashRate(value=0.87411, unit=TH/s, algo='SHA256'), expected_chips=18, total_chips=12, expected_fans=2, fans=[FanData(position=0, rpm=4680.0), FanData(position=1, rpm=4560.0)], psu_fans=[], average_temperature=None, fluid_temperature=None, outlet_fluid_temperature=None, wattage=None, tuning_percent=None, tuning_target=TuningTarget.mode(mode=Normal), scaled_tuning_target=TuningTarget.mode(mode=Normal), tuning_capabilities=None, efficiency=None, light_flashing=False, messages=[], uptime=datetime.timedelta(days=12, seconds=68847), is_mining=True, pools=[PoolGroupData(name='', quota=1, pools=[PoolData(position=0, url=stratum+tcp://zec-ru.kryptex.network:7042, accepted_shares=228314, rejected_shares=252, active=True, alive=True, user='krxY9K2VDD.k003'), PoolData(position=1, url=stratum+tcp://+stratum+tcp:80//mining.viabtc.io:302, accepted_shares=0, rejected_shares=0, active=True, alive=False, user='Kmax71.k8402'), PoolData(position=2, url=stratum+tcp://:80, accepted_shares=0, rejected_shares=0, active=True, alive=False, user='')])])


## Comments

### b-rowan on 2026-07-29

Z15 should just need a configuration added for them, how many chips/boards/fans?

### Kraitcer on 2026-07-31

> Z15 should just need a configuration added for them, how many chips/boards/fans?

chips - 3 per bord/boards - 3/fans - 2?

### b-rowan on 2026-07-31

Nevermind, seems like we have a valid entry.

It might be related to #318, do you get any response from `/cgi-bin/miner_type.cgi`?
