# bitaxeorg/ESP-Miner issue #154: Swarm "Restart" for other devices does not work

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/154
> Collected: 2026-10-07
> Published: 2024-03-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 154
- State: closed
- Author: HypeLaser
- Opened: 2024-03-28
- Closed: 2024-12-27
- Labels: bug, swarm

## Description

Clicking on the "Restart" button for other devices on the Swarm page does not restart those devices. For example, if there are several devices and they all have their own IP address and they're all displaying on the swarm page, the only device that reboots is the IP address of the one you are on.

To reproduce: Connect several BitAxe devices on the same network. Choose one of them, and go to its IP address. For example 192.168.1.10 and then click on "Swarm" on the left hand side. Add the other IP addresses of other devices so they all show up on the Swarm page. You can then click the "Restart" button for devices of different IP addresses. But, the only device that reboots is the device on the IP address you are currently looking at. Even if you click a different order, so that you try to restart the other devices before the one you are currently on. The only way to restart the devices is to click Restart on each individual IP address via their own pages.

The expected behaviour is that the separate devices would restart, and the data would update to show the Uptime and Accepted values reset to zero.

In the image below I am on IP address of the first device ending 121. I click "Restart" for device ending 124, then 123, then 122, and finally I Restart the device I am connected to on 121. However, when I refresh the webpage, the only device that has restarted is device ending 121, as shown in the second image, as the Uptime and Accepted values have not changed for the other devices.

![Screenshot 2024-03-28 at 17 50 38](https://github.com/skot/ESP-Miner/assets/110939572/9d5e21c1-1bf0-404c-a117-15c950afbd35)

![Screenshot 2024-03-28 at 17 56 44](https://github.com/skot/ESP-Miner/assets/110939572/a936ede5-e6d8-45b8-84cf-f464046b556c)

I am using 1x BitAxe 204, and 3x BitAxe 401. They are all on firmware 2.1.3. They are all set to Defaults for voltage and hash frequency.
