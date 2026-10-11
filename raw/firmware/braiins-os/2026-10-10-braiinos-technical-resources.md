# Technical Resources — Braiins OS (Supported Devices, Error Codes, Default Temperatures, Default Power Limits, Supported PSU Models)

> Registry ID: braiins-os
> Source: https://academy.braiins.com/braiins-os/technical-resources (SSG HTML, 30,285 bytes, HTTP 200; the .md llms route returned HTTP 200 with 0 bytes, so content was extracted from the server-rendered HTML)
> Collected: 2026-10-10
> Published: n/d (docs site build 2026-10-02)
> Posture: extract (tables converted from HTML to pipe rows; cell text verbatim; embedded "View fullscreen" tables are rendered inline by the docs site)
> As-Of: 2026-10-10

Technical Resources #
Technical Resource page with handful information
# Introduction
This page provides details about the supported devices, along with the default power and hashrate target limits, as well as a list of error codes you might encounter while using Braiins OS.
# Error Codes
Error codes — Braiins OS
View fullscreen
Error Code | Description | Troubleshooting |
U1 | Tuner failed to start - mining won't start | Tuner failed to start due to misconfiguration or some other reason. Change the configuration and restart bosminer. If you think this is an error, then contact support. |
E1 | No hashboards are available for detection | No plugged-in hashboards were detected. Check the data cable from hashboard to control board, or repair/replace the hashboards. |
E2 | Miner model is very likely unsupported, mining won't start | Create a support package and send it to Braiins support, or at least send the logs containing the hexdumps of EEPROMs. This error should be caught during installation with toolbox, but could have happened if you connected an already installed control board with BOS to a different miner. |
E3 | Failed to read hashboard EEPROM, mining won't start | Raw data could not be read from hashboard. Check the data cable from hashboard to control board, or repair/replace the hashboard. |
E4 | Failed to decode hashboard EEPROM, mining won't start | One or more connected hashboards have corrupted/unknown EEPROM data, or hashboards from mutually incompatible miners are connected. Replace the hashboard(s). |
E5 | Another bosminer instance is already running | Another bosminer process is holding the lock file. Wait for it to finish or stop the other instance before starting a new one. |
HW1 | Failed to create reset pin instance | The device files expected by bosminer are not present. This is very likely caused by the software distribution (not by a hardware error). (Re)install the latest BOS or try a different control board. |
HW2 | Failed to create plug pin instance | The device files expected by bosminer are not present. This is very likely caused by the software distribution (not by a hardware error). (Re)install the latest BOS or try a different control board. |
HW3 | Failed to create PSU control pin instance | The device files expected by bosminer are not present. This is very likely caused by the software distribution (not by a hardware error). (Re)install the latest BOS or try a different control board. |
P1 | PSU error while initializing the chips | Check the PSU connection to the control board or replace the PSU. |
P2 | Error while setting voltage - check the PSU connection to control board | Check the PSU connection to the control board or replace the PSU. |
P3 | Communication with PSU failed (I2C write) | Check the cable connecting the PSU with the control board or replace the PSU. |
P4 | Communication with PSU failed (I2C read) | Check the cable connecting the PSU with the control board or replace the PSU. |
P5 | Connected PSU is not supported for this model (mining won't start) | The PSU is not compatible with the miner model. Check that the PSU can provide the same range of voltage as is expected for this model. If you think it should be supported, then send a support package to Braiins support together with a photo of the sticker on the PSU. |
P6 | Connected PSU is not supported (mining won't start) | The PSU is not recognized by this version of Braiins OS. If you think it should be supported, then send a support package to Braiins support together with a photo of the sticker on the PSU. |
P7 | Connected PSU is not supported for this model (mining won't start) | The PSU is not compatible with the miner model. Replace the PSU with a compatible one. If you think it should be supported, then send a support package to Braiins support together with a photo of the sticker on the PSU. |
V1 | The hashboard measured a different voltage than was set on PSU | This could be caused by the wrong PSU model or a hardware fault that lowers voltage. Either connect a correct PSU, or replace broken hashboards, or send a support package to Braiins support. |
V2 | Overcurrent protection triggered or short circuit | The voltage measured by the hashboard was significantly lower than expected. Either overcurrent protection on PSU disabled the power to hashboard or there's a short circuit somewhere between PSU and hashboard that makes the voltage significantly lower. Replace broken hashboards or set a lower power target/hashrate target. Another reason for short circuit could be a bad connection of the power rail to the hashboard, like loose screws, or faulty PSU. Please try to tighten the screws and check the PSU. |
V3 | The power controller version (PIC chip) on hashboard is unexpected for this model (mining won't start) | Either a PIC is broken or has a version that is not supported. Replace the hashboard or generate a support package and send it to Braiins support. |
V4 | Protocol error when communicating with power controller | PIC chip (on hashboard) sent garbage data. Replace the broken hashboard or send a support package to Braiins. |
I1 | Wrong hash chip revision for this model | The chips either sent garbage (temporary error), or the hashboard is not supported, or the hashboard was misidentified by bosminer. Try to restart the miner. Try to replace the hashboard. If you think this is an error, then contact support. |
I2 | Too many chips on hashchain | Either there was a communication error, or this is a different hashboard than expected. Try restarting the hashboard or contact support. |
I3 | No chips detected | Either chips are too cold to start (temporary problem), or there was a communication glitch (temporary problem), or the hashchain is damaged. Restart the miner or repair the hashboards. |
I5 | Not enough chips on chain | Either chips are too cold to start (temporary problem), or there was a communication glitch (temporary problem), or the hashchain is damaged. Restart the miner or repair the hashboards. |
I6 | Chip communication problem | Either there was a communication glitch (temporary problem), or the hashchain is damaged. Restart the miner or repair the hashboards. |
I7 | Chip initialization problem | Either there was a communication glitch (temporary problem), or the hashchain is damaged. Restart the miner or repair the hashboards. |
I8 | Chip initialization took too long | Either there was a glitch when initializing chips (temporary problem), or the hashchain is damaged. Restart the miner or repair the hashboards. |
F1 | Failed to reach the minimum speed of fans required for start of miner | The fans weren't able to meet the minimum RPM requirements. Either your fans are non-standard and too slow (this is configured with the min_fan_rpm option), or you don't have enough of them because some are broken, or you are running in immersion (this is configured with the min_fans option and/or enabling immersion mode if applicable). Replace fans or change config and then restart bosminer. |
F2 | Failed to initialize fan hardware | Check the fan connection, reinstall BOS, or replace the control board. |
F3 | Some fans broke while the miner was running | There are fewer fans than required for safe operation (this is configured with the min_fans option). Either the fans broke while bosminer was running, or something stopped them. Repair the fans or change the config and restart bosminer. Miner is paused. |
T1 | Temperature reached DANGEROUS level | Some hashboards reached dangerous PCB temperature. Check that cooling is adequate (fans, coolant flow, ambient/inlet temperature). Miner is paused. Auto-resumes after cooldown if the overheat recovery feature is enabled. |
T2 | Temperature reached DANGEROUS level | Some chips reached dangerous internal temperature. Check that cooling is adequate (fans, coolant flow, ambient/inlet temperature). Miner is paused. Auto-resumes after cooldown if the overheat recovery feature is enabled. |
T3 | Reversed coolant flow, inlet is hotter than outlet | Immersing the miner upside down is known to cause overheating. Check the coolant flow direction and correct it. |
T4 | Chip temperature rising too fast | Internal chip temperature is climbing faster than is safe. Check that cooling is adequate (fans, coolant flow, ambient/inlet temperature). Miner is paused. Auto-resumes after cooldown if the overheat recovery feature is enabled. |
T5 | Hashboard temperature sensor outage | Cannot read temperature for a running chain. Power-drain the miner to clear a possibly stuck I2C bus, or reseat the hashboard data cables. If the problem persists, repair or replace the hashboard. |
H1 | DISABLING hashboards not allowed on NoPIC miners | NoPIC miners are powering hashboards all the time and there's no way to disable them in software (they'll have consumption at least 300 W and will heat up even when disabled). If you want to override this behavior, then check allow_disabling_hashboards_on_nopic_miners = true option in bosminer-experimental.toml |
H2 | Hashboard stopped sending hashes | Usually a sign of voltage glitch on the hashboard, the issue will often resolve itself. If it happens frequently, conditions of the hashboard might have changed. Remove tuned profiles. If the hashboard is in bad shape, lowering power/hashrate target can also help. |
# Supported Devices
Below is a table listing the devices supported by Braiins OS, including the compatible control boards, hashboard models, and power supply units (PSUs).
# Current Miners
Supported devices — Braiins OS
View fullscreen
Model | Control Board | Hashboard model | Original PSUs | Supported PSUs |
Antminer S19 XP+ Hyd. | Zynq/Xilinx | HHB68701 , HHB68703 | APW111721a | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c , APW11G0 |
Antminer S21 XP Hyd. HV | Zynq/Xilinx | H6HB70502 | APW11G0 | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c , APW11G0 |
Antminer S21 XP Hyd. | Zynq/Xilinx | H6HB70501 | APW111721a | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c , APW11G0 |
Antminer S21e Hyd. | Zynq/Xilinx | H6HB70801 , H6HB70802 | APW111721b/c | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c , APW11G0 |
Antminer S19e XP Hyd. | Zynq/Xilinx | H6HB56702 | APW111721b/c | APW9 , APW9+ , APW9++ , APW111721a/b/c , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c , APW11G0 |
Antminer U3S21EXPH | Cvitek/CV1835 , Zynq/Xilinx | H1HB70601 , H1HB70602 , H1HB70603 | APW111721b/c | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c , APW11G0 |
Antminer S21+ Hyd. HV | Zynq/Xilinx | H6HB70704 | APW11G0 | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c , APW11G0 |
Antminer S21+ Hyd. | Zynq/Xilinx | H6HB70701 , H6HB70702 | APW111721b/c | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c , APW11G0 |
Antminer S21 Hyd. | Zynq/Xilinx | HHB68501 , HHB68502 , HHB68503 | APW111721b/c | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c , APW11G0 |
Antminer S21++ | Amlogic | A3HB70705 | APW171215a/c | APW11A1216-1a , APW121215d/e/f/g , APW171215a/c |
Antminer S21+ | Amlogic | A3HB70701 , A3HB70702 , A3HB70703 | APW171215a/c | APW11A1216-1a , APW121215d/e/f/g , APW171215a/c |
Antminer S21 XP Imm. | Amlogic | M1HB70602 | APW11A1216-1a | APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S21 Immersion | Amlogic | IHB68601 | APW11A1216-1a | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S19J XP | Amlogic , BeagleBone , Cvitek/CV1835 , Zynq/Xilinx | BHB56804 , BHB56804- | APW171215a/c | APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S21 XP | Amlogic | A3HB70501 , A3HB70502 , A3HB70503 | APW171215a/c | APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S21 Pro+ | Amlogic | A3HB70606 | APW171215a/c | APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S21 Pro | Amlogic | A3HB70601 , A3HB70602 , A3HB70603 | APW171215a/c | APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer T21 | Amlogic , Cvitek/CV1835 , Zynq/Xilinx | BHB68701 , BHB68701- , BHB68703 | APW11A1216-1a | APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S21 | Amlogic | BHB68603 , BHB68603P , BHB68606 , BHB68603- | APW171215a/c | APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S19K Pro NoPic | Amlogic , BeagleBone , Cvitek/CV1835 , Zynq/Xilinx | BHB56902 , BHB56902- , BHB56903 , BHB56907 | APW121215d/e/f/g | APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer T19 Pro Hyd. | Zynq/Xilinx | HHB56702 | APW111721b/c | APW9 , APW9+ , APW9++ , APW111721a/b/c , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c , APW11G0 |
Antminer S19 XP Hydro | Zynq/Xilinx | HHB56601 , HHB56611 | APW111721a | APW9 , APW9+ , APW9++ , APW111721a/b/c , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c , APW11G0 |
Antminer S19 XP | Amlogic , BeagleBone , Cvitek/CV1835 , Zynq/Xilinx | BHB56801 , BHB56802 | APW121215d/e/f/g | APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S19J126NoPic | Amlogic , BeagleBone , Zynq/Xilinx | BHB42841 | APW121215d/e/f/g | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S19J88NoPic | Amlogic , BeagleBone , Zynq/Xilinx | BHB42811 , BHB42821 , BHB42831 | APW121417b | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S19J88 | Amlogic , BeagleBone , Zynq/Xilinx | BHB42801 | APW121417a | APW9 , APW9+ , APW9++ , APW111721a/b/c , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c |
Antminer S19J Pro NoPic | Amlogic , BeagleBone , Cvitek/CV1835 , Zynq/Xilinx | BHB42603 , BHB42631 , BHB42651 | APW121215d/e/f/g | APW111721b/c , APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer T19 | Zynq/Xilinx | | APW121215a/b/c | APW9 , APW9+ , APW9++ , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c |
Antminer S19J Pro Plus NoPic | Amlogic , BeagleBone , Cvitek/CV1835 , Zynq/Xilinx | BHB42612 | APW121215d/e/f/g | APW11A1216-1a , APW121215d/e/f/g , APW121417b , APW171215a/c |
Antminer S19J | Amlogic , BeagleBone , Cvitek/CV1835 , Zynq/Xilinx | BHB42701 | APW121215a/b/c | APW9 , APW9+ , APW9++ , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c |
Antminer S19J Pro | Amlogic , BeagleBone , Cvitek/CV1835 , Zynq/Xilinx | BHB42601 , BHB42621 , BHB42641 | APW121215a/b/c | APW9 , APW9+ , APW9++ , APW111721a/b/c , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c |
Antminer S19a | | | APW121215a/b/c | APW9 , APW9+ , APW9++ , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c |
Antminer S19a Pro | | | APW121215a/b/c | APW9 , APW9+ , APW9++ , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c |
Antminer S19 Pro Plus Hydro | Zynq/Xilinx | HHB42601 , HHB42602 , HHB42631 | APW111721a | APW9 , APW9+ , APW9++ , APW111721a/b/c , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c , APW11G0 |
Antminer S19 Pro | Amlogic , BeagleBone , Cvitek/CV1835 , Zynq/Xilinx | | APW121215a/b/c | APW9 , APW9+ , APW9++ , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c |
Antminer S19+ | | | APW121215a/b/c | APW9 , APW9+ , APW9++ , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c |
Antminer S19 | Amlogic , BeagleBone , Zynq/Xilinx | | APW121215a/b/c | APW9 , APW9+ , APW9++ , APW11A1216-1a , APW121215a/b/c/d/e/f/g , APW121417a/b , APW171215a/c |
Braiins Mini Miner BMM 100 | | BMM100 P1 , BMM100 P02 | | |
Braiins Mini Miner BMM 101 | | BMM101 P00 | | |
# Legacy Miners
The miners listed below are supported, but development has been discontinued. Specifically, for the X17 series , development stopped at version 23.01 , and for the S9 series, it ended at version 22.08.1
Model | Control Board | Hashboard model | Original PSUs |
Antminer T17e | Zynq/Xilinx | | APW9+ |
Antminer T17+ | Zynq/Xilinx | | APW9+ |
Antminer T17 | Zynq/Xilinx | | APW9 |
Antminer S17e | Zynq/Xilinx | | APW9+ |
Antminer S17+ | Zynq/Xilinx | | APW9+ |
Antminer S17 Pro | Zynq/Xilinx | | APW9 |
Antminer S17 | Zynq/Xilinx | | APW9 |
Antminer S9j | Zynq/Xilinx | | AP3++ , APW7 |
Antminer S9i | Zynq/Xilinx | | AP3++ , APW7 |
Antminer S9 | Zynq/Xilinx | | |
# Important Notes
Some notes to consider when installing the Braiins OS on devices.
For smooth operation, Braiins OS on Cvitek control boards requires Braiins Farm Monitor version 23.12 or later. If
the miner reboots into Bitmain stock firmware, Farm Monitor will detect the switch and automatically restart Braiins
OS with the latest settings. During stock firmware use, the miner runs on pre-Braiins OS settings. To streamline
this, ensure Farm Monitor covers all relevant IP ranges for Cvitek miners. More details about Farm Monitor are
available here .
# Default Temperatures
Default temperatures — Braiins OS
View fullscreen
Model | Chip | Num. hbs. | Num. chips. | Num. dom. | NoPIC | Targ. temp | Hot temp | Dang. temp | Cold temp |
Antminer S19 XP+ Hyd. | BM1368 | 3 | 180 | 18 | yes | 65 | 80 | 90 | 10 |
Antminer S21 XP Hyd. HV | BM1370 | 3 | 160 | 20 | yes | 65 | 80 | 90 | 10 |
Antminer S21 XP Hyd. | BM1370 | 3 | 160 | 20 | yes | 65 | 80 | 90 | 10 |
Antminer S21e Hyd. | BM1370 | 3 | 85 | 17 | yes | 65 | 80 | 90 | 10 |
Antminer S19e XP Hyd. | BM1366 | 3 | 204 | 17 | no | 60 | 80 | 90 | 10 |
Antminer U3S21EXPH | BM1370 | 3 | 160 | 20 | yes | 65 | 80 | 90 | 10 |
Antminer S21+ Hyd. HV | BM1370 | 3 | 95 | 19 | yes | 65 | 80 | 90 | 10 |
Antminer S21+ Hyd. | BM1370 | 3 | 95 | 19 | yes | 65 | 80 | 90 | 10 |
Antminer S21 Hyd. | BM1368 | 3 | 216 | 18 | yes | 65 | 80 | 90 | 10 |
Antminer S21+ | BM1370 | 3 | 55 | 11 | yes | 65 | 80 | 90 | - |
Antminer S21 XP Imm. | BM1370 | 3 | 91 | 13 | yes | 65 | 80 | 90 | 10 |
Antminer S21 Immersion | BM1368 | 3 | 156 | 13 | yes | 65 | 80 | 90 | 10 |
Antminer S19J XP | BM1366 | 3 | 110 | 11 | yes | 65 | 80 | 90 | - |
Antminer S21 XP | BM1370 | 3 | 91 | 13 | yes | 65 | 80 | 90 | - |
Antminer S21 Pro | BM1370 | 3 | 65 | 13 | yes | 65 | 80 | 90 | - |
Antminer T21 | BM1368 | 3 | 108 | 12 | yes | 65 | 80 | 90 | - |
Antminer S21 | BM1368 | 3 | 108 | 12 | yes | 65 | 80 | 90 | - |
Antminer S19K Pro NoPic | BM1366 | 3 | 77 | 11 | yes | 65 | 80 | 90 | - |
Antminer T19 Pro Hyd. | BM1366 | 3 | 204 | 17 | no | 60 | 80 | 90 | 10 |
Antminer S19 XP Hydro | BM1366 | 3 | 204 | 17 | no | 60 | 80 | 90 | 10 |
Antminer S19 XP | BM1366 | 3 | 110 | 11 | yes | 65 | 78 | 85 | - |
Antminer S19J126NoPic | BM1362 | 3 | 126 | 42 | yes | 60 | 80 | 90 | - |
Antminer S19J88NoPic | BM1362 | 3 | 88 | 44 | yes | 60 | 80 | 90 | - |
Antminer S19J88 | BM1362 | 3 | 88 | 44 | no | 60 | 80 | 90 | - |
Antminer S19J Pro NoPic | BM1362 | 3 | 126 | 42 | yes | 60 | 80 | 90 | - |
Antminer T19 | BM1398 | 3 | 76 | 38 | no | 60 | 80 | 90 | - |
Antminer S19J Pro Plus NoPic | BM1362 | 3 | 120 | 40 | yes | 60 | 80 | 90 | - |
Antminer S19J | BM1362 | 3 | 108 | 36 | no | 60 | 80 | 90 | - |
Antminer S19J Pro | BM1362 | 3 | 126 | 42 | no | 60 | 80 | 90 | - |
Antminer S19a | BM1398 | 3 | 76 | 38 | no | 60 | 80 | 90 | - |
Antminer S19a Pro | BM1398 | 3 | 114 | 38 | no | 60 | 80 | 90 | - |
Antminer S19 Pro Plus Hydro | BM1362 | 4 | 180 | 60 | no | 60 | 80 | 90 | 10 |
Antminer S19 Pro | BM1398 | 3 | 114 | 38 | no | 60 | 80 | 90 | - |
Antminer S19+ | BM1398 | 3 | 80 | 40 | no | 60 | 80 | 90 | - |
Antminer S19 | BM1398 | 3 | 76 | 38 | no | 60 | 80 | 90 | - |
Braiins Mini Miner BMM 100 | BM1362 | 1 | 4 | 4 | no | 67 | 80 | 90 | - |
Braiins Mini Miner BMM 101 | BM1362 | 1 | 4 | 4 | no | 67 | 80 | 90 | - |
# Legacy Miners
Legacy miners — Braiins OS
View fullscreen
Model | Chip | Num. hbs. | Num. chips. | Num. dom. | NoPIC | Targ. temp | Hot temp | Dang. temp | Cold temp |
Antminer T17e | BM1396 | 3 | 78 | 13 | no | 75 | 82 | 92 | - |
Antminer S17e | BM1396 | 3 | 135 | 15 | no | 75 | 82 | 92 | - |
Antminer T17+ | BM1397 | 3 | 44 | 11 | no | 75 | 82 | 92 | - |
Antminer T17 | BM1397 | 3 | 30 | 10 | no | 75 | 82 | 92 | - |
Antminer S17 Pro | BM1397 | 3 | 48 | 12 | no | 75 | 82 | 92 | - |
Antminer S17+ | BM1397 | 3 | 65 | 13 | no | 75 | 82 | 92 | - |
Antminer S17 | BM1397 | 3 | 48 | 12 | no | 75 | 82 | 92 | - |
# Default Power Limits
The table below outlines the default limits for each supported Antminer model and their performance variants. Keep in mind that pushing the miner to its minimum limit will reduce efficiency, and going to the maximum limit can put the miner at serious risk. It's important to set realistic targets that match your cooling setup and environmental conditions.
# Current Miners
Default power limits — Braiins OS
View fullscreen
Model | PerfVar Power | PerfVar Hashrate | Min Power | Max Power | Min Hashrate | Max Hashrate |
Antminer S19 XP+ Hyd. | 4788 | 252.00 | 1472 | 9900 | 37.90 | 895.75 |
Antminer S19 XP+ Hyd. | 5054 | 266.00 | 1472 | 9900 | 37.90 | 895.75 |
Antminer S19 XP+ Hyd. | 5301 | 279.00 | 1472 | 9900 | 37.90 | 895.75 |
Antminer S19 XP+ Hyd. | 5567 | 293.00 | 1472 | 9900 | 37.90 | 895.75 |
Antminer S21 XP Hyd. HV | 5280 | 440.00 | 3771 | 9900 | 269.28 | 1272.96 |
Antminer S21 XP Hyd. HV | 5676 | 473.00 | 3771 | 9900 | 269.28 | 1272.96 |
Antminer S21 XP Hyd. | 5280 | 440.00 | 3863 | 9900 | 269.28 | 1272.96 |
Antminer S21 XP Hyd. | 5676 | 473.00 | 3863 | 9900 | 269.28 | 1272.96 |
Antminer S21e Hyd. | 4896 | 288.00 | 3161 | 9900 | 143.06 | 676.26 |
Antminer S21e Hyd. | 5270 | 310.00 | 3161 | 9900 | 143.06 | 676.26 |
Antminer S21e Hyd. | 5644 | 332.00 | 3161 | 9900 | 143.06 | 676.26 |
Antminer S19e XP Hyd. | 5280 | 240.00 | 1249 | 9900 | 30.10 | 711.26 |
Antminer S19e XP Hyd. | 5522 | 251.00 | 1249 | 9900 | 30.10 | 711.26 |
Antminer U3S21EXPH | 5590 | 430.00 | 4725 | 9900 | 269.28 | 1272.96 |
Antminer S21+ Hyd. HV | 4785 | 319.00 | 3161 | 9900 | 159.89 | 755.82 |
Antminer S21+ Hyd. HV | 5070 | 338.00 | 3161 | 9900 | 159.89 | 755.82 |
Antminer S21+ Hyd. HV | 5370 | 358.00 | 3161 | 9900 | 159.89 | 755.82 |
Antminer S21+ Hyd. HV | 5925 | 395.00 | 3161 | 9900 | 159.89 | 755.82 |
Antminer S21+ Hyd. | 4785 | 319.00 | 3301 | 9900 | 159.89 | 755.82 |
Antminer S21+ Hyd. | 5070 | 338.00 | 3301 | 9900 | 159.89 | 755.82 |
Antminer S21+ Hyd. | 5370 | 358.00 | 3301 | 9900 | 159.89 | 755.82 |
Antminer S21+ Hyd. | 5925 | 395.00 | 3301 | 9900 | 159.89 | 755.82 |
Antminer S21 Hyd. | 4320 | 270.00 | 1660 | 9900 | 45.48 | 1074.90 |
Antminer S21 Hyd. | 4576 | 286.00 | 1660 | 9900 | 45.48 | 1074.90 |
Antminer S21 Hyd. | 4832 | 302.00 | 1660 | 9900 | 45.48 | 1074.90 |
Antminer S21 Hyd. | 5104 | 319.00 | 1660 | 9900 | 45.48 | 1074.90 |
Antminer S21 Hyd. | 5360 | 335.00 | 1660 | 9900 | 45.48 | 1074.90 |
Antminer S21++ | 3564 | 216.00 | 1990 | 6435 | 92.57 | 437.58 |
Antminer S21++ | 3713 | 225.00 | 1990 | 6435 | 92.57 | 437.58 |
Antminer S21++ | 3878 | 235.00 | 1990 | 6435 | 92.57 | 437.58 |
Antminer S21+ | 3564 | 216.00 | 2537 | 6435 | 92.57 | 437.58 |
Antminer S21+ | 3713 | 225.00 | 2537 | 6435 | 92.57 | 437.58 |
Antminer S21+ | 3878 | 235.00 | 2537 | 6435 | 92.57 | 437.58 |
Antminer S21 XP Imm. | 4050 | 300.00 | 2877 | 9900 | 153.16 | 723.99 |
Antminer S21 Immersion | 3440 | 215.00 | 1214 | 9900 | 32.85 | 776.31 |
Antminer S21 Immersion | 3520 | 220.00 | 1214 | 9900 | 32.85 | 776.31 |
Antminer S21 Immersion | 3632 | 227.00 | 1214 | 9900 | 32.85 | 776.31 |
Antminer S21 Immersion | 3824 | 239.00 | 1214 | 9900 | 32.85 | 776.31 |
Antminer S19J XP | 2795 | 130.00 | 1010 | 6435 | 16.23 | 383.52 |
Antminer S19J XP | 2924 | 136.00 | 1010 | 6435 | 16.23 | 383.52 |
Antminer S19J XP | 3075 | 143.00 | 1010 | 6435 | 16.23 | 383.52 |
Antminer S19J XP | 3247 | 151.00 | 1010 | 6435 | 16.23 | 383.52 |
Antminer S21 XP | 3645 | 270.00 | 2774 | 6435 | 153.16 | 723.99 |
Antminer S21 Pro+ | 3300 | 220.00 | 2207 | 6435 | 109.40 | 517.14 |
Antminer S21 Pro+ | 3510 | 234.00 | 2207 | 6435 | 109.40 | 517.14 |
Antminer S21 Pro+ | 3675 | 245.00 | 2207 | 6435 | 109.40 | 517.14 |
Antminer S21 Pro | 3300 | 220.00 | 2316 | 6435 | 109.40 | 517.14 |
Antminer S21 Pro | 3500 | 234.00 | 2316 | 6435 | 109.40 | 517.14 |
Antminer S21 Pro | 3675 | 245.00 | 2316 | 6435 | 109.40 | 517.14 |
Antminer T21 | 3540 | 180.00 | 1457 | 9900 | 22.74 | 537.45 |
Antminer T21 | 3730 | 190.00 | 1457 | 9900 | 22.74 | 537.45 |
Antminer S21 | 2755 | 151.00 | 927 | 6435 | 22.74 | 537.45 |
Antminer S21 | 2975 | 163.00 | 927 | 6435 | 22.74 | 537.45 |
Antminer S21 | 3155 | 173.00 | 927 | 6435 | 22.74 | 537.45 |
Antminer S21 | 3190 | 175.00 | 927 | 6435 | 22.74 | 537.45 |
Antminer S21 | 3420 | 188.00 | 927 | 6435 | 22.74 | 537.45 |
Antminer S21 | 3535 | 195.00 | 927 | 6435 | 22.74 | 537.45 |
Antminer S21 | 3650 | 200.00 | 927 | 6435 | 22.74 | 537.45 |
Antminer S19K Pro NoPic | 2530 | 110.00 | 771 | 6435 | 11.36 | 268.46 |
Antminer S19K Pro NoPic | 2760 | 120.00 | 771 | 6435 | 11.36 | 268.46 |
Antminer T19 Pro Hyd. | 4928 | 224.00 | 1577 | 9900 | 30.10 | 711.26 |
Antminer T19 Pro Hyd. | 5170 | 235.00 | 1577 | 9900 | 30.10 | 711.26 |
Antminer T19 Pro Hyd. | 5412 | 246.00 | 1577 | 9900 | 30.10 | 711.26 |
Antminer S19 XP Hydro | 4659 | 224.00 | 1706 | 9900 | 30.10 | 711.26 |
Antminer S19 XP Hydro | 4888 | 235.00 | 1706 | 9900 | 30.10 | 711.26 |
Antminer S19 XP Hydro | 5117 | 246.00 | 1706 | 9900 | 30.10 | 711.26 |
Antminer S19 XP Hydro | 5346 | 257.00 | 1706 | 9900 | 30.10 | 711.26 |
Antminer S19 XP | 2559 | 119.00 | 954 | 6435 | 16.23 | 383.52 |
Antminer S19 XP | 2730 | 127.00 | 954 | 6435 | 16.23 | 383.52 |
Antminer S19 XP | 2881 | 134.00 | 954 | 6435 | 16.23 | 383.52 |
Antminer S19 XP | 3031 | 141.00 | 954 | 6435 | 16.23 | 383.52 |
Antminer S19J126NoPic | 2967 | 90.00 | 761 | 6435 | 30.14 | 252.57 |
Antminer S19J88NoPic | 2769 | 84.00 | 882 | 6435 | 58.00 | 176.40 |
Antminer S19J88NoPic | 2868 | 87.00 | 882 | 6435 | 58.00 | 176.40 |
Antminer S19J88NoPic | 2967 | 90.00 | 882 | 6435 | 58.00 | 176.40 |
Antminer S19J88 | 2769 | 84.00 | 898 | 6435 | 59.91 | 176.40 |
Antminer S19J88 | 2868 | 87.00 | 898 | 6435 | 59.91 | 176.40 |
Antminer S19J88 | 2967 | 90.00 | 898 | 6435 | 59.91 | 176.40 |
Antminer S19J Pro NoPic | 2478 | 84.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19J Pro NoPic | 2595 | 88.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19J Pro NoPic | 2714 | 92.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19J Pro NoPic | 2832 | 96.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19J Pro NoPic | 2950 | 100.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19J Pro NoPic | 3068 | 104.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer T19 | 2513 | 67.00 | 659 | 6435 | 54.07 | 184.65 |
Antminer T19 | 2888 | 77.00 | 659 | 6435 | 54.07 | 184.65 |
Antminer T19 | 3038 | 81.00 | 659 | 6435 | 54.07 | 184.65 |
Antminer T19 | 3150 | 84.00 | 659 | 6435 | 54.07 | 184.65 |
Antminer T19 | 3300 | 88.00 | 659 | 6435 | 54.07 | 184.65 |
Antminer S19J Pro Plus NoPic | 2998 | 109.00 | 817 | 6435 | 94.86 | 240.55 |
Antminer S19J Pro Plus NoPic | 3108 | 113.00 | 817 | 6435 | 94.86 | 240.55 |
Antminer S19J Pro Plus NoPic | 3218 | 117.00 | 817 | 6435 | 94.86 | 240.55 |
Antminer S19J Pro Plus NoPic | 3245 | 118.00 | 817 | 6435 | 94.86 | 240.55 |
Antminer S19J Pro Plus NoPic | 3300 | 120.00 | 817 | 6435 | 94.86 | 240.55 |
Antminer S19J | 2829 | 82.00 | 1131 | 6435 | 83.54 | 216.49 |
Antminer S19J | 2967 | 86.00 | 1131 | 6435 | 83.54 | 216.49 |
Antminer S19J | 3105 | 90.00 | 1131 | 6435 | 83.54 | 216.49 |
Antminer S19J | 3243 | 94.00 | 1131 | 6435 | 83.54 | 216.49 |
Antminer S19J Pro | 2478 | 84.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19J Pro | 2595 | 88.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19J Pro | 2714 | 92.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19J Pro | 2832 | 96.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19J Pro | 2950 | 100.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19J Pro | 3068 | 104.00 | 944 | 6435 | 70.75 | 252.57 |
Antminer S19a | 3036 | 88.00 | 433 | 6435 | 65.79 | 184.65 |
Antminer S19a | 3174 | 92.00 | 433 | 6435 | 65.79 | 184.65 |
Antminer S19a | 3312 | 96.00 | 433 | 6435 | 65.79 | 184.65 |
Antminer S19a | 3450 | 100.00 | 433 | 6435 | 65.79 | 184.65 |
Antminer S19a Pro | 3009 | 102.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19a Pro | 3127 | 106.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19a Pro | 3245 | 110.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19 Pro Plus Hydro | 4675 | 170.00 | 2094 | 9900 | 87.53 | 481.10 |
Antminer S19 Pro Plus Hydro | 4868 | 177.00 | 2094 | 9900 | 87.53 | 481.10 |
Antminer S19 Pro Plus Hydro | 5060 | 184.00 | 2094 | 9900 | 87.53 | 481.10 |
Antminer S19 Pro Plus Hydro | 5253 | 191.00 | 2094 | 9900 | 87.53 | 481.10 |
Antminer S19 Pro Plus Hydro | 5445 | 198.00 | 2094 | 9900 | 87.53 | 481.10 |
Antminer S19 Pro | 2478 | 84.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19 Pro | 2596 | 88.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19 Pro | 2714 | 92.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19 Pro | 2832 | 96.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19 Pro | 2950 | 100.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19 Pro | 3068 | 104.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19 Pro | 3098 | 105.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19 Pro | 3250 | 110.00 | 871 | 6435 | 96.33 | 276.98 |
Antminer S19 | 2829 | 82.00 | 359 | 6435 | 65.79 | 184.65 |
Antminer S19 | 2967 | 86.00 | 359 | 6435 | 65.79 | 184.65 |
Antminer S19 | 3105 | 90.00 | 359 | 6435 | 65.79 | 184.65 |
Antminer S19 | 3250 | 95.00 | 359 | 6435 | 65.79 | 184.65 |
Braiins Mini Miner BMM 100 | 40 | 1.00 | 19 | 67 | 0.12 | 1.50 |
Braiins Mini Miner BMM 101 | 40 | 1.00 | 19 | 67 | 0.12 | 1.50 |
# Legacy Miners
Legacy miners — Braiins OS
View fullscreen
Model | PerfVar Power | PerfVar Hashrate | Min Power | Max Power | Min Hashrate | Max Hashrate |
Antminer S17e | 2880 | 64 | 2120 | 4950 | 34.22 | 147.74 |
Antminer S17e | 2700 | 60 | 2120 | 4950 | 34.22 | 147.74 |
Antminer S17e | 2520 | 56 | 2120 | 4950 | 34.22 | 147.74 |
Antminer S17e | 2385 | 53 | 2120 | 4950 | 34.22 | 147.74 |
Antminer S17+ | 3040 | 76 | 1443 | 4950 | 28.83 | 124.48 |
Antminer S17+ | 2920 | 73 | 1443 | 4950 | 28.83 | 124.48 |
Antminer S17+ | 2800 | 70 | 1443 | 4950 | 28.83 | 124.48 |
Antminer S17+ | 2680 | 67 | 1443 | 4950 | 28.83 | 124.48 |
Antminer S17 Pro | 2212 | 56 | 1228 | 3960 | 21.29 | 91.92 |
Antminer S17 Pro | 2094 | 53 | 1228 | 3960 | 21.29 | 91.92 |
Antminer S17 Pro | 1975 | 50 | 1228 | 3960 | 21.29 | 91.92 |
Antminer S17 | 2385 | 53 | 1228 | 3960 | 21.29 | 91.92 |
Antminer S17 | 2250 | 50 | 1228 | 3960 | 21.29 | 91.92 |
Antminer T17e | 2915 | 53 | 1272 | 4811 | 19.77 | 85.36 |
Antminer T17e | 2750 | 50 | 1272 | 4811 | 19.77 | 85.36 |
Antminer T17+ | 3200 | 64 | 1135 | 4253 | 29.18 | 84.26 |
Antminer T17+ | 3050 | 61 | 1135 | 4253 | 29.18 | 84.26 |
Antminer T17+ | 2900 | 58 | 1135 | 4253 | 29.18 | 84.26 |
Antminer T17+ | 2750 | 55 | 1135 | 4253 | 29.18 | 84.26 |
Antminer T17+ | 2600 | 52 | 1135 | 4253 | 29.18 | 84.26 |
Antminer T17 | 2200 | 40 | 809 | 2934 | 28.81 | 57.45 |
# Supported PSU Models
The table below lists all PSU models supported by Braiins OS and their capabilities. Voltage feedback indicates whether the PSU reports the actual output voltage; Power readings whether it reports power consumption.
Models | Voltage feedback | Power readings |
APW121215a/b/c | No | No |
APW121215d/e/f/g | Yes | No |
APW121417a | No | No |
APW121417b | Yes | No |
APW111721a | No | Yes |
APW111721b/c | Yes | Yes |
APW11A1216-1a | Yes | Yes |
APW11G0 | Yes | Yes |
APW171215a/c | Yes | Yes |
# Support and contact
Have questions? Our dev and support teams are always available to help.
Join our Telegram group:
EN group
ES group
RU group
ZH group
You can also send a VIP request to our support team.
