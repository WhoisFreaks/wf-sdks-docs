# Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
# Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
result = api.db_dropped_json((Date.today - 1).to_s)
puts result
