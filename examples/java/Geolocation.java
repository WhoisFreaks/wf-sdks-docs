// Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
// Parameters for geolocation (GET /v1.0/geolocation):
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.GeolocationApi;

public class Geolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        GeolocationApi api = new GeolocationApi(client);
        var result = api.geolocation("8.8.8.8");
        System.out.println(result);
    }
}
