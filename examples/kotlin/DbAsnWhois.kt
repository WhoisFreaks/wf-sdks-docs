// Runnable example: ASN WHOIS Snapshot (GET /v3.3/download/snapshot/asn/whois)
// Parameters for dbAsnWhois (GET /v3.3/download/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - date (string, required)
import com.whoisfreaks.api.DatabasesASNWHOISApi

fun main() {
    val api = DatabasesASNWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.DbAsnWhois("YOUR_API_KEY", java.time.LocalDate.now().minusDays(1).toString())
    println(result)  // status via api.DbAsnWhoisWithHttpInfo(...).statusCode
}
