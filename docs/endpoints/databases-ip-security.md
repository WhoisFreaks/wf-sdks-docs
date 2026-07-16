# Databases - IP Security

IP security database snapshots

2 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## IP Security Snapshot

`GET /v3.3/download/snapshot/ip/security`

IP Security Snapshot. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | yes | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_security_api import DatabasesIPSecurityApi

# Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
#   - date (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPSecurityApi(ApiClient(config))

data = api.db_ip_security(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpSecurity.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpSecurity.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required)
import { Configuration, DatabasesIPSecurityApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPSecurityApi(config);

async function main() {
  const result = await api.dbIpSecurity({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
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
    data, _, err := client.DatabasesIPSecurityAPI.DbIpSecurity(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbIpSecurity.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbIpSecurity.gz\n", len(data))
}

```

</details>

---

## IP Security Snapshot Status

`GET /v3.3/status/snapshot/ip/security`

IP Security Snapshot Status. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_security_api import DatabasesIPSecurityApi

# Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPSecurityApi(ApiClient(config))

result = api.db_ip_security_status()
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPSecurityApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPSecurityApi(config);

async function main() {
  const result = await api.dbIpSecurityStatus({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
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
    result, _, err := client.DatabasesIPSecurityAPI.DbIpSecurityStatus(ctx).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
