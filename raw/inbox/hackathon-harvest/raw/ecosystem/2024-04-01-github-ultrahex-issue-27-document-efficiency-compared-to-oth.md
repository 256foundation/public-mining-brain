# bitaxeorg/ultraHex issue #27: Document efficiency compared to other ASICs

> Source: https://github.com/bitaxeorg/ultraHex/issues/27
> Collected: 2026-10-07
> Published: 2024-04-01

- Repository: bitaxeorg/ultraHex
- Type: issue
- Number: 27
- State: closed
- Author: brandonros
- Opened: 2024-04-01
- Closed: 2024-06-09
- Labels: none

## Description

I don't think this is fully accurate but I wonder if something like this could be added to the README to help users understand how this ranks compared to other ASICs:

![image](https://github.com/skot/bitaxeHex/assets/8949910/39d835a2-9c63-4729-9b2c-9772bfcd8ece)

The bitaxeHex actually seems super efficiency from a watts/terrahash perspective if it truly can hit 3.0TH/s on 50w power consumption at the wall.

I'm not sure if the $250 estiamte to build one is accurate with power supply.

My next question would be, if it really is $250 for 3.0 TH/s, what could be done to make it more efficent from a "cost input -> hash output" perspective? What would it take to support more then 6 BM1366 on a single board? Are there currently plans to support more?

## Comments

### skot on 2024-04-01

There are several other factors to consider when calculating the total $/TH/s. For example, the Compac-F requires a separate controller. All of those big industrial miners require industrial power, and likely something to mitigate the heat and noise.

### brandonros on 2024-04-01

Worded another way: why did you pick 6 ASICs on the board instead of 12 for example? What constraints were you up against? Could the "total $/TH/s" be improved significantly by simply copy and pasting/upsizing the schematic? Obviously not I'm sure.

What does a schematic that can do 12, 24, 48, 96 look like? Just for fun obviously :D

### Tyberyus on 2024-04-01

When i was Reviewing the scematic i was wondering if it would be possible to put 10 bm1366 in series. If we run them at 1.2V each. Than we could get rid of the step down Part. At least for 12v Systems. But would need 7 times more lvl shifters and some kind of fixed 12v supply. Luckily there are a lot of 12V 10A modules out there. 

### macphyter on 2024-05-13

> When i was Reviewing the scematic i was wondering if it would be possible to put 10 bm1366 in series. If we run them at 1.2V each. Than we could get rid of the step down Part. At least for 12v Systems. But would need 7 times more lvl shifters and some kind of fixed 12v supply. Luckily there are a lot of 12V 10A modules out there.

Came across your comment while scrubbing issues.  This approach has been considered, but we didn't go that route for 2 reasons:
1- This was the first open source board to run multiple ASICs, and ASICs are expensive.  We didn't want to jump right into a board with lots of ASICs right away until we got some more understanding around how to run multiple ASICs.
2- Most 12V supplies are not exactly 12.0V, they tend to be close by 5% or so.  This means we wouldn't have exactly 1.2V per domain.  Also, we like having some fine control over the core voltage to provide for overclocking and rate tuning.  With an external 12V supply we don't have an easy way to control the core voltage level.

Since the time the Hex was created, there have been other projects crop up that take several different approaches to core voltage supply.  Eventually there will be someone who tries this, and it might turn out to be very effective.


### macphyter on 2024-06-09

I don't see any immediate action items here, so I'm closing this issue.
