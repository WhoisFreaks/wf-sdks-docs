# Runnable example: IP Reputation Lookup (GET /v1.0/security)
# Parameters for ipReputation (GET /v1.0/security):
#   - ip (string, required)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::IPReputationApi.new
result = api.ip_reputation("8.8.8.8")
puts result
