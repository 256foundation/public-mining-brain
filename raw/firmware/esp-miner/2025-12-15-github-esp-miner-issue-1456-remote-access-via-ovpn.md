# bitaxeorg/ESP-Miner issue #1456: Remote access via OVPN

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1456
> Collected: 2026-10-07
> Published: 2025-12-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1456
- State: closed
- Author: Painerman
- Opened: 2025-12-15
- Closed: 2025-12-17
- Labels: none

## Description

All my devices are managed remotely when I integrate the remote network with my own using OVPN. This software is partially accessible; I can see the menu and almost the entire web interface, except for the data coming from the device. The "waiter" in the center of the screen spins endlessly, and this happens on all menu pages except those that don't show data coming from the device.
To connect to this device, I have to connect to the server via RDP additionally. I can only assume that the VPN doesn't support all protocols or ports, but also that the device's web interface uses non-standard data transfer methods.

esp-miner-factory-lv07A-v2.12.0-1.12.2


## Comments

### Painerman on 2025-12-15

As far as I understand, this software was derived from yours by adding compatibility with other similar devices, but the bugs were originally yours, so I was advised to contact you directly. Those who work on expanding compatibility won't fix every new version you publish with the same errors!

### mutatrum on 2025-12-15

All traffic is normal http and websocket traffic. However, it can only originate from local IP ranges. Is the VPN using a custom IP range?

### luisschwab on 2025-12-15

This seems like a issue with your VPN configuration. I can do what you report when connected over Wireguard and Tailscale.

### Painerman on 2025-12-15

OVPN creates a bridge between two networks. Its unique feature is that it's a secure, low-cost or free option, and OVPN doesn't use GRE protocol like other VPN services. I don't rule out that the server settings block certain ports or protocols, but data from the ASIC isn't downloaded; it only displays a bare web interface with no data.

### mutatrum on 2025-12-15

The API is protected by CORS headers and local subnet limits, the static content isn't. Can you share the local ips it's using, for both the browser as well as the Bitaxe?

### Painerman on 2025-12-16

I don't fully understand what you mean. The subnet of the machine managing Bitaxe (dynamic IP) and Bitaxe's subnet (10.10.10.220) are different. But when I connect to the remote server via RDP, the subnet is the same. Are you suggesting that the access is blocked because of the subnet difference?
For some reason, I think if I create a 10.10.10... subnet at home, it still won't work. They'll be the same, but my subnet won't be local to the subnet where the miner is connected.

### mutatrum on 2025-12-16

Local IP ranges should be ok, both sides needs to be in one of these (not necessarily the same, IINM):

- 10.0.0.0/8 IP addresses: 10.0.0.0 – 10.255.255.255
- 172.16.0.0/12 IP addresses: 172.16.0.0 – 172.31.255.255
- 192.168.0.0/16 IP addresses: 192.168.0.0 – 192.168.255.255

Can you see if there are errors in the logs when you try to open the dashboard over vpn?

### Painerman on 2025-12-18

Right now my IP is: 92.36.15.68. It changes all the time, this is the LTE IP. The VPN isn't logging traffic, maybe on the server side, but I don't have access. Thanks for trying to help! I really appreciate it!
