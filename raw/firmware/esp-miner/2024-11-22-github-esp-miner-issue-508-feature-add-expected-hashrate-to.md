# bitaxeorg/ESP-Miner issue #508: feature: Add expected hashrate to API

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/508
> Collected: 2026-10-07
> Published: 2024-11-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 508
- State: closed
- Author: b-rowan
- Opened: 2024-11-22
- Closed: 2025-06-11
- Labels: enhancement, good first issue

## Description

It would be nice to have the expected hashrate shown in the API directly to make it a bit easier for external tools to parse it.  AFAIU there is some calculation being done involving cores, frequency, etc, to find this value.

I am happy to PR this if someone can start me in the right direction as to where to source this.

## Comments

### jns-codeworks on 2024-11-24

I think it is this line:

`this.expectedHashRate$ = this.info$.pipe(map(info => {
      return Math.floor(info.frequency * ((info.smallCoreCount * info.asicCount) / 1000))
    }))`

[source](https://github.com/skot/ESP-Miner/blob/master/main/http_server/axe-os/src/app/components/home/home.component.ts)

### jpcomps on 2025-01-03

have a first pass of it here, will clean up and submit pull request against this issue:

https://github.com/jpcomps/ESP-Miner/tree/add_expected_hr

@WantClue @skot are we ok with the precision here? 

### mutatrum on 2025-06-11

Fixed by #603
