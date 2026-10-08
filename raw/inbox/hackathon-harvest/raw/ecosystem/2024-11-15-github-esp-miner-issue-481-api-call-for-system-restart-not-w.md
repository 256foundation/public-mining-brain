# bitaxeorg/ESP-Miner issue #481: API call for system restart not working

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/481
> Collected: 2026-10-07
> Published: 2024-11-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 481
- State: closed
- Author: jrkalf
- Opened: 2024-11-15
- Closed: 2024-12-12
- Labels: none

## Description

Tested against version 2.3.0

The console call to restart AxeOS is working, but doing an API call with curl:
`# curl -X POST http://bitaxe_ip/api/system/restart` it fails with a empty reply from server and after that a connection reset by Peer on a second attempt. Net-result is an AxeOS that keeps running, not rebooting.

## Comments

### eandersson on 2024-11-15

I just tried on my 2.3.0 and it worked properly.
> curl -X POST http://192.168.3.103/api/system/restart
> System will restart shortly.

Can you add -v to your curl command to generate a bit more output?

### MyOwn2C on 2024-11-15

I can also confirm it works currently on 2.3.0.
Issue is likely on your side. 

### jrkalf on 2024-11-16

Thank you for the confirmation and guidance.
We tested with multiple people in our solo pool and all had the issue.
After 2 restarts of the esp-miner it did work for me. The machine was already running for 2 weeks without reboot. Perhaps it's only an issue when it's been on for an extensive period of time?

Will check again in two weeks.

```shell
╰─❯ curl -v -X POST http://192.168.x.x/api/system/restart
*   Trying 192.168.x.x:80...
* Connected to 192.168.x.x (192.168.x.x) port 80
> POST /api/system/restart HTTP/1.1
> Host: 192.168.x.x
> User-Agent: curl/8.7.1
> Accept: */*
> 
* Request completely sent off
< HTTP/1.1 200 OK
< Content-Type: text/html
< Content-Length: 28
< 
* Connection #0 to host 192.168.x.x left intact
System will restart shortly.%
```
