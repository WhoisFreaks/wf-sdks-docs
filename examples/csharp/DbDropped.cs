// Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
// Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbDropped {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesExpiringDroppedApi(config);
        var resp = api.DbDroppedWithHttpInfo("YOUR_API_KEY", false, DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}
