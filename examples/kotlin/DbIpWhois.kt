// Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
// Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.api.DatabasesIPWHOISApi

fun main() {
    val api = DatabasesIPWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpWhois("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbIpWhoisWithHttpInfo(...).statusCode
}
