# Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
# Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesDNSApi.new
result = api.db_dns_monthly((Date.today - 1).to_s)
puts result
