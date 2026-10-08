# bitaxeorg/ESP-Miner issue #615: Feature Request: Locate BitAxe

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/615
> Collected: 2026-10-07
> Published: 2025-01-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 615
- State: closed
- Author: StarMikeMichael
- Opened: 2025-01-05
- Closed: 2025-12-19
- Labels: none

## Description

Feature request: 
Locate a specific BitAxe via a link on the AxeOS dashboard.  
An ideal solution is to light up the ENTIRE Screen or blink rapidly between FULL pixels and zero pixels.  
(Similar to how full-size miner's have a 'locate this worker' button which causes LED's to blink on the corresponding miner.)
This will be helpful for locations with multiple BitAxe units.  



## Comments

### dustinb on 2025-01-18

I was looking into this and did a thing where the logo screen is re-used to locate a Bitaxe.
https://github.com/skot/ESP-Miner/compare/master...dustinb:ESP-Miner:locate-bitaxe  

Challenging part is where in the UI it should go.  Probably belongs in Swarm but that table is getting pretty busy.  A checkbox in Settings is cleaner.

Then had a thought about showing the host name on urls screen instead of "Bitaxe IP:"  No locate mode needed, always on.

```
Stratum Host:
public-pool.io
supra_401 IP:
192.168.1.226
```

hostname is in nvs, I'm not sure if it's ok to have screen refresh read from nvs every time.  Could keep it updated in the global state.

### mutatrum on 2025-12-19

Fixed by #1369
