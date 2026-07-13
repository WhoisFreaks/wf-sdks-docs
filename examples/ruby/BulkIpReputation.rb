# Runnable example: Bulk IP Reputation (POST /v1.0/security)
# Parameters for bulkIpReputation (POST /v1.0/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - body: BulkGeolocationRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::IPReputationApi.new
data, status, _headers = api.bulk_ip_reputation_with_http_info("YOUR_API_KEY", WhoisFreaks::BulkGeolocationRequest.new)
puts "status: #{status}"
puts data
