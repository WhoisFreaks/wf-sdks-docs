# Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
# Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
#   - apiKey (string, required): Your WHOISFreaks API key
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
data, status, _headers = api.db_newly_dns_with_http_info("YOUR_API_KEY", (Date.today - 1).to_s)
puts "status: #{status}"
puts data
