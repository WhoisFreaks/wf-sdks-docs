// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;

public class DownloadThreatFeedSpam {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);
        var result = api.downloadThreatFeedSpam(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}
