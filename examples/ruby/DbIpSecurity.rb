# Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
# Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, required)
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPSecurityApi.new
data, status, _headers = api.db_ip_security_with_http_info(api_key: "YOUR_API_KEY", date: (Date.today - 1).to_s)
puts "status: #{status}"
puts data
