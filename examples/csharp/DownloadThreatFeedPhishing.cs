// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DownloadThreatFeedPhishing {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesThreatFeedApi(config);
        var result = api.DownloadThreatFeedPhishing(DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine(result);
    }
}
