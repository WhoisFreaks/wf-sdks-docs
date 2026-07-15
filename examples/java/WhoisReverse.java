// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisReverse {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        WhoisApi api = new WhoisApi(client);
        var resp = api.whoisReverseWithHttpInfo("YOUR_API_KEY", "value", null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
