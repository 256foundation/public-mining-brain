# bitaxeorg/ESP-Miner issue #98: Add suggest difficultly to ui

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/98
> Collected: 2026-10-07
> Published: 2024-01-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 98
- State: closed
- Author: Sledge0001
- Opened: 2024-01-28
- Closed: 2024-03-15
- Labels: enhancement, help wanted, good first issue

## Description

Enhancement request:

Would be helpful to be able to place a suggest difficulty field to the UI to help improve the submitting of shares right from the stratum handshake to help expedite the submitting of valid shares to various pools.

## Comments

### monster4866 on 2024-02-01

that would be nice

### skot on 2024-02-16

We do suggest a fixed difficulty that's good for the bitaxe (`"mining.suggest_difficulty", "params": [1000]`). It's up to the stratum server if they want to use that or not.

What does being able to change this default get you?

### Sledge0001 on 2024-02-18

I don't see that being passed correctly to the pool at the miners startup / handshake.

Seems like the default diff being seen is 8192

### skot on 2024-02-18

I copied that right out of the log for my bitaxe.. Can you post your log?

### Sledge0001 on 2024-02-18

₿ (31601) httpd_txrx: httpd_sock_err: error in recv : 104   <-- I think this maybe it...


₿ (8781) asic_result: Nonce difficulty 2437.76 of 8192.
₿ (12631) asic_result: Nonce difficulty 506.21 of 8192.
₿ (14751) asic_result: Nonce difficulty 476.71 of 8192.
₿ (16821) asic_result: Nonce difficulty 607.28 of 8192.
₿ (24451) asic_result: Nonce difficulty 509.14 of 8192.
₿ (25031) asic_result: Nonce difficulty 308.53 of 8192.
₿ (25051) stratum_task: rx: {"params":["65d28cbf00000003","c976d1bd330f198b18f4bb0dbce26721bf297af900029e740000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff330345ae0c00040a8dd26504047a392c0c","0a636b706f6f6c0f2f4c455453474f4252414e444f4e2fffffffff0398e70e260000000016001416e6be74cfb2090a67e27627a849f5233729674d9fba0a000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9edaf27020696a3e849a04f57f9bc50fe161ff91d11b369b05e4979637a8984211b00000000",["c7217b1433ac695e5d25bf06118879bf7e1c56b0f17d8c36acbe169ed8ed5ade","239ca0e9cd602386339fb69a2094b935683e866e1001d97bdbb63227053232d2","ec274da6ad2c24a0960dd7c6dbff387e41c6a8b0a0cf6dec362a91b54f293125","80945d881aa9c1f0aef49f5a0b9f842e5386c225348a8573c7cb4ce78503a685","fb138b93baaa1167ec255c6a74a27bfeb632cb362e46624f37037347c1e7cbcb","ed7b15dee5cbb5feefa3edee8d623b5492fa0794506b4c7f0f15a8baf4141ccc","4c386b416dd914ead883002e3cf23bd4c36b334c236a4a8e534ee4f5457e8b4f","77ba70cf403f806f11340b4400c9ef09ab5d2b1056a506041882c1824c601e3f","3b0af005b03360af410f94e2abaa362b363d6be5c77c77661835e4d9f1fd6fed","9754c120f40dc9d817bda48351b85d064868850739944239076957142726ca4b","a8f369e2b04afd9b521b4bebe09100e59ee353691cb59faab9b34806ddead558"],"20000000","170371b1","65d28d0a",false],"id":null,"method":"mining.notify"}
₿ (26941) create_jobs_task: New Work Dequeued 65d28cbf00000003
₿ (30231) asic_result: Nonce difficulty 274.68 of 8192.
₿ (33401) asic_result: Nonce difficulty 803.22 of 8192.
₿ (33471) asic_result: Nonce difficulty 1676.35 of 8192.
₿ (42271) asic_result: Nonce difficulty 1262.85 of 8192.
₿ (44031) asic_result: Nonce difficulty 1262.57 of 8192.
₿ (47821) asic_result: Nonce difficulty 329.02 of 8192.
₿ (48571) asic_result: Nonce difficulty 379.64 of 8192.
₿ (52361) asic_result: Nonce difficulty 1572.00 of 8192.
₿ (52881) asic_result: Nonce difficulty 668.91 of 8192.
₿ (55321) stratum_task: rx: {"params":["65d28cbf00000004","c976d1bd330f198b18f4bb0dbce26721bf297af900029e740000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff330345ae0c0004288dd26504da71d0380c","0a636b706f6f6c0f2f4c455453474f4252414e444f4e2fffffffff032d6a13260000000016001416e6be74cfb2090a67e27627a849f5233729674de5bb0a000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed4adac5cc4a3c4b75a261924d95ba4485ab143971a24c5b0ecff818f0de505a6e00000000",["c7217b1433ac695e5d25bf06118879bf7e1c56b0f17d8c36acbe169ed8ed5ade","239ca0e9cd602386339fb69a2094b935683e866e1001d97bdbb63227053232d2","fc8fb2d2e026d922209c778a9ac098759e0da76f63983444a782f9e5936ea5c6","940ff073c898f51248608fbd4007bef66c630060799cc807cb9d0cb322f2a9d9","2589e23eca197715bbe9f94f9411dc3acbe9495cb0edcb90a2d37643f6c593a6","6f49308d5738a02fd8cff9e225a0953e9447039f830aab3b88765b0c58885e4c","235f048d9420d507fb1d44a1753316ec789e2ab46a3c2dea082a45c2b295eab2","48b56b20977cb15b53d115431030a8479082da6e3d4a554dd1e452db56ecc659","b1c501e154148be075ff50c39b342123bf650523a6aff2012295d9d028e16d46","93b5bf3d57adf01a37af9ea8a1fd5513305889ff939582a2d6ab631d03f85963","a9254dab7505f7163cd0d31a1e25af787744bc04989adacc0b1e60912f6e10e5","6423f74de3ac9d994b8236eb24a323d78c7b843bf68c568199b0fcd56ab78ca7"],"20000000","170371b1","65d28d28",false],"id":null,"method":"mining.notify"}

### benjamin-wilson on 2024-02-18

Which version of esp-miner are you on? There was a bug earlier 

### Sledge0001 on 2024-02-18

Model:	BM1366
Uptime:	32 seconds
WiFi Status:	Connected!
Free Heap Memory:	179928
Version:	v2.0.7
Board Version:	204


But also happens on a 201 board as well. It's on all 3 of the devices.


### Sledge0001 on 2024-02-18

What's wild is all 3 of the units start @ 8192 regardless. 


### benjamin-wilson on 2024-02-18

Public-pool? Other pools may not honor the suggest difficulty request 

### Sledge0001 on 2024-02-18

Unique pool code however the previous v2.04 firmware code did seem to get honored. Also the code i am using does honor it with cgminer so I am not sure the pool code is the issue as 8192 seems like a specific number to start the diff at which would go against the start diff I have set on the pool side.

### skot on 2024-02-19

can you connect your bitaxe USB-C to your computer and get the logs starting earlier in the cycle? The log should stream out over serial at 115200 baud. I think you'll see that `mining.suggest_difficulty` is being sent.

### monster4866 on 2024-02-19

₿ (55791) asic_result: Nonce difficulty 313.19 of 10000.
₿ (57521) asic_result: Nonce difficulty 454.24 of 10000.
₿ (59701) asic_result: Nonce difficulty 369.89 of 10000.
₿ (61871) asic_result: Nonce difficulty 4387.23 of 10000.
₿ (66381) asic_result: Nonce difficulty 635.69 of 10000.

Same for me, with ckpool it starts at 8k then it goes to 10k and after 2-3min. The pool corrects this to 400-600

have 10 bitaxes, all the same, fw 2.0.7, boradv. 201-204

### skot on 2024-02-19

> ₿ (55791) asic_result: Nonce difficulty 313.19 of 10000. ₿ (57521) asic_result: Nonce difficulty 454.24 of 10000. ₿ (59701) asic_result: Nonce difficulty 369.89 of 10000. ₿ (61871) asic_result: Nonce difficulty 4387.23 of 10000. ₿ (66381) asic_result: Nonce difficulty 635.69 of 10000.
> 
> Same for me, with ckpool it starts at 8k then it goes to 10k and after 2-3min. The pool corrects this to 400-600
> 
> have 10 bitaxes, all the same, fw 2.0.7, boradv. 201-204

again, I'm pretty sure this is driven by the pool. If you get the full logs by the USB method I mentioned above we can check it out.
