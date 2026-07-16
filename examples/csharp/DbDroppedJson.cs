// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbDroppedJson {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesExpiringDroppedApi(config);
        var result = api.DbDroppedJson(DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"), null);
        Console.WriteLine(result);
    }
}
