# WHOIS

WHOIS lookup APIs (live, historical, reverse, bulk)

4 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Live WHOIS Lookup

`GET /v2.0/whois/live`

Real-time WHOIS lookup from authoritative servers. Cost 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `domainName` | query | yes | string |  |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisLive (GET /v2.0/whois/live):
#   - domainName (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = WHOISApi(ApiClient(config))

result = api.whois_live(domain_name="example.com")
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.whoisLive({ domainName: "example.com", format: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
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
    result, _, err := client.WHOISAPI.WhoisLive(ctx).DomainName("example.com").Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Bulk WHOIS Lookup

`POST /v2.0/bulkwhois/live`

Up to 100 domains in one request. 1 credit per successful domain.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi
from whoisfreaks.models.bulk_whois_request import BulkWhoisRequest

# Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
#   - format (string (one of: json, xml), optional)
#   - body: BulkWhoisRequest (required) -- request body object
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = WHOISApi(ApiClient(config))

bulk_whois_request = BulkWhoisRequest()  # populate fields as needed
result = api.bulk_whois(bulk_whois_request=bulk_whois_request)
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.bulkWhois({ bulkWhoisRequest: {}, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
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
    result, _, err := client.WHOISAPI.BulkWhois(ctx).BulkWhoisRequest(*wf.NewBulkWhoisRequest()).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Historical WHOIS records for a domain

`GET /v2.0/whois/history`

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `domainName` | query | yes | string | Domain to fetch historical WHOIS records for |
| `page` | query | no | integer | Page number |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisHistory (GET /v2.0/whois/history):
#   - domainName (string, required): Domain to fetch historical WHOIS records for
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = WHOISApi(ApiClient(config))

result = api.whois_history(domain_name="example.com")
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.whoisHistory({ domainName: "example.com", page: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
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
    result, _, err := client.WHOISAPI.WhoisHistory(ctx).DomainName("example.com").Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Reverse WHOIS lookup by keyword

`GET /v2.0/whois/reverse`

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `keyword` | query | yes | string | Keyword to search across WHOIS records |
| `page` | query | no | integer | Page number |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisReverse (GET /v2.0/whois/reverse):
#   - keyword (string, required): Keyword to search across WHOIS records
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = WHOISApi(ApiClient(config))

result = api.whois_reverse(keyword="value")
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new WHOISApi(config);

async function main() {
  const result = await api.whoisReverse({ keyword: "value", page: undefined, format: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
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
    result, _, err := client.WHOISAPI.WhoisReverse(ctx).Keyword("value").Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
