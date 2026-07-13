// Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
// Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesExpiringDroppedApi;

public class DbDroppedJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesExpiringDroppedApi api = new DatabasesExpiringDroppedApi(client);
        var resp = api.dbDroppedJsonWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
