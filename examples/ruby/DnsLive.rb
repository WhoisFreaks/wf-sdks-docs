# Runnable example: Live DNS Lookup (GET /v2.0/dns/live)
# Parameters for dnsLive (GET /v2.0/dns/live):
#   - domainName (string, required)
#   - ipAddress (string, required): Use for PTR lookups
#   - type (string, required): all or comma-separated: A,MX,NS,TXT,SOA,SPF,AAAA,CNAME
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DNSApi.new
result = api.dns_live("example.com", "8.8.8.8", "value")
puts result
