# bitaxeorg/ESP-Miner issue #1841: [Bug] Fix access to WebUI via IPv6

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1841
> Collected: 2026-10-07
> Published: 2026-08-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1841
- State: open
- Author: ffrediani
- Opened: 2026-08-03
- Closed: n/a
- Labels: bug, enhancement, good first issue

## Description

Currently IPv6 works and ESP32 gets an address via SLAAC and is able to connect to a Pool with IPv6 support.

However when pointing to http using the IPv6 address shown in System menu with http://[2001:db8::1] it connects but doesn't display the page correctly. It only displays with IPv4-only IP address.

Since the web server responds there may be missing something else to be served in IPv6.

This is specially important in times where IPv4 has been scarse and broadband connections offer CGNAT + IPv6 address which can be used to remote control Bitaxes.

## Comments

### WantClue on 2026-08-03

Currently for the webui only ipv4 is implemented ipv6 is on the to-do list but hasn't been done yet. The only thing i did finish was that it can mine to ipv6 addresses
