// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.SSLApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = SSLApi()
    val result = api.sslLookup("example.com", null, null, null)
    println(result)
}
