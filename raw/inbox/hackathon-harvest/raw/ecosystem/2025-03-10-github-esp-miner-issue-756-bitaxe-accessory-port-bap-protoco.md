# bitaxeorg/ESP-Miner issue #756: Bitaxe Accessory Port (BAP) Protocol

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/756
> Collected: 2026-10-07
> Published: 2025-03-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 756
- State: closed
- Author: skot
- Opened: 2025-03-10
- Closed: 2025-08-21
- Labels: enhancement, help wanted

## Description

BAP protocol is 115200 baud (default). 
format is standard NMEA sentences (in ASCII). Connected accessories can "ask" for any parameter available over the web API. 
accessories can also "subscribe" to receive regular notifications on selected parameters.

## Comments

### mutatrum on 2025-03-10

A quick search found this: https://stackoverflow.com/a/41823625, seems relevant.

You need some sort of packet layer with checksum, otherwise the traffic will very easily get out of sync.



### skot on 2025-03-10

> A quick search found this: https://stackoverflow.com/a/41823625, seems relevant.
> 
> You need some sort of packet layer with checksum, otherwise the traffic will very easily get out of sync.

I think NMEA sentences are the solution here. They have a start byte (`$`), opcode, delimiters (`,`), stop byte (`*`), and a checksum. 

### skot on 2025-03-10

Here is an example of NMEA sentences used in a GPS module; https://aprs.gids.nl/nmea/

### CryptoIceMLH on 2025-03-10

100K SATs - BOUNTY! - Submitted to
https://osmu.wiki/
to start the dev work on bitaxe BAP port


![Image](https://github.com/user-attachments/assets/370f0b30-bac5-43dd-b302-7318bf6823cf)

### CryptoIceMLH on 2025-03-12

> BAP protocol is 115200 baud (default). format is standard NMEA sentences (in ASCII). Connected accessories can "ask" for any parameter available over the web API. accessories can also "subscribe" to receive regular notifications on selected parameters.

Noob proposal starting from a plain and simple esp32 -> esp32 setup 

**1. Hardware Connections:**

- UART Communication:

- [ ] Connect GPIO32 (TX) of the first ESP32 to GPIO33 (RX) of the second ESP32.

- [ ] Connect GPIO33 (TX) of the first ESP32 to GPIO32 (RX) of the second ESP32.

- [ ] Ensure both devices share a common ground (GND).

**2. BAP Protocol Overview:**

The BAP protocol utilizes NMEA 0183 sentence structures for communication. Each message follows this format:


`$BAP,<command>,<parameter>,<value>*<checksum>\r\n`
`$BAP:` Protocol identifier.
`<command>:` Type of message (e.g., REQ for request, RES for response, SUB for subscription).
`<parameter>:` Specific parameter name.
`<value>:` Value associated with the parameter.
`*<checksum>:` Checksum for error detection.
`\r\n:` Carriage return and line feed, marking the end of the sentence.

**3. ESP32 Firmware Implementation:**

Include Necessary Libraries:**

`#include <HardwareSerial.h>`

**Define UART Parameters:**

```
const int uart\_num = 1; // Use UART1 
const int uart\_tx\_pin = 32; // GPIO32 for TX 
const int uart\_rx\_pin = 33; // GPIO33 for RX 
const int uart\_baud\_rate = 115200; 
HardwareSerial mySerial(uart\_num);
```

**Initialize UART:**

```
 void init_uart() {
    mySerial.begin(uart_baud_rate, SERIAL_8N1, uart_rx_pin, uart_tx_pin);
  }
```

**Calculate Checksum:**

```
  uint8_t calculate_checksum(const String& sentence) {
    uint8_t checksum = 0;
    for (size_t i = 1; i < sentence.length(); i++) {
      checksum ^= sentence[i];
    }
    return checksum;
  }
```

**Send NMEA Sentence:**

 ```
 void send_nmea_sentence(const String& sentence) {
    uint8_t checksum = calculate_checksum(sentence);
    String nmea_sentence = "$BAP," + sentence + "*" + String(checksum, HEX) + "\r\n";
    mySerial.print(nmea_sentence);
  }
```

**Parse Incoming Messages:**


```
 void parse_message(const String& message) {
    // Example: Handle "pow" command
    if (message.startsWith("pow")) {
      Serial.println("hello pow");
    }
    // Add more command handlers as needed
  }
```

**Main Loop:**

  ```
void setup() {
    Serial.begin(115200); // Initialize serial monitor
    init_uart();
    // Additional setup code
  }

  void loop() {
    if (mySerial.available()) {
      String message = mySerial.readStringUntil('\n');
      parse_message(message);
    }
    // Additional loop code
  }
```



`


### fatzac on 2025-03-13

BAP Protocol Overview:
The BAP protocol utilizes NMEA 0183 sentence structures for communication. 

Each message follows this format:
`$BAP,<command>,<parameter>,<value>*<checksum>\r\n `

```
$BAP: Protocol identifier. 
<command>: Type of message (e.g., REQ for request, RES for response, SUB for subscription). 
<parameter>: Specific parameter name. 
<value>: Value associated with the parameter. 
*<checksum>: Checksum for error detection. 
\r\n: Carriage return and line feed, marking the end of the sentence. // NMEA uses CR and LF respectively
```


Reserved characters used by NMEA

```
<CR> - Carriage return. // \r in BAP
<LF> - Line feed, end delimiter. // \n in BAP
! - Start of encapsulation sentence delimiter.
$ - Start delimiter.
* - Checksum delimiter.
, - Field delimiter.
\ - TAG block delimiter
^ - Code delimiter for HEX
```

BAP vs NMEA sentence format

Main talker ID + Type of Message (3 letters)
// NMEA is 2 letters - BAP is 3


Main talker ID: BAP


**BAP Sentences**


**$BAPREQ - Request for Information**

Purpose:

Request specific information from the Bitaxe system.

Format:

`$BAP,REQ,<parameter>*<checksum>\r\n`

Example:

`$BAP,REQ,power*4B\r\n`



**$BAPRES - Response with Information**

Purpose: Response with the requested information from the Bitaxe system.

Format:

`$BAP,RES,<parameter>,<value>*<checksum>\r\n`

Example:

Responding with power information:

`$BAP,RES,power,58.35174560546875*5F\r\n`



**$BAPSUB - Subscription to Updates** 

Purpose: Subscribe to periodic updates for specific parameters. 

Format:

`$BAP,SUB,<parameter>*<checksum>\r\n`

Example:

Subscribing to hash rate updates:

`$BAP,SUB,hashRate*6A\r\n`



**$BAPSET - Set a Parameter**

Purpose: To set or update a specific parameter on the Bitaxe system.

Format: 

`$BAP,SET,<parameter>,<value>*<checksum>\r\n`

Example:

Set fan speed to 50:

`$BAP,SET,fanSpeed,50*7C\r\n`



**$BAPACK - Acknowledgment** 

Purpose: To acknowledge the receipt of a command.

Format:

`$BAP,ACK,<parameter>*<checksum>\r\n`

Example:

Acknowledges receipt of a power request:

`$BAP,ACK,power*3D\r\n`



**$BAPERR - Error Message**

Purpose: To report an error or issue.

Format:

`$BAP,ERR,<parameter>,<error_code>*<checksum>\r\n`

Example:

Reports an error with setting the fan speed.

`$BAP,ERR,fanSpeed,01*5E\r\n`



**$BAPCMD - Execute Command**

Purpose: To execute a specific command.

Format:

`$BAP,CMD,<command>*<checksum>\r\n`

Example:

Executes the restart command.

`$BAP,CMD,restart*4F\r\n`



**$BAPSTA - System Status**

Purpose: To report the current status of the Bitaxe system.

Format:

`$BAP,STA,<status_code>*<checksum>\r\n`

Example:

Reports that the system status is OK.

`$BAP,STA,OK*2E\r\n`



**$BAPLOG - Log Message**

Purpose: To log a message or event.

Format:

`$BAP,LOG,<message>*<checksum>\r\n`

Example:

Logs the message “System Restarted”.

`$BAP,LOG,System Restarted*1A\r\n`

### skot on 2025-03-13

Yes!! This is great!

My only suggestion would be to have the subscription responses contain many related values in one sentence (with a fixed order) like voltage, power, current, temps, etc.

### CryptoIceMLH on 2025-03-13

> Yes!! This is great!
> 
> My only suggestion would be to have the subscription responses contain many related values in one sentence (with a fixed order) like voltage, power, current, temps, etc.

yeah would be nice to call individual data when needed but a standardised stream of data on the sub is a great idea. ontop of sensor data do we want a separate subscription stream that outputs mining related data instead like , pool status, hashrate, share count/ status etc

### fatzac on 2025-03-13

We will have to define the commands and then create handler functions, but we should be able to have subscription responses with multiple values. 

### Subscription Command
- **$BAPSUB** - Subscription to Updates
  - **Purpose**: Subscribe to periodic updates for specific parameters.
  - **Format**: `$BAP,SUB,<parameters>*<checksum>\r\n`
  - **Example**: `$BAP,SUB,systemInfo*3E\r\n`
  - **Description**: Subscribe to updates for system information.

### Subscription Response
- **$BAPRES** - Response with Information (Multiple Values)
  - **Purpose**: Provide periodic updates for subscribed parameters.
  - **Format**: `$BAP,RES,<parameter1>,<value1>,<parameter2>,<value2>,...,<parameterN>,<valueN>*<checksum>\r\n`
  - **Example**: `$BAP,RES,voltage,11906.25,power,58.35174560546875,current,16281.25,temp,58,boardtemp1,30,boardtemp2,48*6B\r\n`
 

To parse incomings messages:

'void parse_message(const String& message) {
  int comma1 = message.indexOf(',');
  int comma2 = message.indexOf(',', comma1 + 1);
  int comma3 = message.indexOf(',', comma2 + 1);
  int asterisk = message.indexOf('*');

  String command = message.substring(comma1 + 1, comma2);
  String parameter = message.substring(comma2 + 1, comma3);

  if (command == "SUB") {
    handle_subscription_request(parameter);
  } else {
    Serial.println("Unknown command");
  }
}'

I'm not sure if we have to define the interval for periodic updates in the main loop.

### mutatrum on 2025-03-14

I would opt against multiple values on a single line, unless they are a pair. The counter example from GPS is Lat/Long, as that's a single position, but in the Bitaxe environment there are no such value pairs. Another point here is that different values might be read from sensors with different timings, so sending them as soon as they are read would be simpler implementation wise. Decoding implementation is also simpler that way.

Having said that: what's the frequency of updates? IIRC in GPS NMEA it's as fast as they are available, which can be different per device. For BAP, should a `SUB` command also have an update frequency, or will we always send the newest data as it comes available?
