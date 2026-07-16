# Runnable example: Subdomains Weekly (GET /v3.2/download/dbupdate/weekly/subdomains)
# Parameters for dbSubdomainsWeekly (GET /v3.2/download/dbupdate/weekly/subdomains):
#   - date (string, optional): yyyy-MM-dd; omit for latest
require 'date'
require 'whoisfreaks'

WhoisFreaks.configure do |config|
  config.api_key["apiKey"] = "YOUR_API_KEY"   # set once
end

api = WhoisFreaks::DatabasesSubdomainsApi.new
result = api.db_subdomains_weekly((Date.today - 1).to_s)
puts result
