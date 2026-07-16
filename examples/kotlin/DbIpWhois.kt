// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesIPWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPWHOISApi()
    val result = api.dbIpWhois(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}
