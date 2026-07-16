// Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
// Parameters for dnsLive (GET /v2.0/dns/live):
//   - domainName (string, required)
//   - ipAddress (string, required): Use for PTR lookups
//   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
//   - format (string (one of: json, xml), optional)
using System;
using WhoisFreaks.Api;
using WhoisFreaks.Client;

class DnsLive {
    static void Main() {
        var config = new Configuration { BasePath = "https://api.whoisfreaks.com" };
        config.AddApiKey("ApiKeyAuth", "YOUR_API_KEY");  // set once
        var api = new DNSApi(config);
        var result = api.DnsLive("example.com", "8.8.8.8", "value", null);
        Console.WriteLine(result);
    }
}
