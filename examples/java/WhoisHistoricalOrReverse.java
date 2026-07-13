// Runnable example: WHOIS Historical or Reverse Lookup (GET /v1.0/whois)
// Parameters for whoisHistoricalOrReverse (GET /v1.0/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (string (one of: historical, reverse), required)
//   - domainName (string, required): Required for historical lookup
//   - keyword (string, optional): For reverse — domain keyword search
//   - email (string, optional): For reverse — registrant email search
//   - owner (string, optional): For reverse — registrant name search
//   - company (string, optional): For reverse — company name search
//   - mode (string (one of: default, mini), optional)
//   - exact (boolean, optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.WhoisApi;

public class WhoisHistoricalOrReverse {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        WhoisApi api = new WhoisApi(client);
        var resp = api.whoisHistoricalOrReverseWithHttpInfo("YOUR_API_KEY", "historical", "example.com", true, null, null, null, null, null, null, null);
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
