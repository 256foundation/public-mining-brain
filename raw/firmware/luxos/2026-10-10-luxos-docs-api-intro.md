# LuxOS Docs — LUXminer API Getting Started (TCP/HTTP, port 4028)

> Registry ID: luxos-docs
> Source: https://docs.luxor.tech/firmware/api/intro
> Collected: 2026-10-10
> Published: n/d
> Posture: verbatim
> As-Of: 2026-10-10


## Basics [#basics]

For easier integration with existing tools, LUXminer supports a rich API layer that can be used either for visualization (a custom or alternative dashboard, for example), as well as for scripting (controlling you miner settings remotely).

The API follows the same pattern as the [CGMiner API](https://github.com/ckolivas/cgminer/blob/master/API-README), that is, a raw TCP (**not HTTP**) connection which accepts commands in text or json format, and outputs the result accordingly, closing the connection immediately afterwards. This "strange" behavior might come as a surprise, but this pattern was created at the early days of mining and it stuck on the community.

<Callout emoji="💡">
  Despite supporting both `text` and `json` formats, it is recommended to **always** use JSON, since the format is much less ambiguous and easy to parse in any modern language.

  The format is selected depending on your input; if you send a JSON object, you will receive a JSON response; otherwise it will be parsed as text.
</Callout>

### Command input format [#command-input-format]

All commands are represented by a JSON object with two parameters: `"command"` and `"parameter"`. The `"command"` parameter is, as the name suggests, the command name, and `"parameter"` is *always* a string with comma-separated values, and can be omitted. You can also specify more than one command to be executed on a single request, separating them with `+`, as long as they all are parameterless.

Example of a single, parameterless command:

```json
{ "command": "version" }
```

Example of a command with one parameter:

```json
{ "command": "asc", "parameter": "0" }
```

Example of a command with three parameters. Note that the last parameter is required, but it is blank in this example, so
you still need the comma at the end.

```json
{ "command": "addpool", "parameter": "stratum+tcp://btc.global.luxor.tech:700,account.miner," }
```

Example of multiple commands in a single request. This will only work if all commands are parameterless:

```json
{ "command": "version+summary" }
```

### Command output format [#command-output-format]

All commands use the same pattern for output. Let us take a quick look at it:

```json
{
  "<COMMAND>": [
    // <COMMAND-DATA>
  ],
  "STATUS": [
    {
      "Code": 72,
      "Description": "<DESCRIPTION>",
      "Msg": "<MSG>",
      "STATUS": "S",
      "When": 1672770090
    }
  ],
  "id": 1
}
```

The `<COMMAND>` is normally the name of the command, in upper case. For a given command, it is always the same, and it is always an array with elements in with `<COMMAND-DATA>` shape, **except** in two cases:

1. On the [stats](./cgminer/stats), the first item in the array have a different format, for compatibility reasons.
2. Some commands do not have an output, like [addpool](./cgminer/addpool). In those cases, you will only get the `STATUS` part of the response.

The `STATUS` is always present and contains a `Code` for the response, `Description` and `Msg` fields (which vary depending on the command) and the Unix timestamp of when the command was executed on the `When` field. The most important, however, is the `STATUS` field, which can be either `S` for success or `E` for error, in which case the `Msg` will be used as an error message. Last, the `id` exists for compatibility reasons and is always `1`; it is virtually useless, since every command closes the TCP connection.

<Callout emoji="💡">
  Always use the `STATUS = S` when checking wether a command was successful or not. Do not use the response `Code` for
  that; this field can be changed between LUXminer versions due to compatibility reasons with existing tools.
</Callout>

For multiple commands in a single request, the format is very similar:

```json
// for {"command":"cmd1+cmd2"}
{
  "cmd1": [
    // NORMAL OUTPUT OF 'cmd1'
  ],
  "cmd2": [
    // NORMAL OUTPUT OF 'cmd2'
  ],
  "id": 1
}
```

The "normal output" is everything that the command normally returns, *including* the `STATUS`, and the `id`. This means that is possible to have successful and failed commands in the same response, without one interfering with the other.

<Callout emoji="💡">
  When possible, clump all the commands you need on a single multi-command request. Overall, doing this requires less
  resources and time spent, since everything is done in a single connection.
</Callout>

### Convention used in the examples [#convention-used-in-the-examples]

For practical purposes, the examples in this documentation are all in the following format:

```sh
$ echo '{"command": "version", "parameter":"yJN2nlj1,1,8.9"}' | nc $MINER_IP 4028 | jq
(command output goes here)
```

A quick breakdown:

* `echo` just prints the string, which will be piped (`|`) to the next command.
* `nc` just grabs the output of the previous command and sends it to `$MINER_IP` at the default port. You should either set `$MINER_IP` to the IP of the miner or just replace it altogether.
* `jq` is completely optional; all it does is to nicely format the JSON output, so we can read it easily.

This is a neat convention because it allows to demonstrate the command and is easily copy-pasted for testing purposes, but feel free to adapt it to the available tools in your environment (e.g. `telnet` on Windows).

### Command list [#command-list]

See [Available commands](./available_commands).

## Configuration [#configuration]

The default miner configuration enables the API on port `4028` (the same number as CGMiner). This is defined on the configuration file, `luxminer.toml`:

```toml
# API configuration
#
# This is divided in two parts - the TCP and HTTP configuration.
#
# The TCP configuration has two fields:
# - enabled: Defaults to true; when set to false no API calls will be allowed.
# - port: Defaults to 4028; it is the listening port of the TCP API
#
# The HTTP configuration have:
# - enabled: Defaults to true; when set to false no API calls will be allowed.
# - port: Defaults to 8080; it is the listening port of the HTTP API
#
[app.api.tcp]
enabled = true
port = 4028

[app.api.http]
enabled = true
port = 8080
```

As you can see, this controls in which port the API will listen. To disable the API, set the `enabled` field to false.

## HTTP layer [#http-layer]

If you're paying attention, you might be wondering what is the `app.api.http` configuration key shown in the [Configuration](#configuration) section. This key controls the values to be used by the HTTP layer of the API.

The HTTP layer is a thin RPC-like API to allow for easier integration into the raw TCP API. The API has a single RPC enpoint, `/api` that accepts a JSON body via `POST`. If the body is a valid command (or a multi-command), it will be executed and the results will be returned in the HTTP response.

For example, this will show the miner version:

```bash
curl -X POST -d '{"command":"version"}' -H 'Content-Type: application/json'  http://$MINER_IP:8080/api
```

<Callout emoji="💡">
  When working with LUXminer, always favor the TCP API. It has the same functionality as the HTTP one, but is lighter
  and thus, produces less network traffic.
</Callout>

<Callout type="warning" emoji="⚠️">
  If you disable the HTTP layer, the built-in LUXminer UI won't be able to communicate with the miner.
</Callout>
