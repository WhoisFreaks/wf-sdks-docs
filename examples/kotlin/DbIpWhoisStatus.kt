// Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
// Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.DatabasesIPWHOISApi

fun main() {
    val api = DatabasesIPWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dbIpWhoisStatus("YOUR_API_KEY")
    println(result)  // status via api.dbIpWhoisStatusWithHttpInfo(...).statusCode
}
