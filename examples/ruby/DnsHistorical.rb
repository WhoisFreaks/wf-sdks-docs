# Runnable example: Historical DNS Lookup (GET /v2.0/dns/historical)
# Parameters for dnsHistorical (GET /v2.0/dns/historical):
#   - domainName (string, required)
#   - type (string, required)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DNSApi.new
result = api.dns_historical("example.com", "value")
puts result
