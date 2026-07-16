# Runnable example: IP to City Snapshot (GET /v3.3/download/snapshot/ip/city)
# Parameters for dbIpCity (GET /v3.3/download/snapshot/ip/city):
#   - date (string, required)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesIPGeolocationApi.new
result = api.db_ip_city((Date.today - 1).to_s)
puts result
