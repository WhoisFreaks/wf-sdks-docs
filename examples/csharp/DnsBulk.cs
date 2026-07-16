// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

class DnsBulk {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DNSApi(config);
        var result = api.DnsBulk("value", new DnsBulkRequest(), null);
        Console.WriteLine(result);
    }
}
