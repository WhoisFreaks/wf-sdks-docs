# Runnable example: Dropped With Backlinks (GET /v3.3/download/domainer/dropped/backlinks)
# Parameters for dbDroppedBacklinks (GET /v3.3/download/domainer/dropped/backlinks):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, optional)
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
data, status, _headers = api.db_dropped_backlinks_with_http_info(api_key: "YOUR_API_KEY", whois: false, date: (Date.today - 1).to_s)
puts "status: #{status}"
puts data
