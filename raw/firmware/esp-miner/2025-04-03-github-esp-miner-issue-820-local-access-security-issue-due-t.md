# bitaxeorg/ESP-Miner issue #820: Local access security issue due to HTTP CORS header

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/820
> Collected: 2026-10-07
> Published: 2025-04-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 820
- State: closed
- Author: seepv
- Opened: 2025-04-03
- Closed: 2025-04-17
- Labels: none

## Description

[Tasmota](https://tasmota.github.io) has disabled CORS / set CORS optional for security issues.

Why should CORS set active in ESP-Miner ?

PROBLEM DESCRIPTION

A clear and concise description of what the problem is.

`Tasmota has CORS HTTP headers enabled by default. This is a major security issue that could easily be exploited by any website with some simple Javascript, especially since Tasmota does not require a web password by default.`
[Source](https://github.com/arendst/Tasmota/issues/6767): https://github.com/arendst/Tasmota/issues/6767

and

`If you want to enable CORS, you can do it but it does causes some potential security issues that you need to be aware of.`
[Source](https://github.com/arendst/Tasmota/discussions/21540): https://github.com/arendst/Tasmota/discussions/21540


## Comments

### skot on 2025-04-14

I don't think this currently an issue with esp-miner; see the discussion in #821
