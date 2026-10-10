# bitaxeorg/ESP-Miner issue #111: Different best difficulty in AxeOs and the pool at version 2.0.7

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/111
> Collected: 2026-10-07
> Published: 2024-02-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 111
- State: closed
- Author: chillingbee
- Opened: 2024-02-21
- Closed: 2024-03-05
- Labels: none

## Description

There are different best difficultys in the AxeOs and the pool!
At ckpool my best dif. is about 8.19G and the AxeOs has about 4.29G

## Comments

### MyOwn2C on 2024-02-22

Normal.
Pool best diff is your all-time best, since day 1 that you connected to it.
AxeOS best diff is your session best. It resets after reset/power cycle. 

### skot on 2024-02-22

We have been saving best diff to NVM for a while now. I should persist across restarts. But I NVM can be reset when uploading a new firmware in some cases.

### 0x7a617a75 on 2024-02-25

I am seeing a very similar thing and the differences are pretty drastic. I haven't updated my firmware recently, and the best hash appeared well after my last upgrade.
Running 2.0.7 as well.

```
  {
   "workername": "X",
   "hashrate1m": "422G",
   "hashrate5m": "442G",
   "hashrate1hr": "506G",
   "hashrate1d": "469G",
   "hashrate7d": "461G",
   "lastshare": 1708830059,
   "shares": 414621980,
   "bestshare": 209250669786.6476,
   "bestever": 209250669786
  },
  ```
  and on the bitaxe
  ```
  Results
Hash Rate:	443.68 Gh/s
Efficiency:	35.09 W/Th
Best Difficulty:	4.29G
```

### chillingbee on 2024-02-25

> I am seeing a very similar thing and the differences are pretty drastic. I haven't updated my firmware recently, and the best hash appeared well after my last upgrade. Running 2.0.7 as well.
> 
> ```
>   {
>    "workername": "X",
>    "hashrate1m": "422G",
>    "hashrate5m": "442G",
>    "hashrate1hr": "506G",
>    "hashrate1d": "469G",
>    "hashrate7d": "461G",
>    "lastshare": 1708830059,
>    "shares": 414621980,
>    "bestshare": 209250669786.6476,
>    "bestever": 209250669786
>   },
> ```
> 
> and on the bitaxe
> 
> ```
> Results
> Hash Rate:	443.68 Gh/s
> Efficiency:	35.09 W/Th
> Best Difficulty:	4.29G
> ```

That´s funny and wierd! Two of my Bitaxe do have the exacly same difficulty of 4.29G

### weixiongmei on 2024-02-25

I have the same issue, the I had a best difficulty of 34.9G in pool, but only showing as 4.29G in the miner

### weixiongmei on 2024-02-25

Would like to have the session best difficulty rather than just the life time best difficulty in the Home page, because some of the pool doesn't shows the best difficulty...

### weixiongmei on 2024-02-27

Hi @skot,

```
/Volumes/SSD/Codes/ESP/ESP-Miner/components/bm1397/include/bm1397.h:14:38: warning: overflow in conversion from 'long long int' to 'int' changes value from '4294967296' to '0' [-Woverflow]
   14 | static const u_int64_t NONCE_SPACE = 4294967296;
```


### JWelsh97 on 2024-03-02

Yeah I have the same 4.29G best difficulty

### WantClue on 2024-03-05

> We have been saving best diff to NVM for a while now. I should persist across restarts. But I NVM can be reset when uploading a new firmware in some cases.
