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
