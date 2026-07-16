# Runnable example: IP to Country Snapshot Status (GET /v3.3/status/snapshot/ip/country)
# Parameters for dbIpCountryStatus (GET /v3.3/status/snapshot/ip/country):
#   (no parameters; the API key is set on the client)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesIPGeolocationApi.new
result = api.db_ip_country_status()
puts result
