// Runnable example: Download the daily phishing threat feed (CSV) (GET /v3.4/download/threat-feed/phishing)
// Parameters for downloadThreatFeedPhishing (GET /v3.4/download/threat-feed/phishing):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;

public class DownloadThreatFeedPhishing {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);
        var result = api.downloadThreatFeedPhishing(java.time.LocalDate.now().minusDays(1).toString());
        System.out.println(result);
    }
}
