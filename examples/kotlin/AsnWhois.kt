// Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
// Parameters for asnWhois (GET /v2.0/asn-whois):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - asn (string, required)
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.ASNWHOISApi

fun main() {
    val api = ASNWHOISApi(basePath = "https://api.whoisfreaks.com")
    val result = api.AsnWhois("YOUR_API_KEY", "AS15169", null)
    println(result)  // status via api.AsnWhoisWithHttpInfo(...).statusCode
}
