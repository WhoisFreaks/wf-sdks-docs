// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbNewlyGtld {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesNewlyRegisteredApi(config);
        var result = api.DbNewlyGtld(false, DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"), null);
        Console.WriteLine(result);
    }
}
