// Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
// Parameters for whoisHistory (GET /v2.0/whois/history):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required): Domain to fetch historical WHOIS records for
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.WHOISApi

fun main() {
    val api = WHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.whoisHistory("YOUR_API_KEY", "example.com", null, null)
    println(result)  // status via api.whoisHistoryWithHttpInfo(...).statusCode
}
