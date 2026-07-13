// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

class BulkWhois {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new WHOISApi(config);
        var resp = api.BulkWhoisWithHttpInfo("YOUR_API_KEY", new BulkWhoisRequest(), null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}
