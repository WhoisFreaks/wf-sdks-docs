// Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
// Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;

public class DbIpCity {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);
        var resp = api.dbIpCityWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
