# Databases - IP WHOIS

IP WHOIS database snapshots

2 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## IP WHOIS Snapshot

`GET /v3.3/download/snapshot/ip/whois`

IP WHOIS Snapshot. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | yes | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ipwhois_api import DatabasesIPWHOISApi

# Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
#   - date (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPWHOISApi(ApiClient(config))

data = api.db_ip_whois(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpWhois.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpWhois.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
import { Configuration, DatabasesIPWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPWHOISApi(config);

async function main() {
  const result = await api.dbIpWhois({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
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
    data, _, err := client.DatabasesIPWHOISAPI.DbIpWhois(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbIpWhois.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbIpWhois.gz\n", len(data))
}

```

</details>

---

## IP WHOIS Snapshot Status

`GET /v3.3/status/snapshot/ip/whois`

IP WHOIS Snapshot Status. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ipwhois_api import DatabasesIPWHOISApi

# Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPWHOISApi(ApiClient(config))

result = api.db_ip_whois_status()
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPWHOISApi(config);

async function main() {
  const result = await api.dbIpWhoisStatus({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
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
    result, _, err := client.DatabasesIPWHOISAPI.DbIpWhoisStatus(ctx).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
