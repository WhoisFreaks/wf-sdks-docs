// Runnable example: Newly Registered ccTLD (JSON) (GET /v3.1/domains/newly/cctld)
// Parameters for dbNewlyCctldJson (GET /v3.1/domains/newly/cctld):
//   - date (string, optional): yyyy-MM-dd; omit for latest
//   - tlds (string, optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesNewlyRegisteredApi;

public class DbNewlyCctldJson {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesNewlyRegisteredApi api = new DatabasesNewlyRegisteredApi(client);
        var result = api.dbNewlyCctldJson(java.time.LocalDate.now().minusDays(1).toString(), null);
        System.out.println(result);
    }
}
