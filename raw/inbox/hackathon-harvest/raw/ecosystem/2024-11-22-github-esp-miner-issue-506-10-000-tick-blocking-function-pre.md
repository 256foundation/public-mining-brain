# bitaxeorg/ESP-Miner issue #506: 10,000 tick blocking function present in SYSTEM_task

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/506
> Collected: 2026-10-07
> Published: 2024-11-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 506
- State: closed
- Author: ACSBEN
- Opened: 2024-11-22
- Closed: 2024-12-12
- Labels: help wanted

## Description

**Describe the Issue**
This block of code is Blocking. It creates a timeout mechanism tied to wait_time that doesn't allow the function to move past for 10,000 ticks.

```
// Wait for user input or timeout
        bool input_received = false;
        TickType_t current_time = xTaskGetTickCount();
        TickType_t wait_time = pdMS_TO_TICKS(10000) - (current_time - last_update_time);

        if (wait_time > 0) {
            if (xQueueReceive(user_input_queue, &input_event, wait_time) == pdTRUE) {
                input_received = true;
                if (strcmp(input_event, "SHORT") == 0) {
                    ESP_LOGI(TAG, "Short button press detected, switching to next screen");
                    current_screen = (current_screen + 1) % 2;
                } else if (strcmp(input_event, "LONG") == 0) {
                    ESP_LOGI(TAG, "Long button press detected, toggling WiFi SoftAP");
                    toggle_wifi_softap();
                }
            }
        }

        // If no input received and 10 seconds have passed, switch to the next screen
        if (!input_received && (xTaskGetTickCount() - last_update_time) >= pdMS_TO_TICKS(10000)) {
            current_screen = (current_screen + 1) % 2;
        }

        last_update_time = xTaskGetTickCount();
    
        
    }
```

Based on the xQueueReceive document, 
```
BaseType_t xQueueReceive(
                          QueueHandle_t xQueue,
                          void *pvBuffer,
                          TickType_t xTicksToWait
);
```

xTickstoWait acts as a delay. Setting this to zero allows for non-blocking functionality, it also seems to still keep the original functionality

Example:
```
if (xQueueReceive(user_input_queue, &input_event, 0) == pdTRUE)
        {
            input_received = true;
            if (strcmp(input_event, "SHORT") == 0)
            {
                ESP_LOGI(TAG, "Short button press detected, switching to next screen");
                current_screen = (current_screen + 1) % 2;
            }
            else if (strcmp(input_event, "LONG") == 0)
            {
                ESP_LOGI(TAG, "Long button press detected, toggling WiFi SoftAP");
                toggle_wifi_softap();
            }
            last_update_time = xTaskGetTickCount();
        }
        
        // Separate timer for screen switching
        if ((xTaskGetTickCount() - last_update_time) >= pdMS_TO_TICKS(10000))
        {
            current_screen = (current_screen + 1) % 2;
            last_update_time = xTaskGetTickCount();
        }
    }
```



## Comments

### skot on 2024-11-22

good catch.
https://github.com/skot/ESP-Miner/blob/29a543da76ba5fd19e07f43da87214613d67455a/main/system.c#L251-L274
