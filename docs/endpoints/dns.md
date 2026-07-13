# DNS

DNS lookup APIs (live, historical, reverse, bulk)

4 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Live DNS Lookup

`GET /v2.0/dns/live`

Real-time DNS record lookup. 1 credit per query.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `domainName` | query | no | string |  |
| `ipAddress` | query | no | string | Use for PTR lookups |
| `type` | query | yes | string | all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Live DNS Lookup (GET /v2.0/dns/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsLive (GET /v2.0/dns/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - ipAddress (string, required): Use for PTR lookups
#   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DNSApi(ApiClient(config))

resp = api.dns_live_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com", ip_address="8.8.8.8", var_type="value")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import { Configuration, DNSApi } from "whoisfreaks";

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsLiveRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", ipAddress: "8.8.8.8", type: "value", format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
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
    // apiKey is a builder method on the request, not a config/context value
    result, httpRes, err := client.DNSAPI.DnsLive(context.Background()).ApiKey("YOUR_API_KEY").DomainName("example.com").IpAddress("8.8.8.8").Type("value").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Historical DNS Lookup

`GET /v2.0/dns/historical`

All historical DNS records. 2 credits per page (100 records/page).

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `domainName` | query | yes | string |  |
| `type` | query | yes | string |  |
| `page` | query | no | integer |  |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsHistorical (GET /v2.0/dns/historical):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - type (string, required)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DNSApi(ApiClient(config))

resp = api.dns_historical_with_http_info(api_key="YOUR_API_KEY", domain_name="example.com", var_type="value")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, DNSApi } from "whoisfreaks";

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsHistoricalRaw({ apiKey: "YOUR_API_KEY", domainName: "example.com", type: "value", page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
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
    // apiKey is a builder method on the request, not a config/context value
    result, httpRes, err := client.DNSAPI.DnsHistorical(context.Background()).ApiKey("YOUR_API_KEY").DomainName("example.com").Type("value").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Reverse DNS Lookup

`GET /v2.1/dns/reverse`

Search domains by IP or DNS value. 5 credits per page.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `value` | query | yes | string | IP, CIDR, or record value |
| `type` | query | yes | string |  (one of: a, mx, cname, ns, aaaa, txt, soa) |
| `exact` | query | no | boolean |  |
| `page` | query | no | integer |  |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi

# Parameters for dnsReverse (GET /v2.1/dns/reverse):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - value (string, required): IP, CIDR, or record value
#   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
#   - exact (boolean, optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
config = Configuration()
api = DNSApi(ApiClient(config))

resp = api.dns_reverse_with_http_info(api_key="YOUR_API_KEY", value="value", var_type="a", exact=True)
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import { Configuration, DNSApi } from "whoisfreaks";

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsReverseRaw({ apiKey: "YOUR_API_KEY", value: "value", type: "a", exact: true, page: undefined, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Reverse DNS Lookup (GET /v2.1/dns/reverse)
// Parameters for dnsReverse (GET /v2.1/dns/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - value (string, required): IP, CIDR, or record value
//   - type (string (one of: a, mx, cname, ns, aaaa, txt, soa), required)
//   - exact (boolean, optional)
//   - page (integer, optional)
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
    // apiKey is a builder method on the request, not a config/context value
    result, httpRes, err := client.DNSAPI.DnsReverse(context.Background()).ApiKey("YOUR_API_KEY").Value("value").Type("a").Exact(true).Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Bulk DNS Lookup

`POST /v2.0/dns/bulk/live`

Up to 100 domains + 100 IPs in one request.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `type` | query | yes | string |  |
| `format` | query | no | string |  (one of: json, xml) |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.dns_api import DNSApi
from whoisfreaks.models.dns_bulk_request import DnsBulkRequest

# Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - type (string, required)
#   - format (string (one of: json, xml), optional)
#   - body: DnsBulkRequest (required) -- request body object
config = Configuration()
api = DNSApi(ApiClient(config))

dns_bulk_request = DnsBulkRequest()  # populate fields as needed
resp = api.dns_bulk_with_http_info(api_key="YOUR_API_KEY", var_type="value", dns_bulk_request=dns_bulk_request)
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import { Configuration, DNSApi } from "whoisfreaks";

const api = new DNSApi(new Configuration());

async function main() {
  const resp = await api.dnsBulkRaw({ apiKey: "YOUR_API_KEY", type: "value", dnsBulkRequest: {}, format: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
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
    result, httpRes, err := client.DNSAPI.DnsBulk(context.Background()).ApiKey("YOUR_API_KEY").Type("value").DnsBulkRequest(*wf.NewDnsBulkRequest()).Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
