// Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
// Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesExpiringDroppedApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesExpiringDroppedApi()
    val result = api.dbExpiredCleaned(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}
