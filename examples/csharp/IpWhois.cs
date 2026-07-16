// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class IpWhois {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new IPWHOISApi(config);
        var result = api.IpWhois("8.8.8.8", null);
        Console.WriteLine(result);
    }
}
