# bitaxeorg/ESP-Miner issue #244: [Feature Request| pyasic support

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/244
> Collected: 2026-10-07
> Published: 2024-06-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 244
- State: closed
- Author: pixeldoc2000
- Opened: 2024-06-28
- Closed: 2024-07-31
- Labels: none

## Description

Let get [pyasic](https://github.com/UpstreamData/pyasic/) support for Bitaxe (esp-miner) rolling.

Then we can monitor and control Bitaxe with [Home Assistant](https://www.home-assistant.io/) and [hass-miner](https://github.com/Schnitzel/hass-miner) integration via pyasic to have a simple automation going. For example: mining when enough Solar power is available or restarting Bitaxe if connection with pool is lost.

Created a Feature Request in pyasic Repo too: https://github.com/UpstreamData/pyasic/issues/165

## Comments

### HypeLaser on 2024-06-28

I was already using the API to pull the data into Home Assistant (back in 2.1.4) but I found the BitAxe devices stopped responding to web page requests after a while. So I stopped logging the data.

I do second being able to access and log the data in a way that doesn't stop the devices operating.

### pixeldoc2000 on 2024-06-30

@HypeLaser 
There are some fixed to memory leaks and stuff in current firmware, maybe the problem is already fixed with 2.1.8 .

Other than that, the esp isn't the most powerful device and has to deal with a lot of things. We should limit the requests to the device.

Maybe test again with the current FW.

### pixeldoc2000 on 2024-06-30

Update: basic Bitaxe Support was added to [pyasic master](https://github.com/UpstreamData/pyasic/commits/master/), thanks to https://github.com/b-rowan and https://github.com/UpstreamData .
