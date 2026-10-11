# Quick Guide: Foreman API

> Registry ID: foreman-api
> Source: https://support.foreman.mn/hc/en-us/articles/48780631909531-Quick-Guide-Foreman-API (retrieved via Zendesk Help Center JSON API: /api/v2/help_center/en-us/articles/48780631909531.json)
> Collected: 2026-10-10
> Published: created 2026-04-06; updated 2026-08-07 (article metadata)
> Posture: verbatim
> As-Of: 2026-10-10

Capture notes: article HTML body converted to text verbatim. KB HTML pages are Cloudflare-gated (403) but the Zendesk JSON API is open.

The Foreman API gives developers and operators programmatic access to Foreman's mine management platform. Use it to build custom integrations, automate workflows, pull miner metrics into your own dashboards, or trigger actions from external systems.

For the full interactive reference, including every endpoint, request/response schemas, and a live "Try it out" feature, visit our API docs on SwaggerHub: [https://app.swaggerhub.com/apis-docs/foremanmining/foreman-api/2.0.0#/](→ View the Foreman API Reference on SwaggerHub)

## Base URL

All requests are made to:
https://api.foreman.mn/api/v2/
All requests must be made over HTTPS. Plain HTTP is not supported.

## Authentication

The API uses API key authentication. Include your key in the Authorization header of every request:
Authorization: Token YOUR_API_KEY
Content-Type: application/json
Where to find your API key: Log in to the Foreman dashboard, and navigate to the Man with a Tie icon in the top-right corner. Select My Account from the drop-down menu, then scroll down to the API Information section. Treat your API key like a password — never commit it to source control or share it publicly.

## What you can do with the API

The API is organized into resource groups covering the core areas of mine management:

 | Resource group
 | What you can do

 | Miners
 | List, add, update, delete, and reboot miners. Retrieve real-time metrics including hashrate, temperature, fan speed, and power consumption.

 | Pickaxes
 | Manage Pickaxe agents — the local agents that communicate between your miners and Foreman. Register agents and check connection status.

 | Alerts
 | Configure alert thresholds for hashrate drops, high temperatures, and offline equipment. Retrieve active alerts and alert history.

 | Pools
 | Manage mining pool configurations. Add, update, or switch pools for individual miners or groups programmatically.

 | Farms & groups
 | Organize miners into farms or groups. Perform bulk operations — such as rebooting all miners at a site or switching pools for an entire farm.

 | Power controls
 | Retrieve power consumption data and trigger power management actions on supported hardware.

 | Events & audit logs
 | Pull operational event history for audit, reporting, or integration with external monitoring tools.

## Making requests

## HTTP methods

The API follows standard REST conventions:

- 
GET — Retrieve a resource or list of resources

- 
POST — Create a new resource

- 
PUT / PATCH — Update an existing resource

- 
DELETE — Remove a resource

## Example request

Retrieve all miners in your account:
curl -X GET \
 "https://api.foreman.mn/api/v2/miners" \
 -H "Authorization: Token YOUR_API_KEY" \
 -H "Content-Type: application/json"

## Response format

All responses are returned as JSON. Successful responses contain the requested data; error responses include a message field describing what went wrong.

 | Status code
 | Meaning

 | 200 OK
 | Request succeeded.

 | 201 Created
 | A new resource was successfully created.

 | 204 No Content
 | Request succeeded with no response body (e.g. a DELETE).

 | 400 Bad Request
 | The request was malformed or missing required parameters.

 | 401 Unauthorized
 | Missing or invalid API key.

 | 403 Forbidden
 | Your API key does not have permission to perform this action.

 | 404 Not Found
 | The requested resource does not exist.

 | 429 Too Many Requests
 | You've exceeded the rate limit. Implement exponential backoff and retry.

 | 500 Server Error
 | An unexpected error on the Foreman side. Contact support if this persists.

## Rate limits & pagination

The API enforces rate limits to maintain platform stability. If you hit the limit, you'll receive a 429 response — implement exponential backoff in your client to handle this gracefully.

Endpoints that return lists support pagination via query parameters:

- 
page — Page number to return (default: 1)

- 
per_page — Results per page (default: 25, max: 100)

Tip: For high-volume use cases like polling miner metrics, cache responses locally and fetch on a reasonable interval rather than querying on every page load.

## Staying Up to Date

The API is actively maintained and updated. All changes are documented in the [https://support.foreman.mn/hc/en-us/categories/33246666532507-Release-Notes](Foreman Release Notes). To find API-specific updates, search for API within the Release Notes — this will surface all recent additions, changes, and deprecations.

Checking the Release Notes regularly is the best way to catch new endpoints, parameter changes, or anything that might affect existing integrations.

## Tips for Getting the Most Out of the API

- 
Start with SwaggerHub. Before writing any code, use the interactive docs to understand exactly what each endpoint returns. It saves time and reduces trial-and-error.

- 
Build retry logic with backoff. Even with careful rate limiting, network issues happen. A simple retry with a 1–2 second delay handles most transient failures gracefully.

- 
Use a dedicated test client. Keeping a small test environment separate from production makes it safe to experiment with write operations, such as configuration changes or miner management.

- 
Watch the Release Notes. Set a reminder to check for API updates periodically, especially before deploying new integrations, to avoid surprises from changed behavior.

- 
Scope your API calls. Only request the data you need. Targeted, specific calls are faster, easier to debug, and less likely to run into rate limits than broad queries.

## Need help?

If you run into issues with the API, our support team is here to help! When contacting support, include your endpoint, request payload, and the response received.
