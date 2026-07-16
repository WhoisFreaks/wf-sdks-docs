# Runnable example: IP WHOIS Snapshot (GET /v3.3/download/snapshot/ip/whois)
# Parameters for dbIpWhois (GET /v3.3/download/snapshot/ip/whois):
#   - date (string, required)
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesIPWHOISApi.new
result = api.db_ip_whois((Date.today - 1).to_s)
puts result
