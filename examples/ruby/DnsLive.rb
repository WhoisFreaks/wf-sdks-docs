# Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
# Parameters for dnsLive (GET /v2.0/dns/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - ipAddress (string, required): Use for PTR lookups
#   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::DNSApi.new
data, status, _headers = api.dns_live_with_http_info("YOUR_API_KEY", "example.com", "8.8.8.8", "value")
puts "status: #{status}"
puts data
