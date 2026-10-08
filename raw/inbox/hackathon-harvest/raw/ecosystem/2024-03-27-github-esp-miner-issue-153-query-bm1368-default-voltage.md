# bitaxeorg/ESP-Miner issue #153: Query: BM1368 default voltage

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/153
> Collected: 2026-10-07
> Published: 2024-03-27

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 153
- State: closed
- Author: HypeLaser
- Opened: 2024-03-27
- Closed: 2024-04-05
- Labels: none

## Description

Please confirm the "core voltage" setting for the BM1368 (401, Supra)? The default when the device arrived on an older firmware was running at 1200.

The [edit.components.ts](https://github.com/skot/ESP-Miner/commit/a5daff7b015fbe5331d759ef612bda937e4ab0ad#diff-c4afaa94f901daba70c27e229d732d61530ee2455fd03792375d81ed67d24387) file states the default is "1166", which is what firmware 2.1.3 now shows.

but the [edit.components.html](https://github.com/skot/ESP-Miner/commit/3df855d9b42943a455abd97224caa65ee8387da2#diff-b916291b974e18f57dcad9ca40f8f3419d8444aa4de96b85e9348a7ba4d9b0f6) states "1200".

So should it be 1200 or 1166?

As a side question, what's the consequences of having the wrong voltage set? Should I expect it to run hotter, faster, slower, rejected shares?



## Comments

### MyOwn2C on 2024-03-27

<img width="402" alt="image" src="https://github.com/skot/ESP-Miner/assets/158797249/b3dd9743-4b21-4e09-9269-879767c7ad22">

Higher volt = higher temp but not necessary faster


### HypeLaser on 2024-03-27

Ah ok, so on firmware 2.1.3 the 1166 option is flagged as 'default'.

<img width="381" alt="Screenshot 2024-03-27 at 17 16 08" src="https://github.com/skot/ESP-Miner/assets/110939572/c5ca54d5-ad43-40eb-b532-b021f6a4ba84">


### MyOwn2C on 2024-03-27

If it works with 1166, leave it be. Unless you want to overclock
