# Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
# Parameters for ipWhois (GET /v1.0/ip-whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::IPWHOISApi.new
data, status, _headers = api.ip_whois_with_http_info("YOUR_API_KEY", "8.8.8.8")
puts "status: #{status}"
puts data
