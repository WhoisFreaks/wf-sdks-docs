# Runnable example: WHOIS Database Monthly (GET /v3.3/download/dbupdate/monthly/domains/whois)
# Parameters for dbWhoisMonthly (GET /v3.3/download/dbupdate/monthly/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesWHOISApi.new
result = api.db_whois_monthly((Date.today - 1).to_s)
puts result
