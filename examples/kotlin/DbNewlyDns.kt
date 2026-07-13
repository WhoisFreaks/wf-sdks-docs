// Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
// Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, optional): yyyy-MM-dd; omit for latest
import com.whoisfreaks.api.DatabasesNewlyRegisteredApi

fun main() {
    val api = DatabasesNewlyRegisteredApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbNewlyDns("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbNewlyDnsWithHttpInfo(...).statusCode
}
