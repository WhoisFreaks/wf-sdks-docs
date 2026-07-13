# WHOIS

WHOIS lookup APIs (live, historical, reverse, bulk)

3 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Live WHOIS Lookup

`GET /v2.0/whois/live`

Real-time WHOIS lookup from authoritative servers. Cost 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `domainName` | query | yes | string |  |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisLive (GET /v2.0/whois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = WHOISApi(ApiClient(config))

resp = api.whois_live_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisLiveRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
package main

import (
    "context"
    "fmt"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    result, httpRes, err := client.WHOISAPI.WhoisLive(ctx).DomainName("example.com").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    fmt.Println(result)
}

```

</details>

---

## WHOIS Historical or Reverse Lookup

`GET /v1.0/whois`

Historical WHOIS (all records since 1986) or Reverse WHOIS (search by keyword/email/owner/company). Historical: 2 credits/page (100 records). Reverse: 5 credits/page.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `whois` | query | yes | string |  (one of: historical, reverse) |
| `domainName` | query | no | string | Required for historical lookup |
| `keyword` | query | no | string | For reverse — domain keyword search |
| `email` | query | no | string | For reverse — registrant email search |
| `owner` | query | no | string | For reverse — registrant name search |
| `company` | query | no | string | For reverse — company name search |
| `mode` | query | no | string |  (one of: default, mini) |
| `exact` | query | no | boolean |  |
| `page` | query | no | integer |  |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: WHOIS Historical or Reverse Lookup (GET /v1.0/whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi

# Parameters for whoisHistoricalOrReverse (GET /v1.0/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (string (one of: historical, reverse), required)
#   - domainName (string, required): Required for historical lookup
#   - keyword (string, optional): For reverse — domain keyword search
#   - email (string, optional): For reverse — registrant email search
#   - owner (string, optional): For reverse — registrant name search
#   - company (string, optional): For reverse — company name search
#   - mode (string (one of: default, mini), optional)
#   - exact (boolean, optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = WHOISApi(ApiClient(config))

resp = api.whois_historical_or_reverse_with_http_info(api_key="YOUR_API_KEY", whois="historical", domain_name="example.com", exact=True)
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: WHOIS Historical or Reverse Lookup (GET /v1.0/whois)
// Parameters for whoisHistoricalOrReverse (GET /v1.0/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (string (one of: historical, reverse), required)
//   - domainName (string, required): Required for historical lookup
//   - keyword (string, optional): For reverse — domain keyword search
//   - email (string, optional): For reverse — registrant email search
//   - owner (string, optional): For reverse — registrant name search
//   - company (string, optional): For reverse — company name search
//   - mode (string (one of: default, mini), optional)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.whoisHistoricalOrReverseRaw({ apiKey: "YOUR_API_KEY", whois: "historical", domainName: "example.com", exact: true, keyword: undefined, email: undefined, owner: undefined, company: undefined, mode: undefined, page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: WHOIS Historical or Reverse Lookup (GET /v1.0/whois)
// Parameters for whoisHistoricalOrReverse (GET /v1.0/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (string (one of: historical, reverse), required)
//   - domainName (string, required): Required for historical lookup
//   - keyword (string, optional): For reverse — domain keyword search
//   - email (string, optional): For reverse — registrant email search
//   - owner (string, optional): For reverse — registrant name search
//   - company (string, optional): For reverse — company name search
//   - mode (string (one of: default, mini), optional)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
package main

import (
    "context"
    "fmt"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    result, httpRes, err := client.WHOISAPI.WhoisHistoricalOrReverse(ctx).Whois("historical").DomainName("example.com").Exact(true).Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    fmt.Println(result)
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
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.whois_api import WHOISApi
from whoisfreaks.models.bulk_whois_request import BulkWhoisRequest

# Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - format (string (one of: json, xml), optional)
#   - body: BulkWhoisRequest (required) -- request body object
config = Configuration()
api = WHOISApi(ApiClient(config))

bulk_whois_request = BulkWhoisRequest()  # populate fields as needed
resp = api.bulk_whois_with_http_info(api_key="YOUR_API_KEY", bulk_whois_request=bulk_whois_request)
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import { Configuration, WHOISApi } from "whoisfreaks";

const api = new WHOISApi(new Configuration());

async function main() {
  const resp = await api.bulkWhoisRaw({ apiKey: "YOUR_API_KEY", bulkWhoisRequest: {}, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
package main

import (
    "context"
    "fmt"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    result, httpRes, err := client.WHOISAPI.BulkWhois(ctx).BulkWhoisRequest(*wf.NewBulkWhoisRequest()).Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    fmt.Println(result)
}

```

</details>

---
