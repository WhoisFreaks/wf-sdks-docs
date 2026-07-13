// Runnable example: Newly Registered gTLD (JSON) (GET /v3.1/domains/newly/gtld)
// Parameters for dbNewlyGtldJson (GET /v3.1/domains/newly/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DbNewlyGtldJson {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new DatabasesNewlyRegisteredApi(config);
        var resp = api.DbNewlyGtldJsonWithHttpInfo("YOUR_API_KEY", DateTime.UtcNow.AddDays(-1).ToString("yyyy-MM-dd"), null);
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}
