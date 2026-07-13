# Account

Account, API key, and usage utilities

3 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Rotate API Key

`GET /v1.0/api-key/rotate`

Rotate API Key. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = AccountApi(ApiClient(config))

resp = api.rotate_api_key_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, AccountApi } from "whoisfreaks";

const api = new AccountApi(new Configuration());

async function main() {
  const resp = await api.rotateApiKeyRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
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
    result, httpRes, err := client.AccountAPI.RotateApiKey(context.Background()).ApiKey("YOUR_API_KEY").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Account Usage

`GET /v1.0/whoisapi/usage`

Account Usage. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `apiKey` | query | yes | string | Your WHOISFreaks API key |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Account Usage (GET /v1.0/whoisapi/usage)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for accountUsage (GET /v1.0/whoisapi/usage):
#   - apiKey (string, required): Your WHOISFreaks API key
config = Configuration()
api = AccountApi(ApiClient(config))

resp = api.account_usage_with_http_info(api_key="YOUR_API_KEY")
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   - apiKey (string, required): Your WHOISFreaks API key
import { Configuration, AccountApi } from "whoisfreaks";

const api = new AccountApi(new Configuration());

async function main() {
  const resp = await api.accountUsageRaw({ apiKey: "YOUR_API_KEY" });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
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
    result, httpRes, err := client.AccountAPI.AccountUsage(context.Background()).ApiKey("YOUR_API_KEY").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---

## Database File Status (Public)

`GET /v3.3/status`

No API key required. Returns freshness of all downloadable files.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Database File Status (Public) (GET /v3.3/status)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for databaseFileStatus (GET /v3.3/status):
#   (no parameters besides apiKey)
config = Configuration()
api = AccountApi(ApiClient(config))

resp = api.database_file_status_with_http_info()
print("status:", resp.status_code)
print(resp.data)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
import { Configuration, AccountApi } from "whoisfreaks";

const api = new AccountApi(new Configuration());

async function main() {
  const resp = await api.databaseFileStatusRaw({  });
  console.log("status:", resp.raw.status);
  console.log(await resp.value());
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters besides apiKey)
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
    result, httpRes, err := client.AccountAPI.DatabaseFileStatus(context.Background()).ApiKey("YOUR_API_KEY").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
