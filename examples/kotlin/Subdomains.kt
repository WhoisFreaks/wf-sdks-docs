// Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
// Parameters for subdomains (GET /v1.0/subdomains):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domain (string, required)
//   - after (string, optional)
//   - before (string, optional)
//   - status (string (one of: active, inactive), optional)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.SubdomainsApi

fun main() {
    val api = SubdomainsApi(basePath = "https://api.whoisfreaks.com")
    val result = api.subdomains("YOUR_API_KEY", "example.com", "2000-01-01", java.time.LocalDate.now().toString(), null, null, null)
    println(result)  // status via api.subdomainsWithHttpInfo(...).statusCode
}
