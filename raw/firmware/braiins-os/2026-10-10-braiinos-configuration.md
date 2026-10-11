# Configuration — Braiins OS (Braiins Academy)

> Registry ID: braiins-os
> Source: https://academy.braiins.com/braiins-os/configuration (markdown captured via /braiins-os/configuration.md llms route)
> Collected: 2026-10-10
> Published: n/d (docs site build 2026-10-02, sitemap lastmod 2026-10-04)
> Posture: verbatim
> As-Of: 2026-10-10

# Configuration

## Pool and Workername settings

Navigate to **Top menu > Configuration > Pools**

![Pool and Workername settings](/static/image/Pool_settings.52eab9f5e7.jpg)

If you are mining on Braiins Pool, the userName is case-sensitive.

## Split hashrate with the pool groups

Pool groups allow you to split hashrate into multiple groups where each receives defined portion of hashrate. Each group has its own pools configured. There are two methods you can use - quota or fixed share ratio.

The example below shows two pool groups where the first one receives 75% of the hashrate and has two pools configured, while the second group receives 25% of the hashrate and has only one pool configured.

When all pools in any group become unavailable, the hashrate split is recalculated automatically to exclude the non-working group.

![Pool groups configuration - example](/static/image/pool-config-groups.ff29270085.png)
### Quota

Quota will split hashrate according to the ratio of each quota to the sum of all quotas. In the example below, group 1 will receive 2 parts of the hashrate (2/3), while group 2 will receive only 1 part of the hashrate (1/3).

![Pool groups configuration - quota](/static/image/pool-config-groups-quota.1dec26b513.png)
### Fixed share ratio

Fixed share ratio splits the work according to specified percentages. The total of assigned values must equal 100%; otherwise, an error is returned.

![Pool groups configuration - fixed share ratio](/static/image/pool-config-groups-fixed-share-ratio.4e9cb6d5ce.png)
## Autotuning configuration

Autotuning is available for Power Target or Hashrate Target.

- The Power target refers to a predefined power consumption level or limit that you want your miner to operate within.
- The Hashrate target refers to the desired level of computational power or mining efficiency that you want to achieve with your mining hardware.

1. Navigate to Configuration → Performance and click on "Enable Autotuning"
2. Set the Power/Hashrate Target according to your requirements
3. The progress of the autotuning can be viewed in the Dashboard under "Tuner status"
4. Once the Tuner Status shows "Stable," your miner is autotuned for your Power/Hashrate target


You can use autotuning to adjust your miner for multiple Power/Hashrate target profiles.
If Dynamic Performance Scaling is enabled due to reaching Hot temperature, Power/Hashrate target will be decreased to the values defined in Dynamic Performance Scaling. If you already have tuner profiles for reduced values, you will not need to wait for a new autotuning process.

## Tuner reset

Based on the device control board, the command is different via **BOS Toolbox > Command tab**:

### Zynq/Xilinx devices

```bash
/etc/init.d/bosminer stop && rm /etc/bosminer-autotune.json && /etc/init.d/bosminer start
```

### BBB/AML devices

```bash
/etc/init.d/S99bosminer stop && rm /etc/bosminer-autotune.json && /etc/init.d/S99bosminer start
```

## Custom DNS setting

To add a custom DNS to your device network settings, please navigate to **Top menu > System > Network**

### If you are using DHCP Client Protocol

If you have DHCP Client protocol > Click on Settings > Uncheck the Use DNS servers advertised by peer and add a custom DNS like `8.8.8.8` or `1.1.1.1` in the Use custom DNS servers field.

- Only for Zynq control board, custom DHCP does not work for BBB and AMlogic

### If you are using Static IP Protocol

If you have Static address protocol > set the Use custom DNS servers by adding `8.8.8.8` or `1.1.1.1` in the field.


Keep in mind after these changes Restart BOSminer: **Top right menu > Quick Action > Restart BOSminer**

## Cooling Control

Cooling controls allow to choose from three different modes: automatic, manual, and immersion. In all modes you have the possibility to control three levels of temperatures:

- **Target Temperature** is a temperature miner will target by regulating fans.
- **Hot Temperature** triggers **Dynamic Performance Scaling** (if enabled).
- **Dangerous Temperature** will stop mining. This is useful if there is a cooling failure or extreme temperature change.

We suggest a 10° separation between those values, so an example would be 60°, 70° and 80° if your setup maintains 60° average temperature.

![Temperature configuration](/static/image/config-temperature-control.74be592fa5.png)
### Default (Auto)

In default mode, fans are controlled automatically by the software to reach target temperature. You can also set custom minimum and maximum speed range for the fans.

### Immersion

Immersion mode will disable all fan setting controls and only the temperature setting will be available. Make sure to use the setup only when miners are in immersion.

### Manual

In manual mode you can choose fixed speed of fans and whether to require check for present fans. Usage of the manual mode is generally not recommended.

## Dynamic Performance Scaling

DPS is an adaptive temperature control feature. Documentation is available in [Dynamic Performance Scaling](/braiins-os/dps/index.md)

## Support and contact


Have questions? Our dev and support teams are always available to help.
Join our Telegram group:

[EN group](https://t.me/BraiinsOS)[ES group](https://t.me/BraiinsOS_ES)[RU group](https://t.me/BraiinsOS_RU)[ZH group](https://t.me/BraiinsOS_ZH)

You can also [send a VIP request](https://help.braiins.com/en/support/tickets/new) to our support team.



---

Was this helpful?

Yes, thanks!Sort of, thanks!Not really

Talk to us!
