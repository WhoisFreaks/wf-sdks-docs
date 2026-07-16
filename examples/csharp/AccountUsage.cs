// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class AccountUsage {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new AccountApi(config);
        var result = api.AccountUsage();
        Console.WriteLine(result);
    }
}
