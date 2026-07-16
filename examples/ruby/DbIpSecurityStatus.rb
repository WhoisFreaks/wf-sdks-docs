# Runnable example: IP Security Snapshot Status (GET /v3.3/status/snapshot/ip/security)
# Parameters for dbIpSecurityStatus (GET /v3.3/status/snapshot/ip/security):
#   (no parameters; the API key is set on the client)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesIPSecurityApi.new
result = api.db_ip_security_status()
puts result
