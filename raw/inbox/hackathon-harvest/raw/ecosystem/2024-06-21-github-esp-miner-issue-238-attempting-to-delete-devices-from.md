# bitaxeorg/ESP-Miner issue #238: Attempting to delete devices from swarm from web UI that no longer exist fails

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/238
> Collected: 2026-10-07
> Published: 2024-06-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 238
- State: closed
- Author: rickyboone
- Opened: 2024-06-21
- Closed: 2024-08-19
- Labels: none

## Description

**Describe the bug**
I had set up swarm between two bitaxe supra's a few weeks back, but ran into an unrelated issue that caused the IPs for the miners to change.  Both devices would show their respective old IPs in the swarm page of the AxeOS web UI, but if I attempted to delete either IP from either device, it would fail.  Looking at the request in the browser's dev tools, it was trying to send a modified json list of IPs to the "down" IPs, and never to the current one I was accessing.  Manually sending the PATCH request using curl only to the new IPs, in my case with an empty json list, cleared the old devices.

**To Reproduce**
Steps to reproduce the behavior:
1. Have 2+ bitaxe devices in a working swarm
2. Do something that causes any/all of the device IPs to change
3. Attempt to delete old IP from swarm page

**Expected behavior**
I would expect that the API request would be attempted to all devices that the miner being managed is aware of, however I never see a request to the "current" IP of the miner.  Perhaps a fail-safe when this condition is met would be to warn the user, and give an option to send the request to the current IP, but the other device(s) would need the same process run as well.

**Hardware (please complete the following information):**
 - Bitaxe HW version: Supra 401
 - Bitaxe HW vendor: Bitcoin Merch
 - ESP-Miner FW version: 2.1.3, 2.1.8
 - Hash Frequency: default
 - Voltage: default
 - Pool URL, Port, User: n/a

**Additional context**
Example curl request to send an empty list to one of the devices:
`curl 'http://10.9.8.7/api/swarm' -X 'PATCH' -H 'Content-Type: application/json' --data-raw '[]'`

## Comments

### WantClue on 2024-08-19

WIP with Issue #282
