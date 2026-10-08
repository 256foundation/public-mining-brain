# bitaxeorg/ESP-Miner issue #160: Under version V2.1.3, the best difficulty cannot be displayed properly.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/160
> Collected: 2026-10-07
> Published: 2024-04-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 160
- State: closed
- Author: kakawlala
- Opened: 2024-04-06
- Closed: 2024-04-07
- Labels: bug

## Description

I am under version V2.1.3 and got 5.78G again today.  It can display normally at the moment, but after restarting, it still records the upper limit of 4.29G.  It seems it's still unresolved.

![Screenshot_20240406-185835_Chrome](https://github.com/skot/ESP-Miner/assets/89348834/eeb09b88-f674-48e0-a3b8-ba5c4f7087b7)




![Screenshot_20240406-185922_Chrome](https://github.com/skot/ESP-Miner/assets/89348834/6c8c3de1-029c-4812-ace9-c17d23155fb5)




![P_20240406_190919](https://github.com/skot/ESP-Miner/assets/89348834/5082e584-f113-4faf-a8bc-d7edbb4bc230)







## Comments

### skot on 2024-04-06

Okay, it looks like we're truncating the saved nvm value. Thanks for reporting this!

### benjamin-wilson on 2024-04-07

This was fixed a few days ago, needs to be published.
https://github.com/skot/ESP-Miner/commit/6283a68d4ba7cf406ad570917a62a5bdd47b1395
