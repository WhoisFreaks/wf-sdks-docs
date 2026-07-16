# Account

Account, API key, and usage utilities

3 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Rotate API Key

`GET /v1.0/api-key/rotate`

Rotate API Key. Returns the file/snapshot described by this operation.

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = AccountApi(ApiClient(config))

result = api.rotate_api_key()
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
import { Configuration, AccountApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new AccountApi(config);

async function main() {
  const result = await api.rotateApiKey({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
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
    result, _, err := client.AccountAPI.RotateApiKey(ctx).Execute()
    if err != nil { panic(err) }
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

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Account Usage (GET /v1.0/whoisapi/usage)."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.account_api import AccountApi

# Parameters for accountUsage (GET /v1.0/whoisapi/usage):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = AccountApi(ApiClient(config))

result = api.account_usage()
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
import { Configuration, AccountApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new AccountApi(config);

async function main() {
  const result = await api.accountUsage({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
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
    result, _, err := client.AccountAPI.AccountUsage(ctx).Execute()
    if err != nil { panic(err) }
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
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = AccountApi(ApiClient(config))

result = api.database_file_status()
print(result)

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
//   (no parameters; the API key is set on the client)
import { Configuration, AccountApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new AccountApi(config);

async function main() {
  const result = await api.databaseFileStatus({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Database File Status (Public) (GET /v3.3/status)
// Parameters for databaseFileStatus (GET /v3.3/status):
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
    result, _, err := client.AccountAPI.DatabaseFileStatus(ctx).Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

</details>

---
