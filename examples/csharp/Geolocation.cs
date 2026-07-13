// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class Geolocation {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        var api = new GeolocationApi(config);
        var resp = api.GeolocationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
        Console.WriteLine($"status: {(int)resp.StatusCode}");
        Console.WriteLine(resp.Data);
    }
}
