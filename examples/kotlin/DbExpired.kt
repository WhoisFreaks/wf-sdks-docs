// Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
// Parameters for dbExpired (GET /v3.1/download/domainer/expired):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, required)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesExpiringDroppedApi

fun main() {
    val api = DatabasesExpiringDroppedApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbExpired("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbExpiredWithHttpInfo(...).statusCode
}
