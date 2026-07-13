# Authentication

Every WhoisFreaks API request requires an **API key**, passed as the `apiKey`
query parameter. Each SDK exposes a configuration hook so you set the key once
and it is attached to every request automatically.

## Get an API key

1. Sign in at <https://billing.whoisfreaks.com>.
2. Copy your API key from the dashboard.
3. Keep it secret — do **not** commit it to source control. Prefer an
   environment variable (e.g. `WHOISFREAKS_API_KEY`).

## Base URLs

| Purpose | Base URL |
|---------|----------|
| Live API lookups | `https://api.whoisfreaks.com` |
| Database file downloads | `https://files.whoisfreaks.com` |

## Setting the key per language

### Python

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

### JavaScript

```javascript
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
// whoisfreaks-js is CommonJS (no Configuration class; apiKey is positional)
import pkg from "whoisfreaks-js";
const { ApiClient, WHOISApi } = pkg;
// or:  const { ApiClient, WHOISApi } = require("whoisfreaks-js");

const api = new WHOISApi();   // uses ApiClient.instance

api.whoisLive("YOUR_API_KEY", "example.com")
  .then(data => console.log(data))
  .catch(err => console.error(err));

```

### TypeScript

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

### Java

```java
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisLive {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        WhoisApi api = new WhoisApi(client);
        var resp = api.whoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}

```

### Kotlin

```kotlin
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.WHOISApi

fun main() {
    val api = WHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.whoisLive("YOUR_API_KEY", "example.com", null)
    println(result)  // status via api.whoisLiveWithHttpInfo(...).statusCode
}

```

### C# / .NET

```csharp
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class WhoisLive {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new WHOISApi(config);
        var resp = api.WhoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}

```

### Ruby

```ruby
# Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
# Parameters for whoisLive (GET /v2.0/whois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.whois_live_with_http_info("YOUR_API_KEY", "example.com")
puts "status: #{status}"
puts data

```

### Go

```go
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
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
    // apiKey is a builder method on the request, not a config/context value
    result, httpRes, err := client.WHOISAPI.WhoisLive(context.Background()).ApiKey("YOUR_API_KEY").DomainName("example.com").Execute()
    if err != nil { panic(err) }
    fmt.Println("status:", httpRes.StatusCode)
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}

```

### Swift

```swift
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

do {
    let result = try await WHOISAPI.whoisLive(apiKey: "YOUR_API_KEY", domainName: "example.com", format: nil)
    print(result)
} catch {
    print(error)
}

```

### PHP

```php
<?php
// Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
// Parameters for whoisLive (GET /v2.0/whois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - format (string (one of: json, xml), optional)
require 'vendor/autoload.php';

$config = WhoisFreaks\Configuration::getDefaultConfiguration();
$api = new WhoisFreaks\Api\WHOISApi(new GuzzleHttp\Client(), $config);
list($data, $statusCode, $headers) = $api->whoisLiveWithHttpInfo("YOUR_API_KEY", "example.com", null);
echo "status: " . $statusCode . PHP_EOL;
print_r($data);

```
