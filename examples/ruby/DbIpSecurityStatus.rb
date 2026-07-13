# Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
# Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
#   - apiKey (string, required): Your WHOISFreaks API key
require 'whoisfreaks'

api = WhoisFreaks::DatabasesIPSecurityApi.new
data, status, _headers = api.db_ip_security_status_with_http_info("YOUR_API_KEY")
puts "status: #{status}"
puts data
