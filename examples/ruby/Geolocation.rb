# Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
# Parameters for geolocation (GET /v1.0/geolocation):
#   - ip (string, required)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::GeolocationApi.new
result = api.geolocation("8.8.8.8")
puts result
