// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
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
    data, _, err := client.DatabasesIPGeolocationAPI.DbIpCity(context.Background()).ApiKey("YOUR_API_KEY").Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbIpCity.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbIpCity.gz\n", len(data))
}
