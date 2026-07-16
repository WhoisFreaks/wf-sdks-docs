# Geolocation

IP geolocation lookup

2 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## IP Geolocation Lookup

`GET /v1.0/geolocation`

Get location, ASN, currency for an IP. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `ip` | query | yes | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.geolocation_api import GeolocationApi

# Parameters for geolocation (GET /v1.0/geolocation):
#   - ip (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = GeolocationApi(ApiClient(config))

result = api.geolocation(ip="8.8.8.8")
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
import { Configuration, GeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new GeolocationApi(config);

async function main() {
  const result = await api.geolocation({ ip: "8.8.8.8" });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
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
    result, _, err := client.GeolocationAPI.Geolocation(ctx).Ip("8.8.8.8").Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Bulk IP Geolocation

`POST /v1.0/geolocation`

Up to 100 IPs.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.geolocation_api import GeolocationApi
from whoisfreaks.models.bulk_geolocation_request import BulkGeolocationRequest

# Parameters for bulkGeolocation (POST /v1.0/geolocation):
#   - body: BulkGeolocationRequest (required) -- request body object
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = GeolocationApi(ApiClient(config))

bulk_geolocation_request = BulkGeolocationRequest()  # populate fields as needed
result = api.bulk_geolocation(bulk_geolocation_request=bulk_geolocation_request)
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
import { Configuration, GeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new GeolocationApi(config);

async function main() {
  const result = await api.bulkGeolocation({ bulkGeolocationRequest: {} });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
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
    result, _, err := client.GeolocationAPI.BulkGeolocation(ctx).BulkGeolocationRequest(*wf.NewBulkGeolocationRequest()).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
