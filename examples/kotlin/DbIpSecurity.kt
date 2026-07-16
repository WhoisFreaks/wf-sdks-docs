// Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
// Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesIPSecurityApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPSecurityApi()
    val result = api.dbIpSecurity(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}
