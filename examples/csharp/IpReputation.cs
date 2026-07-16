// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - ip (string, required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class IpReputation {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new IPReputationApi(config);
        var result = api.IpReputation("8.8.8.8");
        Console.WriteLine(result);
    }
}
