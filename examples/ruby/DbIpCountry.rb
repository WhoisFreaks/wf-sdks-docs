# Runnable example: IP to Country Snapshot (GET /v3.3/download/snapshot/ip/country)
# Parameters for dbIpCountry (GET /v3.3/download/snapshot/ip/country):
#   - date (string, required)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesIPGeolocationApi.new
result = api.db_ip_country((Date.today - 1).to_s)
puts result
