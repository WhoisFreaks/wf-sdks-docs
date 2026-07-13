# Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
# Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPGeolocationApi.new
data, status, _headers = api.db_ip_city_status_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data
