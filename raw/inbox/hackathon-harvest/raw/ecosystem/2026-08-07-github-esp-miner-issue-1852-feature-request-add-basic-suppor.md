# bitaxeorg/ESP-Miner issue #1852: [Feature Request] - Add basic support for StartUp URL call for Dynamic DNS update

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1852
> Collected: 2026-10-07
> Published: 2026-08-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1852
- State: closed
- Author: ffrediani
- Opened: 2026-08-07
- Closed: 2026-08-09
- Labels: none

## Description

Currently the only way to know the public IPv4 address in front a Bitaxe in order to remote control it is to know it from the router which may have or not a DDNS function available.

When it is not possible to be done in the router, it may be desirable to have it on the Bitaxe itself, specially to know its own IPv6 address (as soon as #1841 is fixed) that becomes even more valuable for remote control without the need of VPN or anything similar.

This doesn't require install or implement anything on ESP-Miner and bloat the firmware. It only requires ESP-Miner to be able to call a URL once it gets IPv4 and IPv6 address.
For example in order to update Hurricane Electric DDNS record all you have to do is call a URL like the example: curl -6 "https://<domain.tld>:<password>@dyn.dns.he.net/nic/update?hostname=<domain.tld>"
This can be used for other similar DDNS services that have an API.

Further to that it is also necessary to have a watchdog mechanism that when the IP address change, due to router getting a new IPv4 or a new IPv6 Prefix Delegation from the ISP it can call the URL again to update it.
In systems like OpenWrt this is achieved with a cron that compares the resolved hostname IP address with the device's current IP address.

That preserves CPU cycles and network communication to very minimal.

## Comments

### WantClue on 2026-08-09

You should never assign a public ipv4 address or port forward devices to the internet.
And the bitaxe should not be used to call external services, only for local operation and connections to a stratum server. Thats it. 

### ffrediani on 2026-08-10

@WantClue you should not close a detailed and justified feature request like this just because of your personal opinion and lack of understanding on networking.
Having a public IPv4 (via port forward) or IPv6 directly on Bitaxe doesn't necessarily mean it is exposed to the whole internet. You may (and should) have firewall rules protecting it allowing access only from certain sources. This may be very necessary to remote control Bitaxes without the need of a VPN for example and it is valid as long enough protected with such ACL and aggregate control under the Swarm function.

Specially after IPv6 support for ESP-Miner having this feature able to call an URL for updating dynamic DNS can be the main usage for this feature **specially within a LAN environment**. Even for IPv4 it can also be for private IP addresses accessible via a VPN for those who prefer it.

This easy and light feature may be very useful for many users to improve management of several Bitaxes in a single panel and doesn't prevent remote access as is already possible by knowing the Bitaxe's literal IP address, and as such should not be simply closed because of lack of broader understanding on the various networking possibilities. It is not because the IP is public it means it is insecure.
