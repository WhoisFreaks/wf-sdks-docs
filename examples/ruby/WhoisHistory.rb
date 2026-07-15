# Runnable example: Historical WHOIS records for a domain (GET /v2.0/whois/history)
# Parameters for whoisHistory (GET /v2.0/whois/history):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domainName (string, required): Domain to fetch historical WHOIS records for
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.whois_history_with_http_info("YOUR_API_KEY", "example.com")
puts "status: #{status}"
puts data
