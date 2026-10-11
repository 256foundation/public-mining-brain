# LuxOS Docs — Advanced Features (stratum, auto-update, temp/fan, hashboard, PSU settings)

> Registry ID: luxos-docs
> Source: https://docs.luxor.tech/firmware/features/advancedfeatures
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


<Callout title="Advanced Features">
  The following settings can be found in LuxOS under Settings -> Advanced Settings
</Callout>

## Stratum Settings [#stratum-settings]

### Smart Switch [#smart-switch]

Enables Luxminer to automatically revert to the primary mining pool when it becomes available again. This helps ensure maximum mining efficiency.

* **True**: Enabled.
* **False**: Disabled.

### Smart Switch Seconds [#smart-switch-seconds]

Specifies how often (in seconds) Luxminer checks if the primary pool is available.
Default: `60`

### Timeout Seconds [#timeout-seconds]

Defines the timeout in seconds for each connection attempt to a mining pool.
Default: `5`

### Max Errors [#max-errors]

Sets the maximum number of errors allowed before switching pool priority.
Default: `5`

### Backoff On Error [#backoff-on-error]

Enables incremental backoff on subsequent connection errors, helping the miner avoid repeated failed connections when the network is unstable.

* **True**: Enabled.
* **False**: Disabled.

### Hash On Disconnect [#hash-on-disconnect]

Enables the miner to continue hashing with no pool or network connectivity.

* **True**: Enabled.
* **False**: Disabled (default).

![Stratum settings](/images/stratumsettings.png)

## Auto Updates [#auto-updates]

### Source [#source]

<Callout type="info" title="Firmware Branches">
  Selecting a firmware branch will impact both automatic updates and manual firmware updates.
</Callout>

Specifies the type of update LuxOS will download:

* **Stable**: Production-ready updates.
* **Preview**: Beta versions for early access.
* **Testing**: Experimental updates for advanced users.
* **Custom**: Luxor-provided URL for specialized builds.

### Timeout [#timeout]

Defines the interval (in minutes) for checking new updates.
Default: `60`

### On Timeout [#on-timeout]

Determines the action LuxOS takes when a Timeout interval occurs:

* **Off**: No action.
* **Download**: Downloads updates but does not apply them.
* **Apply**: Downloads and applies updates.
* **Full**: Downloads, applies updates, and restarts the miner.

### On Startup [#on-startup]

Determines the action LuxOS takes on miner startup:

* **Off**: No action.
* **Download**: Downloads updates but does not apply them.
* **Apply**: Downloads and applies updates.
* **Full**: Downloads, applies updates, and restarts the miner.

### On User [#on-user]

Determines the action triggered manually via the GUI or updaterun API:

* **Off**: No action.
* **Download**: Downloads updates but does not apply them.
* **Apply**: Downloads and applies updates.
* **Full**: Downloads, applies updates, and restarts the miner.

![Auto update settings](/images/autoupdates.png)

## Temperature Control [#temperature-control]

### Required Critical Temperature Sensors per Board [#required-critical-temperature-sensors-per-board]

Specifies the minimum number of functional critical temperature sensors required per hashboard. If this threshold is not met, the behavior is defined in [Critical Temperature Sensor Behavior](./criticaltempsensorbehavior) based on various factors of the hardware architecture.

**Options:**

**Antminer:** `0`, `1`, `2`, `3` (amount of critical temperature sensors per hashboard can vary based on model)

**Whatsminer:** `0`, `1`

### Max Bad Readings [#max-bad-readings]

Sets the maximum number of consecutive bad temperature readings before considering the sensor "broken."
Default: `10`

### Bad Avg Threshold [#bad-avg-threshold]

Determines the average temperature threshold above which readings are considered unreliable.
Default: `2`

![Temperature Control settings](/images/temperaturecontrol.png)

## Fan Control [#fan-control]

### Power Off Speed [#power-off-speed]

The fan power when the psu is powered off because of curtailment or a power-off event. Default: `20`

### Minimum Fan Speed [#minimum-fan-speed]

The minimum speed that the automatic fans can use. Default: `20`

### Maximum Fan Speed [#maximum-fan-speed]

The maximum speed that the automatic fans can use. Default: `100`

### Minimum Required Fans [#minimum-required-fans]

The minimum number of fans that must be operational for the system to run. Options:

**Antminer:** `1`, `2`, `3`, `4`

**Whatsminer:** `1`, `2`

### Quiet Fan Startup [#quiet-fan-startup]

Sets fan initialization speed to minimum fan speed.

* **True**: Enabled.
* **False**: Disabled (default).

### Immersion Mode [#immersion-mode]

Immersion mode disables all fans.

* **True**: Enabled.
* **False**: Disabled (default).

![Advanced Features, Fan Control](/images/Fancontrol.png)

## Hashboard Settings [#hashboard-settings]

### NoPIC Shutdown [#nopic-shutdown]

LuxOS is able to run any miner (PIC & NoPIC) with a hashboard powered off. However, by default, LuxOS will power off NoPIC miners by powering off hashboards and disabling the PSU when a hashboard fails preventing from sending voltage to failing hashboards. This feature can be disabled by the user. To do so, go into `Settings`, click on the `Advanced Settings` section, then scroll down to disable the `NoPIC Hashboard Protection` setting. Alternatively, users can disable this functionality through the API by calling the [hashboardoptsset](/firmware/api/luxminer/hashboardoptsset) command or with the **Fault Recovery** bulk action in [Commander](/platform/commander/automation/bulk-actions).

* **True**: Enabled (default).
* **False**: Disabled.

### OverTempAutoRecovery [#overtempautorecovery]

As standard behavior, LuxOS will automatically attempt to recover a hashboard that was powered off after a failure, retrying within configurable rate limits (per hour and per day) and cooldown windows before giving up once the board hits the consecutive-error threshold. This behavior can be disabled by the user. To do so, go into `Settings`, click on the `Advanced Settings` section, and disable the\
`Over Temp Auto Recovery` setting. Alternatively, users can disable this functionality through the API by calling the [hashboardoptsset](/firmware/api/luxminer/hashboardoptsset) command or with the **Fault Recovery** bulk action in [Commander](/platform/commander/automation/bulk-actions). If this feature is disabled, a failed hashboard is powered off and left off, with no automatic recovery attempts. The recovery limits themselves can be inspected and tuned via the [recoverctrl](/firmware/api/luxminer/recoverctrl) and [recoverctrlset](/firmware/api/luxminer/recoverctrlset) commands.

* **True**: Enabled (default).
* **False**: Disabled.

![Advanced Features, NoPIC Shutdown and OverTempAutoRecovery](/images/advancedfeatures.gif)

## PSU Control [#psu-control]

### PSU Bypass [#psu-bypass]

Gives the user the ability to hash with a psu that is unrecognized by LuxOS.

* **True**: Enabled.
* **False**: Disabled (default).

### Bypass Voltage [#bypass-voltage]

Available only when PSU Bypass enabled = **True**, allows the user to pass a static voltage value that LuxOS will use for power estimation calculations. Default: `12`

## Uninstall Firmware [#uninstall-firmware]

This option allows users to remove LuxOS from the miner.

To uninstall LuxOS:

1. Navigate to **Settings > Advanced Settings > Uninstall Firmware**, and select **Uninstall**.
2. Follow the on-screen instructions to complete the uninstall process.

![Uninstall LuxOS setting](/images/uninstall.png)
