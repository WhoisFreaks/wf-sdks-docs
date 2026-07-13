# Domain Reputation

Real-time domain threat assessment and trust scoring

1 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Domain Reputation Lookup

`GET /v1/domain/security`

Real-time domain threat assessment. Returns risk verdict, trust score, DGA analysis, threat intelligence matches, and security signals. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `domainName` | query | yes | string | The domain name to assess |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Domain Reputation Lookup (GET /v1/domain/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_reputation_api import DomainReputationApi

# Parameters for domainReputation (GET /v1/domain/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required): The domain name to assess
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DomainReputationApi(ApiClient(config))

resp = api.domain_reputation_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import { Configuration, DomainReputationApi } from "whoisfreaks";

const api = new DomainReputationApi(new Configuration());

async function main() {
  const resp = await api.domainReputationRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
package main

import (
    "context"
    "fmt"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    result, httpRes, err := client.DomainReputationAPI.DomainReputation(ctx).DomainName("example.com").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    fmt.Println(result)
}

```

</details>

---
