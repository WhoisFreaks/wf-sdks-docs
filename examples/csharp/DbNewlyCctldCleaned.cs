// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbNewlyCctldCleaned {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesNewlyRegisteredApi(config);
        var result = api.DbNewlyCctldCleaned(DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine(result);
    }
}
