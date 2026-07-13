// Runnable example: Newly Registered ccTLD Cleaned WHOIS (CSV) (GET /v3.1/download/domainer/cctld/cleaned)
// Parameters for dbNewlyCctldCleaned (GET /v3.1/download/domainer/cctld/cleaned):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesNewlyRegisteredApi

fun main() {
    val api = DatabasesNewlyRegisteredApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbNewlyCctldCleaned("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbNewlyCctldCleanedWithHttpInfo(...).statusCode
}
