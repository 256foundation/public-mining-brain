# bitaxeorg/ESP-Miner issue #89: Consider adding Login page for AxeOS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/89
> Collected: 2026-10-07
> Published: 2024-01-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 89
- State: closed
- Author: StellarStoic
- Opened: 2024-01-14
- Closed: 2024-10-10
- Labels: enhancement, help wanted, good first issue, question

## Description

Can we get a login page to AxeOS? The network can be easily compromised by my curious nephew and masses with my Bitaxe settings :)



## Comments

### skot on 2024-02-16

we could prolly do basic http auth, but that's not real security. maybe just create a new subnet and don't let your nephew on? 😂

### ChimpRocket on 2024-03-28

Hi, I was just here looking to see if someone had already requested this.  My Supra is yet to arrive (I'm so excited :-) ), so I was watching a few YouTube vids and noted @skot talking about the milestone of having 1 million BitAxes online. I work in IT Security and this got me thinking about the IoT security implications. With that much hash power, and so many devices, some bad actors may write malware to try and steal it.  Then today I saw @WantClue 's video on AxeOS and noticed that its a completely anonymous admin portal. And the API calls can also be done anonymously.  

Might be worth baking some security options in early to give users the capability to better secure their IoT miners, and the entire BitAxe pool.  

What about a LetsEncrypt server cert and basic auth as a minimum? Would that be possible?

Thanks and keep up the good work! Loving this project :-)



### benjamin-wilson on 2024-03-29

Issuing https certs to the devices would be a complex task without much benefit, these devices are designed to operate on LAN. (no miners I know of use https) If there is a malicious actor with access to your LAN you've got bigger problems. Stratum protocol also operates over cleartext. 

### MyOwn2C on 2024-03-29

Easier to secure your WLAN than to make AxeOS too bloated.
Add MAC address filter to your WLAN so they can't use it or access your Bitaxe even if they know your SSID and password.
Setup your router firewall and port forwarding so you have control what traffic are going in/out of your router and your WLAN devices.
Encrypting traffic is meaningless as the design intent for blockchain is that EVERYTHING is open. 
Intercepting stratum protocol traffic between the Bitaxe and the pool to know your wallet address etc poses no security threats.
You can also setup VPN on your router.

### ChimpRocket on 2024-03-29

Hi guys. Thanks for the responses. I suppose you have a point about the lack of TLS generally on the blockchain but I still think securing the miner would be a good idea to protect what we are trying to achieve here. Forget me and my network for a moment as this isn't about me but perhaps about those who aren't as tech savvy to create separate vlans, ssids and vpns etc. 

### garretpremo on 2024-04-26

@skot I can implement a login page with http basic or JWT authentication if this is still desired.

### StellarStoic on 2024-04-27

> @skot I can implement a login page with http basic or JWT authentication if this is still desired.

I think it's still better than nothing :)

### skot on 2024-04-27

> @skot I can implement a login page with http basic or JWT authentication if this is still desired.

We should prolly secure the api too?

### benjamin-wilson on 2024-04-27

As everything is over http securing AxeOS is kinda pointless, you should secure your LAN. This also has other effects like the processing overhead to auth every request, esp-miner bloat,.swarm etc. This is a NAK from me

### garretpremo on 2024-05-03

> We should prolly secure the api too?

Yeah, definitely.

> As everything is over http securing AxeOS is kinda pointless, you should secure your LAN.

If we do end up setting up https with the intent to fully secure AxeOS, this issue will need to be tackled, so it could be a good stepping stone. And as @StellarStoic mentioned it's better than nothing.

> This also has other effects like the processing overhead to auth every request, esp-miner bloat,.swarm etc.

Processing overhead seems somewhat negligible, we're talking about a dozen or so extra clock cycles per request.

For the sake of compromise, what if we only secured modifying endpoints? i.e. everything _except_ GET requests? I imagine most people use AxeOS as a monitoring tool and don't change settings often.

On the topic of bloat: a login page, after gzip, would only add on the order of a fraction of a kB to the bundle.

I am admittedly unfamiliar with the swarm aspect of AxeOS, so I would need a bit more information on how auth would affect that.

At the end of the day if we don't want login/auth, that's cool, I am just eager to contribute lol

### ghost on 2024-05-09

Adding a simple onboard firewall would be beneficial, reminiscent of early miners like the S3 that featured similar capabilities. Implementing IP filtering could control which clients have server access, using either a whitelist (allowing only specific IPs) or a blacklist (blocking known problematic IPs).


```
#include <string.h>
#include "lwip/ip4_addr.h"

#define MAX_IP_WHITELIST 10

// List of whitelisted IP addresses
static ip4_addr_t ip_whitelist[MAX_IP_WHITELIST];
static int whitelist_count = 0;

// Function to add an IP to the whitelist
void add_ip_to_whitelist(const char* ip) {
    if (whitelist_count < MAX_IP_WHITELIST) {
        ip4addr_aton(ip, &ip_whitelist[whitelist_count]);
        whitelist_count++;
    }
}

// Firewall check function
static bool check_ip_whitelisted(const char* ip) {
    ip4_addr_t addr;
    ip4addr_aton(ip, &addr);
    for (int i = 0; i < whitelist_count; i++) {
        if (ip4_addr_cmp(&addr, &ip_whitelist[i])) {
            return true;
        }
    }
    return false;
}

```

Integrate IP filtering in your HTTP request handlers to check the IP address of incoming requests before processing

```
// Modify handler to include IP check
static esp_err_t rest_common_get_handler(httpd_req_t *req) {
    char* client_ip = ip4addr_ntoa((ip4_addr_t *)&(req->remote_ip));

    if (!check_ip_whitelisted(client_ip)) {
        ESP_LOGW(TAG, "Access denied for IP: %s", client_ip);
        httpd_resp_send_err(req, HTTPD_403_FORBIDDEN, "Access denied");
        return ESP_FAIL;
    }

    char filepath[FILE_PATH_MAX];
    // Handle the request as before if IP is allowed
    ...
}
```

Secure Login via SSL/TLS
Implement SSL/TLS to encrypt login data, ensuring secure data transmission.

```
Generate a private key
openssl genrsa -out server.key 2048

 Generate a certificate signing request (CSR)
openssl req -new -key server.key -out server.csr

Generate a self-signed certificate
openssl x509 -req -days 365 -in server.csr -signkey server.key -out server.crt
```

Server Initialization with mbedtls:

```
#include "esp_https_server.h"

// HTTPS server configuration
httpd_ssl_config_t config = HTTPD_SSL_CONFIG_DEFAULT();

esp_err_t start_https_server(void) {
    extern const unsigned char server_crt_start[] asm("_binary_server_crt_start");
    extern const unsigned char server_crt_end[] asm("_binary_server_crt_end");
    extern const unsigned char server_key_start[] asm("_binary_server_key_start");
    extern const unsigned char server_key_end[] asm("_binary_server_key_end");

    config.cacert_pem = server_crt_start;
    config.cacert_len = server_crt_end - server_crt_start;
    config.prvtkey_pem = server_key_start;
    config.prvtkey_len = server_key_end - server_key_start;

    httpd_handle_t server = NULL;
    if (httpd_ssl_start(&server, &config) == ESP_OK) {
        // Register handlers
        httpd_register_uri_handler(server, &login_post_handler);
        // Other handlers...
        return ESP_OK;
    }
    return ESP_FAIL;
}

```


SSL/TLS for Form-Based Login:

```
<form action="https://your-esp32-ip/login" method="post">
    Username: <input type="text" name="username"><br>
    Password: <input type="password" name="password"><br>
    <input type="submit" value="Submit">
</form>

```

Handle Login Post Request

```
static esp_err_t login_post_handler(httpd_req_t *req) {
}
```

### pixeldoc2000 on 2024-06-22

I suggest "secure" the Web interface with basic auth would be a great start.

I would take basic auth for web interface any day to avoid having anybody messing with the settings via the web interface or see my wallet address / settings.

If the web interface has basic auth, chances are they will not check if the API requires auth too. If they poke at the API, changes are you are already lost ;-)

This will probably "enough basic security" for most users.

### skot on 2024-06-23

My concern is that is adds a lot of additional complexity for new users without any actual security.

I think if we do it, it will need to be optional, and off by default.

### ffrediani on 2024-07-29

Hi folks, let's do the simple first: secure with basic web auth is enough instead of not having anything. A password field in the Settings should do the job when filled.

Having to create a separate subnet just for one or few Bitaxes is too much for little benefit.
A basic web auth will not make the AxeOS bloated.

I guess if one has several Bitaxes, want HTTPs/Let's Encrypt or wishes to have external access can do a reverse proxy in front of the devices.

Obs: whatever the code is, don't forget to make it listen on IPv6 address as well.

### ghost on 2024-08-10

Any updates on this?

https://github.com/skot/ESP-Miner/issues/89#issuecomment-2101821332

### skot on 2024-10-10

We are not planning on AxeOS security for now.

### ffrediani on 2024-10-10

I wouldn't even call this "security" but a simple anti local curious.
