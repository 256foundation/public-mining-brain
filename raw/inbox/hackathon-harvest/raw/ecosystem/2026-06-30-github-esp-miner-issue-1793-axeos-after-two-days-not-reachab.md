# bitaxeorg/ESP-Miner issue #1793: AxeOS after two days not reachable

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1793
> Collected: 2026-10-07
> Published: 2026-06-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1793
- State: open
- Author: mcdermit667
- Opened: 2026-06-30
- Closed: n/a
- Labels: none

## Description

Hi everyone. AxeOS becomes unreachable after about two days—often with the message "Unable to reach the device for X seconds." It continues running normally in the backend. I’ve tried different browsers. Access to the dashboard is only restored after a reboot or a Wi-Fi channel change.

Can anyone confirm this issue?

## Comments

### WantClue on 2026-06-30

Can you occasionally look into the logs and the system page? a couple hours apart and post that here? also are you leaving the browser tab open all the time ? 

### mcdermit667 on 2026-07-01

The browser tab remained open the entire time. Here is the first log file; I’ll upload the second one later. I noticed an `httpd_sock_err` on line 3,581,243.

The dashboard remained accessible the whole time.

[bitaxe-logs (1).txt](https://github.com/user-attachments/files/29546768/bitaxe-logs.1.txt)
[bitaxe-logs (2).txt](https://github.com/user-attachments/files/29553649/bitaxe-logs.2.txt)

### mcdermit667 on 2026-07-03

My Bitaxe is currently inaccessible via Hashlink or Hashwatcher.
I probably should have mentioned that it drops out there first. It’s still accessible in the browser for now, but it likely won’t be long before it goes down there, too.

[bitaxe-logs (3).txt](https://github.com/user-attachments/files/29640721/bitaxe-logs.3.txt)
[bitaxe-logs (4).txt](https://github.com/user-attachments/files/29640722/bitaxe-logs.4.txt)

### mcdermit667 on 2026-08-24

Unfortunately, the problem with v2.15.0 still persists.

[bitaxe-logs(7).txt](https://github.com/user-attachments/files/31364242/bitaxe-logs.7.txt)

### awi81 on 2026-09-24

This may be what you're hitting. I can reproduce this failure mode on a Gamma 601.

`sdkconfig.defaults` leaves `CONFIG_LWIP_MAX_ACTIVE_TCP` at the IDF default of 16, while `http_server.c` allows `max_open_sockets = 20` (both `master` and `v2.15.x`). httpd only purges its least-recently-used session once it reaches 20, but lwIP runs out of TCP PCBs at 16, and stratum holds one of them. After that, the listen PCB can't get a PCB for a new SYN and drops it, and `tcp_kill_prio()` won't evict connections of equal priority. So every new connection times out while the miner keeps hashing, and a stratum reconnect in that state would find no PCB either.

Clients that keep connections open (an open tab, API pollers, a Swarm page) can get it into that state. Anything that drops their connections clears it, which fits your observation that a reboot or a Wi-Fi change brings it back. Keepalive (#1913) only reaps clients that have vanished, not live ones.

Repro: open idle TCP connections to port 80 one at a time, and after each one try a fresh `GET /api/system/info`:

```
stock limits (16 PCBs)
idle=14  probe OK   in 0.09s
idle=15  probe FAIL in 5.01s  (timed out)
after 10 s hold: probe FAIL
closed 15 idle connections -> reachable again immediately, no reboot, shares kept counting

CONFIG_LWIP_MAX_ACTIVE_TCP=32, CONFIG_LWIP_MAX_SOCKETS=32
idle=20  probe OK   in 0.06s
idle=24  probe OK   in 0.04s
no failure up to 24 idle connections (httpd's LRU purge now does its job)
```

Fix in `sdkconfig.defaults`:

```
CONFIG_LWIP_MAX_SOCKETS=32      # 26 is exactly what's in use: 20 sessions + 3 httpd sockets + captive DNS + stratum + pool probe
CONFIG_LWIP_MAX_ACTIVE_TCP=32   # >= 20 sessions + 5 accept backlog + stratum + pool probe
```

With `MEMP_MEM_MALLOC=1`, the PCB limit is only a counter: PCBs are allocated when used. I tested this on a v2.15.0rc1-based build with the same lwIP and httpd settings as upstream. I can open a PR if that helps.
