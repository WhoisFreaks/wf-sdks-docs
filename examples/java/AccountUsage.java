// Runnable example: Account Usage (GET /v1.0/whoisapi/usage)
// Parameters for accountUsage (GET /v1.0/whoisapi/usage):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AccountApi;

public class AccountUsage {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        AccountApi api = new AccountApi(client);
        var resp = api.accountUsageWithHttpInfo("YOUR_API_KEY");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
