# IP Reputation

*Section: API Solutions*

IP threat intelligence

2 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## IP Reputation Lookup

`GET /v1.0/security`

Threat intel for IP — VPN, proxy, Tor, bots. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `ip` | query | yes | string |  |

**Response** (`IpReputationResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `ip` | string |  |
| `location` | IpLocation |  |
| `network` | IpSecurityNetwork |  |
| `asn` | IpSecurityAsn |  |
| `security` | IpSecurity |  |

<details><summary><code>IpLocation</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `continent_code` | string |  |
| `continent_name` | string |  |
| `country_code2` | string |  |
| `country_code3` | string |  |
| `country_name` | string |  |
| `country_name_official` | string |  |
| `country_capital` | string |  |
| `state_prov` | string |  |
| `state_code` | string |  |
| `district` | string |  |
| `city` | string |  |
| `locality` | string |  |
| `accuracy_radius` | string |  |
| `confidence` | string |  |
| `zipcode` | string |  |
| `latitude` | string |  |
| `longitude` | string |  |
| `is_eu` | boolean |  |
| `geoname_id` | string |  |
| `country_emoji` | string |  |

</details>

<details><summary><code>IpSecurityNetwork</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `connection_type` | string |  |
| `route` | string |  |
| `is_anycast` | boolean |  |

</details>

<details><summary><code>IpSecurityAsn</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `as_number` | string |  |
| `organization` | string |  |
| `country` | string |  |
| `type` | string |  |
| `domain` | string |  |
| `date_allocated` | string |  |
| `rir` | string |  |

</details>

<details><summary><code>IpSecurity</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `threat_score` | integer |  |
| `is_tor` | boolean |  |
| `is_proxy` | boolean |  |
| `proxy_provider_names` | array<string> |  |
| `proxy_confidence_score` | integer |  |
| `proxy_last_seen` | string |  |
| `is_residential_proxy` | boolean |  |
| `is_vpn` | boolean |  |
| `vpn_provider_names` | array<string> |  |
| `vpn_confidence_score` | integer |  |
| `vpn_last_seen` | string |  |
| `is_relay` | boolean |  |
| `relay_provider_name` | string |  |
| `is_anonymous` | boolean |  |
| `is_known_attacker` | boolean |  |
| `is_bot` | boolean |  |
| `is_spam` | boolean |  |
| `is_cloud_provider` | boolean |  |
| `cloud_provider_name` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP Reputation Lookup (GET /v1.0/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ip_reputation_api import IPReputationApi

# Parameters for ipReputation (GET /v1.0/security):
#   - ip (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = IPReputationApi(ApiClient(config))

result = api.ip_reputation(ip="8.8.8.8")
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
import { Configuration, IPReputationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new IPReputationApi(config);

async function main() {
  const result = await api.ipReputation({ ip: "8.8.8.8" });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
package main

import (
    "context"
    "encoding/json"
    "fmt"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    result, _, err := client.IPReputationAPI.IpReputation(ctx).Ip("8.8.8.8").Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Bulk IP Reputation

`POST /v1.0/security`

Up to 100 IPs.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Response** (`IpReputationResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `ip` | string |  |
| `location` | IpLocation |  |
| `network` | IpSecurityNetwork |  |
| `asn` | IpSecurityAsn |  |
| `security` | IpSecurity |  |

<details><summary><code>IpLocation</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `continent_code` | string |  |
| `continent_name` | string |  |
| `country_code2` | string |  |
| `country_code3` | string |  |
| `country_name` | string |  |
| `country_name_official` | string |  |
| `country_capital` | string |  |
| `state_prov` | string |  |
| `state_code` | string |  |
| `district` | string |  |
| `city` | string |  |
| `locality` | string |  |
| `accuracy_radius` | string |  |
| `confidence` | string |  |
| `zipcode` | string |  |
| `latitude` | string |  |
| `longitude` | string |  |
| `is_eu` | boolean |  |
| `geoname_id` | string |  |
| `country_emoji` | string |  |

</details>

<details><summary><code>IpSecurityNetwork</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `connection_type` | string |  |
| `route` | string |  |
| `is_anycast` | boolean |  |

</details>

<details><summary><code>IpSecurityAsn</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `as_number` | string |  |
| `organization` | string |  |
| `country` | string |  |
| `type` | string |  |
| `domain` | string |  |
| `date_allocated` | string |  |
| `rir` | string |  |

</details>

<details><summary><code>IpSecurity</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `threat_score` | integer |  |
| `is_tor` | boolean |  |
| `is_proxy` | boolean |  |
| `proxy_provider_names` | array<string> |  |
| `proxy_confidence_score` | integer |  |
| `proxy_last_seen` | string |  |
| `is_residential_proxy` | boolean |  |
| `is_vpn` | boolean |  |
| `vpn_provider_names` | array<string> |  |
| `vpn_confidence_score` | integer |  |
| `vpn_last_seen` | string |  |
| `is_relay` | boolean |  |
| `relay_provider_name` | string |  |
| `is_anonymous` | boolean |  |
| `is_known_attacker` | boolean |  |
| `is_bot` | boolean |  |
| `is_spam` | boolean |  |
| `is_cloud_provider` | boolean |  |
| `cloud_provider_name` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Bulk IP Reputation (POST /v1.0/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ip_reputation_api import IPReputationApi
from whoisfreaks.models.bulk_ip_reputation_request import BulkIpReputationRequest

# Parameters for bulkIpReputation (POST /v1.0/security):
#   - body: BulkIpReputationRequest (required) -- request body object
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = IPReputationApi(ApiClient(config))

bulk_ip_reputation_request = BulkIpReputationRequest()  # populate fields as needed
result = api.bulk_ip_reputation(bulk_ip_reputation_request=bulk_ip_reputation_request)
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
import { Configuration, IPReputationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new IPReputationApi(config);

async function main() {
  const result = await api.bulkIpReputation({ bulkIpReputationRequest: {} });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - body: BulkIpReputationRequest (required) -- request body object
package main

import (
    "context"
    "encoding/json"
    "fmt"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    result, _, err := client.IPReputationAPI.BulkIpReputation(ctx).BulkIpReputationRequest(*wf.NewBulkIpReputationRequest()).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
