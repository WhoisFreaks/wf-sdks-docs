# Domain Reputation

Real-time domain threat assessment and trust scoring

1 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Domain Reputation Lookup

`GET /v1/domain/security`

Real-time domain threat assessment. Returns risk verdict, trust score, DGA analysis, threat intelligence matches, and security signals. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `domainName` | query | yes | string | The domain name to assess |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Domain Reputation Lookup (GET /v1/domain/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.domain_reputation_api import DomainReputationApi

# Parameters for domainReputation (GET /v1/domain/security):
#   - domainName (string, required): The domain name to assess
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DomainReputationApi(ApiClient(config))

result = api.domain_reputation(domain_name="example.com")
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
//   - format (string (one of: json, xml), optional)
import { Configuration, DomainReputationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DomainReputationApi(config);

async function main() {
  const result = await api.domainReputation({ domainName: "example.com", format: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Domain Reputation Lookup (GET /v1/domain/security)
// Parameters for domainReputation (GET /v1/domain/security):
//   - domainName (string, required): The domain name to assess
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
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    result, _, err := client.DomainReputationAPI.DomainReputation(ctx).DomainName("example.com").Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
