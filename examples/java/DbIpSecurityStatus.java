// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpSecurityApi;

public class DbIpSecurityStatus {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpSecurityApi api = new DatabasesIpSecurityApi(client);
        var resp = api.dbIpSecurityStatusWithHttpInfo("YOUR_API_KEY");
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
