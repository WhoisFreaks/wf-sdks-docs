// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import com.whoisfreaks.api.DNSApi
import com.whoisfreaks.models.DnsBulkRequest

fun main() {
    val api = DNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dnsBulk("YOUR_API_KEY", "value", DnsBulkRequest(), null)
    println(result)  // status via api.dnsBulkWithHttpInfo(...).statusCode
}
