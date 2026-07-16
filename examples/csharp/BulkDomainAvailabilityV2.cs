// Runnable example: Bulk Domain Availability Check (POST /v2.0/domain/availability)
// Parameters for bulkDomainAvailabilityV2 (POST /v2.0/domain/availability):
//   - domain (string, optional): Required for TLD-mode bulk check (base domain).
//   - format (string (one of: json, xml), optional)
//   - body: BulkDomainAvailabilityRequest (required) -- request body object
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

class BulkDomainAvailabilityV2 {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DomainAvailabilityApi(config);
        var result = api.BulkDomainAvailabilityV2(new BulkDomainAvailabilityRequest(), null, null);
        Console.WriteLine(result);
    }
}
