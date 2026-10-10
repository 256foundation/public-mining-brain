# bitaxeorg/ESP-Miner issue #290: Track number of blocks found on dashboard and api

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/290
> Collected: 2026-10-07
> Published: 2024-08-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 290
- State: closed
- Author: eandersson
- Opened: 2024-08-14
- Closed: 2024-08-15
- Labels: invalid

## Description

This is mostly for fun and wishful thinking, but for my own miners I added a tracker that I stored in nvs_config to track the number of blocks found.

e.g. this is how it shows up in my dashboard
![image](https://github.com/user-attachments/assets/3b21f77b-d5d0-4194-9b9c-984fb318e4f3)

```
cJSON_AddNumberToObject(root, "blocksFound", GLOBAL_STATE->SYSTEM_MODULE.blocks_found);
```

```
if (diff > network_diff) {
    module->FOUND_BLOCK = true;
    module->blocks_found++;
    nvs_config_set_u64(NVS_CONFIG_BLOCKS_FOUND, module->blocks_found);
    ESP_LOGI(TAG, "FOUND BLOCK!!!!!!!!!!!!!!!!!!!!!! %f > %f", diff, network_diff);
}
```

## Comments

### MyOwn2C on 2024-08-14

I vote this is worthy to be included in next update 👍

### WantClue on 2024-08-14

If you suggest implementations open a pull request please.
