# bitaxeorg/ESP-Miner issue #1044: PLL lookup table investigation

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1044
> Collected: 2026-10-07
> Published: 2025-06-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1044
- State: closed
- Author: mutatrum
- Opened: 2025-06-17
- Closed: 2025-08-11
- Labels: enhancement

## Description

With #1036, I wanted to take a look at generating a lookup table for the PLL settings, as the current code might be unpredictable/hard to control.

The idea is to calculate all possible PLL variables (`fb_divider`, `refdiv`, `postdiv1` and `postdiv2`) and the resulting frequency. This is done through a simple NodeJS script. Frequency is calculated by taking the `fb_divider` * 25, which is the VCO frequency, and divide that by `refdiv`, `postdiv1` and `postdiv2`.

As there are frequencies that can be achieved by different setting, the better option is to pick one with a lower VCO frequency. One example, for 525Mhz there are two options:

```
fb_divider=189 refdiv=1 postdiv1=3 postdiv2=3 for a vcoFreq of 4725MHz
fb_divider=168 refdiv=2 postdiv1=2 postdiv2=2 for a vcoFreq of 2100Mhz
```

In this case, the 2nd is preferable. Lower VCO freq is lower power consumption. When deduplicating the list, a set of 2424 unique frequencies, from 40.816327Mhz (160, 2, 7, 7) all the way up to 5975Mhz (239, 1, 1, 1).

Graphed everything is shown here:
![Image](https://github.com/user-attachments/assets/d2f2a8e0-9f8a-425e-bf88-b79b8d088e08)

What's very noticeable is there are two bands of VCO Frequencies. One strictly below 3000Mhz, and the other strictly above 4000Mhz. With the dividers, this also means there are no possible frequencies between those two ranges, it's not possible to resolve anything there. This is linked to `refdiv`, all the high frequencies are with `refdiv=1`.

Restricting vcoFreq to 3000Mhz options invalidates all solutions with `refdif=1`:
![Image](https://github.com/user-attachments/assets/9a3a05f3-0223-45a2-ae75-005ead0f38c1)

Interesting part here is there are still no resolvable frequencies between 1500Mhz and 2000Mhz.

This might be a pointer to why there sometimes are wild differences in performance and efficiency even with small frequency changes. If you are on a threshold setting, you can suddenly drop to way less efficient PLL combination. Exposing these values would certainly for OC people be interesting.

Script:
https://github.com/mutatrum/ESP-Miner/blob/pll-table/generate_pll_table.js

Generated table, limited to refdiv=2 and max frequency of 1500Mhz:
https://github.com/mutatrum/ESP-Miner/blob/pll-table/components/asic/include/pll_table.h

## Comments

### mutatrum on 2025-06-17

Looking at the code, I would like to know what `freqbuf[2]` is about, and why it's different when VCO frequency >= 2400?

![Image](https://github.com/user-attachments/assets/206f9015-78d2-4f5b-bbbe-c910fe957abf)

### mutatrum on 2025-06-17

Are these correct for the range of `fb_divider`?

BM1366/BM1368: 144 to 235
BM1370: 160 to 239

### mutatrum on 2025-06-17

Some side-by-side testing with the ramp-up of BM1368 to 490Mhz:

![Image](https://github.com/user-attachments/assets/1fac667a-1ddc-41b0-9b42-b8829a3c662c)

Some `fb_dividers` are lower with the generated table. The `postdiv1`/`postdiv2` differences are less important.

### KillerInk on 2025-06-19

Ai describe it like that

freqbuf[0] - Unknown purpose (probably reserved or not used)

freqbuf[1] - Unknown purpose (probably reserved or not used)

freqbuf[2] - This is where the VCO frequency settings are configured.

freqbuf[3] - The feedback divider setting for the PLL.

freqbuf[4] - The reference divider setting for the PLL.

freqbuf[5] - The post-scale settings for the PLL (usually used to divide down the output of the VCO)


and why 0x40 and 0x50, its there to shift the register values into the next range. with 0x40 max < 2400
if its >=2400 it need 0x50. you can see it as multiplyer i think 

> Looking at the code, I would like to know what `freqbuf[2]` is about, and why it's different when VCO frequency >= 2400?
> 
> ![Image](https://github.com/user-attachments/assets/206f9015-78d2-4f5b-bbbe-c910fe957abf)



### KillerInk on 2025-06-19

i think you are up to something. i rewrote the set frequency for the bm1370 again that it search for the smallest possible refdiv.
miner is dow to 15 watts from 16.5 and hashrate seems to have increased due lower temps but its only running for 10mins now. 


```
void BM1370_send_hash_frequency(double target_freq) {
    unsigned char freqbuf[6] = {0x00, 0x08, 0x40, 0xA0, 0x02, 0x41}; // pll0_parameter
    float newf = 200.0f;

    uint8_t best_fb_divider = 0, best_post_divider1 = 0, best_post_divider2 = 0, best_ref_divider = 0;
    float min_difference = 10.0f;
    const double max_diff = 1.0f;
    uint8_t smallest_refdiv = UINT8_MAX; // Initialize to the maximum possible value of uint8_t

    // Loop over refdiv and postdiv1, solve for postdiv2 algebraically
    for (uint8_t refdiv = 1; refdiv <= 2; ++refdiv) {
        for (uint8_t postdiv1 = 1; postdiv1 <= 7; ++postdiv1) {
            // postdiv2 = (25 * fb_divider) / (refdiv * postdiv1 * target_freq)
            // But we want integer postdiv2 in [1, postdiv1]
            for (uint8_t postdiv2 = 1; postdiv2 <= postdiv1; ++postdiv2) {
                double fb_divider_f = postdiv1 * postdiv2 * target_freq * refdiv / 25.0f;
                int fb_divider = (int)(fb_divider_f + 0.5f);
                if (fb_divider < 0xA0 || fb_divider > 0xEF) continue;

                // Check if postdiv2 is integer and in range
                double actual_freq = 25.0f * fb_divider / (refdiv * postdiv1 * postdiv2);
                double diff = fabsf(target_freq - actual_freq);

                if (diff < min_difference && diff < max_diff) {
                    best_fb_divider = fb_divider;
                    best_post_divider1 = postdiv1;
                    best_post_divider2 = postdiv2;
                    best_ref_divider = refdiv;
                    smallest_refdiv = refdiv; // Update the smallest refdiv found
                    min_difference = diff;
                    newf = actual_freq;
                }
            }
        }
    }

    // If no valid divider found, find the closest possible frequency (even if diff > max_diff)
    if (best_fb_divider == 0) {
        min_difference = 1e6f;
        for (uint8_t refdiv = 1; refdiv <= 2; ++refdiv) {
            for (uint8_t postdiv1 = 1; postdiv1 <= 7; ++postdiv1) {
                for (uint8_t postdiv2 = 1; postdiv2 <= postdiv1; ++postdiv2) {
                    double fb_divider_f = postdiv1 * postdiv2 * target_freq * refdiv / 25.0f;
                    int fb_divider = (int)(fb_divider_f + 0.5f);
                    if (fb_divider < 0xA0 || fb_divider > 0xEF) continue;

                    double actual_freq = 25.0f * fb_divider / (refdiv * postdiv1 * postdiv2);
                    double diff = fabsf(target_freq - actual_freq);

                    if (diff < min_difference) {
                        best_fb_divider = fb_divider;
                        best_post_divider1 = postdiv1;
                        best_post_divider2 = postdiv2;
                        best_ref_divider = refdiv;
                        smallest_refdiv = refdiv; // Update the smallest refdiv found
                        min_difference = diff;
                    }
                }
            }
        }
        if (best_fb_divider == 0) {
            ESP_LOGE(TAG, "Failed to find any PLL settings for target frequency %.2f", target_freq);
            return;
        }
        ESP_LOGW(TAG, "Using next best PLL settings for frequency %.2f (actual %.2f, diff %.2f)", target_freq, newf, min_difference);
    }

    freqbuf[3] = best_fb_divider;
    freqbuf[4] = best_ref_divider;
    freqbuf[5] = (((best_post_divider1 - 1) & 0xF) << 4) | ((best_post_divider2 - 1) & 0xF);

    if ((best_fb_divider * 25.0f / (float)best_ref_divider) >= 2400.0f) {
        freqbuf[2] = 0x50;
    }

    _send_BM1370(TYPE_CMD | GROUP_ALL | CMD_WRITE, freqbuf, 6, BM1370_SERIALTX_DEBUG);

    ESP_LOGI(TAG, "Setting Frequency to %.2fMHz (actual %.2f)", target_freq, newf);
}
```

### mutatrum on 2025-06-19

Not sure if this code works as designed, `smallest_refdiv` is never read.

### mutatrum on 2025-06-19

In the pull request it's now possible to set a specific float value for frequency in the OC settings:

![Image](https://github.com/user-attachments/assets/5fb95b16-5df8-4bfc-ac05-aad05765c554)

![Image](https://github.com/user-attachments/assets/f85077c7-805b-4af2-84b7-fe89e732bb34)

With this, you can select a specific set of PLL parameters:

![Image](https://github.com/user-attachments/assets/501ede18-1b82-4547-9a02-9d6b9bb25d40)

Interestingly, a lot of the frequency code was already using floats. The value was just stored as uint16 in NVS.

### KillerInk on 2025-06-20

> Not sure if this code works as designed, `smallest_refdiv` is never read.

i only left it there a reference^^ but code works, its running here.

with a frequency tabel is see only one problem that it can go big for all possible values.
for me it makes more sense as the code above does. look for the best pll match, if it can not get found increase it.

what is a bit odd that they are often on even numbers. so with that story that 1mhz can increase the hash signifactn is a possible cause they hit an invalid pll and the frequency got ignored befor. so with steps 5 or 10 while trying to oc, you will hit them

### WantClue on 2025-08-08

@mutatrum do you want this to be left open? 

### mutatrum on 2025-08-11

Closed with #1051 and #1069.
