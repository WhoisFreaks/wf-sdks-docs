// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - apiKey (string, required): Your WHOISFreaks API key
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
import WhoisFreaks

DNSAPI.DnsLive(apiKey: "YOUR_API_KEY", domainName: "example.com", ipAddress: "8.8.8.8", type: "value", format: nil) { data, error in
    if let error = error { print(error); return }
    if let data = data { print(data) }
}
