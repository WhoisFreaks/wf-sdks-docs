# Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
# Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
#   - whois (boolean, optional)
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
result = api.db_dropped_backlinks(false, (Date.today - 1).to_s)
puts result
