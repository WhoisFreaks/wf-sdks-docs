# Runnable example: Reverse WHOIS lookup by keyword (GET /v2.0/whois/reverse)
# Parameters for whoisReverse (GET /v2.0/whois/reverse):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - keyword (string, required): Keyword to search across WHOIS records
#   - page (integer, optional): Page number
#   - format (string (one of: json, xml), optional)
require 'whoisfreaks'

api = WhoisFreaks::WHOISApi.new
data, status, _headers = api.whois_reverse_with_http_info("YOUR_API_KEY", "value")
puts "status: #{status}"
puts data
