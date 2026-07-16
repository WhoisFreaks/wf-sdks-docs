// Runnable example: Bulk DNS Lookup (POST /v2.0/dns/bulk/live)
// Parameters for dnsBulk (POST /v2.0/dns/bulk/live):
//   - type (string, required)
//   - format (string (one of: json, xml), optional)
//   - body: DnsBulkRequest (required) -- request body object
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.DnsBulkRequest

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DNSApi()
    val result = api.dnsBulk("value", DnsBulkRequest(), null)
    println(result)
}
