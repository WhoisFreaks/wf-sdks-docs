# Databases - ASN WHOIS

ASN WHOIS database snapshots

2 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## ASN WHOIS Snapshot

`GET /v3.3/download/snapshot/asn/whois`

ASN WHOIS Snapshot. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
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
#   - date (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesASNWHOISApi(ApiClient(config))

data = api.db_asn_whois(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbAsnWhois.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbAsnWhois.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
import { Configuration, DatabasesASNWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesASNWHOISApi(config);

async function main() {
  const result = await api.dbAsnWhois({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
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
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    // returns raw bytes (compressed/binary file) -- write to disk
    data, _, err := client.DatabasesASNWHOISAPI.DbAsnWhois(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
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

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_asnwhois_api import DatabasesASNWHOISApi

# Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesASNWHOISApi(ApiClient(config))

result = api.db_asn_whois_status()
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesASNWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesASNWHOISApi(config);

async function main() {
  const result = await api.dbAsnWhoisStatus({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
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
    result, _, err := client.DatabasesASNWHOISAPI.DbAsnWhoisStatus(ctx).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
