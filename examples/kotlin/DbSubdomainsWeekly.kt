// Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
// Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesSubdomainsApi

fun main() {
    val api = DatabasesSubdomainsApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbSubdomainsWeekly("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbSubdomainsWeeklyWithHttpInfo(...).statusCode
}
