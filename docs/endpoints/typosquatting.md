# Typosquatting

Detect typo variants of brand domains

1 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Typosquatting Lookup

`GET /v3.0/domain/typos`

Find typo variants of a brand. 5 credits per page.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |
| `keyword` | query | no | string |  |
| `pattern` | query | no | string |  |
| `pageToken` | query | no | string |  |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.typosquatting_api import TyposquattingApi

# Parameters for typosquatting (GET /v3.0/domain/typos):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - keyword (string, optional)
#   - pattern (string, optional)
#   - pageToken (string, optional)
config = Configuration()
api = TyposquattingApi(ApiClient(config))

resp = api.typosquatting_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
import { Configuration, TyposquattingApi } from "whoisfreaks";

const api = new TyposquattingApi(new Configuration());

async function main() {
  const resp = await api.typosquattingRaw({ apiKey: "YOUR_API_KEY", keyword: undefined, pattern: undefined, pageToken: undefined });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
package main

import (
    "context"
    "fmt"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    // apiKey is a builder method on the request, not a config/context value
    result, httpRes, err := client.TyposquattingAPI.Typosquatting(context.Background()).ApiKey("YOUR_API_KEY").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    fmt.Println(result)
}

```

</details>

---
