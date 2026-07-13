# Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
# Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPGeolocationApi.new
data, status, _headers = api.db_ip_city_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data
