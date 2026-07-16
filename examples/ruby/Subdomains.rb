# Runnable example: Subdomains Lookup (GET /v1.0/subdomains)
# Parameters for subdomains (GET /v1.0/subdomains):
#   - domain (string, required)
#   - after (string, optional)
#   - before (string, optional)
#   - status (string (one of: active, inactive), optional)
#   - page (integer, optional)
#   - format (string (one of: json, xml), optional)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::SubdomainsApi.new
result = api.subdomains("example.com", "2000-01-01", Date.today.to_s)
puts result
