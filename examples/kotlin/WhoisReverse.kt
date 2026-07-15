// Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
// Parameters for whoisReverse (GET /v2.0/whois/reverse):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - keyword (string, required): Keyword to search across WHOIS records
//   - page (integer, optional): Page number
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.WHOISApi

fun main() {
    val api = WHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.whoisReverse("YOUR_API_KEY", "value", null, null)
    println(result)  // status via api.whoisReverseWithHttpInfo(...).statusCode
}
