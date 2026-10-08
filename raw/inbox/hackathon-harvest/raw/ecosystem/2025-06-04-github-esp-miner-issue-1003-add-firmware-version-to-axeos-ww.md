# bitaxeorg/ESP-Miner issue #1003: Add firmware version to AxeOS / www.bin

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1003
> Collected: 2026-10-07
> Published: 2025-06-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1003
- State: closed
- Author: skot
- Opened: 2025-06-04
- Closed: 2025-06-26
- Labels: none

## Description

I think this can be as "simple" as a static field in AxeOS Settings that gets automagically updated at build time with the current version string. This will be a very helpful indication for users that have forgotten to update www.bin or did run the update and it failed.

This is meant to be a stop-gap until we get get a unified update image like in #1002 

## Comments

### mutatrum on 2025-06-04

You mean somewhere in `www.bin`, so we can compare it against this one:

https://github.com/bitaxeorg/ESP-Miner/blob/f6c9276162ba52b8dcd26ced0c40e33195dda49e/main/http_server/http_server.c#L619

### skot on 2025-06-04

Yes.. the important part is that the version string is somewhere in www.bin so that it's very obvious when the two images don't match.
