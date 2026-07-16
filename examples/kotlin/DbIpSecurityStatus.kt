// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   (no parameters; the API key is set on the client)
import com.whoisfreaks.client.apis.DatabasesIPSecurityApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesIPSecurityApi()
    val result = api.dbIpSecurityStatus()
    println(result)
}
