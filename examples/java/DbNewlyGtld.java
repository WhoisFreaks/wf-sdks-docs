// Runnable example: Newly Registered gTLD (CSV) (GET /v3.1/download/domainer/gtld)
// Parameters for dbNewlyGtld (GET /v3.1/download/domainer/gtld):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyGtld {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var resp = api.dbNewlyGtldWithHttpInfo("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
