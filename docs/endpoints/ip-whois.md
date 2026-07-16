# IP WHOIS

*Section: API Solutions*

IP address WHOIS

1 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## IP WHOIS Lookup

`GET /v1.0/ip-whois`

WHOIS for an IP address. 1 credit.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `ip` | query | yes | string |  |
| `format` | query | no | string |  (one of: json, xml) |

**Response** (`IpWhoisResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `status` | boolean |  |
| `ip_address` | string |  |
| `as_number` | string |  |
| `query_time` | string |  |
| `whois_server` | string |  |
| `whois_raw_response` | string |  |
| `r_whois_raw_response` | string |  |
| `inet_nums` | array<InetNum> |  |
| `organization` | WhoisOrganization |  |
| `irt` | Irt |  |
| `administrative_contacts` | array<WhoisPerson> |  |
| `technical_contacts` | array<WhoisPerson> |  |
| `abuse_contacts` | array<WhoisPerson> |  |
| `routes` | array<Route> |  |

<details><summary><code>InetNum</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `start_ip` | string |  |
| `end_ip` | string |  |
| `cidr` | array<string> |  |
| `net_name` | string |  |
| `net_handle` | string |  |
| `description` | array<string> |  |
| `countries` | array<string> |  |
| `geofeed` | string |  |
| `latitude` | number |  |
| `longitude` | number |  |
| `city` | string |  |
| `languages` | array<string> |  |
| `status` | string |  |
| `organization` | string |  |
| `sponsoring_organization` | string |  |
| `remarks` | array<string> |  |
| `assignment_size` | string |  |
| `notify` | array<string> |  |
| `mnt_by` | array<string> |  |
| `mnt_lower` | array<string> |  |
| `mnt_domains` | array<string> |  |
| `mnt_routes` | array<string> |  |
| `mnt_irt` | array<string> |  |
| `date_created` | string |  |
| `date_updated` | string |  |
| `source` | string |  |
| `parents` | array<string> |  |

</details>

<details><summary><code>WhoisOrganization</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `handle` | string |  |
| `name` | string |  |
| `type` | string |  |
| `description` | array<string> |  |
| `address` | array<string> |  |
| `street` | string |  |
| `city` | string |  |
| `district` | string |  |
| `state` | string |  |
| `zip_code` | string |  |
| `country` | array<string> |  |
| `latitude` | number |  |
| `longitude` | number |  |
| `email` | array<string> |  |
| `abuse_mailbox` | array<string> |  |
| `phone` | array<string> |  |
| `fax_no` | array<string> |  |
| `organizations` | array<string> |  |
| `admin_contacts` | array<string> |  |
| `tech_contacts` | array<string> |  |
| `abuse_contacts` | array<string> |  |
| `languages` | array<string> |  |
| `remarks` | array<string> |  |
| `notify` | array<string> |  |
| `ref_nfy` | array<string> |  |
| `mnt_ref` | array<string> |  |
| `mnt_by` | array<string> |  |
| `date_created` | string |  |
| `date_updated` | string |  |
| `source` | string |  |

</details>

<details><summary><code>Irt</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `handle` | string |  |
| `address` | array<string> |  |
| `street` | string |  |
| `city` | string |  |
| `district` | string |  |
| `state` | string |  |
| `zip_code` | string |  |
| `country` | string |  |
| `email` | array<string> |  |
| `abuse_mailbox` | array<string> |  |
| `phone` | array<string> |  |
| `fax_no` | array<string> |  |
| `organizations` | array<string> |  |
| `admin_contacts` | array<string> |  |
| `tech_contacts` | array<string> |  |
| `remarks` | array<string> |  |
| `signature` | array<string> |  |
| `encryption` | array<string> |  |
| `auth` | array<string> |  |
| `notify` | array<string> |  |
| `irt_nfy` | array<string> |  |
| `mnt_by` | array<string> |  |
| `mnt_ref` | array<string> |  |

</details>

<details><summary><code>WhoisPerson</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `handle` | string |  |
| `name` | string |  |
| `address` | array<string> |  |
| `street` | string |  |
| `city` | string |  |
| `district` | string |  |
| `state` | string |  |
| `zip_code` | string |  |
| `country` | string |  |
| `email` | array<string> |  |
| `abuse_mailbox` | array<string> |  |
| `phone` | array<string> |  |
| `fax_no` | array<string> |  |
| `organizations` | array<string> |  |
| `admin_contacts` | array<string> |  |
| `tech_contacts` | array<string> |  |
| `remarks` | array<string> |  |
| `notify` | array<string> |  |
| `mnt_by` | array<string> |  |
| `mnt_ref` | array<string> |  |
| `date_created` | string |  |
| `date_updated` | string |  |
| `source` | string |  |

</details>

<details><summary><code>Route</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `route` | string |  |
| `description` | array<string> |  |
| `origin` | string |  |
| `pingable` | array<string> |  |
| `ping_hdl` | array<string> |  |
| `holes` | array<string> |  |
| `country` | string |  |
| `organizations` | array<string> |  |
| `member_of` | array<string> |  |
| `inject` | array<string> |  |
| `aggr_mtd` | string |  |
| `aggr_bndry` | string |  |
| `export_comps` | string |  |
| `components` | string |  |
| `remarks` | array<string> |  |
| `notify` | array<string> |  |
| `mnt_lower` | array<string> |  |
| `mnt_routes` | array<string> |  |
| `mnt_by` | array<string> |  |
| `date_created` | string |  |
| `date_updated` | string |  |
| `source` | string |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.ipwhois_api import IPWHOISApi

# Parameters for ipWhois (GET /v1.0/ip-whois):
#   - ip (string, required)
#   - format (string (one of: json, xml), optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = IPWHOISApi(ApiClient(config))

result = api.ip_whois(ip="8.8.8.8")
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import { Configuration, IPWHOISApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new IPWHOISApi(config);

async function main() {
  const result = await api.ipWhois({ ip: "8.8.8.8", format: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
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
    result, _, err := client.IPWHOISAPI.IpWhois(ctx).Ip("8.8.8.8").Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
