# Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
# Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPWHOISApi.new
data, status, _headers = api.db_ip_whois_status_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data
