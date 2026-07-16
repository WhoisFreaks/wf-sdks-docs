// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.auth.ApiKeyAuth;
import com.whoisfreaks.client.api.IpWhoisApi;

public class IpWhois {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        ((ApiKeyAuth) client.getAuthentication("ApiKeyAuth")).setApiKey("YOUR_API_KEY");  // set once
        IpWhoisApi api = new IpWhoisApi(client);
        var result = api.ipWhois("8.8.8.8", null);
        System.out.println(result);
    }
}
