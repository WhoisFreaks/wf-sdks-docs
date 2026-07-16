// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import com.whoisfreaks.client.apis.WHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient
import com.whoisfreaks.client.models.BulkWhoisRequest

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = WHOISApi()
    val result = api.bulkWhois(BulkWhoisRequest(), null)
    println(result)
}
