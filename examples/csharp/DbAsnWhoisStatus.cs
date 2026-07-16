// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbAsnWhoisStatus {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesASNWHOISApi(config);
        var result = api.DbAsnWhoisStatus();
        Console.WriteLine(result);
    }
}
