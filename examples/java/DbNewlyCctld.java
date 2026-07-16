// Runnable example: Newly Registered ccTLD (CSV) (GET /v3.1/download/domainer/cctld)
// Parameters for dbNewlyCctld (GET /v3.1/download/domainer/cctld):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyCctld {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var result = api.dbNewlyCctld(false, java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println(result);
    }
}
