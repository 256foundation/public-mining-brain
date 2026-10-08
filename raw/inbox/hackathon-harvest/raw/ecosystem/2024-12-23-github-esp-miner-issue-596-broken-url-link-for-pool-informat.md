# bitaxeorg/ESP-Miner issue #596: Broken url link for Pool Information (Primary) URL for eusolo ckpool org

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/596
> Collected: 2026-10-07
> Published: 2024-12-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 596
- State: closed
- Author: TheMissingNTLDR
- Opened: 2024-12-23
- Closed: 2026-06-02
- Labels: none

## Description

Build: 2.4.2
Steps:
1. If you are on ck pool for Europe
2. Go to AxeOS website Dashboard > Pool Information (Primary) card at bottom
3. The URL for me is: [eusolo.ckpool.org](https://eusolostats.ckpool.org/users/${address})
4. where address is my btc wallet address
5. Click on Link - Gets 404 as the subdomain eusolostats is incorrect
6. Expected Result: The link should work with subdomain eusolo [eusolo.ckpool.org](https://eusolo.ckpool.org/users/${address})

May be it is caused by Line 233 in home.component.ts ?

## Comments

### mrv777 on 2025-01-10

https://eusolostats.ckpool.org/ should work

### mutatrum on 2026-06-02

Fixed with #847 / #861
