// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesExpiringDroppedApi()
    val result = api.dbExpired(false, java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}
