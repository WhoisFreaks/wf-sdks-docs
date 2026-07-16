# Runnable example: IP WHOIS Snapshot Status (GET /v3.3/status/snapshot/ip/whois)
# Parameters for dbIpWhoisStatus (GET /v3.3/status/snapshot/ip/whois):
#   (no parameters; the API key is set on the client)
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesIPWHOISApi.new
result = api.db_ip_whois_status()
puts result
