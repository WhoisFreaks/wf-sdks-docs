# Runnable example: DNS Database Daily (GET /v3.2/download/dbupdate/daily/dns)
# Parameters for dbDnsDaily (GET /v3.2/download/dbupdate/daily/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesDNSApi.new
data, status, _headers = api.db_dns_daily_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data
