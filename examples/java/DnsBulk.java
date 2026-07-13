// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DnsApi;
import com.whoisfreaks.client.model.DnsBulkRequest;

public class DnsBulk {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DnsApi api = new DnsApi(client);
        var resp = api.dnsBulkWithHttpInfo("YOUR_API_KEY", "value", new DnsBulkRequest(), null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
