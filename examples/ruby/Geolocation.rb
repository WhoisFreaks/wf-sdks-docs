# Runnable example: IP Geolocation Lookup (GET /v1.0/geolocation)
# Parameters for geolocation (GET /v1.0/geolocation):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - ip (string, required)
require 'whoisfreaks'

api = WhoisFreaks::GeolocationApi.new
data, status, _headers = api.geolocation_with_http_info(api_key: "YOUR_API_KEY", ip: "8.8.8.8")
puts "status: #{status}"
puts data
