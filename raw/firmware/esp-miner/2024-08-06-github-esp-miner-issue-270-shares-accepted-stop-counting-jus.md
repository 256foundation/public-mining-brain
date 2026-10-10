# bitaxeorg/ESP-Miner issue #270: Shares accepted stop counting just short of 32767.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/270
> Collected: 2026-10-07
> Published: 2024-08-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 270
- State: closed
- Author: Entropypp
- Opened: 2024-08-06
- Closed: 2024-08-14
- Labels: none

## Description

Shares accepted stop counting just short of 32767. 

I suspect that this is because in global_state.h the declaration of:
uint64_t shares_accepted;
uint64_t shares_rejected

Should be declared as long.

This seems to cause issues in http_server.c when calling
cJSON_AddNumberToObject(root,"sharesAccepted", GLOBAL_STATE->SYSTEM_MODULE.shares_accepted)
   

## Comments

### skot on 2024-08-06

What firmware version are you running?

### Entropypp on 2024-08-08

Verified that this happens in v2.1.8 
**From CJSON Github If the number is bigger than INT_MAX, "uint64_t value = value_js->valueint" will be wrong.**
https://github.com/DaveGamble/cJSON/issues/348

### skot on 2024-08-10

This fix will be in 2.1.10
