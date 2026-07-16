// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbIpSecurity {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DatabasesIPSecurityApi(config);
        var result = api.DbIpSecurity(DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"));
        Console.WriteLine(result);
    }
}
