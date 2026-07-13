# Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
# Parameters for bulkGeolocation (POST /v1.0/geolocation):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - body: BulkGeolocationRequest (required) -- request body object
require 'whoisfreaks'

api = WhoisFreaks::GeolocationApi.new
data, status, _headers = api.bulk_geolocation_with_http_info(api_key: "YOUR_API_KEY", bulk_geolocation_request: WhoisFreaks::BulkGeolocationRequest.new)
puts "status: #{status}"
puts data
