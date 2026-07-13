# Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
# Parameters for whoisLive (GET /v2.0/whois/live):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.whois_live_with_http_info(api_key: "YOUR_API_KEY", domain_name: "example.com")
puts "status: #{status}"
puts data
