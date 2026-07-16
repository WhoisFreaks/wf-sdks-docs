# Databases - IP Geolocation

IP geolocation database snapshots

4 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

IP to Country Snapshot Status. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPGeolocationApi(ApiClient(config))

result = api.db_ip_country_status()
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCountryStatus({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
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
    result, _, err := client.DatabasesIPGeolocationAPI.DbIpCountryStatus(ctx).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## IP to Country Snapshot

`GET /v3.3/download/snapshot/ip/country`

IP to Country Snapshot. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | yes | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
#   - date (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPGeolocationApi(ApiClient(config))

data = api.db_ip_country(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpCountry.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpCountry.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCountry({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
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
    data, _, err := client.DatabasesIPGeolocationAPI.DbIpCountry(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbIpCountry.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbIpCountry.gz\n", len(data))
}

```

</details>

---

## IP to City Snapshot Status

`GET /v3.3/status/snapshot/ip/city`

IP to City Snapshot Status. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPGeolocationApi(ApiClient(config))

result = api.db_ip_city_status()
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCityStatus({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
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
    result, _, err := client.DatabasesIPGeolocationAPI.DbIpCityStatus(ctx).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## IP to City Snapshot

`GET /v3.3/download/snapshot/ip/city`

IP to City Snapshot. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | yes | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
#   - date (string, required)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesIPGeolocationApi(ApiClient(config))

data = api.db_ip_city(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpCity.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpCity.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - date (string, required)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesIPGeolocationApi(config);

async function main() {
  const result = await api.dbIpCity({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
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
    data, _, err := client.DatabasesIPGeolocationAPI.DbIpCity(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbIpCity.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbIpCity.gz\n", len(data))
}

```

</details>

---
