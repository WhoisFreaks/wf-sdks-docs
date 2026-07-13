# Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
# Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPWHOISApi.new
data, status, _headers = api.db_ip_whois_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data
