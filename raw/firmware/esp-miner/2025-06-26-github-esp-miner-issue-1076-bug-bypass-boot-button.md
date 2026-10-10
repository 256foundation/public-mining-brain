# bitaxeorg/ESP-Miner issue #1076: bug bypass boot button

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1076
> Collected: 2026-10-07
> Published: 2025-06-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1076
- State: closed
- Author: WantClue
- Opened: 2025-06-26
- Closed: 2025-06-27
- Labels: bug

## Description

Boot button does not respond on self test bypass

## Comments

### ghost on 2025-06-26

Confirmed, does not work.

Wonder when that crept in ... hmm 

### ghost on 2025-06-26

OK, just did a test -- #617  You have to be quick here with this bit.

Next step, wait for self test to start, the press the RESET button, it takes it out of self test (tested this 4 times).



### mutatrum on 2025-06-27

#979 changed the code, but it should't be functionally different. But I understand what the bug is, not sure what 'self test bypass' means. What is the expected behaviour and what is happening?

### ghost on 2025-06-27

https://github.com/bitaxeorg/ESP-Miner/blob/ee7279919a7808765ee788611b3871051c1f9517/main/screen.c#L336

But it don't work, the RESET button takes it out of that mode now it seems and I can't find any notes on it.

### mutatrum on 2025-06-27

Ah, I understand. This is not a new bug, at least not for 2.9.0.

There's two ways of starting the self test, one is through a setting in NVS, and the other is through the boot button just after power up. AFAIK the boot button self test method never set the NVS flag, so it's stricktly a one-time self test run.

So in this case, the text needs to be different as reset is the only option.

### mutatrum on 2025-06-27

Original commit that added self test on boot functionality: 39a4c4164ae2f5474d1a891ec02d4cfa0251903c

This didn't set the NVS flag.

### mutatrum on 2025-06-27

This is the check to run self-test:
```c
static bool should_test(GlobalState * GLOBAL_STATE) {
    // Optionally hold the boot button
    if (gpio_get_level(CONFIG_GPIO_BUTTON_BOOT) == 0) { // LOW when pressed
        return true;
    }

    bool is_max = GLOBAL_STATE->DEVICE_CONFIG.family.asic.id == BM1397;
    uint64_t best_diff = nvs_config_get_u64(NVS_CONFIG_BEST_DIFF, 0);
    uint16_t should_self_test = nvs_config_get_u16(NVS_CONFIG_SELF_TEST, 0);
    if (should_self_test == 1 && !is_max && best_diff < 1) {
        return true;
    }
    return false;
}
```

The test finished logic:
```c
    if (test_result == TESTS_FAILED) {
        ESP_LOGI(TAG, "SELF TESTS FAIL -- Press RESET to continue");  
        while (1) {
            // Wait here forever until reset_self_test() gives the BootSemaphore
            if (xSemaphoreTake(BootSemaphore, portMAX_DELAY) == pdTRUE) {
                nvs_config_set_u16(NVS_CONFIG_SELF_TEST, 0);
                //wait 100ms for nvs write to finish?
                vTaskDelay(100 / portTICK_PERIOD_MS);
                esp_restart();
            }
        }
    } else {
        nvs_config_set_u16(NVS_CONFIG_SELF_TEST, 0);
        ESP_LOGI(TAG, "Self Tests Passed!!!");
    }
```

It resets the flag on a successfull self test.

It's either boot button, or factory flash (with `NVS_CONFIG_BEST_DIFF` < 1) and `NVS_CONFIG_SELF_TEST` set to 1. I'm not sure why Max isn't allowed to self-test on factory flash.

I _think_ this should be the logic:

| | | Factory self-test | BOOT Button self-test |
| --- | --- | --- | --- |
| Success | Reset | Clear flag, reset, normal boot | Reset, normal boot |
| Success | Hold BOOT| N/A | N/A |
| Failure | Reset | Reset, new self-test | Reset, normal boot |
| Failure | Hold BOOT | Clear flag, reset, normal boot | N/A |

At the end of the button self test (e.g. `NVS_CONFIG_SELF_TEST` is not set), failure or success, the only option is reset.
