# bitaxeorg/ESP-Miner issue #82: lower hashrate after updating to 2.0.5

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/82
> Collected: 2026-10-07
> Published: 2024-01-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 82
- State: closed
- Author: monster4866
- Opened: 2024-01-10
- Closed: 2024-01-11
- Labels: none

## Description

<img width="964" alt="Screenshot 2024-01-10 at 19 59 30" src="https://github.com/skot/ESP-Miner/assets/119421965/bb2020c7-3f13-4c78-8052-d1d36f097863">

Hi, after updating via the web interface from 2.0.4 to 2.0.5 I have a lower hashrate. I didn't change anything in the settings 575/1200. Model: | BM1366
Thanks

## Comments

### benjamin-wilson on 2024-01-10

Can you share the rest of the axos screens please? Have you tried a restart? 

### benjamin-wilson on 2024-01-10

You could try reducing your frequency as well, overlocking instability will sometimes manifest as lower hashrate 


### monster4866 on 2024-01-10

> an you share the rest of the axos screens please? Have you tried a restart?

<img width="1081" alt="Screenshot 2024-01-10 at 20 29 17" src="https://github.com/skot/ESP-Miner/assets/119421965/424dea40-e3eb-4815-85b6-9325977c2818">

I tried restarting several times, downgrading to 2.0.4 didn't bring any change, I had a temperature of 25 degrees (it's very cold in Germany at the moment), I've now moved the Bitaxe to a warmer place and set the settings to 550 /1200 reduced.

Looks better at first, could this be due to the temperature? 25 degrees was already very low

On 575/1200 it ran for over a week without any problems, then I updated to 2.0.5 and the hashrate decreased. If this is due to the overclock, it wouldn't run stable for a week

### benjamin-wilson on 2024-01-10

I think you just had an unstable overclock. It also looks like you have a V1 Ultra where the temperature readings are not accurate. An unstable overlock may not become apparent until a power cycle or another environment change. 

### monster4866 on 2024-01-10

> I think you just had an unstable overclock. It also looks like you have a V1 Ultra where the temperature readings are not accurate. An unstable overlock may not become apparent until a power cycle or another environment change.

yes, it's the v1 board, after 25 minutes it's still at +520GH, I'll let it run overnight and see what it looks like.

First of all, thank you very much for the support :-)

### monster4866 on 2024-01-11

This was the Solution. Now my settings are 550/1200, stable +500Gh
