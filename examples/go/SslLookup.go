// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
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
    result, _, err := client.SSLAPI.SslLookup(ctx).DomainName("example.com").Execute()
    if err != nil { panic(err) }
    b, _ := json.MarshalIndent(result, "", "  ")
    fmt.Println(string(b))
}
