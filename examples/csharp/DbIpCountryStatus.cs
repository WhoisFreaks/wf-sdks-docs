// Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
// Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
//   - apiKey (string, required): Your WHOISFreaks API key
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbIpCountryStatus {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesIPGeolocationApi(config);
        var resp = api.DbIpCountryStatusWithHttpInfo("YOUR_API_KEY");
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}
