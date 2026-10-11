# NiceHash Miner (official GitHub README, verbatim)

> Registry ID: nicehash
> Source: https://raw.githubusercontent.com/NiceHash/NiceHashMiner/master/README.md (repo: https://github.com/NiceHash/NiceHashMiner, default branch master, repo updated 2026-10-04)
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10

NOTE — JS-shell park: www.nicehash.com is a Vue SPA with no SSR content. Probed 2026-10-10 with Chrome 126 UA: https://www.nicehash.com/miner (HTTP 200, 965 B), https://www.nicehash.com/nicehash-miner (HTTP 200, 964 B), https://www.nicehash.com/support/mining-help/nicehash-miner/what-is-nicehash-miner (HTTP 200, 962 B) — all return an identical empty shell (`<div id="app"></div>`, noscript "We're sorry but client doesn't work properly without JavaScript enabled."). The sitemap (HTTP 200, 126,481 B, 2070 URLs) lists /nicehash-miner, /nhos-mining, /easymining, /firmware and ~dozens of /support/mining-help/nicehash-rig-manager/* pages (incl. quickminer-profit-switching), but none render server-side. This README is the product's canonical documentation surface; profitability-switching content is captured here.

Content below verbatim as served (HTTP 200, text/plain, 6,438 bytes).

---

# NiceHash Miner

- [Introduction](#introduction)
- [What are the benefits?](#benefits)
- [Features](#features)
- [Requirements](#requirements)
- [How to get&run it?](#run)
- [Where is the profit coming from?](#profit)
- [How to run NiceHash Miner only when profitability is high enough?](#highprofit)
- [Additional options](#options)
- [Troubleshooting](#troubleshooting)
- [How to report bugs and issues?](#bugs)

# Introduction

NiceHash Miner is a continuation of NiceHash Miner Legacy. This version is intended for beginners or experienced miners that want the quickest updates and highest hashrates, and are okay with customization of the antivirus. Please check out quick [guide](https://www.nicehash.com/guide/nicehash-miner-user-guide) about NiceHash Miner, so that your experience will be even better.

# What are the benefits?

NiceHash Miner is an advanced auto-miner that supports the latest algorithms and miners. No need to go through tons of configuration files, various mining software versions, configuration tuning or cryptocurrency coins market analysis. **Auto-tuning for best performance and efficiency**, automatic selection and runtime **automatic switching to most profitable cryptocurrency algorithm** are all integrated into NiceHash Miner and will enable you seamless, joyful and **profitable mining experience**.

# Features

- Easy one-click CPU mining for CPUs that support at least AES (only works on Windows x64).
- Easy one-click GPU mining for NVIDIA GPUs using microarchitecture (compute capability) SM 5.3+.
- Easy one-click GPU mining for AMD GPUs using any AMD GPU devices that supports OpenCL.
- Full 100% LHR Unlock with selected plugins.
- Integrated support for Simple Multi-Algorithm. Always mine most profitable algorithm.
- Integrated benchmarking tool. Run it only once before you start mining and after every hardware/driver/software upgrade.
- Watch-feature - automatically restart miner if crashed or hanged.
- Display current rate and your balance in real time.
- Auto update notifications.
- Much more...

# Requirements

- **Windows** 10 or newer operating system **64-bit**
- **[Note: Windows 10 is recommended and will provide you a much better user experience]**
- For CPU mining a modern CPU with AES support
- For AMD mining any AMD GPU with OpenCL support
- For NVIDIA mining any NVIDIA GPU with Compute capability (SM) 5.3 or newer
- **up-to-date patches** for OS
- **up-to-date drivers** for all GPUs
- **Reliable** internet connectivity
- For GPU Mining, **paging file size** of 60% of your total GPU VRAM memory
- Personal **Mining wallet** (you can create one by [registering](https://www.nicehash.com/support/general-help/account/creating-a-new-account) on NiceHash page)

# How to get&run it?

All you have to do is download zip package or installer exe from the [releases page](https://github.com/nicehash/NiceHashMiner/releases).
If you choose installer just run it and follow the instructions. In case of zip package extract it and run the miner.
After that enter your Bitcoin wallet address where you want to get your coins sent at - and you are ready to start mining and maximizing your profit.

**Note**: Windows 10 with .NET Framework 6.0 or higher and Microsoft Visual C++ Redistributable 2015 are required. However, if you encounter any issues when starting application (application would fail to start or errors/warnings about missing DLL files are displayed) you should download and install Microsoft **.NET Framework 6.0** and **Visual C++ Redistributable 2015 (vcredist_x64.exe)** (after installation a reboot might be required).

# Where is the profit coming from?

As a back-end NiceHash Miner relies on the NiceHash.com service. By running NiceHash Miner you're essentially selling the hashing power of your CPUs & GPUs to hashing power buyers. Those are using the hashing power to mine various cryptocurrency coins and support decentralized blockchain networks - similar to cloud computing - only that by running NiceHash Miner you're actually being a provider for the cryptocurrency mining hashing power. You are being part of a global compute power network, **empowering decentralized digital currencies**.

# How to run NiceHash Miner only when profitability is high enough?

Profitability of mining can go up and down that may be unprofitable to mine especially places with high electricity cost. By using the "MinimumProfit" settings, NiceHashMiner will stop mining if the current profits are below the minimum amount (in USD). This will help you mine during "profitable" times only.

# Additional options

Go to 'Settings' tab. Alternatively, you can manually modify \configs\General.json for general settings and \configs\device_settings_XXX.json (XXX is your device UUID) files for device benchmark settings (close NiceHash Miner first).

## General settings (selected farm/rig-management-relevant parameters; full table as served)

Parameter | Range | Description
-----------------|----------|-------------------
ConfigFileVersion | Version | This is to identify which version of NiceHashMiner did the config file is made from.
BitcoinAddress | valid BTC address | The address that NiceHashMiner will mine to.
WorkerName | text | To identify the computer on NiceHash web UI.
RigGroup | text | To identify the group your rig belongs to.
AutoStartMining | true or false | When set to true, NiceHashMiner will start mining on program start.
MinerAPIQueryInterval | number | Amount of time between each API call to get the latest stats from miner.
PauseMiningWhenGamingMode | true or false | When set to true, on steam game start, the mining with selected GPU will stop.
StartMiningWhenIdle | true or false | Automatically start mining when computer is idle and stop mining when computer is being used.
MinimumProfit | number | If set to any value, NiceHashMiner will stop mining if the calculated profit falls below the set amount.
MineRegardlessOfProfit | true or false | When set to true, NiceHashMiner will mine regardless of your mining profitability.
UseIFTTT | true or false | When set to true, NiceHashMiner will use the API Key you provide to notify you when profitability has gone below the profitability you have configured.
SwitchSmaTimeChangeSeconds | "lower": number, "upper": number | Set range for SMA check.
SwitchSmaTicksStable | "lower": number, "upper": number | Set range for stable algorithms ticks needed for switch.
SwitchSmaTicksUnstable | "lower": number, "upper": number | Set range for unstable algorithms ticks needed for switch.
KwhPrice | number | Set price for kWh, used for profit calculating.
SwitchProfitabilityThreshold | number | Threshold for algorithm switch. Lower this number is, faster switches will happen.
DisplayPureProfit | true or false | When set to true, net profit will be shown instead of gross.
AllowMultipleInstances | true or false | When set to true, multiple NiceHash Miner instances will be allowed to run at the same time.
CheckForMissingGPUs | true or false | When set to true, Nicehash Miner will check for missing GPUs every 5 minutes.
RestartMachineOnLostGPU | true or false | When set to true, script will be run on detected GPU dead.
DisableDeviceStatusMonitoring | true or false | When set to true, device status monitoring (temp, fan speed, etc.) will be disabled.
AutoUpdateNiceHashMiner | true or false | When set to true, NiceHash Miner will be updated automatically on the new release.
AutoUpdateMinerPlugins | true or false | When set to true, miner plugins will be automatically updated on the new releases.

(Additional rows in the original table cover HideMiningWindows, MinimizeMiningWindows, MinerRestartDelayMS, ApiBindPortPoolStart, DeviceToPauseUuid, EnableSSLMining, IdleCheckType, MinIdleSeconds, IdleWhenNoInternetAccess, DebugConsole, LogToFile, LogMaxFileSize, ShowDriverVersionWarning, DisableWindowsErrorReporting, ShowInternetConnectionWarning, IFTTTKey, Hwid, SwitchSmaTicksUnstable, DisplayCurrency, TimeUnit, AutoScaleBTCValues, Language, MinimizeToTray, DisplayTheme, ShowPowerColumns, GUIWindowsAlwaysOnTop, MainFormSize, UseSmaCache, Use Optimization profiles, RunAtStartup, ShowNotifications, DisableVisualCRedistributableCheck, ResolveNiceHashDomainsToIPs, ShowGPUPCIeBusIDs — see the verbatim repo README for the complete table.)

## Benchmark settings (per device)

Parameter | Range | Description
-----------------|----------|-------------------
DeviceUUID | text | Used for unique identification purposes in the config file (**DO NOT EDIT**)
DeviceName | text | Used for identification purposes in the config file (**DO NOT EDIT**)
Enabled | true or false | When set to false, device won't mine.
MinimumProfit | number | Minimum profit for device to mine.
TDPSettings | settings for tdp | Set tdp settings for specific device.
PluginAlgorithmSettings\Speeds | array[number] | Fine tune algorithm ratios by manually setting benchmark speeds for each algorithmID.
PluginAlgorithmSettings\ExtraLaunchParameters | text | Additional launch parameters when launching miner and this algorithm.
PluginAlgorithmSettings\Enabled | true or false | Set to false if you would like to skip & disable a particular algorithm. Benchmarking as well as actual mining will be disabled for this particular algorithm. That said, auto-switching will skip this algorithm when mining will be running.
PluginAlgorithmSettings\PowerUsage | number | Power usage recorded during benchmarking of this algorithm.

# Troubleshooting (excerpts)

My benchmarking results are not accurate — "Any kind of automation can only be done up to a particular level. We've spent significant effort to make benchmarking as good as possible, but it can't be made ideal."

# How to report bugs and issues?

To report bugs and issues please use the GitHub issue reporting tool: https://github.com/nicehash/NiceHashMiner/issues.
