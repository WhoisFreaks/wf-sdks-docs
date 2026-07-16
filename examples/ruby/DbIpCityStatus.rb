# Runnable example: IP to City Snapshot Status (GET /v3.3/status/snapshot/ip/city)
# Parameters for dbIpCityStatus (GET /v3.3/status/snapshot/ip/city):
#   (no parameters; the API key is set on the client)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesIPGeolocationApi.new
result = api.db_ip_city_status()
puts result
