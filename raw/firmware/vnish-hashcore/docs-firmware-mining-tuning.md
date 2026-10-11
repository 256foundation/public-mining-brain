# docs.hashcore.com — Firmware web UI: Mining (Pools, Cooling, Performance/Auto-tune)

> Registry ID: vnish-site
> Source: https://docs.hashcore.com/raw/en/firmware/obzor-veb-interfeysa/mining.md (HTTP 200)
> Collected: 2026-10-10
> Published: n/d (live docs)
> Posture: verbatim
> As-Of: 2026-10-10


Verbatim raw-markdown export (Mintlify /raw/ route).

---

# Mining

> In all tabs of this section, changes are applied in the same way: click `«Save»` in the top panel, then `«Apply»`. The `«Reset»` button reverts unsaved changes to their state at the time the page was opened. After applying, mining restarts.

### Pools

The **Mining** section tab. Used to configure mining servers and manage their usage order.
![Pools tab](/images/firmware/obzor-veb-interfeysa/fed06f59-6c29-8386-8bf9-81607860feee.png)

#### Pools List

Up to three independent Pools are supported. The miner always connects to Pool #1; if it's unavailable, it automatically switches to the next one in the list. The order of Pools can be changed by dragging and dropping. Switching between Pools occurs without device reboot.
Each Pool is configured with three parameters:

- **URL:** Server address and port, for example: `btc.viabtc.com:3333`. Clicking on the field displays a list of pre-configured Pools with auto-completion of the address upon selection.
![List of pre-configured pools](/images/firmware/obzor-veb-interfeysa/ffa06f59-6c29-83f5-8047-81fdb1cb7143.png)
- **Worker:** The Worker name in the Pool. The format depends on the specific Pool's requirements. For example, for ViabtcPool, the Worker is created in the format `userID.workerID`, where WorkerID consists of digits and lowercase letters, no more than 128 characters. If your userID is `viabtc`, the Worker name could be `viabtc.001`. Check the requirements in your Pool settings.
- **Password:** Worker password. Optional, check the requirements in your Pool settings.

#### HashCore Proxy (optional)

A free VNISH product for centralized management of miner connections to Pools. Instead of each device connecting directly to a Pool, all connections pass through a single point. This reduces network channel load and provides automatic failover to a backup Pool in case of connection loss.
To connect, you need to deploy a HashCore Proxy server on a separate machine and specify its IP address as the URL for the first Pool.
Learn more: [HashCore Proxy documentation](https://docs.hashcore.com/en/proxy/about-hashcore-proxy/system-description).

### Cooling

The **Mining** section tab. Manages the device's temperature mode. Three modes are available:

#### Auto

![Auto cooling mode](/images/firmware/obzor-veb-interfeysa/9ac06f59-6c29-8314-a14f-819567ab4918.png)
The Firmware automatically adjusts fan speeds based on chip temperature. This is the default mode.
Available parameters:

- **Target Temperature:** The chip temperature in °C that the system automatically maintains by adjusting fan speeds. Recommended value is 65°C.
- **Minimum Number of Fans:** The minimum number of working fans required for the device to operate. Default is 4. Used if the actual number of fans differs from the standard.
- **Fan Speed Limit:** A slider to set the permissible range of fan speeds in percentages (default 10–100%). The Firmware regulates speeds within the specified range based on the target temperature. If the range is set too narrowly, the target temperature may not be maintained.

#### Manual

![Manual cooling mode](/images/firmware/obzor-veb-interfeysa/12306f59-6c29-8276-a0eb-8155e4b1162e.png)
Fan speed is set manually to a fixed value, regardless of temperature. The system does not automatically control temperature. You must monitor chip temperature readings yourself.
Available parameters:

- **Minimum Number of Fans:** The minimum number of working fans required for the device to operate. Default is 4.
- **Fan Speed:** A slider sets a fixed fan speed value in percentages.

#### Immersion

![Immersion cooling mode](/images/firmware/obzor-veb-interfeysa/a2c06f59-6c29-8255-ba5a-81c53b966f08.png)
Designed for liquid-cooled setups where temperature control is based on the liquid's inlet and outlet temperatures.
**Minimum Liquid Temperature for Startup:** The minimum liquid temperature in °C at which the miner is allowed to start. If the liquid temperature falls below the set value, the miner stops. Default is 20°C.

### Performance

The **Mining** section tab. Manages Overclocking Presets, frequencies, voltage, and Hashboard monitoring.

#### Overclocking Preset

![Overclocking Preset selection](/images/firmware/obzor-veb-interfeysa/a2606f59-6c29-8308-b90b-01ec9432f408.png)
A dropdown list for selecting the miner's operating mode. Defines the set of available settings.
Three modes are available:

- **No Preset:** Parameters are set manually via global voltage and frequency sliders. Hashboard and chip-level frequency adjustment is available. Automatic Preset switching is unavailable.
- **With Preset, Auto-Switching Off:** The miner operates on the selected Preset with saved Auto-tune settings. The Preset does not change automatically. Hashboard and chip-level frequency adjustment is unavailable.
- **With Preset, Auto-Switching On:** The miner operates on the selected Preset and automatically increases or decreases it depending on temperature, fan speed, and power consumption. Hashboard and chip-level frequency adjustment is unavailable.
The icon next to the list opens the **Reset Auto-tune Settings** window, which resets the saved Auto-tune results for the selected Preset. After resetting, Auto-tune will be performed again.
![Reset Auto-tune Settings window](/images/firmware/obzor-veb-interfeysa/a1c06f59-6c29-8207-b4cc-019ac1e558eb.png)

#### Auto-tune

During ASIC chip manufacturing, even microscopic deviations in the technological process lead to each chip performing slightly differently. Additionally, the quality of device assembly affects performance. With the same frequency and voltage, different chips consume varying amounts of watts and produce different Hashrates. Standard Firmware does not account for this and applies identical parameters to all chips: strong chips operate below their potential, while weak ones operate at the edge of stability.
VNISH solves this problem. When an Overclocking Preset is selected, the system individually tests each chip and selects the optimal frequency for it through trial and error:

- strong chips are Overclocked to their maximum stable frequency;
- weak chips are set to lower frequencies for stable operation without failures.
As a result, the miner delivers the maximum Hashrate within the selected Preset, instead of an averaged compromise for all chips at once.

> ⚠️ Auto-tune only works when an Overclocking Preset is selected. In **No Preset** mode, frequency is set manually: globally, at the Hashboard level, or for individual chips.
> When automatic Preset switching is enabled, the system switches between Presets depending on conditions. If a Preset has been Auto-tuned previously, the saved settings are used. If a Preset has not yet been configured, Auto-tune starts automatically when switching to it.
> **Example**
> Let's take the `3870 watt ~ 212 TH` Preset. VNISH distributes power evenly among three Hashboards, 1290 W for each. First, a base frequency is set for all chips, and the system evaluates the Hashrate and consumption of each. Then, calibration is performed individually for each chip: the system adjusts the frequency for each chip on the Hashboard.
> **Auto-tune Workflow Diagram**![Auto-tune Workflow Diagram](/images/firmware/obzor-veb-interfeysa/f9706f59-6c29-825e-a09a-819844f349e3.png)
> This diagram shows a row of 12 chips. On a real device, chips are arranged in chains on the Hashboard. On an Antminer S21, there are 110 chips on one Hashboard. The number of chips may vary depending on the miner model.
> Auto-tune results depend on the specific equipment's condition and operating environment: chip quality, cooling, room temperature. Two identical miners may show different efficiency gains.
> Temperature directly affects Auto-tune results: at high chip temperatures, the system is forced to reduce the frequency to stay within the Preset's power limit, and Hashrate drops with the same consumption. It is recommended to run Auto-tune during the coolest part of the day if the room is not climate-controlled.
> The process takes some time. During this time, the Hashrate will fluctuate noticeably (this is normal). After completion, the Preset is applied instantly without re-configuration.

#### Mode 1: No Overclocking Preset

![No Overclocking Preset mode](/images/firmware/obzor-veb-interfeysa/4b806f59-6c29-83c8-a424-01dfef8dddb4.png)
In `No Preset` mode, parameters are set manually. Automatic Preset switching is unavailable.

- **Global Voltage:** The voltage level on the Hashboards in volts. A slider with **−** / **+** buttons. The **«Reset to Nominal: 14V»** button returns the nominal value of 14 V.
- **Global Frequency:** The base frequency for all Hashboards in MHz. A slider with **−** / **+** buttons. The **«Reset to Nominal: 485 MHZ»** button returns the factory default value.
**Frequency Priority:**
- **Global Frequency:** Applied to all Hashboards where no specific frequency is set.
- **Hashboard Frequency:** Overrides the global frequency for a specific Hashboard.
- **Domain Frequency:** Overrides the Hashboard frequency for a chip chain.
- **Chip Frequency:** Highest priority, overrides the domain frequency for a specific chip.
**Hashboard Frequency Adjustment**
Frequency is set by a slider in the Hashboard block. For quick adjustment, `+5 Mhz`, `-5 Mhz`, `-10 Mhz` buttons are available. The **«Use Global»** button resets the Hashboard frequency to the global value.
![Hashboard frequency adjustment](/images/firmware/obzor-veb-interfeysa/68406f59-6c29-83b9-8c9b-81843141a164.png)**Chip Frequency Adjustment**![Chip frequency adjustment](/images/firmware/obzor-veb-interfeysa/c9306f59-6c29-83a4-9b48-01d21f47332c.png)
Clicking on a specific chip in the grid opens a panel with its parameters:
- **Hashrate:** Current chip Hashrate in GH/s.
- **Errors:** Number of chip errors.
- **Chip Frequency:** Individual frequency of a specific chip. By default, the Hashboard frequency (`chain`) is used. Set by a slider or **−** / **+** buttons with a 1 MHz step.
- **Domain Frequency:** Frequency of the entire chip chain (domain) on the Hashboard. Changed by **−** / `+` buttons with a 1 MHz step. If an individual frequency is set for a specific chip, it operates at that frequency; other chips in the domain use the domain frequency.
Individual chip frequency adjustment is applied when a specific chip overheats. This can occur due to uneven thermal paste application or chip degradation. Reducing the frequency helps stabilize its operation without affecting other chips.

#### Mode 2: **With Overclocking Preset, Auto-Switching Off**

The miner operates on the selected Preset with saved Auto-tune settings. The Preset does not change automatically.
When a Preset is selected for the first time, Auto-tune has not yet been performed. The miner starts operating with the Preset's basic parameters. After Auto-tune is complete, the settings are saved in the Preset and applied instantly upon subsequent selection without re-configuration.

#### Mode 3: With Overclocking Preset, **Auto-Switching On**

![Auto-switching profiles toggle](/images/firmware/obzor-veb-interfeysa/14406f59-6c29-833b-83c9-01eaad164182.png)
When an Overclocking Preset is selected, the **Auto-Switch Presets** toggle becomes available.
When enabled, the **Auto-Switch Presets Options** block appears.
![Auto-Switch Presets Options block](/images/firmware/obzor-veb-interfeysa/20b06f59-6c29-824f-bf21-01f9e4b8c662.png)
The system continuously monitors chip temperature, fan speed, and power consumption, and automatically increases or decreases the Preset without user intervention:

- there is a temperature and cooling reserve → Preset increases;
- miner overheats or consumes too much → Preset decreases.
**Auto-Switch Presets Options:**
- **Increase Preset at Low Temperature:** The chip temperature threshold below which the system increases the Preset. Range: 20–85°C.
- **Decrease Preset at High Temperature:** The chip temperature threshold above which the system decreases the Preset. Range: 25–90°C.
- **Parameter Measurement Time:** The interval for averaging metrics before switching Presets. Range: 1–10 minutes. Recommended value is 5 minutes.
- **Increase No Higher Than:** The maximum Preset to which the system can increase performance.
- **Decrease No Lower Than:** The minimum Preset below which the system will not drop.
- **Override Top Preset:** In case of an error or instability at the current maximum Overclocking Preset, the system automatically reduces it to the last stable one.

#### Details: Auto-Switch Presets Logic

<accordion-item title="**When the Overclocking Preset Does Not Change**">

The Preset remains at the current level if:

- Auto-switching is disabled.
- A Preset change is already in progress: initiated manually or by the system itself.
- Auto-tune is running, the miner is not yet ready to change Presets.
- The Preset has reached its permissible limit (maximum or minimum).
- Less than 5 minutes have passed since mining started.
- Less than the specified check interval has passed since the last Preset change.
- *(For increasing only)* Less than 30 minutes have passed since the last Preset decrease. This prevents frequent up-and-down switching.

</accordion-item>

<accordion-item title="**When the Overclocking Preset Increases**">

The system increases the Preset if the following conditions are met simultaneously:

- maximum chip temperature is below the increase threshold — there is a thermal reserve;
- in auto-cooling mode, fans operate below 90% — the cooling system is not exhausted.
The system will not increase the Preset if:
- the PSU is approaching its temperature limit;
- consumption has reached ~95% of the power limit, and the next step would exceed permissible consumption;
- the Preset was just decreased due to power excess, and the system is waiting before retrying.

</accordion-item>

<accordion-item title="**When the Overclocking Preset Decreases**">

The system decreases the Preset if:

- maximum chip temperature has reached the decrease threshold;
- in auto-cooling mode, fans have reached 100% — the cooling system is exhausted.
In some situations, the Preset is decreased immediately, without waiting for the check interval:
- the PSU is overheating;
- the power limit has been exceeded;
- the Preset was found to be above the maximum permissible — the system automatically returns it to the allowed range.

</accordion-item>

<accordion-item title="**PSU Protection**">

The system uses three temperature thresholds relative to the critical PSU temperature (default 90°C):
`      Critical − 4°C (86°C) — Preset increase blocked       Critical − 2°C (88°C) — Preset immediately decreases       Critical      (90°C) — Emergency protection, hard stop + error      `
As the PSU heats up, the system first stops increasing (86°C), then starts decreasing (88°C), and only if the temperature still reaches 90°C — emergency protection is triggered.

</accordion-item>

<accordion-item title="**Power Limit**">

Applied if the PSU transmits consumption data and the power limit is enabled in the settings. The system calculates two thresholds from the set limit:

- Operating Ceiling = Limit × 97% — if exceeded, the Preset immediately decreases.
- Increase Block = 95% of the operating ceiling — if reached, Preset increase is blocked.
For example, with a 3000 W limit: increasing stops at ~2765 W, decreasing starts at ~2910 W.
`    Operating Ceiling          = 3000 × 0.97  ≈ 2910 W  → above this — Overclocking Preset immediately decreases     Increase Block     = 2910 × 0.95  ≈ 2765 W  → above this — Overclocking Preset increase is blocked    `

</accordion-item>

#### Hashboard Management

![Hashboard management interface](/images/firmware/obzor-veb-interfeysa/64206f59-6c29-83a3-9011-01a5e0a6570f.png)
Below the Overclocking settings block, all miner Hashboards are displayed. For each Hashboard, a separate block with detailed chip information is available.
The header of each Hashboard displays the current frequency and its source, for example: `490 MHz / Global`.
The icon in the bottom right corner of the block shows the Hashboard's stock data:
![Hashboard stock data icon](/images/firmware/obzor-veb-interfeysa/68606f59-6c29-8271-a9b7-8133b3b4584f.png)

- Hashboard Model;
- Serial Number;
- Chip Bin;
- Factory Frequency;
- Factory Voltage;
- Stock Hashrate.
**Hashboard Menu**
Clicking on the Hashboard name opens a menu:
![Hashboard menu](/images/firmware/obzor-veb-interfeysa/b8f06f59-6c29-8266-8e18-01c3402c0528.png)
- **Hashboard View:** Switches the chip display mode:

  - *Hashrate:* Hashrate of each chip in GH/s.
  - *Errors:* Number of errors for each chip.
  - *Heatmap:* Temperature of each chip.
  - *Sensors:* Temperature of two built-in Hashboard sensors, indicating their location on the topological map.
  - *Frequencies:* Operating frequency of each chip. If a chip is configured individually, its value is displayed; if the Hashboard or global frequency is used, the `chain` status is displayed.
- **Operations:** Available only in **No Preset** mode:

  - *Reset Chip Settings*: Resets individual chip settings, Hashboard or global parameters are applied.
  - *Reset All Settings:* Resets all Hashboard and chip settings, global frequency and voltage are applied.
- **Enabled:** Toggle for enabling/disabling the Hashboard. Disabling requires a reboot. The miner will continue operating on the remaining Hashboards.

### Advanced

![Advanced settings tab](/images/firmware/obzor-veb-interfeysa/f8f06f59-6c29-82e6-9c03-0175fcdde046.png)
The **Mining** section tab. Contains low-level parameters for equipment protection, behavior during failures, and recovery automation.
The section is divided into three blocks:

- **Control:** Monitoring and protection parameters: temperature, Hashrate, and power thresholds at which the system reacts.
- **Other:** Settings for miner behavior during startup, shutdown, and abnormal situations.
- **Danger Zone:** Functions that can lead to equipment damage if used incorrectly.

> ⚠️ Any changes in this section are made at your own risk.
> 
> <accordion-item title="**Possible Scenarios:**">
> 
> 
> 
> </accordion-item>

- **Temperature Issues**
If the miner overheats or individual chips run hotter than others, see:
- Critical Chip Temperature;
- Adapt Voltage by Temperature;
- Automatic Chip Power Regulation.
- **Unstable Operation**
If Hashrate drops or chains break, refer to:
- Restart on Low Hashrate;
- Check Chain Integrity;
- Check Domain Balancing;
- Auto Re-tune on Chain Break.
- **Faulty Hashboard**
If one Hashboard fails and you need to continue operating on the remaining ones, refer to:
- Minimum Number of Working Chains;
- Allow Disabling Chains Without PIC.
- **Startup Management**
If you need to quickly start the miner, synchronize a farm's startup, or restore operation after a power outage, refer to:
- Fast Startup;
- Mining Startup Delay Range;
- Restore Miner State on Boot;
- Start Miner in Pause Mode;
- Offline Mining.
If a temperature sensor fails:
- Ignore Non-functional Temperature Sensors.
If a sensor works but shows anomalous values:
- Ignore Chip Temperature Sensors.
:::

### Control

![Control settings block](/images/firmware/obzor-veb-interfeysa/65006f59-6c29-8265-aac0-010fca33cecb.png)

<accordion-item title="**Restart on Low Hashrate**">

![Restart on Low Hashrate setting](/images/firmware/obzor-veb-interfeysa/7e106f59-6c29-83cf-82bf-017f6b1e5163.png)
Automatic mining restart if performance drops below a set threshold.
Set as a percentage of theoretical Hashrate (0–99%, where 0 means the function is disabled). Theoretical Hashrate is calculated by the formula: `(Chip Frequency × Number of Cores) / 1000`
Function behavior:

- check starts 5 minutes after mining begins (10 minutes with fast startup);
- repeats every 90 seconds;
- does not work during Auto-tune, Preset changes, or in the first 3 minutes after startup.

</accordion-item>

<accordion-item title="**Max. Number of Restarts**">

![Max. Number of Restarts setting](/images/firmware/obzor-veb-interfeysa/86006f59-6c29-8228-a018-01c582517450.png)
Limits the number of consecutive restart attempts in case of errors.
If set to `0`, no restart is performed, and the miner immediately enters an error state.

</accordion-item>

<accordion-item title="**Critical Chip Temperature**">

![Critical Chip Temperature setting](/images/firmware/obzor-veb-interfeysa/79c06f59-6c29-8275-8411-81a0b4a31120.png)
The temperature limit at which mining immediately stops to protect the equipment.
Range: 50–120°C, default 90°C. The system relies on the temperature of the hottest chip or the Hashboard sensor if chip-level measurement is unavailable.

</accordion-item>

<accordion-item title="**Minimum Number of Working Chains**">

![Minimum Number of Working Chains setting](/images/firmware/obzor-veb-interfeysa/88106f59-6c29-8313-8213-01a07263c5a1.png)
Stops the miner if the number of functional Hashboards falls below the specified number.
The system checks each chain regardless of whether it is enabled in the settings. For example: with 3 Hashboards and a value of 3, the failure of one Hashboard will stop the miner. With a value of 2, the miner will continue operating on two functional Hashboards.

> ⚠️ For miners without PIC controllers, to disable a faulty Hashboard, you must additionally enable the **Allow Disabling Chains Without PIC** function.

</accordion-item>

<accordion-item title="**Power Limit**">

![Power Limit setting](/images/firmware/obzor-veb-interfeysa/35f06f59-6c29-82c4-8f48-8150ca786f5b.png)
A hard limit on the actual power consumption of the device in watts.
When enabled, a limit value is set. If actual consumption exceeds the set limit, the system immediately reduces the Overclocking Preset regardless of temperature and other settings. It has the highest priority over all other power settings.

</accordion-item>

<accordion-item title="**Mining Startup Delay Range**">

![Mining Startup Delay Range setting](/images/firmware/obzor-veb-interfeysa/90006f59-6c29-83f8-9d1d-0132736a28b9.png)
Random delay before mining starts to evenly distribute the load on the electrical grid.
A range (0–300 seconds) is set — the system randomly selects a value within it for each device. Used when simultaneously starting a large farm of miners to prevent voltage spikes.

</accordion-item>

### Other

![Other settings block](/images/firmware/obzor-veb-interfeysa/07b06f59-6c29-8399-a911-8147f0fa2d33.png)

<accordion-item title="**Fast Startup**">

![Fast Startup setting](/images/firmware/obzor-veb-interfeysa/13c06f59-6c29-82f4-a872-013c2a9bc198.png)
Accelerated device initialization without standard delays.
Allows the miner to start in full operating mode within seconds (up to 15 seconds on some Hashboards). Critically important in scenarios where immediate load creation on the electrical grid is required.
Although the function is available on all devices, its effectiveness depends on the miner's hardware features. On some models (e.g., S21 Pro), the initialization pause is hardcoded into the hardware and is 120 seconds, so the function will have no effect.

> If a cooling countdown (120, 110, 100 seconds...) is visible in the logs during startup, fast startup does not work on this model.

</accordion-item>

<accordion-item title="**Check Voltage Settings**">

![Check Voltage Settings setting](/images/firmware/obzor-veb-interfeysa/41006f59-6c29-820d-9e66-8199f24b631d.png)
Checks the correspondence of the voltage supplied by the PSU to the chain with the set parameters.
The function is activated with any voltage change: manual adjustment, Auto-tune operation, or system corrections. The system, via the PIC controller, measures the actual voltage on each chain and compares it with the value the system attempted to set. If the voltage does not match, the problematic chain or the entire miner stops operating.
The voltage from the PSU to the chain is monitored, not the internal chip voltage.

- **Miners with PIC controllers:** If there is a mismatch, only the problematic chain is disabled.
- **Miners without PIC controllers:** The function has no effect, as the hardware does not allow measurements.

</accordion-item>

<accordion-item title="**Check Domain Balancing**">

![Check Domain Balancing setting](/images/firmware/obzor-veb-interfeysa/77206f59-6c29-83bd-a247-81b19e193609.jpg)
Checks the uniformity of voltage distribution and stability of chip operation within domains.
If a domain's Hashrate drops — for example, due to a temperature spike or unstable operation of individual chips — the system performs a core reset: chip cores restart, and the miner resumes normal operation without a full device reboot. The check is performed every 10 minutes.
The function does not work if:

- Auto-tune is running;
- the miner has not completed initialization;
- a Preset change is in progress;
- the miner is not in a mining state;
- less than 2 minutes have passed since mining started.

</accordion-item>

<accordion-item title="**Check Chain Integrity**">

![Check Chain Integrity setting](/images/firmware/obzor-veb-interfeysa/12506f59-6c29-82da-b13a-01b35a2d6faf.png)
Checks the integrity of chip chains to prevent incorrect equipment operation.
Periodically polls all chips on the Hashboards. If a chip that does not respond to requests is detected:

- **Miners with PIC controllers:** The system disables only the chain (Hashboards) on which the unresponsive chip was found;
- **Miners without PIC controllers:** In case of any chip failure, the entire miner is completely shut down.
If the function is disabled, the miner will continue to operate even with unresponsive chips.
The Hashrate of the problematic chain decreases, and problematic chips are displayed in red in the **Mining → Performance** section.
If Hashboard problems are detected, see section 5.3 Hashboard Problems.

</accordion-item>

<accordion-item title="**Adapt Voltage by Temperature**">

![Adapt Voltage by Temperature setting](/images/firmware/obzor-veb-interfeysa/20806f59-6c29-822d-a446-012f8850b1b1.png)
Automatic adjustment of chip voltage depending on temperature to maintain stable Hashrate.
Colder chips require more voltage for stable operation, while hotter chips require less. The system monitors these changes and automatically adjusts the voltage continuously.
For example: the device operates at an ambient temperature of 25°C and a target chip temperature of 65°C. If the external temperature drops to 15°C, the fans will slow down to maintain the target 65°C. At the same time, colder chips will require higher voltage for stable mining — the system will adjust it automatically.
Behavior depending on cooling mode:

- **Auto:** If fan speed increases by 4% compared to the previous measurement, the system reduces voltage.
- **Manual** and **Immersion:** If temperature increases by 3%, voltage decreases; if it gets colder, it increases.
The function does not work if:
- the miner has not completed initialization;
- the final operating voltage is not set (Global voltage / Volt control in the Performance section);
- a Preset change is in progress;
- operating frequencies are not set;
- Auto-tune is running.

</accordion-item>

<accordion-item title="**Continue Mining After Reboot**">

![Continue Mining After Reboot setting](/images/firmware/obzor-veb-interfeysa/82706f59-6c29-820c-93d6-8165eec434a8.png)
Automatically starts mining after a reboot or power outage, even if pause was previously enabled.

- **Enabled:** The miner always resumes mining after a reboot or error, ignoring the previous state.
- **Disabled:** The miner restores the last state before shutdown or error.

</accordion-item>

<accordion-item title="**Start Miner in Pause Mode**">

![Start Miner in Pause Mode setting](/images/firmware/obzor-veb-interfeysa/ba906f59-6c29-8219-8675-81d17106df94.png)
Upon each startup, the miner automatically enters pause mode regardless of the reason for startup.
The Firmware first fully checks the equipment's functionality and only after all checks are complete does it enter pause mode. Mining is then started manually.

</accordion-item>

<accordion-item title="**Quiet Mode**">

![Quiet Mode setting](/images/firmware/obzor-veb-interfeysa/67006f59-6c29-83f1-af36-816c492f2eab.png)
Reduces fan speed to 50% during device startup and shutdown to reduce noise.
When activated, fan speed is limited to 50% during miner startup or shutdown. Due to reduced speeds, chip cooling time increases — the miner will start and stop longer than usual.

</accordion-item>

<accordion-item title="**Decrease Preset on Error**">

![Decrease Preset on Error setting](/images/firmware/obzor-veb-interfeysa/85506f59-6c29-827b-9c2d-01c455a67e59.png)
Automatically reduces the Overclocking Preset by one level in case of overheating or chain errors.
Reasons for triggering:

- **Overheating:** Reducing the Preset decreases Overclocking and device operating temperatures.
- **Chain Break:** PSUs have their own consumption limit. If exceeded, the PSU goes into protection and cuts power, chips stop responding. The system interprets this as exceeding the PSU limit and reduces the Preset to decrease the load.

</accordion-item>

<accordion-item title="**Auto Re-tune on Chain Break**">

![Auto Re-tune on Chain Break setting](/images/firmware/obzor-veb-interfeysa/74806f59-6c29-8346-a044-81422a4b279b.png)
Automatic re-tuning when critical errors occur in chip chains.
If a chain break is detected, the system resets the current Preset settings and restarts Auto-tune.
Reasons for triggering:

- **Chain Integrity Violation:** An error detected during a regular check.
- **PSU Limit Exceeded:** A chain break occurred because the PSU went into protection due to exceeding the power limit.

</accordion-item>

<accordion-item title="**Offline Mining**">

![Offline Mining setting](/images/firmware/obzor-veb-interfeysa/95206f59-6c29-82ab-a087-01b5f8ab7b05.png)
Allows the device to continue operating without an internet connection.
By default, if the internet connection is lost, the miner pauses until the connection is restored. When this function is enabled, the miner continues computations, chips receive dummy tasks, and maintain load. Hashrate is present, but it is not transmitted to the Pool, and no revenue is accrued.
Applied in two scenarios:

- **Power Plant Contract:** For some operators, it is important to maintain a constant load on the grid regardless of internet availability.
- **Equipment Protection at Low Temperatures:** Stopping the miner in freezing weather can lead to overcooling and device damage.

</accordion-item>

<accordion-item title="**Automatic Chip Power Regulation**">

![Automatic Chip Power Regulation setting](/images/firmware/obzor-veb-interfeysa/58706f59-6c29-82e0-817d-819476e3dfb0.png)
Balancing frequencies within a row to equalize chip temperatures without Hashrate loss.
The system detects chips that run hotter than others (e.g., due to uneven thermal paste application) and redistributes frequencies: reducing the load on hot chips and increasing it on cold ones. The total Hashrate of the row does not decrease.

- prevents wear and tear of individual chips from overheating;
- allows operation at high Presets even with minor cooling defects.

> This function is only available on models with individual chip temperature sensors and Heatmap support.

</accordion-item>

### Danger Zone

![Danger Zone settings block](/images/firmware/obzor-veb-interfeysa/4ca06f59-6c29-8362-90b5-0187dd1a2ad7.png)

<accordion-item title="**Ignore Non-functional Temperature Sensors**">

![Ignore Non-functional Temperature Sensors setting](/images/firmware/obzor-veb-interfeysa/e1e06f59-6c29-83e6-a50e-810ae2f3adfe.png)
Allows operation to continue if front temperature sensors are faulty.
The system divides sensors into two groups:

- **Front Sensors (inlet)** — record the temperature of incoming air. If front sensors are faulty and the function is enabled, the miner will continue to operate.
- **Rear Sensors (outlet)** — reflect the actual chip temperature. The miner will continue to operate as long as at least one rear sensor is functional. If all rear sensors fail, the miner immediately shuts down.

</accordion-item>

<accordion-item title="**Allow Disabling Chains Without PIC**">

![Allow Disabling Chains Without PIC setting](/images/firmware/obzor-veb-interfeysa/5da06f59-6c29-835a-82a8-01152127f7b7.png)
Allows software disabling of faulty Hashboards on miners without PIC controllers to continue operation on the remaining Hashboards.
On miners with PIC controllers, the `Minimum Number of Working Chains` parameter works independently; the system can physically cut power to a faulty Hashboard via the controller. On miners without PIC, this is not possible — to disable a Hashboard, you must enable **this function**.
Applied when one of the Hashboards has failed and the miner has stopped. The `Minimum Number of Working Chains` parameter is reduced, and this function is enabled — the miner starts on the functional Hashboards. Voltage continues to be supplied to the faulty Hashboard, but it is held in a constant reset state and does not mine.

> ⚠️ According to Bitmain recommendations, prolonged exposure of a Hashboard to voltage in a reset state can lead to component burnout. Use at your own risk.

</accordion-item>

<accordion-item title="**Ignore Chip Temperature Sensors**">

![Ignore Chip Temperature Sensors setting](/images/firmware/obzor-veb-interfeysa/f4106f59-6c29-8375-8460-017d4eeb10cc.png)
The system ignores clearly erroneous readings from individual chips during temperature control and protection.
This is relevant for models with individual sensors on each chip: L9, S21, T21, and similar. During polling, chip sensors may provide clearly erroneous values, such as abnormally high numbers or sudden jumps of 50°C or more, indicating an incorrect sensor reading rather than actual overheating.
When this function is enabled, such incorrect readings are ignored when making protection decisions. Temperature control and overheating protection continue to operate based on general Hashboard sensors located outside the chips.

</accordion-item>

<accordion-item title="**Bad Chip Tuner Hashrate Threshold**">

![Bad Chip Tuner Hashrate Threshold setting](/images/firmware/obzor-veb-interfeysa/9f706f59-6c29-8296-9961-0101d7ed4756.png)
Sets a threshold by which the Auto-tuner determines how well a chip is performing and whether it should be optimized.
Since it's impossible to control voltage individually for each chip, the same voltage is supplied to the entire miner, and some chips are physically unable to operate at full power. The tuner analyzes the Hashrate of each chip and compares it to the threshold. Chips above the threshold are optimized; chips below the threshold are deemed "bad" and are set to lower frequencies. Even if the voltage is increased for the entire miner, such a chip will still be ignored — the threshold defines the physical limit of the chip's capabilities, not voltage settings.
**Threshold Adjustment**
The chosen value directly affects the depth of device optimization:

- **High Threshold (e.g., 80%):** The system is more demanding of chips. The higher the threshold, the fewer chips the tuner will attempt to bring to nominal Hashrate during the check. Auto-tune runs faster, and weak chips operate stably at reduced frequencies. Recommended value.
- **Low Threshold:** The lower the threshold, the more chips the system will try to bring to nominal power. Auto-tune takes longer, but the system attempts to bring more chips to nominal Hashrate.

</accordion-item>
