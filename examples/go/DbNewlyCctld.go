// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
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
    data, _, err := client.DatabasesNewlyRegisteredAPI.DbNewlyCctld(context.Background()).ApiKey("YOUR_API_KEY").Whois(false).Date(time.Now().AddDate(0,0,-1).Format("2006-01-02")).Execute()
    if err != nil { panic(err) }
    if err := os.WriteFile("dbNewlyCctld.gz", data, 0644); err != nil { panic(err) }
    fmt.Printf("saved %d bytes to dbNewlyCctld.gz\n", len(data))
}
