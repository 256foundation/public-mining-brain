# bitaxeorg/ESP-Miner issue #159: No more correct results after a few hours | We need Auto Reboot! (Solution: Board Version: 0.11 and 204. These with 0.11 do not work.)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/159
> Collected: 2026-10-07
> Published: 2024-04-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 159
- State: closed
- Author: unclasp
- Opened: 2024-04-04
- Closed: 2024-04-07
- Labels: none

## Description

After a few hours I no longer get any results. Hashrate remains constant. Excerpt from the log follows...

## Comments

### MyOwn2C on 2024-04-04

What does the log say? Constant hash rate is not necessary an issue


### unclasp on 2024-04-05

Here you can clearly see how someone gets sick. Hach rate remains the same, varies. No results.

<img width="633" alt="111" src="https://github.com/skot/ESP-Miner/assets/36558895/813aa19d-eba1-4949-9d54-657746b8679d">

LOG:
₿ (3289439) create_jobs_task: New Work Dequeued 1e3de8
₿ (3349019) stratum_task: rx: {"id":null,"method":"mining.notify","params":["1e4263","295187c5df29c400f5a7379208441249bfba73990001c9fb0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703eec80c5075626c69632d506f6f6c","ffffffff02fc08a125000000001976a9145393eac07f91185fb220163b68b37c0253e3d6fd88ac0000000000000000266a24aa21a9edf7f5aa4d42c89bfcbabb951f76981900cce343597883cbc1d9fe8bdbcfd3d76300000000",["29c3b783d68406108dcf3b1339b8567f255e1ed81775891636814da48e0a89ce","7a25fb95546374556a56fc3efc1a00ea711e1c13eb55dd3552423d4b9bdbe8c1","ecb7fd28056d66e3ad8721c8cc9ba0fa167ba6f5fe591737a46efbcccf5fbd6f","3b441a7cf7442c85b18b238ad13e165a4672f9a30d1ea02570e7cf001964d3c6","adb1c6144875f018a1e1f0ab5193ac663454ed0706a816962ee8ae06507ff326","4b81a027889cb6bf50dfdececbaa2094e9a426388bd051aafdbf7f74b3c81516","2f22b25e2ed293f2d2bc7e778c56820aab735e56ec87953feb8c933484ab2568","8ac9b09bb5b5c21237789b215bdb494b58e804446f8b70d968ea16c4f8d843ca"],"20000000","170362d3","66104db1",false]}
₿ (3351209) create_jobs_task: New Work Dequeued 1e4263
₿ (3409339) stratum_task: rx: {"id":null,"method":"mining.notify","params":["1e46e0","295187c5df29c400f5a7379208441249bfba73990001c9fb0000000000000000","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff1703eec80c5075626c69632d506f6f6c","ffffffff02fc08a125000000001976a9145393eac07f91185fb220163b68b37c0253e3d6fd88ac0000000000000000266a24aa21a9edf7f5aa4d42c89bfcbabb951f76981900cce343597883cbc1d9fe8bdbcfd3d76300000000",["29c3b783d68406108dcf3b1339b8567f255e1ed81775891636814da48e0a89ce","7a25fb95546374556a56fc3efc1a00ea711e1c13eb55dd3552423d4b9bdbe8c1","ecb7fd28056d66e3ad8721c8cc9ba0fa167ba6f5fe591737a46efbcccf5fbd6f","3b441a7cf7442c85b18b238ad13e165a4672f9a30d1ea02570e7cf001964d3c6","adb1c6144875f018a1e1f0ab5193ac663454ed0706a816962ee8ae06507ff326","4b81a027889cb6bf50dfdececbaa2094e9a426388bd051aafdbf7f74b3c81516","2f22b25e2ed293f2d2bc7e778c56820aab735e56ec87953feb8c933484ab2568","8ac9b09bb5b5c21237789b215bdb494b58e804446f8b70d968ea16c4f8d843ca"],"20000000","170362d3","66104ded",false]}
₿ (3410849) create_jobs_task: New Work Dequeued 1e46e0


### skot on 2024-04-05

Yes, it does look like your units have stopped hashing. no nonces are coming in from the ASIC. If this happens regularly you might have faulty hardware. Have you asked the seller about this?

### unclasp on 2024-04-05

No wait, i will show you in a few hours...
<img width="671" alt="333" src="https://github.com/skot/ESP-Miner/assets/36558895/fe45f305-4868-41cf-b565-2c2344e5af5b">


### unclasp on 2024-04-07

4 miners run at 575/1300 without any problems. Two miners are defective. No matter what I set. I'm now getting two as replacements. I read that you recommend 485/1200 for the 1366 (LM06). I can't do 500 Gh/s with that. Which settings are used most often?

### skot on 2024-04-07

Those luckyminer fans look pretty small to me. You should prolly underclock them. I'm closing this issue as it's not related to esp-miner.

### unclasp on 2024-04-07

I found the problem. They are different products. Board Version: 0.11 and 204. These with 0.11 do not work.
