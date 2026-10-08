# bitaxeorg/ESP-Miner issue #734: Enable / Disable TPS - Start / Stop mining

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/734
> Collected: 2026-10-07
> Published: 2025-02-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 734
- State: closed
- Author: CryptoIceMLH
- Opened: 2025-02-23
- Closed: 2026-03-23
- Labels: enhancement, good first issue

## Description


Following OSMU townhall #29 discussion 

It would be very useful to have the ability to enable/ disable the onboard TPS that feeds the asic. 

this would allow for mining to be commanded by an external source to start/ stop mining whilst keeping the ESP and AxeOs alive , so the user can maintain connectivity, stats, swarm etc. 

a use case scenario is the upcoming solarbit $0/khw project. Currently i will cut the entire power to the bitaxe but would be better to just instruct the bitaxe via the BAP port to stop mining when sun is down.. and start mining when sun is up. a cleaner way that killing the entire miner. 

Summary: 

1) API command to start stop TPS 
2) BAP port ability to accept such commands from external esp32 hardwired via 6pin BAP 
3) Not sure if possible: but if no mining is being conducted .. we dont need active cooling on the asic.. therefore is it possible when TPS is commanded to stop power to asic to also terminate power to the fan ? worst case pwm to minimum ? thinking how we could maximize energy efficiency by only running essentials on bitaxe to maintain heartbeat. fan running for no reason ruins the efficiency and limit wasted power. 

## Comments

### skot on 2025-02-23

I agree, having a API call to enable/disable the voltage regulator (where supported) would be fantastic.

The challenge here is re-initializing everything when ASIC power is turned back on.

### phil31 on 2025-03-22

+1
something i had in mind since long time, to controle the miner by home assistant ..  :o)
