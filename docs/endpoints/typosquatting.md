# Typosquatting

*Section: API Solutions*

Detect typo variants of brand domains

1 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Typosquatting Lookup

`GET /v3.0/domain/typos`

Find typo variants of a brand. 5 credits per page.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `keyword` | query | no | string |  |
| `pattern` | query | no | string |  |
| `pageToken` | query | no | string |  |

**Response** (`TyposquattingResponse`)

| Field | Type | Description |
|-------|------|-------------|
| `status` | boolean |  |
| `totalRecords` | integer |  |
| `currentPage` | integer |  |
| `totalPages` | integer |  |
| `hasNextPage` | boolean |  |
| `nextPageToken` | string |  |
| `domains` | array<TyposquattingDomain> |  |

<details><summary><code>TyposquattingDomain</code> object</summary>

| Field | Type | Description |
|-------|------|-------------|
| `domainName` | string |  |
| `createDate` | string |  |
| `expiryDate` | string |  |
| `lastSeen` | string |  |
| `isDropped` | boolean |  |

</details>


**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.typosquatting_api import TyposquattingApi

# Parameters for typosquatting (GET /v3.0/domain/typos):
#   - keyword (string, optional)
#   - pattern (string, optional)
#   - pageToken (string, optional)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = TyposquattingApi(ApiClient(config))

result = api.typosquatting()
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import { Configuration, TyposquattingApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new TyposquattingApi(config);

async function main() {
  const result = await api.typosquatting({ keyword: undefined, pattern: undefined, pageToken: undefined });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
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
    result, _, err := client.TyposquattingAPI.Typosquatting(ctx).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
