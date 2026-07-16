// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbIpCountryStatus {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesIPGeolocationApi(config);
        var result = api.DbIpCountryStatus();
        Console.WriteLine(result);
    }
}
