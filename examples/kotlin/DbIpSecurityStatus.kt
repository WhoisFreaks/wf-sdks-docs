// Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
// Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.DatabasesIPSecurityApi

fun main() {
    val api = DatabasesIPSecurityApi(basePath = "https://api.whoisfreaks.com")
    val result = api.DbIpSecurityStatus("YOUR_API_KEY")
    println(result)  // status via api.DbIpSecurityStatusWithHttpInfo(...).statusCode
}
