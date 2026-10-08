# bitaxeorg/ESP-Miner issue #829: Password for the web interface

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/829
> Collected: 2026-10-07
> Published: 2025-04-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 829
- State: closed
- Author: Uefi1
- Opened: 2025-04-08
- Closed: 2025-04-08
- Labels: none

## Description

Hello, this morning I woke up and discovered that almost all my settings were changed. Someone accessed the web interface somehow. Please add authentication to the ASIC's web interface.










## Comments

### MyOwn2C on 2025-04-08

You should secure your wifi network first. 

### Uefi1 on 2025-04-08

> You should secure your wifi network first.

My Wi-Fi network is secured, and no external access to other interfaces is possible.










### MyOwn2C on 2025-04-08


> My Wi-Fi network is secured, and no external access to other interfaces is possible.

1. If your WiFi is truly secure, you would not be posting this to begin with.
2. If your WiFi is indeed secure, then someone within your network is messing with the Bitaxe settings. No amount of web login/password will save you. You have an internal saboteur. 

Securing your WiFi is much easier and more effective than a web login/password page


### mdklapwijk on 2025-06-18

It would be an additional barrier/layer of security, for those situations where you find yourself with a compromised client in your network; e.g. a worm/rootkit/malware which automatically searches for esp-miners to change the address/stratum-user. Yes, if your network is compromised you have bigger issues, but password protection combined with a max attempt count would create some extra hurdles.

By the way, this reminds me an awful lot about the discussions about the storage of unencrypted, as in plain text, passwords in [Filezilla](https://www.bleepingcomputer.com/news/software/filezilla-ftp-client-adds-support-for-master-password-that-encrypts-your-logins/)...

### MrTakfly on 2026-07-26

> Securing your WiFi is much easier and more effective than a web login/password page

This is completely and utterly false in every sense of the word. I have written a PoC that exploits a non-public same-origin policy bypass vulnerability, scans the local network for BitAxe devices, and automatically changes the BTC address to an attacker controlled one. It is a relatively simple payload to deploy (it just needs to be embedded into a malicious webpage), and unless you are checking, the BTC address change goes easily unnoticed. If I wasn't a security researcher and governed by a code of ethics, I could probably use it to make a quick bit of money.
