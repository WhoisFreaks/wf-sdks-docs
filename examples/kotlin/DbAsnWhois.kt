// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - date (string, required)
import com.whoisfreaks.client.apis.DatabasesASNWHOISApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DatabasesASNWHOISApi()
    val result = api.dbAsnWhois(java.time.LocalDate.now().minusDays(1).toString())
    println(result)
}
