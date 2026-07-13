# Runnable example: DNS Database Weekly (GET /v3.2/download/dbupdate/weekly/dns)
# Parameters for dbDnsWeekly (GET /v3.2/download/dbupdate/weekly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesDNSApi.new
data, status, _headers = api.db_dns_weekly_with_http_info(api_key: "YOUR_API_KEY", date: (Date.today - 1).to_s)
puts "status: #{status}"
puts data
