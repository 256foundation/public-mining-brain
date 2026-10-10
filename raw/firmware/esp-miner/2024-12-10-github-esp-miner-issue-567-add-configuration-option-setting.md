# bitaxeorg/ESP-Miner issue #567: Add configuration option (setting) for DisplayContrast

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/567
> Collected: 2026-10-07
> Published: 2024-12-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 567
- State: closed
- Author: Torfbold
- Opened: 2024-12-10
- Closed: 2026-10-02
- Labels: enhancement

## Description

Hi, 
as some people might be running the device in their bedrooms and are somewhat sensitive to flashing lights the updating display could cause some issues during sleep. Maybe it would be a nice feature to enable some "night times" ( best would be configurable) at when the display is turned off (and on again  the next morning) . Looking into the code there should be the option to call the commands against the display - either turning it off completely or reducing contrast. 



## Comments

### MyOwn2C on 2024-12-10

You can alap just unplug the display after configuring. 

### Torfbold on 2024-12-10

Agree on plugging out the display - but this leads to the log being basically unreadable:


₿ (73389942) i2c.master: s_i2c_synchronous_transaction(872): I2C transaction failed
₿ (73389952) i2c.master: i2c_master_transmit(1074): I2C transaction failed
₿ (73389962) i2c.master: I2C transaction unexpected nack detec

EDIT:
I just checked - if I plug it in again - the errors from log are gone - display keeps blank - probably until I reboot and it gets initalized again.
So that option is also fine - tyvm

### mutatrum on 2024-12-10

Don't unplug or plug your display while the machine is powered on, that can easily break the display.

No display option will probably come in the future, there's already a screen timeout in the works: #525

### mutatrum on 2024-12-10

This might be difficult, as the Bitaxe doesn't know what time it is. There are two options for that:

 * Use the time given by the `mining.notify` message from the pool. This is block time, so not perfect, and it's in UTC, so without timezone information.
 * Use NTP and query for the time.

Neither are really nice options.

### Torfbold on 2024-12-10

Agree, if "night time" is no option, maybe an alternative is an API call to disable the display (something like the restart button from the menu on the left side). Additionally a contrast Parameter could be helpful to reduce brightness?!

### mutatrum on 2024-12-10

I tested a bit, there is a contrast parameter. Unfortunately it's not built into the driver, so this would be custom code for this panel, which is a bit of a shame:
```
#define SSD1306_CMD_CONTRAST 0x81
ESP_ERROR_CHECK_WITHOUT_ABORT(esp_lcd_panel_io_tx_param(io_handle, SSD1306_CMD_CONTRAST, (uint8_t[]) { 0x00 }, 1));
```
On my display it changes contrast a bit, but not on the range you would expect. Setting it to 0 is about half, maybe one third brightness compared to 255. Apparently it's configured with a resistor on the display? See: https://forums.adafruit.com/viewtopic.php?p=573606#p573606

Some people mentioned not all SSD1306 displays support contrast setting, so YMMV.

### mutatrum on 2024-12-11

I've opened an issue at esp to support contrast through their lcd drivers. https://github.com/espressif/esp-idf/issues/15015

Maybe this ticket can be changed to add a screen contrast settings. That and #525, would that be ok to reduce the impact of the display at night?

### Torfbold on 2024-12-12

@mutatrum : Thank you very much for all your efforts here! I really appreciate it.
Sure - that would be feasible I think.
How to proceed? Should I just update the original issue description?


### mutatrum on 2024-12-12

No problem. Just renaming the title of this issue should be ok.

### mutatrum on 2026-10-02

As it's unpredictable if a display actually can do the contrast change, I think it's unadvisable to add this in the code, it probably causes more support questions than it is useful.
