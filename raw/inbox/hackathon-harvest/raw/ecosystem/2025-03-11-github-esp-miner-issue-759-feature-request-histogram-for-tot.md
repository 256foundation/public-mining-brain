# bitaxeorg/ESP-Miner issue #759: FEATURE REQUEST: Histogram for Total Hash Rate on the swarm page

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/759
> Collected: 2026-10-07
> Published: 2025-03-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 759
- State: open
- Author: jtsmith0101
- Opened: 2025-03-11
- Closed: n/a
- Labels: enhancement, good first issue, design

## Description

I like graphs.  Seeing a histogram on the swarm page similar to what is displayed on the individual worker pages would be cool, IMO.

Cheers,

James

## Comments

### dskvr on 2025-04-13

IMO should be done in a separate interface. The AxeOS runs off a ESP32 and so has an extremely conservative space budget. Additionally, long term statistics aren't stored on-device for similar reasons, there is no historical data.

There is an API (which is how the swarm functionality works) and so writing a small app that both collects/stores data intermittently and runs an interface off-device is entirely possible; on your computer, start9 or umbrel for instance. 

### g1ass1 on 2025-05-21

I have implemented a very basic MQTT broker on my bit axe 601 (and I mean basic, it exports difficulty presently, but it works - this was done just to see if it was possible)- this connects to my home assistant instance which runs MQTT and I intend to use the data from there.

The api is good, but mqtt is better for RealTIME or nearly Realtime data  - probably abit overkill on this use case though?

### akohlsmith on 2026-08-02

+1 on the MQTT idea; the graph on the dashboard doesn't update or keep historic data unless you keep the dashboard open. Being able to send telemetry data (hashrate, shares, temp, voltage, fan speed, efficiency, etc.) to MQTT would be awesome.
