// Runnable example: Newly Registered gTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/gtld/cleaned)
// Parameters for dbNewlyGtldCleaned (GET /v3.1/download/domainer/gtld/cleaned):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesNewlyRegisteredApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesNewlyRegisteredApi()
    val result = api.dbNewlyGtldCleaned(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}
