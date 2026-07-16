// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import com.whoisfreaks.client.apis.DNSApi
import com.whoisfreaks.client.infrastructure.ApiClient

fun main() {
    ApiClient.apiKey["apiKey"] = "YOUR_API_KEY"  // set once
    val api = DNSApi()
    val result = api.dnsLive("example.com", "8.8.8.8", "value", null)
    println(result)
}
