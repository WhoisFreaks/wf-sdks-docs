# IP Reputation

IP threat intelligence

2 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## IP Reputation Lookup

`GET /v1.0/security`

Threat intel for IP — VPN, proxy, Tor, bots. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `ip` | query | yes | string |  |

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
