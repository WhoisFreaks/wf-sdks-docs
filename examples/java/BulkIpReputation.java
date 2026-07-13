// Runnable example: Bulk IP Reputation (POST /v1.0/security)
// Parameters for bulkIpReputation (POST /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - body: BulkGeolocationRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.IpReputationApi;
import com.whoisfreaks.client.model.BulkGeolocationRequest;

public class BulkIpReputation {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        IpReputationApi api = new IpReputationApi(client);
        var resp = api.bulkIpReputationWithHttpInfo("YOUR_API_KEY", new BulkGeolocationRequest());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
