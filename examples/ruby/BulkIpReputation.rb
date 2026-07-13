# Runnable example: Bulk IP Reputation (POST /v1.0/security)
# Parameters for bulkIpReputation (POST /v1.0/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - body: BulkGeolocationRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::IPReputationApi.new
data, status, _headers = api.bulk_ip_reputation_with_http_info(api_key: "YOUR_API_KEY", bulk_geolocation_request: WhoisFreaks::BulkGeolocationRequest.new)
puts "status: #{status}"
puts data
