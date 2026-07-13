// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.api.DatabasesIPSecurityApi

fun main() {
    val api = DatabasesIPSecurityApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpSecurity("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.dbIpSecurityWithHttpInfo(...).statusCode
}
