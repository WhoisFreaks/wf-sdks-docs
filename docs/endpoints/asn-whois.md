# ASN WHOIS

Autonomous System Number WHOIS

1 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## ASN WHOIS Lookup

`GET /v2.0/asn-whois`

WHOIS for an ASN. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `asn` | query | yes | string |  |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.asnwhois_api import ASNWHOISApi

# Parameters for asnWhois (GET /v2.0/asn-whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - asn (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = ASNWHOISApi(ApiClient(config))

resp = api.asn_whois_with_http_info(api_key="YOUR_API_KEY", asn="AS15169")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, ASNWHOISApi } from "whoisfreaks";

const api = new ASNWHOISApi(new Configuration());

async function main() {
  const resp = await api.asnWhoisRaw({ apiKey: "YOUR_API_KEY", asn: "AS15169", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
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
    // apiKey is a builder method on the request, not a config/context value
    result, httpRes, err := client.ASNWHOISAPI.AsnWhois(context.Background()).ApiKey("YOUR_API_KEY").Asn("AS15169").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
