// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbIpSecurityStatus {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesIPSecurityApi(config);
        var resp = api.DbIpSecurityStatusWithHttpInfo("YOUR_API_KEY");
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}
