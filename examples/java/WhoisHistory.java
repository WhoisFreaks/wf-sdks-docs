// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisHistory {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        WhoisApi api = new WhoisApi(client);
        var resp = api.whoisHistoryWithHttpInfo("YOUR_API_KEY", "example.com", null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
