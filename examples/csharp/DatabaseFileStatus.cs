// Runnable example: Database File Status (Public) (GET /v3.4/status)
// Parameters for databaseFileStatus (GET /v3.4/status):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DatabaseFileStatus {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new AccountApi(config);
        var result = api.DatabaseFileStatus();
        Console.WriteLine(result);
    }
}
