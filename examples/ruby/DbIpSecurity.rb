# Runnable example: IP Security Snapshot (GET /v3.3/download/snapshot/ip/security)
# Parameters for dbIpSecurity (GET /v3.3/download/snapshot/ip/security):
#   - date (string, required)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesIPSecurityApi.new
result = api.db_ip_security((Date.today - 1).to_s)
puts result
