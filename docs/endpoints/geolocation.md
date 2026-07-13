# Geolocation

IP geolocation lookup

2 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## IP Geolocation Lookup

`GET /v1.0/geolocation`

Get location, ASN, currency for an IP. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `ip` | query | yes | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.geolocation_api import GeolocationApi

# Parameters for geolocation (GET /v1.0/geolocation):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
config = Configuration()
api = GeolocationApi(ApiClient(config))

resp = api.geolocation_with_http_info(api_key="YOUR_API_KEY", ip="8.8.8.8")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import { Configuration, GeolocationApi } from "whoisfreaks";

const api = new GeolocationApi(new Configuration());

async function main() {
  const resp = await api.geolocationRaw({ apiKey: "YOUR_API_KEY", ip: "8.8.8.8" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
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
    // apiKey is a builder method on the request, not a config/context value
    result, httpRes, err := client.GeolocationAPI.Geolocation(context.Background()).ApiKey("YOUR_API_KEY").Ip("8.8.8.8").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
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
| `apiKey` | query | yes | string | Your WHOISFreaks API key |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.geolocation_api import GeolocationApi
from whoisfreaks.models.bulk_geolocation_request import BulkGeolocationRequest

# Parameters for bulkGeolocation (POST /v1.0/geolocation):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - body: BulkGeolocationRequest (required) -- request body object
config = Configuration()
api = GeolocationApi(ApiClient(config))

bulk_geolocation_request = BulkGeolocationRequest()  # populate fields as needed
resp = api.bulk_geolocation_with_http_info(api_key="YOUR_API_KEY", bulk_geolocation_request=bulk_geolocation_request)
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import { Configuration, GeolocationApi } from "whoisfreaks";

const api = new GeolocationApi(new Configuration());

async function main() {
  const resp = await api.bulkGeolocationRaw({ apiKey: "YOUR_API_KEY", bulkGeolocationRequest: {} });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
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
    // apiKey is a builder method on the request, not a config/context value
    result, httpRes, err := client.GeolocationAPI.BulkGeolocation(context.Background()).ApiKey("YOUR_API_KEY").BulkGeolocationRequest(*wf.NewBulkGeolocationRequest()).Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
