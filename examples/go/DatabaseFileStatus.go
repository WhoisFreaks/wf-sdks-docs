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
