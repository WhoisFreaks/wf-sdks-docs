# Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
# Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
result = api.db_dropped(false, (Date.today - 1).to_s)
puts result
