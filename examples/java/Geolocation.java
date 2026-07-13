// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.GeolocationApi;

public class Geolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        GeolocationApi api = new GeolocationApi(client);
        var resp = api.geolocationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
