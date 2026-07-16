# Runnable example: Subdomains Monthly (GET /v3.2/download/dbupdate/monthly/subdomains)
# Parameters for dbSubdomainsMonthly (GET /v3.2/download/dbupdate/monthly/subdomains):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesSubdomainsApi.new
result = api.db_subdomains_monthly((Date.today - 1).to_s)
puts result
