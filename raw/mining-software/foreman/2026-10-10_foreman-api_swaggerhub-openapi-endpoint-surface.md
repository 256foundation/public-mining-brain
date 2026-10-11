# Foreman API 2.0.0 — OpenAPI endpoint surface (SwaggerHub)

> Registry ID: foreman-api
> Source: https://app.swaggerhub.com/apis-docs/foremanmining/foreman-api/2.0.0 (machine spec: https://api.swaggerhub.com/apis/foremanmining/foreman-api/2.0.0/swagger.json)
> Collected: 2026-10-10
> Published: n/d (spec version 2.0.0)
> Posture: verbatim
> As-Of: 2026-10-10

Capture notes: fetched from SwaggerHub machine endpoint https://api.swaggerhub.com/apis/foremanmining/foreman-api/2.0.0/swagger.json (HTTP 200, 19,151 bytes). Spec title: "Foreman API", version 2.0.0. The interactive UI at app.swaggerhub.com is a JS app; this file captures the OpenAPI document verbatim (full path list below, plus selected endpoint definitions and schemas). 92 paths total.

## Full endpoint list (verbatim summaries from spec)

- `POST /actions/blink/{minerId}` — Blink the miner's LEDs.
- `POST /actions/change-password/{minerId}` — Change the miner password.
- `POST /actions/change-pools/bulk/{clientId}` — Bulk change mining pools for multiple miners.
- `POST /actions/change-pools/{minerId}` — Changes mining pools.
- `POST /actions/fetch-miner-logs/{minerId}` — Initiates the fetch of a miner log.
- `POST /actions/network/{minerId}` — Apply a static IP configuration.
- `POST /actions/power-mode/{minerId}` — Change the power mode.
- `POST /actions/reboot/{minerId}` — Reboots the miner.
- `GET /actions/status/{commandId}` — Obtains the status of a command.
- `POST /actions/vnish-overclock/{minerId}` — Endpoint to overclock vnish firmware.
- `POST /assets` — Create or Update an Asset
- `GET /assets/types/{clientId}` — Obtain all Asset Types for a Client
- `GET /assets/{clientId}` — Obtain Assets from a specific Client
- `POST /assets/{clientId}/delete` — Delete the provided Asset
- `GET /broker/{broker}/dispatches/{clientId}` — Returns all of the dispatches for the provided client ID.
- `POST /broker/{broker}/dispatches/{clientId}` — Creates or updates the provided dispatch.
- `GET /broker/{broker}/dispatches/{clientId}/{eventId}` — Returns the dispatch for the provided dispatch ID.
- `POST /broker/{broker}/dispatches/{clientId}/{eventId}/cancel` — Cancels the provided dispatch.
- `GET /clients` — Returns all of the clients that the authenticated user can access.
- `POST /clients` — Creates a new client with the desired configuration.
- `POST /clients/{clientId}` — Updates the information regarding the provided client ID.
- `GET /clients/{clientId}` — Returns full information regarding the provided client ID.
- `DELETE /clients/{clientId}` — Deletes a client based on the provided client ID.
- `GET /clients/{clientId}/group` — Returns information regarding the group that the client is in, if any.
- `GET /clients/{clientId}/logs` — Returns all of the logs associated with the provided client ID.
- `GET /clients/{clientId}/logs/{minerId}` — Returns all of the logs associated with the provided client ID and miner ID.
- `GET /clients/{clientId}/miners` — Returns all of the miner IDs for the provided client ID and filtered search criteria.
- `POST /clients/{clientId}/miners` — Creates miners.
- `POST /clients/{clientId}/miners/bulk/move` — Bulk moves miners to a new client, and optionally, a new Pickaxes.
- `GET /clients/{clientId}/miners/group-summary` — Returns group summary information for all of the miners.
- `GET /clients/{clientId}/miners/summary` — Returns summary information for all of the miners.
- `GET /clients/{clientId}/miners/{minerId}` — Returns all of the information regarding the provided miner ID.
- `DELETE /clients/{clientId}/miners/{minerId}` — Deletes the provided miner.
- `POST /clients/{clientId}/miners/{minerId}/disable` — Label a miner as disabled
- `POST /clients/{clientId}/miners/{minerId}/enable` — Label a miner as enabled
- `POST /clients/{clientId}/miners/{minerId}/move` — Moves a miner to a new client, and optionally, a new Pickaxe.
- `GET /clients/{clientId}/pickaxes` — Returns all of the Pickaxes associated with the provided client ID.
- `GET /clients/{clientId}/pickaxes/{pickaxeId}` — Returns all of the Pickaxes associated with the provided client ID.
- `GET /cpower/keys` — Returns all of the CPower keys that the provided user can access.
- `GET /cpower/keys/{clientId}` — Returns all of the CPower keys for the provided client.
- `GET /csd/keys` — Returns all of the CSD keys that the provided user can access.
- `GET /csd/keys/{clientId}` — Returns all of the CSD keys for the provided client.
- `GET /csp/{csp}/dispatches/{clientId}` — Returns all of the dispatches for the provided client ID.
- `POST /csp/{csp}/dispatches/{clientId}` — Creates or updates the provided dispatch.
- `GET /csp/{csp}/dispatches/{clientId}/{eventId}` — Returns the dispatch for the provided dispatch ID.
- `POST /csp/{csp}/dispatches/{clientId}/{eventId}/cancel` — Cancels the provided dispatch.
- `POST /curtailment/plans/{planId}` — Edits an existing curtailment plan.
- `DELETE /curtailment/plans/{planId}` — Deletes an existing curtailment plan.
- `POST /curtailment/plans/{planId}/run` — Runs an existing curtailment plan.
- `GET /curtailment/runs/{runId}` — Returns info regarding the provided curtailment run.
- `POST /curtailment/runs/{runId}/cancel` — Cancels the provided run.
- `POST /curtailment/runs/{runId}/revert` — Reverses the provided run id.
- `POST /curtailment/{clientId}/once` — Creates a single-fire curtailment.
- `GET /curtailment/{clientId}/plans` — Returns all of the curtailment plans for the provided client.
- `POST /curtailment/{clientId}/plans` — Creates a new curtailment plan.
- `GET /curtailment/{clientId}/runs` — Returns all curtailment runs for a client
- `GET /custom-field/{clientId}` — Get all miners and custom field information
- `GET /custom-field/{clientId}/{customField}` — Get specific custom field information for all miners
- `GET /custom-field/{clientId}/{minerId}` — Get all of a single miners custom field information
- `GET /custom-field/{clientId}/{minerId}/{customField}` — Get specific custom field information for a specific miners
- `POST /custom-field/{clientId}/{minerId}/{customField}` — Adds a custom field value to a specific miner
- `GET /dispatches/{clientId}` — List dispatches for the client. This is a paid feature disabled by default.
- `POST /dispatches/{clientId}` — Create a dispatch for the client. This is a paid feature disabled by default.
- `GET /dispatches/{clientId}/current` — List current dispatches for the client.
- `GET /dispatches/{clientId}/{eventId}` — List dispatches for the client. This is a paid feature disabled by default.
- `POST /dispatches/{clientId}/{eventId}` — Create or edit a dispatch for the client. This is a paid feature disabled by default.
- `POST /dispatches/{clientId}/{eventId}/cancel` — Cancel dispatches for the given client and event ID. This is a paid feature disabled by default.
- `GET /fiat` — Returns all of the fiat conversion rates.
- `GET /fiat/{symbol}` — Returns the conversion info for the provided currency.
- `GET /firmware/{clientId}/manufacturers` — Returns all of the firmware manufacturers available to the client.
- `GET /firmware/{clientId}/manufacturers/${manufacturerId}` — Returns all of the firmware manufacturers available to the client.
- `GET /firmware/{clientId}/manufacturers/${manufacturerId}/versions` — Returns all of the manufacturer versions available to the client.
- `GET /hive/keys` — Returns all HiveOS farm IDs and authentication token pairs that the user can access.
- `GET /hive/keys/{clientId}` — Returns HiveOS farm IDs and authentication token pairs for a specific client.
- `GET /hive/mappings` — Returns all of the HiveOS to executable mappings.
- `GET /hive/mappings/{hiveExecutable}` — Returns the mapping for the provided HiveOS executable.
- `POST /inventory` — Create or Update an Inventory
- `GET /inventory/types/{clientId}` — Obtain all Inventory Types for a Client
- `GET /inventory/{clientId}` — Obtain Inventory from a specific Client
- `POST /inventory/{clientId}/delete` — Delete the provided Inventory
- `GET /logs/{logId}` — Returns an existing log.
- `DELETE /logs/{logId}` — Deletes an existing log.
- `GET /ping` — Verifies connectivity. Not authenticated.
- `GET /ping/{clientId}` — Verifies connectivity. Authenticated.
- `GET /pool-keys` — Returns all of the pool keys available to the user.
- `GET /pool-keys/{clientId}` — Returns all of the pool keys available to the user for the provided client.
- `POST /qse/prioritypower/rtac/{pickaxeKey}/state` — Updates the stats associated with the current RTAC state.
- `GET /reports/results` — Obtains report results.
- `POST /reports/{clientId}/create` — Runs a report.
- `POST /site-map/location/{minerId}` — Sets the site map location of a miner.
- `GET /site-map/{clientId}/groups` — Returns all of groups within a Site Map.
- `GET /site-map/{clientId}/groups/{groupId}` — Returns the Site Map group.
- `GET /site-map/{clientId}/racks` — Returns all of racks within a Site Map.
- `GET /site-map/{clientId}/racks/{rackId}` — Returns the Site Map rack.
- `GET /system/asics` — Returns all of the currently supported ASICs.
- `GET /system/asics/{systemId}` — Returns the desired ASIC system.
- `GET /system/rigs` — Returns all of the currently supported GPU miners.
- `GET /system/rigs/{systemId}` — Returns the desired rig system.
- `GET /tags/{clientId}` — Returns all of the currently existing tags on the provided client.
- `GET /tags/{clientId}/{tagId}` — Return the desired tag.
- `GET /tickets` — Obtain all tickets from clients user has access to.
- `GET /tickets/{clientId}` — Obtain tickets from a specific client a user has access to.
- `POST /tickets/{clientId}` — Create a ticket for a specific client a user has access to.
- `POST /tickets/{clientId}/delete` — Delete a ticket from a specific client.
- `GET /voltus/keys` — Returns all of the Voltus keys that the provided user can access.
- `GET /voltus/keys/{clientId}` — Returns all of the Voltus keys for the provided client.

## Selected endpoint definitions (verbatim JSON from spec)

### `/actions/power-mode/{minerId}`

```json
{
 "post": {
  "summary": "Change the power mode.",
  "description": "Changes the power mode of a miner.  Currently only ASIC support.\n\nNote: some modes may only be available to certain miner models and manufacturers.\n",
  "tags": [
   "actions"
  ],
  "requestBody": {
   "required": true,
   "content": {
    "application/json": {
     "schema": {
      "$ref": "#/components/schemas/powerMode"
     }
    }
   }
  },
  "parameters": [
   {
    "$ref": "#/components/parameters/minerIdPath"
   }
  ],
  "responses": {
   "200": {
    "description": "OK",
    "content": {
     "application/json": {
      "schema": {
       "$ref": "#/components/schemas/commandAccepted"
      }
     }
    }
   },
   "400": {
    "description": "Request was malformed."
   },
   "401": {
    "description": "No credentials provided."
   },
   "403": {
    "description": "User doesn't have access to this miner or isn't allowed to run this command."
   },
   "404": {
    "description": "Miner doesn't exist."
   }
  }
 }
}
```

### `/actions/reboot/{minerId}`

```json
{
 "post": {
  "summary": "Reboots the miner.",
  "tags": [
   "actions"
  ],
  "parameters": [
   {
    "$ref": "#/components/parameters/minerIdPath"
   }
  ],
  "description": "Changes the miner. Currently only ASIC support.",
  "responses": {
   "200": {
    "description": "OK",
    "content": {
     "application/json": {
      "schema": {
       "$ref": "#/components/schemas/commandAccepted"
      }
     }
    }
   },
   "400": {
    "description": "Request was malformed."
   },
   "401": {
    "description": "No credentials provided."
   },
   "403": {
    "description": "User doesn't have access to this miner or isn't allowed to run this command."
   },
   "404": {
    "description": "Miner doesn't exist."
   }
  }
 }
}
```

### `/actions/change-pools/{minerId}`

```json
{
 "post": {
  "summary": "Changes mining pools.",
  "tags": [
   "actions"
  ],
  "requestBody": {
   "required": true,
   "content": {
    "application/json": {
     "schema": {
      "$ref": "#/components/schemas/changePools"
     }
    }
   }
  },
  "parameters": [
   {
    "$ref": "#/components/parameters/minerIdPath"
   }
  ],
  "description": "Changes the pools of a miner. Currently only ASIC support.",
  "responses": {
   "200": {
    "description": "OK",
    "content": {
     "application/json": {
      "schema": {
       "$ref": "#/components/schemas/commandAccepted"
      }
     }
    }
   },
   "401": {
    "description": "No credentials provided."
   },
   "403": {
    "description": "User doesn't have access to this miner or isn't allowed to run this command."
   },
   "404": {
    "description": "Miner not found or bad request."
   }
  }
 }
}
```

### `/actions/change-pools/bulk/{clientId}`

```json
{
 "post": {
  "summary": "Bulk change mining pools for multiple miners.",
  "tags": [
   "actions"
  ],
  "requestBody": {
   "required": true,
   "content": {
    "application/json": {
     "schema": {
      "$ref": "#/components/schemas/bulkChangePools"
     }
    }
   }
  },
  "parameters": [
   {
    "$ref": "#/components/parameters/clientIdPath"
   }
  ],
  "description": "Apply pool changes to specific miners. The request body is an array of pool-change items; each item includes a `miners` array (individual miner IDs) and the `pools` configuration to apply to those miners. Use multiple items when different miners need different pool settings in the same request.",
  "responses": {
   "200": {
    "description": "OK",
    "content": {
     "application/json": {
      "schema": {
       "$ref": "#/components/schemas/bulkCommandAccepted"
      }
     }
    }
   },
   "400": {
    "description": "Client not found or provided"
   },
   "401": {
    "description": "No credentials provided."
   }
  }
 }
}
```

### `/curtailment/{clientId}/once`

```json
{
 "post": {
  "summary": "Creates a single-fire curtailment.",
  "tags": [
   "curtailment"
  ],
  "requestBody": {
   "required": true,
   "content": {
    "application/json": {
     "schema": {
      "$ref": "#/components/schemas/curtailmentScheduledPlan"
     },
     "examples": {
      "withoutFiltering": {
       "$ref": "#/components/examples/withoutFiltering"
      },
      "withoutFilteringPhaseBalanced": {
       "$ref": "#/components/examples/withoutFilteringPhaseBalanced"
      },
      "filterByPickaxe": {
       "$ref": "#/components/examples/filterByPickaxe"
      },
      "filterByIpRange": {
       "$ref": "#/components/examples/filterByIpRange"
      },
      "filterByTags": {
       "$ref": "#/components/examples/filterByTags"
      }
     }
    }
   }
  },
  "parameters": [
   {
    "$ref": "#/components/parameters/clientIdPath"
   }
  ],
  "description": "Creates a single-fire curtailment.  This is intended to be the mechanism to connect the system to a utility signal.",
  "responses": {
   "200": {
    "description": "OK",
    "content": {
     "application/json": {
      "schema": {
       "$ref": "#/components/schemas/curtailmentScheduled"
      }
     }
    }
   },
   "403": {
    "description": "User doesn't have access to this client or the user doesn't have permission to run instant curtailments."
   },
   "404": {
    "description": "Client doesn't exist."
   }
  }
 }
}
```


## Schema: powerMode (verbatim)

```json
{
 "type": "object",
 "properties": {
  "powerMode": {
   "type": "string",
   "enum": [
    "sleeping",
    "normal",
    "low",
    "high"
   ]
  }
 }
}
```

## Schema: changePools (verbatim)

```json
{
 "type": "object",
 "properties": {
  "pools": {
   "type": "array",
   "items": {
    "type": "object",
    "properties": {
     "url": {
      "type": "string",
      "description": "The stratum URL (without the prefix).",
      "example": "btc.foundryusapool.com:3333"
     },
     "user": {
      "type": "string",
      "description": "The workername.",
      "example": "obminc.worker1"
     },
     "pass": {
      "type": "string",
      "description": "The password.",
      "example": "x"
     }
    }
   }
  },
  "algo": {
   "type": "string",
   "example": null
  }
 }
}
```

