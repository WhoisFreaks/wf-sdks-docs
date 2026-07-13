// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesIpSecurityApi;

public class DbIpSecurity {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesIpSecurityApi api = new DatabasesIpSecurityApi(client);
        var resp = api.dbIpSecurityWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
