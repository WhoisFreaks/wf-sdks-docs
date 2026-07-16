// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class Geolocation {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new GeolocationApi(config);
        var result = api.Geolocation("8.8.8.8");
        Console.WriteLine(result);
    }
}
