# Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
# Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPGeolocationApi.new
data, status, _headers = api.db_ip_country_status_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data
