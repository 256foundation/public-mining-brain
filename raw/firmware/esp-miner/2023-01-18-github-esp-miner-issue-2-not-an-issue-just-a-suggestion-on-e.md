# bitaxeorg/ESP-Miner issue #2: Not an issue - just a suggestion on EMC2101.c

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/2
> Collected: 2026-10-07
> Published: 2023-01-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 2
- State: closed
- Author: developeralgo8888
- Opened: 2023-01-18
- Closed: 2023-05-24
- Labels: bug

## Description

ESP_LOGI(TAG, "Fan Speed = %d RPM", RPM); 

Change the formatter to   %lu  for unint_32t 

## Comments

### skot on 2023-01-18

yess! I'm so happy to have you helping on this project :)

### developeralgo8888 on 2023-01-19

Now i am able to read all sensors except the BM1397 chip , i will try and start or get to that later today .

```
I (1439) esp_netif_handlers: sta ip: 10.0.0.134, mask: 255.255.255.0, gw: 10.0.0.1
I (1439) i2c-test: got ip:10.0.0.134
I (1439) i2c-test: connected to ap SSID:ABHomie
I (1449) i2c-test: Init LEDs!
I (1449) i2c-test: I2C initialized successfully
I (1459) DS4432U.c: DS4432U+ OUT1 = 0xFC
I (1459) DS4432U.c: Writing 0x00
I (1459) i2c-test: Test set 1.000V = 0xFC
I (1469) DS4432U.c: Writing 0xFC
I (1469) EMC2101.c: EMC2101 PRODUCT ID = 0x28
I (3479) EMC2101.c: Raw Fan Speed = FF FF
I (3479) EMC2101.c: Fan Speed = 82 RPM
I (3479) INA260.c: INA260 MANUFACTURE ID = 0x5449
I (3479) INA260.c: INA260 DIE ID = 0x2270
I (3479) INA260.c: INA260 CONFIG VALUE = 0x6127
I (3489) INA260.c: INA260 ENABLE ALERT VALUE = 0x0008
I (3499) INA260.c: INA260 ALERT LIMIT VALUE = 0x0000
I (3499) INA260.c: INA260 SHUNT CURRENT = 0xFFEA
I (3509) INA260.c: INA260 BUS VOLTAGE = 0x09C4
I (3509) INA260.c: INA260 POWER = 0x0009
I (3519) i2c-test: Install temperature sensor, expected temp ranger range: 10~50 ℃
I (3519) temperature_sensor: Range [-10°C ~ 80°C], error < 1°C
I (3529) i2c-test: Enable temperature sensor
I (3539) i2c-test: ESP32-S3 Temperature value 30.46 ℃
I (3539) i2c-test: I2C de-initialized successfully


```

i used the code below to format it correctly while reading the INA260 sensor 


```
void INA260_read(void) {
    uint8_t data[3];

    
    ESP_ERROR_CHECK(register_read(INA260_MANFID_REG, data, 2));
    ESP_LOGI(TAG, "INA260 MANUFACTURE ID = 0x%02X%02X", data[0], data[1]);

    ESP_ERROR_CHECK(register_read(INA260_DIEID_REG, data, 2));
    ESP_LOGI(TAG, "INA260 DIE ID = 0x%02X%02X", data[0], data[1]);

    ESP_ERROR_CHECK(register_read(INA260_CONFIG_REG, data, 2));
    ESP_LOGI(TAG, "INA260 CONFIG VALUE = 0x%02X%02X", data[0], data[1]);

    ESP_ERROR_CHECK(register_read(INA260_MASK_ENABLE_REG, data, 2));
    ESP_LOGI(TAG, "INA260 ENABLE ALERT VALUE = 0x%02X%02X", data[0], data[1]);

    ESP_ERROR_CHECK(register_read(INA260_ALERT_LIMIT_REG, data, 2));
    ESP_LOGI(TAG, "INA260 ALERT LIMIT VALUE = 0x%02X%02X", data[0], data[1]);
    
    ESP_ERROR_CHECK(register_read(INA260_CURRENT_REG, data, 2));
    ESP_LOGI(TAG, "INA260 SHUNT CURRENT VALUE = 0x%02X%02X", data[0], data[1]);

    ESP_ERROR_CHECK(register_read(INA260_BUS_VOLTAGE_REG, data, 2));
    ESP_LOGI(TAG, "INA260 BUS VOLTAGE VALUE = 0x%02X%02X", data[0], data[1]);

    ESP_ERROR_CHECK(register_read(INA260_POWER_REG , data, 2));
    ESP_LOGI(TAG, "INA260 POWER VALUE = 0x%02X%02X", data[0], data[1]);
    
}
```


 

### skot on 2023-01-19

Niice! Do you have a 4-pin fan? I'm getting 82 RPM on my Noctua fan too -- that's definitely not right.

### developeralgo8888 on 2023-01-19

Yes, that's not correct if PWM fans are plugged in. Let me check 

Bought  two Noctua NF-A4x20 5V PWM 4-Pin fans arriving today by amazon for speed adjustment testing. Currently i don't have any 5V fan to use for speed testing but will later today. 

### skot on 2023-01-19

I think you need to set the `ALT_TCH` bit in the configuration register to enable the TACH function. I tried that, but still didn't get much. I'd be curious to know what you come up with. Although BM1397 communication is prolly more important!

<img width="1498" alt="image" src="https://user-images.githubusercontent.com/140785/213477763-3e3d91ba-9cae-42f9-baee-5f252a8944c4.png">


### skot on 2023-01-19

Also Adafruit has a Arduino EMC2101 driver to look at for reference; https://github.com/adafruit/Adafruit_EMC2101

### developeralgo8888 on 2023-01-19

that's great i will give it a crack once the 5V fans arrive.

### skot on 2023-01-19

there is also a INA260 Adafruit Arduino library; https://github.com/adafruit/Adafruit_INA260 -- that might be helpful for converting those register values into Volts and Amps

### developeralgo8888 on 2023-01-19

great . That's helpful. thanks . I was looking at the EMC2101 code and it seems we didn't activate the PWM bit and then write a value for speed


### skot on 2023-01-19

I am able to control the speed though. Not sure what's going on there. I'm going to take a look at this tonight.

### developeralgo8888 on 2023-01-19

did you update the fan speed code ? just got my 5V fans from amazon

### developeralgo8888 on 2023-01-20

The are the results from last code update 

```

I (1933) i2c-test: got ip:10.0.0.34
I (1933) i2c-test: connected to ap SSID:ABHomie
I (1943) i2c-test: I2C initialized successfully
I (1943) DS4432U.c: Test set 1.250V = 0xB9
I (1953) DS4432U.c: Writing 0xB9
I (2453) i2c-test: Fan Speed: 1028 RPM
I (2453) i2c-test: Chip Temp: 110.50 C
I (2453) i2c-test: Current: 8384 mA
I (2453) i2c-test: Voltage: 24018 mV
I (2453) i2c-test: Power: 33280 mW
I (2463) i2c-test: Vcore: 481 mV
I (2463) temperature_sensor: Range [-10°C ~ 80°C], error < 1°C
I (2473) i2c-test: ESP32-S3 Temperature value 36.60 ℃
I (2473) i2c-test: I2C de-initialized successfully
```

Looking at the tests i think we have a wrong readings for EMC2101 Temp sensor , The current ambient temperature here is about  18 C  but it's reading  110.50 C  .

### developeralgo8888 on 2023-01-20

Looking at the adafriut files for EMC on reading the external temperature of the chip and comparing it with the code we are working on . This is my understanding of that code, reads MSB(buffer[0])   then LSB (buffer[1]) then does a bitwise left shift for 8 spaces (<< ) to shift the binary value in the Buffer[0]  (MSB Value) but not Buffer[1] (LSB value) .It then performs a bitwise OR operation ( | )  on each pair of bit sequence ( MSB  and LSB )  i.e buffer[0] and buffer[1] and shifts result  5 spaces to the right. Does that sound right , considering "reading" is a 16-bit uint?

FYI on the EMC2101 datasheet pg 33 on temp data registers. 
As shown in Table 6.2, the internal temperature monitor is stored as an 8-bit value while the external temperature is stored as an 11-bit value.
Please note that the internal temperature monitor is limited to the operating temperature limits of the
part resulting in a guaranteed range of 0ºC to 85ºC.

### skot on 2023-01-20

I _think_ that's right. Maybe not the most efficient way of doing it.

<img width="1386" alt="image" src="https://user-images.githubusercontent.com/140785/213762276-b0579253-9c7c-4ca0-8511-c3cd523515ee.png">

The external diode temperature is a 11 bit, fixed-point decimal. The strange part is that the LSB is left-shifted by 5 in the EMC2101 register. 

so, take the two 8-bit registers and make a 16-bit number. Then right shift it all to make a 11-bit number. Then divide by 8.0 to make it a float and right shift 3.

### developeralgo8888 on 2023-01-20

Did a quick test by changing this code in EMC2101.c:

```
float EMC2101_get_chip_temp(void) {
    uint8_t temp_msb, temp_lsb;
    uint16_t reading;
    uint8_t  temp_shifted_msb;

    ESP_ERROR_CHECK(register_read(EMC2101_EXTERNAL_TEMP_MSB, &temp_msb, 1));
    ESP_ERROR_CHECK(register_read(EMC2101_EXTERNAL_TEMP_LSB, &temp_lsb, 1));
    
    ESP_LOGI(TAG, "After Reading MSB  LSB = %X %X", temp_msb, temp_lsb);
    temp_shifted_msb = (temp_msb << 8);
    ESP_LOGI(TAG, "After 8 bits Left shift MSB = %X %X", temp_shifted_msb, temp_lsb);
    reading = temp_lsb | temp_shifted_msb ;
    ESP_LOGI(TAG, "After BitWise OR -- Reading = 0x%X", reading);
    reading >>= 5;
    ESP_LOGI(TAG, "After 5 Spaces Right Shift -- Reading = 0x%X", reading);

    //return (float)reading / 8.0;
    return (float)reading ;


```

It seems it  (temp_msb << 8 ) was not being shifted correctly
i.e reading = temp_lsb | (temp_shifted_msb << 8 ) ;
so i tried storing that value in a different variable and then doing the bitwise OR  to see what was going on  and compared it with manual values i would expect if the process was performed . 

Below is what i get

```
I (1963) i2c-test: Fan Speed: 1865 RPM
I (1963) EMC2101.c: After Reading MSB  LSB = 6D 60
I (1963) EMC2101.c: After 8 bits Left shift MSB = 0 60
I (1963) EMC2101.c: BitWise -- Reading = 0x60
I (1973) EMC2101.c: After Reading 5 Spaces Right Shift -- Reading = 0x3
I (1963) i2c-test: EMC2101 Chip Temp: 3.00 C
```
that's a little low 

### skot on 2023-01-20

I think this is a problem;
`temp_shifted_msb = (temp_msb << 8);`
temp_shifted_msb is a uint8_t, so left shifting by 8 is going to lose all those bits

change to `uint16_t  temp_shifted_msb;` and you should be good. Don't forget to divide by 8.0

### developeralgo8888 on 2023-01-20

exactly what i was thinking just now 

### skot on 2023-01-20

How'd that work out? Does your chip temp look better?

It seems like you are having some of the same problems as me with the INA260.. those voltage, current and power numbers don't look right.

### developeralgo8888 on 2023-01-20

i think on EMC2101 , The reading or our calculation are not correct . i did this quick reading test to see the difference between Internal  & external EMC2101 temperatures .


```
float EMC2101_get_chip_temp(void) {
    uint8_t temp_msb, temp_lsb, temp_int;
    uint16_t reading, shifted_temp_msb, shifted_temp_lsb;
    
    ESP_ERROR_CHECK(register_read(EMC2101_EXTERNAL_TEMP_MSB, &temp_msb, 1));
    ESP_ERROR_CHECK(register_read(EMC2101_EXTERNAL_TEMP_LSB, &temp_lsb, 1));
   
    shifted_temp_msb = temp_msb;
    shifted_temp_lsb = temp_lsb;    
    reading = shifted_temp_lsb  | (shifted_temp_msb << 8) ;
    reading >>= 5;

    ESP_ERROR_CHECK(register_read(EMC2101_INTERNAL_TEMP, &temp_int, 1));
    ESP_LOGI(TAG, "EMC2101 Chip Internal Temp:   = %d C", temp_int);

    return (float)reading / 8.0;
}


```
Results:

```
I (1953) EMC2101.c: EMC2101 Chip Internal Temp:   = 27 C
I (1953) i2c-test: EMC2101 Chip External Temp: 115.88 C

```
 
That's a huge discrepancy between internal and external  EMC2101 Temp values 



### skot on 2023-01-20

yeah 115.88 C is too hot. When I run it I get around 32 C, which seems plausible.

Can you show me the hex values you get for `EMC2101_EXTERNAL_TEMP_MSB` and `EMC2101_EXTERNAL_TEMP_LSB` ?

### developeralgo8888 on 2023-01-21

As you can see below 

EMC2101_EXTERNAL_TEMP_MSB  =  `0X70 `and EMC2101_EXTERNAL_TEMP_LSB = `0XC0 `

```
I (1943) i2c-test: I2C initialized successfully
I (1943) DS4432U.c: Test set 1.250V = 0xB9
I (1953) DS4432U.c: Writing 0xB9
I (2453) i2c-test: Board Fan Speed: 1756 RPM
I (2453) EMC2101.c: EMC2101 Chip Internal Temp: 26 C
I (2453) EMC2101.c: BM1397 Internal Temp via EMC2101: 0X70 0XC0 C
I (2453) i2c-test: BM1397 Chip Internal Temp: 112.75 C
I (2463) i2c-test: Board Current: 14144 mA
I (2463) i2c-test: Board Voltage: 1618 mV
I (2473) INA260.c: Raw Power = 97 00
I (2473) i2c-test: Board Power: 58880 mW
I (2483) i2c-test: BM1397 Vcore: 481 mV
I (2483) temperature_sensor: Range [-10°C ~ 80°C], error < 1°C
I (2493) i2c-test: ESP32-S3 Temp: 36.16 ℃
I (2493) i2c-test: I2C de-initialized successfully
```

### developeralgo8888 on 2023-01-21

quick question : I was just investigating the issue.  if the EMC2101  DP & DN pins which are basically connected to Temp_P and Temp_N of the BM1397 Chip(s) . How does EMC2101 deal with several BM1397 chips connected ?  lets say you have  4 x BM1397 chips ? Does it just read each BM1397 chip temperature and add all those individual chip temps to get an aggregate value to be stored in MSB & LSB  or does it read each and just report that individual temp of BM1397 .

From the Datasheet: pg.22 
In general, thermal diode temperature measurements are based on the change in forward bias voltage
of a diode when operated at two different currents. The change in forward bias voltage is proportional
to absolute temperature (T)

This would lead me to believe that if you have more than 1 x BM1397 chips it will add the temps of each individual BM1397 chips and report the Absolute aggregate since i don't see how it will distinguish each chip on the chain. so lets say you have 4 chips and the  absolute aggregate temp = 120 C then you divide that by 4 to get average temp of each chip. It sounds strange and inefficient but that's the only thing i could think might be happening with my 4-chip BM1397 board. Not sure but just a theory since in this case i have 4 x BM1397 Chips connected to a single EMC2101 external Thermal diode with (Temp_P & Temp_N)


### skot on 2023-01-21

As far as I understand it, Temp_P & Temp_N are just connected to a temperature sensitive diode inside the BM1397. Because of this I'm pretty sure you need a separate EMC2101 for each BM1397. This is why the S9 (and maybe the S17) don't give you the chip temp for _every_ chip on the hashboard, just a couple. 

The S9 uses the NCT218, which is just a thermal diode reader, not a fan controller. I used one of those on a previous bitaxe rev and it worked well.

Do you have multiple BM1397's hooked up to a single EMC2101? This might be why you are getting incorrect temperature readings.

### skot on 2023-01-21

> As you can see below
> 
> EMC2101_EXTERNAL_TEMP_MSB = `0X70 `and EMC2101_EXTERNAL_TEMP_LSB = `0XC0 `
> 
> ```
> I (1943) i2c-test: I2C initialized successfully
> I (1943) DS4432U.c: Test set 1.250V = 0xB9
> I (1953) DS4432U.c: Writing 0xB9
> I (2453) i2c-test: Board Fan Speed: 1756 RPM
> I (2453) EMC2101.c: EMC2101 Chip Internal Temp: 26 C
> I (2453) EMC2101.c: BM1397 Internal Temp via EMC2101: 0X70 0XC0 C
> I (2453) i2c-test: BM1397 Chip Internal Temp: 112.75 C
> I (2463) i2c-test: Board Current: 14144 mA
> I (2463) i2c-test: Board Voltage: 1618 mV
> I (2473) INA260.c: Raw Power = 97 00
> I (2473) i2c-test: Board Power: 58880 mW
> I (2483) i2c-test: BM1397 Vcore: 481 mV
> I (2483) temperature_sensor: Range [-10°C ~ 80°C], error < 1°C
> I (2493) i2c-test: ESP32-S3 Temp: 36.16 ℃
> I (2493) i2c-test: I2C de-initialized successfully
> ```

Okay 0x70C0 -> 112.75 by my calculation too. So I think you're doing the conversion right.
