// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   - apiKey (string, required): Your WHOISFreaks API key
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class RotateApiKey {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new AccountApi(config);
        var resp = api.RotateApiKeyWithHttpInfo("YOUR_API_KEY");
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}
