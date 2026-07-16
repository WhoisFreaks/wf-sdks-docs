// Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
// Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbIpCityStatus {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesIPGeolocationApi(config);
        var result = api.DbIpCityStatus();
        Console.WriteLine(result);
    }
}
