# bitaxeorg/ESP-Miner issue #215: Lost IP connection leads to strange behaviour

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/215
> Collected: 2026-10-07
> Published: 2024-06-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 215
- State: closed
- Author: adadnc
- Opened: 2024-06-11
- Closed: 2024-12-01
- Labels: bug

## Description

**Describe the bug**
I've switched of the WAN interface on my router and left the Miner without internet, after a few minutes I switched on the WAN interface back on and the miner logs just showed the below entry.

`(146932671) http_server: Handshake done, the new connection was opened`

The AxeOS main page was showing constantly the same hash rate and the log output only the above entry. 


**To Reproduce**
Steps to reproduce the behavior:
1. Switch off internet connection on your router
2. Switch back on internet connection
3. Check AxeOS


**Expected behavior**
After loosing internet connection the miner establishes a new connection to the pool.

**Hardware (please complete the following information):**
 - Bitaxe HW version: Supra (PCB showing 400, UI showing 401)
 - Bitaxe HW vendor: D-Central
 - ESP-Miner FW version: 2.1.8
 - Hash Frequency: 525
 - Voltage: 1250
 - Pool URL, Port, User: ckpool



## Comments

### skot on 2024-06-11

Can you try reloading your browser when the internet comes back up?

### adadnc on 2024-06-11

I did try to reload the browser, but the above log entry comes again and stays. What wonders me was the same hash rate staying and the diagram drawing a straight line.

### adadnc on 2024-06-11

It the German section of bitcointalk.org there is a short discussion where user 5tift reports of regular reboot whenever his Internet is disconnected. In his case the disconnect happens at 03:00am when the DSL forces an IP change.

His comment is here https://bitcointalk.org/index.php?topic=5477020.msg64198559#msg64198559 and some posts above there is a screenshot of his data trace too.  

### skot on 2024-06-11

adding @Georges760 and @BitMaker-hub

### adadnc on 2024-07-31

This problem is really annoying and leads to devices stuck over night. Is there a chance someone could have a look into it.

### skot on 2024-07-31

Is the IP change associated with the DHCP lease expiring? Or what is the mechanism by which the router notifies the clients to change IP? We need to not only fix this but figure out how to reproduce it.

### adadnc on 2024-07-31

Indeed, it might be related to the lease time of DHCP, which has a 24h default value. I've asked one of the bitcointalk user who is suffering from this problem and does not have a forced IP change from his DSL operator.



### skot on 2024-07-31

OK, I'll see if I can reproduce on my end. We might have a fix for this already.

### knockoph on 2024-08-09

I have a similar problem. My router drops and reestablishes the internet connection automatically every night at 4 AM to get a new public (dynamic) IP from the ISP. I can see on public-pool, that from that point on, the bitaxe is dead, because it does not submit shares anymore and only recovers after manually restarting it.

In my understanding this is not about the bitaxe device itself receiving a new IP via DHCP inside the home network (using NAT), but the WAN connection resetting to receive a new public IP from the ISP.

Just a guess: does the Bitaxe use a long ~~keep-alive HTTP~~ connection to the pool, ~~maybe using a websocket~~? If that is the case it should somehow recognize / handle the sudden connection drop and establish a new ~~HTTP~~ connection to the pool.

Edit: had a look at the code: not a keep-alive HTTP connection to the pool, but an RPC connection.

Bitaxe Ultra 204, Firmware 2.1.9

### adadnc on 2024-08-20

The reporter of this problem in the bitcointalk-forum wrote, that the problem is solved. 

### knockoph on 2024-08-22

I updated to 2.1.10 two days ago and can confirm that the Bitaxe now recovers from the nightly internet connection reset of my router.

Thanks everyone for working on this!

### adadnc on 2024-08-24

I had to swap one of my access points from which my Bitaxe Supra is getting it's DHCP package and received it's IP without any problems after installing a new access point. The device has now an uptime of one week with 2.1.10 on board 401.

### WantClue on 2024-12-01

Should be resolved with #320
