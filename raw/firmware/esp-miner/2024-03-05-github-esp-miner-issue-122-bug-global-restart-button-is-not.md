# bitaxeorg/ESP-Miner issue #122: Bug: Global Restart Button is not visible on Mobile Phone Browsing

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/122
> Collected: 2026-10-07
> Published: 2024-03-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 122
- State: closed
- Author: TheMissingNTLDR
- Opened: 2024-03-05
- Closed: 2024-03-15
- Labels: bug

## Description

Steps:
1. Using BitAxe with BM1366 here
2. Bug applies to this version only [v2.1.0](https://github.com/skot/ESP-Miner/releases/tag/v2.1.0)
3. download and upgrade to [esp-miner.bin](https://github.com/skot/ESP-Miner/releases/download/v2.1.0/esp-miner.bin) [www.bin](https://github.com/skot/ESP-Miner/releases/download/v2.1.0/www.bin)
4. Open the www website on a mobile phone via the IP address
5. Check www in both Portrait and Landscape mode
6. I am using iPhoneX and Safari App as browser
7. Actual Result: User is not able to see the (Global) Restart Button
8. Expected Result: User should be able to see the (Global) Restart Button

WORKAROUND: Add your IP to Swarm. Go to Swarm and use the little square Restart button shown there within your worker row.

## Comments

### d4r1as on 2024-03-06

+1

### skot on 2024-03-09

I'm seeing the same here. restart button is nowhere to be found on iOS Safari. 
<img width="700" alt="image" src="https://github.com/skot/ESP-Miner/assets/140785/bf7b5f70-e5dc-4610-8f4c-dc63222ed6d9">


### Sledge0001 on 2024-03-10

Same on Android!

### benjamin-wilson on 2024-03-15

Fixed eb55394d0afe550f5646d5f58a2b118b8a399aeb
