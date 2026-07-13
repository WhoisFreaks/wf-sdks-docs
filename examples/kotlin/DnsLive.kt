// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.api.DNSApi

fun main() {
    val api = DNSApi(basePath = "https://api.whoisfreaks.com")
    val result = api.dnsLive("YOUR_API_KEY", "example.com", "8.8.8.8", "value", null)
    println(result)  // status via api.dnsLiveWithHttpInfo(...).statusCode
}
