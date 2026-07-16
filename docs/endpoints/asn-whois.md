# ASN WHOIS

Autonomous System Number WHOIS

1 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## ASN WHOIS Lookup

`GET /v2.0/asn-whois`

WHOIS for an ASN. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `asn` | query | yes | string |  |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.asnwhois_api import ASNWHOISApi

# Parameters for asnWhois (GET /v2.0/asn-whois):
#   - asn (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = ASNWHOISApi(ApiClient(config))

result = api.asn_whois(asn="AS15169")
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, ASNWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new ASNWHOISApi(config);

async function main() {
  const result = await api.asnWhois({ asn: "AS15169", format: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - asn (string, required)
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
    result, _, err := client.ASNWHOISAPI.AsnWhois(ctx).Asn("AS15169").Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
