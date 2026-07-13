# Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
# Parameters for subdomains (GET /v1.0/subdomains):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - domain (string, required)
#   - after (string, optional)
#   - before (string, optional)
#   - status (string (one of: active, inactive), optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::SubdomainsApi.new
data, status, _headers = api.subdomains_with_http_info("YOUR_API_KEY", "example.com", "2000-01-01", Date.today.to_s)
puts "status: #{status}"
puts data
