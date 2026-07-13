# Runnable example: ASN WHOIS Lookup (GET /v2.0/asn-whois)
# Parameters for asnWhois (GET /v2.0/asn-whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - asn (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::ASNWHOISApi.new
data, status, _headers = api.asn_whois_with_http_info(api_key: "YOUR_API_KEY", asn: "AS15169")
puts "status: #{status}"
puts data
