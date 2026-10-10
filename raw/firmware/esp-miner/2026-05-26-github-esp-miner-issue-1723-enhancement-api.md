# bitaxeorg/ESP-Miner issue #1723: Enhancement: API

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1723
> Collected: 2026-10-07
> Published: 2026-05-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1723
- State: closed
- Author: pjones112000
- Opened: 2026-05-26
- Closed: 2026-05-29
- Labels: none

## Description

I've noticed that the API supports useFallbackStratum, but, how do you force it to switch back to the Primary stratum?  Can you send the same command a second time to revert back to it?  If not, can a usePrimaryStratum be added?

## Comments

### mutatrum on 2026-05-27

Set `useFallbackStratum` to `0`, or does that not work? The value is 0/1.

### pjones112000 on 2026-05-29

Well, that's helpful to know...but, unfortunately, I cannot seem to get it to work with curl.  This is what I'm using:  curl -X PATCH http://<ip address>/api/system -H "Content-Type: application/json" -d '{ "useFallbackStratum": 1 }'  

or 0 to revert to primary?

Did I miss something?

Regardless, it doesn't seem to work and the logs don't record any activity and curl doesn't report anything.


### WantClue on 2026-05-29

to control the pools e.g. switch between them, you need to use the PATCH for chaning the useFallbackStratum and do a POST restart afterwards like this:
``` 
curl -X PATCH "http://10.0.10.183/api/system" -H "Content-Type:application/json" -d '{"useFallbackStratum":0}'
curl -X POST "http://10.0.10.183/api/system/restart"
```
