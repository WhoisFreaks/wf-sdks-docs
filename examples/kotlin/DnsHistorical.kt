// Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
// Parameters for dnsHistorical (GET /v2.0/dns/historical):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - type (string, required)
//   - page (integer, optional)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.DNSApi

fun main() {
    val api = DNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dnsHistorical("YOUR_API_KEY", "example.com", "value", null, null)
    println(result)  // status via api.dnsHistoricalWithHttpInfo(...).statusCode
}
