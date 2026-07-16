# SSL

*Section: API Solutions*

SSL certificate lookup

1 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## SSL Certificate Lookup

`GET /v1.0/ssl/live`

Real-time SSL cert with optional chain.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `domainName` | query | yes | string |  |
| `chain` | query | no | boolean |  |
| `sslRaw` | query | no | boolean |  |
| `format` | query | no | string |  (one of: json, xml) |

**Response** (`SslResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `queryTime` | string |  |
| `sslCertificates` | array<SslCertificate> |  |
| `sslRaw` | string |  |

<details><summary><code>SslCertificate</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `chainOrder` | string |  |
| `authenticationType` | string |  |
| `validityStartDate` | string |  |
| `validityEndDate` | string |  |
| `serialNumber` | string |  |
| `signatureAlgorithm` | string |  |
| `subject` | SslUnitInfo |  |
| `issuer` | SslUnitInfo |  |
| `publicKey` | SslPublicKeyInfo |  |
| `extensions` | SslExtensionsInfo |  |
| `pemRaw` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ssl_api import SSLApi

# Parameters for sslLookup (GET /v1.0/ssl/live):
#   - domainName (string, required)
#   - chain (boolean, optional)
#   - sslRaw (boolean, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = SSLApi(ApiClient(config))

result = api.ssl_lookup(domain_name="example.com")
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, SSLApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new SSLApi(config);

async function main() {
  const result = await api.sslLookup({ domainName: "example.com", chain: undefined, sslRaw: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
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
    result, _, err := client.SSLAPI.SslLookup(ctx).DomainName("example.com").Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
