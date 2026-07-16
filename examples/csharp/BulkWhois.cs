// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

class BulkWhois {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new WHOISApi(config);
        var result = api.BulkWhois(new BulkWhoisRequest(), null);
        Console.WriteLine(result);
    }
}
