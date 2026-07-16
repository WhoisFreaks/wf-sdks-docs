# Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
# Parameters for whoisHistory (GET /v2.0/whois/history):
#   - domainName (string, required): Domain to fetch historical WHOIS records for
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::WHOISApi.new
result = api.whois_history("example.com")
puts result
