# bitaxeorg/ESP-Miner issue #102: Automatically reconnect to wifi

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/102
> Collected: 2026-10-07
> Published: 2024-02-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 102
- State: closed
- Author: pacamoto
- Opened: 2024-02-03
- Closed: 2024-05-24
- Labels: enhancement, help wanted, good first issue

## Description

Sometimes people have issues with the wifi and if the device is disconnected, a manual restart is needed to reconnect. It should retry over and over again to reconnect to WIFI if the connection has failed.

## Comments

### jddebug on 2024-02-03

I have this issue too. If I reboot my wifi the bitAxe never seems to reconnect. Instead they seem to be stuck in the initial setup mode where they are creating a hotspot to get initial settings. I have waited over 30 minutes and they never try the wifi in settings again necessitating a reboot/power cycle to get them back online. Maybe have them try to reconnect to wifi in settings every 5 minutes to see if it is back up and if not go back to hotspot mode for 5 minutes and then try again?

### skot on 2024-02-03

That's a good point. I think we should address this too.

We do have to be careful if we retry every 5min though, it will need to exit host AP mode to do that and that could mess up setup.

### jddebug on 2024-02-03

Can you detect that someone has actually connected to the AP and not try the WiFi reconnect until a reboot if someone has connected?

### pacamoto on 2024-02-03

A possible approach could be if it detects no Wifi connection, reboot, every 5 minutes.

### dreson4 on 2024-03-19

Can we have a way to simply just set max retries to max? If my router has any issue and restarts for example the miner will retry 5 times, fail and simply stop. I read the code directly there's a Wifi max retry value. 

### skot on 2024-03-19

You can put whatever number you want here, but be aware you'll have to wait that long before you can configure the WiFi initially

### skot on 2024-05-23

@modl21 verbally submitted this issue, RHR May 23rd

### jddebug on 2024-05-23

This is my most desired feature. Anytime my wifi glitches or reboots I lose miners. 

### skot on 2024-05-23

the issue is that normally we put up the setup AP when we can't find WiFi to give people a chance to configure new WiFi creds.

### jddebug on 2024-05-23

I get that and it is necessary. Why not have it periodically try for the configured wifi though? Maybe every 5 minutes or even 10 minutes. I'd even be happy with 30 minutes. Anything would be better than never and your away for a day or two and not mining due to a wifi glitch/router reboot.

### skot on 2024-05-23

that seems like a good idea. We have to make sure only to try the reconnect if no connections have been made to the config AP

### skot on 2024-05-23

I think @benjamin-wilson said he's going to fix this one for @modl21

### benjamin-wilson on 2024-05-24

Fixed b53b641c6850756654836ff429374b745bd5393c
