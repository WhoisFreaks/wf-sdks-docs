// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.client.apis.DatabasesSubdomainsApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesSubdomainsApi()
    val result = api.dbSubdomainsMonthly(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}
