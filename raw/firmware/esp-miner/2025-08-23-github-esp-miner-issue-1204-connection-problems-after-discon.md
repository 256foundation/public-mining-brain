# bitaxeorg/ESP-Miner issue #1204: Connection problems after disconnecting from the power supply

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1204
> Collected: 2026-10-07
> Published: 2025-08-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1204
- State: closed
- Author: Travetown
- Opened: 2025-08-23
- Closed: 2025-08-24
- Labels: question

## Description

After disconnecting the Bitaxe from the power supply, I was unable to get 2 of the 3 Bitaxe to work again.
The display showed that they were connected to my Wi-Fi, but the Bitaxe's own Wi-Fi was active and awaiting configuration. Even after repeatedly re-entering the Wi-Fi parameters, nothing changed.
Only restarting the router and the Bitaxe solved the problem.
Since one of the three reconnected to the pool without any problems, I assume it has something to do with the IP address. 
The one that continued to work has 192.168.1.52, and the ones that no longer connected had .54 and .55. 
The new IP after restarting the router are now sequentially .52 - .54 (which I have now assigned permanently).

Bitaxe Gamma 602 Firmware 2.9.0 

Addendum:
I probably could have solved it with the reset button.
But it would still be nice if this could happen automatically. 

One more addition:
Now that the same problem has occurred with a permanently assigned IP address, I'm out of ideas. 
However, I could see that a Bitaxe was marked as active with its IP address. Nevertheless, the error described above still occurred. 
Therefore, I suspect it is a connection problem with the pool (CK). If it occurs again, I will try to save a log via USB.


## Comments

### Travetown on 2025-08-24

I was able to identify the problem. It was due to an incorrect repeater setting.
