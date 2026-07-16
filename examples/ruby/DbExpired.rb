# Runnable example: Expiring Domains (GET /v3.1/download/domainer/expired)
# Parameters for dbExpired (GET /v3.1/download/domainer/expired):
#   - whois (boolean, required)
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
result = api.db_expired(false, (Date.today - 1).to_s)
puts result
