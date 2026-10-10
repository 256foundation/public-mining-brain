# bitaxeorg/ESP-Miner issue #689: Not disconnecting from zombie pools

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/689
> Collected: 2026-10-07
> Published: 2025-02-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 689
- State: closed
- Author: bestel74
- Opened: 2025-02-03
- Closed: 2025-02-15
- Labels: none

## Description

This is the second time I've woken up to find the bitaxe in a bad state:
- Power consumption is high (but normal)
- Temperature is high (but normal)
- The hashrate is still the same on the graph and no activity is detected by the pool

In the logs, here's what's happening:

    ₿ (32683094) bm1370Module: Job ID: 58, Core: 36/3, Ver: 1BBE6000
    ₿ (32683094) bm1370Module: Invalid job nonce found, 0x58
    ₿ (32684094) bm1370Module: Job ID: 58, Core: 93/5, Ver: 07F2A000
    ₿ (32684094) bm1370Module: Invalid job nonce found, 0x58
    ₿ (32684724) bm1370Module: Job ID: 58, Core: 45/12, Ver: 0F958000
    ₿ (32684724) bm1370Module: Invalid job nonce found, 0x58

The soft reboot of the bitaxe does not fix the problem, the bitaxe falls into "another issue" #588: 
- Mesuresd ASIC voltage = 0V
- Power = 5W (so nothing - just the firmware offset)
- ASIC regulator and temp are low 

To fix the problem, I have to hard reboot the bitaxe, maybe it's related to #588 but I'm not sure at all. 


My bitaxe has quite a lot of overclocking, I don't know if this could be the root cause (1.32V measured / 1100MHz). Temperatures are good, ASIC at 62°C and regulator at 92°C (a bit hot but should be ok).

I'm using public pool, I've just changed to ckpool (public pool has been down, and hashrate is bumping a lot these days, so maybe that's where it's coming from). I will report here if it change anything.
**Uptime of public pool was "4 hours" this morning, so maybe it's a pool related issue.**

If you have any ideas or if anyone had this before, please let me know!


## Comments

### MyOwn2C on 2025-02-03

All my Gamma do the same thing randomly. 
Only fix for now is cold restart. 
Many cases have been reported in #588. 
I tag to the same case if I see others reporting it from other platforms. 

### bestel74 on 2025-02-03

What's your pool? Because right now it's running OK on CKPool.
The update rate for public pools is really low these days, a fix is waiting (seen on X).

I think there's a bug in the firmware, but maybe it's triggered by a bad network or bad proxies... I don't know yet. I've kept the settings the same, the room temperature is stable. I'll report back if the same thing happen.

### skot on 2025-02-03

I had 6 bitaxes out of 7 that were on public-pool over the weekend fail like this. The hashrate on all was totally flatlined at some non-zero number.

### bestel74 on 2025-02-03

Maybe the firmware can be improved, but the main cause may be the pool. 12 hours without problem on CKPool.

    Invalid job nonce found

Does the firmware clear all jobID when disconnected from the pool?
I think the correct behavior should be to use the fallback pool.
And also, why it does not recover from a soft-reset?



### skot on 2025-02-03

I think what's happening here is the pool just stops sending work and the esp-miner job queue runs out. For some reason esp-miner isn't getting any indication that the pool is down.

### bestel74 on 2025-02-03

Maybe statum_task "while (1)" main task should handle something like that:

    char *line = NULL;
    uint_8 status = STRATUM_V1_receive_jsonrpc_line(GLOBAL_STATE->sock, line);
    if( status == JSONRPC_TIMEOUT )
    {
        ESP_LOGE(TAG, "Timeout when receiving JSON-RPC line, reconnecting...");
        stratum_close_connection(GLOBAL_STATE);
        break;
    }
    else if (!line)
    {
        ESP_LOGE(TAG, "Failed to receive JSON-RPC line, reconnecting...");
        stratum_close_connection(GLOBAL_STATE);
        break;
    }

STRATUM_V1_receive_jsonrpc_line should handle inside the Timeout, what's your thoughts on that?

### eandersson on 2025-02-03

> I think what's happening here is the pool just stops sending work and the esp-miner job queue runs out. For some reason esp-miner isn't getting any indication that the pool is down.

public-pool has a loadbalancer in front and as long as it's up our TCP Failover won't work. Not sure what lb he is using, but could add a health check so that the port is closed when all the backends are down.

### skot on 2025-02-03

I think we need a watchdog on stratum packets to kick TCP fail

### eandersson on 2025-02-03

> I think we need a watchdog on stratum packets to kick TCP fail

Yes - that as well, but in this case the TCP is up and healthy on both the client and the server (loadbalancer). There just isn't anything on the other end of the loadbalancer.

### skot on 2025-02-03

I think it's safe to trigger a reconnect if we haven't gotten _any_ packets from the stratum server in 10 minutes?

### eandersson on 2025-02-04

> I think it's safe to trigger a reconnect if we haven't gotten _any_ packets from the stratum server in 10 minutes?

Yep - but we would need some additional logic, as right now we reset the retry counter when we successfully establish a TCP connection, so the retry might just re-establish a connection to the loadbalancer (depending on how it is configured). In fact moving the retry counter further down is probably something we should do anyway, so that auth errors etc counts towards the overall health of the pool.

### eandersson on 2025-02-04

Something like this should work until we can implement proper stratrum aware healthchecks. https://github.com/skot/ESP-Miner/commit/856f0a463aa19cb40cec4cefd0a5cc57bbafa358

### benjamin-wilson on 2025-02-04

I would suggest a general watch dog task that monitors when the last share was sent and reset the system if it's been too long. This can not only catch networking hangups but things like the ASIC going unstable due to too high overclock. 

### eandersson on 2025-02-04

> I would suggest a general watch dog task that monitors when the last share was sent and reset the system if it's been too long. This can not only catch networking hangups but things like the ASIC going unstable due to too high overclock.

Well if a pool has a high difficulty that would cause a disconnect?

### benjamin-wilson on 2025-02-04

> > I would suggest a general watch dog task that monitors when the last share was sent and reset the system if it's been too long. This can not only catch networking hangups but things like the ASIC going unstable due to too high overclock.
> 
> Well if a pool has a high difficulty that would cause a disconnect?

That could be a problem, maybe we watch the last valid ASIC result also. 

### bestel74 on 2025-02-04

Could be a mix between sent shares, job received, and successful ASIC work completion with a large windows of 1h?

Maybe a new monitor task?

### skot on 2025-02-04

> Could be a mix between sent shares, job received, and successful ASIC work completion with a large windows of 1h?
> 
> Maybe a new monitor task?

With Datum solo mining the pool diff is the network diff (so I'm told) so I don't think we can timeout on sent shares.


### bestel74 on 2025-02-04

Happened again (uptime +/- 30h) on CKPool, here is the log:

    ₿ (105970148) stratum_task: rx: {"params":["xxxxxxxxxxxxxxxxxxxxxx",false],"id":null,"method":"mining.notify"}
    ₿ (105970268) create_jobs_task: New Work Dequeued 679d5e0200002a99
    ₿ (105999948) stratum_task: rx: {"params":["xxxxxxxxxxxxxxxxxxxxxx,false],"id":null,"method":"mining.notify"}
    ₿ (106000068) create_jobs_task: New Work Dequeued 679d5e0200002a9a

Soft reset does not fix.
I start again with a lower frequency, from 1100MHz to 1000MHz.

### skot on 2025-02-04

> Happened again (uptime +/- 30h) on CKPool, here is the log:
> 
> ```
> ₿ (105970148) stratum_task: rx: {"params":["xxxxxxxxxxxxxxxxxxxxxx",false],"id":null,"method":"mining.notify"}
> ₿ (105970268) create_jobs_task: New Work Dequeued 679d5e0200002a99
> ₿ (105999948) stratum_task: rx: {"params":["xxxxxxxxxxxxxxxxxxxxxx,false],"id":null,"method":"mining.notify"}
> ₿ (106000068) create_jobs_task: New Work Dequeued 679d5e0200002a9a
> ```
> 
> Soft reset does not fix. I start again with a lower frequency, from 1100MHz to 1000MHz.

this looks like #588 

### bestel74 on 2025-02-04

Maybe an ASIC instability problem not handled by the firmware?

Do you want me to close the ticket?

### benjamin-wilson on 2025-02-04

https://github.com/skot/ESP-Miner/pull/693/files thanks @eandersson. We should get this merged and tested
