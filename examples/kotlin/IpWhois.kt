// Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
// Parameters for ipWhois (GET /v1.0/ip-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - ip (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.IPWHOISApi

fun main() {
    val api = IPWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.ipWhois("YOUR_API_KEY", "8.8.8.8", null)
    println(result)  // status via api.ipWhoisWithHttpInfo(...).statusCode
}
