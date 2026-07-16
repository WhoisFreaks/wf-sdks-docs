// Runnable example: Typosquatting Lookup (GET /v3.0/domain/typos)
// Parameters for typosquatting (GET /v3.0/domain/typos):
//   - keyword (string, optional)
//   - pattern (string, optional)
//   - pageToken (string, optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class Typosquatting {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new TyposquattingApi(config);
        var result = api.Typosquatting(null, null, null);
        Console.WriteLine(result);
    }
}
