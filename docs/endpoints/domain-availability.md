# Domain Availability

Check domain availability

2 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Domain Availability Check with Suggestions

`GET /v2.0/domain/availability`

Check availability of a single domain and optionally get suggestions across multiple TLDs. 1 credit per domain checked. sug=false checks only the queried domain; sug=true returns up to `count` (max 100) TLD suggestions.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `domain` | query | yes | string | The domain name to check |
| `sug` | query | no | boolean | Whether to return TLD suggestions alongside the queried domain. |
| `count` | query | no | integer | Number of TLD suggestions to return when sug=true. Maximum is 100. |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_availability_api import DomainAvailabilityApi

# Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, required): The domain name to check
#   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
#   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DomainAvailabilityApi(ApiClient(config))

resp = api.domain_availability_v2_with_http_info(api_key="YOUR_API_KEY", domain="example.com")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
import { Configuration, DomainAvailabilityApi } from "whoisfreaks";

const api = new DomainAvailabilityApi(new Configuration());

async function main() {
  const resp = await api.domainAvailabilityV2Raw({ apiKey: "YOUR_API_KEY", domain: "example.com", sug: undefined, count: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Domain Availability Check with Suggestions (GET /v2.0/domain/availability)
// Parameters for domainAvailabilityV2 (GET /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required): The domain name to check
//   - sug (boolean, optional): Whether to return TLD suggestions alongside the queried domain.
//   - count (integer, optional): Number of TLD suggestions to return when sug=true. Maximum is 100.
//   - format (string (one of: json, xml), optional)
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
    result, httpRes, err := client.DomainAvailabilityAPI.DomainAvailabilityV2(context.Background()).ApiKey("YOUR_API_KEY").Domain("example.com").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Bulk Domain Availability Check

`POST /v2.0/domain/availability`

Two bulk modes. Mode 1: POST domainNames array. Mode 2: POST tld array plus domain query param. Max 100 domains per request. 1 credit per domain checked.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `domain` | query | no | string | Required for TLD-mode bulk check (base domain). |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_availability_api import DomainAvailabilityApi
from whoisfreaks.models.bulk_domain_availability_request import BulkDomainAvailabilityRequest

# Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, optional): Required for TLD-mode bulk check (base domain).
#   - format (string (one of: json, xml), optional)
#   - body: BulkDomainAvailabilityRequest (required) -- request body object
config = Configuration()
api = DomainAvailabilityApi(ApiClient(config))

bulk_domain_availability_request = BulkDomainAvailabilityRequest()  # populate fields as needed
resp = api.bulk_domain_availability_v2_with_http_info(api_key="YOUR_API_KEY", bulk_domain_availability_request=bulk_domain_availability_request)
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
import { Configuration, DomainAvailabilityApi } from "whoisfreaks";

const api = new DomainAvailabilityApi(new Configuration());

async function main() {
  const resp = await api.bulkDomainAvailabilityV2Raw({ apiKey: "YOUR_API_KEY", bulkDomainAvailabilityRequest: {}, domain: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
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
    result, httpRes, err := client.DomainAvailabilityAPI.BulkDomainAvailabilityV2(context.Background()).ApiKey("YOUR_API_KEY").BulkDomainAvailabilityRequest(*wf.NewBulkDomainAvailabilityRequest()).Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
