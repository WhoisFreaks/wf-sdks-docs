// Runnable example: ASN WHOIS Snapshot Status (GET /v3.3/status/snapshot/asn/whois)
// Parameters for dbAsnWhoisStatus (GET /v3.3/status/snapshot/asn/whois):
//   - apiKey (string, required): Your WHOISFreaks API key
import com.whoisfreaks.api.DatabasesASNWHOISApi

fun main() {
    val api = DatabasesASNWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.DbAsnWhoisStatus("YOUR_API_KEY")
    println(result)  // status via api.DbAsnWhoisStatusWithHttpInfo(...).statusCode
}
