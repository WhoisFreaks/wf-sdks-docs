# Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
# Parameters for dnsHistorical (GET /v2.0/dns/historical):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - type (string, required)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::DNSApi.new
data, status, _headers = api.dns_historical_with_http_info("YOUR_API_KEY", "example.com", "value")
puts "status: #{status}"
puts data
