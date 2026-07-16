// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbSubdomainsMonthly {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesSubdomainsApi(config);
        var result = api.DbSubdomainsMonthly(DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine(result);
    }
}
