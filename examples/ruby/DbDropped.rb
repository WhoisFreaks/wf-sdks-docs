# Runnable example: Dropped Domains (GET /v3.1/download/domainer/dropped)
# Parameters for dbDropped (GET /v3.1/download/domainer/dropped):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
data, status, _headers = api.db_dropped_with_http_info(api_key: "YOUR_API_KEY", whois: false, date: (Date.today - 1).to_s)
puts "status: #{status}"
puts data
