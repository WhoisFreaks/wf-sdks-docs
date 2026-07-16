# Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
# Parameters for asnWhois (GET /v2.0/asn-whois):
#   - asn (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::ASNWHOISApi.new
result = api.asn_whois("AS15169")
puts result
