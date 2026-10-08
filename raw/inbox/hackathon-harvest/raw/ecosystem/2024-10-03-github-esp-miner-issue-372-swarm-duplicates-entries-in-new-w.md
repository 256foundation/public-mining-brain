# bitaxeorg/ESP-Miner issue #372: Swarm duplicates entries in new www.bin file

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/372
> Collected: 2026-10-07
> Published: 2024-10-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 372
- State: closed
- Author: Sledge0001
- Opened: 2024-10-03
- Closed: 2024-12-27
- Labels: bug, swarm

## Description

It seems after updating the the newest version of the www.bin files I am now seeing duplicates on the swarm page.

If I try to delete and add them back in it becomes 3 and it appears to have impacted all units swarm pages as well.

Is there a way to do a clean start and re-add all of the miners to the swarm page without getting duplicates?


## Comments

### MyOwn2C on 2024-10-03

Don't add to swarm with the IP where the swarm page is at.
Ie, don't add IP 192.168.0.10 to swarm page at 192.168.0.10
Add 192.168.0.10 to another swarm page (ie, 192.168.0.11). The swarm page at 192.168.0.10 will pick it up in a few seconds. 
Then both swarm pages at 192.168.0.10 and 192.168.0.11 will show the same without duplicates. 

### Sledge0001 on 2024-10-03

Just seems odd that the page wouldn't automatically look and pull out the dups.  Might also add a note on the swarm page alerting people not to add that "controlling" miner IP. As this is the first time I am personally hearing of it!


### skot on 2024-10-10

Is this a duplicate of #282 ?
