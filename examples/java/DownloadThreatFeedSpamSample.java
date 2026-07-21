// Runnable example: Download a sample of the spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam/sample)
// Parameters for downloadThreatFeedSpamSample (GET /v3.4/download/threat-feed/spam/sample):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.DatabasesThreatFeedApi;

public class DownloadThreatFeedSpamSample {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        DatabasesThreatFeedApi api = new DatabasesThreatFeedApi(client);
        var result = api.downloadThreatFeedSpamSample();
        System.out.println(result);
    }
}
