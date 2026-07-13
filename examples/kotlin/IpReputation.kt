// Runnable example: IP Reputation Lookup (GET /v1.0/security)
// Parameters for ipReputation (GET /v1.0/security):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
import com.whoisfreaks.api.IPReputationApi

fun main() {
    val api = IPReputationApi(basePath = "https://api.whoisfreaks.com")
    val result = api.IpReputation("YOUR_API_KEY", "8.8.8.8")
    println(result)  // status via api.IpReputationWithHttpInfo(...).statusCode
}
