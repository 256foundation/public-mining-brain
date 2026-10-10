# 256foundation/hydrapool issue #35: mining.authorize with an invalid Bitcoin address should return an error result

> Source: https://github.com/256foundation/hydrapool/issues/35
> Collected: 2026-10-07
> Published: 2025-11-16

- Repository: 256foundation/hydrapool
- Type: issue
- Number: 35
- State: closed
- Author: rkuester
- Opened: 2025-11-16
- Closed: 2026-01-12
- Labels: none

## Description

When `mining.authorize` contains an invalid Bitcoin address, it should return an error result. Instead, it sends no result and closes the connection. 

**Request**:
```
{"id": 3, "method": "mining.authorize", "params": ["bc1qnp980s5fpp8l94p5cvttntdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq.bitaxe", "x"]}
```

**Hydrapool log**:
```
2025-11-16T18:28:44.181890Z  INFO p2poolv2_lib::stratum::server: New connection from: 10.89.0.3:36632
2025-11-16T18:28:44.227758Z  INFO p2poolv2_lib::stratum::server: Rx 10.89.0.3:36632 Some(Ok("{\"id\": 1, \"method\": \"mining.confi
gure\", \"params\": [[\"version-rolling\"], {\"version-rolling.mask\": \"ffffffff\"}]}"))
2025-11-16T18:28:44.227810Z  INFO p2poolv2_lib::stratum::server: Tx 10.89.0.3:36632 "{\"id\":1,\"result\":{\"version-rolling\":true
,\"version-rolling.mask\":\"1fffe000\"},\"error\":null}"
2025-11-16T18:28:44.280995Z  INFO p2poolv2_lib::stratum::server: Rx 10.89.0.3:36632 Some(Ok("{\"id\": 2, \"method\": \"mining.subsc
ribe\", \"params\": [\"bitaxe/BM1370/v2.11.0b5-1-g671943d-dirty\"]}"))
2025-11-16T18:28:44.281035Z  INFO p2poolv2_lib::stratum::server: Tx 10.89.0.3:36632 "{\"id\":2,\"result\":[[[\"mining.notify\",\"7f
2d7ea71\"],[\"mining.set_difficulty\",\"7f2d7ea72\"]],\"a77e2d7f\",8],\"error\":null}"
2025-11-16T18:28:44.281086Z  INFO p2poolv2_lib::stratum::server: Tx 10.89.0.3:36632 "{\"method\":\"mining.set_difficulty\",\"params
\":[1]}"
2025-11-16T18:28:44.281106Z  INFO p2poolv2_lib::stratum::server: Rx 10.89.0.3:36632 Some(Ok("{\"id\": 3, \"method\": \"mining.autho
rize\", \"params\": [\"bc1qnp980s5fpp8l94p5cvttntdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq.bitaxe\", \"x\"]}"))
2025-11-16T18:28:44.281126Z ERROR p2poolv2_lib::stratum::server: Error handling message from 10.89.0.3:36632: Err(AuthorizationFail
ure("Invalid username: Invalid Bitcoin address: Failed to parse address: legacy address base58 string")). Closing connection.
2025-11-16T18:28:44.281132Z ERROR p2poolv2_lib::stratum::server: Error processing message from 10.89.0.3:36632: Authorization faile
d: Invalid username: Invalid Bitcoin address: Failed to parse address: legacy address base58 string
2025-11-16T18:28:44.281171Z ERROR p2poolv2_lib::stratum::server: Error occurred while handling connection 10.89.0.3:36632. Closing
connection.
```

**Public Pool response to the same request**:
```
{"id":3,"result":null,"error":[20,"Authorization validation error",", bc1qnp980s5fpp8l94p5cvttntdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq"]}
```

For what it's worth, a Bitaxe (esp-miner) responded differently when it encountered an error compared to being abruptly disconnected.

## Comments

### pool2win on 2025-11-19

Good catch. Just verified ckpool returns an error too.

```
telnet solo.ckpool.org 3333                                                                                                    
Trying 15.204.102.129...
Connected to solo.ckpool.org.
Escape character is '^]'.
{"id":1,"method":"mining.subscribe","params":["Node/1.0.0"]}
{"result":[[["mining.notify","6caab69c"]],"6b6c5e6c",8],"id":1,"error":null}
{"params":[10000],"id":null,"method":"mining.set_difficulty"}
{"id": 2, "method": "mining.authorize", "params": ["badaddress", "x"]}
{"result":false,"error":null,"id":2}
^]
telnet> 
```

### pool2win on 2026-01-12

Following ckpool's two srtike policy on auth failure. Fixed: https://github.com/p2poolv2/p2poolv2/pull/312

First one: shows failure reason
Second: disconnect

Two bad attempts:

```
Escape character is '^]'.
{"id":1,"method":"mining.subscribe","params":["Node/1.0.0"]}
{"id":1,"result":[[["mining.notify","9bea31151"],["mining.set_difficulty","9bea31152"]],"1531ea9b",8],"error":null}
{"method":"mining.set_difficulty","params":[10000]}
{"id": 2, "method": "mining.authorize", "params": ["bc1qce93hy5rhg02s6aeu7mfdvxg76x66pqqtrvzs3", "x"]}
{"id":2,"result":null,"error":{"code":-401,"message":"Invalid username Invalid Bitcoin address: Expected an address for network signet"}}
{"id": 2, "method": "mining.authorize", "params": ["bc1qce93hy5rhg02s6aeu7mfdvxg76x66pqqtrvzs3", "x"]}
Connection closed by foreign host.
```

```
Escape character is '^]'.
{"id":1,"method":"mining.subscribe","params":["Node/1.0.0"]}
{"id":1,"result":[[["mining.notify","80cb53721"],["mining.set_difficulty","80cb53722"]],"7253cb80",8],"error":null}
{"method":"mining.set_difficulty","params":[10000]}
{"id": 2, "method": "mining.authorize", "params": ["", "x"]}
{"id":2,"result":null,"error":{"code":-401,"message":"Invalid username Invalid Bitcoin address: Failed to parse address: base58 error"}}
{"id": 2, "method": "mining.authorize", "params": ["", "x"]}
Connection closed by foreign host.
```

Second attempt is correct:
```
Escape character is '^]'.
{"id":1,"method":"mining.subscribe","params":["Node/1.0.0"]}
{"id":1,"result":[[["mining.notify","f2c006c61"],["mining.set_difficulty","f2c006c62"]],"c606c0f2",8],"error":null}
{"method":"mining.set_difficulty","params":[10000]}
{"id": 2, "method": "mining.authorize", "params": ["bc1qce93hy5rhg02s6aeu7mfdvxg76x66pqqtrvzs3", "x"]}
{"id":2,"result":null,"error":{"code":-401,"message":"Invalid username Invalid Bitcoin address: Expected an address for network signet"}}
{"id": 2, "method": "mining.authorize", "params": ["mzRbSbzxZrT4crVFhvzLEEuGuihSk7G7ZL", "x"]}
{"id":2,"result":true,"error":null}
{"method":"mining.set_difficulty","params":[10000]}
{"method":"mining.notify","params":["1889f3b18bf92d0c","d136eacedbc6cd8c5bbdcdc82c53974d1590d067d62534941925836f00000031","02000000010000000000000000000000000000000000000000000000000000000000000000ffffffff4602ce09203f2ff8f3c46400f2c829a06e9c40fbddfb7fc3bccfc12d1263ee3a23639c751701000474c7646904bc8ae01e0c","085032506f6f6c7632ffffffff0200f2052a01000000160014274466e754a1c12d0a2d2cc34ceb70d8e017053a0000000000000000266a24aa21a9ede2f61c3f71d1defd3fa999dfa36953755c690689799962b48bebd836974e8cf900000000",[],"20000000","1e0377ae","6964c76c",true]}

```
