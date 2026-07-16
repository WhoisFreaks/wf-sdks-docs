# Databases - Newly Registered

Newly registered domain downloads

7 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Newly Registered gTLD (CSV)

`GET /v3.1/download/domainer/gtld`

Newly Registered gTLD (CSV). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `whois` | query | yes | boolean |  |
| `date` | query | no | string | yyyy-MM-dd; omit for latest |
| `tlds` | query | no | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_gtld(whois=False, var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyGtld.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyGtld.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyGtld({ whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
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
    data, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyGtld(ctx).Whois(false).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbNewlyGtld.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbNewlyGtld.gz\n", len(data))
}

```

</details>

---

## Newly Registered ccTLD (CSV)

`GET /v3.1/download/domainer/cctld`

Newly Registered ccTLD (CSV). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `whois` | query | yes | boolean |  |
| `date` | query | no | string | yyyy-MM-dd; omit for latest |
| `tlds` | query | no | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_cctld(whois=False, var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyCctld.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyCctld.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyCctld({ whois: false, date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
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
    data, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyCctld(ctx).Whois(false).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbNewlyCctld.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbNewlyCctld.gz\n", len(data))
}

```

</details>

---

## Newly Registered gTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/gtld/cleaned`

Newly Registered gTLD Cleaned WHOIS (CSV). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_gtld_cleaned(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyGtldCleaned.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyGtldCleaned.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyGtldCleaned({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
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
    data, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyGtldCleaned(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbNewlyGtldCleaned.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbNewlyGtldCleaned.gz\n", len(data))
}

```

</details>

---

## Newly Registered ccTLD Cleaned WHOIS (CSV)

`GET /v3.1/download/domainer/cctld/cleaned`

Newly Registered ccTLD Cleaned WHOIS (CSV). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_cctld_cleaned(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyCctldCleaned.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyCctldCleaned.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyCctldCleaned({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
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
    data, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyCctldCleaned(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbNewlyCctldCleaned.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbNewlyCctldCleaned.gz\n", len(data))
}

```

</details>

---

## Newly Registered gTLD (JSON)

`GET /v3.1/domains/newly/gtld`

Newly Registered gTLD (JSON). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | yyyy-MM-dd; omit for latest |
| `tlds` | query | no | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesNewlyRegisteredApi(ApiClient(config))

result = api.db_newly_gtld_json(var_date=str(date.today() - timedelta(days=1)))
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyGtldJson({ date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "time"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    result, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyGtldJson(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Newly Registered ccTLD (JSON)

`GET /v3.1/domains/newly/cctld`

Newly Registered ccTLD (JSON). Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | yyyy-MM-dd; omit for latest |
| `tlds` | query | no | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesNewlyRegisteredApi(ApiClient(config))

result = api.db_newly_cctld_json(var_date=str(date.today() - timedelta(days=1)))
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyCctldJson({ date: new Date(Date.now()-86400000).toISOString().slice(0,10), tlds: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
package main

import (
    "context"
    "encoding/json"
    "fmt"
    "time"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    result, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyCctldJson(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Newly Registered With DNS

`GET /v3.1/download/domainer/newly/dns`

Newly Registered With DNS. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | yyyy-MM-dd; omit for latest |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_newly_registered_api import DatabasesNewlyRegisteredApi

# Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesNewlyRegisteredApi(ApiClient(config))

data = api.db_newly_dns(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("dbNewlyDns.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to dbNewlyDns.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import { Configuration, DatabasesNewlyRegisteredApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesNewlyRegisteredApi(config);

async function main() {
  const result = await api.dbNewlyDns({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
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
    data, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyDns(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbNewlyDns.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbNewlyDns.gz\n", len(data))
}

```

</details>

---
