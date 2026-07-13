# Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
# Parameters for dbExpired (GET /v3.1/download/domainer/expired):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
data, status, _headers = api.db_expired_with_http_info("YOUR_API_KEY", false, (Date.today - 1).to_s)
puts "status: #{status}"
puts data
