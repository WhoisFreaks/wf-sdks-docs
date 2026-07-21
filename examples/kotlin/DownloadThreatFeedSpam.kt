// Runnable example: Download the daily spam threat feed (CSV) (GET /v3.4/download/threat-feed/spam)
// Parameters for downloadThreatFeedSpam (GET /v3.4/download/threat-feed/spam):
//   - date (string, optional): Feed date (yyyy-MM-dd); defaults to latest available
import com.whoisfreaks.client.apis.DatabasesThreatFeedApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesThreatFeedApi()
    val result = api.downloadThreatFeedSpam(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}
