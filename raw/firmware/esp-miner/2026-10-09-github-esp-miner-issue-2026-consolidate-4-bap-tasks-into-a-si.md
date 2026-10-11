# ESP-Miner issue #2026: Consolidate 4 BAP tasks into a single worker

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/2026
> Collected: 2026-10-10
> Published: 2026-10-09
> Registry ID: esp-miner

State: open | Closed: - | Author: mutatrum | Labels: -

## Body

BAP uses four separate tasks (`uart_receive_task`, `uart_send_task`, `mode_management_task`, `subscription_update_task`), all prio 5.

Consolidate BAP into a single unified worker task that blocks on UART reception with a 1,000 ms timeout, handling incoming command parsing and dispatching periodic subscription diffs on the timeout tick. Removing the dedicated send task, send queue, and mode-management loop eliminates 24 KB of stack, removes three tasks from the scheduler, and frees up prio 5 contention with mining telemetry.

## Comments

### mutatrum on 2026-10-09

I think this is all that's needed:
```
static void bap_task(void *pvParameters)
{
    GlobalState *state = (GlobalState *)pvParameters;
    uint8_t data[BAP_BUF_SIZE];
    TickType_t last_update = xTaskGetTickCount();

    while (1) {
        // Block on UART RX with a 1000 ms timeout
        int len = uart_read_bytes(BAP_UART_NUM, data, BAP_BUF_SIZE, pdMS_TO_TICKS(1000));
        
        if (len > 0) {
            // Parse incoming $BAP sentences and execute commands
            BAP_process_incoming_bytes(data, len);
        }

        // Periodic 1-second tick: handle subscription updates if active
        if ((xTaskGetTickCount() - last_update) >= pdMS_TO_TICKS(1000)) {
            last_update = xTaskGetTickCount();
            if (bap_has_active_subscriptions()) {
                BAP_send_subscription_update(state);
            }
        }
    }
}
```
