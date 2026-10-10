# bitaxeorg/ESP-Miner issue #1563: BitAxe does not check certificate expiration date for TLS connections

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1563
> Collected: 2026-10-07
> Published: 2026-02-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1563
- State: closed
- Author: mweinberg
- Opened: 2026-02-20
- Closed: 2026-05-28
- Labels: none

## Description

**Describe the bug**
The Bitaxe does not validate a certificate expiration date (presumably because it has no concept of time).  A miner can successfully connect to a TLS port of a pool regardless of certificate expiration date -- there is no warning or error when encountering an expired certificate.


**To Reproduce**
Connect to any stratum pool with a valid (but expired) certificate.  The TLS connection will work with no warnings or errors in the logs or in the UI.

**Expected behavior**
Ideally, the Bitaxe can understand current time such that it can validate certificate expiration date.

**Screenshots & Photos**

```
% echo | openssl s_client -servername public-pool.io -connect public-pool.io:4333 2>/dev/null | openssl x509 -noout -dates
notBefore=Nov 21 00:38:47 2025 GMT
notAfter=Feb 19 00:38:46 2026 GMT
```

**Hardware (please complete the following information):**
 - Bitaxe HW version: Bitaxe Gamma
 - Bitaxe HW vendor: SoloSathoshi
 - ESP-Miner FW version: v2.13.0b5
 - Hash Frequency: 
 - Voltage:
 - Pool URL, Port, User: public-pool.io:4333

**Additional context**
None

## Comments

### mutatrum on 2026-02-20

This is tricky, as there is no time source on the Bitaxe. Without that, we can only do expiration validation after connection and based on the ntime in the `mining.notify`, which comes from the same source, so that won't tell much.

Second issue is what action to take, if for whatever reason the certificate is expired? Disconnect seems rough, maybe show a warning on the dashboard and/or display?

### 0xdeadbeefnetwork on 2026-02-23

> This is tricky, as there is no time source on the Bitaxe. Without that, we can only do expiration validation after connection and based on the ntime in the `mining.notify`, which comes from the same source, so that won't tell much.
> 
> Second issue is what action to take, if for whatever reason the certificate is expired? Disconnect seems rough, maybe show a warning on the dashboard and/or display?

SNTP sync on boot + build-timestamp check as a fallback? maybe?

### WantClue on 2026-05-28

As we don't know the time and don't intent of connecting with a bitaxe to any other external service than the pool this can't be implemented without loosening our bonds. Therefore this is a NACK unless the majority of the community demands such a change. If so this issue will be reopend
