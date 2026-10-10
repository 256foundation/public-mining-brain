# bitaxeorg/ESP-Miner issue #3: ADC is using deprecated driver. Need to be updated

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/3
> Collected: 2026-10-07
> Published: 2023-01-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 3
- State: closed
- Author: developeralgo8888
- Opened: 2023-01-21
- Closed: 2023-05-25
- Labels: none

## Description

affects  adc.c & adc.h files 

```
W (364) ADC: legacy driver is deprecated, please migrate to `esp_adc/adc_oneshot.h`
I (372) cpu_start: Starting scheduler on PRO CPU.
```

## Comments

### skot on 2023-01-21

Ooo yeah, good call. Here is the official example for the new driver; https://github.com/espressif/esp-idf/tree/master/examples/peripherals/adc/oneshot_read

### skot on 2023-01-21

I noticed from your log output in issue #1 that you have the following;

```
I (1943) DS4432U.c: Test set 1.250V = 0xB9
I (1953) DS4432U.c: Writing 0xB9
...
I (2483) i2c-test: BM1397 Vcore: 481 mV
```

those two numbers should be the same. ie the ADC reads the Vcore that the DS4432U+ and the TPS40305 set. So something isn't right. Can you read the TPS40305 output voltage with a multimeter and see what you're actually getting?

### developeralgo8888 on 2023-01-21

as per the above on Issue # 1. i just measured using the multimeter on DS4432U and TPS40305, Here is what i got 

**DS4432U**

```
Pin 1 (SDA)  == 3.25V 
Pin 2 (SCL ) == 3.25V,
Pin 3 (R21-pad1) == 0.00V
Pin 4 (GND)  == 0.00V
Pin 5 (R20-pad1) == 0.975V
Pin 6 (OUT0) == 0.600V
Pin 7 (OUT1) == 0.150V
Pin 8 (3V3)  == 3.28V , 
```

**TPS40305**
```
Pin 1 (5V) == 4.85V
Pin 2 Net(C74-pad1) == 3.8V
Pin 3 PGOOD == 3.3V
Pin 4 Net(C75-Pad1) == 0.72V
Pin 5 (OUT0)== 0.600V
Pin 6 Net(C77-Pad1) == 4.45V
Pin 7 Net(Q1-Pad4) == 0.72V
Pin 8 SW == 0.490V
Pin 9 Net(Q2-Pad4) == 4.05V
Pin 10 Net(C78-Pad1) == 4.70V

```

### skot on 2023-01-22

Actually, I don't think any of those are Vcore. I'm looking for the core voltage of the BM1387. It's the two pads on the underside of the chip. If you're using the bitaxe design you can just measure across C13, the big 330uF tantalum capacitor.

Either Vcore isn't being set right, or the ADC isn't reading right.

### developeralgo8888 on 2023-01-22

since i have 4 chips on this board i measured all 4 x 330uF tantalum capacitors behind each BM1397 chip on the chain.
Top of chain --> 0.490V for C13 for IC1 -----> 0.405V for C94 for IC2 ----> 0.295V for C95 for IC3 ----> 0.154V for C96 for IC4 ---> Bottom of chain .
i can see the Voltage drop off as expected as the chips are not under any load or mining. So the reading 481mV seems to be closer to first C13  330UF tantalum capacitor reading in top of the chain of Chips. Not sure how to read and identify each chip VCore 


### skot on 2023-01-22

Are all 4 BM1397 powered in series?

### developeralgo8888 on 2023-01-22

Yes, i believe the way S17+ is : 
   IC1 [ +Ve--A(GND) ] -----> IC2 [+Ve(A)--B(GND) ]  ------> IC3 [+Ve(B)--C(GND)] ------> IC4 [+Ve(C)--GND]

### skot on 2023-01-22

Yes the S17 has, I think 13 chips powered in series. They also provide around 20V to the chain so that each chip gets about 1.5V across it.

With 4 chips in series you'll need to give the chain around 6V so that each one gets 1.5V.

### developeralgo8888 on 2023-01-22

ok, Not sure if the components i have can safely handle 6V . i tried once to push 10V on the 4-chips with existing components and it surely fried one of the MCP1824 chips completely on one of my boards( i think the 1.8V output MCP1824 chip) . The MCP1824 is a 300 mA with Standard Fixed Output Voltages: 0.8V, 1.2V, 1.8V, 2.5V, 3.0V, 3.3V, 5.0V and Other fixed output voltages available upon request. The 2 we are using on these boards has 0.8V and 1.8V outputs. i tried pushing 6.5V and that was fine i am just worried that it might fry the 1.8V MCP1824 chip again, Any idea or suggestion . May be 10V was way too much out of Limit but 6V is way close to allowed limits of variable 5V 


### developeralgo8888 on 2023-01-22

updated the ADC Driver and was able to get some results 

```
I (1965) ADC: calibration scheme version is Curve Fitting
I (1975) ADC: Calibration Success
I (1985) ADC: ADC1 Channel[1] Raw BM1397 Core Data: 552
I (1985) ADC: ADC1 Channel[1] Cali BM1397 Core Voltage: 468 mV
I (2995) ADC: ADC1 Channel[2] Raw Data: 1079
I (2995) ADC: ADC1 Channel[2] Cali Voltage: 895 mV
I (3995) ADC: ADC2 Channel[0] Raw Data: 4095
I (3995) ADC: ADC2 Channel[0] Cali Voltage: 3086 mV
I (4995) ADC: deregister Curve Fitting calibration scheme
```

### developeralgo8888 on 2023-01-22

also looking at the declarations the old ADC driver was reffering to ESP32 GPIO37 for ADC1_CHANNEL_1  OR on ESP32-S3 GPIO2 for ADC1_CHANNEL_1 . On the New ADC oneshot driver  it still refers to GPIO2 for ADC_CHANNEL_1

```
#if CONFIG_IDF_TARGET_ESP32
typedef enum {
    ADC1_CHANNEL_0 = 0, /*!< ADC1 channel 0 is GPIO36 */
    ADC1_CHANNEL_1,     /*!< ADC1 channel 1 is GPIO37 */
    ADC1_CHANNEL_2,     /*!< ADC1 channel 2 is GPIO38 */
    ADC1_CHANNEL_3,     /*!< ADC1 channel 3 is GPIO39 */
    ADC1_CHANNEL_4,     /*!< ADC1 channel 4 is GPIO32 */
    ADC1_CHANNEL_5,     /*!< ADC1 channel 5 is GPIO33 */
    ADC1_CHANNEL_6,     /*!< ADC1 channel 6 is GPIO34 */
    ADC1_CHANNEL_7,     /*!< ADC1 channel 7 is GPIO35 */
    ADC1_CHANNEL_MAX,
} adc1_channel_t;
#elif CONFIG_IDF_TARGET_ESP32S2 || CONFIG_IDF_TARGET_ESP32S3
typedef enum {
    ADC1_CHANNEL_0 = 0, /*!< ADC1 channel 0 is GPIO1  */
    ADC1_CHANNEL_1,     /*!< ADC1 channel 1 is GPIO2  */
    ADC1_CHANNEL_2,     /*!< ADC1 channel 2 is GPIO3  */
    ADC1_CHANNEL_3,     /*!< ADC1 channel 3 is GPIO4  */
    ADC1_CHANNEL_4,     /*!< ADC1 channel 4 is GPIO5  */
    ADC1_CHANNEL_5,     /*!< ADC1 channel 5 is GPIO6  */
    ADC1_CHANNEL_6,     /*!< ADC1 channel 6 is GPIO7  */
    ADC1_CHANNEL_7,     /*!< ADC1 channel 7 is GPIO8  */
    ADC1_CHANNEL_8,     /*!< ADC1 channel 8 is GPIO9  */
    ADC1_CHANNEL_9,     /*!< ADC1 channel 9 is GPIO10 */
    ADC1_CHANNEL_MAX,
} adc1_channel_t;

```



New Driver Oneshot 
```

typedef enum {
    ADC_CHANNEL_0,     ///< ADC channel
    ADC_CHANNEL_1,     ///< ADC channel
    ADC_CHANNEL_2,     ///< ADC channel
    ADC_CHANNEL_3,     ///< ADC channel
    ADC_CHANNEL_4,     ///< ADC channel
    ADC_CHANNEL_5,     ///< ADC channel
    ADC_CHANNEL_6,     ///< ADC channel
    ADC_CHANNEL_7,     ///< ADC channel
    ADC_CHANNEL_8,     ///< ADC channel
    ADC_CHANNEL_9,     ///< ADC channel
} adc_channel_t;
```

### developeralgo8888 on 2023-01-22

Can you measure your VDD voltage on Bitaxe_v2 board ? because that should be the voltage being supplied to the BM1397 chip? What should the initial value of VDD be ? 1.8V , 3.3V or 5V or higher or lower ? 

### developeralgo8888 on 2023-01-23

My voltage reading on the Bitaxe_v2  (BM1397 1-Chip ) is now reading correctly.

```
I (1935) DS4432U.c: Test set 1.500V = 0x0C
I (1935) DS4432U.c: Writing 0x0C
I (2445) i2c-test: Board Fan Speed: 1713 RPM
I (2445) EMC2101.c: EMC2101 Chip Internal Temp: 27 C
I (2445) i2c-test: BM1397 Chip Internal Temp: 16.84 C
I (2445) i2c-test: Board Current: 4481 mA
I (2455) i2c-test: Board Voltage: 36818 mV
I (2455) i2c-test: Board Power: 24064 mW
I (2485) ADC: ADC1 Channel[1] Raw BM1397 Core Data: 1893
I (2485) ADC: ADC1 Channel[1] Cali BM1397 Core Voltage: 1551 mV
```

i did send you a quick general question about 6V VDD or 1.5V  VDD for BM1397 4-chips board. if you can check the question that would be great.
