# bitaxeorg/ESP-Miner issue #329: A pool DNS record won't work if it has a zero in one of its IP octets (e.g. 51.81.0.15)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/329
> Collected: 2026-10-07
> Published: 2024-09-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 329
- State: closed
- Author: eandersson
- Opened: 2024-09-07
- Closed: 2024-09-08
- Labels: none

## Description

The current DNS code checks if we have one or more zeros in the IP octets (e.g. 51.81.0.15) and if so fails. Having one or more zero in the IP octets is perfectly valid. This means that any pool that either already has a zero in their IP octet, or in the future change IP is at risk at stop working for all ESP-Miner devices.
```
        if (ip4_addr1(&ip4addr) != 0 && ip4_addr2(&ip4addr) != 0 && 
            ip4_addr3(&ip4addr) != 0 && ip4_addr4(&ip4addr) != 0) {
            ESP_LOGI(TAG, "IP found : %d.%d.%d.%d",ip4_addr1(&ip4addr),ip4_addr2(&ip4addr),ip4_addr3(&ip4addr),ip4_addr4(&ip4addr));
            ip_Addr = *ipaddr;
         }
```
