// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbNewlyDns {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesNewlyRegisteredApi(config);
        var result = api.DbNewlyDns(DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine(result);
    }
}
