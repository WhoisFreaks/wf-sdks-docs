# Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
# Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesDNSApi.new
result = api.db_dns_weekly((Date.today - 1).to_s)
puts result
