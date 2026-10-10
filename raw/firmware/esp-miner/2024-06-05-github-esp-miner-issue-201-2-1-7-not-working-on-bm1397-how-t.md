# bitaxeorg/ESP-Miner issue #201: 2.1.7 not working on BM1397. How to revert to old firmware?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/201
> Collected: 2026-10-07
> Published: 2024-06-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 201
- State: closed
- Author: f1uxx1337
- Opened: 2024-06-05
- Closed: 2024-08-04
- Labels: none

## Description

Is there a way to revert back to old firmware? BM1397 working with the 2.1.7 update.

Zero hashrate and no shares accepted or rejected. Miner has been working for months up until this version.

Thanks

## Comments

### CoanLuciano on 2024-06-05

Just download esp-miner.bin from 2.1.6 release and update using settings page.
I presume that you have access to your AxeOs.
I did it like this and it worked for me.

### pixeldoc2000 on 2024-06-05

Please post any Errors from your Logs **before** reverting to an older Firmware Version, otherwise there is no way to fix potential issues.

Open Webinterface (AxeOS) with your Browser -> Logs -> Show Logs

Maybe there are some Error Messages about DNS Resolution in the Logs?
```
₿ (18824034) stratum_task: Socket unable to connect to pool.example.org:3333 (errno 113)
₿ (18829034) stratum_task: Socket created, connecting to 0.0.0.0:3333
```

### pixeldoc2000 on 2024-06-05

> Just download esp-miner.bin from 2.1.6 release and update using settings page. I presume that you have access to your AxeOs. I did it like this and it worked for me.

To be on the safe side, **always** update / downgrade the corresponding `www.bin` file for the release, too!

### paulscode on 2024-06-09

I saw the same on both versions 2.1.7 and 2.1.8.  The hash rate remained at 0, and in the log message "bm1397Module: return null" appeared.  Downgrading to 2.1.6 (with www.bin from 2.1.5 since there isn't one on 2.1.6 release page) fixed the issue.  For reference, the log message appears to be from here: https://github.com/skot/ESP-Miner/blob/92924f72c6f4e28276fcf902429658c575ac2819/components/bm1397/bm1397.c#L413

Looks like there are three conditions where the BM1397_receive_work() function can return null.  Since there was none of the other messages proceeding the "bm1397Module: return null" message, the condition being matched in this case appears to be the second one (where received == 0):
https://github.com/skot/ESP-Miner/blob/92924f72c6f4e28276fcf902429658c575ac2819/components/bm1397/bm1397.c#L390

Screenshot of the log message attached.
![bitaxe_logs](https://github.com/skot/ESP-Miner/assets/499600/c2df88c8-68c0-48fc-8d35-b7fff458e911)


### yanir99 on 2024-06-12

I've also tried 2.1.7 and 2.1.8 on my BM1397 Bitaxe but they are not working :/
Last version working is 2.1.6.
@skot I'm not sure which changes were made that could have cause this, but I suggest that until solved perhaps add a message in the release notes for 2.1.8 also that it doesn't work with BM1397 🤷 


### chenyang2151 on 2024-06-17

rollback to 2.1.3 or before version ？hi，skot！

### mimi59 on 2024-06-26

Last operational release for me is 2.1.6. Both 2.1.7 and 8 did not produce any shares.

### skot on 2024-06-26

I broke it in 2.1.8 😬 Fix is coming in 2.1.9

### CoanLuciano on 2024-08-03

I did the update to 2.1.9 and it's working with public pool.
