// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
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
    // returns raw bytes (compressed/binary file) -- write to disk
    data, _, err := client.DatabasesExpiringDroppedAPI.DbExpiredCleaned(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbExpiredCleaned.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbExpiredCleaned.gz\n", len(data))
}
