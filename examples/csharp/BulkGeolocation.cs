// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - body: BulkGeolocationRequest (required) -- request body object
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;
using WhoisFreaks.Model;

class BulkGeolocation {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new GeolocationApi(config);
        var result = api.BulkGeolocation(new BulkGeolocationRequest());
        Console.WriteLine(result);
    }
}
