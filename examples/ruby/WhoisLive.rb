# Runnable example: Live WHOIS Lookup (GET /v2.0/whois/live)
# Parameters for whoisLive (GET /v2.0/whois/live):
#   - domainName (string, required)
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::WHOISApi.new
result = api.whois_live("example.com")
puts result
