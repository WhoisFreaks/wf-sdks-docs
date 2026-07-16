# Runnable example: IP WHOIS Lookup (GET /v1.0/ip-whois)
# Parameters for ipWhois (GET /v1.0/ip-whois):
#   - ip (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::IPWHOISApi.new
result = api.ip_whois("8.8.8.8")
puts result
