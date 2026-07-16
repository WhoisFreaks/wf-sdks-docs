# Subdomains

*Section: API Solutions*

Subdomain enumeration

1 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Subdomains Lookup

`GET /v1.0/subdomains`

All subdomains including nested. 2 credits per query.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `domain` | query | yes | string |  |
| `after` | query | no | string |  |
| `before` | query | no | string |  |
| `status` | query | no | string |  (one of: active, inactive) |
| `page` | query | no | integer |  |
| `format` | query | no | string |  (one of: json, xml) |

**Response** (`SubdomainsResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `domain` | string |  |
| `status` | boolean |  |
| `current_page` | integer |  |
| `total_pages` | integer |  |
| `query_time` | string |  |
| `total_records` | integer |  |
| `subdomains` | array<Subdomain> |  |

<details><summary><code>Subdomain</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `subdomain` | string |  |
| `first_seen` | string |  |
| `last_seen` | string |  |
| `inactive_from` | string |  |
| `dns_records` | DnsResponse |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Subdomains Lookup (GET /v1.0/subdomains)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.subdomains_api import SubdomainsApi

# Parameters for subdomains (GET /v1.0/subdomains):
#   - domain (string, required)
#   - after (string, optional)
#   - before (string, optional)
#   - status (string (one of: active, inactive), optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = SubdomainsApi(ApiClient(config))

result = api.subdomains(domain="example.com", after="2000-01-01", before=str(date.today()))
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, SubdomainsApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new SubdomainsApi(config);

async function main() {
  const result = await api.subdomains({ domain: "example.com", after: "2000-01-01", before: new Date().toISOString().slice(0,10), status: undefined, page: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "time"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    result, _, err := client.SubdomainsAPI.Subdomains(ctx).Domain("example.com").After("2000-01-01").Before(time.Now().Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
