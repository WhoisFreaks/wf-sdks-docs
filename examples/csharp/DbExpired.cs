// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbExpired {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesExpiringDroppedApi(config);
        var result = api.DbExpired(false, DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine(result);
    }
}
