# bitaxeorg/ESP-Miner issue #1453: Incorrect line break

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1453
> Collected: 2026-10-07
> Published: 2025-12-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1453
- State: closed
- Author: matlen67
- Opened: 2025-12-14
- Closed: 2025-12-15
- Labels: none

## Description

 v12.13.0b1 (Bitaxe Gamma 601)

After changing the font, line breaks no longer work correctly for long lines. To select the entire line, you have to select at least one character from the next line.


<img width="2163" height="590" alt="Image" src="https://github.com/user-attachments/assets/c057373b-4aad-458e-a6d1-cee964a54665" />



`₿ (171964622) stratum_api: rx: {"params":["692b89f20000aaa2","b39aed0368c33b0bb45d7e8c1abad79e65ce77560001cdc00000000000000000","01000000010000000000000000000000000000000000000000000000000000000000000000ffffffff370365280e000499943e69042f55a9050c","0a636b706f6f6c1365752f736f6c6f2e636b706f6f6c2e6f72672fffffffff0362a24b1200000000160014cf3815a968c8d3cd9e58facfdb7f85c3762159db99955f000000000016001451ed61d2f6aa260cc72cdf743e4e436a82c010270000000000000000266a24aa21a9ed7337b21e9f13762c762671f322be3020e89db681404bad847661ba5316ccd1a000000000",["8e052b2d80c19ae65a674f60b6af1edff34ec1bdc304cdef208037b81057508f","4162aabe33b620442bb9887f4376852777c33ace89b75d8769baff19193c41b8","fc9b9b8712c34d1f7e76a628614252d752fdf82f1e3abe07b2594179e2cf03dd","8d1bfb5c13647804148d9ef1dcf6c2a9ec55da04002ae7846d7013d5abb67ee3","6429dd6bae354e6b7ce35cb11ff7556e2a36bd7b64012a381aba2e8671347b8f","5e1e5c19185d04375e7b8e654a5d6fed56c806baf9ddc9d13840faebae19a97d","ec678e2a190528b4288dd2819e46d0ae16a86d458c9c95a2fd6dc8bfc124ea0c","491361146e0ffff4da6e9d6351471ef891b9dcfd1a05405f8c9e13c70d8181e2","662a4a2691650fbce81bd1c95390ffd131c5105236a619d7736857ce5cfc0071","57ed9278535f5b98e1dd21dd27595353e63cb7753c090ddd1151c88028d49a28"],"20000000","1701e63a","693e9499",false],"id":null,"method":"mining.notify"}`


## Comments

### duckaxe on 2025-12-14

Fixed https://github.com/bitaxeorg/ESP-Miner/pull/1448

### mutatrum on 2025-12-15

Fixed by #1448
