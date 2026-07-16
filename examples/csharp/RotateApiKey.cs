// Runnable example: Rotate API Key (GET /v1.0/api-key/rotate)
// Parameters for rotateApiKey (GET /v1.0/api-key/rotate):
//   (no parameters; the API key is set on the client)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class RotateApiKey {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new AccountApi(config);
        var result = api.RotateApiKey();
        Console.WriteLine(result);
    }
}
