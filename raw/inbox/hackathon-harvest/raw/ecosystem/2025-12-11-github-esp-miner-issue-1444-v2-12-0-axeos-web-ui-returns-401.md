# bitaxeorg/ESP-Miner issue #1444: v2.12.0 AxeOS Web UI returns 401 Unauthorized on all PATCH requests (Gamma 601)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1444
> Collected: 2026-10-07
> Published: 2025-12-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1444
- State: closed
- Author: kdesch5000
- Opened: 2025-12-11
- Closed: 2025-12-24
- Labels: bug

## Description

**Hardware:** Bitaxe Gamma 601 (from Plebsource)
**Firmware:** v2.12.0 (clean install via web flasher)
**AxeOS:** v2.12.0

## Issue
Cannot save any settings via AxeOS web UI. All PATCH requests return 401 Unauthorized.

## What Works
- Viewing web UI (all GET requests work)
- API via curl: `curl -u ":bitaxe" -X PATCH ... ` returns 200 OK
- All monitoring and display functions

## What Doesn't Work
- Any "Save" button in web UI returns 401
- Applies to ALL settings pages
- Error persists across Chrome, Firefox, Edge
- Error persists in incognito mode
- Cache cleared, extensions disabled

## Evidence
```bash
# This works perfectly:
curl -v -u ":bitaxe" -X PATCH \
  -H "Content-Type: application/json" \
  -d '{"fanspeed": 100}' \
  http://192.168.86.69/api/system
# Returns: HTTP/1.1 200 OK

# But same request from browser returns 401
```

## Environment
- Browser: Chrome 131, Firefox, Edge (all tested)
- OS: Linux, Windows (both tested)
- Network: Home LAN, no proxy/firewall
- Installation: Clean install via bitaxeorg.github.io/bitaxe-web-flasher/

## Request
Web UI should send proper authentication headers on PATCH requests, matching what curl does successfully.


## Comments

### WantClue on 2025-12-21

Are you accessing the webUI via hostname or via the IP address? 

### kdesch5000 on 2025-12-21

Hostname

—
Kristian Desch
***@***.***
[M]: +1.773.251.1635
________________________________
From: WantClue ***@***.***>
Sent: Sunday, December 21, 2025 3:50:26 AM
To: bitaxeorg/ESP-Miner ***@***.***>
Cc: Kristian Desch ***@***.***>; Author ***@***.***>
Subject: Re: [bitaxeorg/ESP-Miner] v2.12.0 AxeOS Web UI returns 401 Unauthorized on all PATCH requests (Gamma 601) (Issue #1444)

[https://avatars.githubusercontent.com/u/86001033?s=20&v=4]WantClue left a comment (bitaxeorg/ESP-Miner#1444)<https://github.com/bitaxeorg/ESP-Miner/issues/1444#issuecomment-3678647148>

Are you accessing the webUI via hostname or via the IP address?

—
Reply to this email directly, view it on GitHub<https://github.com/bitaxeorg/ESP-Miner/issues/1444#issuecomment-3678647148>, or unsubscribe<https://github.com/notifications/unsubscribe-auth/ABMKQINVAU5J6UYL5MNEVOT4CZUOFAVCNFSM6AAAAACOZDHFXGVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTMNZYGY2DOMJUHA>.
You are receiving this because you authored the thread.Message ID: ***@***.***>


### WantClue on 2025-12-24

due to the cors policy we use it's currently not possible to perform these actions via hostname, only via ip address. This is been worked and and this issue will be closed because there is a fix in the pipeline for this
