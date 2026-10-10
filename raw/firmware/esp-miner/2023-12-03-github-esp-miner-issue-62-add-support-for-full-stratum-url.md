# bitaxeorg/ESP-Miner issue #62: Add support for full stratum URL

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/62
> Collected: 2026-10-07
> Published: 2023-12-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 62
- State: closed
- Author: Dolu89
- Opened: 2023-12-03
- Closed: 2025-06-26
- Labels: none

## Description

Some pools have specific params like nicehash for lower accepted rate
`stratum+tcp://sha256asicboost.auto.nicehash.com:9200#xnsub`
On AxeOS, it's impossible to add this `#xnsub`

source: https://www.nicehash.com/support/mining-help/asic-mining/how-to-connect-your-asic-machine-to-nicehash

## Comments

### benjamin-wilson on 2023-12-25

I'm not sure how other firmware parse this out but TCP connections can't accept any additional parameters beyond IP and port.

### johnny9 on 2023-12-25

Here is the nice hash blog that describes this specific parameter.

https://www.nicehash.com/blog/post/what-is-extranonce-subscribe-extension-xnsub#!

### benjamin-wilson on 2023-12-25

This should be an extra pool option, not in the URL though as the issue describes 

### Dolu89 on 2024-03-02

XNSUB is now required for mining on nicehash: https://www.nicehash.com/blog/post/notice-for-miners-xnsub-support

### CoanLuciano on 2024-03-25

We could use Bitaxe with Nicehash to make some sats if we solve this issue...
Nicehash uses the lightning network as a payment method...

### mutatrum on 2025-06-26

Fixed with #1064
