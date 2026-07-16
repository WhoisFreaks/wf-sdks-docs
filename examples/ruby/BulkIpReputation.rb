# Runnable example: Bulk IP Reputation (POST /v1.0/security)
# Parameters for bulkIpReputation (POST /v1.0/security):
#   - body: BulkIpReputationRequest (required) -- request body object
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::IPReputationApi.new
result = api.bulk_ip_reputation(WhoisFreaks::BulkIpReputationRequest.new)
puts result
