# Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
# Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPGeolocationApi.new
data, status, _headers = api.db_ip_country_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data
