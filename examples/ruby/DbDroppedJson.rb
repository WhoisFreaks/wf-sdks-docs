# Runnable example: Dropped Domains (JSON) (GET /v3.1/domains/dropped)
# Parameters for dbDroppedJson (GET /v3.1/domains/dropped):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
#   - tlds (string, optional)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
data, status, _headers = api.db_dropped_json_with_http_info(api_key: "YOUR_API_KEY", date: (Date.today - 1).to_s)
puts "status: #{status}"
puts data
