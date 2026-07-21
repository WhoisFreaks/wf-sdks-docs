// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DownloadThreatFeedSpamSample {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesThreatFeedApi(config);
        var result = api.DownloadThreatFeedSpamSample();
        Console.WriteLine(result);
    }
}
