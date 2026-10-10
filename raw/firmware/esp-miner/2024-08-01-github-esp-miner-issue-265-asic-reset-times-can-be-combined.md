# bitaxeorg/ESP-Miner issue #265: Asic reset times can be combined to low levels

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/265
> Collected: 2026-10-07
> Published: 2024-08-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 265
- State: closed
- Author: manan1199
- Opened: 2024-08-01
- Closed: 2024-08-10
- Labels: none

## Description

If the asic reset is only active at a low level，the raised delay of 100ms can be appended to the low level maintenance period,this helps to improve the reliability of 1.2V IO level reset asics.100ms is the reset threshold for most MCUS.

static void _reset(void)
{
    gpio_set_level(BM1366_RST_PIN, 0);

    // delay for 100ms
    vTaskDelay(200 / portTICK_PERIOD_MS);

    // set the gpio pin high
    gpio_set_level(BM1366_RST_PIN, 1);

    // delay for 100ms
    //vTaskDelay(100 / portTICK_PERIOD_MS);
}
