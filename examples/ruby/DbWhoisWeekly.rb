# Runnable example: WHOIS Database Weekly (GET /v3.3/download/dbupdate/weekly/domains/whois)
# Parameters for dbWhoisWeekly (GET /v3.3/download/dbupdate/weekly/domains/whois):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesWHOISApi.new
result = api.db_whois_weekly((Date.today - 1).to_s)
puts result
