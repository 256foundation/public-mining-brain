# bitaxeorg/ESP-Miner issue #1626: Add support of HTTPS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1626
> Collected: 2026-10-07
> Published: 2026-03-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1626
- State: closed
- Author: Kywalh
- Opened: 2026-03-22
- Closed: 2026-08-16
- Labels: none

## Description

Thanks for taking a look at this 👍

Just to clarify the intent a bit more:

The main concern is that when users expose their Bitaxe via port forwarding, everything is served over HTTP, so configuration data (including the wallet address) is visible in clear text.

I totally understand that adding full HTTPS support on ESP32 might not be trivial (resources, certificates, etc.), so this is not necessarily about pushing for a heavy implementation.

Maybe there are lighter or more pragmatic options, for example:
- documenting a recommended reverse proxy setup (nginx, caddy, etc.)
- avoiding anything that breaks HTTPS when used behind a proxy
- optionally protecting sensitive endpoints (config, wallet…) with a token or password
- or even making some endpoints disable-able when exposed externally

The main goal is simply to make remote access safer without overcomplicating the firmware.

Happy to test or help if needed 👍

## Comments

### mutatrum on 2026-03-22

This probably depends on #1240, as you can't have a certificate on IP address.

### Kywalh on 2026-03-23

> This probably depends on [#1240](https://github.com/bitaxeorg/ESP-Miner/pull/1240), as you can't have a certificate on IP address.

Are you sure ?

### mutatrum on 2026-03-23

> Are you sure ?

No 😆 But it would make it easier to have a self signed cert on hostname instead of IP.

### Kywalh on 2026-03-23

> > Are you sure ?
> 
> No 😆 But it would make it easier to have a self signed cert on hostname instead of IP.

I don't think so tbh because the main problème is that if you have access to any Bitaxe, you can change the settings, change the wallet, etc...

### mutatrum on 2026-03-23

> I don't think so tbh because the main problème is that if you have access to any Bitaxe, you can change the settings, change the wallet, etc...

That is the topic of many, many discussions and there's no consensus on if and/or how we would like to lock down the device, without running the risk of locking out non-technical users. It's a hard problem.

### NilByte on 2026-03-25

Run VPN on the bitaxe?

https://github.com/CamM2325/microlink

### WantClue on 2026-05-27

https has been discusses many times and there is no clear benefit of implementing it, rather there is a big concern about self signed certs and the overhead https brings with it. 

### crypro1 on 2026-06-10

- optionally protecting sensitive endpoints (config, wallet…) with a token or password

That was one thing I was thinking about too and would like to see implemented. Not everyone is living alone and to prevent someone to swap the wallet adress a password would be sufficent.

### mutatrum on 2026-06-10

See #1750. Not final yet.

### 0xf0xx0 on 2026-08-16

nack, the bitaxe is intended to be run on a private network. if you want external access i suggest tailscale, exposing your bitaxe on the public internet is *not* a good idea, if you really need to you should use a battle-tested proxy like nginx.

### crypro1 on 2026-08-23

private network can also include children , dormatory, shared flat and whatever. That's a little bit shortsighted for me.
