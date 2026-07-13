// Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
// Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - whois (boolean, optional)
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesExpiringDroppedApi

fun main() {
    val api = DatabasesExpiringDroppedApi(basePath = "https://api.whoisfreaks.com")
    val result = api.DbDroppedBacklinks("YOUR_API_KEY", false, java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.DbDroppedBacklinksWithHttpInfo(...).statusCode
}
