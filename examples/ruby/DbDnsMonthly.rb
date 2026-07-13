# Runnable example: DNS Database Monthly (GET /v3.2/download/dbupdate/monthly/dns)
# Parameters for dbDnsMonthly (GET /v3.2/download/dbupdate/monthly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesDNSApi.new
data, status, _headers = api.db_dns_monthly_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data
