# bitaxeorg/ESP-Miner issue #79: Problems adding and deleting Bitaxes in the swarmfunction

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/79
> Collected: 2026-10-07
> Published: 2024-01-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 79
- State: closed
- Author: Patsch91
- Opened: 2024-01-09
- Closed: 2024-12-01
- Labels: bug

## Description

Had 6 Axes integrated in the swarm and deleting one of them from the list resulted in deleting every single one.
Now trying set up a new swarm i cannot add any of them back into it Tried to "start" adding them one by one on each of the OS but everytime i hit the "add" button nothing happens.

all on Version 2.0.5.

I will try if the same behaviour occurs when they are running  on 2.0.4

## Comments

### Patsch91 on 2024-01-09

Just adding another thing that occured couple times before while running on 2.0.4.:  in my case there were three different AxeOS open in one Browser and in one of them i hit the swarmfunction trying to get the three of them into one swarm.  I typed in the IP hit the add button and then the same IP was added three times to the swarm. Then i closed one of the three tabs and did the same thing... then the same IP was added twice to the swarm. So it looks like it gets in trouble while multiple Axes are connected at the same time? Maybe this helps improving the swarm function somehow 

### justinuhickey on 2024-01-10

I would like to add to this issue. I am running 2.0.5 on two BitAxe 201's. Since I do not have static IP's assigned to the bitaxe units, the router does change the IP's once in a while, if I reboot the units. This happened and I needed to update the SWARM setup for the units. I attempted to delete the old SWARM entries (with the invalid IP's) and the web portal freezes for a moment and then, it returns an error stating the entry cannot be deleted. The same error and behavior exists on both of my bitaxe units. At this time, I am unable to remove SWARM entries. I have attached an image that shows what is returned in the app.
![bitaxe_swarm_delete_error](https://github.com/skot/ESP-Miner/assets/142689262/0a263a38-d5c8-4cad-bc54-83677df056da)


### thalpius on 2024-02-07

I've had the same issue. I deleted the miners by clicking the remove button, copying the PATCH request and changing the invalid IP address to the IP address of the miner and send it again. Now the list is empty.

Maybe it will help others who wants a clear list before the fix 😊

### WantClue on 2024-12-01

Current swarm does not have any issues anylonger. Swarm has been reworked lately
