// Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
// Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesIpGeolocationApi;

public class DbIpCountry {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesIpGeolocationApi api = new DatabasesIpGeolocationApi(client);
        var result = api.dbIpCountry(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}
