# Runnable example: Expiring Cleaned WHOIS (GET /v3.1/download/domainer/expired/cleaned)
# Parameters for dbExpiredCleaned (GET /v3.1/download/domainer/expired/cleaned):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesExpiringDroppedApi.new
data, status, _headers = api.db_expired_cleaned_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data
