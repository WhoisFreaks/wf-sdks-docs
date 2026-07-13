# Databases - DNS

DNS database snapshots

3 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## DNS Database Daily

`GET /v3.2/download/dbupdate/daily/dns`

DNS Database Daily. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_dns_api import DatabasesDNSApi

# Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesDNSApi(ApiClient(config))

data = api.db_dns_daily(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDnsDaily.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDnsDaily.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesDNSApi } from "whoisfreaks";

const api = new DatabasesDNSApi(new Configuration());

async function main() {
  const resp = await api.dbDnsDailyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
// Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
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
    data, _, err := client.DatabasesDNSAPI.DbDnsDaily(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbDnsDaily.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbDnsDaily.gz\n", len(data))
}

```

</details>

---

## DNS Database Weekly

`GET /v3.2/download/dbupdate/weekly/dns`

DNS Database Weekly. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_dns_api import DatabasesDNSApi

# Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesDNSApi(ApiClient(config))

data = api.db_dns_weekly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDnsWeekly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDnsWeekly.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesDNSApi } from "whoisfreaks";

const api = new DatabasesDNSApi(new Configuration());

async function main() {
  const resp = await api.dbDnsWeeklyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
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
    data, _, err := client.DatabasesDNSAPI.DbDnsWeekly(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbDnsWeekly.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbDnsWeekly.gz\n", len(data))
}

```

</details>

---

## DNS Database Monthly

`GET /v3.2/download/dbupdate/monthly/dns`

DNS Database Monthly. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_dns_api import DatabasesDNSApi

# Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
api = DatabasesDNSApi(ApiClient(config))

data = api.db_dns_monthly(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbDnsMonthly.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbDnsMonthly.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesDNSApi } from "whoisfreaks";

const api = new DatabasesDNSApi(new Configuration());

async function main() {
  const resp = await api.dbDnsMonthlyRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
// Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
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
    data, _, err := client.DatabasesDNSAPI.DbDnsMonthly(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbDnsMonthly.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbDnsMonthly.gz\n", len(data))
}

```

</details>

---
