# bitaxeorg/ESP-Miner issue #93: About the time it takes to reconnect

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/93
> Collected: 2026-10-07
> Published: 2024-01-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 93
- State: closed
- Author: kakawlala
- Opened: 2024-01-17
- Closed: 2024-06-03
- Labels: none

## Description

When the external network of the router is lost and restored.  My NerdMiner_v2_1.6.3 reconnects to the pool after 5 minutes.  However, bitaxe 2.0.6 takes 25 minutes to reconnect to the pool.

![Screenshot_20240118-065453_Chrome_1](https://github.com/skot/ESP-Miner/assets/89348834/db8abd83-ae6e-4a65-910c-5148bf49fd47)

![Screenshot_20240118-070125_Chrome (1)](https://github.com/skot/ESP-Miner/assets/89348834/b0ff16db-4fc0-4935-99a7-44440d446c23)


## Comments

### jddebug on 2024-01-30

Not sure if you are describing the same issue as I am having but if I reboot my wifi the bitAxe never seem to reconnect. Instead they seem to be stuck in the initial setup mode where they are creating a hotspot to get initial settings. I have waited over 30 minutes and they never see to try the wifi in settings again necessitating a reboot/power cycle to get them back online. Maybe have them try to reconnect to wifi in settings every 5 minutes to see if it is back up and if not go back to hotspot mode for 5 minutes and then try again?
