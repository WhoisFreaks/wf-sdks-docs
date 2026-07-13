# Runnable example: IP Reputation Lookup (GET /v1.0/security)
# Parameters for ipReputation (GET /v1.0/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
require 'whoisfreaks'

api = WhoisFreaks::IPReputationApi.new
data, status, _headers = api.ip_reputation_with_http_info(api_key: "YOUR_API_KEY", ip: "8.8.8.8")
puts "status: #{status}"
puts data
