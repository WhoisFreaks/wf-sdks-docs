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
