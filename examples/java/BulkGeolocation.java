// Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
// Parameters for bulkGeolocation (POST /v1.0/geolocation):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.GeolocationApi;
import com.whoisfreaks.client.model.BulkGeolocationRequest;

public class BulkGeolocation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        GeolocationApi api = new GeolocationApi(client);
        var resp = api.bulkGeolocationWithHttpInfo("YOUR_API_KEY", new BulkGeolocationRequest());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
