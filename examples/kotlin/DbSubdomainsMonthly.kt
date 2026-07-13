// Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
// Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesSubdomainsApi

fun main() {
    val api = DatabasesSubdomainsApi(basePath = "https://api.whoisfreaks.com")
    val result = api.DbSubdomainsMonthly("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.DbSubdomainsMonthlyWithHttpInfo(...).statusCode
}
