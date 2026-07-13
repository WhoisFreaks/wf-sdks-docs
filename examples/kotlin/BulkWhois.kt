// Runnable example: Bulk WHOIS Lookup (POST /v2.0/bulkwhois/live)
// Parameters for bulkWhois (POST /v2.0/bulkwhois/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - format (string (one of: json, xml), optional)
//   - body: BulkWhoisRequest (required) -- request body object
import com.whoisfreaks.api.WHOISApi
import com.whoisfreaks.models.BulkWhoisRequest

fun main() {
    val api = WHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.bulkWhois("YOUR_API_KEY", BulkWhoisRequest(), null)
    println(result)  // status via api.bulkWhoisWithHttpInfo(...).statusCode
}
