# Canaan Avalon Home Miner APIs

> Source: https://forum.heatpunks.org/t/canaan-avalon-home-miner-apis/168
> Collected: 2026-10-10
> Published: 2025-08-21
> Registry ID: heatpunks-forum

tylerkstevens | 2025-08-21 15:00:31 UTC | #1

Hey All,

Found this documentation for the Canaan Avalon Mini3 and Avalon Q API control. It’s been useful for @tronsington and I for building Home Assistant automations and additional features on the Canaan space heaters.

Avalon Q: [Docs](https://www.canaan.io/resource/api/avalon-q-commands)
Avalon Mini3: [Docs](https://www.canaan.io/resource/api/avalon-mini-3)

-------------------------

hfuhruhurr | 2025-08-28 14:17:55 UTC | #2

It has also has [Nano 3S docs](https://www.canaan.io/docs/api/avalon-nano-3s), for those wondering.

-------------------------

tylerkstevens | 2025-08-28 15:51:34 UTC | #3

Here’s a walkthrough of our self made home thermostat for whole home heating with Home Assistant and the Avalon Mini 3s.

[x.com](https://x.com/tylerkstevens/status/1961093502625780070)

#### https://x.com/tylerkstevens/status/1961093502625780070

@

-------------------------

Atreyu | 2025-08-29 04:42:52 UTC | #4

If you guys do a tutorial on how you set this up Id absolutely give it a try on my side! Congrats on getting it live

-------------------------

tylerkstevens | 2025-08-31 01:07:02 UTC | #5

We’re polishing up the controls and will then open source the configuration file for Home Assistant! The Exergy team will post an update here once ready!

-------------------------

Cas | 2025-09-01 18:08:41 UTC | #6

Hi, looking forward to learning more here. I got the nano3s api working with node red. Pretty cool

-------------------------

tronsington | 2025-09-01 19:18:20 UTC | #7

Nice! At the very least it’s nice to have the ability to control your machines remotely, which you can’t do with the Avalon app (for now).

-------------------------

Cas | 2025-09-06 11:09:32 UTC | #8

It’s probably already been done. Anyhow, here’s some code to get power out of the nano3s in NodeRed:

```auto
// Nano3s "estats" parser for Node-RED
// Works even when output is "…|STATS=0,ID=...,PS[...],…|"

// 1) Normalize payload to string
let raw = Buffer.isBuffer(msg.payload) ? msg.payload.toString('utf8') : String(msg.payload ?? '');
raw = raw.replace(/\x00/g, '').trim();

// 2) Grab PS[...] directly (don’t rely on section headers)
const psMatch = raw.match(/PS\[(.*?)\]/);
let power_w = null, volts_v = null;

if (psMatch) {
    const parts = psMatch[1].trim().split(/\s+/).map(n => Number(n));
    // Expect at least 6 fields: PS[0 0 <mV> <A> 0 <raw> ...]
    if (parts.length >= 6 && Number.isFinite(parts[2]) && Number.isFinite(parts[5])) {
        const mv = parts[2];           // millivolts
        const rawp = parts[5];         // raw power code
        const volts = mv / 1000.0;     // volts
        if (volts > 0) {
            volts_v = volts;
            power_w = rawp / volts;      // W  (matches Nano LCD)
        }
    }
}

// 3) Also pull temp/fan/freq using bracket-token regexes (and fallbacks)
const getNum = (re) => {
    const m = raw.match(re);
    return m ? Number(m[1]) : null;
};

const temp_c = getNum(/OTemp\[(\-?\d+)\]/) ?? getNum(/TAvg\[(\-?\d+)\]/) ?? null;
const fan_rpm = getNum(/Fan1\[(\d+)\]/) ?? null;
const freq = getNum(/Freq\[(\d+(\.\d+)?)\]/) ?? null;

// 4) Build payload for HA MQTT sensors you already have
msg.topic = "home/nano3s/estats";
msg.payload = {
    ts: Date.now(),
    power_w: power_w !== null ? Math.round(power_w) : 0,
    temp_c: temp_c,
    fan_rpm: fan_rpm,
    freq_mhz: freq,
    voltage_v: volts_v !== null ? Number(volts_v.toFixed(2)) : null
};

return msg;

```

-------------------------

Atreyu | 2025-09-06 22:42:24 UTC | #9

It’s a miss on their side for sure to not have that ability natively within app

Guess it’s time to buy a few of these guys

-------------------------

tylerkstevens | 2025-09-06 23:03:33 UTC | #10

Node Red is amazing. @tronsington will share his for the Mini 3 and Q soon.

-------------------------

tylerkstevens | 2025-09-08 22:44:51 UTC | #11

Here’s a video walkthrough of how the walk thermostat works. Parts list and documentation coming soon.

[x.com](https://x.com/tylerkstevens/status/1965178520789025022)

#### https://x.com/tylerkstevens/status/1965178520789025022

@

-------------------------

Cas | 2025-09-27 21:27:30 UTC | #12

I got the mini3 working with Node-RED. How are you guys getting on? The biggest pain in the ass is the softon/softoff commands, which are misleading they’re just scheduled, not an actual state. That meant the miner often ignored the first heat level. Fix was a handshake + follow chain in Node-RED i.e wake it, wait for estats to show it’s alive, then apply mode/level change. Without that ‘follow’ step it always fell back to ECO or did nothing, pretty happy it’s working now with a aeotec multisensor 6.

-------------------------

MaX | 2025-10-27 21:56:50 UTC | #13

it seems that Avalaon has taken down the API documentation from their website, the link does now lead to the main page.
Can somebody post the file here please?

thank you MaX

-------------------------

tylerkstevens | 2025-10-28 14:26:46 UTC | #14

They updated the links.

Here you go: [Canaan Customer Support](https://www.canaan.io/resource/api/getting-started)

-------------------------

tronsington | 2025-10-28 20:39:17 UTC | #15

# Avalon Mini 3 API Docs

just in case the site goes down again

# Query Version Information

version
Example
echo -n “version” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753681930,Code=22,Msg=CGMiner versions,Description=cgminer 4.11.1|VERSION,CGMiner=4.11.1,API=3.7,PROD=Avalon Q,MODEL=Q,HWTYPE=Q_MM1v1_X1,SWT
shell

# Query Brief Information

summary
Example
echo -n “summary” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753682020,Code=11,Msg=Summary,Description=cgminer 4.11.1|SUMMARY,Elapsed=1272,MHS av=50391540.54,MHS 5s=45851037.27,MHS 1m=39157558.90,MHS 5
shell

# Query Device Log

estats
Example
echo -n “estats” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753682105,Code=70,Msg=CGMiner stats,Description=cgminer 4.11.1|STATS=0,ID=AVALON0,Elapsed=1357,Calls=0,Wait=0.000000,Max=0.000000,Min=999999
shell

# Query Mining Pool Configuration Information

pools
Example
echo -n “pools” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753682215,Code=7,Msg=3 Pool(s),Description=cgminer 4.11.1|POOL=0,URL=stratum+tcp://10.100.106.101:5555,Status=Alive,Priority=0,Quota=1,Long
shell

# Set Mining Pool

setpool|,,,,,
Parameter Explanation
-web username，default：admin
-web login password，default : admin
-range 0-2，set which mining pool
-mining pool address
-pool worker
-pool worker password
Note: Mining pool settings will not take effect until restarting manually
Example
echo -n “setpool|admin,admin,0,stratum+tcp://10.100.106.101:4444, avalonaging,123” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753682452,Code=133,Msg=Pool set info:
pool 0 success set to stratum+tcp://10.100.106.101:4444
worker is avalonaging
workerpassword is 123
Please reboot miner to make config work.
,Description=cgminer 4.11.1|
shell

# Set Fan Speed

ascset|0,fan-spd,
Parameter Explanation
-The value accounts for expected fan speed ratio，range：15-100 ; When SPEED is equal to -1, automatic fan speed control resumes.
Example
echo -n “ascset|0,fan-spd,100” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753682966,Code=119,Msg=ASC 0 set OK,Description=cgminer 4.11.1|
shell

# Set work mode

ascset|0,workmode,set,
Parameter Explanation
-range：0~2
Example
echo -n “ascset|0,workmode,set,1” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753683064,Code=119,Msg=ASC 0 set OK,Description=cgminer 4.11.1|
shell

# Set Reboot

ascset|0,reboot,0
Example
echo -n “ascset|0,reboot,0” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753683145,Code=119,Msg=ASC 0 set OK,Description=cgminer 4.11.1|
shell

# Set Standby

ascset|0,softoff,1:timestamp
Parameter Explanation
- time stamp
Example
echo -n “ascset|0,softoff,1: 1753683300” | socat -t 300 stdio tcp:10.100.288.9:4028,shut-none && echo
shell
Response
STATUS=I,When=1753683293,Code=118,Msg=ASC 0 set info: success softoff:1753683300,Description=cgminer 4.11.1|
shell

# Set Wake-up

ascset|0,softon,1:timestamp
Parameter Explanation
- time stamp
Example
echo -n “ascset|0,softon,1: 1753683460” | socat -t 300 stdio tcp:10.100.228.9:4028,shut-none && echo
shell
Response
STATUS=I,When=1753683415,Code=118,Msg=ASC 0 set info: success softon:1753683460,Description=cgminer 4.11.1|
shell

-------------------------

tronsington | 2025-10-28 20:41:10 UTC | #16

# Avalon Q API Docs

# Query Version Information

version
Example
echo -n “version” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753681930,Code=22,Msg=CGMiner versions,Description=cgminer 4.11.1|VERSION,CGMiner=4.11.1,API=3.7,PROD=Avalon Q,MODEL=Q,HWTYPE=Q_MM1v1_X1,SWT
shell

# Query Brief Information

summary
Example
echo -n “summary” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753682020,Code=11,Msg=Summary,Description=cgminer 4.11.1|SUMMARY,Elapsed=1272,MHS av=50391540.54,MHS 5s=45851037.27,MHS 1m=39157558.90,MHS 5
shell

# Query Device Log

estats
Example
echo -n “estats” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753682105,Code=70,Msg=CGMiner stats,Description=cgminer 4.11.1|STATS=0,ID=AVALON0,Elapsed=1357,Calls=0,Wait=0.000000,Max=0.000000,Min=999999
shell

# Query Mining Pool Configuration Information

pools
Example
echo -n “pools” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753682215,Code=7,Msg=3 Pool(s),Description=cgminer 4.11.1|POOL=0,URL=stratum+tcp://10.100.106.101:5555,Status=Alive,Priority=0,Quota=1,Long
shell

# Set Mining Pool

setpool|,,,,,
Parameter Explanation
-web username，default：admin
-web login password，default : admin
-range 0-2，set which mining pool
-mining pool address
-pool worker
-pool worker password
Note: Mining pool settings will not take effect until restarting manually.
Example
echo -n “setpool|admin,admin,0,stratum+tcp://10.100.106.101:4444, avalonaging,123” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753682452,Code=133,Msg=Pool set info:
pool 0 success set to stratum+tcp://10.100.106.101:4444
worker is avalonaging
workerpassword is 123
Please reboot miner to make config work.
,Description=cgminer 4.11.1|
shell

# Set Fan Speed

ascset|0,fan-spd,
Parameter Explanation
-The value accounts for expected fan speed ratio，range：15-100 ; When SPEED is equal to -1, automatic fan speed control resumes.
Example
echo -n “ascset|0,fan-spd,100” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753682966,Code=119,Msg=ASC 0 set OK,Description=cgminer 4.11.1|
shell

# Set work mode

ascset|0,workmode,set,
Parameter Explanation
-range：0~2
Example
echo -n “ascset|0,workmode,set,1” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753683064,Code=119,Msg=ASC 0 set OK,Description=cgminer 4.11.1|
shell

# Set Reboot

ascset|0,reboot,0
Example
echo -n “ascset|0,reboot,0” | socat -t 300 stdio tcp:10.100.228.209:4028,shut-none && echo
shell
Response
STATUS=S,When=1753683145,Code=119,Msg=ASC 0 set OK,Description=cgminer 4.11.1|
shell

# Set Standby

ascset|0,softoff,1:timestamp
Parameter Explanation
- time stamp
Example
echo -n “ascset|0,softoff,1: 1753683300” | socat -t 300 stdio tcp:10.100.288.9:4028,shut-none && echo
shell
Response
STATUS=I,When=1753683293,Code=118,Msg=ASC 0 set info: success softoff:1753683300,Description=cgminer 4.11.1|
shell

# Set Wake-up

ascset|0,softon,1:timestamp
Parameter Explanation
- time stamp
Example
echo -n “ascset|0,softon,1: 1753683460” | socat -t 300 stdio tcp:10.100.228.9:4028,shut-none && echo
shell
Response
STATUS=I,When=1753683415,Code=118,Msg=ASC 0 set info: success softon:1753683460,Description=cgminer 4.11.1|
shell

-------------------------

tronsington | 2025-10-28 20:42:32 UTC | #17

# Avalon Nano 3S API Docs

# Query Version Information

version
Example
echo -n “version” | socat -t 300 stdio tcp:10.100.228.112:4028,shut-none && echo
shell
Response
STATUS=S,When=1753874463,Code=22,Msg=CGMiner versions,Description=cgminer 4.11.1|VERSION,CGMiner=4.11.1,API=3.7,PROD=Avalon Nano3s,MODEL=Nano3s,HWTYPE=N_MM
shell

# Query Brief Information

summary
Example
echo -n “summary” | socat -t 300 stdio tcp:10.100.228.112:4028,shut-none && echo
shell
Response
STATUS=S,When=1753874517,Code=11,Msg=Summary,Description=cgminer 4.11.1|SUMMARY,Elapsed=1520,MHS av=3054523.99,MHS 5s=4124783.48,MHS 1m=2986271.31,MHS 5m=2
shell

# Query Device Log

estats
Example
echo -n “estats” | socat -t 300 stdio tcp:10.100.228.112:4028,shut-none && echo
shell
Response
STATUS=S,When=1753874606,Code=70,Msg=CGMiner stats,Description=cgminer 4.11.1|STATS=0,ID=AVALON0,Elapsed=1611,Calls=0,Wait=0.000000,Max=0.000000,Min=999999
shell

# Query Mining Pool Configuration Information

pools
Example
echo -n “pools” | socat -t 300 stdio tcp:10.100.228.112:4028,shut-none && echo
shell
Response
STATUS=S,When=1753874825,Code=7,Msg=3 Pool(s),Description=cgminer 4.11.1|POOL=0,URL=stratum+tcp://10.100.106.101:4444,Status=Alive,Priority=0,Quota=1,Long
shell

# Set Mining Pool

setpool|,,,,,
Parameter Explanation
-web username，default：admin
-web login password，default：admin
-range 0-2，set which mining pool
-mining pool address
-pool worker
-pool worker password
Note: Mining pool settings will not take effect until restarting manually.
Example
echo -n “setpool|admin,admin,0,stratum+tcp://10.100.106.101:4444, avalonaging,123” | socat -t 300 stdio tcp:10.100.228.112:4028,shut-none && echo
shell
Response
STATUS=S,When=1753874998,Code=133,Msg=Pool set info:
pool 0 success set to stratum+tcp://10.100.106.101:4444
worker is avalonaging
workerpassword is 123
Please reboot miner to make config work.
,Description=cgminer 4.11.1|
shell

# Set work mode

ascset|0,workmode,set,
Parameter Explanation
-range：0~2；Low = ‘0’ , Mid = ‘1’, High = ‘2’
Example
echo -n “ascset|0,workmode,set,1” | socat -t 300 stdio tcp:10.100.228.143:4028,shut-none && echo
shell
Response
STATUS=S,When=1753928037,Code=119,Msg=ASC 0 set OK,Description=cgminer 4.11.1|
shell

# Set LED

ascset|0,ledset,effect-bright-temper-r-g-b
Parameter Explanation
-< effect >effect：0=off；1=on；2=flash；3=breath；4=loop
-< bright >brightness，range：0-100
-< temper >color temperature，range：0-100
-< r-g-b >red green blue，range：0-255
Example
echo -n “ascset|0,ledset,1-100-100-255-50-50” | socat -t 300 stdio tcp:10.100.228.20:4028,shut-none && echo
shell
Response
STATUS=I,When=1754015825,Code=118,Msg=ASC 0 set info: led set ok,Description=cgminer 4.11.1|
shell

# Set Reboot

ascset|0,reboot,0
Example
echo -n “ascset|0,reboot,0” | socat -t 300 stdio tcp:10.100.228.143:4028,shut-none && echo
shell
Response
STATUS=S,When=1753928136,Code=119,Msg=ASC 0 set OK,Description=cgminer 4.11.1|
shell
