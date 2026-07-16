# Databases - WHOIS

WHOIS database snapshots

3 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## WHOIS Database Daily

`GET /v3.3/download/dbupdate/daily/domains/whois`

WHOIS Database Daily. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_whois_api import DatabasesWHOISApi

# Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesWHOISApi(ApiClient(config))

data = api.db_whois_daily(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbWhoisDaily.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbWhoisDaily.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesWHOISApi(config);

async function main() {
  const result = await api.dbWhoisDaily({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: WHOIS Database Daily (GET /v3.3/download/dbupdate/daily/domains/whois)
// Parameters for dbWhoisDaily (GET /v3.3/download/dbupdate/daily/domains/whois):
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
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    // returns raw bytes (compressed/binary file) -- write to disk
    data, _, err := client.DatabasesWHOISAPI.DbWhoisDaily(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbWhoisDaily.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbWhoisDaily.gz\n", len(data))
}

```

</details>

---

## WHOIS Database Weekly

`GET /v3.3/download/dbupdate/weekly/domains/whois`

WHOIS Database Weekly. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_whois_api import DatabasesWHOISApi

# Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesWHOISApi(ApiClient(config))

data = api.db_whois_weekly(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbWhoisWeekly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbWhoisWeekly.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesWHOISApi(config);

async function main() {
  const result = await api.dbWhoisWeekly({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
// Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
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
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    // returns raw bytes (compressed/binary file) -- write to disk
    data, _, err := client.DatabasesWHOISAPI.DbWhoisWeekly(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbWhoisWeekly.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbWhoisWeekly.gz\n", len(data))
}

```

</details>

---

## WHOIS Database Monthly

`GET /v3.3/download/dbupdate/monthly/domains/whois`

WHOIS Database Monthly. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_whois_api import DatabasesWHOISApi

# Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesWHOISApi(ApiClient(config))

data = api.db_whois_monthly(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbWhoisMonthly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbWhoisMonthly.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesWHOISApi(config);

async function main() {
  const result = await api.dbWhoisMonthly({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
// Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
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
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    // returns raw bytes (compressed/binary file) -- write to disk
    data, _, err := client.DatabasesWHOISAPI.DbWhoisMonthly(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbWhoisMonthly.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbWhoisMonthly.gz\n", len(data))
}

```

</details>

---
