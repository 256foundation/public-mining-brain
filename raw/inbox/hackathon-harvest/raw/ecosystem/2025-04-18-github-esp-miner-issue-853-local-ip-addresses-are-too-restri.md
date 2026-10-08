# bitaxeorg/ESP-Miner issue #853: Local IP addresses are too restricted

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/853
> Collected: 2026-10-07
> Published: 2025-04-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 853
- State: closed
- Author: CryptoTech-Guy
- Opened: 2025-04-18
- Closed: 2025-04-18
- Labels: none

## Description

**Describe the bug**
http server checks is the IP of the client is in the local network, however it seems it allows or expects specific IP ranges.  My local network uses different ranges, hence I always get 401 unauthorized.
I see in the http server code it expects these specific ranges:
    // 10.0.0.0 - 10.255.255.255 (Class A)
    // 172.16.0.0 - 172.31.255.255 (Class B)
    // 192.168.0.0 - 192.168.255.255 (Class C)

**To Reproduce**
Steps to reproduce the behavior:
1. Go to <device local IP> when the local network is not in one of the above ranges, e.g. 20.0.0.x
2. UI is stuck on 'loading' and in the network response you'll see 'unauthorized'

![Image](https://github.com/user-attachments/assets/bf5b967c-ef77-441d-b793-2a8102dd4315)

**Expected behavior**
Server should allow any client in the local network as long as they share the same range.

**Hardware (please complete the following information):**
 - Bitaxe HW version: 601
 - Bitaxe HW vendor: 
 - ESP-Miner FW version: tested on 2.5.1, 2.6.1, 2.6.5 (all return 401)
 - Hash Frequency:
 - Voltage:
 - Pool URL, Port, User:

**Additional context**
Add any other context about the problem here.


## Comments

### skot on 2025-04-18

Yeah I guess badasses with phat CIDR blocks are going to have trouble here. And people with their local networks misconfigured.

### ghost on 2025-04-18

~That private network range is not commonly used either.~ 

Microsoft uses that IP range it seems, so not private anymore.

Reconfigure your local (internal) network...

![Image](https://github.com/user-attachments/assets/c0ed0a47-f660-4b2e-98c4-1e5163f59152)


### skot on 2025-04-18

> ~That private network range is not commonly used either.~ 
> 
> Microsoft uses that IP range it seems, so not private anymore.
> 
> Reconfigure your local (internal) network...
> 
> ![Image](https://github.com/user-attachments/assets/c0ed0a47-f660-4b2e-98c4-1e5163f59152)
> 

It is perfectly fine for an entity with a large block of IP addresses to use them internally. It's commonly done at OG tech companies.

AFAIK Bitaxe will not currently work on these networks.

### skot on 2025-04-18

we can track this in #821
