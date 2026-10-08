# bitaxeorg/ESP-Miner issue #1245: Isolate NVS and Flash write tasks

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1245
> Collected: 2026-10-07
> Published: 2025-09-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1245
- State: closed
- Author: mutatrum
- Opened: 2025-09-22
- Closed: 2025-10-25
- Labels: none

## Description

From https://github.com/bitaxeorg/ESP-Miner/pull/1217#discussion_r2367274016

Each tasks allocates heap, and by design, this always uses internal memory. It is possible to move this heap off to PSRAM, but only if that task does not write to NVS or Flash. 

Currently NVS is misused as an event bus between tasks, this should be replaced by some other means of inter-task communications, and ideally only a single task should update the NVS store.

One alternative options would be to use the ESP Event handling system. This would also decouple components and reduce the use of GlobalState.

## Comments

### KillerInk on 2025-09-23

nvs_config.c 

```
#include "freertos/FreeRTOS.h"
#include "freertos/queue.h"
#include "freertos/task.h"

// ---------------------------------------------------------------------------
//  Queue Item Definition
// ---------------------------------------------------------------------------
typedef enum {
    NVS_ITEM_TYPE_U8,
    NVS_ITEM_TYPE_U16,
    NVS_ITEM_TYPE_I32,
    NVS_ITEM_TYPE_U64,
    NVS_ITEM_TYPE_BOOL,
    NVS_ITEM_TYPE_FLOAT,
    NVS_ITEM_TYPE_STRING
} nvs_item_type_t;

typedef union {
    uint8_t u8;
    uint16_t u16;
    int32_t  i32;
    uint64_t u64;
    bool     b;
    float   f;
    char *  s;          // pointer to dynamically allocated string
} nvs_value_u;

typedef struct {
    const char *key;
    nvs_item_type_t type;
    nvs_value_u val;
} nvs_item_t;

// Global queue handle
static QueueHandle_t nvs_queue = NULL;

// ---------------------------------------------------------------------------
//  Task that processes the queue
// ---------------------------------------------------------------------------
void nvs_write_task(void *pvParameters)
{
    (void) pvParameters;

    nvs_item_t item;
    for (;;) {
        if (xQueueReceive(nvs_queue, &item, portMAX_DELAY) == pdPASS) {
            switch (item.type) {
                case NVS_ITEM_TYPE_U8:
                    // Convert to u16 because no u8 setter
                    nvs_config_set_u16(item.key, (uint16_t)item.val.u8);
                    break;

                case NVS_ITEM_TYPE_U16:
                    nvs_config_set_u16(item.key, item.val.u16);
                    break;

                case NVS_ITEM_TYPE_I32:
                    nvs_config_set_i32(item.key, item.val.i32);
                    break;

                case NVS_ITEM_TYPE_U64:
                    nvs_config_set_u64(item.key, item.val.u64);
                    break;

                case NVS_ITEM_TYPE_BOOL:
                    nvs_config_set_bool(item.key, item.val.b);
                    break;

                case NVS_ITEM_TYPE_FLOAT:
                    nvs_config_set_float(item.key, item.val.f);
                    break;

                case NVS_ITEM_TYPE_STRING:
                    nvs_config_set_string(item.key, item.val.s);
                    free(item.val.s);          // clean up allocated string
                    break;
            }
        }
    }
}

// ---------------------------------------------------------------------------
//  Queue and Task initialization helper
// ---------------------------------------------------------------------------
void init_and_start(void)
{
    // Create queue with a reasonable depth (e.g., 10 items)
    nvs_queue = xQueueCreate(10, sizeof(nvs_item_t));
    if (!nvs_queue) return;

    // Start the background task
    xTaskCreate(&nvs_write_task,
                "NVS_Write_Task",
                configMINIMAL_STACK_SIZE * 2,
                NULL,
                tskIDLE_PRIORITY + 1,
                NULL);
}

// ---------------------------------------------------------------------------
//  Helper functions that enqueue various types
// ---------------------------------------------------------------------------
void enqueue_nvs_uint8(const char *key, uint8_t value)
{
    if (!nvs_queue) init_and_start();
    nvs_item_t item = { key, NVS_ITEM_TYPE_U8 };
    item.val.u8 = value;
    xQueueSendToBack(nvs_queue, &item, portMAX_DELAY);
}

void enqueue_nvs_uint16(const char *key, uint16_t value)
{
    if (!nvs_queue) init_and_start();
    nvs_item_t item = { key, NVS_ITEM_TYPE_U16 };
    item.val.u16 = value;
    xQueueSendToBack(nvs_queue, &item, portMAX_DELAY);
}

void enqueue_nvs_int32(const char *key, int32_t value)
{
    if (!nvs_queue) init_and_start();
    nvs_item_t item = { key, NVS_ITEM_TYPE_I32 };
    item.val.i32 = value;
    xQueueSendToBack(nvs_queue, &item, portMAX_DELAY);
}

void enqueue_nvs_uint64(const char *key, uint64_t value)
{
    if (!nvs_queue) init_and_start();
    nvs_item_t item = { key, NVS_ITEM_TYPE_U64 };
    item.val.u64 = value;
    xQueueSendToBack(nvs_queue, &item, portMAX_DELAY);
}

void enqueue_nvs_bool(const char *key, bool value)
{
    if (!nvs_queue) init_and_start();
    nvs_item_t item = { key, NVS_ITEM_TYPE_BOOL };
    item.val.b = value;
    xQueueSendToBack(nvs_queue, &item, portMAX_DELAY);
}

void enqueue_nvs_float(const char *key, float value)
{
    if (!nvs_queue) init_and_start();
    nvs_item_t item = { key, NVS_ITEM_TYPE_FLOAT };
    item.val.f = value;
    xQueueSendToBack(nvs_queue, &item, portMAX_DELAY);
}

void enqueue_nvs_string(const char *key, const char *value)
{
    if (!nvs_queue) init_and_start();
    char *copy = strdup(value);   // allocate copy for queue
    nvs_item_t item = { key, NVS_ITEM_TYPE_STRING };
    item.val.s = copy;
    xQueueSendToBack(nvs_queue, &item, portMAX_DELAY);
}
```

something like this should work

### mutatrum on 2025-09-25

Related PR in NerdAxe repo: https://github.com/shufps/ESP-Miner-NerdQAxePlus/pull/219
