// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;

public class IpReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        IpReputationApi api = new IpReputationApi(client);
        var resp = api.ipReputationWithHttpInfo("YOUR_API_KEY", "8.8.8.8");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
