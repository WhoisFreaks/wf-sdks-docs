# Runnable example: Newly Registered With DNS (GET /v3.1/download/domainer/newly/dns)
# Parameters for dbNewlyDns (GET /v3.1/download/domainer/newly/dns):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesNewlyRegisteredApi.new
result = api.db_newly_dns((Date.today - 1).to_s)
puts result
