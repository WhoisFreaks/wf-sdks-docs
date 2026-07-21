# Databases - Threat Feed

*Section: Databases*

6 endpoint(s). All requests require your API key — see [Authentication](../authentication.md).

## Download the daily phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing`

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | Feed date (yyyy-MM-dd); defaults to latest available |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_threat_feed_api import DatabasesThreatFeedApi

# Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
#   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesThreatFeedApi(ApiClient(config))

data = api.download_threat_feed_phishing(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("downloadThreatFeedPhishing.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to downloadThreatFeedPhishing.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import { Configuration, DatabasesThreatFeedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesThreatFeedApi(config);

async function main() {
  const result = await api.downloadThreatFeedPhishing({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
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
    data, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedPhishing(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("downloadThreatFeedPhishing.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to downloadThreatFeedPhishing.gz\n", len(data))
}

```

</details>

---

## Download a sample of the phishing threat feed (CSV)

`GET /v3.4/download/threat-feed/phishing/sample`

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_threat_feed_api import DatabasesThreatFeedApi

# Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesThreatFeedApi(ApiClient(config))

data = api.download_threat_feed_phishing_sample()   # bytes
with open("downloadThreatFeedPhishingSample.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to downloadThreatFeedPhishingSample.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesThreatFeedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesThreatFeedApi(config);

async function main() {
  const result = await api.downloadThreatFeedPhishingSample({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Download a sample of the phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing/sample)
// Parameters for downloadThreatFeedPhishingSample (GET /v3.4/download/threat-feed/phishing/sample):
//   (no parameters; the API key is set on the client)
package main

import (
    "context"
    "fmt"
    "os"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    // returns raw bytes (compressed/binary file) -- write to disk
    data, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedPhishingSample(ctx).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("downloadThreatFeedPhishingSample.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to downloadThreatFeedPhishingSample.gz\n", len(data))
}

```

</details>

---

## Download the daily malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware`

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | Feed date (yyyy-MM-dd); defaults to latest available |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Download the daily malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_threat_feed_api import DatabasesThreatFeedApi

# Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
#   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesThreatFeedApi(ApiClient(config))

data = api.download_threat_feed_malware(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("downloadThreatFeedMalware.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to downloadThreatFeedMalware.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Download the daily malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware)
// Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import { Configuration, DatabasesThreatFeedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesThreatFeedApi(config);

async function main() {
  const result = await api.downloadThreatFeedMalware({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Download the daily malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware)
// Parameters for downloadThreatFeedMalware (GET /v3.4/download/threat-feed/malware):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
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
    data, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedMalware(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("downloadThreatFeedMalware.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to downloadThreatFeedMalware.gz\n", len(data))
}

```

</details>

---

## Download a sample of the malware threat feed (CSV)

`GET /v3.4/download/threat-feed/malware/sample`

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Download a sample of the malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware/sample).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_threat_feed_api import DatabasesThreatFeedApi

# Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesThreatFeedApi(ApiClient(config))

data = api.download_threat_feed_malware_sample()   # bytes
with open("downloadThreatFeedMalwareSample.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to downloadThreatFeedMalwareSample.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Download a sample of the malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware/sample)
// Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesThreatFeedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesThreatFeedApi(config);

async function main() {
  const result = await api.downloadThreatFeedMalwareSample({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Download a sample of the malware threat feed (CSV) (GET /v3.4/download/threat-feed/malware/sample)
// Parameters for downloadThreatFeedMalwareSample (GET /v3.4/download/threat-feed/malware/sample):
//   (no parameters; the API key is set on the client)
package main

import (
    "context"
    "fmt"
    "os"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    // returns raw bytes (compressed/binary file) -- write to disk
    data, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedMalwareSample(ctx).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("downloadThreatFeedMalwareSample.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to downloadThreatFeedMalwareSample.gz\n", len(data))
}

```

</details>

---

## Download the daily spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam`

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|
| `date` | query | no | string | Feed date (yyyy-MM-dd); defaults to latest available |

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from datetime import date, timedelta
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_threat_feed_api import DatabasesThreatFeedApi

# Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
#   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesThreatFeedApi(ApiClient(config))

data = api.download_threat_feed_spam(var_date=str(date.today() - timedelta(days=1)))   # bytes
with open("downloadThreatFeedSpam.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to downloadThreatFeedSpam.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import { Configuration, DatabasesThreatFeedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesThreatFeedApi(config);

async function main() {
  const result = await api.downloadThreatFeedSpam({ date: new Date(Date.now()-86400000).toISOString().slice(0,10) });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
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
    data, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedSpam(ctx).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("downloadThreatFeedSpam.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to downloadThreatFeedSpam.gz\n", len(data))
}

```

</details>

---

## Download a sample of the spam threat feed (CSV)

`GET /v3.4/download/threat-feed/spam/sample`

**Parameters**

| Parameter | In | Required | Type | Description |
|-----------|----|----------|------|-------------|

**Usage**

<details><summary>Python</summary>

```python
"""Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample).
Returns raw bytes (a compressed/binary file) -- write to disk, do not print."""
from whoisfreaks import Configuration, ApiClient
from whoisfreaks.api.databases_threat_feed_api import DatabasesThreatFeedApi

# Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
#   (no parameters; the API key is set on the client)
config = Configuration()
config.api_key["ApiKeyAuth"] = "YOUR_API_KEY"   # set once
api = DatabasesThreatFeedApi(ApiClient(config))

data = api.download_threat_feed_spam_sample()   # bytes
with open("downloadThreatFeedSpamSample.gz", "wb") as f:
    f.write(data)
print(f"saved {len(data)} bytes to downloadThreatFeedSpamSample.gz")

```

</details>

<details><summary>TypeScript</summary>

```typescript
// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
import { Configuration, DatabasesThreatFeedApi } from "whoisfreaks";

const config = new Configuration({ apiKey: "YOUR_API_KEY" });  // set once
const api = new DatabasesThreatFeedApi(config);

async function main() {
  const result = await api.downloadThreatFeedSpamSample({  });
  console.log(result);
}
main().catch(console.error);

```

</details>

<details><summary>Go</summary>

```go
// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
package main

import (
    "context"
    "fmt"
    "os"
    wf "github.com/WhoisFreaks/whoisfreaks-go"
)

func main() {
    cfg := wf.NewConfiguration()
    client := wf.NewAPIClient(cfg)
    // apiKey is set once via the request context
    ctx := context.WithValue(context.Background(), wf.ContextAPIKeys,
        map[string]wf.APIKey{"ApiKeyAuth": {Key: "YOUR_API_KEY"}})
    // returns raw bytes (compressed/binary file) -- write to disk
    data, _, err := client.DatabasesThreatFeedAPI.DownloadThreatFeedSpamSample(ctx).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("downloadThreatFeedSpamSample.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to downloadThreatFeedSpamSample.gz\n", len(data))
}

```

</details>

---
