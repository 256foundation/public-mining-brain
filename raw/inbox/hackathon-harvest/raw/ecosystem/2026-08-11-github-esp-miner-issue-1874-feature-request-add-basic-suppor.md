# bitaxeorg/ESP-Miner issue #1874: [Feature Request] - Add basic support for StartUp URL call for Dynamic DNS update bis

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1874
> Collected: 2026-10-07
> Published: 2026-08-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1874
- State: open
- Author: ffrediani
- Opened: 2026-08-11
- Closed: n/a
- Labels: none

## Description

Currently the only way to know the IPv4 address in a Bitaxe in order to remote control it is to know it from the router which may have or not a DDNS function available.

When it is not possible to be done in the router, it may be desirable to have it on the Bitaxe itself, specially to know its own IPv6 address (as soon as #1841 is fixed) that becomes even more valuable for remote control without the need of VPN or anything similar.

This doesn't require install or implement anything on ESP-Miner and bloat the firmware. It only requires ESP-Miner to be able to call a URL once it gets IPv4 and IPv6 address.
For example in order to update Hurricane Electric DDNS record all you have to do is call a URL like the example: curl -6 "https://<domain.tld>:@dyn.dns.he.net/nic/update?hostname=<domain.tld>"
This can be used for other similar DDNS services that have an API.

Further to that it is also necessary to have a watchdog mechanism that when the IP address changes, due to router getting a new IPv4 or a new IPv6 Prefix Delegation from the ISP it can call the URL again to update it.
In systems like OpenWrt this is achieved with a cron that compares the resolved hostname IP address with the device's current IP address.

That preserves CPU cycles and network communication to very minimal.

**Considerations about Security**

This feature doesn't not necessarily imposes security risks to a Bitaxes it is perfectly possible (and should be done) to use ACL in the router to protect it and restrict access from only certain sources which can control it (ex: other Bitaxes in remote locations)
Having an IPv4 (via port forward) or IPv6 directly doesn't necessarily mean it is exposed to the whole internet.
This is very useful to remote control Bitaxes without the need of a VPN for example and it is valid as long enough protected with such ACL and aggregate control under the Swarm function.

Specially after full IPv6 support for ESP-Miner is completed, having this feature can be the main usage **specially within a LAN environment**. Even for private IPv4 it can also be used to be accessible via a VPN for those who prefer it.
