// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.AsnWhoisApi;

public class AsnWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        AsnWhoisApi api = new AsnWhoisApi(client);
        var resp = api.asnWhoisWithHttpInfo("YOUR_API_KEY", "AS15169", null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
