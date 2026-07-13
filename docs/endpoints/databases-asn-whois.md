# Databases - ASN WHOIS

ASN WHOIS database snapshots

2 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

ASN WHOIS Snapshot. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `date` | query | yes | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_asnwhois_api import DatabasesASNWHOISApi

# Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesASNWHOISApi(ApiClient(config))

data = api.db_asn_whois(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbAsnWhois.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbAsnWhois.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import { Configuration, DatabasesASNWHOISApi } from "whoisfreaks";

const api = new DatabasesASNWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbAsnWhoisRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
package main

import (
    "context"
    "fmt"
    "os"
    "time"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    // returns raw bytes (compressed/binary file) -- write to disk
    data, _, err := client.DatabasesASNWHOISAPI.DbAsnWhois(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbAsnWhois.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbAsnWhois.gz\n", len(data))
}

```

</details>

---

## ASN WHOIS Snapshot Status

`GET /v3.3/status/snapshot/asn/whois`

ASN WHOIS Snapshot Status. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_asnwhois_api import DatabasesASNWHOISApi

# Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesASNWHOISApi(ApiClient(config))

resp = api.db_asn_whois_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, DatabasesASNWHOISApi } from "whoisfreaks";

const api = new DatabasesASNWHOISApi(new Configuration());

async function main() {
  const resp = await api.dbAsnWhoisStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
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
    result, httpRes, err := client.DatabasesASNWHOISAPI.DbAsnWhoisStatus(context.Background()).ApiKey("YOUR_API_KEY").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
