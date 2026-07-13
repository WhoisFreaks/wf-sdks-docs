// Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
// Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.ApiClient;
import com.whoisfreaks.client.Configuration;
import com.whoisfreaks.client.api.DatabasesDnsApi;

public class DbDnsWeekly {
    public static void main(String[] args) throws Exception {
        ApiClient client = Configuration.getDefaultApiClient();
        client.setBasePath("https://api.whoisfreaks.com");
        DatabasesDnsApi api = new DatabasesDnsApi(client);
        var resp = api.dbDnsWeeklyWithHttpInfo("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString());
        System.out.println("status: " + resp.getStatusCode());
        System.out.println(resp.getData());
    }
}
