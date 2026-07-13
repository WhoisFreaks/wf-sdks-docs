// Runnable example: SSL Certificate Lookup (GET /v1.0/ssl/live)
// Parameters for sslLookup (GET /v1.0/ssl/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - chain (boolean, optional)
//   - sslRaw (boolean, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.SSLApi

fun main() {
    val api = SSLApi(basePath = "https://api.whoisfreaks.com")
    val result = api.SslLookup("YOUR_API_KEY", "example.com", null, null, null)
    println(result)  // status via api.SslLookupWithHttpInfo(...).statusCode
}
