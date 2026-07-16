# Runnable example: Bulk IP Geolocation (POST /v1.0/geolocation)
# Parameters for bulkGeolocation (POST /v1.0/geolocation):
#   - body: BulkGeolocationRequest (required) -- request body object
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::GeolocationApi.new
result = api.bulk_geolocation(WhoisFreaks::BulkGeolocationRequest.new)
puts result
