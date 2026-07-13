# Databases - Subdomains

Subdomain database snapshots

3 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Subdomains Daily

`GET /v3.2/download/dbupdate/daily/subdomains`

Subdomains Daily. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_subdomains_api import DatabasesSubdomainsApi

# Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesSubdomainsApi(ApiClient(config))

data = api.db_subdomains_daily(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbSubdomainsDaily.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbSubdomainsDaily.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesSubdomainsApi } from "whoisfreaks";

const api = new DatabasesSubdomainsApi(new Configuration());

async function main() {
  const resp = await api.dbSubdomainsDailyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Subdomains Daily (GET /v3.2/download/dbupdate/daily/subdomains)
// Parameters for dbSubdomainsDaily (GET /v3.2/download/dbupdate/daily/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
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
    data, _, err := client.DatabasesSubdomainsAPI.DbSubdomainsDaily(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbSubdomainsDaily.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbSubdomainsDaily.gz\n", len(data))
}

```

</details>

---

## Subdomains Weekly

`GET /v3.2/download/dbupdate/weekly/subdomains`

Subdomains Weekly. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_subdomains_api import DatabasesSubdomainsApi

# Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesSubdomainsApi(ApiClient(config))

data = api.db_subdomains_weekly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbSubdomainsWeekly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbSubdomainsWeekly.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesSubdomainsApi } from "whoisfreaks";

const api = new DatabasesSubdomainsApi(new Configuration());

async function main() {
  const resp = await api.dbSubdomainsWeeklyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
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
    data, _, err := client.DatabasesSubdomainsAPI.DbSubdomainsWeekly(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbSubdomainsWeekly.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbSubdomainsWeekly.gz\n", len(data))
}

```

</details>

---

## Subdomains Monthly

`GET /v3.2/download/dbupdate/monthly/subdomains`

Subdomains Monthly. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_subdomains_api import DatabasesSubdomainsApi

# Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesSubdomainsApi(ApiClient(config))

data = api.db_subdomains_monthly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbSubdomainsMonthly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbSubdomainsMonthly.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesSubdomainsApi } from "whoisfreaks";

const api = new DatabasesSubdomainsApi(new Configuration());

async function main() {
  const resp = await api.dbSubdomainsMonthlyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
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
    data, _, err := client.DatabasesSubdomainsAPI.DbSubdomainsMonthly(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbSubdomainsMonthly.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbSubdomainsMonthly.gz\n", len(data))
}

```

</details>

---
