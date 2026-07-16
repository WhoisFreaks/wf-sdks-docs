# Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
# Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesDNSApi.new
result = api.db_dns_daily((Date.today - 1).to_s)
puts result
