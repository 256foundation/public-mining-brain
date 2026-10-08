# bitaxeorg/ESP-Miner issue #1464: [2.13.0b1] ipv6 link-local and resolution broken

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1464
> Collected: 2026-10-07
> Published: 2025-12-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1464
- State: closed
- Author: 0xf0xx0
- Opened: 2025-12-18
- Closed: 2025-12-24
- Labels: none

## Description

**Describe the bug**
Ipv6 link-local connections fail, and dns resolution prefers ipv4.

**To Reproduce**
Steps to reproduce the behavior:
1. Run v2.13.0b1
2. Open the logs
3. Connect to an ipv6 pool, either atlaspool.io or on your lan
4. See error in logs

link-local:
```
I (16072) stratum_task: Opening connection to pool: fe80::9a48:27ff:fe60:d3a1:5661
I (16072) stratum_task: Starting heartbeat thread for primary pool: fe80::9a48:27ff:fe60:d3a1:5661
# falls back here
I (16081) stratum_task: Connecting to: stratum+tcp://10.42.0.1:5661 (10.42.0.1)
I (16098) stratum_api: TLS disabled, Using TCP transport
I (16104) stratum_task: Transport initialized, connecting to 10.42.0.1:5661
# ...stratum chatter...
I (26091) stratum_task: Link-local IPv6 address detected, scope_id: 0
W (26092) stratum_task: Warning: Link-local IPv6 without scope ID - attempting to set from WIFI_STA_DEF
I (26100) stratum_task: Set scope_id to interface index: 2
I (26104) stratum_api: TLS disabled, Using TCP transport
E (26111) esp-tls: [sock=43] connect() error: Host is unreachable
E (26117) transport_base: Failed to open a new connection: 32772
```

dns resolution seems to prefer ipv4 as well, connecting to atlaspool will always use the ipv4.

**Hardware:**
 - Bitaxe HW version: Gamma 601
 - ESP-Miner FW version: v2.13.0b1

**Additional context**
Add any other context about the problem here.


## Comments

### mweinberg on 2025-12-19

I believe I know the issue with v6 DNS resolution, but I can't test at the moment as I'm away on a trip.  

I *think* the issue is that this line is missing from sdkconfig.defaults:

`CONFIG_LWIP_USE_ESP_GETADDRINFO=y`

I believe that this is needed to do v6 DNS resolution too.  My theory is that the miner is not attempting to get AAAA records... hence, it won't connect via v6 and "prefers" v4.

Per the documentation:
```CONFIG_LWIP_USE_ESP_GETADDRINFO[](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/kconfig-reference.html#config-lwip-use-esp-getaddrinfo)

Enable esp_getaddrinfo() instead of lwip_getaddrinfo()

Found in: [Component config](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/kconfig-reference.html#component-config) > [LWIP](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/kconfig-reference.html#component-config-lwip) > [DNS](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/api-reference/kconfig-reference.html#component-config-lwip-dns)

Use esp_getaddrinfo() for DNS lookups instead of lwip_getaddrinfo(). This function correctly handles the AF_UNSPEC flag for resolving both IPv4 and IPv6 addresses. Available only when both IPv4 and IPv6 are enabled.

Default value:
No (disabled)
```


Can anyone add this line to sdkconfig.defaults, recompile, and test again from a v6-enabled miner?  Fingers crossed.

### WantClue on 2025-12-19

The IPv4 preferred way is correct and not an issue. The vast majority of people will not have IPv6 hence IPv4 needs to be preferred.

I'll look into the resolution 

### mweinberg on 2025-12-19

If my theory is correct, then v6 DNS resolution won't *ever* work until this config change is made.  I'm not sure if the v6 DNS resolution issue described by @0xf0xx0 impacted them only... or if it's a universal issue with ESP-Miner.

### mutatrum on 2025-12-21

It seems with `CONFIG_LWIP_USE_ESP_GETADDRINFO` enabled the function `esp_getaddrinfo` will return both resolved addresses if they are available, so we can choose which one to prefer in the firmware.
