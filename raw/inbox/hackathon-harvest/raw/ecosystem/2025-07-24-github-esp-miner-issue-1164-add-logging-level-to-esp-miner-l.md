# bitaxeorg/ESP-Miner issue #1164: add logging level to esp-miner logs and AxeOS log viewer

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1164
> Collected: 2026-10-07
> Published: 2025-07-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1164
- State: open
- Author: skot
- Opened: 2025-07-24
- Closed: n/a
- Labels: enhancement, help wanted, design

## Description

it would be nice to add a couple logging levels to esp-miner. the default would be very succinct and show the highlights.. Kinda like what we have now. debug logging level would have much more information shown in the log and would be useful for users trying to debug problems (but not necessarily practical for everyday usage)

some things that could be in debug level logs;
- fan control PID
- more detailed temperature readings
- more information about jobs sent to ASIC
- more information about validating shares and computing hashrate
- exact hex of packets sent to the ASIC
- more detail about power and TPS546 error codes
- more

## Comments

### skot on 2025-07-24

And then of course AxeOS needs an update in the logs tab to choose between logging levels. We can also think about whether this log level setting should be stored in nvs. (could be useful to have the debug setting remembered at boot)

### kakulukia on 2025-09-26

Id like to help with this feature. Is there a possiblility to have the web UI running locally using the API of the Bitaxe to get its data? This would make implementing features a bit easier.
