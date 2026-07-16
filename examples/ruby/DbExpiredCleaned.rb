# Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
# Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
result = api.db_expired_cleaned((Date.today - 1).to_s)
puts result
