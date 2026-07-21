// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DownloadThreatFeedSpam {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesThreatFeedApi(config);
        var result = api.DownloadThreatFeedSpam(DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine(result);
    }
}
