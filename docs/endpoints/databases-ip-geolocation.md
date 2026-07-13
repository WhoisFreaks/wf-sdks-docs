# Databases - IP Geolocation

IP geolocation database snapshots

4 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## IP to Country Snapshot Status

`GET /v3.3/status/snapshot/ip/country`

IP to Country Snapshot Status. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesIPGeolocationApi(ApiClient(config))

resp = api.db_ip_country_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const api = new DatabasesIPGeolocationApi(new Configuration());

async function main() {
  const resp = await api.dbIpCountryStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
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
    result, httpRes, err := client.DatabasesIPGeolocationAPI.DbIpCountryStatus(context.Background()).ApiKey("YOUR_API_KEY").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
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
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
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
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesIPGeolocationApi(ApiClient(config))

data = api.db_ip_country(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpCountry.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpCountry.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const api = new DatabasesIPGeolocationApi(new Configuration());

async function main() {
  const resp = await api.dbIpCountryRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
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
    data, _, err := client.DatabasesIPGeolocationAPI.DbIpCountry(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
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
| `apiKey` | query | yes | string | Your WHOISFreaks API key |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_ip_geolocation_api import DatabasesIPGeolocationApi

# Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = DatabasesIPGeolocationApi(ApiClient(config))

resp = api.db_ip_city_status_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const api = new DatabasesIPGeolocationApi(new Configuration());

async function main() {
  const resp = await api.dbIpCityStatusRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
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
    result, httpRes, err := client.DatabasesIPGeolocationAPI.DbIpCityStatus(context.Background()).ApiKey("YOUR_API_KEY").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
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
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
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
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
config = Configuration()
api = DatabasesIPGeolocationApi(ApiClient(config))

data = api.db_ip_city(api_key="YOUR_API_KEY", var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbIpCity.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbIpCity.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import { Configuration, DatabasesIPGeolocationApi } from "whoisfreaks";

const api = new DatabasesIPGeolocationApi(new Configuration());

async function main() {
  const resp = await api.dbIpCityRaw({ apiKey: "YOUR_API_KEY", date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
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
    data, _, err := client.DatabasesIPGeolocationAPI.DbIpCity(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbIpCity.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbIpCity.gz\n", len(data))
}

```

</details>

---
