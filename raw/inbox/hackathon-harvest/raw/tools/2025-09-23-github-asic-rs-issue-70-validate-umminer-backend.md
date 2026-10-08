# 256foundation/asic-rs issue #70: Validate Umminer Backend

> Source: https://github.com/256foundation/asic-rs/issues/70
> Collected: 2026-10-07
> Published: 2025-09-23

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 70
- State: open
- Author: s0kil
- Opened: 2025-09-23
- Closed: n/a
- Labels: enhancement

## Description

## CGI Endpoints

```bash
/cgi-bin/blink.cgi
/cgi-bin/cgi_lib.cgi
/cgi-bin/create_conf_backup.cgi
/cgi-bin/create_log_backup.cgi
/cgi-bin/get_blink_status.cgi
/cgi-bin/get_kernel_log.cgi
/cgi-bin/get_miner_conf.cgi
/cgi-bin/get_miner_status.cgi
/cgi-bin/get_multi_option.cgi
/cgi-bin/get_network_info.cgi
/cgi-bin/get_status_api.cgi
/cgi-bin/get_system_info.cgi
/cgi-bin/kill_umminer.cgi
/cgi-bin/log.cgi
/cgi-bin/miner_apools.cgi
/cgi-bin/miner_pools.cgi
/cgi-bin/miner_stats.cgi
/cgi-bin/miner_summary.cgi
/cgi-bin/minerAdvanced.cgi
/cgi-bin/minerConfiguration_check_pools.cgi
/cgi-bin/minerConfiguration.cgi
/cgi-bin/minerStatus.cgi
/cgi-bin/monitor.cgi
/cgi-bin/network_diag.cgi
/cgi-bin/passwd.cgi
/cgi-bin/reboot.cgi
/cgi-bin/recovery.cgi
/cgi-bin/reset_conf.cgi
/cgi-bin/reset_miner_conf.cgi
/cgi-bin/set_miner_conf.cgi
/cgi-bin/set_network_conf.cgi
/cgi-bin/upgrade_clear.cgi
/cgi-bin/upgrade.cgi
```


## Comments

### b-rowan on 2025-09-23

Where is this backend from?  Literally never seen this before, but it looks like modified BMMiner...


### s0kil on 2025-09-23

https://www.bitfufu.com/FuFuMinerOS

### taserz on 2026-05-13

That firmware broke one of our test miners. I think only bitfufu runs that

### b-rowan on 2026-05-13

> That firmware broke one of our test miners. I think only bitfufu runs that

Makes sense.  I don't know where you guys find this stuff LOL.
