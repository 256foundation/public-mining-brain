# LuxOS Docs — Temperature & Fans

> Registry ID: luxos-docs
> Source: https://docs.luxor.tech/firmware/features/tempsandfans
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


LuxOS provides three user-customizable temperatures that drive different actions in the miner.

**The temperatures shown by default in LuxOS are hashboard temperatures and should not be confused with chip temperatures.** These are two different measurements: hashboard temperature comes from dedicated sensors on the board itself, while chip temperature refers to the temperature of the individual ASIC chips. On most S19-series Antminers, stock firmware and other aftermarket firmwares display chip temperatures that are estimated by adding \~15°C to the hashboard sensor reading. Because these are estimates rather than direct measurements, LuxOS does not surface them — it shows only the hashboard temperatures that are actually measured. Some hardware does report real, per-chip temperatures from on-die sensors. On MicroBT Whatsminers and on certain Antminer models that include on-die chip sensors, LuxOS surfaces those real readings (not estimates) — in the chip topology view in the GUI and through the [healthchipget API](../api/luxminer/healthchipget) command.

Sensor counts vary by vendor and model. Bitmain Antminers typically have 4 temperature sensors per hashboard, though some models ship with 2. MicroBT Whatsminers have 1 temperature sensor per hashboard. Antminer Equihash ASIC miners, such as the Antminer Z15 Pro, have one sensor per chip (six per hashboard), each reporting both a hashboard temperature and the chip's on-die temperature; only the hashboard readings on the exhaust side are critical (see [temps](../api/cgminer/temps#antminer-z15-pro)). Regardless of how many sensors are present, LuxOS makes decisions based on the highest reading across all hashboard temperature sensors on each board.

<Callout type="info">
  The following temperature settings can be configured via [Commander](https://luxor.tech/commander), the miner's web
  UI, or the [tempctrlset](../api/luxminer/tempctrlset) API command.
</Callout>

* **Target Temperature:** Used for the fan algorithm. Once the maximum temperature reading reaches the Target Temperature threshold fan speeds will be set to 100% unless the LuxOS fan algorithm is overridden with Manual fans settings.

* **Hot Temperature:** Used by [ATM (Advanced Thermal Management)](./atmsettings) to drive steps up and steps down in profiles or power target based on board sensor temperature.

* **Dangerous Temperature:** When any of the board sensor temperatures reaches this temperature the hashboard will be shutdown to prevent damage.

* **Chip Target Temperature:** The chip die temperature equivalent of Target Temperature, for miners that report chip-level temps. Uses the same fan curve but evaluated independently — whichever demands higher fan speed wins. Only applies to models with chip die temperature sensors.

* **Chip Hot Temperature:** Used by ATM to drive steps up and steps down in profiles or power target based on chip temperature.

* **Chip Dangerous Temperature:** When any ASIC chip on a hashboard reaches this temperature the hashboard will be shutdown to prevent damage.

* **Water Inlet Startup Temperature:** When the water inlet temperature is below this threshold the miner will not start hashing, preventing operation when the cooling loop is too cold.

* **Water Inlet Hot Temperature:** Used by ATM to drive steps up and steps down in profiles or power target based on water inlet temperature.

* **Water Inlet Dangerous Temperature:** When the water inlet temperature reaches this threshold the miner will shutdown all hashboards to prevent damage from insufficient cooling.

**Bitmain Antminer**

| Temperature Setting   | Default | Fiber Glass Hashboards                                                                                                                                        | Aluminium Hashboards                                                                                                                                          |
| :-------------------- | :-----: | :------------------------------------------------------------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Target Temperature    |   55C   | 55C                                                                                                                                                           | 55C                                                                                                                                                           |
| Hot Temperature       |   65C   | For units with ATM enabled and if the user wants to experience less underclocking then increase this setting.                                                 | To preserve the lifespan of the miner we don't recommend increasing the hot temperature for sustained periods of time.                                        |
| Dangerous Temperature |   70C   | Maximum of 75C, ideally a 8C buffer from your Hot Temperature for ATM to have enough room to cool-down a miner before it shuts down due to high temperatures. | Maximum of 72C, ideally a 8C buffer from your Hot Temperature for ATM to have enough room to cool-down a miner before it shuts down due to high temperatures. |

**Antminer Z15 Pro**

| Target |  Hot | Dangerous | Chip Target | Chip Hot | Chip Dangerous |
| :----: | :--: | :-------: | :---------: | :------: | :------------: |
|  70°C  | 75°C |    80°C   |     70°C    |   90°C   |      95°C      |

These defaults match the stock firmware. By default the Z15 Pro also requires every fan to be running; you can lower the minimum number of fans with `min_fans` in [fanset](../api/luxminer/fanset).

**MicroBT Whatsminer**

<Accordions type="single">
  <Accordion title="M50 — 1 miner type">
    | Miner Type | Target |  Hot | Dangerous | Chip Hot | Chip Panic |
    | :--------- | :----: | :--: | :-------: | :------: | :--------: |
    | M50\_VK40  |  80°C  | 83°C |    93°C   |   115°C  |    120°C   |
  </Accordion>

  <Accordion title="M50S — 3 miner types">
    | Miner Type | Target |  Hot | Dangerous | Chip Hot | Chip Panic |
    | :--------- | :----: | :--: | :-------: | :------: | :--------: |
    | M50S\_VK20 |  80°C  | 83°C |    93°C   |   115°C  |    120°C   |
    | M50S\_VK30 |  80°C  | 83°C |    93°C   |   115°C  |    120°C   |
    | M50S\_VK80 |  80°C  | 83°C |    93°C   |   115°C  |    120°C   |
  </Accordion>

  <Accordion title="M50S+ — 3 miner types">
    | Miner Type  | Target |  Hot | Dangerous | Chip Hot | Chip Panic |
    | :---------- | :----: | :--: | :-------: | :------: | :--------: |
    | M50S+\_VK10 |  80°C  | 83°C |    93°C   |   115°C  |    120°C   |
    | M50S+\_VK20 |  74°C  | 83°C |    93°C   |   115°C  |    120°C   |
    | M50S+\_VK30 |  80°C  | 83°C |    93°C   |   115°C  |    120°C   |
  </Accordion>

  <Accordion title="M50S++ — 1 miner type">
    | Miner Type   | Target |  Hot | Dangerous | Chip Hot | Chip Panic |
    | :----------- | :----: | :--: | :-------: | :------: | :--------: |
    | M50S++\_VK50 |  80°C  | 83°C |    93°C   |   115°C  |    120°C   |
  </Accordion>

  <Accordion title="M60 — 1 miner type">
    | Miner Type | Target |  Hot | Dangerous | Chip Hot | Chip Panic |
    | :--------- | :----: | :--: | :-------: | :------: | :--------: |
    | M60\_VK20  |  80°C  | 83°C |    93°C   |   115°C  |    120°C   |
  </Accordion>

  <Accordion title="M60S — 1 miner type">
    | Miner Type | Target |  Hot | Dangerous | Chip Hot | Chip Panic |
    | :--------- | :----: | :--: | :-------: | :------: | :--------: |
    | M60S\_VK20 |  80°C  | 83°C |    93°C   |   115°C  |    120°C   |
  </Accordion>
</Accordions>

### Automatic Fan Control [#automatic-fan-control]

LuxOS provides a fan algorithm that automatically adjusts fan speeds based on the temperature of the miner. The fan algorithm is designed to keep the miner at the target temperature set by the user. LuxOS reads temperatures from the temperatures sensors once every seconds and adjusts fan speeds accordingly.

The following scenarios have a different fan behavior:

1. If temperatures can't be read from any temperature sensor, the PSU is enabled and at least one hashboard is detected (regardless if it's enabled or disabled), fans will be set to 100% for safety reasons.
2. If temperatures can't be read from any temperature sensor, the PSU is disabled or no hashboard is detected, fans will be set to 20%.
3. If the miner is curtailed, fans will be set to 20%.

### Manual Fan Control [#manual-fan-control]

If users wish to override the automatic fan control, they can set the fans to a specific percentage. In this scenario, LuxOS won't adjust the fan speed dynamically based on temperature. We suggest keeping the fans set to Automatic mode for the best performance and longevity of the miner. If immersion mode is enabled, all fans will be disabled entirely.

### Cold Start [#cold-start]

Warming up miners correctly is crucial for a reliable start up, and for improved LuxOS Autotuner performance in cold environments. Miners that are excessively cold and don't warm up properly won't hash or tune as well as properly warmed-up miners.

To tackle warming up miners, LuxOS will first attempt to bring all hashboards to a similar temperature. This is accomplished by first running the fans at 100% for a period of time to equalize the temperature across all boards. Once this has been completed, if the environmental temperature is cold enough, then profile voltage will be ramped up to bring chips and boards up to temperature evenly. This will ensure a more consistent and efficient ramp for the miner.
