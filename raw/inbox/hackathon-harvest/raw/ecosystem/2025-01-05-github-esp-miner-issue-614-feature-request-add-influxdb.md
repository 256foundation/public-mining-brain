# bitaxeorg/ESP-Miner issue #614: [Feature Request] Add InfluxDB

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/614
> Collected: 2026-10-07
> Published: 2025-01-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 614
- State: open
- Author: zlorfi
- Opened: 2025-01-05
- Closed: n/a
- Labels: none

## Description

I'm trying to add the InfluxDB feature from the [NerdAxe+](https://github.com/shufps/ESP-Miner-NerdQAxePlus) back to ESP-miner. The Angular frontend looks promising, I'm stuggling a little bit with the `main/tasks/power_management_task.c` addition.
My understanding here is that this task in the NerdAxe+ version is also pushing the power management values to InfluxDB but I don't quite see how to insert this task into the current code as it deviates quite a bit. Any ideas?
https://github.com/shufps/ESP-Miner-NerdQAxePlus/blob/0de81ab5eadd330e01f5b35dd5bbf6f134d3cfd3/main/tasks/power_management_task.cpp#L98-L114

``` 
float vin = board->getVin();
float iin = board->getIin();
float pin = board->getPin();
float pout = board->getPout();
float vout = board->getVout();
float iout = board->getIout();

influx_task_set_pwr(vin, iin, pin, vout, iout, pout);

m_voltage = vin * 1000.0;
m_current = iin * 1000.0;
m_power = pin;
board->getFanSpeed(&m_fanRPM);

m_chipTempAvg = board->readTemperature(0);
m_vrTemp = board->readTemperature(1);
influx_task_set_temperature(m_chipTempAvg, m_vrTemp);
```

I really enjoy this feature and would love to see this option to be added here. 

#613 

## Comments

### b-rowan on 2025-01-06

A lot of this is referenced in `http_server.c` for the API, specifically these lines:
https://github.com/skot/ESP-Miner/blob/39a4c4164ae2f5474d1a891ec02d4cfa0251903c/main/http_server/http_server.c#L372-L374

For some reason they have both in and out values, you really should only need one of these.  so `vin` becomes `voltage`, `iin` becomes `current`, and `pin` becomes `power`.

Hopefully this helps!

### shufps on 2025-03-05

The TPS53647 used on the NerdQaxe+ and derivatives can measure voltage, current and power of both input and output of the buck converter.

There are boards that don't support this like the NerdAxe (that is based on the Bitaxe Ultra). In this case the values only would be zero. 

```c
float NerdAxe::getVin() {
    return INA260_read_voltage() / 1000.0;
}

float NerdAxe::getIin() {
    return INA260_read_current() / 1000.0;
}

float NerdAxe::getPin() {
    return INA260_read_power() / 1000.0;
}

float NerdAxe::getVout() {
    return ADC_get_vcore() / 1000.0;
}

float NerdAxe::getIout() {
    return 0.0;
}

float NerdAxe::getPout() {
    return 0.0;
}
```
